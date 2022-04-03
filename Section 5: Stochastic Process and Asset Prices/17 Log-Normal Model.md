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

We may also look at this from the point of view of stationarity. Strict stationarity means the multivariate distribution of returns does not change with time; stationarity means this is true up to second moments, variances and autocorrelations. Empirically, asset returns tend to be stationary over reasonable periods of time. And this is what we would expect in principle (primacy of returns). But returns and price jumps cannot both be stationary. A 10% return implies a $1 jump for a stock trading at $10 but a $20 jump for a stock trading at $200. 

<img src="../Images/S9_working_Capital_days.png" alt="Working Capital Days"/>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=">
</p>
