---
abstract: This is a template file to journal the progress of the AI research team's experiments. The experiments are done in scripts and jupyter notebooks. The report is to explain why those experiments are being done, how and what are the expected outcomes. This is to journal the progress such that the project can be quickly explained to a new researcher or your future selves should the project be paused for a while. Eventually, this report can be expanded into a conference or journal paper. You may wish to include references to the jupyter notebooks in codex experimenta. This report will also be helpful for SRED tax credit reporting, so do report failures as well as success.
author: Vasken Dermardiros
categories: note
date: February 2, 2023
geometry: margin=1in
header-includes: '\usepackage{tikz,pgfplots}'
monofont: FiraCode-Regular
numbersections: true
subtitle: Tracking Experiments and Journaled Thinking
tags:
- management
- research
- template
- journal
- reference
title: Report Template
titlepage: true
titlepage-rule-color: da3737
titlepage-text-color: da3737
toc: true
toc_depth: 2
toccolor: red
urlcolor: red
---


# Preface
> Delete this section after copying over.

The report is written in a plain text format called [markdown](https://daringfireball.net/projects/markdown/) which can easily be converted to HTML, PDF, LaTeX and other formats using [Pandoc](https://pandoc.org/index.html). Markdown is also the default format used in many online code repositories such as GitHub, GitLab, and so on. Markdown allows for embedding HTML and LaTeX snippets, so you can have the best of all worlds. It's also very easy and simple to use.  If you've never used it before, now's your chance to learn! You can refer to the [[markdown_cheatsheet]] this current folder.

In the top TOML section, for the title, please use what is on [our Jira Roadmap](https://brainboxai.atlassian.net/jira/software/c/projects/AIR/boards/30/roadmap?selectedIssue=AIR-13) to ease tracking. The rest of the document is *greatly* inspired by the report we had to fill with Mila. In each section, provide details for what is quoted (with a `>`). Do not delete any of the sections and subheaders below.

For figures, please put them in the `./figures` subfolder. You can create a more specific folder in there if you want.

# AI Canvas
> Fill out the AI Canvas (if applicable, else delete section), for more information, please read: https://hbr.org/2018/04/a-simple-tool-to-start-making-decisions-with-the-help-of-ai, note that there's a section added

| Prediction | Judgement | Action | Outcome |
| ---------- | --------- | ------ | ------- |
|            |           |        |         |

| Input | Training | Feedback | Theory |
| ----- | -------- | -------- | ------ |
|       |          |          |        |

BBAI example: Reduce consumption while increasing comfort in a building
+ Prediction: state of the room in the future
+ Judgement: will the controls affect comfort or energy consumption
+ Action: turn on/off equipment, change setpoints
+ Outcome: reduction in building consumption, increase in overall comfort in building
+ Inputs: weather data, room temperature, setpoints, HVAC equipment data
+ Training: historical inputs
+ Feedback: which controls positively affected the outcome, negatively affected?
+ Theory of success/failure: underlying phenomenon is based on basic heat transfer, a neural network should be able to capture it, however, the amount or quality of data might break the model

# Task Definition
> Context description of the Proof of Concept (PoC)

## Problem Description
> Describe the PoC
> Qualitative description of the available data
> Qualitative description of existing solutions (e.g. AI as a service or in-house) and drawbacks if relevant

## Evaluation Metrics
> Define the evaluation metrics

## Relevant Literature
> Cite the works done recently on similar questions or similar data

# Experimental Protocol
## Dataset Description
> Description of the data extracted from the database
>> Description the approach used to create the dataset
>> Provide a description of each feature including units of measurement, ranges of values and techniques used to handle missing values
>> Give the total number of observations in the entire dataset, if the dataset is fixed
>> Give the total number of labeled observations in the entire dataset. How many of those have high quality/reliable labels?
>> How similar are the entries in the dataset to those that will be processed in production?
>> Is there additional information about the data that needs to be considered while working on the project?
> Describe data augmentation techniques
> Describe how the test set was created?

## Experimental Settings
> Block diagram and detailed description of the model
> Description of the hyperparameters
> Description of the loss function
> Description of the optimizer
> Description of the hyper-parameter tuning technique

## Empirical Results
> Provide empirical results that are relevant for the PoC - the following are only examples
> Description of the training dynamic
> Plot of training curves
> Evaluation metrics
> Discussion on the results

# Conclusion and Future Work
> A reminder of the PoC description and the conclusions (feasible/not feasible). Remember that the conclusions will most of the time be, “we **believe** that the PoC was successful to demonstrate the feasibility of the idea because …” The arguments are the most important to explain why we believe so.
> Arguments based on empirical evidence to support the conclusion
> What are the next questions to be addressed?

# Acknowledgment

# References

# Appendix

[//begin]: # "Autogenerated link references for markdown compatibility"
[markdown_cheatsheet]: markdown_cheatsheet.md "Markdown Cheatsheet"
[//end]: # "Autogenerated link references"