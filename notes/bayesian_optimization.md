---
author:
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-07-29 11:24:00-04:00
slug: bayesian_optimization
tags:
- research
- bayesian
title: Bayesian Optimization
links:
- https://distill.pub/2020/bayesian-optimization/
---

<https://distill.pub/2020/bayesian-optimization/>

Assume objective is to find the location of most amount of gold:

![[2020-07-29_10-57-14_screenshot.png]]

Two ways of approaching it:

- Problem 1: Best Estimate of Gold Distribution (Active Learning)
    In this problem, we want to accurately estimate the gold distribution on the
    new land. We can not drill at every location due to the prohibitive cost.
    Instead, we should drill at locations providing **high information** about the
    gold distribution. This problem is akin to Active Learning.

- Problem 2: Location of Maximum Gold (Bayesian Optimization)
    In this problem, we want to find the location of the maximum gold content. We,
    again, can not drill at every location. Instead, we should drill at locations
    showing **high promise** about the gold content. This problem is akin to Bayesian
    Optimization.

## Active Learning {#active-learning}

Active learning minimizes labeling costs while maximizing modeling accuracy.
While there are various methods in active learning literature, we look at
uncertainty reduction. This method proposes labeling the point whose model
uncertainty is the highest. Often, the variance acts as a measure of
uncertainty.

This gives us the following procedure for Active Learning:

- Choose and add the point with the highest uncertainty to the training set (by
    querying/labeling that point)
- Train on the new training set
- Go to #1 till convergence or budget elapsed

![[2020-07-29_11-01-26_screenshot.png]]

Model fits the uncertainty and not what the underlying function would look like.

## Bayesian Optimization {#bayesian-optimization}

In the previous section, we picked points in order to determine an accurate
model of the gold content. But what if our goal is simply to find the location
of maximum gold content? Of course, we could do active learning to estimate the
true function accurately and then find its maximum. But that seems pretty
wasteful — why should we use evaluations improving our estimates of regions
where the function expects low gold content when we only care about the maximum?

To solve this problem, we will follow the following algorithm:

- We first choose a surrogate model for modeling the true function \\(f\\) and
    define its prior.
- Given the set of observations (function evaluations), use Bayes rule to obtain
    the posterior.
- Use an acquisition function \\(\alpha(x)\\), which is a function of the posterior,
    to decide the next sample point \\(x\_t = \text{argmax}\_x\\).
- Add newly sampled data to the set of observations and goto step #2 till
    convergence or budget elapses.

## Acquisition Functions {#acquisition-functions}

### Probability of Improvement (PI) {#probability-of-improvement--pi}

This acquisition function chooses the next query point as the one which has the
highest probability of improvement over the current max \\(f(x^+)\\).

![[2020-07-29_11-06-11_screenshot.png]]

\\(\epsilon\\) is a factor to tradeoff exploration-exploitation (higher &epsilon;
means higher exploration). Too high and we will sample everything. Too low, we
will get stuck in a local minimum rather quickly.

### Expected Improvement (EI) {#expected-improvement--ei}

Probability of improvement only looked at how likely is an improvement, but, did
not consider how much we can improve. The next criterion, called Expected
Improvement (EI), does exactly that!

The idea is fairly simple — choose the next query point as the one which has the
highest expected improvement over the current max \\(f(x^+)\\), where \\(x^+ =
\text{argmax}\_{x\_i \in x\_{1:t}}f(x\_i)\\) and \\(x\_i\\)​ is the location queried at
\\(i^{th}\\) time step.

[Seems much better than PI in finding the optima quickly.]

### Thompson Sampling {#thompson-sampling}

Another common acquisition function is Thompson Sampling. At every step, we
sample a function from the surrogate’s posterior and optimize it. For example,
in the case of gold mining, we would sample a plausible distribution of the gold
given the evidence and evaluate (drill) wherever it peaks.

![[2020-07-29_11-13-41_screenshot.png]]

We can understand the intuition behind Thompson sampling by two observations:

