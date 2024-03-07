---
author:
- Sam Greydanus
categories: website
draft: false
lastmod: 2021-01-03 22:49:05-05:00
slug: scaling_down_deep_learning
tags:
- research
title: Scaling down Deep Learning
links:
- https://greydanus.github.io/2020/12/01/scaling-down/
---

<https://greydanus.github.io/2020/12/01/scaling-down/>#

MNIST-1D dataset to have in a more controlled and simplified way to compare the
different deep learning methods together. He does tests to check the advantage
of CNN over MLP; winning lottery ticket tests; double descent; metalearning an
activation function: activation function does OK on a new example.

Double descent doesn't quite happen in CNN as it does in MLP.

![[2020-12-28_09-48-09_overview_a.png]]
caption="Figure 1: MNIST-1D Dataset

Learned activation function:

![[2020-12-28_09-49-40_metalearn_afunc_c.png]]
caption="Figure 2: Learned activation function


[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-12-28_09-48-09_overview_a.png]: ../attachments/2020-12-28_09-48-09_overview_a.png "2020-12-28_09-48-09_overview_a.png"
[[2020-12-28_09-49-40_metalearn_afunc_c.png]: ../attachments/2020-12-28_09-49-40_metalearn_afunc_c.png "2020-12-28_09-49-40_metalearn_afunc_c.png"
[//end]: # "Autogenerated link references"