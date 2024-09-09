from setuptools import find_packages, setup

setup(
    name="grok",
    packages=find_packages(),
    version="0.0.1",
    install_requires=[
        "torch==1.13.1",
        "pytorch_lightning==1.5.0",
        "torchmetrics==0.11.4",
        "numpy==1.21.6",
        "blobfile",
        "tqdm",
        "scipy",
        "mod",
        "matplotlib",
        "sympy"
    ],
)
