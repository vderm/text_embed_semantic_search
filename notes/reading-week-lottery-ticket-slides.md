---
author:
- Vasken Dermardiros
categories: note
date: 2020-05-21 00:00:00-04:00
draft: false
lastmod: 2020-06-19 12:04:56-04:00
tags:
- reading-week
- lottery-ticket
- model-compression
- model-pruning
title: "Reading Week: Winning Lottery Ticket"
---

## <span class="section-num">1</span> Neural Network Compression {#neural-network-compression}

### <span class="section-num">1.1</span> References {#references}

- <sup id="fae309ae7608af7e44eaff924a3e92a8"><a href="#frankle_lottery_2019" title="Frankle \&amp; Carbin, The {Lottery} {Ticket} {Hypothesis}: {Finding} {Sparse}, {Trainable} {Neural} {Networks}, {arXiv:1803.03635 [cs]}, v(), (2019).">frankle_lottery_2019</a></sup>: [[Frankle_LotteryTicketHypothesis_2019]]
- <sup id="3c62a4073469411a37feaf86505d4b66"><a href="#liu_rethinking_2019" title="Liu, Sun, Zhou, Huang \&amp; Darrell, Rethinking the {Value} of {Network} {Pruning}, {arXiv:1810.05270 [cs, stat]}, v(), (2019).">liu_rethinking_2019</a></sup>: [[Liu_RethinkingValueNetwork_2019]] (to read more)
- <https://ai.facebook.com/blog/understanding-the-generalization-of-lottery-tickets-in-neural-networks/>
- <https://towardsdatascience.com/breaking-down-the-lottery-ticket-hypothesis-ca1c053b3e58>
- <https://towardsdatascience.com/how-the-lottery-ticket-hypothesis-is-challenging-everything-we-knew-about-training-neural-networks-e56da4b0da27>
- <https://techxplore.com/news/2020-05-early-bird-energy-deep-neural.html>
- <sup id="09182eaec4c8da4650d3fb417136e0f3"><a href="#morcos_one_2019" title="Morcos, Yu, Paganini \&amp; Tian, One ticket to win them all: generalizing lottery ticket initializations across datasets and optimizers, {arXiv:1906.02773 [cs, stat]}, v(), (2019).">morcos_one_2019</a></sup>
- <sup id="c5a879c8a89c0c1db063f663ea547fca"><a href="#yu_playing_2020" title="Yu, Edunov, Tian \&amp; Morcos, Playing the lottery with rewards and multiple languages: lottery tickets in {RL} and {NLP}, {arXiv:1906.02768 [cs, stat]}, v(), (2020).">yu_playing_2020</a></sup>

### <span class="section-num">1.2</span> Models are Big and Heavy&#x2026; for now {#models-are-big-and-heavy-and-x2026-for-now}

- Slow in inference
- Energy consumption
- Heavy on computational and memory usage; heavy on data retrieval
- NVIDIA announced Ampere architecture: 1/10th train time, 1/20th energy use;
    data-center clients first (AWS, Azure, Google); smaller footprint
  - 54bil transistors, 7nm FinFET process, 40GB HBM2 memory
  - GPU virtualization -> split into 7

![[2020-05-21_08-32-20_pvtNn9LjZZ7P4f3nJVYoX6-970-80.jpg]]

### <span class="section-num">1.3</span> Quantization {#quantization}

Lower Precision: do we need float32? can we use float16? int8? int4?

- Hardware support else no benefits

Weight Sharing (Deep Compression)

- Filters -> look-up tables
- Sparse <- optimized implementation?

![[2020-05-21_08-39-33_screenshot.png]]

### <span class="section-num">1.4</span> Student-Teacher: Knowledge Distillation {#student-teacher-knowledge-distillation}

Train a simpler model to emulate a more complex model. Also used in
interpretable training where the student model is more "white" and can be
trained in a specific input space (_eg._ specific DNA location for disease
identification) or the whole range.

