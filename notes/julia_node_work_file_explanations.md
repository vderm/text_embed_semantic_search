---
author: Vasken Dermardiros
categories: note
tags:
- brainbox
- journal
title: Julia NODE work file explanations
---

# Julia
the clean part of the approach is what I have to run on clearml : https://git.brainboxai.net/cogitamus/Explore_Julia/-/tree/master/UODE_RTU_pred/clearml

it has the prep data in python and calling predict and train from julia

the julia script is much cleaner and lighter with only the libraries being used

https://git.brainboxai.net/cogitamus/Explore_Julia/-/blob/master/UODE_RTU_pred/clearml/NODE_RTU_pred.jl

for the tests/research part I use this julia script:https://git.brainboxai.net/cogitamus/Explore_Julia/-/blob/master/simple_test.jl
which has more libraries and needs some cleaning

## model in simple_test.jl
+ simple_dynamics: train T_asymptote and t_inv_ext
+ dynamics_hvac: freeze T_asymptote and t_inv_ext, and learn hvac params
+ dynamics_all: same as dynamics_hvac + black box model
+ Flux.destructure -> recreate model

## UODE_RTU_pred/clearml/NODE_RTU_pred.jl
+ closest to production
+ python takes care of everything except training the model

## DP_controller.py
+ using NOMAD to run an optimization routine on the model

## Load/extract parameters
+ julia functions available to do there in NODE_RTU_pred.jl
+ load_params, merge_params, extract_params
+ python wrapper for those

## tuneable parameters
+ put variables into `[]` to make them tunable?
+ <https://fluxml.ai/Flux.jl/stable/models/advanced/>
+ loss(theta): theta are the parameters, p are somehow fixed
+ Optimization to train the model, using NelderMead()
+ ADAM is in OptimizationFlux