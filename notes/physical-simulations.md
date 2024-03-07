---
author:
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-08-03 10:35:58-04:00
slug: physical_simulations
tags:
- research
- simulation
- annex-81
- physics-based
title: Physical Simulations
---


Framework to compare and validate modeling and control approaches.

## BOPTEST {#boptest}

From David Blum's work from LBNL/IBPSA:

- <https://github.com/ibpsa/project1-boptest>
- <sup id="75f18c1620bc0908cfd0fb29e9d58bdf"><a href="#Blum_PrototypingBOPTESTFramework_2019" title="Blum, Jorissen, Huang, Chen, Arroyo, Benne, Li, Gavan, Rivalin, Helsen, Vrabie, Wetter \&amp; Sofos, Prototyping {{The BOPTEST Framework For Simulation}}-{{Based Testing Of Advanced Control Strategies In Buildings}}, 2737--2744, in in: {Building {{Simulation}} 2019}, edited by (2019)">Blum_PrototypingBOPTESTFramework_2019</a></sup>: D. Blum, F. Jorissen, S. Huang, Y.
    Chen, J. Arroyo, K. Benne, Y. Li, V. Gavan, L. Rivalin, L. Helsen, D. Vrabie,
    M. Wetter, and M. Sofos. (2019). “Prototyping the BOPTEST framework for
    simulation-based testing of advanced control strategies in buildings.” In
    Proc. of the 16th International Conference of IBPSA, Sep 2 – 4. Rome, Italy.

Modelica based, controllers in Python (2.7) or Julia (1.0.3).

## IBPSA Project 1 {#ibpsa-project-1}

- <https://ibpsa.github.io/project1/>: BIM/GIS and Modelica Framework for building
    and community energy system design and operation

- Task 1: Modelica Libraries: <https://github.com/ibpsa/modelica-ibpsa>
  - AixLib, from RWTH Aachen University, Germany: <https://github.com/RWTH-EBC/AixLib>
  - Buildings, from LBNL, Berkeley, CA, USA: <http://simulationresearch.lbl.gov/modelica>
  - BuildingSystems, from UdK Berlin, Germany: <http://www.modelica-buildingsystems.de>
  - IDEAS from KU Leuven, Belgium: <https://github.com/open-ideas/IDEAS>
- Task 2: Building and City Quarter Models: able to simulate 1000-10'000
    buildings for community/urban studies
- Task 3: Application and Dissemination

- Duration: 2017-2022
- Operating Agents: Michael Wetter, LBNL, Berkeley, CA & Christoph van Treeck,
    RWTH Aachen, Germany

### Task 1: Modelica Libraries {#task-1-modelica-libraries}

All models are documented and validated against analytical solutions, against
the results of other simulators or against measurement data.

Work Package 1.2: Building Optimization Performance Tests and Modelica library
for MPC

Work Package Leader: Lieve Helsen, KU Leuven, Belgium.

This work package is developing a software package called BOPTEST that allows
testing, assessing, comparing and benchmarking Model Predictive Control
algorithms and other control formulations. It is also developing a Modelica
library for use within a Model Predictive Controller.

The BOPTEST framework consist of reference building emulation test cases, key
performance indicators (KPIs) for quantification and assessment, and a software
platform to select and manage test cases, exchange control and measurement data,
calculate KPIs and generate reports. The aim of a test case is to provide a
clear and unambiguously defined scenario where any controller can be tested to
enable a fair comparison between different control strategies. Therefore, a test
case is defined as a combination of a building emulator model and a data-set
gathering boundary conditions like weather, energy prices, emission factors,
occupancy schedules and comfort requirements for a one-year duration. The
selected test cases represent combinations of buildings and energy systems
typically encountered in Europe and the US. Each test case describes the signals
that are accessible at different control levels, e.g. room temperature set
points at high level, and damper and valve positions and fan and pump speeds at
low level. Baseline controllers are included and operate whenever the control
signal is not overwritten by the external (tested) controller.

