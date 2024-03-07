---
author: Vasken Dermardiros
categories: note
tags:
- inbox
title: Inbox
---

## Software

### Fundamentals

- [Design patterns](https://refactoring.guru)
- The original "blue book", Domain-Driven Design by Eric Evans (Addison-Wesley Professional)
- The "red book", Implementing Domain-Driven Design by Vaughn Vernon (Addison-Wesley Professional)
- [[big_O]], e.g. [sorting algorithms](https://www.bigocheatsheet.com/)
- [[data_types]]

### General programming

- [Programming learning resources](https://matklad.github.io/2023/08/06/fantastic-learning-resources.html)
  - [CSES problem set](https://cses.fi/problemset/): a bunch of problems to solve
  - [Project Euler](https://projecteuler.net/archives): more problems
- [[oop-is-dead-long-live-data-oriented-design]]
- [[unlearn-oop]]
- [[better-software-architecture-for-saas-startups]]: that long Django article
- [Kraken Technologies: How we organise our very large Python monolith](https://blog.europython.eu/kraken-technologies-how-we-organize-our-very-large-pythonmonolith/)
- [[programming_tags]]: TODO, FIXME, SOURCE, ASSUMPTION, NOTE, USELATER, UNUSED, TEMPORARY, MISSING, XXX, HACK, BUG.
- [[code_review]]
- [[json-yaml-toml]]
- [Magical: autofill stuff](https://www.getmagical.com/)
- [UML diagrams](https://plantuml.com/) and [UML editor](https://www.planttext.com/)
- [Mermaid (upgrade to UML)](https://mermaid.js.org/#/)
- [RegEx testing](https://regexr.com/)
- Reuseable pipelines like [Airflow](https://airflow.apache.org/) but not as crazy:
  - [Snakemake](https://snakemake.github.io/) can use any programming languages, most examples for gene stuff, not sure if I'm crazy about loading/saving files for every step. Would perhaps want to have the full graph available for it to be optimized down.
    - [Example for unsupervised analysis](https://github.com/epigen/unsupervised_analysis)
  - [Luigi](https://luigi.readthedocs.io/en/stable/running_luigi.html) this is in Python
  - Then again, some people argue that using [Makefiles](https://drivendata.github.io/cookiecutter-data-science/#analysis-is-a-dag) are sufficient with [Parallel](https://www.gnu.org/software/parallel/)

### Linux

- [[git]]
- [[vim]]
- [[bash]]
- [[tmux]]
- [[parallel]]
- [[awk]]
- [[sed]]
- [Linux commands, shortcuts](https://xmind.app/m/WwtB/)
- <https://explainshell.com/>
- [Systemd services](https://www.shellhacks.com/systemd-service-file-example) and [two](https://fedoramagazine.org/systemd-template-unit-files)
- [FZF](https://www.freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff/)

### Python

- [[idiomatic-python]]
- [[python-properties]]: `@property`
- [Better Python 59 Ways](https://github.com/SigmaQuan/Better-Python-59-Ways)
- [[functional-programming-howto]], however, Python list comprehensions prefered
- [[architecture-patterns-with-python]]
- [[pytest]]
- [Cloud-Native Pytest Tips and Tricks from Ground Zero](https://www.youtube.com/watch?v=EOCtbjuICbA&list=PL57ryHEtR9W7He66XAkHUkMQvYLABGSuO&index=2&t=2689s)
- [[presentation_logging]] and [[presentation_logging.pdf]]
- [[the_naming_algorithm.jpeg]]
- [[jax]]
- [A basic introduction to NumPy's einsum"](https://ajcr.net/Basic-guide-to-einsum/) and [wiki](https://en.wikipedia.org/wiki/Einstein_notation)
- [Dependency graphs using pydeps](https://github.com/thebjorn/pydeps)
  - better to just use poetry

### Julia

- [[julia]]
- [[Julia-cheatsheet.pdf]]
- [[state-of-ml-in-julia]]
- [AI for HVAC: How Julia Computing Uses Machine Learning to Tackle Building Efficiency with JuliaSim](https://www.youtube.com/watch?v=_G9jfE-xNFM)

### Cloud

- [[aws-cli]]
- [Ideal CI/CD pipeline](https://www.youtube.com/watch?v=OPwU3UWCxhw)
  - need to run cron jobs on API endpoints -> hardcode response/reaction and monitor this (canary function)
  - traffic balancing -> 10% to pre-full-production - 90% production
- [[microservices]]
- [gRPC](https://grpc.io/docs/what-is-grpc/introduction/)
- [[containerization]]
- [[k3s]]
- [[udemy-course-docker]]
- [[udemy-course-kubernetes]]
- [[dramble]]: had set this up with k3s and also to [read measurements following a YouTube video and IOTStack](https://www.youtube.com/watch?v=_DO2wHI6JWQ&ab_channel=LearnEmbeddedSystems)
- [[databases]]
  - [[s3bucket]]
  - [[influxdb]]
- [Frugal solo dev tech stack](https://getwaitlist.com/blog/solo-dev-startup-stack)
- [[farm-stack]]
- [Locust Python-based API load testing](https://locust.io/)
- [[swagger_client]]: to be used with FastAPI and other `openapi.json`-compatible APIs

### MLOps

- [MLE Book](http://www.mlebook.com/wiki/doku.php), Fede's fave
- [MLOps book and DTU course](https://skaftenicki.github.io/dtu_mlops)
- [Curated list of MLOps projects](https://mlops.toys/)
- [Models in prod](https://towardsdatascience.com/hugging-face-transformer-inference-under-1-millisecond-latency-e1be0057a51c)
- [[practical-mlops]]
- ML Test Score [[Breck_MLTestScore_2017.pdf]]: Google article to test how ML-production-ready the company is: checklist
- [[visulize-pytorch-model]]

### Other programming languages

- [[lua]]: cute programming language
- used to build games in [pico-8](https://www.lexaloffle.com/pico-8.php), which saves the game as a png "cartridge"
- [apl](https://tryapl.org/): array-oriented programming
- [orca](https://100r.co/site/orca.html): 2-d music programming language
  - made by [100 rabbits](https://100r.co/site/home.html) and they also have lots of cool minimal projects
- should learn [TypeScript](https://learnxinyminutes.com/docs/typescript/) at some point maybe

## Data science, (Sci)ML, modeling, controls

- [Super VIP Cheatsheet](https://github.com/afshinea/stanford-cs-229-machine-learning/blob/master/en/super-cheatsheet-machine-learning.pdf) or [[super-cheatsheet-machine-learning.pdf]]
- [[f1-score]]
- [[statistics-sensitivity-analysis]]
- [The intuition behind Shannon's Entropy](https://towardsdatascience.com/the-intuition-behind-shannons-entropy-e74820fe9800)
  - entropy: $H(x) = -\sum_x ( p(x) \cdot log(p(x) ) = \sum_x ( p(x) \cdot log(1/p(x) )$
  - if event 1 has prob 0.75 and event 2 has prob 0.25, entropy = $0.75 \cdot log(1/0.75) + 0.25 \cdot log(1/0.25) = 0.81$
  - how information is contained in a message? how compressed is it? by knowing some, how much of the rest collapses? unlikely event has higher entropy -> it's "news", suprise, etc
- [[principle-of-least-action]]]: Richard Feynman
+ Binary cross entropy loss typically used for binary classification: <https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a>
  + If you know the real distribution of data, then we can calculate the entropy in the data. (Worst case is a 50-50 split in a binary case). If we don't know the true distribution of the data (usually the case), then we instead use a cross-entropy. The difference between the entropy and cross-entropy is the KL-divergence! It's a measure of dissimilarity between two distributions. Probability of selecting a data point is $1/N$ if we have $N$ points.
+ [Visual Informtion Theory](http://colah.github.io/posts/2015-09-Visual-Information/)

### EDA

- [pygwalker: Tableau but for Python](https://github.com/Kanaries/pygwalker)
- [ydata-profiler, formerly pandas-profiler](https://github.com/ydataai/ydata-profiling)
- [[Runge_DetectingQuantifyingCausal_2019.pdf]] with the [tigramite Python package](https://github.com/jakobrunge/tigramite)

### Data Science, SciML

- [Streamlit code generation for ML image recognition](https://traingenerator.jrieke.com) and it's [Github repo](https://github.com/jrieke/traingenerator#adding-new-templates)
- [PerceptiLabs Model weight inspector](https://www.perceptilabs.com/papers)
- [Model predictive control python toolbox](https://www.do-mpc.com/en/latest/)
- [SciML book](https://github.com/SciML/SciMLBook) and [Course](https://book.sciml.ai)
- [Better goodness of fit evaluations](https://medium.com/microsoftazure/how-to-better-evaluate-the-goodness-of-fit-of-regressions-990dbf1c0091)
- BROKEN LINK, catapult example: <https://fluxml.ai/blog/2019/03/05/dp-vs-rl.html>
- [Neural ODE in JaX](https://colab.research.google.com/drive/1o2jWvmrQYjX99hZpTF415uT1rc35Mvft?usp=sharing)
- [Diffrax: ODE, etc](https://github.com/patrick-kidger/diffrax)
- [PPO code from CleanRL](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo.py)
  - [Proximal Policy Optimization (PPO) Explained](https://towardsdatascience.com/proximal-policy-optimization-ppo-explained-abed1952457b)
- [Physics-Based Deep Learning](https://physicsbaseddeeplearning.org/intro.html)
  - [Intro to Physics-Based Deep Learning book](https://www.youtube.com/watch?v=SU-OILSmR1M&t=3s)
  - [Examples and blog](https://ge.in.tum.de/)
- [Gradient boosting tutorial](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)
- [DDPS | Differentiable Programming for Modeling and Control of Dynamical Systems by Jan Drgona](https://www.youtube.com/watch?v=_iN2cggDY7E)
  - [Neuromancer SI](https://github.com/pnnl/neuromancer/tree/master/examples/system_identification)
  - [Differentiable Predictive Control by Draguna Vrabie](https://crossminds.ai/video/differentiable-predictive-control-614bbf633c7a224a90901ef5/)
- [Decision awareness in reinforcement learning](https://darl-workshop.github.io/)
- [Computational Linear Algebra for Coders (FastAI)](https://github.com/fastai/numerical-linear-algebra)
  - YouTube videos: [Computational Linear Algebra 1: Matrix Math, Accuracy, Memory, Speed, & Parallelization](https://www.youtube.com/watch?v=8iGzBMboA0I&list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY&index=2)
- [Halide Talk: Parallelism, Cache](https://www.youtube.com/watch?v=3uiEyEKji0M)
- [[differentiable_programming_from_scratch]]
- [[differentiable_programming_for_modeling_and_control_of_dynamical_systems]]
- [[linear-mpc-state-space]]
- [[state-of-ml-in-julia]]
- [[the-use-and-practice-of-scientific-machine-learning]]
- [[model_based_machine_learning]]

### Optimization

- [Ceres: non-linear solver by Google](http://ceres-solver.org/index.html)
- [MiniZinc: constraint modeling language](https://www.minizinc.org/)

### ML Resources

- [[reinforcement-learning]]
- [[a-brief-introduction-to-causal-inference]]
- [[deepmind_deep_learning_lectures]]
- [[deepmind_muzero]]
- [Distill.pub](https://distill.pub/): publications about hot ML topics; not updated as often and I think the author sort of stopped doing them
- [Andrej Karphaty's videos](https://www.youtube.com/@AndrejKarpathy/videos): He was the head of AI at Tesla and is now working again at OpenAI. He also has this repo that's an interesting learn
- [MicroGrad](https://github.com/karpathy/micrograd)
- [tinygrad](https://github.com/tinygrad/tinygrad)
- [DL book](https://www.deeplearningbook.org/): classic deep learning book at this point by Goodfellow (inventor of GANs), Bengio and Courville
- [Rich Sutton's Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) writing of Rich Sutton about how software should be approached
- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) Andrej Karpathy's "Software 2.0" and with transformers, we are there
- [HuggingFace](https://huggingface.co/) this is the github-equivalent to ml models
- [Andrew Ng's ML course](https://www.coursera.org/specializations/machine-learning-introduction) the OG online course about Deep Learning by Andrew Ng
- [David Silver's RL course](https://www.youtube.com/watch?v=C9JGEfFF_EQ&list=PL8Ndnh4x737oIVNEQw2KM7FPmGDg2odKK) the OG online course about Reinforcement Learning by David Silver
- [Chris Rauckauckus' UDE workshop](https://www.youtube.com/watch?v=QwVO0Xh2Hbg) Universal Differential Equations workshop, part of Scientific Machine learning SciML

### Simulation, HVAC statistics and other tools

- [[digital-twin]] using [[haystack]] tags
- [[rtu-solution]]
- [[project_impetus]]
- [[competitor_companies_to_bbai]] other HVAC and grid optimization companies
- [[open-source-projects]] and [[physical-simulations]]: HVAC and building energy related projects available online.
  - [EnergyPlus Gym](https://energym.readthedocs.io/en/latest/pages/environments.html)
  - [NYSERDA client](https://onboard-data-python-client-api.readthedocs.io/en/latest/index.html)
  - [Prototype Building Models](https://www.energycodes.gov/prototype-building-models)
- [EEmeter: tools for calculating metered energy savings](http://eemeter.openee.io/)
- [AI for HVAC: How Julia Computing Uses Machine Learning to Tackle Building Efficiency with JuliaSim](https://www.youtube.com/watch?v=_G9jfE-xNFM)
- [CBECS](https://www.eia.gov/consumption/commercial/)
- [IBPSA-BOPTEST controls simulation in Python and Julia by D.Blum](https://github.com/ibpsa/project1-boptest), they also have a Gym environment
- Model composition paper take home message: if auto-correlation between residuals (ACF) is low, no more information left in the data; also check cumulated peridogram of the residuals.

## Transformers and LLM
+ [Transformer Deploy ELS-RD](https://github.com/ELS-RD/transformer-deploy)
    + This is the production code to run the models. Not too many details on the models themselves; need to check the code.
+ [Fine-tuning a model](https://pytorch.org/tutorials/beginner/finetuning_torchvision_models_tutorial.html): This is the case where you have a pretrained model and only want to add a layer at the top

## Business

### Startup market

- [[saas-financial-models]]
- [[saas_metrics]]
- [[saas_pricing_model]]
- [[start-ups]]: stock options: a deal gone bad; founder rule; premature scaling.
- <https://www.techstars.com/>
- <https://www.nextcanada.com/next-ai-fr/>
- <https://www.ycombinator.com/blog/rfs-climatetech>

### Energy market and renewables

- <https://www.iea.org/reports/world-energy-outlook-2022>
- <https://www.iea.org/fuels-and-technologies/renewables>

### Business books

- [[ai-canvas]]: AI start-ups have to fill the canvas
- [[rework]]: more of a "fun" book. One-liners given and then explained. Sometimes goes counter-sense from what we're taught, but it really makes sense in practice.
- [[great-at-work]]: do less and obsess; redesign your work; don't just learn, loop; passion and purpose; forceful champions; fight and unite; two signs of collaboration.
- [[prioritization-the-other-definition]]: order a todo list and do only the top item. Lower maintenance is better than new features. Say no; focus; and maintain flexibility.
- [[bullshit-jobs]]
- [[the-leader-you-want-to-be]]: Five Essential Principles for Bringing Out Your Best Self Ever Day. Leader A vs B lens: assessing the pitfalls of doing given the leader you feed. Delegate, trust, inspire vs taking it on yourself.
- [[leadership-foundation]]: types of managers with their pros and cons.
- [[way-of-the-wolf]]: "The Three Tens" of certainty, lower the action threshold, raise the pain threshold; logical and emotional certainty. People make a judgment in 4 seconds.
- [[48-laws-of-power]] and [[the-art-of-seduction]]
- [[bargaining-for-advantage]]: getting to know what kind of negotiator you are to better build the approaches needed to gain the advantage you want; about setting expectations and building relationships.
- [[getting-to-yes]]: classic book on negotiation based on working together on a problem instead of working on the person.
- [[the-10-commandments-of-salary-negotiation]] and <https://candor.co/offers>
- [[business-model-generation]]: shaping a product, offering, customers, finances.
- [[influencing-notes]]: notes from an exchange with my aunt.

### Management

- [[managers_playbook]]
- [[self-managed-team]]: hire well, manage little.
- [[goals]]: more than goals, explains about purpose, note-taking, covid-tax, etc.
- [[AI-team-revamp]]
- [[100-lessons-from-1-year-of-AI-research]]
- [[designing-a-better-career-path-for-designers]] from Facebook/Meta, also see [Dropbox Engineering Career Framework](https://dropbox.github.io/dbx-career-framework/)
- [[how-to-interview-engineers]]: talent, judgement, personality, theatrics.
- [[how-tech-loses-out]]
- [[influencing-notes]]
- [[shape-up]]: project delivery based on 8-week cycles: 6-week on, 2-week off. Scoping and pitching next cycle in parallel. No backlogs.
- [[shields-down]]
- [[secrets-to-optimal-client-service]] vs my [[conversation-with-Cole]]
- [[bullshit-game]]: how language no longer means anything
- [Asking smart questions](http://www.catb.org/~esr/faqs/smart-questions.html)

### Self-help

- [[thinking-fast-and-slow]]: fast/automatic thinking (system 1) vs slow/logical thinking (system 2). Bengio loves this.
- [[atomic-habits]]: how a tiny shift of 1% can compound over time.
- [[how-to-think-more-effectively]]: 12 ways of thinking.
- [[progressive-summarization]]
- [[taking-better-notes]]: Zettlekasten method (basically this), PARA (projects-areas-resources-archives).
- [Bullet Journal](https://www.youtube.com/watch?v=fm15cmYU0IM): `-,x,>` stuff with index, postpone, etc sections in physical notebook
- [[civilized-mans-eight-deadly-sins]]
- [[optimization-of-brain-and-life-performance]]: sleep; love and sex; deep breathing and daily exercises; water and chewing; fruits, unrefined products, no meat or dairy; power foods; *homo ludens*.
- [[health]]: health-specific topics in linked section
- [[Chiang_WhatExpectedUs_2005.pdf]]: button that lights up when pressed
- [Age of Entanglement](https://jods.mitpress.mit.edu/pub/ageofentanglement/release/1) which includes the Krebs Cycle of Creativity: --> Science -> Engineering -> Design -> Art ->

### Personal finances

- [[freelancing]]: pre-pandemic, things might be easier
- [Nomad List](https://nomadlist.com/) to see where other freelancers are and suggest
- [[a-programmers-guide-to-saving-investing-and-retiring-early]]
- [[building_ai_trading_systems]]
- [[learning_to_trade_with_RL]]
- [[predicting_the_stock_market_is_easier_than_you_think]]

## Research

- [[scientific_progress]]: academia about incremental gains and not taking risks since `success == number of papers`!

### Search tools

- [Semantic search](https://www.semanticscholar.org/)
- [Connected papers](https://www.connectedpapers.com/)
- ...also see LewlGPT notes

### Report and publication creation

- [[foam-howto]]
- [[markdown_cheatsheet]]
- [LaTeX Mathematical Symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
- [[template_report]]
- [[pandoc-latex-template]] and [[pandoc-latex-test]]
- [[templating_drawing_writing]]
- [[where-to-publish]]

## Unsorted

- [Experience web today](https://how-i-experience-web-today.com/)

[//begin]: # "Autogenerated link references for markdown compatibility"
[big_O]: big_O.md "Big O notation"
[data_types]: data_types.md "Data Types"
[oop-is-dead-long-live-data-oriented-design]: oop-is-dead-long-live-data-oriented-design.md "OOP Is Dead, Long Live Data Oriented Design"
[unlearn-oop]: unlearn-oop.md "Unlearn OOP"
[better-software-architecture-for-saas-startups]: better-software-architecture-for-saas-startups.md "Better Software Architecture For SaaS Startups"
[programming_tags]: programming_tags.md "Programming Tags"
[code_review]: code_review.md "Code Review"
[json-yaml-toml]: json-yaml-toml.md "JSON"
[git]: git.md "Git"
[vim]: vim.md "Vim"
[bash]: bash.md "Bash"
[tmux]: tmux.md "Tmux"
[parallel]: parallel.md "Parallel"
[awk]: awk.md "awk"
[sed]: sed.md "Sed"
[idiomatic-python]: idiomatic-python.md "Transforming Code into Beautiful, Idiomatic Python"
[python-properties]: python-properties.md "Python Properties"
[functional-programming-howto]: functional-programming-howto.md "Functional Programming How-To"
[architecture-patterns-with-python]: architecture-patterns-with-python.md "Practical Mlops"
[pytest]: pytest.md "PyTest"
[presentation_logging]: presentation_logging.md "Logging"
[presentation_logging.pdf]: presentation_logging.pdf "presentation_logging.pdf"
[the_naming_algorithm.jpeg]: ../attachments/the_naming_algorithm.jpeg "the_naming_algorithm.jpeg"
[jax]: jax.md "jax"
[julia]: julia.md "Julia"
[Julia-cheatsheet.pdf]: ../attachments/Julia-cheatsheet.pdf "Julia-cheatsheet.pdf"
[state-of-ml-in-julia]: state-of-ml-in-julia.md "State of Machine Learning in Julia"
[aws-cli]: aws-cli.md "AWS CLI"
[microservices]: microservices.md "Microservices"
[containerization]: containerization.md "Containerization"
[k3s]: k3s.md "k3s"
[udemy-course-docker]: udemy-course-docker.md "Udemy Course Docker"
[udemy-course-kubernetes]: udemy-course-kubernetes.md "Udemy Course Kubernetes"
[dramble]: dramble.md "Raspberry Pi Dramble"
[databases]: databases.md "Databases"
[s3bucket]: s3bucket.md "S3Bucket"
[influxdb]: influxdb.md "InfluxDB"
[farm-stack]: farm-stack.md "Farm Stack"
[swagger_client]: swagger_client.md "Swagger Client Generation"
[practical-mlops]: practical-mlops.md "Practical Mlops"
[Breck_MLTestScore_2017.pdf]: ../articles/Breck_MLTestScore_2017.pdf "Breck_MLTestScore_2017.pdf"
[visulize-pytorch-model]: visulize-pytorch-model.md "visulize-pytorch-model"
[lua]: lua.md "Lua"
[super-cheatsheet-machine-learning.pdf]: ../attachments/super-cheatsheet-machine-learning.pdf "super-cheatsheet-machine-learning.pdf"
[f1-score]: f1-score.md "Metrics"
[statistics-sensitivity-analysis]: statistics-sensitivity-analysis.md "Statistics, Sensitivity Analysis"
[principle-of-least-action]: principle-of-least-action.md "Principle Of Least Action"
[Runge_DetectingQuantifyingCausal_2019.pdf]: ../articles/Runge_DetectingQuantifyingCausal_2019.pdf "Runge_DetectingQuantifyingCausal_2019.pdf"
[differentiable_programming_from_scratch]: differentiable_programming_from_scratch.md "Differentiable Programming from Scratch"
[differentiable_programming_for_modeling_and_control_of_dynamical_systems]: differentiable_programming_for_modeling_and_control_of_dynamical_systems.md "Differentiable Programming for Modeling and Control of Dynamical Systems"
[linear-mpc-state-space]: linear-mpc-state-space.md "State-Space Model + Convex MPC"
[the-use-and-practice-of-scientific-machine-learning]: the-use-and-practice-of-scientific-machine-learning.md "The Use and Practice of Scientific Machine Learning (Chris Rackauckas) - nextgen_ai Freiburg 2021"
[model_based_machine_learning]: model_based_machine_learning.md "Model-Based Machine Learning"
[reinforcement-learning]: reinforcement-learning.md "Reinforcement Learning"
[a-brief-introduction-to-causal-inference]: a-brief-introduction-to-causal-inference.md "A Brief Introduction to Causal Inference"
[deepmind_deep_learning_lectures]: deepmind_deep_learning_lectures.md "DeepMind Deep Learning Lectures"
[deepmind_muzero]: deepmind_muzero.md "DeepMind MuZero"
[digital-twin]: digital-twin.md "Digital Twin"
[haystack]: haystack.md "Haystack"
[rtu-solution]: rtu-solution.md "Pathway towards solving the RTU Case"
[project_impetus]: project_impetus.md "Project Impetus"
[competitor_companies_to_bbai]: competitor_companies_to_bbai.md "Competitor Companiers to BrainBox AI"
[open-source-projects]: open-source-projects.md "Open-Source Projects"
[physical-simulations]: physical-simulations.md "Physical Simulations"
[saas-financial-models]: saas-financial-models.md "SaaS Financial Models"
[saas_metrics]: saas_metrics.md "20 Key SaaS Metrics for Startups to Track"
[saas_pricing_model]: saas_pricing_model.md "Top 6 SaaS Pricing Models and How to Choose the Right One"
[start-ups]: start-ups.md "Start-Ups"
[ai-canvas]: ai-canvas.md "Reading Week: AI Canvas"
[rework]: rework.md "Rework"
[great-at-work]: great-at-work.md "Great At Work"
[prioritization-the-other-definition]: prioritization-the-other-definition.md "How to Do Less: Prioritization, the other definition"
[bullshit-jobs]: bullshit-jobs.md "Bullshit Jobs"
[the-leader-you-want-to-be]: the-leader-you-want-to-be.md "The Leader You Want To Be"
[leadership-foundation]: leadership-foundation.md "Leadership Foundation"
[way-of-the-wolf]: way-of-the-wolf.md "Way of the Wolf"
[48-laws-of-power]: 48-laws-of-power.md "The 48 Laws of Power"
[the-art-of-seduction]: the-art-of-seduction.md "The Art of Seduction"
[bargaining-for-advantage]: bargaining-for-advantage.md "Bargaining for Advantage"
[getting-to-yes]: getting-to-yes.md "Getting to Yes"
[the-10-commandments-of-salary-negotiation]: the-10-commandments-of-salary-negotiation.md "The 10 Commandments Of Salary Negotiation"
[business-model-generation]: business-model-generation.md "Business Model Generation"
[influencing-notes]: influencing-notes.md "Influencing Notes"
[managers_playbook]: managers_playbook.md "Manager's Playbook"
[self-managed-team]: self-managed-team.md "Self-Managed Teams Survey Results"
[goals]: goals.md "I want to make goal setting useful for you and me"
[AI-team-revamp]: AI-team-revamp.md "AI Team Organization"
[100-lessons-from-1-year-of-AI-research]: 100-lessons-from-1-year-of-AI-research.md "100 Lessons from 1 Year of AI Research"
[designing-a-better-career-path-for-designers]: designing-a-better-career-path-for-designers.md "Designing a Better Career Path for Designers"
[how-to-interview-engineers]: how-to-interview-engineers.md "How To Interview Engineers"
[how-tech-loses-out]: how-tech-loses-out.md "How Tech Loses Out"
[shape-up]: shape-up.md "Shape Up - Stop Running in Circles and Ship Work that Matters"
[shields-down]: shields-down.md "Shields Down: Happy people don’t leave jobs they love"
[secrets-to-optimal-client-service]: secrets-to-optimal-client-service.md "Secrets to Optimal Client Service"
[conversation-with-Cole]: conversation-with-cole.md "Conversation with Cole Schoolland"
[bullshit-game]: bullshit-game.md "Playing the Bullshit Game: How Empty and Misleading Communication Takes Over Organizations"
[thinking-fast-and-slow]: thinking-fast-and-slow.md "Thinking, Fast and Slow"
[atomic-habits]: atomic-habits.md "The Three Layers of Behaviour Change"
[how-to-think-more-effectively]: how-to-think-more-effectively.md "How to Think More Effectively: A guide to greater productivity, insight and creativity"
[progressive-summarization]: progressive-summarization.md "Progressive Summarization"
[taking-better-notes]: taking-better-notes.md "Taking Better Notes"
[civilized-mans-eight-deadly-sins]: civilized-mans-eight-deadly-sins.md "Civilized Man's Eight Deadly Sins"
[optimization-of-brain-and-life-performance]: optimization-of-brain-and-life-performance.md "Optimization of brain and life performance: Striving for playing at the top for the long run"
[health]: health.md "Health"
[Chiang_WhatExpectedUs_2005.pdf]: ../articles/Chiang_WhatExpectedUs_2005.pdf "Chiang_WhatExpectedUs_2005.pdf"
[freelancing]: freelancing.md "Freelancing"
[a-programmers-guide-to-saving-investing-and-retiring-early]: a-programmers-guide-to-saving-investing-and-retiring-early.md "A Programmers Guide To Saving, Investing, And Retiring Early"
[building_ai_trading_systems]: building_ai_trading_systems.md "Building AI Trading Systems"
[learning_to_trade_with_RL]: learning_to_trade_with_RL.md "Learning to Trade with Reinforcement Learning"
[predicting_the_stock_market_is_easier_than_you_think]: predicting_the_stock_market_is_easier_than_you_think.md "Predicting the Stock Market is Easier than you think"
[scientific_progress]: scientific_progress.md "Scientific Progress"
[foam-howto]: foam-howto.md "Foam How-To"
[markdown_cheatsheet]: markdown_cheatsheet.md "Markdown Cheatsheet"
[template_report]: template_report.md "Report Template"
[pandoc-latex-template]: pandoc-latex-template.md "The Document Title"
[pandoc-latex-test]: pandoc-latex-test.md "Test Output Pandoc LaTeX"
[templating_drawing_writing]: templating_drawing_writing.md "Templating Drawing Writing"
[where-to-publish]: where-to-publish.md "Where to publish"
[//end]: # "Autogenerated link references"
