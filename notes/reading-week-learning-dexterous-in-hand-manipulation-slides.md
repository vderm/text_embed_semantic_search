---
author:
- Vasken Dermardiros
categories: note
date: 2020-06-04 00:00:00-04:00
draft: false
lastmod: 2020-06-29 23:19:06-04:00
tags:
- domain-randomization
- simulation
- robotics
- reinforcement-learning
- reading-week
title: Learning Dexterous In-Hand Manipulation
---

## <span class="section-num">1</span> Physics-Engine Back-End {#physics-engine-back-end}

### <span class="section-num">1.1</span> References {#references}

- <https://openai.com/blog/learning-dexterity/>
- <https://arxiv.org/abs/1808.00177>, or
- <sup id="fb9eb8051eed9773248081ca69f75090"><a href="#OpenAI_Learningdexterousinhand_2018" title="OpenAI, Andrychowicz, Baker, Chociej, J\'ozefowicz, McGrew, Pachocki, Petron, Plappert, Powell, Ray, Schneider, Sidor, Tobin, Welinder, Weng \&amp; Zaremba, Learning Dexterous In-Hand Manipulation, {CoRR}, v(), (2018).">OpenAI_Learningdexterousinhand_2018</a></sup>

### <span class="section-num">1.2</span> Paper Chosen {#paper-chosen}

![[2020-06-03_22-43-34_screenshot.png]]

OpenAI, Andrychowicz, M., Baker, B., Chociej, M., Jozefowicz, R., McGrew, B.,
Pachocki, J., …, **Learning Dexterous In-Hand Manipulation**, arXiv:[1808.00177](https://arxiv.org/abs/1808.00177) [cs,
stat], (), (2019). -> [Blog post with videos](https://openai.com/blog/learning-dexterity/)

### <span class="section-num">1.3</span> Learning Dexterous In-Hand Manipulation {#learning-dexterous-in-hand-manipulation}

Paper by <sup id="fb9eb8051eed9773248081ca69f75090"><a href="#OpenAI_Learningdexterousinhand_2018" title="OpenAI, Andrychowicz, Baker, Chociej, J\'ozefowicz, McGrew, Pachocki, Petron, Plappert, Powell, Ray, Schneider, Sidor, Tobin, Welinder, Weng \&amp; Zaremba, Learning Dexterous In-Hand Manipulation, {CoRR}, v(), (2018).">OpenAI_Learningdexterousinhand_2018</a></sup> which got me thinking about leveraging
simulation engines to train RL-based controllers.

**What is it about?** Training an RL agent to manipulate a block through cameras
held by a very complex robotic hand (24 DoF) to match a desired pose.

**Why should we care?** RL agent is trained in a noised physics-based environment
and does very well in the real world. Many years of equivalent experience can be
gathered through simulation; plus you don't break things IRL.

**What did I like?** The physics simulation can't simulate everything in the real
robot &#x2013; there's a "reality gap" &#x2013;, so they've noised various parts to try to
cover various scenarios (I'm imagining this approach building a sort of convex
hull containing the real world within and so the agent would interpolate between
experiences). Field: _domain randomization_.

**What did I dislike?** How much computational resources that had to be used.
Arguably, we could skip the ablation studies, or do those once.

### <span class="section-num">1.4</span> Training {#training}

![Figure 1: Training process](../attachments/2023-08-04-11-10-33.png)

### <span class="section-num">1.5</span> Inference {#inference}

![Figure 2: Inference process](../attachments/2023-08-04-11-11-21.png)

### <span class="section-num">1.6</span> Setup {#setup}

![Figure 3: Real-world vs simulation environments](../attachments/2023-08-04-11-12-09.png)

### <span class="section-num">1.7</span> Why does it work? {#why-does-it-work}

Obtained policies perform well in the real world because of:

1. extensive randomizations and added effects in the simulated environment
    alongside calibrations,
2. memory augmented control policies which admit the possibility to learn
    adaptive behaviour and implicit system identification on the fly, and
3. training at large scale with distributed reinforcement learning

### <span class="section-num">1.8</span> Approach: PPO {#approach-ppo}

- Many randomizations persists beyond episodes so agent should be able to
    identify properties of the current environment
- PPO = two networks: policy + value; both same architecture
- Value network used only in training, Asymmetric Actor-Critic approach is used
    which exploits the fact that the value network can have access to information
    that is not available on the real robot system.
- Discrete actions yielded better results
- Memory &#x2013; in the form of LSTM over feed-forward NN &#x2013; helps achieve good
    performance in the randomized simulation.

### <span class="section-num">1.9</span> Ablation of randomizations {#ablation-of-randomizations}

Adding randomizations make learning slower, however, to transfer the policy to a
real robot, these randomizations are critical! -> full rando = best results

![Figure 4: Effect of randomizations on convergence](../attachments/2023-08-04-11-12-36.png)

### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.10</span> References to follow-up on {#references-to-follow-up-on}

- [10] P. F. Christiano, Z. Shah, I. Mordatch, J. Schneider, T. Blackwell, J.
    Tobin, P. Abbeel, and W. Zaremba. Transfer from simulation to real world
    through learning deep inverse dynamics model.CoRR,abs/1610.03518, 2016.
- [47] L. Pinto, J. Davidson, and A. Gupta. Supervision via competition: Robot
    adversaries for learning tasks. In 2017 IEEE International Conference on
    Robotics and Automation, ICRA 2017, Singapore, Singapore, May 29 - June 3,
    2017, pages 1601–1608, 2017.
- [48] L. Pinto, J. Davidson, R. Sukthankar, and A. Gupta. Robust adversarial
    reinforcement learning. In Proceedings of the 34th International Conference on
    Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017, pages
    2817–2826, 2017

## <span class="section-num">2</span> References {#references}

### <span class="section-num">2.1</span> References {#references}

# Bibliography

<a id="OpenAI_Learningdexterousinhand_2018"></a>[OpenAI_Learningdexterousinhand_2018] OpenAI, Andrychowicz, Baker, Chociej, J\'ozefowicz, McGrew, Pachocki, Petron, Plappert, Powell, Ray, Schneider, Sidor, Tobin, Welinder, Weng & Zaremba, Learning Dexterous In-Hand Manipulation, <i>CoRR</i>,  (2018). [↩](#fb9eb8051eed9773248081ca69f75090)

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-06-03_22-43-34_screenshot.png]: ../attachments/Physics-Engine_Back-End/2020-06-03_22-43-34_screenshot.png "2020-06-03_22-43-34_screenshot.png"
[//end]: # "Autogenerated link references"