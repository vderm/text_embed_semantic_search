---
author: Valohai
date: January 13, 2022
categories: book
tags:
- organizing
- mlops
- clearml
- improve
- reference
- revisit
title: Practical Mlops
---

Book: [[Valohai_PracticalMLOps_2020.pdf]]

# Foreword

Machine learning has remained a topic for research. MLOps tried to marry techniques from DevOps into ML to better push models into production.

![Survey results for State of ML](../attachments/2022-01-13-11-15-01.png)

# People of Machine Learning

+ **Data Scientist**: finding data-driven solutions to business problems. Deployed first to analyze existing data and to find patterns. While the primary purpose of data science is to explore data and build models, often a large portion of time is spent manipulating data to suit the use case.
+ **Data Engineer**: Responsible of the infrastructure that the data is stored and available for data scientists. They build the system to ingest raw data and push it to a centralized data lake.
+ **Machine Learning Engineer**: They take the work from Data Scientists and build a production-scale system. ML engineers understand the theoretical side of machine learning but are more involved with paradigms found in engineering such as continuous integration (CI) and continuous delivery (CD). They tackle automating and scaling model training, testing models before deployment and deploying and monitoring models in production.
+ **DevOps Engineer**: Software engineering with cloud infrastructure. Link between the ML model and the end-user application. Scalability, stability and responsiveness is at the forefront of their mind.
+ **IT**: Resource management, access controls and information security. Vendor approuval.
+ **Business Owner**: Deepest understanding of the end-user and use case. Guide the team to producing ML systems that are not just accurate and well-engineered but also valuable. Identify risks on operational and regulatory perspective.
+ **Manager**: Still new and unclear since work is highly multidisciplinary.

# How is ML different from Traditional Software?

Data! The reliance on data adds a layer of complexity. Code change can't be tested immediately, a new model needs to be trained to be tested. Version control not only on the code but on the data as well.

# The MLOps Workflow

**Only models in production bring value.**

![Messy handover](../attachments/2022-02-14-08-56-58.png)

The goal of MLOps is to reduce technical friction to get the model from an idea into production in the shortest possible time to market *with as little risk as possible*.

Three primary types of risks:

+ Loss of knowledge
  + Only one person knows how to do it and they get hit by a bus
  + Software can be understood, but data manipulations might be messy in various notebooks
  + You might forget what you did in the past
  + Model = code + data + parameters + training env >> git
+ Failures in production
  + Ensure the data used to train the model looks like you expected it to -> monitor for changes upstream
  + Make sure the model works in a real-world env; not overfit to training
  + Consistent infrastructure so model produces the same result for same inputs -> able to roll back
+ Regulatory and ethical

# Time to Market

By having a shared language with DevOps, MLOps can get to market quicker -> utilize same tooling (CI/CD, version control, microservices).

![Easing the handover](../attachments/2022-02-14-09-07-13.png)

# The MLOps Workflow Enforces Best Practices

MLOps ties model development and operations together into a continuous loop through a set of best practices:

+ Version control everything, including models, code, data, parameters, and environment. Enable anyone to trace how a model was produced.
+ Componentize the steps of the model creation process and build them into a pipeline. A single notebook is not a pipeline.
+ Codify testing. With checkpoints and safeguards in place, there is a standard that models have to adhere to.
+ Automate work to increase how much time can be spent on future development.

# How to Quantify Success in an MLOps Project?

1. Define your objective in clearm, concrete and measurable metrics with all the relevant stakeholders
   + Everyone to understand the "why" with the benefits it brings -> how it'll be evaluated
   + How the work is currently done and what it takes to replace it
   + Work out all the assumptions that different team members have by hosting a session: data, model, and how to run experiments to test the hypotheses
2. Measure the success of different stages of the project - not just the end outcome
   + Total time to deliver value; can't just know when it works 6-12 months later
   + Show progress every 6 weeks or so; incremental
   + Document the lessons learned
3. Have a multi-disciplinary team with clear roles and responsibilities.

# Shared Objective and Metrics

**What’s the minimum viable product?**
Define the bare minimum that will be needed to test the model. This will help you split the project into smaller pieces and “get to a number” faster.

**MLOps metrics**
Here you’ll find some additional metrics you might want to consider for your MLOps project.

+ Model update frequency met (and able to identify stale models)
+ Time to re-train and deploy a new model and push to production
+ Time to test and push new approach to production
+ Performance of model endpoint for online predictions (e.g. response time in ms)
+ nmbr of calls / % of failed calls to the model endpoint
+ Collaboration between the multi-disciplinary team (e.g. data scientists, engineers, IT-Ops, legal, business)
+ Attendance of key stakeholders to regular project updates (for example, every six weeks)
+ Infrastructure scales to the machine learning teams without manual work from Ecosystem/DevOps/IT

# Automated Approach

![Pipeline](../attachments/2022-02-14-09-21-42.png)

Company took a few months to build the pipeline and then put it in production -> everything in the future is now consistent and the team can concentrate on further development rather than firefighting.

# The MLOps Toolchain

## Model and data exploration

Understand the data. Explore data leads to exploring models.

Fastest way is to draw visualizations and work on notebooks.

Model exploration may require AutoML tools and makes more sense to have these run on a cluster.

**Keep model exploration part of MLOps** otherwise there will be a disconnect between the data scientists and engineers!

## Metrics and model optimization

Metrics, model training, dataset splits...

Different training and validation metrics. Validation metrics might be harder to computer so it only makes sense to do so at the end.

# Productionalization - End-to-end pipelines

![Manual ML Pipeline](../attachments/2022-02-16-10-28-28.png)

Characteristics of a manual ML pipeline:

+ *The model is the product*
+ Manual or script-driven process
+ A disconnect between the data scientist and the engineer
+ Slow iteration cycle
+ No automated testing or performance monitoring
+ No version control

![Automated ML Pipeline](../attachments/2022-02-16-10-28-47.png)

Characteristics of an automated ML pipeline:

+ *The pipeline is the product*
+ Fully automated process
+ Co-operation between the data scientist and the engineer
+ Fast iteration cycle
+ Automated testing and performance monitoring
+ Version-controlled

## Key Takeaways

1. The pipeline is the product, not the model. Do not deploy the model; deploy the pipeline.
2. To build a pipeline, split the system down into small well-defined components.
3. Model accuracy will eventually degrade as the world changes. Prepare for it.

# Feature Stores

![Feature Store: Interface between Models and Data](../attachments/2022-02-16-10-32-50.png)

Have feature stores as services transforming raw data into a clean signal that certain models may consume.

It's almost like a live transformation that serves pre-treated data to end-users.

# Testing

Testing in ML is like trying to hit a moving target. The system’s behavior depends on the data’s dynamic qualities and the various model configuration choices.

## Data Testing

**In ML projects: data >> code. Since the data defines the behaviour of the system, we need to test the data!**

## Infrastructure Testing

Run two or more models side-by-side with the same data and measure any discrepancies between metrics.

# Deployment and Inference

Deployment is the act of serving an ML model to the rest of the world via API, application, or otherwise. Inference is what the model does, once it is deployed.

[Valohai_PracticalMLOps_2020.pdf]: ../articles/Valohai_PracticalMLOps_2020.pdf "Valohai_PracticalMLOps_2020.pdf"

[//begin]: # "Autogenerated link references for markdown compatibility"
[Valohai_PracticalMLOps_2020.pdf]: ../articles/Valohai_PracticalMLOps_2020.pdf "Valohai_PracticalMLOps_2020.pdf"
[//end]: # "Autogenerated link references"