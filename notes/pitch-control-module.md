---
author:
- Vasken Dermardiros
date: TBD
categories: pitch
tags:
- controlkit
- clearml
- module-control
- organizing
- pitch-unshaped
title: Control Module Pitch
subtitle: On and Off
titlepage: true
titlepage-rule-color: da3737
titlepage-text-color: da3737
toc: false
urlcolor: red
links:
- [[pitch-predicition-module-interface]]
- [[fastapi_standard_and_helper]]
---


# Problem
> The raw idea, a use case, or something we’ve seen that motivates us to work on this


## Background
Unlike ControlKit 1.0, ControlKit 2.0 is based on FastAPI and running the "main loop" is actually a single call.

![FastAPI Endpoints](../attachments/2022-03-07-17-16-27.png)

How does it work? Quite simply, a call is made to the ControlKit endpoint which runs a few sequential processes. It starts by getting and compiling the data, passes it to the ControlModule (algos), get back a sequence of controls, maybe passes that to the PredictionModule, gets predictions, passes it to the SafetyModule which will confirm if all is good and then pushes this to the proposed controls database (we may not write all the commands all the time). The process reads specific settings from the ConfigModule along the way as required.

![OLD Draft of ControlKit 2.0 and 3.0](../attachments/2022-03-07-17-12-26.png)

The difference between ControlKit 2.0 and 3.0 is that 3.0 is event-based where each phase or action is completely independant of the former. Each time an action is complete, the action would broadcast this state where some subscribed module(s) may pick it up from there. This is much trickier to orchestrate and we don't have the infrastructure now to do things like this. Would require a much tighter integration with DataStreams and full Kubernetes (k8s) deployment.

Lastly, so what's the trigger? It is a script that checks the `extraction_cycles` table for new data and once satisfied makes the call. Down the line, we may have the edge device itself make this call when it sees that its `tape` is either running out or the predictions are diverging. The `tape` is the two-or-more-hours of predictions and controls that will be sent to the edge device which will then write to the building one after the other. Alternately, the `tape` may be a decision tree that is updated regularly.

This API and triggered approach solves the data synchonizing issue and allows to have different versions or setups of ControlKit running for a given building in parallel. It allows to run a staging version of ControlKit in "virtual mode" which could be swapped into "control mode" for a short while. This simplifies our rollout strategy. We may also have a certain configuration used for special cases such as demand response or have specific algos running, and so on. This would reduce the need to develop a multi-control module.

![Trigger to call ControlKit endpoint](../attachments/2022-03-07-17-13-03.png)

## Main Problem
TODO

# Appetite
> How much time we want to spend and how that constrains the solution

Time budget: six weeks starting **?? May, 2022**.

Solution is to ...


# Solution
> The core elements we came up with, presented in a form that’s easy for people to immediately understand


# Rabbit Holes
> Details about the solution worth calling out to avoid problems


# No-Gos
> Anything specifically excluded from the concept: functionality or use cases we intentionally aren’t covering to fit the appetite or make the problem tractable


# Notes that helped shape this pitch
> These are notes and not deliverables!

##  Chat with Marc-Olivier on Apr 5, 2022
Link to Confluence: https://brainboxai.atlassian.net/wiki/spaces/ALGO/pages/427753497/Ideas+for+a+simpler+and+improved+BK

Main points for our side:
+ Algos going towards objects per systems. Basically, an AHU is an object with properties -- last value, point_ids, etc. -- which also has children like coils, that themselves have properties.
+ Building area or HVAC equipment can have multiple “algo” (or controller) registered on them,
+ All configuration should be retrieved from an interface (internal module for now) to make it easier to integrate with a company-wide Config service (relying on FastAPI)
+ Algo relies on a local database but will accept receiving a dataframe or JSON

Spoke about the `control_zone_id`, they are thinking of using `building_area` but it's not finalized yet.

Can be a string like `AHU_1_v1` for the first setup of AHU 1. If the building is remodelled, we can increment the version like `AHU_1_v2`.

**Whatever the case, the underlying points must not change!**

Cache database vs JSON -> go with JSON since it's simpler. Message size shouldn't be a huge concern for now.