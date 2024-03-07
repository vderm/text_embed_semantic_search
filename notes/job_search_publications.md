---
author: Vasken Dermardiros
categories: note
tags:
- organizing
- publication
title: Personal Publications
---

<https://orcid.org/0000-0001-5229-7764>


## Thesis

``` bibtex
@phdthesis{library987920,
            note = {Unpublished},
           month = {December},
            year = {2020},
           title = {Data-Driven Optimized Operation of Buildings with Intermittent Renewables and Application to a Net-Zero Energy Library},
          school = {Concordia University},
        keywords = {optimal control; net-zero energy building; reduced-order modelling; data-driven},
        abstract = {We are at the intersection of three major trends in the built environment where: (i) occupants' comfort, health and safety requirements are needed to support a productive workplace while maintaining a low operating cost, (ii) economic and environmental advantages are favouring an increased use of renewable energy generation and to reduce our reliance on fossil fuels, and (iii) major utilities will require regulation and are gradually shifting towards a more dynamic energy market. This thesis contributes a modelling and control framework that unifies and addresses these three points together.

This thesis contributes a methodology for the development of a bootstrapped ensemble-based low-order data-driven grey-box thermal models for supervisory-level optimal controls. The model is integral to a robust sampling-based predictive control (MPC) framework. This approach is directly applicable to most commercial buildings operating on a schedule and can be extended to consider occupant-driven spaces.

The methodology is applied to the Varennes Net-Zero Energy Library: Canada's first institutional net-zero energy building. Exogenous inputs are modelled to consider likely probabilistic outcomes for ambient temperature, cloudiness and interior plug loads. Bounding cases are simulated to contrast the proposed approach against conventional methods. MPC is applied to minimize various cost functions and emphasis is placed on a flexible profile-tracking cost function. The profile to track can be an open-market electrical price or a demand response signal thus improving the grid's flexibility while satisfying the building constraints and better utilizing its systems and storage. In a morning peak demand reduction case, given at least a 4-hour notice, our method is able to pre-heat the building, use minimal energy on-peak and yield the full benefits. Considering a profile tracking case to reduce grid interaction, a 10-12\% total energy reduction was achieved for winter where the space was gradually heated in the morning and evening while maximizing HVAC utilization during periods of large photovoltaic generation promoting self-consumption. A similar strategy would be near-impossible to handcraft without optimization-based approaches.

This proposed methodology can guide later implementations in the development of the next generation of low-cost cloud-connected controllers that are easy to deploy and can be adapted dynamically.},
          author = {Dermardiros, Vasken},
             url = {https://spectrum.library.concordia.ca/id/eprint/987920/}
}

@mastersthesis{library980456,
            note = {Unpublished},
           month = {September},
           title = {Modelling and Experimental Evaluation of an Active Thermal Energy Storage System with Phase-Change Materials for Model-Based Control},
            year = {2015},
          school = {Concordia University},
          author = {Dermardiros, Vasken},
             url = {https://spectrum.library.concordia.ca/id/eprint/980456/},
        abstract = {This thesis presents an experimental and numerical investigation of an active thermal energy storage (TES) system utilizing phase change material (PCM). The PCM-TES intended for building integration consists of PCM panels with active air circulation between the panels. Air is drawn through a channel to charge and discharge the PCM enabling the system to be used for both heating and cooling purposes - conditioned air, room air or outdoor air for night cooling can be utilized. This creates the possibility of a low thermal mass building to operate more like a high mass building and thereby gaining advantages commonly associated with traditional TES systems such as an ability to incorporate peak load reducing and shifting strategies without the significant weight of a traditional high mass building.

A prototype PCM-TES is built and tested in an environmental chamber. The experimental data collected is used for model validation. A 30th order non linear model with varying thermal capacitance \{C(T)\} is developed and compared for fitness to experimental data. A simplified 2nd order model is shown to adequately predict the dynamic response of the system for thermal charging/discharging and can be incorporated into model-based control systems, which are effective in peak load reducing and shifting strategies. Simplified models are easier to implement and calibrate since they contain fewer parameters to adjust which could be learned in real time (online calibration) by using measurements from the building automation system to compensate for installation and construction tolerances.

The model was extended to investigate the effect of increasing the exposed surface area to the air stream by having more air circulation channels while keeping the total air mass flow rate and convective heat transfer coefficients constant. Increasing the exposed area resulted in faster responding systems.

A case study was simulated to demonstrate the use of the simplified 2nd order non-linear PCM-TES model for heating peak load reduction. The PCM-TES was shown to reduce the peak by at least 50\% for the simulated conditions.}
}

```

## Publications (may not be complete)

