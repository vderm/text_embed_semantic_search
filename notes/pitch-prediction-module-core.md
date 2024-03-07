---
author:
- Vasken Dermardiros
date: January 10, 2022
categories: pitch
tags:
- controlkit
- clearml
- model
- module-prediction
- organizing
- pitch-shaped
title: Prediction Module Pitch
subtitle: Core Functionality
titlepage: true
titlepage-rule-color: da3737
titlepage-text-color: da3737
toc: false
urlcolor: red
---

# Problem
>
> The raw idea, a use case, or something we’ve seen that motivates us to work on this

We keep with the skateboard, bicycle, motorcycle, car analogy. What we have right now works, but seeing how the summer went with the interns, how production went with sending models back and forth, the request files and unannounced updates and bug fixes, things would need to be simplified.

![Quite difficult to experiment with models quickly: settings and processing steps spread in multiple libraries and layers](../attachments/2022-01-06-13-52-23.png)

Our current framework is a baseline to imagine something better: easier to use, easier to understand, easier to maintain, easier to test (!) and easier to extend.

The objective is to give full prediction authority to the prediction module with this and following works. The work in here will supersede the work spread around in `MLKit`, `ControlKit.prediction`, `DataKit.features` and `DataKit.utils`, `KitUtils` and can even touch `KitVisualizations`.

# Appetite
>
> How much time we want to spend and how that constrains the solution

Time budget: six weeks starting January 10, 2022. **End date is February 18, 2022**. No extensions. Next cycle begins March 7, 2022.

Solution should at least contain a linear model and a sequence-to-sequence model. Test cases to prove that learning occurs (synthetic data: sine wave, exponential decay).

Keep using TensorFlow 2.x for the models and keep it raw. No need to make the models overly parametric, I'm fine with setting the recurrent layer as a GRU and calling the model "seq2seq". If we eventually find a different layer that's better, we can use that instead. Remember, this is mainly for production. In experimentation, people can define their own model classes and work like that. Would make sense to have a `Base` model class however.

That being said, I do find it would be worthwhile to explore different loss functions, eg. including a physics constraint. So the loss would need to be customizable (default: MSE). Again though, it's simpler to hard-code it and have a new model (inheriting everything else from the normal model) for a new loss function. Similar to how the OPMs are now; we don't customize the underlying models at all.

XUWO: we're keeping this. Down the line, we may rely on Haystack, but it'll still output an XUWO list anyway.

DeployKit will be what's running this library. The work in this pitch is to refactor the `DLT`, `OPM` and the `DataTask.default` stuff. Please remove all reliance on BrainBox libraries. Don't worry, we will move common code to a Utils submodule afterwards when the work on the Config Module and Data Module have progressed. I like the ideas behind the OPM and MLKit, I think it can be simplified and flattened. You can also decide what should be in the `request.json`, but it's not really part of the core functionality *per se.* We're keeping the SQS and s3bucket stuff too.

**Copy stuff over! Don't restart from scratch if you don't need to! You only have six weeks and QA is in there!**

# Solution
>
> The core elements we came up with, presented in a form that’s easy for people to immediately understand

Flatten the current set up so that everything can be seen from a high level, starting from the raw data, all the way down to the prediction evaluation going through all the steps to pre-process and prepare the data, instantiate the model, train and save the model. If any step were to fail, a reaction would be triggered.

![Example Recipe](../attachments/2022-01-07-15-42-54.png)

The Recipe (or just call it what you want) has parts of it acting like the `DataTask.default.fn_post`, part of it like `MLKit.DeepLearningTask` and the `ControlKit.prediction.OPM1`. The point is not to have "one recipe to rule them all", but to have the recipes act like the OPMs; they can be designed for a particular use and specialized based on `request.json` settings.

Let's put all the modules back together so that it's more obvious what's going on. All steps must be visible and can be interrupted and probed. The way to do it is already there. Might need to include probing functions.

![Troubleshooting](../attachments/2022-01-07-15-49-34.png)

And the part that gets a bit tricky is when we no longer map one-to-one (building-to-model). So here are some recipes that might do the trick.

![Cases to consider](../attachments/2022-01-07-15-51-22.png)

## Nice-to-Haves

+ Handle a lot of data, eg. through a sliding window training by loading and training a model with months 1 to 3, then loading and training with months 2 to 4, etc. Or whatever is reasonable and fits in memory.
+ Bring over the `DataKit.encode_decode` module, have the `combination_dict` settings for these as part of the artifact or request.
+ Min/max values of variables for the min/max scaler to be in the artifact or request; eg. room temperatures range can be fixed to min/max = 10 to 40 degC, instead of relying on the data itself and saving the parameters of this trained scaler.
+ Grid-search using scikit-optimize. Can be a rabbit hole, so if you are thinking of doing this, come talk to me since I've done it already in the past in `MLKit.grid_search`. ClearML might have a grid search too. The grid search TensorFlow had was crap back then.
+ Missing data side-fill using k-means. This could fit in the framework by considering it equivalent to the "socket" layer. The "socket" is really a model that feeds another model.

