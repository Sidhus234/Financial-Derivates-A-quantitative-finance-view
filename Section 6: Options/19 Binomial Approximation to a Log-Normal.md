<h1>Binomial Approximation to a Log-Normal</h1>
In this lecture we will see how to approximate a log-normal asset price process by a binomial model. In this way we will be able to pass our results for pricing options in a binomial model to a more realistic continuous time model. As noted in our treatment of asset price models, the log-normal model is a benchmark asset price model. Therefore, this approximation leads to a benchmark option pricing theory. Our final result will be the Black-Scholes formula for the fair price for a call (or put).

We begin by assuming that our underlying asset price _S(t)_ can be modelled by a log normal process

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S \( t ) = S \( 0 ) e^{ \mu t %2B \sigma W \( t )}">
</p>

where _W(t)_ is Brownian motion. <img src="https://render.githubusercontent.com/render/math?math=\mu \: \: \text{and} \: \: \sigma"> are the drift and volatility parameters. In our treatment of random walks and Brownian motion we saw that the scaled random walks converge to Brownian motion.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{t}^{\( m )} = \sum_{j = 1}^{\lfloor m t \rfloor} \frac{X_{j}}{\sqrt{m}}">
</p>

A modified random walk can be shown to converge to Brownian motion with drift. Let <img src="https://render.githubusercontent.com/render/math?math=X_j \: \: \text{for} \: \: j = 1 \cdots \infinity"> be a sequence of independent, identically distributed random variables where

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( X_j = %2B 1 ) = \frac{1}{2}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Prob \( X_j = - 1 ) = \frac{1}{2}"><br>
</p>

Then, for any positive integer _n_ define

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Y_{j}^{\( n )} = \frac{\mu}{n} %2B \frac{\sigma}{\sqrt{n}} X_j">
</p>

We define a sequence of modified random walks

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=U^{\( n ) } \( t ) = \sum_{j=1}^{\lfloor n t \rfloor} Y_{j}^{ \( n )}">
</p>

Then, similar to the case of the original random walk approximating Brownian motion, it can be shown that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} U^{ \( n )} \( t ) = \mu t %2B \sigma W \( t )">
</p>

As for the basic random walk, this is weak convergence of stochastic processes, not just convergence at some particular time _t_. We then define

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t ) = e^{U^{\( n )} \( t )}">
</p>

The weak convergence alluded to is strong enough to conclude

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t ) \rightarrow e^{\mu t %2B \sigma W \( t )} = S \( t )">
</p>

So <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t )"> is a discrete process that approximates our log-normal asset price process. In fact <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t )"> is a binomial process. To see this, start by writing out the logarithms of <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t )"> evaluated at the distance times <img src="https://render.githubusercontent.com/render/math?math=t = \frac{k}{n}">. We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\log \( S^{\( n )} \( \frac{k}{n} ) ) = U^{\( n )} \( \frac{k}{n} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\sum_{j=1}^{k} Y_{j}^{ \( n )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math==Y_{k}^{ \( n )} %2B \sum_{j=1}^{\( k - 1 )} Y_{j}^{ \( n )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math==Y_{k}^{ \( n )} %2B U^{\( n )} \( \frac{k-1}{n} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==Y_{k}^{ \( n )} %2B \log \( S^{\( n )} \( \frac{k-1}{n} ))"><br>
</p>

Now we exponentiate both sides

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( \frac{k}{n} ) = e^{Y_{k}^{\( n)}} S^{\( n )} \(  \frac{k-1}{n} )">
</p>

Now recall that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Y_{k}^{\( n )} = \frac{\mu}{n} %2B \frac{\sigma}{\sqrt{n}} X_{j}">
</p>

takes 2 values, each with the probability of 1/2, depending on whether or not <img src="https://render.githubusercontent.com/render/math?math=X_{j}"> takes the value of +1 or -1: 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Y_{k}^{\( n )} = \frac{\mu}{n} %2B \frac{\sigma}{\sqrt{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Y_{k}^{\( n )} = \frac{\mu}{n} - \frac{\sigma}{\sqrt{n}}"><br>
</p>

So if we define up factors and down factors

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=u = e^{\frac{\mu}{n} %2B \frac{\sigma}{\sqrt{n}}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=d = e^{\frac{\mu}{n} - \frac{\sigma}{\sqrt{n}}}"><br>
</p>

then we have either

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( \frac{k}{n} ) = u S^{\( n )} \(  \frac{k-1}{n} ) \:\: \text{or}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( \frac{k}{n} ) = d S^{\( n )} \(  \frac{k-1}{n} )"><br>
</p>

each with probability 1/2. But this is exactly a binomial model at the discrete times <img src="https://render.githubusercontent.com/render/math?math=\frac{k}{n}">.

With jumps in the binomial model occuring at the discrete times <img src="https://render.githubusercontent.com/render/math?math=\frac{k}{n}"> the number of jumps per unit time is _n_. We thus have a binomial model that converges to our original log-normal price process as the number of steps in the binomial model per unit time goes to infinity. We would like to use this to find formulas for option prices in the log-normal model by taking the limit as <img src="https://render.githubusercontent.com/render/math?math=n \rightarrow \infinity"> of the binomial call pricing formula.

One Problem: the call pricing formula was an expectation in the risk neutral distribution, but what we have is the convergence of the binomial model in the original "real world" distribution. 

To pass our call pricing formula to the limit, we need to know the limit, as a stochastic process, of the binomial model in the risk neutral distribution. We can show that, in the risk neutral distribution, the binomial process converges to a modified log-normal process:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} S^{\( n )} \( t ) = S_{0} e^{t \( r - \frac{\sigma^{2}}{2}} ) %2B \sigma W \( t )">
</p>

That is, in the risk neutral distribution, the binomial process <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t )"> converges to a modified log-normal distribution with a drift

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r - \frac{\sigma^{2}}{2}">
</p>

The technical details of the 2 limits described in this lecture (in the original real world distribution and the risk neutral distribution) will be presented in a supplementary article. The identification of the risk neutral limit of the binomial model will aloow us to derive a formula for the call price when the underlying asset is modified with a log-normal model. The result will be the Black-Scholes formula. This will be the subject of the next lecture. 