Also, a library with models that are suited for use in nonlinear Model
Predictive Control (MPC) is being developed.

## Spawn-of-EnergyPlus {#spawn-of-energyplus}

- <https://lbl-srg.github.io/soep/>

The Spawn of EnergyPlus, called SOEP, is a next-generation simulation engine,
for building and control energy systems. SOEP will combine

- The OpenStudio front-end for model authoring, simulation and as a workflow
    automation tool,
- the Modelica Buildings Library as a repository of models,
- JModelica as a translator that translate models from the Modelica standard to
    the Functional Mockup Interface standard for simulation and for execution on
    control systems,
- PyFMI as a master algorithm that conducts a time domain simulation.

![[2020-08-03_10-25-14_screenshot.png]]

## Open Building Control {#open-building-control}

- <https://github.com/lbl-srg/obc>
- Project site: <https://obc.lbl.gov/>

![[2020-08-03_10-35-29_screenshot.png]]

OpenBuildingControl will develop tools and processes for the performance
evaluation, specification, deployment and verification of building control
sequences.

There will be three key efforts to develop tools that support design, deployment
and operation:

Design
: We develop a controls design tool that will enable the selection and
    performance comparison of building control strategies that reduce energy and
    peak power while increasing air quality and comfort. This tool will also allow
    to export control sequences and functional verification tests, expressed in a
    digital form using an open-standard controls description language (CDL).

Deployment
: We support the industry development of tools to interpret CDL in
    order to provide submittal documents and generate programming code for the
    building control vendor’s product line.

Operation
: For commissioning and operation, we develop a functional
    verification tool that takes CDL, together with a list of control points, to
    verify that the control sequences have been implemented correctly and are
    functioning correctly.

**Follow-up** on the slides on git, many examples of strategies they've tested,

## EnergyPlus v9.3: Python EMS support {#energyplus-v9-dot-3-python-ems-support}

<https://github.com/NREL/EnergyPlus/releases/tag/v9.3.0>

A new Python Plugin/EMS system where the user can write Python scripts instead
of using the Erl language.

<https://www.energyplus.net/sites/all/modules/custom/nrel%5Fcustom/pdfs/pdfs%5Fv9.3.0/EMSApplicationGuide.pdf>

See Section 1.46:
<https://www.energyplus.net/sites/all/modules/custom/nrel%5Fcustom/pdfs/pdfs%5Fv9.3.0/InputOutputReference.pdf>

## IBM Japan EnergyPlus RL Environment {#ibm-japan-energyplus-rl-environment}

- <https://github.com/IBM/rl-testbed-for-energyplus>
- <sup id="dcb6076827533dfad12b662fbd27e860"><a href="#Moriyama_Reinforcementlearningtestbed_2018" title="Moriyama, De Magistris, Tatsubori, Pham, Munawar \&amp; Tachibana, Reinforcement Learning Testbed for Power-Consumption Optimization, 45--59, in in: {Methods and Applications for Modeling and Simulation of Complex Systems}, edited by {Springer Singapore} (2018)">Moriyama_Reinforcementlearningtestbed_2018</a></sup>

## Alfalfa: Haystack implementation backed by a virtual building {#alfalfa-haystack-implementation-backed-by-a-virtual-building}

<https://github.com/NREL/alfalfa>

This is a Haystack implementation backed by a virtual building. Virtual building
simulation is performed using OpenStudio and EnergyPlus.

Runs on a docker instance.

## IEA EBC - Annex 81 - Data-Driven Smart Buildings {#iea-ebc-annex-81-data-driven-smart-buildings}

<https://annex81.iea-ebc.org/>

This project imagines a future world empowered by access to discoverable,
reliable, ubiquitous real-time data from buildings, such that digital solutions
can rapidly scale and where energy efficiency knowledge can be widely
encapsulated and disseminated within highly accessible software ‘Applications’.
Applications, in this context, are conceived as easy-to-configure and
instantiate software micro-services, built on top of a common software
infrastructure that facilitates data access under well-defined application
program interfaces (APIs), deployed on edge-computing devices or the cloud. Such
Applications are somewhat analogous to the ‘Apps‘ we use on personal mobile
devices.

