<h1>Binomial 2 Step Model</h1>
We will extend the 1 step binomal model now to 2 steps. We thus consider 3 times, _t=0, 1, and 2_. We have a probability space as depicted in the next slide. We have a stock price <img src="https://render.githubusercontent.com/render/math?math=S_{t}"> defined for the 3 times. <img src="https://render.githubusercontent.com/render/math?math=S_{0}"> is a given number, the initial value of the stock price, 

<img src="https://render.githubusercontent.com/render/math?math=S_{1}"> is a random variable taking 2 possible values <img src="https://render.githubusercontent.com/render/math?math=S_{1} \( %2B ) \: \: \text{and} \: \: S_{1} \( - )">. 

<img src="https://render.githubusercontent.com/render/math?math=S_{2}"> is a random variable taking 3 possible values <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( %2B %2B ), S_{2} \( %2B - ) \: \: \text{and} \: \: S_{2} \( - - )">. 

<h3>The "probability space" for the 2 step binomial model</h3>

<img src="../Images/S6_2Step_binomial_model.png" alt="2 Step Binomial Model"/>

<h3>Stock Price in 2 Step Binomial Model</h3>

<img src="../Images/S6_2Step_binomial_model_stockvalues.png" alt="Stock Price in 2 Step Binomial Model"/>

Implicitly <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( - - ) < S_{2} \( %2B - ) < S_{2} \( %2B %2B )">

Extending both the model and notation from the 1 step model, we assume there are numbers _d , u_ with _d < u_ such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{1} \( %2B ) = uS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{1} \( - ) = dS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( %2B %2B ) = uS_{1} \( %2B ) = u^{2}S_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( %2B - ) = dS_{1} \( %2B ) = udS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( %2B - ) = uS_{1} \( %2B ) = udS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{2} \( - - ) = dS_{1} \( - ) = d^{2}S_{0}"><br>
</p>

We assume we have a risk free interest rate _r_ such that an initial investment of _K_ at time 0 is worth _K ( 1 + r)_ at time 1 and _K(1+r)(1+r)_ at time 2. And we assume there is a derivative asset with the stock as its underlying and expiring at time 2. The value of the derivative at time _t_ is <img src="https://render.githubusercontent.com/render/math?math=D__{t}">. The values given of <img src="https://render.githubusercontent.com/render/math?math=D_{2}"> are the payoff of the derivative, but the earlier values <img src="https://render.githubusercontent.com/render/math?math=D_{1} \: \: \text{and} \: \: D_{0}"> are determined by arbitrage. 

<h3>Derivative Values in 2 Step Binomial Model</h3>

<img src="../Images/S6_2Step_binomial_model_derivative_values.png" alt="Derivative Values in 2 Step Binomial Model"/>

<img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B )"> bears the same relationship to its descendents <img src="https://render.githubusercontent.com/render/math?math=\( D_{2} \( %2B %2B ), D_{2} \( %2B - )"> as <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> does to its descendents, and similarly for <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - )">.

In particular, to calculate the arbitrage value of <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B )"> we discount <img src="https://render.githubusercontent.com/render/math?math=D_{2} \( %2B %2B ) \: \: \text{and} \: \: D_{2} \( %2B - )"> and then take the risk neutral expectation. 

Similarly <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - )"> is the risk neutral expectation of the discounted values of <img src="https://render.githubusercontent.com/render/math?math=D_{2} \( %2B - ) \: \: \text{and} \: \: D_{2} \( - - )">. 

Finally to calculate <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> we take the risk neutral expectation of <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B ) \: \: \text{and} \: \: D_{1} \( - )"> after discounting them. 

Because of the relationship between the stock price values and their descendents in the binomial model ( ir the same _u_ and _d_ is used at each step) the risk neutral probabilities are the same for each step. This outlines a "backpropagation algorithm" for pricing derivatives in the 2 step model.


<h3>Example</h3>
Consider a 2 step binomial model for a stock with u = 1.2 and d= 0.9. Suppose the risk free interest rate is 6%. Suppose there is a derivative, with the stock as its underlying, and expiring at time 2, with a payoff given by <img src="https://render.githubusercontent.com/render/math?math=D_{2} \( %2B %2B ) = 10 \: \: \text{and} \: \: D_{2} \( - - ) = 25">.  Compute the fair price of this derivative at time 0.

<img src="../Images/S6_15_example_Derivatives.png" alt="Derivatives Values"/>

The values at time 2 represent the known payoff. All other values must be determined by arbitrage. To compute arbitrage price for the derivative, we will use risk neutral expectations, and so we need the risk neutral probabilities. Recall the risk neutral probabilities are:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = \frac{1 %2B r - d}{u - d} \: \: \text{and} \: \: \tilde{q} = \frac{u - 1- r}{u -d}">
</p>

We compute these using our given data: _u =1.2, d=0.9, r=6% = 0.06_.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = \frac{1 %2B 0.06 - 0.9}{1.2 - 0.9} = 0.53333"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\tilde{q} = \frac{1.2 - 1 - 0.06}{1.2 - 0.9} = 0.46667">
</p>

Now we compute risk neutral expectations and arbitrage prices for the derivative. 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B ) = \tilde{p} \frac{-15}{1 %2B r} %2B \tilde{q} \frac{10}{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \( 0.53333 ) \frac{-15}{1.06} %2B \( 0.46667 ) \frac{10}{1.06} = -3.145"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - ) = \tilde{p} \frac{10}{1 %2B r} %2B \tilde{q} \frac{25}{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - ) = \( 0.53333 ) \frac{10}{1.06} %2B \( 0.46667 ) \frac{25}{1.06} = 16.038"><br>
</p>

<img src="../Images/S6_15_example_Derivatives_2.png" alt="Updated Derivate Chart"/>

Now, given the values we have computed for <img src="https://render.githubusercontent.com/render/math?math=D_{1}"> we can carry out the final step of computing <img src="https://render.githubusercontent.com/render/math?math=D_{0}">, once again, using the risk neutral expectation. We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \tilde{p} \frac{-3.145}{1 %2B r} %2B \tilde{q} \frac{16.038}{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \( 0.53333 ) \frac{-3.145}{1.06} %2B \( 0.46667 ) \frac{16.038}{1.06} = 5.478"><br>
</p>

So we have calculated the fair price of our derivative. We plot the final version of our binomial diagram:

<img src="../Images/S6_15_example_Derivatives_3.png" alt="Updated Derivative Diagram"/>
