---
author:
- Kyle Wiggers
categories: article
draft: false
lastmod: 2020-12-26 16:21:49-05:00
slug: deepmind_muzero
tags:
- deepmind
- research
- reinforcement-learning
title: DeepMind MuZero
---


## DeepMind’s MuZero picks up the rules of games as it plays {#deepmind-s-muzero-picks-up-the-rules-of-games-as-it-plays}

- <https://venturebeat.com/2020/12/23/deepminds-muzero-picks-up-the-rules-of-games-as-it-plays/amp/>

RL system that learns the rules as it goes. Different than AlphaGo and AlphaZero
who knew the rules.

Dave Silver, who leads the reinforcement learning group at DeepMind, says MuZero
paves the way for learning methods in a host of real-world domains, particularly
those lacking a simulator or dynamics rules. “We think this really matters for
enriching what AI can actually do because the world is a messy place. It’s
unknown — no one gives us this amazing rulebook that says, ‘Oh, this is exactly
how the world works,'” he told VentureBeat in a phone interview last week. “If
we want our AI to go out there into the world and be able to plan and look ahead
in problems where no one gives us the rulebook, we really, really need this.”

Enter MuZero, which combines a model with AlphaZero’s lookahead tree search.
Instead of trying to model an entire environment using an algorithm, MuZero
models only aspects it determines are important to the decision-making process.

![[2020-12-23_22-49-37_Figure1-Timeline-AlphaGo-to-MuZero.png.png]]

Intuitively, MuZero internally invents game rules or dynamics that lead to
accurate planning.

![[2020-12-23_22-51-35_Figure6.png.png]]

For MuZero, DeepMind instead pursued an approach focusing on end-to-end
prediction of a value function, where an algorithm is trained so the expected
sum of rewards matches the expected value with respect to real-world actions.
The system has no semantics of the environment state but simply outputs policy,
value, and reward predictions, which an algorithm similar to AlphaZero’s search
(albeit generalized to allow for single-agent domains and intermediate rewards)
uses to produce a recommended policy and estimated value. These in turn are used
to inform an action and the final outcomes in played games.

MuZero beat AlphaZero in Go and beats the previous state-of-the-art approach
(R2D2) in Atari games.

## MuZero: Mastering Go, chess, shogi and Atari without rules {#muzero-mastering-go-chess-shogi-and-atari-without-rules}

