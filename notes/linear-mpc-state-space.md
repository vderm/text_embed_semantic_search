---
author:
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-06-12 22:59:46-04:00
tags:
- linear
- model
- mpc
- physics-based
- kalman-filter
- research
title: State-Space Model + Convex MPC
---


Following up on the work from Benoit Delcroix, I'm working on a proof-of-concept
(POC) to have a simple state-space transitional model that can be used for
building with rooftop units (RTU). Work so far can be clone from [here](https://git.brainboxai.net/Toolkit/MLOpsTest/src/branch/state%5Fspace/linear%20models).

**Why?** Explicit mapping of controllable inputs to outputs; less free parameters
 and so training is much quicker. I'm using Google Popular Times as a surrogate
 to occupancy and discretizing spaces into single zones. Another advantage of
 using physics-based modeling is that the model parameters have a meaning and
 this can be used to group buildings together.

**Why not deep learning?** I'm not against deep learning approaches, just
 wondering if a simpler method also has value here. Heat transfer dynamics for
 normal buildings is mainly linear and so a linear model is theoretically
 sufficient to describe the transition process. Probabilistic models can be used
 as a functional feature (inserted in `ai_config.json` as a `$function$`). This
 can be pushed further into the field of Model-based machine learning (see
 <http://mbmlbook.com/> or through Tensorflow's [multilevel modeling](https://github.com/tensorflow/probability/blob/master/tensorflow%5Fprobability/examples/jupyter%5Fnotebooks/Multilevel%5FModeling%5FPrimer.ipynb)).

Lastly, I'm always a little unsure if deep learning methods are actually
learning the dependence between controllable input towards the prediction
output. If I turn on the heating, does the temperature go up because of this? Or
does it go up because it's 9:00 AM?

When using reinforcement learning, the agent learns to map the input state to an
action so it _has to_ understand this effect. We just can't experiment on the
real building, so we need to approach this somehow. The RC model here can be
used as a transitional model for the RL to train on. We can also use EnergyPlus
as a simulator ([version 9.3](https://github.com/NREL/EnergyPlus/releases) has a Python interface).

## <span class="section-num">1</span> State-Space Model {#state-space-model}

### <span class="section-num">1.1</span> Overview {#overview}

Surprise surprise! This is where are friends \\({X,U,W}\\) come from! Without going
through all the details, I'm looking to use a simple variant: explicit discrete
linear time-invariant. Which is defined as:

\\(y(t) = x(t+1) = Ax(t) + Bu(t) + Cw(t)\\), where:

\\(y(t)\\)
: model output, which is the same as what goes back in for the following timestep (recursive)

\\(x(t)\\)
: model input, eg. zone temperature

\\(u(t)\\)
: controllable inputs, eg. heating/cooling stages, fan, damper position, etc.

\\(w(t)\\)
: exogenous inputs, eg. weather and time indicators

\\(A,B,C\\)
: state and input matrices; these need to be identified/fitted

In the literature the state space model is expressed:

\\(x(t+1) = A x(t) + B\_1 u(t) + B\_2 w(t) + \epsilon\\)

\\(y(t) = C x(t) + D\_1 u(t) + D\_2 w(t) + k \epsilon\\)

but for buildings, C is an identity matrix and D\_1 and D\_2 are vectors with zeros which is then
equivalent to the expression at the top since what we observe is what we
want to control. The random noise term \\(\epsilon\\) is not fitted and assumed
to be normal and centered.

### <span class="section-num">1.2</span> Node assumption {#node-assumption}

Here's an example for a 2-zone building in Figure&nbsp;[fig:circuit](#fig:circuit). I'm
assuming that each zone has an effective capacitance; all the RTU
heating/cooling is supplied to its node directly; all other sources of heat
within that zone are input to the node (occupancy loads, solar gains, plug
loads, lighting); all nodes have a conductance to every other zone (regardless
of adjacency) and towards the ambient air. I'm thinking of adding something to
represent fresh air coming into the building because the fan is on (conditional
leakage).

<a id="code-snippet--fig:circuit"></a>

```nil
        +----------++----------+
        |          ||          |
        |  Zone 0  ||  Zone 1  |
T_ext   |          ||          |   T_ext (=F0)
     F00|          ||U01       |F10
   O---www---o----wwww----o---www---O
        |     | C0 |  |  | C1 |
        | --- || --- |
| --- ||    --- |
        |    |     ||     |    |
        |   GND    ||    GND   |
        +----------++----------+
```

<div class="src-block-caption">
  <span class="src-block-number"><a href="#code-snippet--fig:circuit">Code Snippet 1</a></span>:
  Bobo representation of the thermal circuit
</div>

### <span class="section-num">1.3</span> Matrices A, B, C {#matrices-a-b-c}

It's a linear model. To get the future \\(x\\), you sum 3 matrix multiplications.
This means, matrix \\(A\\) somewhat tracks how the current temperature has an
influence on the next timestep and how the zones influence each other. Matrix
\\(B\\) maps HVAC states into a change in temperature and matrix \\(C\\) maps exogenous
inputs into a change in temperature. You can add more past steps, but let's keep
in simple.

To see what these matrices look like (with conductances and capacitances that
need to be fit), please see Benoit's paper [I don't feel like writing matrices
of equations in LaTeX right now&#x2026;] or see the code directly.

### <span class="section-num">1.4</span> Fitting the models {#fitting-the-models}

Using 'leastsq' in [lmfit](https://lmfit.github.io/lmfit-py/) followed by [emcee](https://lmfit.github.io/lmfit-py/fitting.html#label-emcee) to calculate the posterior
probability distribution of parameters. The prediction errors from \\(t+1\\) to
\\(t+ph\\) are to be minimized (MSE). Can weigh zones differently too based on
importance or size of the zone (similar to parachute).

### <span class="section-num">1.5</span> Results: <span class="timestamp-wrapper"><span class="timestamp">&lt;2020-06-01 Mon&gt;</span></span> {#results}

What do you think? Figures&nbsp;[fig:pnt_1](#fig:pnt_1) and [fig:pnt_2](#fig:pnt_2) seem to be okay
but Figure&nbsp;[fig:pnt_3](#fig:pnt_3) doesn't look too great. Table&nbsp;[tab:fit](#tab:fit)
gives the best fit parameters and their uncertainties; which aren't bad at all;
Figure&nbsp;[fig:emcee](#fig:emcee) shows the MCMC sampling of the parameters. You can
observe that the parameter distributions are unimodal and that there is a strong
correlation between parameters &#x2013; least-squares assumes variables are
independent.

<a id="org57fe6f9"></a>

PNT_1.png caption="Figure 1: Building 271 PNT-1

<a id="org47a196c"></a>

PNT_2.png" caption="Figure 2: Building 271 PNT-2

<a id="orgde3e5e0"></a>

PNT_3.png" caption="Figure 3: Building 271 PNT-3

<a id="table--tab:fit"></a>
<div class="table-caption">
  <span class="table-number"><a href="#table--tab:fit">Table 1</a></span>:
  EMCEE Fit Results
</div>

| Parameter     | Value                                                    |
| ------------- | -------------------------------------------------------- |
| C\_1          | 32609572.8 +/- 1845252.17 (5.66%) (init = 3.238194e+07)  |
| Cool\_stg1\_1 | 0 (fixed)                                                |
| Cool\_stg2\_1 | 0 (fixed)                                                |
| Fan\_1        | 1 (fixed)                                                |
| Heat\_stg1\_1 | 1 (fixed)                                                |
| Heat\_stg2\_1 | 1 (fixed)                                                |
| Solar\_1      | 2.6737e-14 +/- 6.0411e-15 (22.59%) (init = 5.551115e-15) |
| Fan\_infil\_1 | 0 (fixed)                                                |
| U\_ext\_1     | 2140.45885 +/- 18.4987996 (0.86%) (init = 2160.907)      |
| C\_2          | 1.3863e+08 +/- 1638664.16 (1.18%) (init = 1.372595e+08)  |
| Cool\_stg1\_2 | 0 (fixed)                                                |
| Cool\_stg2\_2 | 0 (fixed)                                                |
| Fan\_2        | 1 (fixed)                                                |
| Heat\_stg1\_2 | 1 (fixed)                                                |
| Heat\_stg2\_2 | 1 (fixed)                                                |
| Fan\_infil\_2 | 0 (fixed)                                                |
| U\_ext\_2     | 566.862843 +/- 17.1910143 (3.03%) (init = 537.9736)      |
| U\_1\_2       | 9987.51108 +/- 42.7019031 (0.43%) (init = 9999.988)      |
| C\_3          | 4.6985e+08 +/- 13739384.4 (2.92%) (init = 4.510568e+08)  |
| Cool\_stg1\_3 | 0 (fixed)                                                |
| Cool\_stg2\_3 | 0 (fixed)                                                |
| Fan\_3        | 1 (fixed)                                                |
| Heat\_stg1\_3 | 1 (fixed)                                                |
| Heat\_stg2\_3 | 1 (fixed)                                                |
| Fan\_infil\_3 | 0 (fixed)                                                |
| U\_ext\_3     | 50.6552266 +/- 1.01994897 (2.01%) (init = 50)            |
| U\_1\_3       | 8386.80542 +/- 190.305523 (2.27%) (init = 8535.802)      |
| U\_2\_3       | 9985.03941 +/- 124.989181 (1.25%) (init = 10000)         |
| IntLoad\_1    | 27400 (fixed)                                            |
| IntLoad\_2    | 76500 (fixed)                                            |
| IntLoad\_3    | 1500 (fixed)                                             |

<a id="orgec9d9e2"></a>

../attachments/emcee_plot.png
caption="Figure 4: Building 271 MCMC Posterior

## <span class="section-num">2</span> Convex optimization MPC {#convex-optimization-mpc}

Linear models fit nicely into convex MPC. This is basically my thesis.

### <span class="section-num">2.1</span> So far&#x2026; {#so-far-and-x2026}

I started writing the MPC formulation, but since this is a POC, I didn't put too
much thinking on making this generalized for any RTU-type building. Not too
difficult to do it, but let's see if this actually works first.

This is largely inspired by [this](https://colab.research.google.com/github/cvxgrp/cvx%5Fshort%5Fcourse/blob/master/intro/control.ipynb) example, but I've modified comfort constraints
to be a bit more flexible by utilizing a slack variable. I've put in some
commented code for how the actions come in; haven't tested this since I'm still
working on the modeling.

The objective function here is to minimize ON toggled states. I will talk to
Marion to better integrate PowerKit here and also to set the limits and steps of
all the actions and their nominal powers. Again, this is a POC so I've put those
in manually.

```python
@timer
def run_mpc_step(matrices, features, opti_settings={}):
    import cvxpy as cp

    A, B, C = matrices
    X, U, W = features
    nN, nM, nL = A.shape[1], B.shape[1], C.shape[1]

    ct, ph = opti_settings['ct'], opti_settings['ph']

    x = cp.Variable((nN, ph+1))
    u = cp.Variable((nM, ph))
    w = W[ct:ct+ph,]

    s_comfort = cp.Variable(ph)

    obj = cp.sum(u, axis=0)

    cost = 0
    constr = constraints = []
    for t in range(ph): cons.append(x[:,t+1] == A @ x[:,t] + B @ u[:,t] + C @ w[:,t],)
    cons.append(x[:,0] == X[ct,])
    cons.append(x[:,1:] >= Tint_min[ct+1:ct+ph+1] - s_comfort)
    cons.append(x[:,1:] <= Tint_max[ct+1:ct+ph+1] + s_comfort)
    cons.append(s_comfort >= 0,)
    cons.append(cp.sum(s_comfort)/st <= comfort_budget,)  # st = steps/hour

    # add constraints for U's
    # add constraint that stg 2 can't happen without stg 1 and can't happen without fan; ditto cooling
    # add constraint that at least 1 fan has to be on when occupied

    '''
    # Creates a 10-vector constrained to have boolean valued entries.
    x = cp.Variable(10, boolean=True)

    # expr1 must be boolean valued.
    constr1 = (expr1 == x)

    # Creates a 5 by 7 matrix constrained to have integer valued entries.
    Z = cp.Variable((5, 7), integer=True)

    # expr2 must be integer valued.
    constr2 = (expr2 == Z)

    problem.solve(solver=cp.ECOS_BB, verbose=True)
    '''

    constraints.extend(cons)

    problem = cp.Problem(obj, constraints)
    problem.solve(solver=cp.ECOS, verbose=True)

    return x, u, s_comfort # problem.cost
```

### <span class="section-num">2.2</span> Are we really convex? {#are-we-really-convex}

Is our problem really convex? If we add in occupancy models, are they dynamic
based on the actions taken? If yes, then we may no longer be convex, else, we
are. The actions are mostly discrete, so we may need a mixed-integer solver.
[CVXPY](https://www.cvxpy.org/tutorial/advanced/index.html) documents how to do it and which solver interfaces are available.

```python
>>> import cvxpy
>>> print(cvxpy.installed_solvers())
['ECOS', 'ECOS_BB', 'OSQP', 'SCS']
```

[ECOS\_BB](https://github.com/embotech/ecos#mixed-integer-socps-ecos%5Fbb) is not a high-performance solver however, might not work with large
problems = 1000? 10000 variables?

Alternatives (commercial licenses):

- [CBC](https://projects.coin-or.org/Cbc)
- [GLPK\_MI](https://www.gnu.org/software/glpk/)
- [CPLEX](https://www-01.ibm.com/software/commerce/optimization/cplex-optimizer/)
- [GUROBI](http://www.gurobi.com/)
- [MOSEK\*](https://www.mosek.com/)

Greater alternative would be to use meta-heuristic optimization like genetic
algorithms, particle swarm, firefly, brute-force, and so on.

## <span class="section-num">3</span> <code>[0/3]</code> A list of TODOs {#a-list-of-todos}

### <span class="org-todo todo TODO">TODO</span> <span class="section-num">3.1</span> Improve and check model {#improve-and-check-model}

- Resample
- Add features
- Add time feature
- Are nominal powers OK?

### <span class="org-todo todo TODO">TODO</span> <span class="section-num">3.2</span> Test MPC with dummy cost function {#test-mpc-with-dummy-cost-function}

- See if this runs
- Results look okay?

### <span class="org-todo todo TODO">TODO</span> <span class="section-num">3.3</span> Test MPC with modified constraints {#test-mpc-with-modified-constraints}

- Vary setpoints
- Add toggle penalty
- Add temperature rate of change penalty
- 1 fan always ON per day; rotate daily -> handle this in MPC or outside?
