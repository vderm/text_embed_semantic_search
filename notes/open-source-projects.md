---
author: Vasken Dermardiros
categories: note
tags:
- collaboration
- programming
- research
title: Open-Source Projects
---

# TODO

+ add tags
+ categories? control, simulation, mapping, operation/implementation to actual controller

# Building Energy Management Toolkit

+ [GitHub Repo](https://github.com/Carleton-DBOM-Research-Group/Building_energy_management_toolkit)
+ Multiple papers

    This repository contains the web application version of a multi-sourced, data-driven toolkit for addressing building energy deficiencies and is open-source for others to learn from, adapt, and foster into more specialised versions of multi-sourced, data-driven toolkits. At this stage, the toolkit is undergoing active development. Additions and revisions are expected and the repository will be updated periodically to reflect the most recent changes.

Burak's tools for energy baseline, AHU/Zone anomaly detection, hot/cold complaints analysis and occupancy count estimation.

# Model-Based Reinforcement Learning for Energy Efficient Data Centre HVAC Control

+ [GitHub Repo](https://github.com/VectorInstitute/MBRL-HVAC-Energy-Optimization)
+ [ArXiV Paper](https://arxiv.org/ftp/arxiv/papers/2106/2106.05497.pdf)

    This repository introduces a reference solution for training a Model-Based Reinforcement Learning (MBRL) agent to control the HVAC system in a small-room datacentre such that energy utilization is minimized. When this agent was piloted in a small site, cooling savings of 18% (excluding IT load) and heating savings of 10% (excluding IT load) were realized, for a combined estimated annual electricity savings of 11.5%. Therefore, potentially this agent can be implemented to reduce electricity costs as well as harmful greenhouse gas emissions that contribute to climate change.

OpenAI gym based RL agent. HVAC model in environment.py file. Work with Telus.

# Reinforcement Learning Testbed for Power Consumption Optimization using EnergyPlus

+ [GitHub Repo](https://github.com/IBM/rl-testbed-for-energyplus)

    Reinforcement Learning Testbed for Power Consumption Optimization.

IBM Japan using RL on E+ model.

# Center for the Built Environment

## Thermal Comfort Tool for ASHRAE-55

+ [GitHub Repo](https://github.com/CenterForTheBuiltEnvironment/comfort_tool)
+ [More Info](http://comfort.cbe.berkeley.edu/)

    A web interface for comfort model calculations and visualizations according to ASHRAE Standard-55, EN Standard 16798 and ISO Standard 7730.

## PyThermalComfort

+ [GitHub Repo](https://github.com/CenterForTheBuiltEnvironment/pythermalcomfort)
+ [Docs](https://pythermalcomfort.readthedocs.io/en/latest/)

     Package to calculate several thermal comfort indices (e.g. PMV, PPD, SET, adaptive) and convert physical variables.

## Clima

+ [GitHub Repo](https://github.com/CenterForTheBuiltEnvironment/clima)
+ [Docs](https://clima.cbe.berkeley.edu/)

     The CBE Clima Tool is a web-based application built to support the need of architects and engineers interested in climate-adapted design. It allows users to analyze the climate data of more than 27,500 locations worldwide using the data contained in EPW files.

## Mave

+ [GitHub Repo](https://github.com/CenterForTheBuiltEnvironment/mave)

    Mave is a tool for automated measurement and verification (M&V). At its most simple, the aim is to read energy consumption data from before and after a retrofit (pre-retrofit and post-retrofit data) and to predict how much energy the retrofit saved. Mave does this by training multiple models to the data and using the best model to predict energy consumption what the energy consumption would have been in the post-retrofit period, had the retrofit not happened.

    Mave automatically resolves common problems with input files (missing data, irregular timestamps, outliers, etc.), builds input features from the data (including federal holidays, downloading weather data for the location, etc.), and normalizes the results to a Typical Meteorological Year (TMY) for a given physical address.

# Sinergym EnergyPlus

+ [GitHub Repo](https://github.com/ugr-sail/sinergym)
+ [Docs](https://energym.readthedocs.io/en/latest/index.html)

    The goal of sinergym is to create an environment following OpenAI Gym interface for wrapping simulation engines for building control using deep reinforcement learning.

EnergyPlus OpenAI gym interface where the agent can control the setpoint in the building. Setpoints are discretized into steps.

# Prototype Building Models

= [Link](https://www.energycodes.gov/prototype-building-models)

    The U.S. Department of Energy (DOE) supports the development of commercial and residential building energy codes and standards by participating in industry review and update processes, and providing technical analyses to support both published model codes and potential changes. DOE publishes its findings in an effort to ensure transparency in its support, and to make its analysis available for public review and use.

They have different archetype buildings with different construction standards.

# ModelicaGym

+ [GitHub Repo](https://github.com/ucuapps/modelicagym)
+ [ArXiV Paper](https://arxiv.org/abs/1909.08604)

    This ModelicaGym toolbox was developed to employ Reinforcement Learning (RL) for solving optimization and control tasks in Modelica models. The developed tool allows connecting models using Functional Mock-up Interface (FMI) to OpenAI Gym toolkit in order to exploit Modelica equation-based modelling and co-simulation together with RL algorithms as a functionality of the tools correspondingly. Thus, ModelicaGym facilitates fast and convenient development of RL algorithms and their comparison when solving optimal control problem for Modelica dynamic models.

This is what is used in the library Scott developed and is set up in sim-2.

# Eppy

+ [GitHub Repo](https://github.com/santoshphilip/eppy)
+ [Documentation](https://eppy.readthedocs.io/en/latest/runningeplus.html)
+ [Quickstart](https://eppy.readthedocs.io/en/latest/Main_Tutorial.html)

    Scripting language for E+, Energyplus Eppy is a scripting language for EnergyPlus idf files, and EnergyPlus output files. Eppy is written in the programming language Python. As a result it takes full advantage of the rich data structure and idioms that are available in Python. You can programmatically navigate, search, and modify EnergyPlus idf files using eppy. The power of using a scripting language allows you to do the following:

        + Make a large number of changes in an idf file with a few lines of eppy code.
        + Use conditions and filters when making changes to an idf file
        + Make changes to multiple idf files.
        + Read data from the output files of a EnergyPlus simulation run.
        + Based on the results of a EnergyPlus simulation run, generate the input file for the next simulation run.

    So what does this matter? Here are some of the things you can do with eppy:

        + Change construction for all north facing walls.
        + Change the glass type for all windows larger than 2 square meters.
        + Change the number of people in all the interior zones.
        + Change the lighting power in all south facing zones.
        + Change the efficiency and fan power of all rooftop units.
        + Find the energy use of all the models in a folder (or of models that were run after a certain date)

# MPCPy

+ [GitHub Repo](https://github.com/lbl-srg/MPCPy)

    MPCPy is a python package that facilitates the testing and implementation of occupant-integrated model predictive control (MPC) for building systems. The package focuses on the use of data-driven, simplified physical or statistical models to predict building performance and optimize control. Four main modules contain object classes to import data, interact with real or emulated systems, estimate and validate data-driven models, and optimize control input.

Code is >2 years old.

# OpenBuildingControl

+ [Documentation](https://obc.lbl.gov/)

    OpenBuildingControl will develop tools and processes for the performance evaluation, specification, deployment and verification of building control sequences.

    There will be three key efforts to develop tools that support design, deployment and operation:
  + Design: We develop a controls design tool that will enable the selection and performance comparison of building control strategies that reduce energy and peak power while increasing air quality and comfort. This tool will also allow to export control sequences and functional verification tests, expressed in a digital form using an open-standard controls description language (CDL).
  + Deployment: We support the industry development of tools to interpret CDL in order to provide submittal documents and generate programming code for the building control vendor’s product line.
  + Operation: For commissioning and operation, we develop a functional verification tool that takes CDL, together with a list of control points, to verify that the control sequences have been implemented correctly and are functioning correctly.

# Myriad

+ [GitHub Repo](https://github.com/nikihowe/myriad)
+ [ArXiV Paper](https://arxiv.org/abs/2202.10600)

    Myriad is a real-world testbed that aims to bridge the gap between trajectory optimization and deep learning. Myriad offers many real-world relevant, continuous space and time dynamical system environments for optimal control. Myriad is written in JAX, and both environments and trajectory optimization routines are fully differentiable. The tools in Myriad can be used for trajectory optimization, system identification, imitation learning, and reinforcement learning.

    The aim of this repository is to offer trajectory optimization tools to the machine learning community in a way that can be seamlessly integrated in deep learning workflow. Simultaneously, we hope that Myriad will serve as a stepping stone towards the increased development of machine learning algorithms with the goal of addressing real-world problems.

Able or want to merge a simulator with Neural ODE and do trajectory optimization on top of that.

# PyEPO

+ [GitHub Repo](https://github.com/khalil-research/PyEPO)
+ [Documentation](https://khalil-research.github.io/PyEPO/build/html/index.html)

    PyEPO (PyTorch-based End-to-End Predict-and-Optimize Tool) is a Python-based, open-source software that supports modeling and solving predict-and-optimize problems with the linear objective function. The core capability of PyEPO is to build optimization models with GurobiPy, Pyomo, or any other solvers and algorithms, then embed the optimization model into an artificial neural network for the end-to-end training. For this purpose, PyEPO implements SPO+ loss [1] and differentiable Black-Box optimizer [3] as PyTorch autograd functions.

# Pandas-Profiling

+ [GitHub Repo](https://github.com/ydataai/pandas-profiling)
+ [Documentation](https://pandas-profiling.ydata.ai/docs/master/index.html)

    pandas-profiling generates profile reports from a pandas DataFrame. The pandas df.describe() function is handy yet a little basic for exploratory data analysis. pandas-profiling extends pandas DataFrame with df.profile_report(), which automatically generates a standardized univariate and multivariate report for data understanding.

# popmon

+ [GitHub Repo](https://github.com/ing-bank/popmon)
+ [Documentation](https://popmon.readthedocs.io/en/latest/)

    popmon creates histograms of features binned in time-slices, and compares the stability of the profiles and distributions of those histograms using statistical tests, both over time and with respect to a reference. It works with numerical, ordinal, categorical features, and the histograms can be higher-dimensional, e.g. it can also track correlations between any two features. popmon can automatically flag and alert on changes observed over time, such as trends, shifts, peaks, outliers, anomalies, changing correlations, etc, using monitoring business rules.

# Building Ontology and Tagging

+ [Project Haystack tags](https://project-haystack.org/tag): list of tags
+ [BricksSchema v1.1](https://brickschema.org/ontology/1.1): list of additional tags
+ [Bricks Visualization tools](https://brickschema.org/tools) BrickStudio, QueryBuilder, Brick Viewer, useful to see
    what the TTL file looks like -> tend to be more visual than useful, cluttered
    and slow
+ [VBIS Classification Tags Search Table](https://vbis.com.au/search-and-download): adds more granularity to tags, very
    much useful to track assets
  + eg. ME-Fa-Cf-DWDI: Mechanical-Fan-Centrigual-Double With Double Inlet

# Google Digital Buildings

+ [GitHub Repo](https://github.com/google/digitalbuildings)

    Digital Buildings (ontology and SDK) currently being used by Google internally to manage our own buildings.

    The Digital Buildings project is an open-source, Apache-licensed effort to create a uniform schema and toolset for representing structured information about buildings and building-installed equipment. A version of the Digital Buildings ontology and toolset is currently being used by Google to manage buildings in its portfolio.

    The Digital Buildings project originated from the need to manage a very large, heterogeneous building portfolio in a scalable way. The project aims to enable management applications/analyses that are trivially portable between buildings. This goal is achieved through a combination of semantically-expressive abstract modeling, an easy-to-use configuration language, and robust validation tooling. Digital Buildings work has been inspired by Project Haystack and BrickSchema and maintains cross-compatibility and/or convergence as a long-term objective.

    In creating the Digital Buildings project, we have considered the following:

  + Human Readability
  + Machine readability and interpretation
  + Composable functionality
  + Dimensional Analysis
  + Correctness validation
  + Cross compatibility

# Azure Open Digital Twins Definition Language

+ [GitHub Repo](https://github.com/Azure/opendigitaltwins-dtdl)
+ [Version 2](https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md)

    The Digital Twins Definition Language (DTDL) is a language for describing models and interfaces for IoT digital twins. Digital twins are models of entities in the physical environment such as shipping containers, rooms, factory floors, or logical entities that participate in IoT solutions. Using DTDL to describe a digital twin's capabilities enables the IoT platform and IoT solutions to leverage the semantics of the entity.

    DTDL is open to the community and Microsoft welcomes collaboration with customers, partners, and the industry. It is based on open W3C standards such as JSON-LD and RDF which allow for easier adoption across services and tooling.

# Physics-Based Deep Learning

+ [GitHub Repo](https://github.com/tum-pbs/Physics-Based-Deep-Learning)
+ [PhiFlow GitHub Repo](https://github.com/tum-pbs/PhiFlow): optimization toolkit
+ [Project Homepage](https://ge.in.tum.de/)

    The following collection of materials targets "Physics-Based Deep Learning" (PBDL), i.e., the field of methods with combinations of physical modeling and deep learning (DL) techniques. Here, DL will typically refer to methods based on artificial neural networks. The general direction of PBDL represents a very active and quickly growing field of research.

+ [PBDL Book](https://physicsbaseddeeplearning.org/intro.html)

# Other Packages

+ [Scikit-Optimize Surrogate Modelling](https://scikit-optimize.github.io/stable/)
+ [cvxpy](https://www.cvxpy.org/)
+ [MPC PyTorch Layer](https://locuslab.github.io/mpc.pytorch/)
+ [Julia Modeling Toolkit](https://mtk.sciml.ai/stable/)
+ [k3sup](https://github.com/alexellis/k3sup)

# Resources

+ [Physics-Based DL](https://physicsbaseddeeplearning.org/intro.html)
+ [Differentiable Control Problems](https://fluxml.ai/blog/2019/03/05/dp-vs-rl.html)
+ [Differentiable Programming and Neural ODEs](https://medium.com/swlh/neural-ode-for-reinforcement-learning-and-nonlinear-optimal-control-cartpole-problem-revisited-5408018b8d71)
+ [Machine Learning on Time Series Data with Julia](https://www.youtube.com/watch?v=YPS9j8Aijeo)
+ [Global Workspace Theory](https://en.wikipedia.org/wiki/Global_workspace_theory)

# Interesting Articles

Probably not the best place for this

+ [Neural Network Loss Landscapes: What do we know?](https://damueller.com/#/blog-post/NNLLs)
