---
author:
- Chris Rackauckas
- Vasken Dermardiros
categories: website
draft: false
lastmod: 2022-01-13
tags:
- julia
- programming
- physics-based
- model
- reinforcement-learning
- revisit
title: State of Machine Learning in Julia
links:
- https://discourse.julialang.org/t/state-of-machine-learning-in-julia/74385
---

Looks like it's an active discussion.

Also see the [HN posts](https://news.ycombinator.com/item?id=29902846)

# Questions

1. Where does ML in Julia really shine *today*? Where do you see the ecosystem outperforming other popular ML frameworks (e.g. PyTorch, Flax, etc) in the near future, and why?
2. Where is Julia’s ML ecosystem currently inferior in features or performance? What’s the realistic timeline for it becoming competitive in these areas?
3. How do Julia’s ML packages for “standard ML” (e.g. deep learning) compare with popular alternatives in terms of performance (faster, slower, same order of magnitude)? Are there regularly updated benchmarks somewhere?
4. What don’t we know yet but suspect is an important experiment to make for benchmarking against popular ML alternatives?
5. If a company or institution is considering creating multi-year positions to contribute to Julia’s ML ecosystem, what is the best case you can make why they should do this? What contributions would be most impactful?
6. What is the best case you can make why independent developers who work with other frameworks should consider contributing to Julia’s ML ecosystem?
7. What packages do you tend to reach for for some specific tasks? Why those packages vs some other Julia package or one in another language? What do you wish existed but currently doesn’t?

# Reply from Chris Rackauckas

## Question 1: Where does Julia Shine

For scientific machine learning (also known as physics-informed learning, or science-guided AI, or expert-guided AI, etc. see the note at the bottom), Julia is really good. If you don’t know what that is, check out this recent seminar talk which walks through SciML for model discovery in epidemics, climate modeling, and more.

[The Use and Practice of Scientific Machine Learning (Chris Rackauckas) - nextgen_ai Freiburg 2021](https://www.youtube.com/watch?v=FihLyzdjN_8&t=4s)

It's not the physics that helps but having a good ODE solver:
[Faster Policy Learning with Continuous-Time Gradients](https://arxiv.org/pdf/2012.06684.pdf)

The other thing is differentiable programming on non quasi-static programs, and I’ll let this blog speak for itself.
[Useful Algorithms That Are Not Optimized By Jax, PyTorch, or Tensorflow](https://www.stochasticlifestyle.com/useful-algorithms-that-are-not-optimized-by-jax-pytorch-or-tensorflow/)

## Question 2: where is the Julia ML ecosystem currently inferior?

[Engineering Trade-Offs in Automatic Differentiation: from TensorFlow and PyTorch to Jax and Julia](https://www.stochasticlifestyle.com/engineering-trade-offs-in-automatic-differentiation-from-tensorflow-and-pytorch-to-jax-and-julia/)

Julia uses its own compiler. TensorFlow and Jax might win in very large problems because they will rely on cudnn kernels which have optimized operations, eg.`cudnn_convolution_add_relu` for `relu(conv(x)) .+ y,`.

A lot of these optimizations will start to be done too in Julia, see
[Automated Code Optimization with E-Graphs](https://arxiv.org/pdf/2112.14714.pdf)

So in theory getting ML performance is simple: you just use fast kernels.

## Question 3: How well does Julia perform in “standard ML”?

Basically the same. On CPUs it wins, for AD, its about the same because the matrix multiplier overhead dominates anyway, and since Julia doesn't fuse kernals, others might do better through argument calls only.

## Question 4: What important experiments and benchmarks should we be tracking?

(not sure I understand)

## Question 5: Which companies and institutions are looking to give multi-year positions?

Both Julia Computing and Pumas-AI have many folks doing SciML though, and if you’re interested in SciML stuff please get in touch.

## Question 6: Why should independent developers consider contributing?

# Question 7: What packages do you use and which packages do you wish existed?

I tend to reach to Flux when I need to, but try to stick to DiffEqFlux. Flux is just the most complete in terms of kernels that exist, but its style irks me.

# There's another person who replied under and is much more critical about things :)

Follow up with Diffractor.jl
Better autodifferentiation. I know there’s ongoing work in this space (i.e. Diffractor.jl, which I haven’t tried yet) but so far IMO Julia hasn’t yet caught up to PyTorch/JAX on this front.
