---
author: Vasken Dermardiros
categories: note
tags:
- research
- statistics
- sensitivity-analysis
title: Statistics, Sensitivity Analysis
---

p-values, normality, auto-correlation, Pearson, sensitivity, emulators,
financial statistics

# Quantopian Notes: Statistical tests for finance
From: [2017-09-28 Thu 08:52]
+ Dicky Fuller test to capture wrong assumptions/biases
+ Breush Pagan test to capture heteroskedasticity
+ Durbin Watson and/or Ljun-Box test to capture autocorrelation: all/most
  statistics are developed for non-auto-correlated data!
+ Newey West corrections for autocorrelation
+ Jarque Bera test for p-values

# Standardize or Normalize? — Examples in Python

https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc
Normalization makes training less sensitive to the scale of features, so we can
better solve for coefficients. Normalization makes it so that the input features
are in the same range (between 0 and
1)

Standardization makes the data centered around 0 -> z = (x_i - mean) / std To
compare features that have different units or scales.

# A Gentle Introduction to Normality Tests in Python

https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
An important decision point when working with a sample of data is whether to use
parametric or nonparametric statistical methods. Parametric statistical methods
assume that the data has a known and specific distribution, often a Gaussian
distribution. If a data sample is not Gaussian, then the assumptions of
parametric statistical tests are violated and nonparametric statistical methods
must be used.

If Data Is Gaussian:
	Use Parametric Statistical Methods
Else:
	Use Nonparametric Statistical Methods

Quantile-Quantile Plot
This plot generates its own sample of the idealized distribution that we are
comparing with, in this case the Gaussian distribution. The idealized samples
are divided into groups (e.g. 5), called quantiles. Each data point in the
sample is paired with a similar member from the idealized distribution at the
same cumulative distribution.

The tests assume that that the sample was drawn from a Gaussian distribution.
Technically this is called the null hypothesis, or H0. A threshold level is
chosen called alpha, typically 5% (or 0.05), that is used to interpret the
p-value.

In the SciPy implementation of these tests, you can interpret the p value as
follows.

p <= alpha: reject H0, not normal.
p > alpha: fail to reject H0, normal.

This means that, in general, we are seeking results with a larger p-value to
confirm that our sample was likely drawn from a Gaussian distribution.

A result above 5% does not mean that the null hypothesis is true. It means that
it is very likely true given available evidence. The p-value is not the
probability of the data fitting a Gaussian distribution; it can be thought of as
a value that helps us interpret the statistical test.

The *Shapiro-Wilk* test evaluates a data sample and quantifies how likely it is
that the data was drawn from a Gaussian distribution, named for Samuel Shapiro
and Martin Wilk.
=from scipy.stats import shapiro=
=stat, p = shapiro(data)=

The *D’Agostino’s K^2* test calculates summary statistics from the data, namely
kurtosis and skewness, to determine if the data distribution departs from the
normal distribution, named for Ralph D’Agostino. (The p-value is interpreted
against an alpha of 5% and finds that the test dataset does not significantly
deviate from normal.)
+ Skew is a quantification of how much a distribution is pushed left or right, a
  measure of asymmetry in the distribution.
+ Kurtosis quantifies how much of the distribution is in the tail. It is a
  simple and commonly used statistical test for normality.

*Anderson-Darling* Test is a statistical test that can be used to evaluate
*whether a data sample comes from one of among many known data samples, named
*for Theodore Anderson and Donald Darling.

It can be used to check whether a data sample is normal. The test is a modified
version of a more sophisticated nonparametric goodness-of-fit statistical test
called the Kolmogorov-Smirnov test.

A feature of the Anderson-Darling test is that it returns a list of critical
values rather than a single p-value. This can provide the basis for a more
thorough interpretation of the result.

Hard fail: A failure of one normality test means that your data is not normal.
As simple as that. Soft fail: If some of the methods suggest that the sample is
Gaussian and some not, then perhaps take this as an indication that your data is
Gaussian-like.

# P-values

https://www.statsdirect.com/help/basics/p_values.htm The P value, or calculated
probability, is the probability of finding the observed, or more extreme,
results when the null hypothesis (H0) of a study question is true – the
definition of ‘extreme’ depends on how the hypothesis is being tested. P is also
described in terms of rejecting H0 when it is actually true, however, it is not
a direct probability of this state.

