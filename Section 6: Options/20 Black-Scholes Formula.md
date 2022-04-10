<h1>Black-Scholes Formula</h1>
We have derived the arbitrage determined premium for a call option in an _n_ step binomial model. We have also shown that in the limit as the number of timesteps in the binomial model converges to a log-normal process. This suggests a strategy for deriving the value for a call when the underlying is assumed to have a log-normal distribution:

Take the limit, as <img src="https://render.githubusercontent.com/render/math?math=n \rightarrow \infinity"> of the call price in the _n_ step binomial model. We have expressed the call premium in the binomial model as a risk neutral expectation of the discounted payoff of the call:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{0} = E^{\text{bin} \( %3B n, \tilde{p})} \[ \frac{ \max \( S_n - K, 0) }{ \( 1 %2B r )^{n}} ]">
</p>

This is an expectation in the binomial distribution at time _n_ in the model, but it is the risk neutral expecation, since the binomial is the risk neutral distribution. We may write the expectation explicitly:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_0 = \sum_{j=0}^{n} \frac{n!}{ j! \( n - j )!} \tilde{p}^{j} \tilde{q}^{ \(n-j ) } \frac{ \max \( u^{j} d^{n-j} S_0 - K, 0) }{ \( 1 %2B r)^{n}}">
</p>

However, although there are approaches to the problem that use the explicit form for <img src="https://render.githubusercontent.com/render/math?math=C_0">, we will use a different approach. We will only need the expression as a risk neutral expectation. We write the expectation in terms of the approximating binomial process we have studies in previous lectures:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{0} = E^{\text{bin} \( %3B n, \tilde{p})} \[ \frac{ \max \( S^{ \( n )} \( T ) - K, 0) }{ \( 1 %2B \frac{r}{n} )^{\lfloor nT \rfloor}} ]">
</p>

The convergence of <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t )"> to the log-normal model established in the last lectures in sufficient to allow us to pass this expectation to the sme continuum limit.

Specifically: in the last lecture we showed that as <img src="https://render.githubusercontent.com/render/math?math=n \rightarrow \infinity">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( t ) \rightarrow S_0 e^{t \( r - \frac{\sigma^{2}}{2} ) %2B \sigma W \( t )}">
</p>

as a stochastic pricess (to be precise: weak convergence of stochastic process). To take the limit of the expectation, all we need is convergence at time T:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( T ) \rightarrow S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma W \( T )}">
</p>

This is also weak convergence, of the random variable <img src="https://render.githubusercontent.com/render/math?math=S^{\( n )} \( T )">, and this is sufficient to also take the limit of the expectation. This convergence is strong enough to imply

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} E^{\text{bin} \( %3B n, \tilde{p})} \[ \max \( S^{ \( n )} \( T ) - K, 0) ] = E^{L.N.} \[ \max \( S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma W \( T )} - K, 0) ]">
</p>

L.N. denotes the log-normal distribution. In this distribution, _W(t)_ is a Brownian motion. In particular, _W(t)_ has a normal distribution with mean 0 and variance _T_. It follows that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Z = \frac{W \( T )}{\sqrt{T}} \thicksim \mathcal{N} \( 0, 1)">
</p>

We may therefore write the limiting expectation above as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=E^{L.N.} \[ \max \( S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma \sqrt{T} \frac{W \( T )}{\sqrt{T}}} - K, 0) ] = E^{L.N.} \[ \max \( S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma \sqrt{T} Z} - K, 0) ]">
</p>

We must also take the limit of the discounting factor

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\( 1 %2B \frac{r}{n} )^{\lfloor n T \rfloor}">
</p>

For this, we use

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} \frac{\lfloor n T \rfloor}{n} = T">
</p>

and from calculas

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} \( 1 %2B \frac{r}{n}) = e^{r}">
</p>

So that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} \( 1 %2B \frac{r}{n} )^{\lfloor n T \rfloor} = \lim_{n \rightarrow \infinity} \( 1 %2B \frac{r}{n} )^{n \frac{\lfloor n T \rfloor}{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \lim_{n \rightarrow \infinity} \[ \( 1 %2B \frac{r}{n} )^n ]^{\frac{\lfloor n T \rfloor}{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\[ e^r ]^T = e^{rT}"><br>
</p>

Now we take the limit of the call price as the number of timesteps in the binomial model goes to infinity.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{n \rightarrow \infinity} C_0 = \lim_{n \rightarrow \infinity } E^{\text{bin} \( %3B n, \tilde{p})} \[ \frac{ \max \( S^{ \( n )} \( T ) - K, 0) }{ \( 1 %2B \frac{r}{n} )^{\lfloor nT \rfloor}} ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \lim_{n \rightarrow \infinity } \frac{1}{\( 1 %2B \frac{r}{n} )^{\lfloor nT \rfloor}} E^{\text{bin} \( %3B n, \tilde{p})} \[ \max \( S^{ \( n )} \( T ) - K, 0)]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \frac{1}{e^{rT}} E^{L.N.} \[ \max \( S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma W \( T )} - K, 0)]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== e^{-rT} E^{L.N.} \[ \max \( S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma \sqrt{T} Z} - K, 0)]">
</p>

Since we knoe the probability density function of _Z_, a standard normal random variable, we may write the expectation as an explicit integral. This integral can be evaluated yielding the __Black-Scholes formula__:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim{n \rightarrow \infinity} = e^{-rT} \int_{- \infinity}^{\infinity} \max \(  S_0 e^{T \( r - \frac{\sigma^{2}}{2} ) %2B \sigma \sqrt{T} Z} - K, 0 ) \frac{e^{-z^{2} / 2}}{\sqrt{2 \pi}} dz">
  <img src="https://render.githubusercontent.com/render/math?math==S_0 N \( d_{%2B} ) - K e^{-rT} N d_{-}">
</p>

where

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d_{\pm} = \frac{1}{\sigma \sqrt{T}} \[ \log \( \frac{S_0}{K} ) %2B \( r \pm \frac{\sigma^2}{2} ) T]">
</p>

and

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=N \( x ) = \frac{1}{\sqrt{2 \pi}} \int_{- \infinity}^{infinity} e^{-z^{2}/2} dz">
</p>

The integral is straightforward to evaluate, though somewhat tedious. In next few lectures we will discuss the supporting theory for Black-Scholes formula. 

<h3>Decomposition of the process of deriving Black-Scholes Formula</h3>
<li>Justifying why the integral (the expected value of the call payoff when the underlying has a log-normal distribution at expiration) is call price. </li>
<li>Evaluating the integral to obtain the Black-Scholes formula. Step 2 is purely mechanical process.</li>
<li>The financial core of the arguement is demonstrating that the call premium is the expected value of the payoff under  alog-normal distribution for the underlying at expiry.</li>
