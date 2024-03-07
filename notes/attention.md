---
author:
- Vasken Dermardiros
categories: website
draft: false
lastmod: 2021-01-03 22:49:09-05:00
tags:
- attention
- model
- research
- tft
title: Attention-Based Models
---


## Attention is All You Need {#attention-is-all-you-need}

<https://arxiv.org/abs/1706.03762>
<sup id="d91e0cc104a7c55638980581a2868ea4"><a href="#Vaswani_Attentionallyou_2017" title="Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser \&amp; Polosukhin, Attention {{Is All You Need}}, {arXiv:1706.03762 [cs]}, v(), (2017).">Vaswani_Attentionallyou_2017</a></sup>

Original paper on Transformers!


## LSTM is dead. Long Live Transformers! {#lstm-is-dead-dot-long-live-transformers}

author: Leo Dirac

<https://www.youtube.com/watch?v=S27pHKBEp30>

Transformers:

- Created for translation models
- Many attention mechanisms: each can specialize (grammar, vocabulary,
    punctuation, etc.
- Use of cos/sin features of varying frequencies to give model an idea of
    relative location of words/ideas to one another. These features are
    **multiplied** with the input vectors, not added as an extra column!
- Parallelizable -> LSTM needs previous output to calculate the next;
    transformers don't, but although they are in O(n^2), GPUs are highly parallel
    so doing a 10x10 matrix inversion isn't much faster than a 10'000x10'000 one

Some general DL wisdom

- Different activations don't matter
    - Don't bother trying tanh/sigmoid
    - Use ReLU -> strong opinion; above saturate at larger values
- Different optimizers do matter
    - ADAM is fast, but tends to over-fit
    - SGD is slow but gives great results
    - Sometimes RMSProp works best
    - SWA can easily improve quality
    - AdaTune: <https:/github.com/awslabs/adatune>: auto calculates learning rate
        dynamically

Good place to start: <https://github.com/huggingface/transformers>

Re-usable pre-trained models (transfer learning)

- MegatronLM: Massive transformer language model from NVIDIA, 8.3B model
- XLM-RoBERTa: FB trained on 2.5TB of data in 100 languages


## Self-Attention {#self-attention}

<https://github.com/google-research/google-research/tree/master/tft>
<sup id="1dc369642340f0209273395e79981819"><a href="#Lim_TemporalFusionTransformers_2019" title="">Lim_TemporalFusionTransformers_2019</a></sup>