The only situation in which you should use a one sided P value is when a large
change in an unexpected direction would have absolutely no relevance to your
study. This situation is unusual; if you are in any doubt then use a two sided P
value.

The alternative hypothesis (H1) is the opposite of the null hypothesis; in plain
language terms this is usually the hypothesis you set out to investigate. For
example, question is "is there a significant (not due to chance) difference in
blood pressures between groups A and B if we give group A the test drug and
group B a sugar pill?" and alternative hypothesis is " there is a difference in
blood pressures between groups A and B if we give group A the test drug and
group B a sugar pill".

The choice of significance level at which you reject H0 is arbitrary.
Conventionally the 5% (less than 1 in 20 chance of being wrong), 1% and 0.1% (P
< 0.05, 0.01 and 0.001) levels have been used. These numbers can give a false
sense of security.

Most authors refer to statistically significant as P < 0.05 and statistically
highly significant as P < 0.001 (less than one in a thousand chance of being
wrong).

At this point, a word about error. *Type I error* is the false rejection of the
null hypothesis and *type II error* is the false acceptance of the null
hypothesis. As an aid memoir: think that our cynical society rejects before it
accepts.

The significance level (alpha) is the probability of type I error. The power of
a test is one minus the probability of type II error (beta). Power should be
maximised when selecting statistical methods. If you want to estimate sample
sizes then you must understand all of the terms mentioned here.

# P-value (probability value)

https://en.wikipedia.org/wiki/P-value If we state one hypothesis only and the
aim of the statistical test is to verify whether this hypothesis is not false,
but not, at the same time, to investigate other hypotheses, then such a test is
called a significance test. A statistical hypothesis that refers only to the
numerical values of unknown parameters of a distribution is called a parametric
hypothesis. Methods of verifying statistical hypotheses are called statistical
tests. Tests of parametric hypotheses are called parametric tests.[6] We can
likewise also have non-parametric hypotheses and non-parametric tests.

The p-value is used in the context of null hypothesis testing in order to
quantify the idea of statistical significance of evidence. Null hypothesis
testing is a reductio ad absurdum argument adapted to statistics. In essence, a
claim is assumed valid if its counter-claim is improbable.

As a general example, if a null hypothesis is assumed to follow the standard
normal distribution N(0,1), then the rejection of this null hypothesis can
either mean (i) the mean is not zero, or (ii) the variance is not unity, or
(iii) the distribution is not normal, depending on the type of test performed.

The smaller the p-value, the higher the significance because it tells the
investigator that the hypothesis under consideration may not adequately explain
the observation.

Another concern is that the p-value is often misunderstood as being the
probability that the null hypothesis is true.

*Important* The p-value is widely used in statistical hypothesis testing,
specifically in null hypothesis significance testing. In this method, as part of
experimental design, before performing the experiment, one first chooses a model
(the null hypothesis) and a threshold value for p, called the significance level
of the test, traditionally 5% or 1% and denoted as α. If the p-value is less
than the chosen significance level (α), that suggests that the observed data is
sufficiently inconsistent with the null hypothesis and that the null hypothesis
may be rejected. However, that does not prove that the tested hypothesis is
true. When the p-value is calculated correctly, this test guarantees that the
type I error rate is at most α. For typical analysis, using the standard α =
0.05 cutoff, the null hypothesis is rejected when p < .05 and not rejected when
p > .05. The p-value does not, in itself, support reasoning about the
probabilities of hypotheses but is only a tool for deciding whether to reject
the null hypothesis.

The use of the p-value in statistics was popularized by Ronald Fisher, and it
plays a central role in his approach to the subject. In his influential book
Statistical Methods for Research Workers (1925), Fisher proposed the level p =
0.05, or a 1 in 20 chance of being exceeded by chance, as a limit for
statistical significance, and applied this to a normal distribution (as a
two-tailed test), thus yielding the rule of two standard deviations (on a normal
distribution) for statistical significance.

# Misunderstandings of p-values

