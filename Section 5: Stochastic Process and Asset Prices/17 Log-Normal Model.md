<h1>The Log-Normal Model</h1>
Here, we will further modify the Brownian motion model to remedy some of the outstanding problems. Like the random walk model Brownian motion has a significant probability of attaining negative values. Adding a drift term reduces this probability, but does not eliminate it. More serious is the limitation shared by both the random walk and Brownian motion that the size of the jumps does not scale with the price level: a $10 jump is just as likely for an asset trading at $15 as one trading at $250. We wil like to extend the model to remedy these defects, while still preserving the elements of market efficiency implicity in the independence of increments. _S(t)_ denotes the asset price.

We consider changes in _log(S(t))_. Let 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\psi \( t ) = log \( S \( t ) )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S \( t ) = e^{ \psi \( t ) }"><br>
</p>

If <img src="https://render.githubusercontent.com/render/math?math=\psi \( t %2B 1 ) = \psi \( t ) %2B \delta"> then 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S \(t %2B 1 ) = e^{ \psi \( t %2B 1 ) }"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S \(t %2B 1 ) = e^{ \psi \( t  ) %2B \delta }"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S \(t %2B 1 ) = e^{ \delta } e^{ \psi \( t ) }"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S \(t %2B 1 ) = e^{ \delta } S \( t )"><br>
</p>

So the price jump can be written as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S \( t %2B 1 ) - S \( t ) = e^{\delta} S \( t ) - S \( t )"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \( e^{\delta} - 1 ) S \( t )">
</p>

This relationship holds no matter what the overall price level. We could multiply the prices by 2, 10, 100, or any other factor and still the price jump would be the constant <img src="https://render.githubusercontent.com/render/math?math=e^{\delta} - 1"> times the initial price. So a fixed additive jump in _log(S(t))_ implies a price jump that scales witht he price level. A model in which the dynamics involve jumps of fixed size (on average) in _log(S(t))_ would have the sensitivity to the overall price level we are seeking. This suggests the idea of modelling _log(S(t))_ as Brownian motion (or a random walk) rather tha _S(t)_ itself.  

We may also look at this from the point of view of stationarity. Strict stationarity means the multivariate distribution of returns does not change with time; stationarity means this is true up to second moments, variances and autocorrelations. Empirically, asset returns tend to be stationary over reasonable periods of time. And this is what we would expect in principle (primacy of returns). But returns and price jumps cannot both be stationary. A 10% return implies a $1 jump for a stock trading at $10 but a $20 jump for a stock trading at $200. If we want returns to be stationarity, then we have to give up price levels being stationarity. 

In financial economics and econometrics, the consensus view is that asset returns are stationary, at least as a first approximation. Therefore it is reasonable to choose asset price models that lead to stationary returns. These considerations lead us to consider modelling _log(S(t))_ as a Brownian motion rather than _S(t)_ itself.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=log \( S \(t ) ) = W \( t )">
</p>

For the returns we will then have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=log \( \frac{S \( t )}{S \( t - 1 )} ) = log \( S \( t ) ) - log \( S \( t - 1 ) ) = W \( t ) - W \( t - 1 )">
</p>

From the properties of Brownian motion the sequence of Brownian differences _W(t) - W(t-1), W(t+1) - W(t), ... , W(t+k) - W(t+k-1)

are stationary as well as uncorrelated (independent in fact). Thus the log returns will also have these properties. Thus, modelling _log(S(t))_ as Brownian motion accomplishes 3 things:
<ol>
  <li>Average price jumps are proportional to the price level.</li>
  <li>Returns are stationary.</li>
  <li>Returns are uncorrelated.</li>
  </ol>

<h3>Pound-USD Returns</h3>

<img src="../Images/S5_GBP_USD_Returns.png" alt="GBP/USD Returns"/>

The returns are stationary in normal circumstances but there are external shocks which may divert the behavior. In long period of time period (18 years in above chart), we would observe few years of stationarity (till 2008, and then financial crisis hit and we observe high volatility).

<h3>Soyabean Returns</h3>

<img src="../Images/S5_Soyabean_Returns.png" alt="GBP/USD Returns"/>

High volatility in earlier period (2004 to 2005) and again in financial crisis (2008-2010). 2000 to 2003 and 2011 to 2020 we could identify the regime of stationarity. 

<h3>Successive Brownian MotionDifferences</h3>

<img src="../Images/S5_Successive_brownian_Motion_Differences.png" alt="GBP/USD Returns"/>

This model is not going to exhibit volatility clustering. And also there are no big shocks. 

<h2>Log-Normal Model</h2>
It is standard to add a drift term and a volatility factor <img src="https://render.githubusercontent.com/render/math?math=\sigma">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=log \( S \( t ) ) = \mu t %2B \sigma W \( t ) ">
</p>

Also, an initial value _S(0)_ should be included:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=log \( S \( t ) ) = log \( S \( 0 ) ) %2b \mu t %2B \sigma W \( t ) ">
</p>

We may then exponentiate both sides of this equation. The below equation is called __log-normal model__ of asset prices. Another term commonly used is __geometric Brownian Motion.__

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\( S \( t ) ) = S \( 0 ) e^{ \mu t %2B \sigma W \( t ) }">
</p>
