---
author:
- Denny Britz
categories: note
draft: false
lastmod: 2021-01-03 22:49:05-05:00
tags:
- management
- finance
- freelancing
- reinforcement-learning
- business
title: Learning to Trade with Reinforcement Learning
links:
- http://www.wildml.com/2018/02/introduction-to-learning-to-trade-with-reinforcement-learning/
---


Website: [Intro to Learning to Trade with RL](http://www.wildml.com/2018/02/introduction-to-learning-to-trade-with-reinforcement-learning/)

There's a strong case for using RL in stock trading since the agent can learn
market movements while optimizing their policies. Policies can be written
explicitly to track what you want as a trader vs conventional approaches to try
to model the market behaviour then hand-tune rules and backtest and optimzed
etc. The RL approach is much quicker to iterate and can be brought live much
sooner.

## Basics of Market Microstructure {#basics-of-market-microstructure}

Bid-ask spread, liquidity, etc.

## Data {#data}

Need a good source of data. This is why he's relying on cryptos! Many platforms
offer phantom trades just to make their platform look more liquid.

## Trading Metrics {#trading-metrics}

### Net PnL (Net Profit and Loss) {#net-pnl--net-profit-and-loss}

Simply how much money an algorithm makes (positive) or loses (negative) over
some period of time, minus the trading fees.

### Alpha and Beta {#alpha-and-beta}

[Alpha](https://en.wikipedia.org/wiki/Alpha%5F(finance)) defines how much better, in terms of profit, your strategy is when
compared to an alternative, relatively risk-free, investment, like a government
bond. Even if your strategy is profitable, you could be better off investing in
a risk-free alternative. [Beta](https://en.wikipedia.org/wiki/Beta%5F(finance)) is closely related, and tells you how volatile
your strategy is compared to the market. For example, a beta of 0.5 means that
your investment moves $1 when the market moves $2.

### Sharpe Ratio {#sharpe-ratio}

The [Sharpe Ratio](https://en.wikipedia.org/wiki/Sharpe%5Fratio#Use%5Fin%5Ffinance) measures the excess return per unit of risk you are taking.
It’s basically your return on capital over the standard deviation, adjusted for
risk. Thus, the higher the better. It takes into account both the volatility of
your strategy, as well as an alternative risk-free investment.

### Maximum Drawdown {#maximum-drawdown}

The [Maximum Drawdown](https://en.wikipedia.org/wiki/Drawdown%5F(economics)) is the maximum difference between a local maximum and the
subsequent local minimum, another measure of risk. For example, a maximum
drawdown of 50% means that you lose 50% of your capital at some point. You then
need to make a 100% return to get back to your original amount of capital.
Clearly, a lower maximum drawdown is better.

### Value at Risk (VaR) {#value-at-risk--var}

[Value at Risk](https://en.wikipedia.org/wiki/Value%5Fat%5Frisk) is a risk metric that quantifies how much capital you may lose
over a given time frame with some probability, assuming normal market
conditions. For example, a 1-day 5% VaR of 10% means that there is a 5% chance
that you may lose more than 10% of an investment within a day.

![[2020-06-27_17-00-09_screenshot.png]]

## Typical Strategy Development Workflow with a Supervised Learning Approach {#typical-strategy-development-workflow-with-a-supervised-learning-approach}

1. Data Analysis
2. Supervised Model Training
3. Policy Development (by hand)
4. Strategy Backtesting
5. Parameters Optimization (simulation)
6. Simulation & Paper Trading
7. Live Trading

Not very effective because:

1. Iteration cycles are slow. Step 1-3 are based on intuition and you don't know
    if approach works until steps 4-5 -> doesn't work, start from scratch!
2. Simulation comes too late. Not take into account environmental factors such
    as latencies, fees and liquidity until step 4. Shouldn't these things
    directly inform you strategy development or the parameters of you model?
3. Policies are developed independently from supervised models even though they
    interact closely. Supervised predictions are an input to the policy. Why not
    jointly optimize them?
4. Policies are simple. Limited to what humans can come up with.
5. Parameter optimization is inefficient.

## Deep RL for Trading {#deep-rl-for-trading}

### Agent {#agent}

Buys and sell assets.

### Environment {#environment}

- Simply: Trading platform + all the other agents trading
- Potentially: We can try to reverse engineer their trading strategies and
    exploit them; Multi-agent RL (MARL) problem setting

### State {#state}

- Partially Observable Markov Decision Process (POMDP)
- Can't see everything nor what the other agents are doing

### Time Scale {#time-scale}

Days? Hours? Minutes? Variable scales?

All require a different approach: buy-and-hold, vs high frequency trading with
algorithms running on FPGAs.

RL can act in between: faster than a human, but long enough to make a decision.

### Action Space {#action-space}

Discrete vs continuous actions spaces by complexity:

- Buy, Hold and Sell -> fixed amount
- How much money to use? -> discrete action buy/hold/sell, continuous quantity
- Place limit orders: at what price to strike; which orders to cancel

### Reward Function {#reward-function}

- Absolute feedback: realized PnL (profit and loss)
- More frequent feedback: unrealized PnL
- Both naively optimize for profit; better to minimize risk
  - Use Sharpe Ratio
  - Maximum Drawdown

## The Case for Reinforcement Learning {#the-case-for-reinforcement-learning}

End-to-End optimization of what we care about

![[2020-06-27_17-13-02_screenshot.png]]

- Fix the reward to what you want instead of hard-coding/testing a surrogate to
    get back to your desires
- Learned policies not hand-programmed
- Train directly in Simulation Environments
  - Include everything that happens in _the real world_
  - Agents learns to deal with them
  - /That’s a very powerful concept. By building an increasingly complex
        simulation environment that models the real world you can train very
        sophisticated agents that learn to take environment constraints into
        account./

Trading agents have characteristics very similar to those for multiplayer games.
But you can easily test them live! You can deploy your agent on an exchange
through their API and immediately get real-world market feedback.
**Iteration cycle can be extremely fast.**

_Last part talks about continuous time, nonstationary, lifelong learning,
catastrophic forgetting and transfer learning, but only on the surface._

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-06-27_17-00-09_screenshot.png]: ../attachments/Trading_Metrics/2020-06-27_17-00-09_screenshot.png "2020-06-27_17-00-09_screenshot.png"
[[2020-06-27_17-13-02_screenshot.png]: ../attachments/The_Case_for_Reinforcement_Learning/2020-06-27_17-13-02_screenshot.png "2020-06-27_17-13-02_screenshot.png"
[//end]: # "Autogenerated link references"