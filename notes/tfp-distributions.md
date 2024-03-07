---
author:
- Vasken Dermardiros
categories: website
draft: false
lastmod: 2020-07-17 08:46:35-04:00
tags:
- tensorflow
- state-space
- model
- linear
- reference
- research
title: TFP_Distributions
links:
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/StructuralTimeSeries
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/LinearRegression
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/distributions/LinearGaussianStateSpaceModel
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/AdditiveStateSpaceModel
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/AutoregressiveStateSpaceModel
- https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/forecast
---

State-Space modeling in Tensorflow using Distributions. Auto-regressive and
state space models in Tensorflow. Doing more of a gray-box modeling approach.

## StructuralTimeSeries {#structuraltimeseries}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/StructuralTimeSeries>

Base class for structural time series models.

```python
tfp.sts.StructuralTimeSeries(
    parameters, latent_size, name='StructuralTimeSeries'
)
```

A StructuralTimeSeries object represents a declarative specification of a
structural time series model, including priors on model parameters. It
implements a joint probability model p(params, y) = p(params) p(y | params),
where params denotes a list of real-valued parameters specified by the child
class, and p(y | params) is a linear Gaussian state space model with structure
determined by the child class.

Args:

parameters
: list of Parameter namedtuples, each specifying the name and
    prior distribution of a model parameter along with a bijective transformation
    from an unconstrained space to the support of that parameter. The order of
    this list determines the canonical parameter ordering used by fitting and
    inference algorithms.

latent\_size
: Python int specifying the dimensionality of the latent state
    space for this model.

name
: Python str name for this model component.

Attributes:

batch\_shape
: Static batch shape of models represented by this component.

latent\_size
: Python int dimensionality of the latent space in this model.

name
: Name of this model component.

parameters
: List of Parameter(name, prior, bijector) namedtuples for this
    model.

## LinearRegression {#linearregression}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/LinearRegression>

Formal representation of a linear regression from provided covariates.

Inherits From: StructuralTimeSeries

```python
tfp.sts.LinearRegression(
    design_matrix, weights_prior=None, name=None
)
```

This model defines a time series given by a linear combination of covariate time
series provided in a design matrix:

`observed_time_series = matmul(design_matrix, weights)`

The design matrix has shape [num\_timesteps, num\_features]. The weights are
treated as an unknown random variable of size [num\_features] (both components
also support batch shape), and are integrated over using the same approximate
inference tools as other model parameters, i.e., generally HMC or variational
inference.

This component does not itself include observation noise; it defines a
deterministic distribution with mass at the point matmul(design\_matrix,
weights). In practice, it should be combined with observation noise from another
component such as tfp.sts.Sum, as demonstrated below.

### Examples {#examples}

Given series1, series2 as Tensors each of shape [num\_timesteps] representing
covariate time series, we create a regression model that conditions on these
covariates:

```python
regression = tfp.sts.LinearRegression(
    design_matrix=tf.stack([series1, series2], axis=-1),
    weights_prior=tfd.Normal(loc=0., scale=1.))
```

Here we've also demonstrated specifying a custom prior, using an informative
Normal(0., 1.) prior instead of the default weakly-informative prior.

As a more advanced application, we might use the design matrix to encode holiday
effects. For example, suppose we are modeling data from the month of December.
We can combine day-of-week seasonality with special effects for Christmas Eve
(Dec 24), Christmas (Dec 25), and New Year's Eve (Dec 31), by constructing a
design matrix with indicators for those dates.

```python
holiday_indicators = np.zeros([31, 3])
holiday_indicators[23, 0] = 1  # Christmas Eve
holiday_indicators[24, 1] = 1  # Christmas Day
holiday_indicators[30, 2] = 1  # New Year's Eve

holidays = tfp.sts.LinearRegression(design_matrix=holiday_indicators,
                                    name='holidays')
day_of_week = tfp.sts.Seasonal(num_seasons=7,
                               observed_time_series=observed_time_series,
                               name='day_of_week')
model = tfp.sts.Sum(components=[holidays, seasonal],
                    observed_time_series=observed_time_series)
```

Note that the Sum component in the above model also incorporates observation
noise, with prior scale heuristically inferred from observed\_time\_series.

