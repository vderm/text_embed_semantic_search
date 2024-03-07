---
author:
- Chris Rackauckas
categories: website
draft: false
lastmod: 2022-01-20
tags:
- julia
- programming
- physics-based
- model
- reinforcement-learning
title: The Use and Practice of Scientific Machine Learning (Chris Rackauckas) - nextgen_ai Freiburg 2021
links:
- https://www.youtube.com/watch?v=FihLyzdjN_8&t=4s
---

+ How much data do you need to train a neural network that can predict general relativity?
  + They were based on 30 or so experiments
+ In physics, we make approximations
  + Linearizing in local
  + Ignore friction

+ What has changed so that we can do SciML?
  + Put as much of the field we know and let the neural net cover what we don't know
  + Doesn't get too far from the physics

![Embed NN in mechanistic models](../attachments/2022-01-20-16-13-01.png)

![Probability of Missing Mechanisms](../attachments/2022-01-20-16-15-15.png)

Probability that there are missing structural inputs that can be recovered.

+ Approach learns mechanistic model -> can we do counterfactuals? Chris points to yes.
  + SciML can get there more quickly

![QSIR Counterfactuals](../attachments/2022-01-20-16-23-48.png)

![DeepNLME to speed-up clinical trials](../attachments/2022-01-20-16-32-02.png)

This ^ spits out a LaTeX representation of the found equation and places it in a report.

![Neural ODE paper](../attachments/2022-01-20-16-43-01.png)

Paper is mathematically correct but numerically unstable. Can lead to a 10^30 error in a stiff-ODE, like if it comes from a Navier-Stokes equation.

![Problems with naïve adjoint approaches](../attachments/2022-01-20-16-42-30.png)

You need to care on how the derivative is calculated.

![Discretization: forward or backward](../attachments/2022-01-20-16-45-41.png)

Depends on which data is available for the time "t". Stable given [von Neumann stability analysis](https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis).

So naïve way can be stable in forward direction, but not backward (adjoint). Or the other way around if backward difference is taken.

Need something stable and good so that people use it. No one in practice uses the implicit or Crank-Nicholson method.

**Chris disagrees with some professors stating that robust methods and software will push scientific progress.**

![Composable tools, models, functions](../attachments/2022-01-20-16-52-17.png)

![Fitting process is fully automated](../attachments/2022-01-20-17-06-20.png)

![DiffEqFlux: Library of Robust Fitting Techniques](../attachments/2022-01-20-17-07-52.png)

![Chaotic systems](../attachments/2022-01-20-17-11-51.png)

![DiffEqSensitivity.jl: every adjoint is optimized for a different case](../attachments/2022-01-20-17-14-35.png)

But how do you automate the solver selection? They're working on it.

![SciML Common Interface, Oversimplified](../attachments/2022-01-20-17-39-53.png)
