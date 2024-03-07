---
author:
- Vasken Dermardiros
categories: website
draft: false
lastmod: 2020-06-19 12:21:09-04:00
tags:
- model
- brainbox
- research
- tensorflow
- linear
- mpc
- organizing
- physics-based
- prod
- reference
- tft
title: Models at BrainBox AI
---

![AI/ML models recognized by the industry](../attachments/2022-04-07-15-54-23.png)

Models are approximation to an underlying phenomenon. To quote George Box, all models are wrong, but some are useful. I've tried to compile a list of approaches we've so-far used at BrainBox and will try to mention if these went into production or they never graduated from being a proof-of-concept. Please keep this somewhere close in case you get asked again. Don't reproduce any of it ad verbatim since it's not writen in a professional and exact language. Some of this work is published and we would encourage to use those instead.

+ Machine Learning / Supervised Learning / Regression category
  - Linear regression models: the things you can do on Excel. Infinitely useful!
  - MLP: the most basic model, kind of okay performance. Benoit Delcroix was pushing this approach about 3 years ago. We still use these types of models for very simple things and parts of another model (yes, you can mix and match)
  - LSTM: you know this one
  - CNN-LSTM: a mix of an LSTM with a convolutional neural network (CNNs are designed for image recognition but timeseries data can be seen as an image where the "height" of the picture is time); this one was used in our 'legacy' pipeline on bb-ec2, we don't use this anymore
  - sequence-to-sequence model aka seq2seq aka encoder-decoder model: two LSTMs back-to-back where the first takes in as input the past, encodes it and passes it to the decoder which also takes in future data (weather, controls) and outputs future predictions (temperature). This does better than the CNN-LSTM. Fatma used this at the beginning for Gargamel
  - Attention-based models aka Transformers: Models much more suited for longer time predictions since the model can learn to put attention at any specific timestep. The LSTM would squash multiple timesteps into a vector, the Transformer doesn't need to squash anything. Emilio used a specific version of this called the "Temporal Fusion Transformer" model to try to combine many buildings into a single model. Didn't work too well since the features from building to building are too different. Will explore again for Walmart and SleepCountry soon.
  - "Control-first attention-based model" (I don't remember the exact name Fatma gave to her model): it's a Transformer model where the controls are given a higher emphasis than the other inputs.
  - "Control-sensitive model": Ysael's design. 3 LSTM models that output changes of temperature. Each LSTM is trained to predict the residual of the previous. First, we try to predict the change of temperature strictly based on the controls. We freeze the first model. Then, we train an additional model based on past-state to predict the residual. We freeze the second model. And then we train one last model based on exogenous inputs (weather, time features). We may decide to unfreeze all the models and fine-tune them a bit together.
  - Physics-informed LSTM model: training an LSTM model where the training function also includes a physics term (like dT = U*(T_out - T_in); so the loss function to train the model is that and the usual mean squared error term: sum[(T_predicted - T_actual)^2] ) This was part of Emma's internship and as she just got comfortable with it, her internship ended.
  - Universal differential equation: this approach is about writing out a differential equation representing the rate of change of temperature in a room described by a sum of physical terms, like dT_in / dt = U_ext*(T_ext - T_in) + U_ij*(T_neighbour - T_in) + dQ/dt + ... the fun part here is to replace the terms we don't know with a function approximator (read: neural network). Example: dT_in / dt = U*(T_ext - T_in) + U*(T_neighbour - T_in) + neural_network(hvac_states) + ... And for this one, we've also moved to the Julia programming language instead of Python/TensorFlow and are using higher-order differential equation solvers. Finally, the numerical methods course is paying off!
  - This sort of approach can also be used to model specific equipment like chillers, boilers, cooling towers that don't have a linear response. They might be modelled with a polynomial and we can also add a small neural network to them to capture the residuals.
  - As engineers, we don't really like neural networks because they are black boxes. To "lighten" them a bit, we've also experimented with a technique called SINDy (sparse identification of nonlinear dynamics). Here, we try to replicate the behaviour of the neural network with a sparse set of simpler equations.
  - k-NN (k-nearest neighbours) is used as an "emergency data filler" in production to fill in values of zones where we don't have data. The controls for these zones are later dropped since the temperatures are approximations.
  - [Been a long while] Bag-of-thermal-moments (BoTM). This is also an MLP model just with a very heavy pre-processing step. We said, let the model learn this instead, and we abandoned that a long time ago.
+ Machine Learning / Supervised Learning / Classification category:
  - Support vector machines + random forests to predict haystack tags given a timeseries; if you haven't guessed it, this is Autobot. How these two models are connected is a little particular.
  - [Been a long while] Peak power warning system: we had started work with Marion to have a model signal if we're anticipating a peak event in the near future. We abandoned this in lieu to simply make a call to PowerKit with the future controls instead. The API work in underway.
  - There might be a model somewhere that predicts zone temperature by temperature bins, but i think this is just on Ysael's laptop.
+ Machine Learning / Unsupervised Learning / Clustering category:
 - We've used k-means to determine "typical days" and this is used mainly in the exploratory data analysis phase; it's not consumed by algos.
 - We had tested a gaussian mixture model to quantify whether a zone was unoccupied or not, didn't work well (thus enphasizing that you can't just throw data at a model and hope it'll work); the simpler solution was: if CO2_concentration(t+1) - CO2_concentration(t) >= threshold --> then it's occupied, otherwise it's not. Ez pz.
+ Machine Learning / Reinforcement Learning / Decision Making category:
  - We tested RL methods on controlling an RTU unit with Ysael; we wrote a paper too but it got rejected and haven't updated it since. There's still some merit in continuing this work. It would fall under a model-based reinforcement learning approach. This never went in production.
+ Operational research / model-based predictive controls:
  - Not necessarily ML since the controller doesn't learn here, however worth mentionning: the Gargamel algos consist of two parts: the model and the optimizer. The model is described above and can be swapped for anything. The optimizer is based on a genetic algorithm approach and aims to minimize operational costs while adhering to comfort and equipement limits. Since the first version of Gargamel, we're on a second iteration that is decentralized. There's a supervisor/aggregator layer that looks at the operational cost and the agent layer that tries to maintain comfort in its assigned zone given an energy budget from the supervisor. We're on our 2nd draft of a journal paper for this work.
  - There's other work brewing on the optimal control side, we'll let you know what it is as soon as we're convinced it works. To quote Frank Sullivan, stay tuned.
+ Machine Learning / Semi-supervised Learning / Fault-Detection category:
  - For run fault detection, we're relying on the same models we use for temperature prediction. To do the uncertainty estimates, any model with a "dropout" layer can be used. A dropout layer basically drops incoming connections randomly to make sure models can generalize better. The uncertainty estimate bootstraps this layer to generate multiple slightly different predictions. With many predictions, you can do some statistics on it, like min/max/average/st.dev/percentiles, etc.
  - Faults are rare compared to non-faults so the dataset becomes highly unbalanced. We've tested a method called MADI (Multidimensional multimodal Anomaly Detection with Interpretation) and it gave some good results however we never got solid feedback to know whether what it detected were actual faults or not. Faults are tricky because we can't just go on side and verify.

Generally speaking, it's not just the model type/architecture, but how things are connected, how pre-processing was done and how these things were trained. It's really more art than science still.