By embracing modern IT approaches and advances in digital technology, the
project aims to overcome barriers to the provision of energy efficiency software
services, and reduce reliance on manual/onsite service delivery.

The project will investigate the potential of Software-as-a-Service innovation
and intelligent data-driven building automation, in order to reduce energy use
in buildings and enable buildings to participate as distributed energy resources
in support of increased use of variable renewable electricity sources.

The project objectives are to:

- provide the knowledge, standards, protocols and procedures for low-cost high-quality data capture, sharing and utilization in buildings
- develop a control-oriented building modelling framework that enables testing, development and assessment of the impact of alternative building HVAC control strategies in a digital environment
- develop building energy efficiency software Applications that can be used and ideally commercialized for reducing energy use in buildings
- drive the adoption of results through case studies, business model innovation and results dissemination

## The CityLearn Challenge {#the-citylearn-challenge}

- <https://sites.google.com/view/citylearnchallenge>
- <https://github.com/intelligent-environments-lab/CityLearn>

I checked and they use pre-simulated data...

![[2020-06-09_22-22-51_screenshot.png]]

### CityLearn {#citylearn}

CityLearn is an OpenAI Gym environment for the easy implementation of
reinforcement learning agents in a multi-agent demand response setting to
reshape the aggregated curve of electrical demand by controlling the storage of
energy by diverse types of buildings. Its main objective is to facilitate and
standardize the evaluation of RL agents such that it enables easy comparison of
different algorithms.

CityLearn allows to control the storage of domestic hot water (DHW), and chilled
water. CityLearn also includes energy models of air-to-water heat pumps,
electric heaters, and the pre-computed energy loads of the buildings, which
include space cooling, dehumidification, appliances, DHW, and solar generation.

### Motivation {#motivation}

Periods of high demand for electricity raise electricity prices and the overall
cost of power distribution networks. Flattening, smoothing, and reducing the
curve of electrical demand helps reduce operational and capital costs of
electricity generation, transmission, and distribution. Demand response is the
coordination of electricity consuming agents (i.e. buildings) in order to
reshape the overall curve of electrical demand.

Reinforcement learning (RL) has gained popularity in the research community as a
model-free and adaptive controller for the built-environment. RL has the
potential to become an inexpensive plug-and-play controller that can be easily
implemented in any building regardless of its model (unlike MPC), and coordinate
multiple buildings for demand response and load shaping. Despite its potential,
there are still open questions regarding its plug-and-play capabilities,
performance, safety of operation, and learning speed. Yet, a lack of
standardization on previous research has made it difficult to compare different
RL algorithms with each other, as different publications aimed at solving
different problems. It is also unclear how much effort was required to tune each
RL agent for each specific problem, or how well an RL agent would perform in a
different building or under different weather conditions.

In an attempt to tackle these problems, we have organized this challenge using
CityLearn, an OpenAI Gym Environment for the implementation of RL agents for
demand response at the urban level. The environment allows the implementation of
single-agent (as a centralized agent) and multi-agent decentralized RL
controllers.

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-08-03_10-25-14_screenshot.png]: ../attachments/Spawn-of-EnergyPlus/2020-08-03_10-25-14_screenshot.png "2020-08-03_10-25-14_screenshot.png"
[[2020-08-03_10-35-29_screenshot.png]: ../attachments/Open_Building_Control/2020-08-03_10-35-29_screenshot.png "2020-08-03_10-35-29_screenshot.png"
[[2020-06-09_22-22-51_screenshot.png]: ../attachments/The_CityLearn_Challenge/2020-06-09_22-22-51_screenshot.png "2020-06-09_22-22-51_screenshot.png"
[//end]: # "Autogenerated link references"