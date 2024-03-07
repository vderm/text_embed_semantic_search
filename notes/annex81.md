---
author:
- Vasken Dermardiros
- Clayton Miller
- Gabe Fierro
- Tianzhen Hong
- Zoltan Nagy
categories: note
date: 2020-06-01 00:00:00-04:00
draft: false
lastmod: 2021-01-03 22:49:02-05:00
tags:
- meeting
- annex-81
- mapping
- simulation
- model
- research
title: Annex 81 Webinar
---

## <span class="section-num">1</span> Crowdsource ML for Building Energy Prediction: Learning from the ASHRAE Great Energy Predictor III Kaggle Competition {#crowdsource-ml-for-building-energy-prediction-learning-from-the-ashrae-great-energy-predictor-iii-kaggle-competition}


### <span class="section-num">1.1</span> Crowdsource ML for Building Energy Prediction: Learning from the ASHRAE Great Energy Predictor III Kaggle Competition {#crowdsource-ml-for-building-energy-prediction-learning-from-the-ashrae-great-energy-predictor-iii-kaggle-competition}

Inability to compare various techniques from various sources/papers -> Need
common benchmark.

Slides available: <https://bit.ly/geps3-ashrae>


### <span class="section-num">1.2</span> Original Competition {#original-competition}

![[2020-06-18_19-09-39_screenshot.png]]

- Floppy disk was sent
- 150 entrants, 6 winners
- Creation of benchmarking techniques


### <span class="section-num">1.3</span> ASHRAE GEP III {#ashrae-gep-iii}

![[2020-06-18_19-11-25_screenshot.png]]


### <span class="section-num">1.4</span> ASHRAE GEP III {#ashrae-gep-iii}

![[2020-06-18_19-12-06_screenshot.png]]


### <span class="section-num">1.5</span> ASHRAE GEP III {#ashrae-gep-iii}

- 3 years of hourly data including weather data
- 10'000 more data than the original competition
- 62.5 mil data points
- 2380 different meters: electricity, hot an chilled water and steam meters
- Most from educational primary uses, then offices, public assembly, residential
    - From University campuses mostly
    - Across North America and Europe
- Using Root Mean Square Log Error (RMSLE)
    - Minimize impact of higher consuming buildings vs smaller ones


### <span class="section-num">1.6</span> Participants {#participants}

- 4370 participants who submitted 39'403 predictions
- 94 countries from across the world
- Winning team was matched on the platform, they didn't know each other.

![[2020-06-18_19-19-36_screenshot.png]]


### <span class="section-num">1.7</span> Solutions {#solutions}

**Solutions are all open**, top 3 are presenting in ASHRAE 2020 Virtual
Conference: June 22 to July 3, 2020

![[2020-06-18_19-21-45_screenshot.png]]

![[2020-06-18_19-21-33_screenshot.png]]


### <span class="section-num">1.8</span> Solutions {#solutions}

- <https://github.com/buds-lab/ashrae-great-energy-predictor-3-solution-analysis>
- Most work very well but very complicated; they're looking at ways to simplify
    the methods that they can be more scalable.
- Kaggle high levels achieved by sharing through notebooks, people give medals,
    etc.
- 96.1% people used Python, 3.9% used R
- Model used: gradient boosting, model stacking, neural network, linear
    regression
- A lot of preprocessing code: 45.8%, prediction models 34.2%
    - Removing outliers


### <span class="section-num">1.9</span> Building Data {#building-data}

<https://github.com/buds-lab/building-data-genome-project2>

$25'000 investment -> prize

Looking to host a **Great Predictor Competition IV**: Machine Learning for
Time-Series Building Data Tagging Translations


### <span class="section-num">1.10</span> Machine Learning vs Contextual Awareness {#machine-learning-vs-contextual-awareness}

- Most people were from building engineering and computer science
- To get a very high result, knowledge of building science lead
    - Outliers: which are true, which are errors? -> context helped
- How much data do we need?
    - Kaggle imposes restrictions so that it matches their other competitions
    - Competition-style ML vs real-world ML
    - Those 2 are different
    - Certain things would've made the approaches more useful, but not
        "competitively" enough


## <span class="section-num">2</span> A Platform for Data-Driver Analytics with Brick {#a-platform-for-data-driver-analytics-with-brick}


### <span class="section-num">2.1</span> A Platform for Data-Driver Analytics with Brick {#a-platform-for-data-driver-analytics-with-brick}

Programming, deploying, maintaining analytics in building, IoT is _hard_
&#x2026; lack of consistency of <span class="underline">data sources</span> and their <span class="underline">context</span>
-> we need **semantic metadata**.

- Extreme heterogeneity in buildings!
    - As-built/as-design etc are all different
- Info is rarely "written down"
    - In a machine-readable way
    - In a consistent way


### <span class="section-num">2.2</span> Porting {#porting}

![[2020-06-18_19-40-30_screenshot.png]]


### <span class="section-num">2.3</span> Porting in Reality {#porting-in-reality}

![[2020-06-18_19-40-46_screenshot.png]]


### <span class="section-num">2.4</span> Porting in Reality {#porting-in-reality}

- _Porting_ an application!
- Have to undertake this for <span class="underline">each individual building</span>.
- Metadata:
    - Human labels
    - Tags with dictionary -> Project **Haystack**
    - BIM -> wrong level of detail


### <span class="section-num">2.5</span> Brick Schema {#brick-schema}

![[2020-06-18_19-42-43_screenshot.png]]

Python application then queries the graph!


### <span class="section-num">2.6</span> Relationships {#relationships}

![[2020-06-18_19-44-59_screenshot.png]]


### <span class="section-num">2.7</span> Example {#example}

