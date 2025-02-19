# pytoke

**pytoke** is a Python library that calculates fertility and parity scores for text using tokenizers from the [transformers](https://github.com/huggingface/transformers) library. It also provides visualization tools to analyze token metrics across datasets.

## Features

- **Fertility Score:** Calculate the ratio of token count to word count for a given text.
- **Parity Score:** Compare token counts between two texts (e.g., original and translated).
- **TokenMetrics Class:** Easily process and visualize token metrics for a dataset.

## Installation

Install pytoke using pip:

```bash
pip install pytoke
```
## Works Cited

Parity calculation from https://arxiv.org/abs/2305.15425 (page 3).
