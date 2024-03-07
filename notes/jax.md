---
author: Vasken Dermardiros
categories: website
tags:
- research
- programming
- reference
title: jax
links:
- https://jax.readthedocs.io/en/latest/notebooks/quickstart.htm
- https://github.com/google/jax
---

- Quickstart :: https://jax.readthedocs.io/en/latest/notebooks/quickstart.html
- Repo :: https://github.com/google/jax
- Autodiff cookbook :: https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html
- [Autogram](https://github.com/hips/autograd)

JAX is a system for high-performance machine learning research and numerical
computing. It offers the familiarity of Python+NumPy together with hardware
acceleration, and it enables the definition and composition of user-wielded
function transformations. These transformations include automatic
differentiation, automatic vectorized batching, end-to-end compilation (via
XLA), parallelizing over multiple accelerators, and more.

# JAX: Accelerated Machine Learning Research | SciPy 2020 | VanderPlas
https://www.youtube.com/watch?v=z-WSrQDXkuM

Motivating JAX
- What if you want to write a neural network from scratch?
  - Numpy isn't optimized
  - Gradient descent, autodiff not possible
  - sum(diff^2) -> do this in one go not possible
  - Parallelization

- jax :: numpy equivalent can compile to XLA -> run on GPU/TPU accelerators
- grad :: gradient, autodiff
- vmap :: vectorization
- jit :: just-in-time compilation, fusing of operations
- xla :: accelerated linear algebra

## Example
``` python
import jax.numpy as np
from jax import grad, vmap, jit
# and go as you would
# gradient_fun = grad(loss)

# compilation
gradient_fun = jit(grad(loss))
perexample_grads = jit(vmap(grad(loss), in_axes=(None, 0)))
# vmap() -> gmap() :: parallelization -> use GPU/TPU/multiple-CPU
```


``` python
import jax.numpy as jnp
y = jnp.array(x)
# -> y is a DeviceArray -> lives on device
```

``` python
  def f(x):
      for i in range(10):
          x -= 0.1 * x
      return x

  %timeit f(y)

  from jax import jit
  g = jit(f)
  g(y)
  %timeit g(y)
```

Basically, write out code that makes sense, JIT will make it efficient!

## Automatic Differentiation
``` python
  def f(x):
      return x * jnp.sin(x)

  f(4)

  def grad_f(x):
      return jnp*sin(x) + x * kjp.cos(x)
  grad_f(4.0)

  from jax import grad
  grad_f_jax = grad(f)
  grad_f_jax(4.0)
```

Not doing a finite difference, actually getting an analytical solution.

## Vectorization
``` python
  def square(x):
      return jnp.sum(x ** 2)

  square(jnp.arange(10))

  x = jnp.arange(100).reshape(10, 10)
  [square(row) for row in x]  # not the best


  from jax import vmap
  vmap(square)(x)
```

## Jax vs Numba
jax.jit uses /tracers/ to observe how a function operates on /abstract inputs/,
and compiles via /XLA/.

numba.jit /transpiles/ python bytecode directly to /LLVM/ for compilation

## TODO Robots -> efficient
cite:Yang_DataEfficientReinforcement_2019

# Introduction to JAX
@jit decorate
https://www.youtube.com/watch?v=0mVmRHMaOJ4


Example of defining and training a neural network on MNIST
https://colab.research.google.com/github/google/jax/blob/master/docs/notebooks/neural_network_with_tfds_data.ipynb