## Working on the Solution

Put your tasks in Asana please, make the sections as you discover the `scopes`; organize tasks by scopes and not people. (See Chapter 12) Prefix `nice-to-have` items with the tilde `~` and put them at the bottom of the list.

# Rabbit Holes
>
> Details about the solution worth calling out to avoid problems

Overly customizable and flexible models: no. If tomorrow you tell me a linear model is good enough to predict the next 12 hours, I will flush everything else. Our customers pay us to save energy, not build complex libraries.

Excessive documentation: do the bare minimum for commenting and instead focus on well structured code, obvious variable names, explicit if statements (eg. `if buildings_list == []:`), and so on. No need to decorate or litter your code with ascii art (yes, I'm guilty too); git maintains authorship and date info.

Planning this project too much from the beginning: don't wait to have everything perfect before starting. Plan area by area and fill in the details. Expand the territory and split the lists in Asana. Assure to *very quickly* have something that can run: aim to have a full thing running within a week on synthetic data. Build on your successes.

Local time vs UTC: everything in UTC. What about time features? Let's assume we will have the timezone in the artifact or request and don't need to make a query via DataKit or SQLAlchemy.

# No-Gos
>
> Anything specifically excluded from the concept: functionality or use cases we intentionally aren’t covering to fit the appetite or make the problem tractable

In your coding, do think about how external interaction can be made without explicitly working on them. Therefore, do not work on FastAPI interactions and do not set up databases for settings and results storage. Use s3buckets, ClearML artifacts and, at worst, local files.

Similarly, do think about how certain procedures will be encapsulated in a service, eg. poor evaluation triggers a retraining or a new model. End goal is for the final Prediction Module to have full authority on the predictions, which also includes maintaining models, publishing, updating, archiving and deleting them.

Finally, model management is another service that will be running in ClearML. You can think of this while considering the step of splitting buildings into submodels or having a model be used for multiple buildings, but don't start overly working on the model publication functions and playing the librarian in ClearML.

Weather features: simply use the same hack you have in DeployKit. Maroun is working on the DataModule and will include weather data fetching in there; this can be incorporated when it's ready.

Generally, database interactions and connectors: don't work on these as part of the prediction module; you wouldn't need to anyway.

PyTorch: from what I've read, PyTorch is the *de facto* framework for research and experimentation. When it comes to production, TensorFlow still seems to be the most popular. Both TensorFlow and PyTorch are trying to get into each other's backyards. For now, let's stick with TensorFlow since we've accumulated quite some experience with it.

Jax: this is also quite an interesting avenue, quite research-y too, but if we're gonna go with Jax, then why not Julia? Julia has much stronger algebraic differentiation tools. But no. TensorFlow (and scikit-learn, numpy, scipy) for now.

gRPC: similar to FastAPI, please do not venture there. This is also part of the interactions and this won't even be used for a very long time. We can update when this arrives.

CI/CD: don't go there either.

# Debrief after successful project delivery

+ After first cycle of a [[shape-up]] delivery
+ Location: <https://git.brainboxai.net/Toolkit/PredictionModule>

## Feedback

+ Very positive to have 6 weeks to **focus** on one thing. Not stretched left and right.
+ Prediction Module was very broad. Very big endeavour.
+ First week was very hard.
+ PR in middle failed. Having an outside reviewer at beginning is not ideal since things will change a lot.
+ Reserve last week for QA/CI/CD.
+ 6 weeks good, but certain tasks were too much -> submodelling too much!
+ Unclear part: what needed to be QA'ed? QA part inside 6 weeks made the dev period 5 weeks
+ Can be 1 week for planning, 5-6 weeks work, 1 week QA/testing
+ Next cycle may be easier since the framework is there
+ Work extra? How many hours did you spend weekly?
  + Fahimeh: 40-45 hrs, mid project worked extra, end worked less
  + Federico: 40 hrs, watched videos at night
  + Emilio: 40 hrs
  + Hours were very focused!
+ Careful when mixing people, this 6 weeks worked well because they all know each other quite well
+ Asana: scope/unscope alright, hill not great -> needs to be more interactive
+ Unclear sometimes which cycle this belongs to or next
+ Have input on the pitch

[shape-up]: shape-up.md "Shape Up - Stop Running in Circles and Ship Work that Matters"

[//begin]: # "Autogenerated link references for markdown compatibility"
[shape-up]: shape-up.md "Shape Up - Stop Running in Circles and Ship Work that Matters"
[//end]: # "Autogenerated link references"