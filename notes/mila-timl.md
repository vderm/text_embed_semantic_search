---
author: Vasken Dermardiros
categories: note
date: May 18, 2022
tags:
- research
- collaboration
- mila
- timl
title: "BBAI-MILA: Equipment-Informed Meta-Learning"
---

+ Accepted Project: /attachments/BrainBox AI_MILA_Meta Learning.docx
+ Shared Drive: <https://drive.google.com/drive/u/1/folders/13ofQPu6g9NUOC6c3CTnAroRse7FGa_te>

People involved:

+ David Rolnick, McGill
+ Gabriel Tseng, McGill
+ Ysael Desage, BrainBox AI
+ Vasken Dermardiros, BrainBox AI
+ Annie-Shan Morin, MILA

# Building Timeseries Data

|       | 1   | 2   | 3    | ... | n   |
| ----- | --- | --- | ---- | --- | --- |
| $t_0$ | 0   | 0.1 | 21.2 | ... | 0   |
| $t_1$ | 1   | 0.5 | 21.2 | ... | 0   |
| $t_2$ | 1   | 0.3 | NaN  | ... | 0   |
| $t_3$ | 0   | NaN | 21.4 | ... | 0   |
| ...   | ... | ... | ...  | ... | ... |
| $t_i$ | 1   | 0.7 | 22.7 | ... | 0   |

where $t_i - t_{i-1} \approxeq \textrm{5 min}$, which can be interpolated and forward-filled to assure a homogenous step.

Do note that there can be missing values that must either be filled or the whole row must be dropped.

**There are 40 buildings currently that are tagged.** This set includes a mix of different building archetypes located around the world. The rest of our buildings are currently in the process of being converted to this tag-based approach. Buildings can have from 100 to 20'000 columns where the average is around 3000-5000.

# Weather Timeseries Data

Similar to building case but $t_i - t_{i-1} \approxeq \textrm{60 min}$. Weather data is per city.

# Building Points Metadata

The columns $1, 2, 3, ..., n$ are unique numbers per a given building and we call these columns *building points* or *building equipment*. These then are described by a list of tags.

+ $1$: $[tag_1, tag_2]$
+ $2$: $[tag_1, tag_4, tag_5, tag_6]$
+ $3$: $[tag_{10}, tag_{11}, tag_{12}, tag_{13}]$
+ and so on

