<img src="./fig4.png" width="400px"></img>

## Deep Cross Attention

Implementation of the proposed [DeepCrossAttention](https://arxiv.org/abs/2502.06785) by [Mike Heddes](https://www.mikeheddes.nl/) while at Google research, in Pytorch

My analysis is although I still prefer [Hyper Connections](https://arxiv.org/abs/2409.19606), they have an important idea here that I have been trying concurrently. Mainly the queries, keys, values can be [routed from different layers](https://github.com/lucidrains/x-transformers/blob/main/x_transformers/x_transformers.py#L1226) of the past

## Install

```bash
$ pip install deep-cross-attention
```

## Usage

```python
import torch
from deep_cross_attention import DCAGPT

gpt = DCAGPT(
    num_tokens = 256,
    dim = 512,
    depth = 6,
    heads = 8,
    dim_head = 64,
    past_layers_k = 2
)

ids = torch.randint(0, 256, (2, 4096))

logits = gpt(ids) # (2, 4096, 256)
```

## Example

First

```bash
$ pip install .[examples]
```

Next

```bash
$ python train.py
```

## Citations

```bibtex
@inproceedings{Heddes2025DeepCrossAttentionST,
    title   = {DeepCrossAttention: Supercharging Transformer Residual Connections},
    author  = {Mike Heddes and Adel Javanmard and Kyriakos Axiotis and Gang Fu and MohammadHossein Bateni and Vahab S. Mirrokni},
    year    = {2025},
    url     = {https://api.semanticscholar.org/CorpusID:276250576}
}
```
