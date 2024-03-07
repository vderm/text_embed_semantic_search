---
author: Vasken Dermardiros
categories: note
tags:
- prod
title: Containerization
---


About containerization in general. More extensive work coming closer to summer. Very useful to be used in calvin and [[clearml]]!

Originally spoke on 2021-05-31.

## Advantages

+ Reducing cost: right now, we reserve resources and within this reserved resources, we pay the whole thing
  + If you request a VM with 16 cores but only use 2 cores normally; we're wasting a lot of resources!
  + As a container, the service is ran when needed and terminated after: save money since don't need to reserve a resource
+ Maintainability: package versioning set within a container
+ Automate versioning: use `latest` for container or a specific image commit
  + kubernetes is what does the version management, load balancing, problem resolution, really tries to not let stuff go down
+ User management: pain in the ass with VMs
  + Easier to handle with group management in AWS

## Difficulties

+ Applications must be stateless -> everything has to be inside an encapsulated capsule, so that when a container goes down, it can be replaced immediately
  + There's a way of maintaining states via sessions; persistence
  + User dashboard is an example where a state needs to be maintained -> keep where the client was at
+ Packages to containerize need to be *mature*!
  + Advantage of a VM: you can have the whole thing running

## How do you design what goes on a container?

+ Farzam: One for algo, one for ... one for a building?
+ Naveen: Each service is a container. So yes, one per algo, per this, per building...
  + Logfiles logged completely. Path might be different.
  + Need to go over the data pipeline, document it, catalogue it, does one service need another service to run? What are the dependencies?

## Heading towards an event-driven approach

+ Container is sleeping until data comes in
+ Moving towards an event-driven framework truly vs a schedule-based approach

## Work to be done on the AI side

+ **think of what we're going to do with Haystack**
+ Mostly, ControlKit needs to be broken down?
+ How do containers talk to each other?
  + Through a sort of API: so the one asking doesn't care who answered, as long as it's answered
+ ControlKit as a REST API

+ **David to draw a diagram of new pipeline**
+ **Naveen thinks that putting/splitting ControlKit into containers would be the best place to start!**

## Data Flow from David from 2021-06-03

Control Kit:
Inputs:

1. Data from the building,
2. State of the building from config file
3. LEO State
Outputs:
1. Command to the building, state of the data to visualization tools (like Mission Control)
** Note that CK is taking its state from the building satellite table. The way it is setup now, it keeps in memory all (or pretty much all) the information it needs. There are also some pickle files that are saved to be re-loaded later. Each cycle of execution takes about 5 minutes to be completed, but there are some sleep times between the processes. They can last from 2 seconds to 2 minutes depending on the state.

MASTER:
Inputs:

1. Building Kit objects (config + systems)
2. Building Satellite object (Representation of Control Kit)
3. Path where running
From the path, obtains the information from LEO to run or not the algorithms.

Outputs:

1. Commands sent to the building.

Building Kit:
Inputs:

1. Configuration file
2. Path where running
3. Building Dataframe (from the data module) + Weather DataFrame

Outputs:

1. Configuration in object format
2. System object
3. Weather data in form of object

Optimus Prime & other Algos:
Inputs:

1. Building Kit objects (config + systems)
2. Building Console object (Representation of Control Kit)
3. Optional: Other algorithms state

Outputs:

1. Commands to be transformed into DF format for Control Kit.

## Data Flow from David and Saeid from 2021-06-04

1. So, am I getting right that when we are fully migrated to CK, all the existing HVAC algos (OP, Master, etc.) will be run as tasks executed by CK as opposed to standalone services?

+ There are still the water side algorithms that are not in Control Kit (at least for now). They are running using the same instance of Master. In that case, Master is the service running them. Same input outputs, except Master sends the commands directly to the building.

2. When you mention the files being created to keep track of the status, what happens if those files are lost? Does that incur an initiation phase to get the info again or will it cause malfunction?

+ Some files will cause a crash, others should simply not be deleted. For example, there is a file that saves the previous occupied set point. That one should not be deleted. Other files are the status of the systems to keep track if they were released or not. That one should also not be deleted to avoid sending repetitive commands to the writer.

3. Is my assumption right that the only risk to restart CK is to have the reloading of configs and that 7 days of data?

+ I think that is the only risk yes, but to do that, we would probably need to re-visit the time module. That one is responsible to make sure we run every 5 minutes and that there are specific times for each process. A restart would probably reset it. There is also the MC question. Not sure if they can use it if the service is off. Redis is also an option as Farzam mentioned.

[//begin]: # "Autogenerated link references for markdown compatibility"
[clearml]: clearml.md "ClearML"
[//end]: # "Autogenerated link references"