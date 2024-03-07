---
author: Vasken Dermardiros
categories: note
date: August 1, 2022
tags:
- research
- collaboration
- mila
- autobot
title: "BBAI-MILA: Autobot"
---

# MILA Interactive Visit Kickoff
Persons present:
+ Bruno Rousseau: condense matter physics
+ Sonia Yousfi: worked on AI since 2011, industrial project: communication, autonomous vehicles, solar energy
+ Claude Demers-Belanger
+ Vasken Dermardiros


## High Level
+ Meet weekly for 4 months ideally on Mondays
+ Client: provide a weekly summary
+ Project report to update periodically
+ Purpose: all aligned, continuous progress
+ Useful report for new collegue and so on -> bootstrap to new project/continuation
+ Template: Google Docs / shared
+ First few meetings: get a protocol (BBAI implements, MILA is a sound board / suggestions, MILA will not code)
+ Can only give 30 hours (Sonia's time is free)
+ Two checkpoints:
  + 10 hours: review with colleague (person's time counts)
  + End of project: review, if it went well or not
+ Bruno will be on vacation end of August for 3 weeks -> interaction will go to December


## Scientific Topic
+ Bruno: 2 sequential data: name (sequential characters), 2 weeks of data
  + Output: categories
+ Concatenate the encoded vectors -> representation vector
+ Vector to yes/no per label
  + Labels are not independent -> sensor vs actuator
  + Nothing preventing to predict inconsistent behaviours

+ Correlated labels:: structured output

Tree based approach:
+ Am I a sensor? Am I a SP? Am I a command?
+ Goal is to predict a node in the tree
+ Could not predict inconsistent output (limited by the structure of the model)

Can we build a model that's possible?


Another alternative:
+ RNN decoder... given you said sensor, what else can you say?


+ Can we provide seasons? Different modalities?
+ Time of day, week of year, etc / relative times


Question: heating example -> can we ignore this until we can't?

Graph model -> not yet... 4 months go by very quickly...



We care about markerValues

We can discretize CoolingStage:{1,2,3} into CoolingStage1, CoolingStage2, CoolingStage3 as long as there aren't too many.


+ Can we tag sequentially? -> Node in a graph
+ Take all tags -> run an algorithm to discover who's connected to who -> *leave it for a future study* -> may lead to ambiguities


+ Missing data? Ignore 2 week window if you missing more than 80%; we are calculating statistics on them


+ Can we stratify in different ways?
  + One models to rule them all -> very much simpler (we will have to train/test various model structures)
  + Otherwise, a model per equipment type or building archetype -> depends on the number of buildings per type

+ Fine tune model possible (start with general trained model)
  + Active learning also possible here


## TODO
+ Give a sort of table of what are the inputs, what are the outputs
+ Result we're trying to get to -> F1 score (why?)
+ Fill out the AI canvas sheet
+ Unbalanced classes -> get the count for each -> show the analysis (append to the report)

+ Set up an experimental approach (sort of a makefile)

+ UA model -> send results
+ Pain points? -> F1 score too low, user doesn't trust and do things manually, issues with selecting training data

# Shared Documents
## Mila interactive visit methodology
The methodology used in the Mila-IRAP interactive visit is based on three elements: weekly reports, weekly meetings and a project report. The templates can be found in the same archive associated to this file.

### Weekly report
- Each week, one working day before the weekly meeting, you must send an email that summarizes the action points status (in progress/completed), open questions and general comments about the project.
- We use this information to prepare the weekly meeting.

### Project report
- The purpose of the project report is to have a clearly written document that the company and Mila can use to make sure we have the same understanding of the project and its progress.
- At the end of the project, you have a complete reference document.
- You are responsible for writing the report for two reasons: the Mila advisor has more time to help you build the PoC, and writing the project report is a good way to make sure you understand the technical details.
- The project report structures the interactive visit with different milestones. The order of the milestones must be respected.
- Your Mila advisor uses the project report to make a sanity check with a second member of the Mila tech transfer team. The purpose of this sanity check is to make sure that the proposed solution is sound for your context.

### Weekly meeting
- A one-hour meeting that is fixed every week at the same moment.
- We review the completed action points.
- We discuss the difficulties of the action points in progress.
- We provide answers to the open questions of the weekly report.
- We define with you the next action points to be done.
- It is important that you understand and validate the reasons for the action points proposed by the Mila advisor.
- Some action points will be about completing and updating the sections of the project report.

Remember that your commitment is essential for the project to be successful.

## Weekly summary
+ https://docs.google.com/document/d/10w_zfaN6i3q0qV_Qzkvk3jYzILg6Tgl4uiI3YoTUdf4/edit#heading=h.2sqhobx7o709

## Project report
+ https://docs.google.com/document/d/1BOI_5fm32VLoXCyaR3nJsRJgb6Xjoq7GeCr1L7RO4Yk/edit#heading=h.tbecab7hzrn


# 2022 08 08
Instead of concatenating, we can also just sum them together.

Proposed by Bruno: semantic loss -> promote respect of contraints

Tagging in a sequence won't work too well since the model might predict the same tag over and over (architecture 1.5). Tree idea too might be too complex for the beginning (architecture 2).

## Papers
+ A semantic loss function for deep learning with symbolic knowledge
+ Pylon
  + There's a repo implementing the loss function (in PyTorch)
  + https://proceedings.mlr.press/v176/ahmed22a/ahmed22a.pdf
  + https://pylon-lib.github.io/

Review of Pylon libary -> hasn't been updated since the conference, typos in readmen, OK for a PoC, be wary in putting this in production without a full review

Put cross-entropy on all logits. (Cross entropy is y2)

Use SamplingSolver -> 10'000 etc vs doing the whole thing would be 2^80 since we have 80 tags.

Could also be a WeightedSamplingSolver -> what would be the weights? frequency?

We can add rules incrementally.

## Feedback on architecture
+ Character-level convolutional networks for text classification
  + Yann LeCun

Raw string encoder: character level -> let model decide where to put emphasis.

Raw name -> low case, remove URL bit -> simplify to a small ASCII -> one-hot that encoding

Input can be a CNN or RNN (LSTM, GRU).

Data augmentation -> add some random characters to add robustness?

Swap tag with timeseries if they are the same point.

Use a very incremental approach.

For every modules -> list all possibilities

## Hyperparameter selection
+ Epistimio/Orion, made by Mila
+ Simplest approach: random search
+ PyTorch Ligntning ~= Keras of PyTorch
  + Bruno uses PyTorch exclusively, is Jax-curious, not too much care for TensorFlow

## Splitting the data
+ 60/20/20? Or do we go by controller / system?
+ Split by complexity?
+ Split by building since point in a building are not IID

# 2022 08 15
+ Do a checksum of the data
+ Time series features / indicators -> day of week, weekday/weekend

## Tutorial on PyTorch
+ Do a PyTorch tutorial -> quick tutorials (lightning round)
+ 1st 3 tutorials -> do the NLP ones
+ Afterwards, move to PyTorch Lightning (do those tutorials)

## Group of tags as a 1-hot mega-tag
+ Do the precision calculations for the 90th-percentile sort of thing
+ Normalized confusion matrix
+ Which ones are typically wrong vs most popular?

## Staged systems
+ Can we flatten the stages and rely on a heuristic to get the numbers?
  + Count(Stage 1) > count(stage 2) > count(stage 3)

## Todo during the next 3 weeks
+ Project report -> fill it in, answer the questions in the report

# 2022 09 12
Model is ready and being trained in ClearML!

+ if we want to add capital letters, might as well go to utf-8 over plain ascii
+ might be overfitting in the validation

+ use "Precision" as the early stopping criteria
+ [[f1-score]], can also be an F-beta
+ or use a false-positive score or something else?
+ metric needs to convince the users to use the product/tool

## To ask Claude
+ Should I be present in these in the future?
+ Would want JSV to be present around the mid point to see if we should continue this sort of contract in the future?

[//begin]: # "Autogenerated link references for markdown compatibility"
[f1-score]: f1-score.md "Metrics"
[//end]: # "Autogenerated link references"