![[2020-06-18_19-46-05_screenshot.png]]


### <span class="section-num">2.8</span> Encoding application requirements with Brick {#encoding-application-requirements-with-brick}

Self-Customizing CPS Applications

- Query **semantic metadata** for a building
    - Control code customizes to this automatically&#x2026;

- SPARQL query: based on graph patterns
- Query definition encodes the types of data sources, relationships over things


### <span class="section-num">2.9</span> Encoding application requirements with Brick {#encoding-application-requirements-with-brick}

![[2020-06-18_19-48-04_screenshot.png]]


### <span class="section-num">2.10</span> Same Building: Different Model {#same-building-different-model}

![[2020-06-18_19-50-17_screenshot.png]]


### <span class="section-num">2.11</span> Prototype Available {#prototype-available}

![[2020-06-18_19-53-45_screenshot.png]]


### <span class="section-num">2.12</span> Various Applications {#various-applications}

- Rule-based FDD, etc. 105 lines of code -> applied to 50 buildings without
    changing anything!

- Version 2 in the works with a simplified API.


### <span class="section-num">2.13</span> Resources {#resources}

![[2020-06-18_19-55-57_screenshot.png]]


### <span class="section-num">2.14</span> Can ML create Bricks models? {#can-ml-create-bricks-models}

- How go about it?
    - Use analysis -> data between 50-80F -> temp sensor
    - Clustering -> parse 1 -> apply to rest
- Can Bricks be used to model occupant model data?
    - No, but can be extended -> occ count/types available
- Effort required?
    - Depends on what you want to use it for
- Controls to be included soon integrating Control description language (LBNL,
    Wetter) and Brick
- Work on translating IFC and BIM data to Bricks

**Marco Pritoni: Looking for people to share data to work on the platform**


## <span class="section-num">3</span> Data for New Insights into Building Performance {#data-for-new-insights-into-building-performance}


### <span class="section-num">3.1</span> Data for New Insights into Building Performance {#data-for-new-insights-into-building-performance}

![[2020-06-18_20-22-45_screenshot.png]]


## <span class="section-num">4</span> CityLearn {#citylearn}


### <span class="section-num">4.1</span> CityLearn {#citylearn}

www.citylearn.net

Intelligent Energy Management OpenAI Gym Environment

- Energy supply
- Energy storage
- Uncontrolled loads
- Electricity prices


### <span class="section-num">4.2</span> Goal {#goal}

Pre-simulated buildings, agent controls a storage system (action: {charge,
discharge}) that sites between the building and the grid. No influence on
building operation.

![[2020-06-18_20-39-58_screenshot.png]]


### <span class="section-num">4.3</span> Also see&#x2026; {#also-see-and-x2026}

- My co-supervisor Prof. Scott Bucking's work: community optimization
    - Better goal/cost function
- David Blum's thesis
- `cvxpower`


### <span class="section-num">4.4</span> Thesis Defence Online {#thesis-defence-online}

- Jose Ramon Vazquez-Canteli
- Date: August 7th, 2020, 2PM CDT (3PM New York, 9PM Berlin)
- Title: Multi-agent reinforcement learning for adaptive demand response in smart cities


### <span class="section-num">4.5</span> RL in Energy Management Special Issue {#rl-in-energy-management-special-issue}

![[2020-06-18_20-49-58_screenshot.png]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-06-18_19-09-39_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-09-39_screenshot.png "2020-06-18_19-09-39_screenshot.png"
[[2020-06-18_19-11-25_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-11-25_screenshot.png "2020-06-18_19-11-25_screenshot.png"
[[2020-06-18_19-12-06_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-12-06_screenshot.png "2020-06-18_19-12-06_screenshot.png"
[[2020-06-18_19-19-36_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-19-36_screenshot.png "2020-06-18_19-19-36_screenshot.png"
[[2020-06-18_19-21-45_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-21-45_screenshot.png "2020-06-18_19-21-45_screenshot.png"
[[2020-06-18_19-21-33_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-21-33_screenshot.png "2020-06-18_19-21-33_screenshot.png"
[[2020-06-18_19-40-30_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-40-30_screenshot.png "2020-06-18_19-40-30_screenshot.png"
[[2020-06-18_19-40-46_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-40-46_screenshot.png "2020-06-18_19-40-46_screenshot.png"
[[2020-06-18_19-42-43_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-42-43_screenshot.png "2020-06-18_19-42-43_screenshot.png"
[[2020-06-18_19-44-59_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-44-59_screenshot.png "2020-06-18_19-44-59_screenshot.png"
[[2020-06-18_19-46-05_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-46-05_screenshot.png "2020-06-18_19-46-05_screenshot.png"
[[2020-06-18_19-48-04_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-48-04_screenshot.png "2020-06-18_19-48-04_screenshot.png"
[[2020-06-18_19-50-17_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-50-17_screenshot.png "2020-06-18_19-50-17_screenshot.png"
[[2020-06-18_19-53-45_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-53-45_screenshot.png "2020-06-18_19-53-45_screenshot.png"
[[2020-06-18_19-55-57_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_19-55-57_screenshot.png "2020-06-18_19-55-57_screenshot.png"
[[2020-06-18_20-22-45_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_20-22-45_screenshot.png "2020-06-18_20-22-45_screenshot.png"
[[2020-06-18_20-39-58_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_20-39-58_screenshot.png "2020-06-18_20-39-58_screenshot.png"
[[2020-06-18_20-49-58_screenshot.png]: ../attachments/Annex_81_Webinar/2020-06-18_20-49-58_screenshot.png "2020-06-18_20-49-58_screenshot.png"
[//end]: # "Autogenerated link references"