![[2020-05-21_08-43-11_screenshot.png]]

### <span class="section-num">1.5</span> Tensorflow Model Optimization {#tensorflow-model-optimization}

Emulates low-precision with tricks, original work by
<sup id="001c92a7a11815b89568bfe325cb399a"><a href="#jacob_quantization_2017" title="Jacob, Kligys, Chen, Zhu, Tang, Howard, Adam \&amp; Kalenichenko, Quantization and {Training} of {Neural} {Networks} for {Efficient} {Integer}-{Arithmetic}-{Only} {Inference}, {arXiv:1712.05877 [cs, stat]}, v(), (2017).">jacob_quantization_2017</a></sup>.

```python
import tensorflow_model_optimization as tfmot

model = tf.keras.Sequential([
   ...
])
# Quantize the entire model.
quantized = tfmot.quantization.keras.quantize_model(model)

# Continue with training as usual.
quantized_model.compile(...)
quantized_model.fit(...)
```

### <span class="section-num">1.6</span> Pruning {#pruning}

- Not all weights are useful
- For CNNs, most weights are at the end where it's mostly full-connected (FC)
- Weights near input could be more sensitive towards output since the modified
    features are carried forward -> drop weights via importance not uniformly ->
    how can you tell?
- Pruning is typically a 3 stage pipeline: training (a large model), pruning and
    fine-tuning. During pruning, redundant weights are pruned and important
    weights are kept. <sup id="3c62a4073469411a37feaf86505d4b66"><a href="#liu_rethinking_2019" title="Liu, Sun, Zhou, Huang \&amp; Darrell, Rethinking the {Value} of {Network} {Pruning}, {arXiv:1810.05270 [cs, stat]}, v(), (2019).">liu_rethinking_2019</a></sup>

![[2020-05-21_08-46-07_screenshot.png]]

## <span class="section-num">2</span> Winning Lottery Ticket {#winning-lottery-ticket}

### <span class="section-num">2.1</span> Winning Lottery Ticket {#winning-lottery-ticket}

