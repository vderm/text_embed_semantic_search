---
author:
- Vasken Dermardiros
categories: website
draft: false
lastmod: 2021-01-03 22:49:00-05:00
tags:
- tensorflow
- research
- neural-structured-learning
title: Neural Structured Learning
links:
- https://www.tensorflow.org/neural%5Fstructured%5Flearning/
- https://blog.tensorflow.org/2019/09/introducing-neural-structured-learning.html
---


<https://www.tensorflow.org/neural%5Fstructured%5Flearning/>

<https://blog.tensorflow.org/2019/09/introducing-neural-structured-learning.html>

Neural Structured Learning (NSL) is a new learning paradigm to train neural
networks by leveraging structured signals in addition to feature inputs.
Structure can be explicit as represented by a graph or implicit as induced by
adversarial perturbation.

Structured signals are commonly used to represent relations or similarity among
samples that may be labeled or unlabeled. Therefore, leveraging these signals
during neural network training harnesses both labeled and unlabeled data, which
can improve model accuracy, particularly when the amount of labeled data is
relatively small. Additionally, models trained with samples that are generated
by adding adversarial perturbation have been shown to be robust against
malicious attacks, which are designed to mislead a model's prediction or
classification.