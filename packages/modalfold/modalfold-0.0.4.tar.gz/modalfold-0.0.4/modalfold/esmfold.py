"""ESMFold implementation for protein structure prediction using Meta AI's ESM-2 model."""

import logging
from dataclasses import dataclass
from typing import Union, Sequence, Optional

import modal
import numpy as np

from . import app
from .base import FoldingAlgorithm, StructurePrediction, PredictionMetadata
from .images.esmfold import esmfold_image
from .images.volumes import model_weights
from .utils import MINUTES, MODEL_DIR
from .utils import Timer

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)


@dataclass
class ESMFoldOutput(StructurePrediction):
    """Output from ESMFold prediction including all model outputs."""

    # Required by StructurePrediction protocol
    positions: np.ndarray
    metadata: PredictionMetadata

    # Additional ESMFold-specific outputs
    frames: np.ndarray
    sidechain_frames: np.ndarray
    unnormalized_angles: np.ndarray
    angles: np.ndarray
    states: np.ndarray
    s_s: np.ndarray
    s_z: np.ndarray
    distogram_logits: np.ndarray
    lm_logits: np.ndarray
    aatype: np.ndarray
    atom14_atom_exists: np.ndarray
    residx_atom14_to_atom37: np.ndarray
    residx_atom37_to_atom14: np.ndarray
    atom37_atom_exists: np.ndarray
    residue_index: np.ndarray
    lddt_head: np.ndarray
    plddt: np.ndarray
    ptm_logits: np.ndarray
    ptm: np.ndarray
    aligned_confidence_probs: np.ndarray
    predicted_aligned_error: np.ndarray
    max_predicted_aligned_error: np.ndarray
    pdb: Optional[list[str]] = None

    # TODO: can add a save method here (to a pickle and a pdb file) that can be run locally


with esmfold_image.imports():
    import torch
    from transformers import EsmForProteinFolding, AutoTokenizer


@app.cls(
    image=esmfold_image,
    gpu="T4",
    timeout=20 * MINUTES,
    container_idle_timeout=10 * MINUTES,
    volumes={MODEL_DIR: model_weights},
)
class ESMFold(FoldingAlgorithm):
    """ESMFold protein structure prediction model."""

    # We need to properly asses whether using this or the original ESMFold is better
    # based on speed, accuracy, bugs, etc.; as well as customizability
    # For instance, if we want to also allow differently sized structure modules, than this would be good
    # TODO: we should add a settings dictionary or something, that would make it easier to add new options
    # TODO: maybe use OmegaConf instead to make it easier instead of config
    def __init__(self, config: dict = {"output_pdb": False, "output_cif": False}) -> None:
        """Initialize ESMFold."""
        super().__init__()
        self.config = config
        self.tokenizer: Optional[AutoTokenizer] = None
        self.model: Optional[EsmForProteinFolding] = None
        self.metadata = self._initialize_metadata(
            model_name="ESMFold",
            model_version="v4.49.0",  # HuggingFace transformers version
        )

    @modal.enter()
    def _load(self) -> None:
        """Load the ESMFold model and tokenizer."""
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1", cache_dir=MODEL_DIR)
        self.model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", cache_dir=MODEL_DIR)
        self.device = "cuda"
        self.model = self.model.cuda()
        self.model.eval()
        self.model.trunk.set_chunk_size(64)
        self.ready = True

    @modal.method()
    def fold(self, sequences: Union[str, Sequence[str]]) -> ESMFoldOutput:
        """Predict protein structure(s) using ESMFold."""
        if self.tokenizer is None or self.model is None:
            raise RuntimeError("Model not loaded. Call _load() first.")

        # TODO: make sure to the glycine linker thing
        # TODO: check we are doing positional encodings properly
        # TODO: multiple sequences at once likely doesn't work yet!
        sequences = self._validate_sequences(sequences)
        self.metadata.sequence_length = len(sequences)

        tokenized = self.tokenizer(
            sequences, return_tensors="pt", add_special_tokens=False, padding=True, truncation=True, max_length=1024
        )["input_ids"].cuda()

        with Timer("Model Inference") as timer:
            with torch.inference_mode():
                outputs = self.model(tokenized)

        outputs = self._convert_outputs(outputs, timer.duration)
        return outputs

    def _convert_outputs(self, outputs: dict, prediction_time: float) -> ESMFoldOutput:
        """Convert model outputs to ESMFoldOutput format."""
        outputs = {k: v.cpu().numpy() for k, v in outputs.items()}
        self.metadata.prediction_time = prediction_time

        if self.config["output_pdb"]:
            outputs["pdb"] = self._convert_outputs_to_pdb(outputs)
        if self.config["output_cif"]:
            outputs["cif"] = self._convert_outputs_to_cif(outputs)

        return ESMFoldOutput(metadata=self.metadata, **outputs)

    def _convert_outputs_to_pdb(self, outputs: dict) -> list[str]:
        from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
        from transformers.models.esm.openfold_utils.feats import atom14_to_atom37

        final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
        final_atom_mask = outputs["atom37_atom_exists"]
        pdbs = []
        for i in range(outputs["aatype"].shape[0]):
            aa = outputs["aatype"][i]
            pred_pos = final_atom_positions[i]
            mask = final_atom_mask[i]
            resid = outputs["residue_index"][i] + 1
            pred = OFProtein(
                aatype=aa,
                atom_positions=pred_pos,
                atom_mask=mask,
                residue_index=resid,
                b_factors=outputs["plddt"][i],
                chain_index=outputs["chain_index"][i] if "chain_index" in outputs else None,
            )
            pdbs.append(to_pdb(pred))

        return pdbs

    def _convert_outputs_to_cif(self, outputs: dict) -> list[str]:
        raise NotImplementedError("CIF conversion not implemented yet")
        from transformers.models.esm.openfold_utils.protein import to_modelcif, Protein as OFProtein
        from transformers.models.esm.openfold_utils.feats import atom14_to_atom37

        final_atom_positions = atom14_to_atom37(outputs["positions"][-1], outputs)
        final_atom_mask = outputs["atom37_atom_exists"]
        cifs = []
        for i in range(outputs["aatype"].shape[0]):
            aa = outputs["aatype"][i]
            pred_pos = final_atom_positions[i]
            mask = final_atom_mask[i]
            resid = outputs["residue_index"][i] + 1
            pred = OFProtein(
                aatype=aa,
                atom_positions=pred_pos,
                atom_mask=mask,
                residue_index=resid,
                b_factors=outputs["plddt"][i],
                chain_index=outputs["chain_index"][i] if "chain_index" in outputs else None,
            )
            cifs.append(to_modelcif(pred))

        return cifs