Paper by <sup id="fae309ae7608af7e44eaff924a3e92a8"><a href="#frankle_lottery_2019" title="Frankle \&amp; Carbin, The {Lottery} {Ticket} {Hypothesis}: {Finding} {Sparse}, {Trainable} {Neural} {Networks}, {arXiv:1803.03635 [cs]}, v(), (2019).">frankle_lottery_2019</a></sup> which got a lot of people rethinking what ML
training really is. Also see [1](https://towardsdatascience.com/how-the-lottery-ticket-hypothesis-is-challenging-everything-we-knew-about-training-neural-networks-e56da4b0da27) and [2](https://towardsdatascience.com/breaking-down-the-lottery-ticket-hypothesis-ca1c053b3e58).

**Why should we care?** Less weights = smaller memory footprint, can also be much
faster in inference.

**What is it about?** Determining a network architecture that has 90% less weights
than the original one while retaining the same accuracy. Winning tickets learn
faster than the original network and reach higher test accuracy. Previous works
about iterative pruning claim its hard to train sparse network from the
beginning; that's why it's an iterative pruning method; doesn't apply here.

**What did I like?** Method much more straightforward compared to
reduced-precision methods.

**What did I dislike?** Not very clear how to apply to CNN models; pruning method
seems haphazard.

### <span class="section-num">2.2</span> The Lottery Ticket Hypothesis {#the-lottery-ticket-hypothesis}

A randomly-initialized, dense neural network contains a subnetwork that is
initialized such that &#x2013; when trained in isolation &#x2013; it can match the test
accuracy of the original network after training for at most the same number of
iterations.

### <span class="section-num">2.3</span> Pruning without maintaining weights {#pruning-without-maintaining-weights}

Typically the weights of the pruned model are re-initialized.

![[2020-05-21_15-19-26_screenshot.png]]

### <span class="section-num">2.4</span> Pruning with maintaining weights: proposed method {#pruning-with-maintaining-weights-proposed-method}

In this article, they argue that the "winning ticket" is both the structure and
the initial weights.

![[2020-05-21_15-15-23_screenshot.png]]

### <span class="section-num">2.5</span> Identifying the winning tickets {#identifying-the-winning-tickets}

1. Randomly initialize a neural network \\(f(x; \theta\_0)\\) (where \\(\theta\_0 \sim
       \mathcal{D}\_\theta\\)).
2. Train the network for \\(j\\) iterations, arriving at parameters \\(\theta\_j\\).
3. Prune \\(p\%\\) of the parameters in \\(\theta\_j\\), creating a mask \\(m\\).
4. Reset the remaining parameters to their values in \\(\theta\_0\\), creating the
    winning ticket \\(f(x; m \odot \theta\_0)\\).

Pruning approach is **one-shot**: the network is trained once, \\(p\%\\) of weights
are pruned, and the surviving weights are reset.

Comment for step 4: how is the mask really applied? setting certain weights with
a mask to zero may not result in improved computation time.

### <span class="section-num">2.6</span> Does that make sense? {#does-that-make-sense}

- Is there some sort of proof for this?
- Are we really exploring a local minima?
- Why would the initial weights matter when we have interconnected layers?

### <span class="section-num">2.7</span> Extensions of work {#extensions-of-work}

FB AI Research: [Understanding the generalization of lottery tickets in neural
networks](https://ai.facebook.com/blog/understanding-the-generalization-of-lottery-tickets-in-neural-/networks/)

Has also been applied to RL in the paper "One ticket to win them all:
generalizing lottery ticket initializations across datasets and optimizers" by
<sup id="09182eaec4c8da4650d3fb417136e0f3"><a href="#morcos_one_2019" title="Morcos, Yu, Paganini \&amp; Tian, One ticket to win them all: generalizing lottery ticket initializations across datasets and optimizers, {arXiv:1906.02773 [cs, stat]}, v(), (2019).">morcos_one_2019</a></sup>.

## <span class="section-num">3</span> Another view {#another-view}

### <span class="section-num">3.1</span> Not everyone agrees sees rosy {#not-everyone-agrees-sees-rosy}

In the "Rethinking the Value of Network Pruning" paper by
<sup id="3c62a4073469411a37feaf86505d4b66"><a href="#liu_rethinking_2019" title="Liu, Sun, Zhou, Huang \&amp; Darrell, Rethinking the {Value} of {Network} {Pruning}, {arXiv:1810.05270 [cs, stat]}, v(), (2019).">liu_rethinking_2019</a></sup>, they observe that:

1. training a large, over-parameterized model is often not necessary to obtain
    an efficient final model
2. learned “important” weights of the large model are typically not useful for
    the small pruned model, and
3. the pruned architecture itself, rather than a set of inherited “important”
    weights, is more crucial to the efficiency in the final model, which suggests
    that in some cases pruning can be useful as an architecture search paradigm.

Sparse large networks > dense small networks regardless of initialization
because structure is most important.

Unstructured pruning limitation is that resulting weight matrices are sparse,
which cannot lead to compression and speedup without dedicated
hardware/libraries.

### <span class="section-num">3.2</span> Early Bird {#early-bird}

Early Bird uses 10 times less energy to train deep neural networks: [TechXplot
article](https://techxplore.com/news/2020-05-early-bird-energy-deep-neural.html), [ICLR 2020 submission](https://iclr.cc/virtual%5F2020/poster%5FBJxsrgStvr.html) and [paper](https://openreview.net/pdf?id=BJxsrgStvr).

_To review_: barely start training a large model and quickly identify "the
winning ticket". No need to train a giant network.

Idea is to make AI/ML more green.

## <span class="section-num">4</span> References {#references}

### <span class="section-num">4.1</span> References {#references}

# Bibliography

<a id="frankle_lottery_2019"></a>[frankle_lottery_2019] Frankle & Carbin, The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks, <i>arXiv:1803.03635 [cs]</i>,  (2019). <a href="http://arxiv.org/abs/1803.03635">link</a>. [↩](#fae309ae7608af7e44eaff924a3e92a8)

<a id="liu_rethinking_2019"></a>[liu_rethinking_2019] Liu, Sun, Zhou, Huang & Darrell, Rethinking the Value of Network Pruning, <i>arXiv:1810.05270 [cs, stat]</i>,  (2019). <a href="http://arxiv.org/abs/1810.05270">link</a>. [↩](#3c62a4073469411a37feaf86505d4b66)

<a id="morcos_one_2019"></a>[morcos_one_2019] Morcos, Yu, Paganini & Tian, One ticket to win them all: generalizing lottery ticket initializations across datasets and optimizers, <i>arXiv:1906.02773 [cs, stat]</i>,  (2019). <a href="http://arxiv.org/abs/1906.02773">link</a>. [↩](#09182eaec4c8da4650d3fb417136e0f3)

<a id="yu_playing_2020"></a>[yu_playing_2020] Yu, Edunov, Tian & Morcos, Playing the lottery with rewards and multiple languages: lottery tickets in RL and NLP, <i>arXiv:1906.02768 [cs, stat]</i>,  (2020). <a href="http://arxiv.org/abs/1906.02768">link</a>. [↩](#c5a879c8a89c0c1db063f663ea547fca)

<a id="jacob_quantization_2017"></a>[jacob_quantization_2017] Jacob, Kligys, Chen, Zhu, Tang, Howard, Adam & Kalenichenko, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference, <i>arXiv:1712.05877 [cs, stat]</i>,  (2017). <a href="http://arxiv.org/abs/1712.05877">link</a>. [↩](#001c92a7a11815b89568bfe325cb399a)

[//begin]: # "Autogenerated link references for markdown compatibility"
[Frankle_LotteryTicketHypothesis_2019]: ../articles/Frankle_LotteryTicketHypothesis_2019.md "Frankle_LotteryTicketHypothesis_2019: The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
[Liu_RethinkingValueNetwork_2019]: ../articles/Liu_RethinkingValueNetwork_2019.md "Liu_RethinkingValueNetwork_2019: Rethinking the Value of Network Pruning"
[[2020-05-21_08-32-20_pvtNn9LjZZ7P4f3nJVYoX6-970-80.jpg]: ../attachments/Big_Picture_Idea/2020-05-21_08-32-20_pvtNn9LjZZ7P4f3nJVYoX6-970-80.jpg "2020-05-21_08-32-20_pvtNn9LjZZ7P4f3nJVYoX6-970-80.jpg"
[[2020-05-21_08-39-33_screenshot.png]: ../attachments/Big_Picture_Idea/2020-05-21_08-39-33_screenshot.png "2020-05-21_08-39-33_screenshot.png"
[[2020-05-21_08-43-11_screenshot.png]: ../attachments/Big_Picture_Idea/2020-05-21_08-43-11_screenshot.png "2020-05-21_08-43-11_screenshot.png"
[[2020-05-21_08-46-07_screenshot.png]: ../attachments/Big_Picture_Idea/2020-05-21_08-46-07_screenshot.png "2020-05-21_08-46-07_screenshot.png"
[[2020-05-21_15-19-26_screenshot.png]: ../attachments/Winning_Lottery_Ticket/2020-05-21_15-19-26_screenshot.png "2020-05-21_15-19-26_screenshot.png"
[[2020-05-21_15-15-23_screenshot.png]: ../attachments/Winning_Lottery_Ticket/2020-05-21_15-15-23_screenshot.png "2020-05-21_15-15-23_screenshot.png"
[//end]: # "Autogenerated link references"