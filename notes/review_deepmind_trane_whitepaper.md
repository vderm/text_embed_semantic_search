---
author: Vasken Dermardiros
categories: note
tags:
- brainbox
- review
title: Review of DeepMind and Trane whitepaper
links: https://www.deepmind.com/publications/controlling-commercial-cooling-systems-using-reinforcement-learning
---

*(as sent as an email to Josh, Omar, and friends on November 30, 2022)*

Hello,

First, thanks Josh for sharing this white paper. I recognized a few of the Trane people in the author list.

Second, DeepMind authors admitted that no off-the-shelf approach worked and a lot of domain expertise was needed to get this to run and often times the method did not produce any valid actions. At the end, they were still able to save some energy.

Trane did have to modify some of its software to make them “AI ready” and I wonder if they’ll allow others to provide overrides to their secret Sequence of Operations (SOO). Perhaps this is a good thing since we no longer need to do that work.

When it comes to the modeling, they’re using a neural network (no physics) to go from observations to action values. Basically, if you’re in a certain state (water temperature is X, OAT is Y, load is Z, etc), what would be the value of doing a certain action? How much energy would cost me to (a) turn on another chiller, (b) reduce the supply temperature, etc. And by having a value attributed to all these actions, one would pick the least cost. Except that this doesn’t always handle constraints, so what they did is to then prune out actions that violate constraints and apply the best action from the pruned set. If there’s nothing left: release.

The problem they faces is that their historical data was basically doing the same thing following deterministic rules. Although they had a fair amount of data, the data had very little variance. Because of this, the model was not able to properly attribute an action to what would be its energy use. Since some pumps were always ON, turning them OFF did not predict a decrease in energy use. To go around this, they had to hand-pick their inputs, do some feature engineering (e.g. instead of having pump flowrates and temperatures, to convert them in heat flux; I don’t know if they did this, but I’m guessing they did something like this; or maybe use pump affinity laws?). This is a typical problem I see in papers by non-experts, they tend to use all the data without understanding what drives what.

Besides feature engineering, they played around with the model architecture (Figure 2) which isn’t particularly particular. To get some uncertainties from the model part, they trained a few of these in parallel and so are able to get multiple predictions (1 per model and then calculate an average across). We’ve done something similar in the past by keeping dropout layers active during inference (talk to Fahimeh if you want to learn more).

What I liked is that they modified the typical reinforcement learning (RL) value function (the function that says “given you are here, what is the value of taking the next action”) so that it’s more relatable to building operators. Instead of reporting a discounted future return, they are reporting an energy use over a time horizon. That’s nice since they’d eventually want the building operator to be comfortable with the algo.

Some of the other challenges are starting to be specific to the plants: sensor drift, lockout period, chiller staging order, etc. Those are nice lessons, but not much we can do about them.

Should we be afraid/concerned? So-so. It’s still preliminary work and a case study during the shoulder season, but the ML community is realizing that you can’t just plug it in and off it goes; you need to understand the problem/domain. On the flip side, many ML/RL tools and libraries are becoming easier and easier to use. Engineers will be able to get good results. However, to be able to mass-deploy these algorithms, you will need software engineers and perhaps hardware folks too, and this is somewhat of a rare mix. Then again, there are 20’000 ex-Meta, ex-Amazon, ex-Twitter, ex-… getting bored and hearing about “building decarbonization” and seeing how the narcissist Adam Neumann’s vapourware carbon credit company is already valued >$1bil…

Let me know if you’d want to discuss this white paper further…