https://en.wikipedia.org/wiki/Misunderstandings_of_p-values
1. *The p-value is /not/ the probability that the null hypothesis is true, or
   the probability that the alternative hypothesis is false.* A p-value can
   indicate the degree of compatibility between a dataset and a particular
   hypothetical explanation (such as a null hypothesis). Specifically, the
   p-value can be taken as the prior probability of an observed effect given
   that the null hypothesis is true—which should not be confused with the
   posterior probability that the null hypothesis is true given the observed
   effect (see prosecutor's fallacy). In fact, frequentist statistics does not
   attach probabilities to hypotheses.
2. *The p-value is not the probability that the observed effects were produced
   by random chance alone.* The p-value is computed under the assumption that a
   certain model, usually the null hypothesis, is true. This means that the
   p-value is a statement about the relation of the data to that hypothesis.
3. *The 0.05 significance level is merely a convention.* The 0.05 significance
   level (alpha level) non-significant p-value. However, this does not imply
   that there is generally a scientific reason to is often used as the boundary
   between a statistically significant and a statistically consider results on
   opposite sides of any threshold as qualitatively different, and the common
   choice of 0.05 as the threshold is only a convention. can be observed for an
   effect that is not meaningful or important. In fact, the larger the sample
4. *The p-value does not indicate the size or importance of the observed
   effect.* A small p-value size, the smaller the minimum effect needed to
   produce a statistically significant p-value (see effect size).

https://en.wikipedia.org/wiki/Null_hypothesis This is analogous to the legal
principle of presumption of innocence, in which a suspect or defendant is
assumed to be innocent (null is not rejected) until proven guilty (null is
rejected) beyond a reasonable doubt (to a statistically significant degree).

# Confidence interval

https://en.wikipedia.org/wiki/Confidence_interval In statistics, a confidence
interval (CI) is a type of interval estimate, computed from the statistics of
the observed data, that might contain the true value of an unknown population
parameter. The interval has an associated confidence level that, loosely
speaking, quantifies the level of confidence that the parameter lies in the
interval. More strictly speaking, the confidence level represents the frequency
(i.e. the proportion) of possible confidence intervals that contain the true
value of the unknown population parameter. In other words, if confidence
intervals are constructed using a given confidence level from an infinite number
of independent sample statistics, the proportion of those intervals that contain
the true value of the parameter will be equal to the confidence level.

A 95% confidence level does not mean that for a given realized interval there is
a 95% probability that the population parameter lies within the interval (i.e.,
a 95% probability that the interval covers the population parameter).

# Ridge regression vs lasso vs OLS

OLS tried to pick model parameters as to minimize the squared error between
model and true values. In Ridge regression, a squared parameter penalizing term
is added (L2 regularizer). In Lasso, an absolute parameter penlizing term is
added (L1 regularizer) and so removes weak features.

Data should be whitened first.

# F-tests and ANOVAs — Examples with the Iris dataset

https://medium.com/@rrfd/f-tests-and-anovas-examples-with-the-iris-dataset-fe7caa3e21d0

# One-Sided F-test

Just as you would perform a t-test to determine if a sample mean (test group)
came from another distribution (control group) with the same mean, an F-test can
compare the means of various groups and determine if they are equal by looking
at their variances. We can do this be checking the variations between the groups
and within the groups.

F-statistic = variance between groups / variance within groups

Before we jump into the F-test make sure a few assumptions are met from the
data, as this test is highly sensitive to non-normal data. This is because the
sampling distribution of a sample variance is directly affected by kurtosis of
the underlying distribution. The flatter or skinnier our sample distribution,
the more likely the chi-squared distribution will provide an incorrect answer.

*homoscedasticity* Finally let’s check for homoscedasticity using a Bartlett
test. If we reject the null hypothesis, we can also reject the assumption of
homoscedasticity. What about our Levene test, which has the same assumption as
Bartlett.

Keep in mind, the Bartlett test can provide incorrect results if the data is
non-normal, while Levene’s test is more robust against that type of data. This
is why it is possible to get different results from the two tests.

(In statistics, a sequence or a vector of random variables is homoscedastic if
all random variables in the sequence or vector have the same finite variance.
This is also known as homogeneity of variance. The complementary notion is
called heteroscedasticity.)

# Time-Series Analysis using Statsmodels Python package

http://www.statsmodels.org/stable/tsa.html
http://www.statsmodels.org/dev/examples/notebooks/generated/regression_diagnostics.html

# Dicky Fuller test to capture wrong assumptions/biases

http://www.statsmodels.org/dev/generated/statsmodels.tsa.stattools.adfuller.html
https://machinelearningmastery.com/time-series-data-stationary-python/
statsmodels.tsa.stattools.adfuller

In statistics, the Dickey–Fuller test tests the null hypothesis of whether a
unit root is present in an autoregressive model. The alternative hypothesis is
different depending on which version of the test is used, but is usually
stationarity or trend-stationarity.

![Stationary vs Non-Stationary](../attachments/Stationarycomparison.png)

Stationary means that the values stay around a mean.

There are three main versions of the test:

1. Test for a unit root:
\[ {\displaystyle \nabla y_{t}=\delta y_{t-1}+u_{t}\,} \nabla y_t =\delta y_{t-1}+u_t \, \]

2. Test for a unit root with drift:
\[ {\displaystyle \nabla y_{t}=a_{0}+\delta y_{t-1}+u_{t}\,} \nabla y_t =a_0+\delta y_{t-1}+u_t \, \]

3. Test for a unit root with drift and deterministic time trend:
\[ {\displaystyle \nabla y_{t}=a_{0}+a_{1}t+\delta y_{t-1}+u_{t}\,} \nabla y_t = a_0+a_1t+\delta y_{t-1}+u_t \, \]

The Augmented Dickey-Fuller test can be used to test for a unit root in a
univariate process in the presence of serial correlation.

Null Hypothesis (H0): If accepted, it suggests the time series has a unit root,
meaning it is non-stationary. It has some time dependent structure.

Alternate Hypothesis (H1): The null hypothesis is rejected; it suggests the time
series does not have a unit root, meaning it is stationary. It does not have
time-dependent structure.

p-value > 0.05: Accept the null hypothesis (H0), the data has a unit root and is
non-stationary.

p-value <= 0.05: Reject the null hypothesis (H0), the data does not have a unit
root and is stationary.

# Breush Pagan test to capture heteroskedasticity

In statistics, a collection of random variables is heteroscedastic if there are
sub-populations that have different variabilities from others. Here
"variability" could be quantified by the variance or any other measure of
statistical dispersion. Thus heteroscedasticity is the absence of
homoscedasticity.

In statistics, the Breusch–Pagan test, developed in 1979 by Trevor Breusch and
Adrian Pagan,[1] is used to test for heteroskedasticity in a linear regression
model. It was independently suggested with some extension by R. Dennis Cook and
Sanford Weisberg in 1983.[2] It tests whether the variance of the errors from a
regression is dependent on the values of the independent variables. In that
case, heteroskedasticity is present.

Suppose that we estimate the regression model

\[ {\displaystyle y=\beta _{0}+\beta _{1}x+u,\,} y=\beta _{0}+\beta _{1}x+u,\, \]

and obtain from this fitted model a set of values for $\hat{u}$, the residuals.
Ordinary least squares constrains these so that their mean is 0 and so, given
the assumption that their variance does not depend on the independent variables,
an estimate of this variance can be obtained from the average of the squared
values of the residuals. If the assumption is not held to be true, a simple
model might be that the variance is linearly related to independent variables.
Such a model can be examined by regressing the squared residuals on the
independent variables, using an auxiliary regression equation of the form

\[{\displaystyle {\hat {u}}^{2}=\gamma _{0}+\gamma _{1}x+v.\,} {\hat {u}}^{2}=\gamma _{0}+\gamma _{1}x+v.\, \]

This is the basis of the Breusch–Pagan test. It is a chi-squared test: the test
statistic is distributed nχ2 with k degrees of freedom. If the test statistic
has a p-value below an appropriate threshold (e.g. p<0.05) then the null
hypothesis of homoskedasticity is rejected and heteroskedasticity assumed.

# Durbin Watson test to capture autocorrelation

http://www.statsmodels.org/dev/generated/statsmodels.stats.stattools.durbin_watson.html
statsmodels.stats.stattools.durbin_watson

+ all/most statistics are developed for non-auto-correlated data! this is a way to check

In statistics, the Durbin–Watson statistic is a test statistic used to detect
the presence of autocorrelation (a relationship between values separated from
each other by a given time lag) in the residuals (prediction errors) from a
regression analysis. It is named after James Durbin and Geoffrey Watson. The
small sample distribution of this ratio was derived by John von Neumann (von
Neumann, 1941). Durbin and Watson (1950, 1951) applied this statistic to the
residuals from least squares regressions, and developed bounds tests for the
null hypothesis that the errors are serially uncorrelated against the
alternative that they follow a first order autoregressive process. Later, John
Denis Sargan and Alok Bhargava developed several von Neumann–Durbin–Watson type
test statistics for the null hypothesis that the errors on a regression model
follow a process with a unit root against the alternative hypothesis that the
errors follow a stationary first order autoregression (Sargan and Bhargava,
1983). Note that the distribution of this test statistic does not depend on the
estimated regression coefficients and the variance of the errors.[1]

A similar assessment can be also carried out with the Breusch–Godfrey test and
the Ljung–Box test.

If et is the residual associated with the observation at time t, then the test statistic is

\[ {\displaystyle d={\sum _{t=2}^{T}(e_{t}-e_{t-1})^{2} \over {\sum _{t=1}^{T}e_{t}^{2}}},} \]

where T is the number of observations.

If the Durbin–Watson statistic is substantially less than 2, there is evidence
of positive serial correlation. As a rough rule of thumb, if Durbin–Watson is
less than 1.0, there may be cause for alarm. Small values of d indicate
successive error terms are, on average, close in value to one another, or
positively correlated. If d > 2, successive error terms are, on average, much
different in value from one another, i.e., negatively correlated.

# Ljun-Box test to capture autocorrelation

The Ljung–Box test (named for Greta M. Ljung and George E. P. Box) is a type of
statistical test of whether any of a group of autocorrelations of a time series
are different from zero. Instead of testing randomness at each distinct lag, it
tests the "overall" randomness based on a number of lags, and is therefore a
portmanteau test.

The Ljung–Box test may be defined as:

H0: The data are independently distributed (i.e. the correlations in the
population from which the sample is taken are 0, so that any observed
correlations in the data result from randomness of the sampling process).

Ha: The data are not independently distributed; they exhibit serial correlation.

The test statistic is:

\[ {\displaystyle Q=n\left(n+2\right)\sum _{k=1}^{h}{\frac {{\hat {\rho }}_{k}^{2}}{n-k}}} \]

where /n/ is the sample size, $\hat{\rho }}_{k}$ is the sample autocorrelation at
lag /k/, and /h/ is the number of lags being tested. Under $H_{0}$ the statistic Q
follows a ${\displaystyle \chi _{(h)}^{2}}$. For significance level /α/, the
critical region for rejection of the hypothesis of randomness is.

