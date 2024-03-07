---
author:
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-06-19 12:22:06-04:00
tags:
- linear
- model
- mpc
- physics-based
- kalman-filter
- research
title: Linear MPC and Kalman Filters
---


cvxpy and lmfit to get something running for RTUs using Kalman filters and
convex MPC.

Honestly, I'm not seeing the ease-of-use of using tensorflow to run state space
models, not as clear/transparent as I'd like it to be. Maybe Fatma N or someone
else might find better use of the multi-linear modeling approach, but maybe it's
more worth it to use this and build on it as we go.

Possible to have more complex approaches to correct this approach.

Work so far: <~/Toolkit_Merged/MLOpsTest/linear_models/grey_box.py>
with report: [[notes/linear-mpc-state-space]]


## Robust Kalman Filtering for Vehicle Tracking {#robust-kalman-filtering-for-vehicle-tracking}

<https://www.cvxpy.org/examples/applications/robust%5Fkalman.html>
<https://colab.research.google.com/github/cvxgrp/cvxpy/blob/master/examples/notebooks/WWW/robust%5Fkalman.ipynb>


### Robust Kalman filtering for vehicle tracking {#robust-kalman-filtering-for-vehicle-tracking}

We will try to pinpoint the location of a moving vehicle with high accuracy from
noisy sensor data. We'll do this by modeling the vehicle state as a
discrete-time linear dynamical system. Standard ****Kalman filtering**** can be used
to approach this problem when the sensor noise is assumed to be Gaussian. We'll
use ****robust Kalman filtering**** to get a more accurate estimate of the vehicle
state for a non-Gaussian case with outliers.


### Problem statement {#problem-statement}

A discrete-time linear dynamical system consists of a sequence of state vectors
\\(x\_t \in \mathbf{R}^n\\), indexed by time \\(t \in \lbrace 0, \ldots, N-1 \rbrace\\)
and dynamics equations

\begin{align}
x\_{t+1} &= Ax\_t + Bw\_t\\\\\\
y\_t &=Cx\_t + v\_t,
\end{align}

where \\(w\_t \in \mathbf{R}^m\\) is an input to the dynamical system (say, a drive
force on the vehicle), \\(y\_t \in \mathbf{R}^r\\) is a state measurement, \\(v\_t \in
\mathbf{R}^r\\) is noise, \\(A\\) is the drift matrix, \\(B\\) is the input matrix, and
\\(C\\) is the observation matrix.

Given \\(A\\), \\(B\\), \\(C\\), and \\(y\_t\\) for \\(t = 0, \ldots, N-1\\), the goal is to estimate
\\(x\_t\\) for \\(t = 0, \ldots, N-1\\).


### Kalman filtering {#kalman-filtering}

A Kalman filter estimates \\(x\_t\\) by solving the optimization problem

\begin{array}{ll}
\mbox{minimize} & \sum\_{t=0}^{N-1} \left(
\\|w\_t\\|\_2^2 + \tau \\|v\_t\\|\_2^2\right)\\\\\\
\mbox{subject to} & x\_{t+1} = Ax\_t + Bw\_t,\quad t=0,\ldots, N-1\\\\\\
& y\_t = Cx\_t+v\_t,\quad t = 0, \ldots, N-1,
\end{array}

This model performs well when \\(w\_t\\) and \\(v\_t\\) are Gaussian. However, the
quadratic objective can be influenced by large outliers, which degrades the
accuracy of the recovery. To improve estimation in the presence of outliers, we
can use ****robust Kalman filtering****.

where \\(\tau\\) is a tuning parameter. This problem is actually a least squares
problem, and can be solved via linear algebra, without the need for more general
convex optimization. Note that since we have no observation \\(y\_{N}\\), \\(x\_N\\) is
only constrained via \\(x\_{N} = Ax\_{N-1} + Bw\_{N-1}\\), which is trivially resolved
when \\(w\_{N-1} = 0\\) and \\(x\_{N} = Ax\_{N-1}\\). We maintain this vestigial constraint
only because it offers a concise problem statement.


### Robust Kalman filtering {#robust-kalman-filtering}

To handle outliers in \\(v\_t\\), robust Kalman filtering replaces the quadratic cost
with a Huber cost, which results in the convex optimization problem

