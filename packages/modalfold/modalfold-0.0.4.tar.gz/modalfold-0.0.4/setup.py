from setuptools import setup, find_packages

setup(
    name="modalfold",
    version="0.0.1",
    packages=find_packages(),
    author="Jakub Lála",
    author_email="jakublala@gmail.com",
    description="A protein structure prediction package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jakublala/modalfold",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="~=3.12",
)