$Q > \chi_{1-\alpha,h}^2$

where $\chi_{1-\alpha,h}^2$ is the 1-/α/-quantile of the chi-squared distribution
with /h/ degrees of freedom.

# Breusch-Godfrey test to capture autocorrelation

acorr_breush_godfrey function in the module statsmodels.stats.diagnostic

In statistics, the Breusch–Godfrey test, named after Trevor S. Breusch and
Leslie G. Godfrey,[1][2] is used to assess the validity of some of the modelling
assumptions inherent in applying regression-like models to observed data series.
In particular, it tests for the presence of serial correlation that has not been
included in a proposed model structure and which, if present, would mean that
incorrect conclusions would be drawn from other tests, or that sub-optimal
estimates of model parameters are obtained if it is not taken into account. The
regression models to which the test can be applied include cases where lagged
values of the dependent variables are used as independent variables in the
model's representation for later observations. This type of structure is common
in econometric models.

The Breusch–Godfrey serial correlation LM test is a test for autocorrelation in
the errors in a regression model. It makes use of the residuals from the model
being considered in a regression analysis, and a test statistic is derived from
these. The null hypothesis is that there is no serial correlation of any order
up to p.

# Newey West corrections for autocorrelation

A Newey–West estimator is used in statistics and econometrics to provide an
estimate of the covariance matrix of the parameters of a regression-type model
when this model is applied in situations where the standard assumptions of
regression analysis do not apply. It was devised by Whitney K. Newey and
Kenneth D. West in 1987, although there are a number of later variants.The
estimator is used to try to overcome autocorrelation (also called serial
correlation), and heteroskedasticity in the error terms in the models, often for
regressions applied to time series data.

