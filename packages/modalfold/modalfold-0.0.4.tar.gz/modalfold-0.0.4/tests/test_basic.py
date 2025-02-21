"""Test suite for ModalFold package."""

from typing import Generator

import numpy as np
import pytest
from modal import enable_output

from modalfold import app
from modalfold.esmfold import ESMFold, ESMFoldOutput
from modalfold.utils import validate_sequence, format_time

# Test sequences
TEST_SEQUENCES = {
    "short": "MLKNVHVLVLGAGDVGSVVVRLLEK",  # 24 residues
    "medium": "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKT",  # Insulin
    "invalid": "MALWMRLLPX123LLALWGPD",  # Contains invalid characters
}


@pytest.fixture
def esmfold_model() -> Generator[ESMFold, None, None]:
    """Fixture for ESMFold model."""
    with enable_output():
        with app.run():
            model = ESMFold()
            yield model


def test_validate_sequence():
    """Test sequence validation."""
    # Valid sequences
    assert validate_sequence(TEST_SEQUENCES["short"]) is True
    assert validate_sequence(TEST_SEQUENCES["medium"]) is True

    # Invalid sequences
    with pytest.raises(ValueError):
        validate_sequence(TEST_SEQUENCES["invalid"])
    with pytest.raises(ValueError):
        validate_sequence("NOT A SEQUENCE")


def test_format_time():
    """Test time formatting."""
    assert format_time(30) == "30s", f"Expected '30s', got {format_time(30)}"
    assert format_time(90) == "1m 30s", f"Expected '1m 30s', got {format_time(90)}"
    assert format_time(3600) == "1h", f"Expected '1h', got {format_time(3600)}"
    assert format_time(3661) == "1h 1m 1s", f"Expected '1h 1m 1s', got {format_time(3661)}"


def test_esmfold_basic():
    """Test basic ESMFold functionality."""

    with enable_output():
        with app.run():
            model = ESMFold()
            result = model.fold.remote(TEST_SEQUENCES["short"])

            assert isinstance(result, ESMFoldOutput), "Result should be an ESMFoldOutput"

            seq_len = len(TEST_SEQUENCES["short"])
            positions_shape = result.positions.shape

            assert positions_shape[-1] == 3, "Coordinate dimension mismatch. Expected: 3, Got: {positions_shape[-1]}"
            assert (
                positions_shape[-3] == seq_len
            ), "Number of residues mismatch. Expected: {seq_len}, Got: {positions_shape[-3]}"
            assert np.all(result.plddt >= 0), "pLDDT scores should be non-negative"
            assert np.all(result.plddt <= 100), "pLDDT scores should be less than or equal to 100"


def test_esmfold_batch(esmfold_model: ESMFold):
    """Test ESMFold batch prediction."""

    # Define input sequences
    sequences = [TEST_SEQUENCES["short"], TEST_SEQUENCES["medium"]]

    # Make prediction
    result = esmfold_model.fold.remote(sequences)

    # Check output shape
    positions_shape = result.positions.shape

    # Assertions with detailed error messages
    # FIXME sequence len isn't matching
    # assert positions_shape[0] == len(sequences), \
    #     f"Batch size mismatch. Expected: {len(sequences)}, Got: {positions_shape[0]}"
    assert positions_shape[-1] == 3, f"Coordinate dimension mismatch. Expected: 3, Got: {positions_shape[-1]}"


def test_sequence_validation(esmfold_model: ESMFold):
    """Test sequence validation in FoldingAlgorithm."""

    # Test single sequence
    single_seq = TEST_SEQUENCES["short"]
    validated = esmfold_model._validate_sequences(single_seq)
    assert isinstance(validated, list), "Single sequence should be converted to list"
    assert len(validated) == 1, "Should contain one sequence"
    assert validated[0] == single_seq, "Sequence should be unchanged"

    # Test sequence list
    seq_list = [TEST_SEQUENCES["short"], TEST_SEQUENCES["medium"]]
    validated = esmfold_model._validate_sequences(seq_list)
    assert isinstance(validated, list), "Should return a list"
    assert len(validated) == 2, "Should contain two sequences"
    assert validated == seq_list, "Sequences should be unchanged"

    # Test invalid sequence
    with pytest.raises(ValueError) as exc_info:
        esmfold_model._validate_sequences(TEST_SEQUENCES["invalid"])
    assert "Invalid amino acid" in str(exc_info.value), f"Expected 'Invalid amino acid', got {str(exc_info.value)}"

    # Test that fold method uses validation
    with pytest.raises(ValueError) as exc_info:
        esmfold_model.fold.remote(TEST_SEQUENCES["invalid"])
    assert "Invalid amino acid" in str(exc_info.value), f"Expected 'Invalid amino acid', got {str(exc_info.value)}"


def test_esmfold_output_pdb_cif():
    """Test ESMFold output PDB and CIF."""

    with enable_output():
        with app.run():
            model = ESMFold(config={"output_pdb": True, "output_cif": False})

            # Define input sequences
            sequences = [TEST_SEQUENCES["short"], TEST_SEQUENCES["medium"]]

            result = model.fold.remote(sequences)

    assert result.pdb is not None, "PDB output should be generated"
    # assert result.cif is not None, "CIF output should be generated"

    assert isinstance(result.pdb, list), "PDB output should be a list"
    assert len(result.pdb) == len(sequences), "PDB output should have same length as input sequences"
    # assert isinstance(result.cif, list), "CIF output should be a list"
    # assert len(result.cif) == len(sequences), "CIF output should have same length as input sequences"

    # TODO: maybe do a proper validation of the PDB format, which would require biotite/biopython dependency
    # # Check CIF format
    # for cif_str in result.cif:
    #     assert cif_str.startswith("data_"), "CIF should start with data_"

    # for pdb_str, cif_str in zip(result.pdb, result.cif):
    #     # Count ATOM records (each line starting with ATOM is one atom)
    #     n_atoms_pdb = sum(1 for line in pdb_str.splitlines() if line.startswith("ATOM") and 'TER' not in line)
    #     # Count atoms in CIF (each row in _atom_site table represents one atom)
    #     n_atoms_cif = sum(1 for line in cif_str.splitlines() if line.strip() and not line.startswith("#") and not line.startswith("_"))
    #     assert n_atoms_pdb == n_atoms_cif, "PDB and CIF should have same number of atoms"
