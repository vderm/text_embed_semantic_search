---
author: Vasken Dermardiros
categories: note
date: September 26 2022
tags:
- research
- collaboration
- mila
- autobot
title: "BBAI-MILA: NODE Myriad"
---

# MILA Interactive Visit Kickoff

Persons present:

+ Annie-Shan Morin
+ Pierre-Luc Bacon
+ Niki Howe
+ Vasken Dermardiros
+ Ysael Desage

## NODE Control

+ Direction

## EnergyPlus

+ Need a configuration
+ Control of a multi-zone system

## How can we provide explanation?

+ Cris Olah
+ Reward hacking? -> bad things happen you optimize the wrong thing -> human preferences?
+ Reward is compressed -> contraints MPD

# October 31, 2022

Persons present:

+ Annie-Shan Morin
+ Pierre-Luc Bacon
+ Vincent Taboga
+ ... prof from Poly
+ Vasken Dermardiros
+ Ysael Desage

+ Pierre-Luc support Vincent for RL
+ Vincent's method now: randomized shooting + recurring state-space model
  + States: temp, power, weather, ~10-15 features
  + $\delta$: setpoint change, bound by $M$
  + high-level control ships max power requirement, low-level tried to come up with SP schedule to meet that bound
  + Pierre-Luc wants: Optimize trajectory w/ grad descent
+ Incorporate to Myriad -> help by Niki and Simon

Links shared:

+ <https://darl-workshop.github.io/>
+ <https://arxiv.org/abs/1810.13400>
+ <https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/admm.pdf>

# November 14, 2022

Persons present:

+ Pierre-Luc Bacon
+ Vincent Taboga
+ Hanane Dagdougui
+ Vasken Dermardiros

Neural ODE in JaX and got the EnergyPlus stuff working :)

Trained on 3-6 months.

PLB: use ODE-int instead of euler_integrade -> better than RK4, uses adaptive step-size, implements continuous adjoint

+ Incorporate temperature information -> observation at different intervals

Trying to prediction power and interior temperature.

PLB: have you closed the loop?

Ubuntu 20.04 + python 3.10

# November 28, 2022

Persons present:

+ Pierre-Luc Bacon
+ Vincent Taboga
+ Vasken Dermardiros

Step size controller is funky; PID can be funky too.

The objective of the HVAC controller would be to minimize the operating cost over a time period:

$$ \min ~~ cost = \textrm{\$/kW}*\|power(u)\|_\infty + \textrm{\$/kWh}*\sum (power(u)* \Delta t) $$

The mapping from controllable inputs $u$

I'll start by saying that I'm assuming you'd want to control the HVAC heating/cooling states. If instead you want to control the setpoints, some of the following will need to be updated.

Your HVAC controller's objective would be to minimize the operational cost over a small time period, e.g. peak power *$/kW + energy use in period* $/kWh, while satisfying comfort, equipment and other constraints.

The system dynamics are expressed using the system of differential equations which may or may not rely on physics. Can be a neural net, can be an RC circuit, can be an RC circuit with a neural net only for the known unknowns (for example, depends only on time features and would be predicting the residuals which might be caused by internal loads, solar gains, etc.). Regardless, these would all be predicting the change of temperature in the various spaces.

What are the inputs to these models? Space temperatures (past), HVAC heating/cooling/fan states (past and future), exterior temperature (past and forecast), (maybe) solar radiation (past and forecast), (maybe) time features (careful as the model might just learn the occupancy schedule), and perhaps other features.

The HVAC heating/cooling/fan states are a function of the basic HVAC controller. It's probably an ON/OFF controller that will turn ON the heating if the space temperature is below the heating setpoint - a deadband, and turn it OFF if the temperature if above the heating setpoint + a deadband. Or, you might have just one setpoint and the heating turns ON if the temperature is below this setpoint - a deadband. Cooling can turn ON if the temperature if above this setpoint + a deadband. The setpoints can be different when the space is occupied or unoccupied. Hope this part is clear. Of course, your idea is to try to beat this strategy.

What I'm getting at is that make sure to keep in mind what drives what. We want a room to be at 22 degC, so we put the room temperature setpoint to 22 degC. If the current room temperature is 20 degC, because it's lower than the setpoint, the heating turns ON. The injection of heat into the space drives up its temperature until it reaches the desired temperature. You want to make sure that your model can go from heating states to change in temperature (dT/dt). If you instead use setpoints as the input, then the model is also learning the logic of the underlying controller. (If that's what you wanted to do, that's a different story, and then it would make sense to also predict the HVAC states and even power.)

And now the last part, how to go from HVAC heating/cooling/fan states to power. The mapping is either a linear relationship like: total_hvac_power_electrical = heating_state *heating_power_electrical + cooling_state* cooling_power_electrical + fan_state *fan_power_electrical; or it can be something that depends on exterior temperature: total_hvac_power_electrical = heating_state* heating_power_electrical(T_exterior) + cooling_state *cooling_power_electrical(T_exterior) + fan_state* fan_power_electrical. Try with a linear regression to fit this sort of model.

If heating is by gas, then the cost of heating would use $/m^3 of gas factors instead of electrical factors.

# November 29, 2022
Presentation of Vincent Taboga's thesis. Grid optimization via HVAC. (Didn't paste those slides here)

Pierre-Luc said that Yoshua hired a post-doc to work on building decarbonization.

![Proposed Approach](../attachments/2022-11-29-11-28-27.png)

![Centralized Problem Formulation](../attachments/2022-11-29-11-30-25.png)

![Centralized Problem Formulation 2](../attachments/2022-11-29-11-39-47.png)

![Centralized Problem Formulation 3](../attachments/2022-11-29-11-42-01.png)

![ADMM](../attachments/2022-11-29-11-43-47.png)

ADMM works very well in convex problems; works also in non-convex settings but no real proofs...

![ADMM algorithm](../attachments/2022-11-29-11-47-19.png)

![PlaNet](../attachments/2022-11-29-11-55-16.png)

Dreamer is the paper that came after.
+ PlaNet: https://ai.googleblog.com/2019/02/introducing-planet-deep-planning.html
+ Dreamer: https://ai.googleblog.com/2020/03/introducing-dreamer-scalable.html?m=1
+ Dreamer v2: https://ai.googleblog.com/2021/02/mastering-atari-with-discrete-world.html

Works well for apartments that it has not seen before.

![Results on Demand Response Events](../attachments/2022-11-29-11-57-55.png)

![Future Research](../attachments/2022-11-29-11-59-15.png)

# January 9, 2023

Persons present:

+ Pierre-Luc Bacon
+ Vincent Taboga
+ Vasken Dermardiros

Hanane part of Mila now.

If MPC -> linearize over the near term -> try ILQR (iterative LQR)

Newton's method more brittle when there's noise

# March 7, 2023

Dockerfile for EnergyPlus for Vincent
