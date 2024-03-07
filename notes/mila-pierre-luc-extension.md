---
author: Vasken Dermardiros
categories: note
date: March 7, 2023
tags:
- research
- collaboration
- mila
title: "BBAI-MILA: Extension with Pierre-Luc"
---

# Safety in Controls (handling uncertainties) – Extension to NODE Project w/ Pierre-Luc Bacon
## Description of the project
A Lyapunov function is a mathematical function that that measures the "energy" or "stability" of a dynamical system. It has the particular property that its value decreases over time as the system evolves toward a stable equilibrium point. Lyapunov theory has a long history in nonlinear control theory, and researchers have used it for both controller synthesis and verification. However, much of this work is analytical and only applies to simple domains. Neural Lyapunov functions address this challenge by adopting a data-driven approach to learn functions with Lyapunov-like properties from observations of a nonlinear dynamical system.
Using neural Lyapunov functions in HVAC control systems is particularly well-suited to stabilization problems, which involve ensuring that a system moves towards a stable equilibrium point. HVAC control is a natural fit for the Lyapunov framework because it consists in maintaining the desired temperature, the stable equilibrium point of a complicated nonlinear dynamical system. We plan to build on Chang et al. (2020) to synthesize stable neural network controllers and accompanying "safety certificates." For example, this safety certificate could be used to establish that the total power consumption will never exceed a given maximum value while ensuring sufficient comfort for the building occupants.
We will also propose several theoretical improvements to the method of Chang et al. (2020), namely: compute the lie derivative efficiently through a combination of forward and reverse mode automatic differentiation, improve the Monte Carlo sampling method through either adaptive importance sampling or kernel embedding of the candidate Lyapunov functions (akin to Gretton et al. (2010)), and replace the SAT-based post-processing by a high probably confidence bound using concentration inequalities.

## Your data (amount, amount annotated, right to share it with Mila for a project)
We will use Energyplus and synthetic models. No data from BrainboxAI will be shared with the Mila team.

## The work done so far by your team on this project
My PhD student Aneri Muni has started working on Neural Lyapunov functions. So far, she has only been trying to reproduce the original paper. Our goal was then to build a “funnel”/LQR Tree-like extension. We may re-direct those research goals to be more in-line with this project.

# Sim 2 Real – Extension to NODE Project w/ Pierre-Luc Bacon
## Description of the project
This project aims to accelerate the deployment of a controller to a new building by learning general-purpose models, trained in simulation and fined-tuned on real-world data to improve its performance, resulting in a more accurate and robust optimal control policy. We would use a similar methodology as that of robotics. For example, a simplified unmanned aerial vehicle (UAV) model is used to bootstrap learning and is then fined-tuned in the real world to capture ground effects, which is a complicated nonlinear phenomenon depending on many dynamic factors. These simplified models are typically easy to identify and stabilize, for example, by assuming a "point mass" model with no rotational dynamics, by fail short of sufficient robustness for direct real-world deployments.
The same story holds in the HVAC control setting, where RC models play the role of "point mass" models in the UAV setting. RC models represent the system's thermal behaviour using a set of linear differential equations that relate the system's temperature to the inputs and outputs of the HVAC system. The underlying assumption here is that the thermal properties of the materials in the system do not change with time and that the heat transfer dynamics within the system are linear: a linear time-invariant system (LTI). While this model can explain the building dynamics at a coarser level, it needs more expressivity to capture the nonlinear dynamics arising from the interaction of interdependent subsystems and that of the building and its occupants. We propose addressing this challenge by taking inspiration from advances in sim2real and model-based RL. Specifically: 1. use data augmentation and randomization to learn a more robust controller in simulation based on RC models 2. learn a "residual" non-linear neural ODE to account for the unmodeled dynamics at deployment time and fine-tune the learned controller on this model.

## Your data (amount, amount annotated, right to share it with Mila for a project)
We will use Energyplus and synthetic models. No data from BrainboxAI will be shared with the Mila team.

## The work done so far by your team on this project
We would piggyback on Vincent Toboga’s work on optimal control Neural CDEs. Vincent's work is reminiscent of Dreamer V3 and SPR, which uses a latent model of the dynamics and data augmentation in a self-supervised fashion to address the distribution shift problem in model-based RL. Aneri Muni (see above project) has also written her Msc thesis at ETHZ on the problem of sim2real for quadcopters using bayesian optimization. Her expertise would also be relevant for this project.