<h1>Binomial Model - General Case</h1>
Here we will generalize our arbitrage pricing technique from the previous notes for any asset. Assume we have a stock (or any asset) with value <img src="https://render.githubusercontent.com/render/math?math=S_{t}"> so that at _t=0_ the stocj takes an initial value <img src="https://render.githubusercontent.com/render/math?math=S_{0}"> and at time 1 the stock has may take one of the 2 values <img src="https://render.githubusercontent.com/render/math?math=S_{1} \( - ) < S_{1} \( %2B )"> with probabilities

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{1} = S_{1} \( %2B ) ) = p \: \text{and} \: Prob \( S_{1} = S_{1} \( - ) ) = q \: \text{where} \: q = 1-p">
</p>

Aboout the probabilities _p_ and _q_ we assume only that _0< p, q_. Let _d_, and _u_ be numbers with _0 < d < u_ such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{1} \( %2B ) = uS_{0} \: \text{and} \: S_{1} \( - ) = dS_{0}">
</p>

<img src="../Images/S6_Stock_Prive_in_BinomialModel.png" alt="Stock Prive in Binomial Model"/>

While not required, one may assume conceptually that _d < 1 < u_. Notice that _u_ and _d_ are the gross returns in the + and - states respectively. 

As befpre we ssume there is a risk free interest rate _r_ such that a cash investment of value _K_ at time _0_ worth _K(1+r)_ at time 1. Absence of arbitrage requires we assume

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d < 1 %2B r < u">
</p>

For if _1+r <= d_ than with certainty the stock returns at least as well as the risk free investment. We could create an arbitrage by borrowing at the risk free rate and spending the proceeds on the stock. If _u <= 1+r_ we construct an arbitrate by shorting the stock and investing the proceeds at the risk free rate.

As before, we also assume we have a derivative, with stock as its underlying, with values <img src="https://render.githubusercontent.com/render/math?math=D_{t}">, with an initial value <img src="https://render.githubusercontent.com/render/math?math=D_{0]"> and such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{1} = D_{1} \( %2B ) \: \text{when} \: S_{1} = S_{1} \( %2B )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{1} = D_{1} \( - ) \: \text{when} \: S_{1} = S_{1} \( - )">
</p>

<img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B ) \: \text{and} \: D_{1} \( - )"> constitute the payoff of the derivative, and are assumed known. <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> is the fair value of the derivative at time 0 and must be determined by arbitrage. The arbitrage will be realized by delta hedging, as in the example from last time, but now for the general case.

For delta hedging, recall we form a portfolio consisting of <img src="https://render.githubusercontent.com/render/math?math=\delta"> units of the stock and a short position in the derivative. <img src="https://render.githubusercontent.com/render/math?math=\delta"> is chosen such that the portfolio is riskless. Let our arbitrage portfolio have value function

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{t} = \delta S_{t} - D_{t}">
</p>

<img src="https://render.githubusercontent.com/render/math?math=\delta"> is chosen so that <img src="https://render.githubusercontent.com/render/math?math=V_{1}"> is the same in all states of the world at time 1 and so in not random. Thus <img src="https://render.githubusercontent.com/render/math?math=\delta"> solves the equation

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\delta u S_{0} - D_{1} \( %2B ) = \delta d S_{0} - D \( - )">
</p>

Solving this linear equation for <img src="https://render.githubusercontent.com/render/math?math=\delta"> gives

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\delta = \frac{D_{1} \( %2B ) - D_{1} \( - )}{ \( u - d ) S_{0}}">
</p>

Thus

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{1} = \delta S_{1} - D_{1} = \frac{D_{1} \( %2B ) - D_{1} \( - ) }{ \( u - d ) S_{0}} S_{1} - D_{1}">
</p>

is the same value in both states of the world. We can calculate its deterministic value by evaluating it in either state. Using the + state:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{1} = \frac{D_{1} \( %2B ) - D_{1} \( - ) }{ \( u - d ) S_{0}} uS_{0} - D_{1} \( %2B )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V_{1} = \frac{D_{1} \( %2B ) - D_{1} \( - ) }{ \( u - d ) } u - D_{1} \( %2B )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V_{1} = \frac{ \( D_{1} \( %2B ) - D_{1} \( - ) ) u - \( u - d ) D_{1} \( %2B )}{u - d}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V_{1} = \frac{ dD_{1} \( %2B ) - uD_{1} \( - ) }{u - d}"><br>
</p>

<img src="https://render.githubusercontent.com/render/math?math=V_{1}"> has the same value in the - state. As <img src="https://render.githubusercontent.com/render/math?math=V_{1}"> is, with probabilit 1, a constant value, by arbitrage, its value at time 0 must be the dicounted value of the value at time 1:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{1} = \frac{ dD_{1} \( %2B ) - uD_{1} \( - ) }{ \( 1 %2B r ) \( u - d )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\text{Since} \: \: \text{also}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V_{0} = \delta S_{0} - D_{0}"><br>
</p>

we may determine <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> by equating these expressions and solving for <img src="https://render.githubusercontent.com/render/math?math=D_{0}">. So

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\delta S_{0} - D_{0} = \frac{ dD_{1} \( %2B ) - uD_{1} \( - ) }{ \( 1 %2B r ) \( u - d )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\text{Solving} \: \: \text{for} \: \: D_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{0} = \delta S_{0} - \frac{ dD_{1} \( %2B ) - uD_{1} \( - ) }{ \( 1 %2B r ) \( u - d )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{0} = \frac{ D_{1} \( %2B ) - D_{1} \( - ) }{ \( u - d ) S_{0} } S_{0} - \frac{ dD_{1} \( %2B ) - uD_{1} \( - ) }{ \( 1 %2B r ) \( u - d )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{0} = \frac{ \( 1 %2B r ) \( D_{1} \( %2B ) - D_{1} \( - ) ) - \( dD_{1} \( %2B ) - uD_{1} \( - ) ) }{ \( 1 %2B r ) \( u - d )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{0} = \frac{ \( 1%2B r - d ) D_{1} \( %2B ) %2B \( u - 1 - r ) D_{1} \( - )}{\( 1 %2B r ) \( u - d )}"><br>
</p>

This gives us the fair value of the derivative at time 0. Rewrite the expression in the following way:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \frac{1 %2B r - d}{u - d} \( \frac{D_{1} \( %2B )}{1 %2B r} ) %2B \frac{u - 1 - r}{u - d} \( \frac{D_{1} \( - )}{1 %2B r} )">
</p>

This presents the fair price of the derivative as a linear combination of the discounted values it takes on expiry. Next, we will use this representation to great effect to derive a powerful method for pricing derivatives in the binomial model.