The problem in autocorrelation, often found in time series data, is that the
error terms are correlated over time. This can be demonstrated in $Q^{*}$, a
matrix of sums of squares and cross products that involves $\sigma _{{(ij)}}$
and the rows of /X/. The least squares estimator /b/ is a consistent estimator
of $\beta$. This implies that the least squares residuals $e_{i}$ are
"point-wise" consistent estimators of their population counterparts $E_{i}$. The
general approach, then, will be to use $X$ and /e/ to devise an estimator of
$Q^{*}$. This means that as the time between error terms increases, the
correlation between the error terms decreases. The estimator thus can be used to
improve the ordinary least squares (OLS) regression when the residuals are
heteroskedastic and/or autocorrelated.

\[ {\displaystyle w_{\ell}=1-{\frac {\ell }{L+1}}} \]

In R, the packages sandwich[7] and plm[8] include a function for the Newey–West
estimator.
https://cran.r-project.org/package=sandwich
https://cran.r-project.org/package=plm

# Jarque Bera test for p-values, normality test

http://www.statsmodels.org/dev/generated/statsmodels.stats.stattools.jarque_bera.html
statsmodels.stats.stattools.jarque_bera

Test for normality.

In statistics, the Jarque–Bera test is a goodness-of-fit test of whether sample
data have the skewness and kurtosis matching a normal distribution.

