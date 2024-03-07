---
author:
- Vasken Dermardiros
categories: article
draft: false
lastmod: 2020-09-08 14:34:03-04:00
slug: acme_rl_building_blocks
tags:
- reinforcement-learning
- research
title: ACME RL Building Blocks
links:
- https://github.com/deepmind/acme
- https://arxiv.org/pdf/2006.00979.pdf
---

<https://github.com/deepmind/acme>

<https://arxiv.org/pdf/2006.00979.pdf>

Acme is a library of reinforcement learning (RL) agents and agent building
blocks. Acme strives to expose simple, efficient, and readable agents, that
serve both as reference implementations of popular algorithms and as strong
baselines, while still providing enough flexibility to do novel research. The
design of Acme also attempts to provide multiple points of entry to the RL
problem at differing levels of complexity.

Overall, the high-level goals of Acme are as follows:

1.  To enable the reproducibility of our methods and results — this will help
    clarify what makes an RL problem hard or easy, something that is seldom
    apparent.
2.  To simplify the way we (and the community at large) design new algorithms —
    we want that next RL agent to be easier for everyone to write!
3.  To enhance the readability of RL agents — there should be no hidden surprises
    when transitioning from a paper to code.