---
author:
- Tim Dettmers
categories: website
draft: false
lastmod: 2021-01-03 22:49:12-05:00
slug: gpu_for_deep_learning
tags:
- research
- programming
- tensorflow
title: GPU for Deep Learning
links:
- https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/
---


Link: <https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/>

Most important spec is getting a GPU with Tensor Cores (parallelization); these
are responsible of multiplying matrices together in one go.

Even if Tensor Cores are very efficient, most of the time they are waiting for
data to arrive. Eg. to train the BERT model, core utilization was 30%. So even
if you have many tensor cores, if memory speed is low, no computation will be
performed. Between A100 and V100, just the memory bandwidth difference will lend
to a 1.73x performance boost.

TPUs have a lot more register memory and so can perform more computation than
GPUs. See [here](https://timdettmers.com/2018/10/17/tpus-vs-gpus-for-transformers-bert/).

Ampere can do [sparse network training](https://arxiv.org/abs/1907.04840), but this is something not really
exploited.

It also has a new low-precision data type (TF32): TF32 can be a drop-in
replacement to FP32 and Brain Float 16 (BF16) can be a replacement for FP16.

Here some rough guidelines for memory:

- Using pretrained transformers; training small transformer from scratch>= 11GB
- Training large transformer or convolutional nets in research / production: >= 24 GB
- Prototyping neural networks (either transformer or convolutional nets) >= 10 GB
- Kaggle competitions >= 8 GB
- Applying computer vision >= 10GB

Typically, very large models or research on such models will need >= 11 GB of
memory. Also, working with very large images (medical) will need lots of memory.

Suppose I would lead a research lab/startup. I would put 66-80% of my budget in
RTX 3080 machines and 20-33% for “rollout” RTX 3090 machines with a robust water
cooling setup. The idea is, RTX 3080 is much more cost-effective and can be
shared via a slurm cluster setup as prototyping machines. Since prototyping
should be done in an agile way, it should be done with smaller models and
smaller datasets. RTX 3080 is perfect for this. Once students/colleagues have a
great prototype model, they can rollout the prototype on the RTX 3090 machines
and scale to larger models.