# Examples for autocorrelations

http://www.johnwittenauer.net/a-simple-time-series-analysis-of-the-sp-500-index/

Autocorrelation, also known as serial correlation, is the correlation of a
signal with a delayed copy of itself as a function of delay. Informally, it is
the similarity between observations as a function of the time lag between them.
The analysis of autocorrelation is a mathematical tool for finding repeating
patterns, such as the presence of a periodic signal obscured by noise, or
identifying the missing fundamental frequency in a signal implied by its
harmonic frequencies. It is often used in signal processing for analyzing
functions or series of values, such as time domain signals.

*It's basically the Pearson correlation coefficient with lagged terms.*

#+BEGIN_SRC python
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf

lag_correlations = acf(stock_data['Logged First Difference'].iloc[1:])
lag_partial_correlations = pacf(stock_data['Logged First Difference'].iloc[1:])

fig, ax = plt.subplots(figsize=(16,12))
ax.plot(lag_correlations, marker='o', linestyle='--')
#+END_SRC

The auto-correlation function computes the correlation between a variable and
itself at each lag step up to some limit (in this case 40). The partial
auto-correlation function computes the correlation at each lag step that is NOT
already explained by previous, lower-order lag steps. We can plot the results to
see if there are any significant correlations

# Cross-Correlation

Technically, auto-correlation is a type of cross-correlation.

In signal processing, cross-correlation is a measure of similarity of two series
as a function of the displacement of one relative to the other. This is also
known as a sliding dot product or sliding inner-product. It is commonly used for
searching a long signal for a shorter, known feature.

For continuous functions f and g, the cross-correlation is defined as:

\[ (f\star g)(\tau )\ {\stackrel {\mathrm {def} }{=}}\int _{-\infty }^{\infty
}f^{*}(t)\ g(t+\tau )\,dt, \]

where $f^{*}$ denotes the complex conjugate of $f$, and $\tau$ is the
displacement, also known as lag, although a positive value of $\tau$ actually means that \[{\displaystyle
g(t+\tau )}\] leads $g(t)$.

Similarly, for discrete functions, the cross-correlation is defined as:

\[ (f\star g)[n]\ {\stackrel {\mathrm {def} }{=}}\sum _{m=-\infty }^{\infty
}f^{*}[m]\ g[m+n]. \]

# Vector autoregression

Vector autoregression (VAR) is a stochastic process model used to capture the
linear interdependencies among multiple time series. VAR models generalize the
univariate autoregressive model (AR model) by allowing for more than one
evolving variable. All variables in a VAR enter the model in the same way: each
variable has an equation explaining its evolution based on its own lagged
values, the lagged values of the other model variables, and an error term. VAR
modeling does not require as much knowledge about the forces influencing a
variable as do structural models with simultaneous equations: The only prior
knowledge required is a list of variables which can be hypothesized to affect
each other intertemporally.

A VAR model describes the evolution of a set of k variables (called endogenous
variables) over the same sample period (t = 1, ..., T) as a linear function of
only their past values. The variables are collected in a k × 1 vector yt, which
has as the i th element, yi,t, the observation at time "t" of the i th variable.
For example, if the i th variable is GDP, then yi,t is the value of GDP at
time t.

A p-th order VAR, denoted VAR(p), is