In these examples, we've used a single design matrix, but batching is also
supported. If the design matrix has batch shape, the default behavior constructs
weights with matching batch shape, which will fit a separate regression for each
design matrix. This can be overridden by passing an explicit weights prior with
appropriate batch shape. For example, if each design matrix in a batch contains
features with the same semantics (e.g., if they represent per-group or
per-observation covariates), we might choose to share statistical strength by
fitting a single weight vector that broadcasts across all design matrices:

```python
design_matrix = get_batch_of_inputs()
design_matrix.shape  # => concat([batch_shape, [num_timesteps, num_features]])

# Construct a prior with batch shape `[]` and event shape `[num_features]`,
# so that it describes a single vector of weights.
weights_prior = tfd.Independent(
    tfd.StudentT(df=5,
                 loc=tf.zeros([num_features]),
                 scale=tf.ones([num_features])),
    reinterpreted_batch_ndims=1)
linear_regression = LinearRegression(design_matrix=design_matrix,
                                     weights_prior=weights_prior)
```

## LinearGaussianStateSpaceModel {#lineargaussianstatespacemodel}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/distributions/LinearGaussianStateSpaceModel>
NOTE: hard to get a full grasp of what's going on, example is incomplete.

```python
tfp.distributions.LinearGaussianStateSpaceModel(
    num_timesteps, transition_matrix, transition_noise, observation_matrix,
    observation_noise, initial_state_prior, initial_step=0, validate_args=False,
    allow_nan_stats=True, name='LinearGaussianStateSpaceModel'
)
```

A linear Gaussian state space model, sometimes called a Kalman filter,
posits a latent state vector z[t] of dimension latent\_size that evolves over
time following linear Gaussian transitions,

`z[t+1] = F * z[t] + N(b; Q)  # latent state`
`x[t] = H * z[t] + N(c; R)    # observed series`

for transition matrix F, transition bias b and covariance matrix Q, and
observation matrix H, bias c and covariance matrix R. At each timestep, the
model generates an observable vector x[t], a noisy projection of the latent
state. The transition and observation models may be fixed or may vary between
timesteps.

The event shape is [num\_timesteps, observation\_size], where observation\_size is
the dimension of each observation x[t]. The observation and transition models
must return consistent shapes.

This implementation **supports vectorized computation over a batch of models**.
All of the parameters (prior distribution, transition and observation operators
and noise models) must have a consistent batch shape.