- [DeepMind Blog Post](https://deepmind.com/blog/article/muzero-mastering-go-chess-shogi-and-atari-without-rules)
- [ICAPS 2020 Presentation](https://www.youtube.com/watch?v=L0A86LmH7Yw)

### Blog post {#blog-post}

Specifically, MuZero models three elements of the environment that are critical
to planning:

- The value: how good is the current position?
- The policy: which action is the best to take?
- The reward: how good was the last action?

![[2020-12-23_22-58-46_screenshot.png]]
caption="Figure 1: ILLUSTRATION OF HOW MONTE CARLO TREE SEARCH CAN BE USED TO PLAN WITH THE MUZERO NEURAL NETWORKS. STARTING AT THE CURRENT POSITION IN THE GAME (SCHEMATIC GO BOARD AT THE TOP OF THE ANIMATION), MUZERO USES THE REPRESENTATION FUNCTION (H) TO MAP FROM THE OBSERVATION TO AN EMBEDDING USED BY THE NEURAL NETWORK (S0). USING THE DYNAMICS FUNCTION (G) AND THE PREDICTION FUNCTION (F), MUZERO CAN THEN CONSIDER POSSIBLE FUTURE SEQUENCES OF ACTIONS (A), AND CHOOSE THE BEST ACTION.

![[2020-12-23_22-59-17_screenshot.png]]
caption="Figure 2: MUZERO USES THE EXPERIENCE IT COLLECTS WHEN INTERACTING WITH THE ENVIRONMENT TO TRAIN ITS NEURAL NETWORK. THIS EXPERIENCE INCLUDES BOTH OBSERVATIONS AND REWARDS FROM THE ENVIRONMENT, AS WELL AS THE RESULTS OF SEARCHES PERFORMED WHEN DECIDING ON THE BEST ACTION.

![[2020-12-23_22-59-36_screenshot.png]]
caption="Figure 3: DURING TRAINING, THE MODEL IS UNROLLED ALONGSIDE THE COLLECTED EXPERIENCE, AT EACH STEP PREDICTING THE PREVIOUSLY SAVED INFORMATION: THE VALUE FUNCTION V PREDICTS THE SUM OF OBSERVED REWARDS (U), THE POLICY ESTIMATE (P) PREDICTS THE PREVIOUS SEARCH OUTCOME (Π), THE REWARD ESTIMATE R PREDICTS THE LAST OBSERVED REWARD (U).

### ICAPS 2020 Video {#icaps-2020-video}

Starts with talking about MCTS where you want to explore the tree but still be
able to exploit to max rewards.

Links the benefits of pre-search, with MCTS and a learned model.

<!--list-separator-->

- Go

    Value network
    : how well am I doing?
        - Reduce depth with value network, search a bit and then check the nodes

    Prior network
    : what are the most likely actions?
        - What would we intuitively do?

    Both together: reduce breath and width of the tree

    ![[2020-12-26_11-00-36_screenshot.png]]

<!--list-separator-->

- Monte Carlo Tree Search

  - **Evaluate** many **interesting** positions/actions.
  - **Aggregate** the information for better action selection.
  - We want to explore promising locations (high prior and/or high value) OR
        locations that are very little known
    - Classical exploration/exploitation problem

    The selection method used called PUCB does this trade-off:

    ![[2020-12-23_23-10-18_screenshot.png]]

    AlphaZero played chess more "human-like" vs other programs -> points per pieces
    are not programmed -> other programs are more about exploiting points.

<!--list-separator-->

- Planning with a Learned Model

    ![[2020-12-26_15-50-45_screenshot.png]]

    Planning can be viewed as an improvement operator.

    ![[2020-12-26_15-51-52_screenshot.png]]

    Dirichlet noise applied at root node for exploration inside the search; it has
    nice properties to not disturbed the prior too much.

    Action selected based on the visit counts at the root of the search tree.

    To assure games are not determinimistic.

    \\[ a ~ \pi^T \\]

    Temperature \\(T\\) controls exploration: uniform when \\(T=0\\), arg-max when
    \\(T=\infty\\).

    ![[2020-12-26_15-56-14_screenshot.png]]

    With this, we have everything we need to train an agent.

    Can be combined with MCTS.

    h
    : is the embedding of observations,

    g
    : represents the dynamics of the system,

    a
    : actions,

    r
    : rewards,

    f
    : to make predictions of values

<!--list-separator-->

- Update the learned model towards the MCTS

    ![[2020-12-26_15-59-51_screenshot.png]]

<!--list-separator-->

- MuZero at a Glance

    ![[2020-12-26_16-00-32_screenshot.png]]

<!--list-separator-->

- Results

    MuZero performs as well as AlphaZero; training time is also greatly reduced.

    Still uses quite a bit of data to train.

    Can we reuse old trajectories to reduce the training data required?

    They do this by replaying older episodes and by splitting the training into
    actors and learners.

    ![[2020-12-26_16-08-40_screenshot.png]]

    ![[2020-12-26_16-13-13_screenshot.png]]

<!--list-separator-->

- Some take-aways for reproducing work

    1. Visualization is the best way to find bugs!

    ![[2020-12-26_16-17-24_screenshot.png]]

    2.Profile everything too

    ![[2020-12-26_16-18-03_screenshot.png]]

    1. Supervised learning dataset
    2. Unit tests, integration tests
    3. Standard infrastructure: reuse what's out there, he's a fan of JAX; OpenSpiel
    4. Reliable evaluations: go against known good agents; don't come up with your
        own metrics unless really needed

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-12-23_22-49-37_Figure1-Timeline-AlphaGo-to-MuZero.png.png]: ../attachments/DeepMinds_MuZero_picks_up_the_rules_of_games_as_it_plays/2020-12-23_22-49-37_Figure1-Timeline-AlphaGo-to-MuZero.png.png "2020-12-23_22-49-37_Figure1-Timeline-AlphaGo-to-MuZero.png.png"
[[2020-12-23_22-51-35_Figure6.png.png]: ../attachments/DeepMinds_MuZero_picks_up_the_rules_of_games_as_it_plays/2020-12-23_22-51-35_Figure6.png.png "2020-12-23_22-51-35_Figure6.png.png"
[[2020-12-23_22-58-46_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-23_22-58-46_screenshot.png "2020-12-23_22-58-46_screenshot.png"
[[2020-12-23_22-59-17_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-23_22-59-17_screenshot.png "2020-12-23_22-59-17_screenshot.png"
[[2020-12-23_22-59-36_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-23_22-59-36_screenshot.png "2020-12-23_22-59-36_screenshot.png"
[[2020-12-26_11-00-36_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_11-00-36_screenshot.png "2020-12-26_11-00-36_screenshot.png"
[[2020-12-23_23-10-18_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-23_23-10-18_screenshot.png "2020-12-23_23-10-18_screenshot.png"
[[2020-12-26_15-50-45_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_15-50-45_screenshot.png "2020-12-26_15-50-45_screenshot.png"
[[2020-12-26_15-51-52_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_15-51-52_screenshot.png "2020-12-26_15-51-52_screenshot.png"
[[2020-12-26_15-56-14_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_15-56-14_screenshot.png "2020-12-26_15-56-14_screenshot.png"
[[2020-12-26_15-59-51_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_15-59-51_screenshot.png "2020-12-26_15-59-51_screenshot.png"
[[2020-12-26_16-00-32_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_16-00-32_screenshot.png "2020-12-26_16-00-32_screenshot.png"
[[2020-12-26_16-08-40_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_16-08-40_screenshot.png "2020-12-26_16-08-40_screenshot.png"
[[2020-12-26_16-13-13_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_16-13-13_screenshot.png "2020-12-26_16-13-13_screenshot.png"
[[2020-12-26_16-17-24_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_16-17-24_screenshot.png "2020-12-26_16-17-24_screenshot.png"
[[2020-12-26_16-18-03_screenshot.png]: ../attachments/MuZero__Mastering_Go,_chess,_shogi_and_Atari_without_rules/2020-12-26_16-18-03_screenshot.png "2020-12-26_16-18-03_screenshot.png"
[//end]: # "Autogenerated link references"