\[ y_{t}=c+A_{1}y_{{t-1}}+A_{2}y_{{t-2}}+\cdots +A_{p}y_{{t-p}}+e_{t},\, \]

where the l-periods back observation yt−l is called the l-th lag of y, c is a k
× 1 vector of constants (intercepts), Ai is a time-invariant k × k matrix and et
is a k × 1 vector of error terms satisfying

1. \[ {\mathrm {E}}(e_{t})=0\ \], — every error term has mean zero;
2. \[ {\mathrm {E}}(e_{t}e_{t}')=\Omega \, \] — the contemporaneous covariance
   matrix of error terms is Ω (a k × k positive-semidefinite matrix);
3. \[ {\mathrm {E}}(e_{t}e_{{t-k}}')=0\ \], for any non-zero k — there is no
   correlation across time; in particular, no serial correlation in individual
   error terms.[1]

A pth-order VAR is also called a VAR with p lags. The process of choosing the
maximum lag p in the VAR model requires special attention because inference is
dependent on correctness of the selected lag order.

# Econometric model

https://en.wikipedia.org/wiki/Econometric_model

# Mathieu Le Cam's thesis

Le Cam, Mathieu. “Short-Term Forecasting of the Electric Demand of HVAC Systems.” Concordia University, 2016. http://spectrum.library.concordia.ca/981381/.

The inputs of the autoregressive model are selected by autocorrelation analysis.
The past values of the regressor that are moderately to strongly correlated to
the value at time t are retained, with an autocorrelation coefficient greater or
equal to 0.7 [102].

> 0.7: moderate
> 0.9: strong

[102] Reddy TA. Applied data analysis and modeling for energy engineers and
scientists. New York, NY: Springer Science & Business Media, 2011.

# Pearson correlation coefficient

https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

For a population
\[ \rho _{X,Y}={\frac {\operatorname {cov} (X,Y)}{\sigma _{X}\sigma _{Y}}} \]

where:
\[ \operatorname {cov} \]  is the covariance
\[ \sigma _{X} \] is the standard deviation of X
\[ \sigma_Y \] is the standard deviation of Y

For a sample
\[ {\displaystyle r={\frac {\sum _{i=1}^{n}(x_{i}-{\bar {x}})(y_{i}-{\bar {y}})}{{\sqrt {\sum _{i=1}^{n}(x_{i}-{\bar {x}})^{2}}}{\sqrt {\sum _{i=1}^{n}(y_{i}-{\bar {y}})^{2}}}}}} \]

where:
n is the number of samples
\[ x_{i},y_{i} \] are the single samples indexed with i
\[ {\bar {x}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i} \] (the sample mean); and analogously for \[ {\bar {y}} \]

# What is sensitivity analysis?

According to Wikipedia, sensitivity analysis is “the study of how the
uncertainty in the output of a mathematical model or system (numerical or
otherwise) can be apportioned to different sources of uncertainty in its
inputs.” The sensitivity of each input is often represented by a numeric value,
called the sensitivity index. Sensitivity indices come in several forms:

1. First-order indices: measures the contribution to the output variance by a
   single model input alone.
2. Second-order indices: measures the contribution to the output variance caused
   by the interaction of two model inputs.
3. Total-order index: measures the contribution to the output variance caused by
   a model input, including both its first-order effects (the input varying
   alone) and all higher-order interactions.

# Sensitivity Analysis: Morris

http://salib.readthedocs.io/en/latest/api.html#method-of-morris

In applied statistics, the Morris method for global sensitivity analysis is a
so-called one-step-at-a-time method (OAT), meaning that in each run only one
input parameter is given a new value. It facilitates a global sensitivity
analysis by making a number r of local changes at different points x(1 → r) of
the possible range of input values.

# Sensitivity Analysis: Sobol

http://salib.readthedocs.io/en/latest/basics.html#an-example
http://salib.readthedocs.io/en/latest/api.html#sobol-sensitivity-analysis
https://en.wikipedia.org/wiki/Variance-based_sensitivity_analysis

Variance-based sensitivity analysis (often referred to as the Sobol method or
Sobol indices, after Ilya M. Sobol) is a form of global sensitivity analysis.
Working within a probabilistic framework, it decomposes the variance of the
output of the model or system into fractions which can be attributed to inputs
or sets of inputs. For example, given a model with two inputs and one output,
one might find that 70% of the output variance is caused by the variance in the
first input, 20% by the variance in the second, and 10% due to interactions
between the two. These percentages are directly interpreted as measures of
sensitivity. Variance-based measures of sensitivity are attractive because they
measure sensitivity across the whole input space (i.e. it is a global method),
they can deal with nonlinear responses, and they can measure the effect of
interactions in non-additive systems.

From a black box perspective, any model may be viewed as a function Y=f(X),
where X is a vector of d uncertain model inputs {X1, X2, ... Xd}, and Y is a
chosen univariate model output (note that this approach examines scalar model
outputs, but multiple outputs can be analysed by multiple independent
sensitivity analyses). Furthermore, it will be assumed that the inputs are
independently and uniformly distributed within the unit hypercube, i.e.
$X_{i}\in [0,1]$ for i=1,2,...,d. This incurs no loss of generality because any
input space can be transformed onto this unit hypercube. f(X) may be decomposed
in the following way,

\[ {\displaystyle Y=f_{0}+\sum _{i=1}^{d}f_{i}(X_{i})+\sum _{i<j}^{d}f_{ij}(X_{i},X_{j})+\cdots +f_{1,2,\dots ,d}(X_{1},X_{2},\dots ,X_{d})} \]

all the terms in the functional decomposition are orthogonal. This leads to
definitions of the terms of the functional decomposition in terms of conditional
expected values,

$f_{0}=E(Y)$
$f_{i}(X_{i})=E(Y|X_{i})-f_{0}$
$f_{{ij}}(X_{i},X_{j})=E(Y|X_{i},X_{j})-f_{0}-f_{i}-f_{j}$

# Sensitivity Analysis: Fractional Factorial

http://salib.readthedocs.io/en/latest/api.html#fractional-factorial

# Emulators

https://en.wikipedia.org/wiki/Sensitivity_analysis

Emulators (also known as metamodels, surrogate models or response surfaces) are
data-modeling/machine learning approaches that involve building a relatively
simple mathematical function, known as an emulator, that approximates the
input/output behaviour of the model itself.[30] In other words, it is the
concept of "modelling a model" (hence the name "metamodel"). The idea is that,
although computer models may be a very complex series of equations that can take
a long time to solve, they can always be regarded as a function of their inputs
Y=f(X). By running the model at a number of points in the input space, it may be
possible to fit a much simpler emulator η(X), such that η(X)≈f(X) to within an
acceptable margin of error. Then, sensitivity measures can be calculated from
the emulator (either with Monte Carlo or analytically), which will have a
negligible additional computational cost. Importantly, the number of model runs
required to fit the emulator can be orders of magnitude less than the number of
runs required to directly estimate the sensitivity measures from the model.[31]

Clearly the crux of an emulator approach is to find an η (emulator) that is a
sufficiently close approximation to the model f. This requires the following
steps,

+ Sampling (running) the model at a number of points in its input space. This
  requires a sample design.
+ Selecting a type of emulator (mathematical function) to use.
+ "Training" the emulator using the sample data from the model – this generally
  involves adjusting the emulator parameters until the emulator mimics the true
  model as well as possible.

Sampling the model can often be done with low-discrepancy sequences, such as the
Sobol sequence – due to mathematician Ilya M. Sobol or Latin hypercube sampling,
although random designs can also be used, at the loss of some efficiency. The
selection of the emulator type and the training are intrinsically linked, since
the training method will be dependent on the class of emulator. Some types of
emulators that have been used successfully for sensitivity analysis include,

+ Gaussian processes[31] (also known as kriging), where the any combination of
  output points is assumed to be distributed as a multivariate Gaussian
  distribution. Recently, "treed" Gaussian processes have been used to deal with
  heteroscedastic and discontinuous responses.[32][33]
+ Gradient boosting,[30] where a succession of simple regressions are used to
  weight data points to sequentially reduce error.
+ Random forests,[30] in which a large number of decision trees are trained, and
  the result averaged.
+ Polynomial chaos expansions,[34] which use orthogonal polynomials to
  approximate the response surface.
+ Smoothing splines,[35] normally used in conjunction with HDMR truncations (see
  below).

The use of an emulator introduces a machine learning problem, which can be
difficult if the response of the model is highly nonlinear. In all cases it is
useful to check the accuracy of the emulator, for example using
cross-validation.