Able to have [time-varying](https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/distributions/LinearGaussianStateSpaceModel#time-varying%5Fprocesses%5F2) transitional matrices (weekday/weekend).

### Examples {#examples}

Consider a simple tracking model, in which a two-dimensional latent state
represents the position of a vehicle, and at each timestep we see a noisy
observation of this position (e.g., a GPS reading). The vehicle is assumed to
move by a random walk with standard deviation step\_std at each step, and
observation noise level std. We build the marginal distribution over noisy
observations as a state space model:

```python
ndims = 2
step_std = 1.0
noise_std = 5.0
model = LinearGaussianStateSpaceModel(
  num_timesteps=100,
  transition_matrix=tfl.LinearOperatorIdentity(ndims),
  transition_noise=tfd.MultivariateNormalDiag(
   scale_diag=step_std**2 * tf.ones([ndims])),
  observation_matrix=tfl.LinearOperatorIdentity(ndims),
  observation_noise=tfd.MultivariateNormalDiag(
   scale_diag=noise_std**2 * tf.ones([ndims])),
  initial_state_prior=tfd.MultivariateNormalDiag(
   scale_diag=tf.ones([ndims]))
)
```

using the identity matrix for the transition and observation operators. We can
then use this model to generate samples, compute marginal likelihood of observed
sequences, and perform posterior inference.

```python
x = model.sample(5) # Sample from the prior on sequences of observations.
lp = model.log_prob(x) # Marginal likelihood of a (batch of) observations.

# Compute the filtered posterior on latent states given observations,
# and extract the mean and covariance for the current (final) timestep.
_, filtered_means, filtered_covs, _, _ = model.forward_filter(x)
current_location_posterior = tfd.MultivariateNormalFullCovariance(
              loc=filtered_means[..., -1, :],
              scale=filtered_covs[..., -1, :])

# Run a smoothing recursion to extract posterior marginals for locations
# at previous timesteps.
posterior_means, posterior_covs = model.posterior_marginals(x)
initial_location_posterior = tfd.MultivariateNormalFullCovariance(
              loc=posterior_means[..., 0, :],
              scale=posterior_covs[..., 0, :])
```

## AdditiveStateSpaceModel {#additivestatespacemodel}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/AdditiveStateSpaceModel>
NOTE: Basically a model of models...

A state space model representing a sum of component state space models.

Inherits From: LinearGaussianStateSpaceModel

```python
tfp.sts.AdditiveStateSpaceModel(
    component_ssms, constant_offset=0.0, observation_noise_scale=None,
    initial_state_prior=None, initial_step=0, validate_args=False,
    allow_nan_stats=True, name=None
)
```

### Examples {#examples}

To construct an additive state space model combining a local linear trend and
**day-of-week** seasonality component (note, the StructuralTimeSeries classes, e.g.,
Sum, provide a higher-level interface for this construction, which will likely
be preferred by most users):

```python
num_timesteps = 30
local_ssm = tfp.sts.LocalLinearTrendStateSpaceModel(
    num_timesteps=num_timesteps,
    level_scale=0.5,
    slope_scale=0.1,
    initial_state_prior=tfd.MultivariateNormalDiag(
        loc=[0., 0.], scale_diag=[1., 1.]))
day_of_week_ssm = tfp.sts.SeasonalStateSpaceModel(
    num_timesteps=num_timesteps,
    num_seasons=7,
    initial_state_prior=tfd.MultivariateNormalDiag(
        loc=tf.zeros([7]), scale_diag=tf.ones([7])))
additive_ssm = tfp.sts.AdditiveStateSpaceModel(
    component_ssms=[local_ssm, day_of_week_ssm],
    observation_noise_scale=0.1)

y = additive_ssm.sample()
print(y.shape)
# => []
```

## AutoregressiveStateSpaceModel {#autoregressivestatespacemodel}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/AutoregressiveStateSpaceModel>

State space model for an autoregressive process.

Inherits From: LinearGaussianStateSpaceModel

```python
tfp.sts.AutoregressiveStateSpaceModel(
    num_timesteps, coefficients, level_scale, initial_state_prior,
    observation_noise_scale=0.0, initial_step=0, validate_args=False, name=None
)
```

A state space model (SSM) posits a set of latent (unobserved) variables that
evolve over time with dynamics specified by a probabilistic transition model
p(z[t+1] | z[t]). At each timestep, we observe a value sampled from an
observation model conditioned on the current state, p(x[t] | z[t]). The special
case where both the transition and observation models are Gaussians with mean
specified as a linear function of the inputs, is known as a linear Gaussian
state space model and supports tractable exact probabilistic calculations; see
tfp.distributions.LinearGaussianStateSpaceModel for details.

In an autoregressive process, the expected level at each timestep is a linear
function of previous levels, with added Gaussian noise:

`level[t+1] = sum(coefs * levels[t:t-order:-1]) + N(0., level_scale)`

The process is characterized by a vector coefficients whose size determines the
order of the process (how many previous values it looks at), and by level\_scale,
the standard deviation of the noise added at each step.

### Mathematical Details {#mathematical-details}

The autoregressive model implements a
tfp.distributions.LinearGaussianStateSpaceModel with latent\_size = order and
observation\_size = 1. The latent state vector encodes the recent history of the
process, with the current value in the topmost dimension. At each timestep, the
transition sums the previous values to produce the new expected value, shifts
all other values down by a dimension, and adds noise to the current value. This
is formally encoded by the transition model.

### Examples {#examples}

A simple model definition:

```python
ar_model = AutoregressiveStateSpaceModel(
    num_timesteps=50,
    coefficients=[0.8, -0.1],
    level_scale=0.5,
    initial_state_prior=tfd.MultivariateNormalDiag(
        scale_diag=[1., 1.]))

y = ar_model.sample() # y has shape [50, 1]
lp = ar_model.log_prob(y) # log_prob is scalar
```

Passing additional parameter dimensions constructs a batch of models. The
overall batch shape is the broadcast batch shape of the parameters:

```python
ar_model = AutoregressiveStateSpaceModel(
    num_timesteps=50,
    coefficients=[0.8, -0.1],
    level_scale=tf.ones([10]),
    initial_state_prior=tfd.MultivariateNormalDiag(
        scale_diag=tf.ones([10, 10, 2])))

y = ar_model.sample(5) # y has shape [5, 10, 10, 50, 1]
lp = ar_model.log_prob(y) # has shape [5, 10, 10]
```

## tfp.sts.forecast {#tfp-dot-sts-dot-forecast}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/forecast>

Construct predictive distribution over future observations.

```python
tfp.sts.forecast(
    model, observed_time_series, parameter_samples, num_steps_forecast,
    include_observation_noise=True
)
```

Given samples from the posterior over parameters, return the predictive
distribution over future observations for num\_steps\_forecast timesteps.

Args:

model
: An instance of StructuralTimeSeries representing a time-series model.
    This represents a joint distribution over time-series and their parameters
    with batch shape [b1, ..., bN].

observed\_time\_series
: float Tensor of shape concat([sample\_shape,
    model.batch\_shape, [num\_timesteps, 1]]) where sample\_shape corresponds to
    i.i.d. observations, and the trailing [1] dimension may (optionally) be
    omitted if num\_timesteps > 1. May optionally be an instance of
    tfp.sts.MaskedTimeSeries including a mask Tensor to encode the locations of
    missing observations.

parameter\_samples
: Python list of Tensors representing posterior samples of
    model parameters, with shapes [concat([[num\_posterior\_draws],
    param.prior.batch\_shape, param.prior.event\_shape]) for param in
    model.parameters]. This may optionally also be a map (Python dict) of
    parameter names to Tensor values.

num\_steps\_forecast
: scalar int Tensor number of steps to forecast.

include\_observation\_noise
: Python bool indicating whether the forecast
    distribution should include uncertainty from observation noise. If True, the
    forecast is over future observations, if False, the forecast is over future
    values of the latent noise-free time series. Default value: True.

Returns:

forecast\_dist
: a tfd.MixtureSameFamily instance with event shape
    [num\_steps\_forecast, 1] and batch shape concat([sample\_shape,
    model.batch\_shape]), with num\_posterior\_draws mixture components.

### Examples {#examples}

Suppose we've built a model and fit it to data using HMC:

```python
day_of_week = tfp.sts.Seasonal(
    num_seasons=7,
    observed_time_series=observed_time_series,
    name='day_of_week')
local_linear_trend = tfp.sts.LocalLinearTrend(
    observed_time_series=observed_time_series,
    name='local_linear_trend')
model = tfp.sts.Sum(components=[day_of_week, local_linear_trend],
                    observed_time_series=observed_time_series)

samples, kernel_results = tfp.sts.fit_with_hmc(model, observed_time_series)
```

Passing the posterior samples into forecast, we construct a forecast
distribution:

```python
forecast_dist = tfp.sts.forecast(model, observed_time_series,
                                 parameter_samples=samples,
                                 num_steps_forecast=50)

forecast_mean = forecast_dist.mean()[..., 0]  # shape: [50]
forecast_scale = forecast_dist.stddev()[..., 0]  # shape: [50]
forecast_samples = forecast_dist.sample(10)[..., 0]  # shape: [10, 50]
```

If using variational inference instead of HMC, we'd construct a forecast using
samples from the variational posterior:

```python
(variational_loss,
  variational_distributions) = tfp.sts.build_factored_variational_loss(
    model=model, observed_time_series=observed_time_series)

# OMITTED: take steps to optimize variational loss

samples = {k: q.sample(30) for (k, q) in variational_distributions.items()}
forecast_dist = tfp.sts.forecast(model, observed_time_series,
                                      parameter_samples=samples,
                                      num_steps_forecast=50)
```

We can visualize the forecast by plotting:

```python
from matplotlib import pylab as plt
def plot_forecast(observed_time_series, forecast_mean, forecast_scale, forecast_samples):
  plt.figure(figsize=(12, 6))

  num_steps = observed_time_series.shape[-1]
  num_steps_forecast = forecast_mean.shape[-1]
  num_steps_train = num_steps - num_steps_forecast

  c1, c2 = (0.12, 0.47, 0.71), (1.0, 0.5, 0.05)
  plt.plot(np.arange(num_steps), observed_time_series,
            lw=2, color=c1, label='ground truth')

  forecast_steps = np.arange(num_steps_train, num_steps_train+num_steps_forecast)
  plt.plot(forecast_steps, forecast_samples.T, lw=1, color=c2, alpha=0.1)
  plt.plot(forecast_steps, forecast_mean, lw=2, ls='--', color=c2, label='forecast')
  plt.fill_between(forecast_steps,
                    forecast_mean - 2 * forecast_scale,
                    forecast_mean + 2 * forecast_scale, color=c2, alpha=0.2)

  plt.xlim([0, num_steps])
  plt.legend()

plot_forecast(observed_time_series,
              forecast_mean=forecast_mean,
              forecast_scale=forecast_scale,
              forecast_samples=forecast_samples)
```

## tfp.sts.fit\_with\_hmc {#tfp-dot-sts-dot-fit-with-hmc}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/fit%5Fwith%5Fhmc>

Draw posterior samples using Hamiltonian Monte Carlo (HMC).

```python
tfp.sts.fit_with_hmc(
    model, observed_time_series, num_results=100, num_warmup_steps=50,
    num_leapfrog_steps=15, initial_state=None, initial_step_size=None,
    chain_batch_shape=(), num_variational_steps=150, variational_optimizer=None,
    variational_sample_size=5, seed=None, name=None
)
```

Markov chain Monte Carlo (MCMC) methods are considered the gold standard of
Bayesian inference; under suitable conditions and in the limit of infinitely
many draws they generate samples from the true posterior distribution. HMC [1]
uses gradients of the model's log-density function to propose samples, allowing
it to exploit posterior geometry. However, it is computationally more expensive
than variational inference and relatively sensitive to tuning.

This method attempts to provide a sensible default approach for fitting
StructuralTimeSeries models using HMC. It first runs variational inference as a
fast posterior approximation, and initializes the HMC sampler from the
variational posterior, using the posterior standard deviations to set
per-variable step sizes (equivalently, a diagonal mass matrix). During the
warmup phase, it adapts the step size to target an acceptance rate of 0.75,
which is thought to be in the desirable range for optimal mixing [2].

### Examples {#examples}

Assume we've built a structural time-series model:

```python
day_of_week = tfp.sts.Seasonal(num_seasons=7,
    observed_time_series=observed_time_series,
    name='day_of_week')
local_linear_trend = tfp.sts.LocalLinearTrend(
    observed_time_series=observed_time_series,
    name='local_linear_trend')
model = tfp.sts.Sum(components=[day_of_week, local_linear_trend],
                    observed_time_series=observed_time_series)
```

To draw posterior samples using HMC under default settings:

```python
samples, kernel_results = tfp.sts.fit_with_hmc(model, observed_time_series)

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  samples_, kernel_results_ = sess.run((samples, kernel_results))

print("acceptance rate: {}".format(
  np.mean(kernel_results_.inner_results.is_accepted, axis=0)))
print("posterior means: {}".format(
  {param.name: np.mean(param_draws, axis=0)
   for (param, param_draws) in zip(model.parameters, samples_)}))
```

We can also run multiple chains. This may help diagnose convergence issues and
allows us to exploit vectorization to draw samples more quickly, although warmup
still requires the same number of sequential steps.

```python
from matplotlib import pylab as plt

samples, kernel_results = tfp.sts.fit_with_hmc(
  model, observed_time_series, chain_batch_shape=[10])

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  samples_, kernel_results_ = sess.run((samples, kernel_results))

print("acceptance rate: {}".format(
  np.mean(kernel_results_.inner_results.inner_results.is_accepted, axis=0)))

# Plot the sampled traces for each parameter. If the chains have mixed, their
# traces should all cover the same region of state space, frequently crossing
# over each other.
for (param, param_draws) in zip(model.parameters, samples_):
  if param.prior.event_shape.ndims > 0:
    print("Only plotting traces for scalar parameters, skipping {}".format(
      param.name))
    continue
  plt.figure(figsize=[10, 4])
  plt.title(param.name)
  plt.plot(param_draws)
  plt.ylabel(param.name)
  plt.xlabel("HMC step")

# Combining the samples from multiple chains into a single dimension allows
# us to easily pass sampled parameters to downstream forecasting methods.
combined_samples_ = [np.reshape(param_draws,
                                [-1] + list(param_draws.shape[2:]))
                     for param_draws in samples_]
```

## impute\_missing\_values / MaskedTimeSeries {#impute-missing-values-maskedtimeseries}

<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/MaskedTimeSeries>
<https://www.tensorflow.org/probability/api%5Fdocs/python/tfp/sts/impute%5Fmissing%5Fvalues>

### Examples {#examples}

To construct a simple MaskedTimeSeries instance:

```python
observed_time_series = tfp.sts.MaskedTimeSeries(
    time_series=tf.random_normal([3, 4, 5]),
    is_missing=[True, False, False, True, False])
```

Note that the mask we specified will broadcast against the batch dimensions of
the time series.

For time series with missing entries specified as NaN 'magic values', you can
generate a mask using tf.is\_nan:

```python
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

time_series_with_nans = [-1., 1., np.nan, 2.4, np.nan, 5]
observed_time_series = tfp.sts.MaskedTimeSeries(
  time_series=time_series_with_nans,
  is_missing=tf.is_nan(time_series_with_nans))

# Build model using observed time series to set heuristic priors.
linear_trend_model = tfp.sts.LocalLinearTrend(
  observed_time_series=observed_time_series)
model = tfp.sts.Sum([linear_trend_model],
                    observed_time_series=observed_time_series)

# Fit model to data
parameter_samples, _ = tfp.sts.fit_with_hmc(model, observed_time_series)

# Forecast
forecast_dist = tfp.sts.forecast(
  model, observed_time_series, num_steps_forecast=5)

# Impute missing values
observations_dist = tfp.sts.impute_missing_values(model, observed_time_series)
print('imputed means and stddevs: ',
      observations_dist.mean(),
      observations_dist.stddev())
```

## Edward2 {#edward2}

<https://github.com/tensorflow/probability/blob/master/tensorflow%5Fprobability/python/experimental/edward2/README.md>

Example of [logistic regression](https://github.com/tensorflow/probability/blob/master/tensorflow%5Fprobability/examples/logistic%5Fregression.py)

## Structural Time Series modeling in TensorFlow Probability {#structural-time-series-modeling-in-tensorflow-probability}

<https://medium.com/tensorflow/structural-time-series-modeling-in-tensorflow-probability-344edac24083>

### Structural Time Series {#structural-time-series}

Structural time series (STS) models [3] are a family of probability models for
time series that includes and generalizes many standard time-series modeling
ideas, including:

- autoregressive processes,
- moving averages,
- local linear trends,
- seasonality, and
- regression and variable selection on external covariates (other time series
    potentially related to the series of interest).

An STS model expresses an observed time series as the sum of simpler components:

![[screenshot-03.png]]

### Linear model to predict electricity demand given temperature {#linear-model-to-predict-electricity-demand-given-temperature}

Full code [here](https://github.com/tensorflow/probability/blob/master/tensorflow%5Fprobability/examples/jupyter%5Fnotebooks/Structural%5FTime%5FSeries%5FModeling%5FCase%5FStudies%5FAtmospheric%5FCO2%5Fand%5FElectricity%5FDemand.ipynb)

Data is hourly; they also show a decomposition of all the effects (temperature,
hour of day, day of week, residual)

```python
temperature_effect = tfp.sts.LinearRegression(
    design_matrix=tf.reshape(temperature - np.mean(temperature),
                              (-1, 1)), name='temperature_effect')
hour_of_day_effect = tfp.sts.Seasonal(
    num_seasons=24,
    observed_time_series=demand,
    name='hour_of_day_effect')
day_of_week_effect = tfp.sts.Seasonal(
    num_seasons=7,
    num_steps_per_season=24,
    observed_time_series=demand,
    name='day_of_week_effect')
residual_level = tfp.sts.Autoregressive(
    order=1,
    observed_time_series=demand, name='residual')
model = tfp.sts.Sum([temperature_effect,
                      hour_of_day_effect,
                      day_of_week_effect,
                      residual_level],
                      observed_time_series=demand)
```

[//begin]: # "Autogenerated link references for markdown compatibility"
[[screenshot-03.png]: ../attachments/images/screenshot-03.png "screenshot-03.png"
[//end]: # "Autogenerated link references"