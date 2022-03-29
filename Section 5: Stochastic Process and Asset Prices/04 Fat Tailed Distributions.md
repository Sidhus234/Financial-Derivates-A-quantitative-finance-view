<h1>Fat-Tailed Distributions</h1>
The density of a normal distribution:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=f\(x) = \frac{1}{\sqrt{2\pi\sigma^{2}}} \exp^{-\(x-\mu)^{2}/2\sigma^{2}}">
</p>

for a normal distribution with mean <img src="https://render.githubusercontent.com/render/math?math=\mu"> and variance <img src="https://render.githubusercontent.com/render/math?math=\sigma^{2}">.

As <img src="https://render.githubusercontent.com/render/math?math=x \rightarrow \pm\infinity"> the normal density decays exponentially.

Probability distributions whose densities decay slower than exponeniatlly are referred to as __fat-tailed__.

Typically, a fat-tailed density decays algenraically, ie as a power <img src="https://render.githubusercontent.com/render/math?math=1/x^{k}">. For instance, the Student t distribution with <img src="https://render.githubusercontent.com/render/math?math=\nu"> degress of freedom has a density decaying as 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{\vert x\vert^{\nu %2B 1}} as x \rightarrow \pm\infinity">
</p>

<img src="../Images/S5_Normal_vs_Fat_tailed_Distribution.png" alt="Normal vs Fat Tailed Distribution"/>

<h2>Normal Q-Q Plots:</h2>
Generally a quantile-quantile plot (q-q) is a plot of quantiles of one random sample against the quantiles of another.
A normal q-q plot is a plot of quantiles of the sample against the theoretical quantiles of a normal distribution.
<li>Key property of normal q-q plots: if a random sample <img src="https://render.githubusercontent.com/render/math?math=\{ x_{i} \}_{i=1}^{N}"> is from a normal distribution then it's q-q plot will be close to a straight line.</li>
<li>If the sample is from a fat-tailed distribution, its normal q-q plot will deviate from a straight line at extremes.</li>

<img src="../Images/S5_QQPLOT_Normal_dist.png" alt="Q-Q plot for Normal Distribution"/>

<img src="../Images/S5_QQPLOT_T_Dist.png" alt="Q-Q Plot for t distribution"/>

<h2>Fat Tails and Kurtosis:</h2>
Kurtosis is a statistic related to the fourth moment of a random variable. It is thus even more sensitive to extreme values than the variance. 

The standard definition of kurtosis is as a normalized version of the fourth moment.

If _X_ is a random variable with mean <img src="https://render.githubusercontent.com/render/math?math=\mu"> and variance <img src="https://render.githubusercontent.com/render/math?math=\sigma^{2}"> then the __kurtosis__ of _X_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Kurt \( X ) = \E \[ \( \frac{ X - \mu }{ \sigma} )^{4} ]">
</p>

The kurtosis of a normally distributed random varianle is 3. So, for any random variable _X_ we define its __excess kurtosis__ as

<p align="center">Excess Kurtosis = Kurt(X) - 3</p>

As a fourth moment, the kurtosis is a measure of dispersion that is more sensitive to extreme values than the second moment, the variance.

Excess kurtosis, is a measure of how much more of a tendency there is for extreme values than a normal distribution.

Thus positive excess kurtosis is a measure of the fat-tailedness of a distribution.

The t distribution with 5 degrees of freedom has an excess kurtosis of 6 (it is undefined or infinite for <img src="https://render.githubusercontent.com/render/math?math=\nu < 6"> and decreases to 0 for larger <img src="https://render.githubusercontent.com/render/math?math=\nu">.

We will use excess kurtosis as one measure of fat-tailedness in empirical return distributions.
