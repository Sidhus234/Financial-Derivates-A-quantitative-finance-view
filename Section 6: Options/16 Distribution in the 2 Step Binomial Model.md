<h1>Distribution in the 2 Step Binomial Model</h1>
Here, we will calculate the risk neutral probability distribution for the asset price <img src="https://render.githubusercontent.com/render/math?math=S_{2}"> at time 2 in the 2 step binomial model. 

In doing so, we will also express the arbitrage price of any derivative contingent on the asset as a risk neutral expectation.

<img src="../Images/S6_2Step_binomial_model_derivative_values.png" alt="Derivative Values in 2-Step Binomial Model"/>

We use risk neutral expecations to express <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B )"> and <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - )"> in terms of the values of <img src="https://render.githubusercontent.com/render/math?math=D_{2}">.

Let <img src="https://render.githubusercontent.com/render/math?math=\tilde{p} \: \: \text{and} \: \: \tilde{q}"> be the risk neutral probabilities. Then

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B ) = \tilde{p} \frac{D_{2} \( %2B %2B )}{1 %2B r } %2B \tilde{q} \frac{D_{2} \( %2B - ) }{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - ) = \tilde{p} \frac{D_{2} \( %2B - )}{1 %2B r } %2B \tilde{q} \frac{D_{2} \( - - ) }{1 %2B r}">
</p>

where _r_ is the risk free rate. Now we express <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> as a risk neutral expectation of the values of <img src="https://render.githubusercontent.com/render/math?math=D_{1}"> and expand:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \tilde{p} \frac{D_{1} \( %2B )}{1 %2B r} %2B \tilde{q} \frac{D_{1} \( - )}{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \frac{\tilde{p}}{1 %2B r} \[ \tilde{p} \frac{D_{2} \( %2B %2B )}{1 %2B r } %2B \tilde{q} \frac{D_{2} \( %2B - ) }{1 %2B r} ] %2B \frac{\tilde{q}}{1 %2B r} \[ \tilde{p} \frac{D_{2} \( %2B - )}{1 %2B r } %2B \tilde{q} \frac{D_{2} \( - - ) }{1 %2B r} ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \tilde{p}^{2} \frac{D_{2} \( %2B %2B )}{ \( 1 %2B r)^{2}} %2B 2 \tilde{p} \tilde{q} \frac{D_{2} \( %2B - )}{ \( 1 %2B r )^{2} } %2B \tilde{q}^{2} \frac{D_{2} \( - - )}{ \( 1 %2B r)^{2}}"><br>
</p>

Recall the binomial distribution from our random walk study. These are the binomial probabilities <img src="https://render.githubusercontent.com/render/math?math=bin \( k %3B 2, \tilde{p} )"> 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \text{bin} \( 2 %3B 2, \tilde{p} ) \frac{D_{2} \( %2B %2B )}{ \( 1 %2B r)^{2}} %2B \text{bin} \( 1 %3B 2, \tilde{p} ) \frac{D_{2} \( %2B - )}{ \( 1 %2B r )^{2} } %2B \text{bin} \( 0 %3B 2, \tilde{p} ) \frac{D_{2} \( - - )}{ \( 1 %2B r)^{2}}">
</p>

This represents the derivative price <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> as a binomial expectation of its discounted payoff values:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\text{bin} \( %3B, 2, \tilde{p}} \[ \frac{D_{2}}{ \( 1 %2B r)^{2}} ]">
</p>

<h3>Example</h3>
We will apply the previous formula to the derivative pricing problem from the last notes. The final result is displayed in a 2-step binomial diagram here:

<img src="../Images/S6_15_example_Derivatives_3.png" alt="Solved Example- Derivative Binomial tree diagram"/>

We will solve this problem using the risk neutral expectation formula we have derived here. Recall the data from this problem <img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = 0.53333, \tilde{q} = 0.46667, r = 6% = 0.06">. We will calculate the derivative price at time 0 from the risk neutral expectation

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\text{bin} \( %3B, 2, \tilde{p}} \[ \frac{D_{2}}{ \( 1 %2B r)^{2}} ]">
</p>

Explictly:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math== \tilde{p}^{2} \frac{D_{2} \( %2B %2B )}{ \( 1 %2B r)^{2}} %2B 2 \tilde{p} \tilde{q} \frac{D_{2} \( %2B - )}{ \( 1 %2B r )^{2} } %2B \tilde{q}^{2} \frac{D_{2} \( - - )}{ \( 1 %2B r)^{2}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \(0.53333)^{2} \frac{-15}{ \( 1.06)^{2}} %2B 2 \(0.53333) \(0.46667) \frac{10}{ \( 1.06 )^{2} } %2B \(0.46667)^{2} \frac{25}{ \( 1.06)^{2}} = 5.4785">
</p>

Thus our previous answer (and the risk neutral expectation formula) is confirmed. 
