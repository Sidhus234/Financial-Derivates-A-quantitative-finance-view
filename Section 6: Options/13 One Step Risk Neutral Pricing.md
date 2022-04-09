<h1>One Step Risk Neutral Pricing</h1>
Here we continue from the last notes, deriving the fair price of a general derivative in the 1 step binomial model. Recall that we ended with the final form for the fair price of a derivative at time 0:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \frac{1 %2B r - d}{u - d} \( \frac{D_{1} \( %2B )}{1 %2B r} ) %2B \frac{u - 1 - r}{u - d} \( \frac{D_{1} \( - )}{1 %2B r} )">
</p>

Define

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = \frac{1 %2B r - d}{ u - d} \: \: \text{and} \: \: \tilde{q} = \frac{u - 1 - r}{u - d} \: \: \text{and} \: \: \tilde{p} %2B \tilde{q} = 1">
</p>

So, in fact, the fair price of the derivative at time 0 is a weighted average of its discounted possible values at expiry:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \tilde{p} \( \frac{D_{1} \( %2B )}{1 %2B r} ) %2B \tilde{q} \( \frac{D_{1} \( - )}{1 %2B r} )">
</p>

We define

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{P} = \( \tilde{p} , \tilde{q} )">
</p>

<img src="https://render.githubusercontent.com/render/math?math=\tilde{P}"> defines a probability distribution on our 2 point set { + , - }. And the above shows that <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> is the expected value in this distribution of <img src="https://render.githubusercontent.com/render/math?math=D_{1}"> after discounting:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\tilde{P}} \[ \frac{D_{1}}{1 %2B r} ]">
</p>

<img src="https://render.githubusercontent.com/render/math?math=\tilde{P}"> is called the __risk neutral distribution__ on the 2 point set { +, -}. So we have found that in absence of arbitrage the price of any asset contingent on our stock is the expected value, in the risk neutral distribution, of its dicounted value at time 1. In other words: in the 1-step binomial model, we may compute the arbitrage price of any derivative (at time 0) by computing the risk neutral expectation of its discounted value at time 1.

__Remark:__ Why is <img src="https://render.githubusercontent.com/render/math?math=\tilde{P}"> called a "risk neutral distribution"?

We have shown that for any asset defined in our 1 step binomial model (any such asset is a derivative or contingent on the stock price) with _W(t)_, we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W \( 0 ) = E^{\tilde{P}} \[ \frac{W \( 1 )}{1 %2B r} ]">
</p>

Because _W(0)_ and 1 %2B r are deterministic we may move them in and out of the expectation, so we can rewrite:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=1 %2B r = E^{\tilde{P}} \[ \frac{W \( 1 )}{W \( 0 )} ] = E^{\tilde{P}} \[ \text{Gross} \: \: \text{Return} \: \: \text{of} \: \: W ]">
</p>

In particular this is true for the stock:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=1 %2B r = E^{\tilde{P}} \[ \frac{S \( 1 )}{S \( 0 )} ] = E^{\tilde{P}} \[ \text{Gross} \: \: \text{Return} \: \: \text{of} \: \: S ]">
</p>

The risk neutral distribution is therefore that distribution such that the expected return on any asset is the same as the return on a riskless asset. This is true no matter what the risk level of the asset is. Therefore the risk neutral distribution is that distribution for asset prices that would hold in the economy if all investors were indifferent to risk levels.

In the real economy, asset prices are not distributed as a risk neutral distribution. Investors expect a better return if they are to take on a risky investment. The use of the risk neutral distribution to calculate arbitrage prices is simply a mathematical device (a trick) that allows us to calculate arbitrage prices in a very convenient way. It is not meant to imply that the distribution of asset prices is risk neutral in the real world. As observed, the actual real world possibilities are inrrelevant for calculating arbitrage based prices. 
