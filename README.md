# OpenAI Grok Curve Experiments

## Paper

This is the code for the paper [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) by Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, and Vedant Misra

## Setup environment

```bash
conda create -n openai_grok python=3.8 -y
conda activate openai_grok
export version="1.5.0"
python3 -m venv lightning_${version}
. ./lightning_${version}/bin/activate

```
Because the conda repositories can't support lower version of pytorch_lightning(lower than 2.0 version), so we must use python3's public pip repositories, in order to do so, we need setup a virtual env  named with lightning_1.5.0

## Installation and Training

Under the openai_grok(Conda), and lightning_1.5.0(python3 venv) environment, we execute the following commands:

```bash
pip install -e .
./scripts/train.py
```