\begin{array}{ll}
\mbox{minimize} & \sum\_{t=0}^{N-1} \left( \\|w\_t\\|^2\_2 + \tau \phi\_\rho(v\_t) \right)\\\\\\
\mbox{subject to} & x\_{t+1} = Ax\_t + Bw\_t,\quad t=0,\ldots, N-1\\\\\\
& y\_t = Cx\_t+v\_t,\quad t=0,\ldots, N-1,
\end{array}

where \\(\phi\_\rho\\) is the Huber function
\\[
\phi\_\rho(a)= \left\\{ \begin{array}{ll} \\|a\\|\_2^2 & \\|a\\|\_2\leq \rho\\\\\\
2\rho \\|a\\|\_2-\rho^2 & \\|a\\|\_2>\rho.
\end{array}\right.
\\]

The Huber penalty function penalizes estimation error linearly outside of a ball
of radius \\(\rho\\), whereas in standard Kalman filtering, all errors are penalized
quadratically. Thus, large errors are penalized less harshly, making this model
more robust to outliers.


### Vehicle tracking example {#vehicle-tracking-example}

We'll apply standard and robust Kalman filtering to a vehicle tracking problem
with state \\(x\_t \in \mathbf{R}^4\\), where \\((x\_{t,0}, x\_{t,1})\\) is the position of
the vehicle in two dimensions, and \\((x\_{t,2}, x\_{t,3})\\) is the vehicle velocity.
The vehicle has unknown drive force \\(w\_t\\), and we observe noisy measurements of
the vehicle's position, \\(y\_t \in \mathbf{R}^2\\).

The matrices for the dynamics are

\\[
A = \begin{bmatrix}
1 & 0 & \left(1-\frac{\gamma}{2}\Delta t\right) \Delta t & 0 \\\\\\
0 & 1 & 0 & \left(1-\frac{\gamma}{2} \Delta t\right) \Delta t\\\\\\
0 & 0 & 1-\gamma \Delta t & 0 \\\\\\
0 & 0 & 0 & 1-\gamma \Delta t
\end{bmatrix},
\\]

\\[
B = \begin{bmatrix}
\frac{1}{2}\Delta t^2 & 0 \\\\\\
0 & \frac{1}{2}\Delta t^2 \\\\\\
\Delta t & 0 \\\\\\
0 & \Delta t \\\\\\
\end{bmatrix},
\\]

\\[
C = \begin{bmatrix}
1 & 0 & 0 & 0 \\\\\\
0 & 1 & 0 & 0
\end{bmatrix},
\\]
where \\(\gamma\\) is a velocity damping parameter.


### 1D Model {#1d-model}

The recurrence is derived from the following relations in a single dimension. For this subsection, let \\(x\_t, v\_t, w\_t\\) be the vehicle position, velocity, and input drive force. The resulting acceleration of the vehicle is \\(w\_t - \gamma v\_t\\), with \\(- \gamma v\_t\\) is a damping term depending on velocity with parameter \\(\gamma\\).

The discretized dynamics are obtained from numerically integrating:
$$

\begin{align}
x\_{t+1} &= x\_t + \left(1-\frac{\gamma \Delta t}{2}\right)v\_t \Delta t + \frac{1}{2}w\_{t} \Delta t^2\\\\\\
v\_{t+1} &= \left(1-\gamma\right)v\_t + w\_t \Delta t.
\end{align}

$$

Extending these relations to two dimensions gives us the dynamics matrices \\(A\\)
and \\(B\\).


## Control (MPC) {#control--mpc}

<https://colab.research.google.com/github/cvxgrp/cvx%5Fshort%5Fcourse/blob/master/intro/control.ipynb>

Convex optimization can be used to solve many problems that arise in control. In
this example we show how to solve such a problem using CVXPY. We have a system
with a state \\(x\_t\in {\bf R}^n\\) that varies over the time steps \\(t=0,\ldots,T\\),
and inputs or actions \\(u\_t\in {\bf R}^m\\) we can use at each time step to affect
the state. For example, \\(x\_t\\) might be the position and velocity of a rocket and
\\(u\_t\\) the output of the rocket's thrusters. We model the evolution of the state
as a linear dynamical system, i.e.,

\\[ x\_{t+1} = Ax\_t + Bu\_t \\]

where \\(A \in {\bf R}^{n\times n}\\) and \\(B \in {\bf R}^{n\times m}\\) are known matrices.

Our goal is to find the optimal actions \\(u\_0,\ldots,u\_{T-1}\\) by solving the optimization problems

\begin{array}{ll} \mbox{minimize} & \sum\_{t=0}^{T-1} \ell (x\_t,u\_t) + \ell\_T(x\_T)\\\\\\
\mbox{subject to} & x\_{t+1} = Ax\_t + Bu\_t\\%, \quad t=0, \ldots, T-1\\\\\\
& (x\_t,u\_t) \in \mathcal C, \quad x\_T\in \mathcal C\_T,
%, \quad \quad t=0, \ldots, T
\end{array}

where \\(\ell: {\bf R}^n \times {\bf R}^m\to {\bf R}\\) is the stage cost, \\(\ell\_T\\) is the terminal cost,
\\(\mathcal C\\) is the state/action constraints, and \\(\mathcal C\_T\\) is the terminal constraint.
The optimization problem is convex if the costs and constraints are convex.

```python
# Generate data for control problem.
import numpy as np
np.random.seed(1)
n = 8
m = 2
T = 50
alpha = 0.2
beta = 5
A = np.eye(n) + alpha*np.random.randn(n,n)
B = np.random.randn(n,m)
x_0 = beta*np.random.randn(n)


# Form and solve control problem.
import cvxpy as cp

x = cp.Variable((n, T+1))
u = cp.Variable((m, T))

cost = 0
constr = []
for t in range(T):
    cost += cp.sum_squares(x[:,t+1]) + cp.sum_squares(u[:,t])
    constr += [x[:,t+1] == A@x[:,t] + B@u[:,t],
               cp.norm(u[:,t], 'inf') <= 1]
# sums problem objectives and concatenates constraints.
constr += [x[:,T] == 0, x[:,0] == x_0]
problem = cp.Problem(cp.Minimize(cost), constr)
problem.solve(solver=cp.ECOS)


# Plot results.
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'svg'

f = plt.figure()

# Plot (u_t)_1.
ax = f.add_subplot(411)
plt.plot(u[0,:].value)
plt.ylabel(r"$(u_t)_1$", fontsize=16)
plt.yticks(np.linspace(-1.0, 1.0, 3))
plt.xticks([])

# Plot (u_t)_2.
plt.subplot(4,1,2)
plt.plot(u[1,:].value)
plt.ylabel(r"$(u_t)_2$", fontsize=16)
plt.yticks(np.linspace(-1, 1, 3))
plt.xticks([])

# Plot (x_t)_1.
plt.subplot(4,1,3)
x1 = x[0,:].value
plt.plot(x1)
plt.ylabel(r"$(x_t)_1$", fontsize=16)
plt.yticks([-10, 0, 10])
plt.ylim([-10, 10])
plt.xticks([])

# Plot (x_t)_2.
plt.subplot(4,1,4)
x2 = x[1,:].value
plt.plot(range(51), x2)
plt.yticks([-25, 0, 25])
plt.ylim([-25, 25])
plt.ylabel(r"$(x_t)_2$", fontsize=16)
plt.xlabel(r"$t$", fontsize=16)
plt.tight_layout()
plt.show()
```


## Mixed-Integer solvers {#mixed-integer-solvers}

<https://www.cvxpy.org/tutorial/advanced/index.html>
<https://github.com/embotech/ecos#mixed-integer-socps-ecos%5Fbb>

ECOS\_BB is not a high-performance solver however, might not work with large
problems = 1000? 10000 variables?

```python
>>> import cvxpy
>>> print(cvxpy.installed_solvers())
['ECOS', 'ECOS_BB', 'OSQP', 'SCS']
```

Alternatives:

- [CBC](https://projects.coin-or.org/Cbc)
- [GLPK\_MI](https://www.gnu.org/software/glpk/)
- [CPLEX](https://www-01.ibm.com/software/commerce/optimization/cplex-optimizer/)
- [GUROBI](http://www.gurobi.com/)
- [MOSEK\*](https://www.mosek.com/)

Or even using GAs or maybe TF2?

[//begin]: # "Autogenerated link references for markdown compatibility"
[notes/linear-mpc-state-space]: linear-mpc-state-space.md "State-Space Model + Convex MPC"
[//end]: # "Autogenerated link references"