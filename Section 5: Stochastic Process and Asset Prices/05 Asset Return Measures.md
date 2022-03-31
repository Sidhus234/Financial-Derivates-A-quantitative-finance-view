<h1>Continuously Compounded Returns</h1>

Let _P(t)_ be the price of some asset observed at time _t_.

We define the 1-period __continuously compounded return__ or __log return__ as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r \( t ) = log \( \frac{P \( t )}{P \( t - 1 )} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math== log \( P \( t ) ) - log \( P \( t - 1 ) )"><br>
</p>

Define the _k_-period continusously compounded return

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r_{k} \( t ) = log \( \frac{P \( t )}{P \( t - k )} )">
</p>

Note that the continuously compounded return is the log of the corresponding gross return.

Continuosuly compounded returns combine across periods very simply.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r_{k} \( t ) = log \( \frac{P \( t )}{P \( t - k )} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math== log \( P \( t ) - log \(P \( t - k ))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== log \( P \( t ) - log \(P \( t - 1 )) %2B"><br>
  <img src="https://render.githubusercontent.com/render/math?math=log \( P \( t - 1 ) - log \(P \( t - 2 )) %2B"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\cdots %2B "><br>
  <img src="https://render.githubusercontent.com/render/math?math=log \( P \( t - k %2B 1 ) - log \(P \( t - k )) %2B"><br>
  <img src="https://render.githubusercontent.com/render/math?math== r \( t ) %2B r \( t - 1 ) %2B \cdots r \( t - k %2B 1 )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\sum_{i=0}^{k - 1} r \( t - i )"><br>
</p>

<h2>Example</h2>

Let _t_ = 1, 2, 3, 4, 5, 6 be successive (business days). Suppose we observe the prices for a stock on those days as P(1) = 105, P(2) = 111, P(3) = 102, P(4) = 109, P(5) = 107, P(6) = 108.
Compute the daily and weekly log returns.

The daily log or continuously compounded returns are

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r \( 2 ) = log \( \frac{P \( 2 )}{P \( 1 )} ) = log \( \frac{111}{105} ) = 0.0556"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r \( 3 ) = log \( \frac{P \( 3 )}{P \( 2 )} ) = log \( \frac{102}{111} ) = -0.0846"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r \( 4 ) = log \( \frac{P \( 4 )}{P \( 3 )} ) = log \( \frac{109}{102} ) = 0.064"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r \( 5 ) = log \( \frac{P \( 5 )}{P \( 4 )} ) = log \( \frac{107}{109} ) = -0.0185"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r \( 6 ) = log \( \frac{P \( 6 )}{P \( 5 )} ) = log \( \frac{108}{107} ) = 0.0093"><br>
  </p>
  
The weekly compounded returns are

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r_{5} \( 6 ) = r \( 2 ) %2B r \( 3 ) %2B r \( 4 ) %2B r \( 5 ) %2B r \( 6 ) = 0.0282"><br>
  </p>
 
 We will study the daily log returns _r(t)_ as a time series indexed by _t_ for a variety of assets.

The focus will be on certain cash products: stocks, currencies and commodities.
