---
author:
- Claude Demers-Belanger
categories: note
tags:
- reading-week
- business
title: "Reading Week: AI Canvas"
links:
- "https://realtermenergy-my.sharepoint.com/personal/c_dbelanger_brainboxai_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fc%5Fdbelanger%5Fbrainboxai%5Fcom%2FDocuments%2FRecordings%2FReading%20Session%20%28Claude%29%2D20220224%5F150228%2DMeeting%20Recording%2Emp4&parent=%2Fpersonal%2Fc%5Fdbelanger%5Fbrainboxai%5Fcom%2FDocuments%2FRecordings"
- https://hbr.org/2018/04/a-simple-tool-to-start-making-decisions-with-the-help-of-ai
---

# Introduction
Presentation based on readings from the book [Prediction Machines: The Simple Economics of Artificial Intelligence](https://www.predictionmachines.ai/) by Ajay Agrawal, Joshua Gans and Avi Goldfard

Part of the work Claude had to do at his previous start up was to pitch their company's idea. He had a hard time to communicate with others to get them to understand "where does the AI go?". Filling the AI Canvas was a good way to locate it.

![The AI Canvas](../attachments/2022-02-28-16-07-32.png)

![Example: AI to Improve Home Security](../attachments/2022-02-28-16-09-53.png)

Limit false positives since dispatching police is expensive.

# Overview
+ Predictions: what does the model output
+ Judgement: human or machine looking at the predictions -> which one do we take an action on?
+ Actions: do something
+ Outcome: KPI
+ Inputs: sensor data
+ Training: historical sensor data
+ Feedback: how to improve the system, how to monitor and incorporate the feedback

# Example for BBAI
Reduce consumption while increasing comfort in a building

+ Predictions: state of the room in the future
+ Judgement: will the behaviour correction affect comfort or energy consumption
+ Actions: turn on/off equipment, change setpoints
+ Outcome: reduction in building consumption, increase in overall comfort in building
+ Inputs: weather data, room temperature, setpoints, HVAC equipment data
+ Training: historical inputs
+ Feedback: which behavioral correction positively affected the outcome, negatively affected?

**Judgement part will remain very important!**

"Can you apply AI in our building?" --> show the AI canvas instead.