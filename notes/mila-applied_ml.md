---
author: Vasken Dermardiros
categories: note
date: Feb 21, 2023
tags:
- research
- collaboration
- mila
title: "BBAI-MILA: Applied Research Project in Distributed Learning"
---

# 2023 02 21
Persons present:
+ Annie-Shan Morin
+ Gaetan Marceau Caron
+ Alexia Corcoran
+ Vasken Dermardiros
+ Mathieu Le Cam

## Email from Gaetan
The first step of the project is to set up the experimental platform that will simulate your infrastructure. I see multiple components to this platform:
+ the calibrated simulators generating the data for the 200 buildings,
+ the communication layer between the buildings and the server for training models,
+ the storage of the data capturing the constraints that the data of some clients cannot be mixed with the data of other clients,
+ the models being fine-tuned with the incoming data,
+ the performance indicators measuring prediction accuracy (e.g., MAE) and communication cost,
+ the optimization strategy to balance accuracy and communication cost (e.g., federated learning).

The project is quite ambitious.

Do you happen to have existing work concerning these components, or do we start from scratch? If we start from scratch, we need a software engineer to design an architecture so that the platform is efficient for running experiments: it should be fast (parallel?) so that the computation costs are not too high. Some people in my team have the experience to do this, but could your experts do this task since it depends on your domain expertise?

The other point concerns the calibration of the simulators.
Do you have an existing model of the buildings we want to simulate?
If so, I'd like to know more about your calibration process.

It doesn't need to be perfect for this project since you will use real data after implementing our recommendations from simulations. It is not like an RL problem, where the trained model in simulation needs to generalize to the real-world (i.e., reality gap). Am I right?
Also, do we want to use real-world or only simulated data in the platform?

Finally, I need to double-check, but do we need the building simulators at all?
Can we do the optimization process only on real data?
If we have enough data, we could simulate the communication layers and train our models by considering the storage constraints.

Finally, I found this paper from DeepMind with Trane: [Controlling Commercial Cooling Systems Using Reinforcement Learning](https://arxiv.org/pdf/2211.07357.pdf). The problem is different, but I would like to know your opinion on their work. I'm quite surprised they could handle the exploration/exploitation dilemma on the real system without needing a simulator.

## Discussion with Mathieu
+ Go straight into the controls problem
+ Building with missing data
+ Want to control all of them
+ Can use simulator but we are collecting quite a bit

## Gaetan notes / conversation
+ Replay building process -> no need for simulation
+ communication cost isn't an issue
+ the models being fine-tuned with the incoming data -> new building online with very little data

+ the performance indicators measuring prediction accuracy (e.g., MAE) and communication cost,
+ the optimization strategy to balance accuracy and communication cost (e.g., federated learning).

## Next step
+ More into the data -> small snapshot

# Email from Gaetan Caron
+ Inputs:
  + controllable binary inputs: past (has happened) + future (optimizer proposes)
  + weather: past + future
  + time features: past + future
  + space temperature: past
  + meta-data? -> how will the model know from which building this data is from?
  + _missing values_
+ Output:
  + space temperature: future
  + power? -> can also be estimated with virtual meters
+ Although we spoke about SleepCountry that has 1-4 zones, we do have other clients with 30-40 zones. Very much the same settings, just a larger store, e.g. Walmart.

What is the goal of predicting the temperature in the following two hours? How do you use this prediction afterward?
> Model to be used to drive control decisions that will minimize a cost. Cost can be energy, power, $, comfort and/or others and/or a combination of all above.
> Constraint to comfort, equipment capacity, equipment cycling, rate of change of temperature
> Ideally using a form of differentiable controls, or training a controller using RL, or extract a decision tree that can run on the edge
> Can have a shared "core" with specific/specialized "heads" per building
> How do we pool the data of various SleepCountries together? What about other buildings?
> Doesn't need to be 2 hours, can be longer -> depends on the planning horizon we want. We can decide to have a coarse planning horizon and a more refined control horizon.
> > We do sometimes observe buildings that are very quick acting -> heating ON for 5 minutes yields a large temperature swing

What are your performance metrics (MAE)?
> For temperature prediction: MAE, MSE, RMSE, NMBE, CV(RMSE), ... and weighing can also change given horizon and/or size of zone

For the goal described previously, what are your requirements in terms of errors?
> Errors are okay, but what matters is to assure the model output has a strong sensitivity to the HVAC controls (heating, cooling)
> We do just use RMSE -> temperature sensors are +/- 0.5 degC, so if the predictions are within this range, then there's no reason to be better
> It also has to be linked with human comfort... if the error causes discomfort (human perception isn't linear)
> Any averaged metric might miss the extremes

This question is important because we predict the temperature in a controlled environment. Just predicting the average value of the past 30min. (blue curve) if the target (orange curve) is constant could be a strong baseline (probably MAE<2 Celsius for the left or the right part of the figure).
> We will write to the HVAC system directly
> What we see in the curve is how the system currently works (using an ON-OFF or Bang-bang controller). Given the setpoint (orange curve), the HVAC system tries to have the room temperature (blue curve) as close as possible by turning on the heating when this value is below the "setpoint - 0.5", and turns OFF when the temperature surpasses "setpoint + 0.5". (The 0.5 is a deadband. This explanation is for the system in heating mode.)
> We think we can do better than this ON-OFF controller by directly writing to the system directly.

The tricky part concerns the transition between 9h30 and 11h30; we need to know that the target changes to predict well.
> We're not sure which day this is on.
> Typically, the setpoints are relaxed in unoccupied periods to reduce energy use. However, there's no guarantee that this strategy will yield a minimal cost since there are peak power charges in the utility tariff.
> The limitations of most HVAC controllers is that they are unaware of the utility rate structure.

I think we need to make the hypothesis about the target temperature for the following 2 hours explicit, maybe as an input of the temperature model, which another model predicts.
> The optimal controller would drive the controls, no need for setpoints.

This is equivalent to using a conditional model to get different predictions for different hypotheses about the target temperature. Do you think it makes sense?
> See above.

For the data inventory in the project prerequisites of the SoW, you will give us access to the data specified in the readme file you shared for 200 similar buildings.
> At least 100, not all 200 buildings fully mapped yet.
> We do have other portfolios with similar systems with more zones.

For the data you shared, it is about five months except for building 391, which has a lot of missing values and outliers (around 29 Celsius at the end): Is five months the maximum duration? How many buildings among the 200 have almost no missing values over a significant period (1 month?)
> We expect a few hours of missing data per month. The building with 1 month missing is more of an exception.
> That said however, in non-SleepCountry buildings, we do expect many more faulty sensors. We replaced the sensors/thermostats in SleepCountry as part of our contract with them.
> These types of buildings are large open-spaces. The temperatures across the building tend to be around the same.