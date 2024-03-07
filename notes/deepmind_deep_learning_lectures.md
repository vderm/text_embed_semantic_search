---
author:
- Alex Graves
categories: note
draft: false
lastmod: 2020-12-24 09:01:31-05:00
slug: deepmind_deep_learning_lectures
tags:
- research
- attention
- deepmind
- lecture
title: DeepMind Deep Learning Lectures
links:
- https://www.youtube.com/playlist?list=PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF
---


Playlist: <https://www.youtube.com/playlist?list=PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF>

## What is intelligence? {#what-is-intelligence}

{{< figure src="images/what is intelligence.PNG]]

## <span class="org-todo todo TODO">TODO</span> Clean up / Follow up from notes for lectures 1-7 {#clean-up-follow-up-from-notes-for-lectures-1-7}

<https://arxiv.org/pdf/1402.1869.pdf>

The Nature of Statistical Learning Theory
Authors: Vapnik, Vladimir
<https://www.springer.com/gp/book/9780387987804>

Belkin
Reconciling modern machine-learning practice and the classical bias-variance trade-off (2019)

- paper about overfitting then back to better performance

also see
Nakkiran
Deep double descent: where bigger models and more data hurt (2019)
1912.02292

start with few data and overfit
monitor training loss
add shape asserts everywhere -> multiply 2 vectors -> vector or matrix?

Siddhant (2019)
Multiplicative interactions and where to find them

## DeepMind x UCL | Deep Learning Lectures | 8/12 | Attention and Memory in Deep Learning {#deepmind-x-ucl-deep-learning-lectures-8-12-attention-and-memory-in-deep-learning}

Link: <https://youtu.be/AIiwuClvH6k>

Attention is more about ignoring things to be able to focus on specific parts.

### Implicit Attention {#implicit-attention}

Normal NN have an _implicit attention_: we can visualize this using the Jacobian
of the net, and it really depends on the cost or the end purpose. He shows the
example of RL with two heads: state-value and action-advantage. Both "look" at
different things.

In RNNs: the Jacobian is 3d where the 3rd dimension is time.

### Explicit Attention (Hard) {#explicit-attention--hard}

Implicit attention is great, but explicit might be better:

- Computational efficiency
- Scalability, eg. fixed sized glimpse for any size image
- Sequential processing of static data, eg. moving gaze
- Easier to interpret

Implicit attention uses Jacobian as a guide, not very clear-cut.

### Glimpse {#glimpse}

![[Screen Shot 2020-09-08 at 9.56.02 AM.png]]

### Explicit Attention (Soft/Differentiable) {#explicit-attention--soft-differentiable}

Instead of using a sample, we take an expectation over all possible glimpses.

![[Screen Shot 2020-09-08 at 10.03.40 AM.png]]

### Attention Weights {#attention-weights}

![[Screen Shot 2020-09-08 at 10.07.16 AM.png]]

### Associative Attention {#associative-attention}

Attend to content instead of location. Learns how to align data.

![[Screen Shot 2020-09-08 at 10.32.29 AM.png]]

### Introspective Attention {#introspective-attention}

Memory. Pay attention to a certain point in time.

![[Screen Shot 2020-09-08 at 10.40.49 AM.png]]

### Neural Turing Machine {#neural-turing-machine}

![[Screen Shot 2020-09-08 at 10.42.02 AM.png]]

Want to separate the memory from the computation/controller; in RNN, you'd need
to make the network very complex. Here, it's more scalable with storage.

NTM doesn't process the whole memory at once. (NTM inspired by the handwriting
synthesis network.)

![[Screen Shot 2020-09-08 at 10.44.55 AM.png]]

Memory would be accessed as an associative array.

Allows to do one-to-one copies. NN can't do that because they do more pattern
recognition and not exact things.

### Differential Neural Computers! {#differential-neural-computers}

Follow-up to NTM. Instead of sequences, operations on graphs.

![[Screen Shot 2020-09-08 at 11.03.38 AM.png]]

### Self-Attention (Transformers) {#self-attention--transformers}

- Transformer networks: <sup id="d91e0cc104a7c55638980581a2868ea4"><a href="#Vaswani_Attentionallyou_2017" title="Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser \&amp; Polosukhin, Attention Is All You Need, v(), (2017).">Vaswani_Attentionallyou_2017</a></sup>
- Also see blog "The Annotated Transformer":
    <https://nlp.seas.harvard.edu/2018/04/03/attention.html>
- [[Lim_TemporalFusionTransformers_2019]]

Instead of controller network that uses heads, it comes from data; anarchist
attention.

### Universal Transformers {#universal-transformers}

Links weights. Can make this approach to function more algorithmically.
Can also be applied on variable lengths like an RNN.

![[Screen Shot 2020-09-08 at 11.17.34 AM.png]]

### Time to answer: concentration {#time-to-answer-concentration}

'Pondering' with Adaptive Computation Time: attention by concentration?

### Summary {#summary}

![[Screen Shot 2020-09-08 at 11.27.16 AM.png]]

## DeepMind x UCL | Deep Learning Lectures | 9/12 | Generative Adversarial Networks {#deepmind-x-ucl-deep-learning-lectures-9-12-generative-adversarial-networks}

Link: <https://youtu.be/wFsI2WqUfdA>

[Lim_TemporalFusionTransformers_2019]: ../articles/Lim_TemporalFusionTransformers_2019.md "Lim_TemporalFusionTransformers_2019: Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting"

[//begin]: # "Autogenerated link references for markdown compatibility"
[[Screen Shot 2020-09-08 at 9.56.02 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 9.56.02 AM.png> "Screen Shot 2020-09-08 at 9.56.02 AM.png"
[[Screen Shot 2020-09-08 at 10.03.40 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.03.40 AM.png> "Screen Shot 2020-09-08 at 10.03.40 AM.png"
[[Screen Shot 2020-09-08 at 10.07.16 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.07.16 AM.png> "Screen Shot 2020-09-08 at 10.07.16 AM.png"
[[Screen Shot 2020-09-08 at 10.32.29 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.32.29 AM.png> "Screen Shot 2020-09-08 at 10.32.29 AM.png"
[[Screen Shot 2020-09-08 at 10.40.49 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.40.49 AM.png> "Screen Shot 2020-09-08 at 10.40.49 AM.png"
[[Screen Shot 2020-09-08 at 10.42.02 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.42.02 AM.png> "Screen Shot 2020-09-08 at 10.42.02 AM.png"
[[Screen Shot 2020-09-08 at 10.44.55 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 10.44.55 AM.png> "Screen Shot 2020-09-08 at 10.44.55 AM.png"
[[Screen Shot 2020-09-08 at 11.03.38 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 11.03.38 AM.png> "Screen Shot 2020-09-08 at 11.03.38 AM.png"
[Lim_TemporalFusionTransformers_2019]: ../articles/Lim_TemporalFusionTransformers_2019.md "Lim_TemporalFusionTransformers_2019: Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting"
[[Screen Shot 2020-09-08 at 11.17.34 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 11.17.34 AM.png> "Screen Shot 2020-09-08 at 11.17.34 AM.png"
[[Screen Shot 2020-09-08 at 11.27.16 AM.png]: <../attachments/images/Screen Shot 2020-09-08 at 11.27.16 AM.png> "Screen Shot 2020-09-08 at 11.27.16 AM.png"
[//end]: # "Autogenerated link references"