``` bibtex
@article{Dermardiros2021,title = {Context-aware Model Predictive Control framework for multi-zone buildings},journal = {Journal of Building Engineering},year = {2021},volume = {42},author = {Mtibaa, F. and Nguyen, K.-K. and Dermardiros, V. and Cheriet, M.}},
@article{Dermardiros2021,title = {Online Genetic-Algorithm-based Model Predictive Control Framework for Multi-Zone Buildings},journal = {2021 European Control Conference, ECC 2021},year = {2021},pages = {1011-1017},author = {Mtibaa, F. and Nguyen, K.-K. and Dermardiros, V. and Cheriet, M.}},
@article{Dermardiros2019,title = {A simplified building controls environment with a reinforcement learning application},journal = {Building Simulation Conference Proceedings},year = {2019},volume = {2},pages = {956-964},author = {Dermardiros, V. and Bucking, S. and Athienitis, A.K.}},
@article{Dermardiros2019,title = {Energy Flexibility for an Institutional Building with Integrated Solar System: Case Study Analysis},journal = {IOP Conference Series: Earth and Environmental Science},year = {2019},volume = {352},number = {1},author = {Amara, F. and Dermardiros, V. and Athienitis, A.K.}},
@article{Dermardiros2019,title = {Energy flexibility for an institutional building with integrated solar system: Case study analysis},journal = {2019 IEEE Electrical Power and Energy Conference, EPEC 2019},year = {2019},author = {Amara, F. and Dermardiros, V. and Athienitis, A.K.}},
@article{Dermardiros2019,title = {Energy performance, comfort, and lessons learned from an institutional building designed for net zero energy},journal = {ASHRAE Transactions},year = {2019},volume = {125},pages = {682-695},author = {Dermardiros, V. and Athienitis, A.K. and Bucking, S.}},
@article{Dermardiros2019,title = {Simulation and performance analysis of an active PCM-heat exchanger intended for building operation optimization},journal = {Energy and Buildings},year = {2019},volume = {199},pages = {47-61},author = {Morovat, N. and Athienitis, A.K. and Candanedo, J.A. and Dermardiros, V.}},
@article{Dermardiros2018,title = {A numerical and experimental study of a simple model-based predictive control strategy in a perimeter zone with phase change material},journal = {Science and Technology for the Built Environment},year = {2018},volume = {24},number = {9},pages = {933-944},author = {Papachristou, A.C. and Vallianos, C.A. and Dermardiros, V. and Athienitis, A.K. and Candanedo, J.A.}},
@article{Dermardiros2018,title = {Distributed evolutionary algorithm for co-optimization of building and district systems for early community energy masterplanning},journal = {Applied Soft Computing Journal},year = {2018},volume = {63},pages = {14-22},author = {Bucking, S. and Dermardiros, V.}},
@article{Dermardiros2017,title = {Buildings integrated phase change materials: Modelling and validation of a novel tool for the energy performance analysis},journal = {Building Simulation Applications},year = {2017},volume = {2017-February},pages = {459-467},author = {Avagliano, G. and Buonomano, A. and Cellura, M. and Dermardiros, V. and Guarino, F. and Palombo, A.}},
@article{Dermardiros2017,title = {Model-based control of a hydronic radiant slab for peak load reduction},journal = {Building Simulation Conference Proceedings},year = {2017},volume = {3},pages = {1351-1359},author = {Dermardiros, V. and Vallianos, C. and Athienitis, A.K. and Bucking, S.}},
@article{Dermardiros2016,title = {Development of reduced-order thermal models of building-integrated active PCM-TES},journal = {ASHRAE Transactions},year = {2016},volume = {122},pages = {267-277},author = {Dermardiros, V. and Daoud, A. and Chen, Y. and Athienitis, A.K.}},
@article{Dermardiros2015,title = {Daylight performance of perimeter office fa?ades utilizing semi-transparent photovoltaic windows: A simulation study},journal = {Energy Procedia},year = {2015},volume = {78},pages = {334-339},author = {Kapsis, K. and Dermardiros, V. and Athienitis, A.K.}},
@article{Dermardiros2015,title = {Development of a new control strategy for improving the operation of multiple shades in a solarium},journal = {Solar Energy},year = {2015},volume = {122},pages = {277-292},author = {Bastien, D. and Dermardiros, V. and Athienitis, A.K.}},
@article{Dermardiros2015,title = {Modelling of an active PCM thermal energy storage for control applications},journal = {Energy Procedia},year = {2015},volume = {78},pages = {1690-1695},author = {Dermardiros, V. and Chen, Y. and Athienitis, A.K.}}
@phdthesis{library987920,month={December},year={2020},title={Data-Driven Optimized Operation of Buildings with Intermittent Renewables and Application to a Net-Zero Energy Library},school={Concordia University},keywords={optimal control; net-zero energy building; reduced-order modelling; data-driven},author={Dermardiros, Vasken},url={https://spectrum.library.concordia.ca/id/eprint/987920/}},
@thesis{library980456,month={September},title={Modelling and Experimental Evaluation of an Active Thermal Energy Storage System with Phase-Change Materials for Model-Based Control},year={2015},school={Concordia University},author={Dermardiros, Vasken},url={https://spectrum.library.concordia.ca/id/eprint/980456/},}}%
```