More specifically, these tags are following the standards: [Project Haystack](https://project-haystack.org/doc/appendix/tags) and [Bricks Schema](https://brickschema.org/ontology/1.2). At BrainBox, we've also added extra tags for the equipment power information. Some tags are indicators: whether a certain point can be described by a certain tag or not. Some tags will need a value too: if the tag is for a floor, then the floor number would also need to be included; if it's a child equipment, then the parent would need to be indicated.

We also have tags for these points to know whether they are *writeable* or not. Writeable points act as the *control variables*, meaning these are points we can actuate and override. Non-writeable points fall under two categories: *state variables* like zone temperature, supply temperature, and *status or observational variables* such as a fan status or damper state; the latter are more to confirm whether a system is ON or OFF for safety reasons. We would like to predict the behaviour of state variables given the others. The other variables are known in the future.

**There are 450 tags** that can be used from our dictionary.

# Building Location Metadata

Last, the building location can be used as a static feature. Location can also be linked to climate zone. Construction years are sometimes known, but it's not very reliable since buildings are remodelled every 7-10 years.

# Getting to our Data

We are finalizing our Data Service API to be able to fetch the timeseries and tag lists in a much more simplified approach. I'll share the client with you soon, however, you would have to be in our VPN.

I received an oral confirmation from Jean-Simon Venne about being able to publish some data as long as its anonymized: not disclose building name, address, or whatever else that might give away the identity of the client.

# Journal

## May 11, 2022

+ Kick-off meeting, spoke with David and Gaby
+ Ask was to get a confirmation about data sharing with the public

## May 18, 2022

+ Chat with David and Annie-Shan
+ Presented above document

can we split the timeseries data by tags/equipment?
prepare some sample data for Gaby
get a written confirmation from JSV about data publication

## June 7, 2022

+ Persons present
  + Carlos Prieto
  + Gabriel Tseng
  + David Rolnick
  + Annie-Shan Morin
  + Vasken Dermardiros

Next step

+ David and Carlos to work out internship

## July 27, 2022

+ Persons present
  + David Rolnick
  + Annie-Shan Morin
  + Vasken Dermardiros
  + Gabriel Tseng
  + Carlos Prieto

Data sharing permissions

+ <carlos.prieto@polymtl.ca>

## August 2, 2022

Spoke to Carlos one-on-one to get to know him better. He's very strong on inverse modelling and expertise in geothermal heat pumps. He understands HVAC and this should be quite an interesting project. He's genuinely interested.

## August 10, 2022

+ Persons present
  + David Rolnick
  + Annie-Shan Morin
  + Vasken Dermardiros
  + Gabriel Tseng
  + Carlos Prieto

Climate zone information.

![3 candidates to predict zone temperature](../attachments/2022-08-10-09-07-11.png)

![SARIMAX fit with Naive decomposition](../attachments/2022-08-10-09-10-14.png)

LightGBM: gradient boosting library from Microsoft

## September 21, 2022

+ Persons present
  + David Rolnick
  + Vasken Dermardiros
  + Gabriel Tseng
  + Carlos Prieto
  + Mathieu Le Cam

Carlos met with Gaby to coordinate with TIML

**We (Carlos) would need more data!**

Next steps: contact with BrainBox -> standard pipeline in the data

Aim for publication:

+ JMLR Climate Issue/Track; prob not ICRL yet
+ No deadline to consider

## September 31, 2022

+ Persons present
  + Vasken Dermardiros
  + Mathieu Le Cam
  + Carlos Prieto

![Trained on one building and then tested on another](../attachments/2022-09-30-09-38-39.png)

+ Trained on 92, tested on 95
  + 92: MTL-SleepCountry-0309
  + 95: MTL-SleepCountry-0326

What is the meta you're providing?
Do you have a sort of architecture diagram?

Prediction horizon: 24 timesteps -> 2 hours
Meta-windows: 6 hours (3 time windows)

![MAML and TIML](../attachments/2022-09-30-09-58-27.png)

![Pseudo-code](../attachments/2022-09-30-09-58-44.png)

## October 5, 2022

+ Persons present
  + Carlos Prieto
  + Gabriel Tseng
  + David Rolnick
  + Vasken Dermardiros
  + Mathieu Le Cam

Carlos meets with Gaby every other week.

When will Mathieu be moving to North America.

move meeting? evening and not Wednesday -> ideally monday (2-3 PM) or tuesday

Gaby and Carlos to meet about meta-data massaging, etc.

Next step:

+ BBAI: get Carlos more data
+ MILA: validate the capacity of the model
+ Carlos: try different metrics
+ David: how are we exploiting the different meta-data? common between equipment?

# October 18, 2022

+ Persons present
  + Carlos Prieto
  + Gabriel Tseng
  + David Rolnick
  + Vasken Dermardiros

Meta-learning is being used because we're not incorporating the meta-data.

![Training MAML](../attachments/2022-10-18-14-37-21.png)

Thermal response on 3 buildings.

![New method: training with whole meta-data](../attachments/2022-10-18-14-38-47.png)

![MAML result on VAV](../attachments/2022-10-18-14-40-02.png)

![New method on VAV](../attachments/2022-10-18-14-40-39.png)

Straight TIML.

![New method RTU](../attachments/2022-10-18-14-42-28.png)

Meta-data encoded using VRE, data. Everything is normalized for range in 0-1.

More building with VAVs

# November 1, 2022

+ Persons present
  + Carlos Prieto
  + Gabriel Tseng
  + David Rolnick
  + Vasken Dermardiros
  + Mathieu Le Cam

Spoke about results. Carlos will not work from Nov 28 to Jan 4 since he has to finalize his thesis and has to attend conferences. David was upset to hear this a little last minute. Carlos did say he'd be willing to then extend his internship until February (instead of ending on the second week of Jan)

We also discussed that we should come up with a list of deliverables. I sent this email to Carlos and will chat with him on Thursday:

``` md
Sending you the list before sending it to David and Gaby. This list is really more to try to wrap up the project. We don’t want you to start new things at this point. We also binned things by what’s important to us. There’s no real binding agreement for these points on our side; the agreement between you and David is between you two actually.

# Most excellent to have
+ Is TIML useful for the built environment application to have one model for multiple zones or buildings? Or should we also explore another avenue? If yes, what would you suggest?
+ Can TIML predict multiple buildings with similar equipment?
+ Can a TIML approach handle dissimilar equipment? E.g. RTU vs AHU.
+ What is the performance impact between having a specific model (for a given zone or building; using a gradient-boosting model, or other) vs TIML? Would TIML actually do better because it has access to data from multiple buildings?
+ Given controls and context, is a TIML okay to predict the temperature or rate of change of temperature in a space for timesteps `t` to `t+n` where `n` is around 2 hours?

# Nice to have
+ Distribution of prediction error (MSE, MAE, percentiles, etc.) per timesteps `t` (can be for t+5min, t+10min, t+15min, t+30min, t+45min, t+60min, t+90min, t+120min, t+…; reasoning: we care more about the recent future than the distant one)

# Bonus
+ Which meta-data is useful? Can be determined heuristically by adding/dropping features
+ For deployment, what is the inference speed?
```

# November 10, 2022

+ Persons present
  + Carlos Prieto
  + Vasken Dermardiros
  + Mathieu Le Cam

Chat with Carlos, wrapping up this month. Will build a document. Code will be part of Mila.

Meta-learning very useful for modeling cases not seen -> need to make sure inputs are good. Fast adaptation.

Train on some buildings, test on another, validate on another.
Feature learning -> one batch.

LSTM model with variational dropout.

Timestamps encoded with sin/cos -> overfitting? since this would include the SP schedule

Weather has to be the same -> featur is fixed.

Project til April.

# November 10, 2022

+ Persons present
  + Gabriel Tseng
  + David Rolnick
  + Carlos Prieto
  + Vasken Dermardiros
  + Mathieu Le Cam

One of the last meetings with Carlos. He just submitted his thesis!

Will prepare a report with slight modification on the code. We will have time to give feedback and let him update it. He will have time to update it, but not much more than that.

# Email with questions

## Reply by Vasken

Hey Carlos,

Thanks for preparing that. I do have a few follow up questions to clarify.

+ Can you explain the difference between a feature, meta-data and task?
+ In the report, can you show a window of data (say for September 1
for a few hours) and show the meta-window on top? How does the
meta-window move? This is what I’m thinking of when I think of a
meta-window:
+ [arima - Backtesting: Which is better? Sliding Window or
Expanding Window? -  Stack Overflow]
+ But the part that’s still confusing is that the one part of the
model sees a larger time range than the other part. This is why a
diagram of the architecture can help. Are there two different time
windows in the TIML model? What are they?
+ For the statement about the model not needing more data (point 4
in black), it seems counter-intuitive. I’m thinking that a TIML model
will have many more weights than a vanilla LSTM and therefore will
need more data to reach a same performance. The advantage of TIML
would be that 1x TIML model that can cover 10 buildings would be much
more valuable than 10x LSTM models each covering a single building.
There would be a point where the TIML model outperforms the
individual building models. If you have to predict 1 building (or 1
RTU), then TIML is much more expensive than a simple LSTM. If you
have to predict 100 buildings, then TIML is cheaper than 100 LSTMs. I
hope that’s clearer. Is my understanding correct? Please elaborate.
+ Lastly, the question on whether a model trained on an RTU system
can be used on another type of equipment: if we have a way to
map/encode the raw features of the RTU and AHU so that it’s in an
equivalent representation, then we would be able to use this for
multiple equipment, correct? This raw feature to encoded feature can
potentially be a trained model or via the use of thermodynamic
equations. Or would you have to train another model? Or would that be
another task?

## Reply by Carlos Nov 18, 2022

Hello Vasken,

Thank you for your points. They are very interesting. I'm happy about
your points.

1.- The meta-data is based on the data used as experience for the
training, which in this case is constructed by a support and query set
(e.g. meta-training, meta-validation and meta-testing). Features are
the data used for constructing the task, for instance, location,
weather conditions, encoding time stamps, etc. The task is the
collection of support and query sets, in this case, the collection of
meta-windows belonging to the same equipment.

2.- Sure!. I will include the task construction based on meta-windows
for illustration purposes. Thank you for this insight.

3.- Good point. This point is related to a comment by Mathieu, and an
illustration for modulation and task network will be included.
About having two time windows, could be considered as two different
time windows. One is a meta-window, and the other is a time window.
However, the meta-window is a function of the time window.

4.- The goal of few-shot learning is to train a model to adapt to new
tasks using only a few data points and training iterations. Although
the training data set is the same, the training process is different
in that only a small number of examples can the model optimize its
parameters. Even though vanilla LSTM could be smaller (depending on
the configuration), TIML can adapt to unknown datapoint much more
quickly while maintaining good accuracy in its prediction. That is why
TIML does a great job of zero-shot learning. In short, in performance
time, vanilla LSTM could be faster, but the adaptation to unknown
tasks could be a drawback. Therefore, your point is correct about TIML
should be better when considering new (i.e. your 100 building example)
conditions.

A couple of points I would like to add to this extent:

+ Reducing the training and deployment time is an essential part of
BrainBox AI: The proposed meta-learning algorithm can perform fast
adaptation requiring fewer data points in the learning process. So
far, BrainBox AI retrains its models once per week, which requires a
lot of resources. Now the training could be faster and not
"necessarily" be performed once per week. Of course, this statement
should be further studied.

+ A contribution towards a "unified" model to predict thermal response
for multiple buildings: This is the main contribution of this project.
The proposed model aims to avoid having a specific model per building,
and this is crucial because BrainBox AI is constantly growing and
acquiring more clients. Therefore, having more buildings would require
more models for such buildings and constantly retraining them. Hence,
fewer meta-models could be used for this end.

I firmly believe the project has good results towards those objectives
because we work together.

5.- Thank you for your question and comment. Yes, it could be
possible. This was my first thought, and I commented on this with you
in one of the meetings (firsts meetings). Still, we have decided
together to move with RTU and know how this works.

Please, do not hesitate if you have more questions. I'm pleased with
this project, and thank you for helping me.

Best regards,
Carlos Prieto

# November 21, 2022

+ Persons present
  + Carlos Prieto
  + Vasken Dermardiros
  + Mathieu Le Cam

## Questions regarding the report to clarify

Tasks:
+ support set -> inner loop
+ query set -> validate inner loop
+ also see: <https://github.com/learnables/learn2learn/blob/master/examples/maml_sine.py>

Whole thing -> validation set is another building
Meta-window: multiple of the window

Training set: 4 buildings -> 1400 meta-windows
Validation set: 1 building with a few RTU -> 400 meta-windows
Testing set: 1 building -> 200-300 meta-windows
Batch: 20 meta-windows per epoque

Input space

+ Inside task encoder -- Features: sensors, heating/cooling stages, setpoint

2 networks:

+ task network -> injecting 1 time window (short term), sample from query set
+ modulation network -> meta-window (3x time window; long term), sample from support set
+ encoding/decoding
  + Inputs: weather conditions, circular time encoding, room SP, HVAC stages
  + Output: room temperature
+ No "static" information to identify building -> how do you know this RTU is for this building? some equip oversized, broken, etc

+ 1 task -> predict room temperature for RTU
+ Another task -> encode another equipment, but a task == meta-window...

# January 4, 2023 - Final reply from Carlos Prieto

[Yesterday 7:17 PM] Carlos Prieto
Hello Mathieu

[Yesterday 7:17 PM] Carlos Prieto
These are my answers:

[Yesterday 7:17 PM] Carlos Prieto
o   What is the architecture used for the task network?
§  The architecture for each task and modulation network is stated in page 3 and 5.
o   What are the features extracted?
§  For features on each layer, this is stated in page 2.
o   Why the use of the FiLM layer in particular? Any trial with other approach? Do provide the source that said FiLM was a better choice for time series forecasts.
§  There is not a particular paper to refer to this assertion instead, and according to Gabi comment, this is a useful layer.
o   Have you looked into the tasks’ groups and their distribution? How many groups of tasks? how many tasks per group?
§  This interesting point has not been studied.
o   Is the generator from the modulation network using any information from the task network when sampling from latent space? Is it done in a similar way to the TIML approach below? Please give some details
§  Here I would suggest follows the logic on both figures, this one and the one in the report specifically in page 4. The generator uses the encoder information and then passing to the task layer. You can explore a new strategy on this.
+ What are the features used for the modulation network and the task network? If same please specify, it might be something we want to investigate in the future.

o   This point it was stated in the report (i.e. page 3-5) and it is, I believe, with one of the previous question.
+ Any insight on the performance of the auto-encoder of the modulation network? How is the reconstruction error after training?

o   This point should be further studied.
+ The prediction results are given over a prediction horizon of 10 meta-windows (60 hours) whereas the task network on figure 2 seems to give a prediction over a query single time window (2 hours). Is the 60-hour prediction a multi-step prediction? Please explain how this result was produced.

o   As per as one of our conversation the 60-hour could be done as multi-step or one-shot. Particularly, for this paper was done one-shot.

[Yesterday 7:18 PM] Carlos Prieto
Hopefully you have had a great year and this new year full of nice activities.

[Yesterday 7:20 PM] Carlos Prieto
This would be my last answers to this project. The next steps should be addressed with David and Gabi.
I got a very nice experience with you guys and looking forward to know more about BrainBox AI in the near future.
Take care Mathieu and say hello to Vasken on my behalf.

[Yesterday 7:21 PM] Carlos Prieto
All the best!

# Message to David

Hey David,

Hope you had a nice relaxing holiday period!

For our project together, we got the last reply from Carlos (see below). It's a little superficial and we're hoping we can dive into some of the details with you and Gaby. Basically, our research question is whether "could a meta-model approach be used to have a single model cover multiple buildings"? On one side, since data from multiple buildings are pooled together, this would offer more coverage; on the other side, a model per building can specifialize to its own case much better. These questions were to help us better decide whether or not to continue this work.

There are some irks on how the experiment is setup: (1) the modulation and task network inputs are the same, (2) the future weather and actuator/controls information isn't passed to the model and yet we're predicting for the next 60 hours (this doesn't make sense). There are other too, but these 2 are the most important and we'd want to focus on getting an answer for those first.

o   What is the architecture used for the task network?
§  The architecture for each task and modulation network is stated in page 3 and 5.
o   What are the features extracted?
§  For features on each layer, this is stated in page 2.
o   Why the use of the FiLM layer in particular? Any trial with other approach? Do provide the source that said FiLM was a better choice for time series forecasts.
§  There is not a particular paper to refer to this assertion instead, and according to Gabi comment, this is a useful layer.
o   Have you looked into the tasks’ groups and their distribution? How many groups of tasks? how many tasks per group?
§  This interesting point has not been studied.
o   Is the generator from the modulation network using any information from the task network when sampling from latent space? Is it done in a similar way to the TIML approach below? Please give some details
§  Here I would suggest follows the logic on both figures, this one and the one in the report specifically in page 4. The generator uses the encoder information and then passing to the task layer. You can explore a new strategy on this.
+ What are the features used for the modulation network and the task network? If same please specify, it might be something we want to investigate in the future.

o   This point it was stated in the report (i.e. page 3-5) and it is, I believe, with one of the previous question.
+ Any insight on the performance of the auto-encoder of the modulation network? How is the reconstruction error after training?

o   This point should be further studied.
+ The prediction results are given over a prediction horizon of 10 meta-windows (60 hours) whereas the task network on figure 2 seems to give a prediction over a query single time window (2 hours). Is the 60-hour prediction a multi-step prediction? Please explain how this result was produced.

o   As per as one of our conversation the 60-hour could be done as multi-step or one-shot. Particularly, for this paper was done one-shot.

# Gaby's answers

o: Mathieu/Vasken's questions
§: Carlos' answers
+: Gaby's answers
-: Extra notes by Vasken

o   What is the architecture used for the task network?

+ we can try better approaches
o   What are the features extracted?
§  For features on each layer, this is stated in page 2.
o   Why the use of the FiLM layer in particular? Any trial with other approach? Do provide the source that said FiLM was a better choice for time series forecasts.
+ FiLM worked in a paper -> element-wise multiplication + summation
§  There is not a particular paper to refer to this assertion instead, and according to Gabi comment, this is a useful layer.
o   Have you looked into the tasks’ groups and their distribution? How many groups of tasks? how many tasks per group?
§  This interesting point has not been studied.
o   Is the generator from the modulation network using any information from the task network when sampling from latent space? Is it done in a similar way to the TIML approach below? Please give some details
§  Here I would suggest follows the logic on both figures, this one and the one in the report specifically in page 4. The generator uses the encoder information and then passing to the task layer. You can explore a new strategy on this.
+ to be done as a next step

- What are the features used for the modulation network and the task network? If same please specify, it might be something we want to investigate in the future.

o   This point it was stated in the report (i.e. page 3-5) and it is, I believe, with one of the previous question.
+ Any insight on the performance of the auto-encoder of the modulation network? How is the reconstruction error after training?

o   This point should be further studied.
+ The prediction results are given over a prediction horizon of 10 meta-windows (60 hours) whereas the task network on figure 2 seems to give a prediction over a query single time window (2 hours). Is the 60-hour prediction a multi-step prediction? Please explain how this result was produced.

o   As per as one of our conversation the 60-hour could be done as multi-step or one-shot. Particularly, for this paper was done one-shot

+ from code -> consecutive predictions

+ David -> someone from Mila can do it
+ doesn't need to be an intern

# 2023 01 24

Met up with Annie-Shan and Michel Dubois to talk about handoff of project to the AI Activation team.

## Sent an email to JS

Hello JS,

For the sake of brevity, the intern from the TIML project with David Rolnick ended his contract at the end of November. David, instead of hiring and training another intern, proposed that we go through the Mila AI Activation program (<https://mila.quebec/en/industry/ai-activation-program/>).

I was at Mila yesterday and spoke with Annie-Shan and met Michel Dubois (<https://www.linkedin.com/in/michelduboisai/?originalSubdomain=ca>) from the AI Activation program. In this program, we would be working with full-time applied research scientists that are on the Mila payroll. The activation program typically costs $5’000 for a project that would last 3-4 months. The cost is highly subsidized since they will have to publishing a report, results and the code with some data since their mandate is to disseminate the AI know-how.

For the TIML project, we had already agreed to allow David + team to publish all their work and we would be providing some anonymized data but mainly simulated data. So, we wouldn’t be renegotiating a new contract, but we will need to give Michel an OK to proceed. The only irk is that beside David advertising his collaboration with us, the AI Activation program will also be advertising as well. We will have 7 days to review and propose changes before anything is published.

Annie-Shan and I also spoke about the projects we had proposed for the Applied Research team led by Gaetan Marceau Caron: the federated / distributed learning project.

I’m drafting a timeline with all our projects and will send it to you ideally end of week.

## Given an email from Annie-Shan

Hi Vasken,

Following our conversation yesterday, we'd like to move forward with the Meta-Learning project in collaboration with David Rolnick.

To recap our conversation, a scientist from the Activation team could work with David, just like Carlos did, to continue this project. As a bonus, Mila would publish an abstract of the project on our website with the report. The code would be accessible on Github and workshops would be given to other companies in the industry. Importantly, we would publish synthetic data to ensure BrainBox intellectual property would be respected.

On our side, we're waiting to hear back from you and Jean-Simon regarding this collaboration. I've cc'd Michel who could follow up with David internally this week if needed.

We're looking forward to hearing from you hopefully before the end of the week!

Cheers,

# 2023 02 07

For AIA people, stuff we want:

1. Prove that the future weather and controls are input to the model to make predictions on future temperature
2. Task network: what are the meta-data used to differentiate one building from the other
3. Have you looked into the tasks’ groups and their distribution? How many groups of tasks? how many tasks per group?
4. Robustness to randomly missing values: what happens when we train a model on randomly masked inputs? Simple.

# 2023 02 21

+ Jacob Lavoie: RL in retinal implants, MRI data, touched many things

Will start working on the project in March, update in mid-March

# June 29, 2023

+ Persons present
  + David Rolnick
  + Vasken Dermardiros
  + Mathieu Le Cam
  + Jacob Lavoie

## Question of meta-data

+ Support and query datasets should be quite different else there's a leak...
+ Use other buildings and other years
+ Task-information/features need not be discrete

## UMAP

+ 3 buildings plotted -> they're all close to each other, even for other 3 buildings
+ The green one is showing smaller clusters -> maybe add more feature to TIML -> showing structure
  + done by task_id -> task_id is a time "key"
+ 72 steps * 5-minutes -> meta-window?

## Model capacity

+ y-axis in log, would show more the trend
+ 5-fold experiment for medians -> more than 3-ish buildings don't add anything --> make model bigger!

## Future work

+ SHAP -> wiggle inputs to see which parameters are important
+ Meta-window too close...

## Next steps

+ All licenses are commercial use, but public
+ Next step is on our side... Activation AI?
+ Get code from Jacob, see the details

## Experience working with David

+ Passive role, becomes active only at the end to try to continue the project
+ Will contribute very little and we have doubts that he fully understands how methods work; students/workers are good however
+ Probably with us for self-promotion or to say that his work is contributing to improve climate change due to collaboration with BrainBox; his success is directly dependent on our success (but he will just ride on it)
