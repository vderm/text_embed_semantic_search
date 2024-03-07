---
author:
- Vasken Dermardiros
categories: note
date: 2020-07-30 00:00:00-04:00
draft: false
lastmod: 2020-07-30 10:31:54-04:00
slug: occupancy_modeling
tags:
- research
- occupancy
- model
title: Occupancy Modeling
---

## <span class="section-num">1</span> Problem Statement {#problem-statement}

### <span class="section-num">1.1</span> TL;DR {#tl-dr}

Infer building schedule based on occupancy; admit fresh air as required;
condition space as required; reduce HVAC load; save.

Secondly, occupancy density estimation for COVID-19 compliance. Need for better
estimation techniques perhaps with additional sensors.

Thirdly, show clients how things were before BrainBox and after
BrainBox. Problem: data is collected during abnormal times, how offices are used
is transforming.

### <span class="section-num">1.2</span> Current practice {#current-practice}

Even before the pandemic, knowing occupancy can lead to
substantial savings and have a more tailored control system.

There exist many studies (search Liam O'Brian from Carleton, [IEA Annex 79](https://annex79.iea-ebc.org/)) that
show individual offices don't follow prescribed schedule (ASHRAE). Largely
outdated! But easy.

### <span class="section-num">1.3</span> _Desiderata_ {#desiderata}

Based on data we're collecting and using judgement, can we:

- Estimate if a space is occupied or unoccupied?
- Estimate when a space is likely to be occupied?
- Estimate when a space is likely to later become unoccupied?
- Estimate how long a space is occupied, i.e. what is the distribution of the
    length of stay? Basically, if the space becomes occupied, how long does it
    remain so? [F-distribution?]
- Estimate the impact of lunch breaks and coffee breaks
- Estimate the density of occupants: none, minimal (1 person), low, normal, high
    (flag for covid?)

### <span class="section-num">1.4</span> When CO<sub>2</sub> isn't available {#when-co-isn-t-available}

For buildings without CO<sub>2</sub> sensors, we need to rely on the thermal models. Since
COVID, occupant-based loads in offices are practically nil. This can serve as a
baseline &#x2013;> anything OoD can be attributated to occupants returning to the
office.

### <span class="section-num">1.5</span> Edmonton Tower: 839 {#edmonton-tower-839}

See the [Jupyter Notebook](https://git.brainboxai.net/vdermardiros/Occupancy%5FEstimation)!

In this file, we are obtaining and plotting zone-level data from Edmonton Tower
space 839 which is an ****open office space**** [top left space] (building ID: 20,
building<sub>name</sub>: EDM-AIMCO-EdTower, database: EDM<sub>104EdmTower</sub>, table:
TL<sub>measures</sub>).

### <span class="section-num">1.6</span> How the air system works {#how-the-air-system-works}

Edmonton tower is a LEED-Gold (or -Platinum?) building

- Cooling by chilled beams
- Fresh air based on CO<sub>2</sub> (on-demand ventilation)
- When building is **occupied** based on a schedule, the system admit the minimum amount of fresh air

into a space

- More people (people exhale CO<sub>2</sub> btw) = more and more fresh air
- When people leave, the system is turned OFF.

### <span class="section-num">1.7</span> CO<sub>2</sub> concentration decay {#co-concentration-decay}

Over time, the CO<sub>2</sub> in the space slowly leaks out towards the exterior (through
small cracks/openings, through the elevator shaft, etc. &#x2013; interesting way to
assess the air-tightness of a building btw).

Same
behaviour in thermal conductance or any system under a
concentration gradient (CO<sub>2</sub> inside != outside, so things will tend towards an
equilibrium state &#x2013;> CO<sub>2</sub> inside == outside as t &#x2013;> infinite)

### <span class="section-num">1.8</span> Exponential decay {#exponential-decay}

$\frac{\delta CO_2}{\delta t} = -\lambda CO_2$

with the solution:

$CO_2(t) = CO_2^{t=0} e^{-\lambda t}$

Where $\lambda$ represents a leakage or diffusion rate.

### <span class="section-num">1.9</span> Modeling {#modeling}

Need to add to previous equation:

1. term to represent the CO<sub>2</sub> generation rate (multiplied by the number of
    people &#x2013; assume all same activity level == same CO<sub>2</sub> output per person),
2. bias representing the outside CO<sub>2</sub> concentration (close to 400 ppm in
    Edmonton as per the data),
3. consider the HVAC system that is diluting the air in the space with fresh air
    (concentration of CO<sub>2</sub> of supplied air == outside CO<sub>2</sub>).

### <span class="section-num">1.10</span> NOTE: Concentration vs total amount {#note-concentration-vs-total-amount}

The thermostat in the room is measuring a CO<sub>2</sub> concentration (= amount of
CO<sub>2</sub> in space / volume of space). People are releasing CO<sub>2</sub> molecules over time.

So we need to know the volume of the space (4), but Robert has a way to estimate
this or we can assume a density of people per floor area (pre-COVID).

## <span class="section-num">2</span> Estimating occupancy in heterogeneous sensor environment {#estimating-occupancy-in-heterogeneous-sensor-environment}

### <span class="section-num">2.1</span> Estimating occupancy in heterogeneous sensor environment {#estimating-occupancy-in-heterogeneous-sensor-environment}

- <sup id="267362612ff2ba2a5c089f1b7a870d84"><a href="#Amayri_Estimatingoccupancyheterogeneous_2016" title="Amayri, Arora, Ploix, Bandhyopadyay, Ngo \&amp; Badarla, Estimating Occupancy in Heterogeneous Sensor Environment, {Energy and Buildings}, v(), 46--58 (2016).">Amayri_Estimatingoccupancyheterogeneous_2016</a></sup>
- Amayri, M., Arora, A., Ploix, S., Bandhyopadyay, S., Ngo, Q., & Badarla, V.
    R., Estimating occupancy in heterogeneous sensor environment, Energy and
    Buildings, 129(), 46–58 (2016).
    <http://dx.doi.org/10.1016/j.enbuild.2016.07.026>

### <span class="section-num">2.2</span> Approach {#approach}

- Using: temperature, RH, luminance, motion detection, power consumption, CO<sub>2</sub>
    concentration, microphone and/or door/window positions
- Most information gain
- Modeling approach: decision tree -> human interpretable
- Lit review suggests CO<sub>2</sub> measurements are useful
- Time bins: {Night: 20-8, Pre-lunch: 8-12, Lunch: 12-14, Post-lunch: 14-20}
    [French study]
- Additional features: &Delta; T(in-out), &Delta; CO<sub>2</sub>

### <span class="section-num">2.3</span> CO<sub>2</sub> model (see ASHRAE Fundamentals) {#co-model--see-ashrae-fundamentals}

![[2020-07-30_09-10-24_screenshot.png]]

### <span class="section-num">2.4</span> Fit {#fit}

Use an iterative nonlinear optimization approach to fit invariant parameters S,
C<sub>out</sub>, Q<sub>out</sub><sup>0</sup>, Q<sub>cor</sub><sup>0</sup>, Q<sub>W</sub> and Q<sub>D</sub>; minimize error between ground truth
and predicted number of people.

**Information we don't have!**

## <span class="section-num">3</span> IEA Annex 66 Technical Report {#iea-annex-66-technical-report}

### <span class="section-num">3.1</span> IEA Annex 66 Technical Report {#iea-annex-66-technical-report}

- Annex 66: Definition and Simulation of Occupant Behavior in Buildings
    Technical Report: Occupant Behavior Modeling Approaches and Evaluation
- [Link to report](https://annex66.org/sites/default/files/2018FinalReport/Annex%2066%20Deliverable%20-%20Occupant%20behavior%20modeling%20approaches%20and%20evaluation.pdf)

Largest concerns: plug-in appliance use, light switch, blind operation; visual
and thermal discomfort

### <span class="section-num">3.2</span> Modeling non-adaptive behaviours: schedules {#modeling-non-adaptive-behaviours-schedules}

- Schedules: ratio of people present given time of day
- Discrete-time Markov models: likelihood of an arrival when occupants are
    absent, likelihood of a departure when occupants are present; weakness:
    arrival and departure are independent whereas people tend to leave early if
    they came in early
- Survival models

### <span class="section-num">3.3</span> Schedule {#schedule}

![[2020-07-30_08-37-03_screenshot.png]]

- Advantage: easy and straightforward, archetype buildings
- Limitation: not adaptive to local effects and to peoples' responses

### <span class="section-num">3.4</span> Discrete-time Markov model {#discrete-time-markov-model}

![[2020-07-30_08-44-35_screenshot.png]]

- Advantage: model transitions that may not be symmetric
- Limitation: treats certain events independently, detecting events may be
    difficult

- See also <sup id="c5a99978d22faaff09dd34544d06b3f6"><a href="#Jia_Occupancymodellingshared_2017" title="Jia \&amp; Spanos, Occupancy Modelling in Shared Spaces of Buildings: A Queueing Approach, {Journal of Building Performance Simulation}, v(4), 406--421 (2017).">Jia_Occupancymodellingshared_2017</a></sup>: Jia, R., & Spanos, C.,
    Occupancy modelling in shared spaces of buildings: a queueing approach,
    Journal of Building Performance Simulation, 10(4), 406–421 (2017).
    <http://dx.doi.org/10.1080/19401493.2016.1267802>
  - Able to reproduce variations of occupancy, peak occupancy time, first
        arrival (Poisson distribution) and last departure times, occupied duration
        (exponential distribution); fits per day of week

### <span class="section-num">3.5</span> Survival model {#survival-model}

![[2020-07-30_08-45-27_screenshot.png]]

- Advantage: methods can be transferred to other building models and archetypes
- Limitation: rounding errors since keeping track of events over time

## <span class="section-num">4</span> Realistic Schedule for Office Spaces for BEM {#realistic-schedule-for-office-spaces-for-bem}

### <span class="section-num">4.1</span> Realistic Schedule for Office Spaces for BEM {#realistic-schedule-for-office-spaces-for-bem}

- Simulator: <http://occupancysimulator.lbl.gov/>
- Method based on Markov-chain model, see [their report](https://simulationresearch.lbl.gov/sites/all/files/t%5Fhong%5F-%5Fan%5Fagent-based%5Fstochastic%5Foccupancy%5Fsimulator.pdf)
- [Occupant Behavior Research at LBNL BTUS](https://behavior.lbl.gov/)

![[2020-07-30_08-55-43_screenshot.png]]

## <span class="section-num">5</span> A Bayesian approach for probabilistic classification and inference of occupant thermal preferences in office buildings {#a-bayesian-approach-for-probabilistic-classification-and-inference-of-occupant-thermal-preferences-in-office-buildings}

### <span class="section-num">5.1</span> A Bayesian approach for probabilistic classification and inference of occupant thermal preferences in office buildings {#a-bayesian-approach-for-probabilistic-classification-and-inference-of-occupant-thermal-preferences-in-office-buildings}

- <sup id="676b731b7cdb87169d73b6a3da1b4559"><a href="#Lee_Bayesianapproachprobabilistic_2017" title="Lee, Bilionis, Karava \&amp; Tzempelikos, A {{Bayesian}} Approach for Probabilistic Classification and Inference of Occupant Thermal Preferences in Office Buildings, {Building and Environment}, v(), 323--343 (2017).">Lee_Bayesianapproachprobabilistic_2017</a></sup>: Lee, S., Bilionis, I., Karava,
    P., & Tzempelikos, A., A Bayesian approach for probabilistic classification
    and inference of occupant thermal preferences in office buildings, Building
    and Environment, 118(), 323–343 (2017).
    <http://dx.doi.org/10.1016/j.buildenv.2017.03.009>
  - "Different people prefer different thermal conditions"
  - Influenced by (1) overall thermal stress [prior knowledge], (2) personal
        thermal preference characteristic [hidden variable]
  - Approach: build profiles (5); new occupants are a mixture of these profiles
        -> data efficient

### <span class="section-num">5.2</span> Clustering {#clustering}

![[2020-07-30_10-21-23_screenshot.png]]

### <span class="section-num">5.3</span> Graphical model {#graphical-model}

![[2020-07-30_10-22-17_screenshot.png]]

In the paper, they break down every component into equations based on Fanger's
comfort model [in Appendix] or other physical quantities/relationships.

### <span class="section-num">5.4</span> Thermal preference {#thermal-preference}

![[2020-07-30_09-27-51_screenshot.png]]

### <span class="section-num">5.5</span> Fahimeh's preference xp {#fahimeh-s-preference-xp}

![[2020-07-30_09-28-10_screenshot.png]]

## <span class="section-num">6</span> Inference of thermal preference profiles for personalized thermal environments with actual building occupants {#inference-of-thermal-preference-profiles-for-personalized-thermal-environments-with-actual-building-occupants}

### <span class="section-num">6.1</span> Inference of thermal preference profiles for personalized thermal environments with actual building occupants {#inference-of-thermal-preference-profiles-for-personalized-thermal-environments-with-actual-building-occupants}

- <sup id="8a2b2d83736694af2265b70c137369eb"><a href="#Lee_Inferencethermalpreference_2019a" title="Lee, Karava, Tzempelikos \&amp; Bilionis, Inference of Thermal Preference Profiles for Personalized Thermal Environments with Actual Building Occupants, {Building and Environment}, v(), 714--729 (2019).">Lee_Inferencethermalpreference_2019a</a></sup>: Lee, S., Karava, P., Tzempelikos,
    A., & Bilionis, I., Inference of thermal preference profiles for personalized
    thermal environments with actual building occupants, Building and Environment,
    148(), 714–729 (2019). <http://dx.doi.org/10.1016/j.buildenv.2018.10.027>
  - Tuning approach

![[2020-07-30_09-29-59_screenshot.png]]

## <span class="section-num">7</span> Implementation of a self-tuned HVAC controller to satisfy occupant thermal preferences and optimize energy use {#implementation-of-a-self-tuned-hvac-controller-to-satisfy-occupant-thermal-preferences-and-optimize-energy-use}

### <span class="section-num">7.1</span> Implementation of a self-tuned HVAC controller to satisfy occupant thermal preferences and optimize energy use {#implementation-of-a-self-tuned-hvac-controller-to-satisfy-occupant-thermal-preferences-and-optimize-energy-use}

- <sup id="af402877d987e2f5fedbb6b6ca080881"><a href="#Lee_ImplementationselftunedHVAC_2019a" title="Lee, Joe, Karava, Bilionis \&amp; Tzempelikos, Implementation of a Self-Tuned {{HVAC}} Controller to Satisfy Occupant Thermal Preferences and Optimize Energy Use, {Energy and Buildings}, v(), 301--316 (2019).">Lee_ImplementationselftunedHVAC_2019a</a></sup>: Lee, S., Joe, J., Karava, P.,
    Bilionis, I., & Tzempelikos, A., Implementation of a self-tuned HVAC
    controller to satisfy occupant thermal preferences and optimize energy use,
    Energy and Buildings, 194(), 301–316 (2019).
    <http://dx.doi.org/10.1016/j.enbuild.2019.04.016>
  - Case study using adaptive comfort model, grey-box model for system, MPC,
        radiant system

### <span class="section-num">7.2</span> Methodology {#methodology}

![[2020-07-30_10-15-01_screenshot.png]]

### <span class="section-num">7.3</span> Bound sensitivity {#bound-sensitivity}

![[2020-07-30_10-14-03_screenshot.png]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-07-30_09-10-24_screenshot.png]: ../attachments/Estimating_occupancy_in_heterogeneous_sensor_environment/2020-07-30_09-10-24_screenshot.png "2020-07-30_09-10-24_screenshot.png"
[[2020-07-30_08-37-03_screenshot.png]: ../attachments/IEA_Annex_66_Technical_Report/2020-07-30_08-37-03_screenshot.png "2020-07-30_08-37-03_screenshot.png"
[[2020-07-30_08-44-35_screenshot.png]: ../attachments/IEA_Annex_66_Technical_Report/2020-07-30_08-44-35_screenshot.png "2020-07-30_08-44-35_screenshot.png"
[[2020-07-30_08-45-27_screenshot.png]: ../attachments/IEA_Annex_66_Technical_Report/2020-07-30_08-45-27_screenshot.png "2020-07-30_08-45-27_screenshot.png"
[[2020-07-30_08-55-43_screenshot.png]: ../attachments/Realistic_Schedule_for_Office_Spaces_for_BEM/2020-07-30_08-55-43_screenshot.png "2020-07-30_08-55-43_screenshot.png"
[[2020-07-30_10-21-23_screenshot.png]: ../attachments/A_Bayesian_approach_for_probabilistic_classification_and_inference_of_occupant_thermal_preferences_in_office_buildings/2020-07-30_10-21-23_screenshot.png "2020-07-30_10-21-23_screenshot.png"
[[2020-07-30_10-22-17_screenshot.png]: ../attachments/A_Bayesian_approach_for_probabilistic_classification_and_inference_of_occupant_thermal_preferences_in_office_buildings/2020-07-30_10-22-17_screenshot.png "2020-07-30_10-22-17_screenshot.png"
[[2020-07-30_09-27-51_screenshot.png]: ../attachments/Review_of_Work_from_Purdue_University/2020-07-30_09-27-51_screenshot.png "2020-07-30_09-27-51_screenshot.png"
[[2020-07-30_09-28-10_screenshot.png]: ../attachments/Review_of_Work_from_Purdue_University/2020-07-30_09-28-10_screenshot.png "2020-07-30_09-28-10_screenshot.png"
[[2020-07-30_09-29-59_screenshot.png]: ../attachments/Review_of_Work_from_Purdue_University/2020-07-30_09-29-59_screenshot.png "2020-07-30_09-29-59_screenshot.png"
[[2020-07-30_10-15-01_screenshot.png]: ../attachments/Review_of_Work_from_Purdue_University/2020-07-30_10-15-01_screenshot.png "2020-07-30_10-15-01_screenshot.png"
[[2020-07-30_10-14-03_screenshot.png]: ../attachments/Review_of_Work_from_Purdue_University/2020-07-30_10-14-03_screenshot.png "2020-07-30_10-14-03_screenshot.png"
[//end]: # "Autogenerated link references"