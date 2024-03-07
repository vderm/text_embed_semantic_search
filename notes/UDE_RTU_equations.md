---
author: Scott McDonald, Vasken Dermardiros
categories: note
tags:
- mpc
- algo
- julia
- model
- physics-based
- research
title: UDE RTU Equations and Approach
---

# Training
Dynamics model:

$$
\begin{align}
    \frac{\delta T_i}{\delta t} &= \frac{1}{C_i} \left[ \textrm{EXT} + \textrm{NEIGH} + \textrm{HVAC} \right] ~(+~\epsilon) \\
    U &= 1/R \\
    \textrm{EXT}_1 &= U_{ext} [T_{ext} - T_i] \\
    \textrm{EXT}_2 &= U_{ext} [(AT_{ext} + b) - T_i] \\
    \textrm{NEIGH}_1 &= \sum^j_{i \neq j} U_{i,j} [T_j - T_i] \\
    \textrm{HVAC}_1 &= \textrm{NN}_i(\textrm{SP}_i, ...) \\
    \textrm{HVAC}_2 &= \sum^n \mu_n \textrm{HVAC}_n ~|~ n \in \textrm{(heat, cool)}
\end{align}
$$

HVAC model is in $kW$ once trained. Also, $\epsilon$ should looks a lot like normal noise.

To train the differential model, you would have to minimize MSE or MAE or a weighted MSE (weighted relative to a time or zone).

If the order of magnitude need to be close, try to have:
+ $C$ in $kWh/K$
+ $1/R = U$ in $kW/K$
+ $\dot{Q}$ in $kW$
+ $\delta t$ in $h$

# Controls
$$
\begin{align}
    \min_{SP} & ~~\sum_{i=t}^{ph} ( \textrm{cost}_{\textrm{energy},~i} * \textrm{Power}_i * \Delta t ) +  \textrm{cost}_{\textrm{power},~i} || \textrm{Power}_i ||_\infin\\
    \textrm{s.t.} ~~\frac{\delta T_i}{\delta t} &= \frac{1}{C_i} \left[ \textrm{EXT} + \textrm{NEIGH} + \textrm{HVAC} \right] ~(+~\epsilon) \\
    & \underbar{SP} \leq SP \leq \bar{SP} \\
    & \underbar{ROC} \leq \frac{\delta T_i}{\delta t} \leq \bar{ROC}
\end{align}
$$

This way, we don't care about HVAC states of cycling, etc.

Need a surrogate for power: $\textrm{Power} = \iota\textrm{NN}(\textrm{SP}) ~(+ \beta)$ and $\iota$ can be some monotonic function which represents the efficacy of the HVAC system to provide or remove heat from a room given electricity or fuel being consumed by the HVAC equipment.

# Algorithm
1. Build a config -> RTU agent
2. For modeling -> load Nzones, NHVAC from RTU agent
   1. Train for decay terms
   2. Freeze decay terms
   3. Train NN component using mini-batch
   4. Save NN model parameters "p"
3. For controls
   1. Load model
   2. Generate control sequences
   3. Per proposed control
      1. Run ODE solver to get space temperature
      2. Check cost and discomfort
   4. Stop when satisfied -> out of iterations, solution stagnation



Copied this from Fatma's paper, we can adopt it to our needs:
$$
\begin{algorithm}
\DontPrintSemicolon

  \KwIn{dataframe, $P_{budget_{i}}^{t+k|t}(\hat{u_{i}})$}
  \KwOut{optimal agent control}
  Load CAM-LSTM prediction models for each agent \;

  \For{generation}
    {
        Predict temperature \;
        Compute fitness using model defined in (\ref{op:1}) \;%\tcp*{execute agent model}
        Select individual by tournament \;
        Crossover \;
        Mutation \;
        Get $argmin$ of scores\;
    }
    Get optimal control $\hat{u}$ \;
    Save outputs in $csv$ file \;
    Create new population \;
    Add best chromosomes to new population \;
\caption{Local Agent Algorithm}
\label{algo:agent}
\end{algorithm}
$$