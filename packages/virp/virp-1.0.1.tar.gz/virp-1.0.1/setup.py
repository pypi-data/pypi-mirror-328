from setuptools import setup, find_packages

setup(
    name="virp",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pymatgen",
        "chgnet",
        "matgl==1.0.1",
        "dgl",
        "poshcar"
    ],
)
