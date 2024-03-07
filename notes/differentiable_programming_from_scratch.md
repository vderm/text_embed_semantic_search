---
author: Vasken Dermardiros
categories: website
tags:
- programming
- improve
- research
- autodiff
title: Differentiable Programming from Scratch
links:
- https://thenumb.at/Autodiff/
---

A large part of the beginning of the tutorial is about gradients.

## Numerical Differentiation

Then it's about numerical differentiation -> which is to use a small term $\epsilon$ and add that to the function and divide it by that. Basically approximating the derivative by approximating the slope via a line.

## Symbolic Differentiation

Using rules to come up with the differentiation. Like, cos is the derivative of sine and so on. Not the best approach as the number of terms blow up.

## Automatic Differentiation

More efficient and general than the other methods.

Chris Rackauckas has written a whole post on it:
<http://www.stochasticlifestyle.com/engineering-trade-offs-in-automatic-differentiation-from-tensorflow-and-pytorch-to-jax-and-julia/>
Also check how [TinyGrad]([https://github.com/geohot/tinygrad) and [MicroGrad](https://github.com/karpathy/micrograd) works.

AD uses dual numbers where $\epsilon^2=0$.

In particular, we can use the $\epsilon$ part of a dual number to represent the derivative of the scalar part. If we replace each variable $x$ with $x+x'\epsilon$.

## Implementation

Implementing forward-mode autodiff in code can be very straightforward: we just have to replace our `Float` type with a `DiffFloat` that keeps track of both our value and its dual coefficient. If we then implement the relevant math operations for `DiffFloat`, all we have to do is run the program!