- Locations with high uncertainty (σ(x) &sigma;(x) σ(x)) will show a large
    variance in the functional values sampled from the surrogate posterior. Thus,
    there is a non-trivial probability that a sample can take high value in a
    highly uncertain region. Optimizing such samples can aid exploration.

    As an example, the three samples (sample #1, #2, #3) show a high variance
    close to x=6x=6x=6. Optimizing sample 3 will aid in exploration by evaluating
    x=6x=6x=6.

- The sampled functions must pass through the current max value, as there is no
    uncertainty at the evaluated locations. Thus, optimizing samples from the
    surrogate posterior will ensure exploiting behavior.

    As an example of this behavior, we see that all the sampled functions above
    pass through the current max at x=0.5x = 0.5x=0.5. If x=0.5x = 0.5x=0.5 were
    close to the global maxima, then we would be able to exploit and choose a
    better maximum.

### Random {#random}

Lol!

### Upper Confidence Bound (UCB) {#upper-confidence-bound--ucb}

One such trivial acquisition function that combines the exploration/exploitation
tradeoff is a linear combination of the mean and uncertainty of our surrogate
model. The model mean signifies exploitation (of our model’s knowledge) and
model uncertainty signifies exploration (due to our model’s lack of
observations). \\(\alpha(x) = \mu(x) + \lambda \times \sigma(x)\\)

The intuition behind the UCB acquisition function is weighing of the importance
between the surrogate’s mean vs. the surrogate’s uncertainty. The \\(\lambda\\)
above is the hyperparameter that can control the preference between exploitation
or exploration.

We can further form acquisition functions by combining the existing acquisition
functions though the physical interpretability of such combinations might not be
so straightforward. One reason we might want to combine two methods is to
overcome the limitations of the individual methods.

### Probability of Improvement + \\(\lambda \ \times\\) Expected Improvement (EI-PI) {#probability-of-improvement-plus--lambda-times--expected-improvement--ei-pi}

One such combination can be a linear combination of PI and EI. We know PI
focuses on the probability of improvement, whereas EI focuses on the expected
improvement. Such a combination could help in having a tradeoff between the two
based on the value of \\(\lambda\\).

### Gaussian Process Upper Confidence Bound (GP-UCB) {#gaussian-process-upper-confidence-bound--gp-ucb}

Before talking about GP-UCB, let us quickly talk about **regret**. Imagine if the
maximum gold was \\(a\\) units, and our optimization instead samples a location
containing \\(b < a\\) units, then our regret is \\(a - b\\). If we accumulate
the regret over nnn iterations, we get what is called cumulative regret.

GP-UCB’s formulation is given by:

&alpha;<sub>GP-UCB</sub>(x) = &mu;\_t(x) + \sqrt{\beta\_t}&sigma;\_t(x)$

Where \\(t\\) is the timestep.

Srinivas et. al. developed a schedule for β\betaβ that they theoretically
demonstrate to minimize cumulative regret.

### Comparison {#comparison}

![[2020-07-29_11-19-50_screenshot.png]]

## Hyperparameter Tuning {#hyperparameter-tuning}

Example on using Bayesian optimization for hyperparameter tuning...

![[2020-07-29_11-21-29_screenshot.png]]

Overall, PI and GP-UCB tend to be the better approaches.

[[2020-07-29_10-57-14_screenshot.png]: ../attachments/2020-07-29_10-57-14_screenshot.png "2020-07-29_10-57-14_screenshot.png"
[[2020-07-29_11-01-26_screenshot.png]: ../attachments/Active_Learning/2020-07-29_11-01-26_screenshot.png "2020-07-29_11-01-26_screenshot.png"
[[2020-07-29_11-06-11_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-06-11_screenshot.png "2020-07-29_11-06-11_screenshot.png"
[[2020-07-29_11-13-41_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-13-41_screenshot.png "2020-07-29_11-13-41_screenshot.png"
[[2020-07-29_11-19-50_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-19-50_screenshot.png "2020-07-29_11-19-50_screenshot.png"
[[2020-07-29_11-21-29_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-21-29_screenshot.png "2020-07-29_11-21-29_screenshot.png"
[//end]: # "Autogenerated link references"

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-07-29_10-57-14_screenshot.png]: ../attachments/2020-07-29_10-57-14_screenshot.png "2020-07-29_10-57-14_screenshot.png"
[[2020-07-29_11-01-26_screenshot.png]: ../attachments/Active_Learning/2020-07-29_11-01-26_screenshot.png "2020-07-29_11-01-26_screenshot.png"
[[2020-07-29_11-06-11_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-06-11_screenshot.png "2020-07-29_11-06-11_screenshot.png"
[[2020-07-29_11-13-41_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-13-41_screenshot.png "2020-07-29_11-13-41_screenshot.png"
[[2020-07-29_11-19-50_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-19-50_screenshot.png "2020-07-29_11-19-50_screenshot.png"
[[2020-07-29_11-21-29_screenshot.png]: ../attachments/Bayesian_Optimization/2020-07-29_11-21-29_screenshot.png "2020-07-29_11-21-29_screenshot.png"
[//end]: # "Autogenerated link references"