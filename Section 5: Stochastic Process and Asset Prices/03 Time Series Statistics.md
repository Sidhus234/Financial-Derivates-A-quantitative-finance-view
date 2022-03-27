# Time Series Statistics

<h2>Autocorrelation Function of a Stationary Time Series:</h2>
Consider a time series:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=X(t_0), X(t_0 %2B 1), X(t_0 %2B 2) \cdots X(t_0 %2B k) \cdots">
</p>

It is called __strictly stationary__ if the distribution of 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\( X(k), X(k %2B 1), \cdots X(k %2B j) )">
</p>

only depends on _j_ and not _k_.

This means:  _X(k)_ has the same distribution as _X(1), X(k), X(k+1))_ has the same joint distribution as _(X(1), X(2))_ etc.

Strict stationarity is weakened to just stationarity if the condition holds only up to second moments.

The __autocovariance__ function for a time series _X(t)_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\gamma(k,l) = cov(X(k), X(l))"><br>
<img src="https://render.githubusercontent.com/render/math?math=\E\[X\(k\) - \E\(X\(k)))\(X\(l) - \E\(X\(l)))]">
</p>

The time series is __stationary__ if its autocovariance function is translation invariant along with the expection <img src="https://render.githubusercontent.com/render/math?math=\E\[X\(k)] = \mu"> (ie <img src="https://render.githubusercontent.com/render/math?math=\mu"> independent of _k_).

Translation invariance means:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\gamma\(k %2B t, l %2B t) = \gamma\(k, l)">
</p>

This means <img src="https://render.githubusercontent.com/render/math?math=cov\(X\(k), X\(l))"> only depends on the lag _l-k_.

In other worjds, stationarity implies:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=cov\(X\(0), X\(1)) = cov\(X\(1), X\(2))"><br>
<img src="https://render.githubusercontent.com/render/math?math==cov\(X\(2), X\(3))"><br>
<img src="https://render.githubusercontent.com/render/math?math=\cdots"><br>
<img src="https://render.githubusercontent.com/render/math?math==cov\(X\(k), X\(k %2B 1))"><br>  
</p>

The same applies to nonsuccessive pairs:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=cov\(X\(0), X\(5)) = cov\(X\(1), X\(6))\cdots">
</p>

as well as variances:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Var\(X\(0)) = Var\(X\(1)) = \cdots = Var\(X(k))">
</p>

In the stationary case we may thus redefine the autocovariance function as:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\gamma\(k) = cov\(X\(t), X\(t %2B))">
</p>

This is independent of t.

So far a stationary time series the autocorrelation function is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\rho\(k) = corr\(X\(t), X\(t %2B K)) = \frac{\gamma\(k)}{\gamma\(0)}">
</p>

which is also independent of t.

Note that <img src="https://render.githubusercontent.com/render/math?math=\rho\(0) = 1"> for any time series. 

<h2>Sample Autocovariance and Autocorrelation Functions:</h2>
Given a realized sample of a time series

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=x\(1), x\(2), \cdots x\(t) \cdots x\(N)"><br>
</p>

and with the sample mean

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\bar{x} = \frac{1}{N}\sum_{i=1}^{N}{x\(i)}"><br>
</p>

the sample autocovariance function is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\hat{\gamma\(k)} = \frac{1}{N} \sum_{i=1}^{N - k}{\(x\(i) - \bar{x}) \(x\(i %2B k) - \bar{x})}"><br>
</p>

The same autocorrelation function is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\hat{\rho\(k)} = \frac{\hat{\gamma\(k)}}{\hat{\gamma\(0)}}"><br>
</p>

We will plot the autocorrelaiton function for an independent sample _x(1), x(2) ... x(2000)_ from a standard normal, and for a lagged series

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y\(t) = 0.5x\(t - 2) %2B 0.3x\(t - 1) %2B 0.2x\(t)"><br>
</p>

<img src="../Images/S5_auto_corr_independent_sequence.png" alt="Autocorrelation for independent Sample"/>

<img src="../Images/S5_auto_corr_correlated_sequence.png" alt="Autocorrelation for a 3-Step Correlated Sequence"/>




