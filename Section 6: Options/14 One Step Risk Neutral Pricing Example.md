<h1>One Step Risk Neutral Pricing Example</h1>
We will consider the example of a call in a 1 step binomial model considered previously. We will analyze this problem from the point of view of the risk neutral distribution.

Recall the stock has initial value 50 and at time 1 takes the value 65 with probability _p_ > 0 and the value 40 with probability _1-p_. The values of the call option were

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{1} \( %2B ) = \max \( 0, 65-55) = 10"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{1} \( - ) = \max \( 0, 40-55) = 0"><br>
</p>

Recall the risk free interest rate is _r = 8% = 0.08._

<img src="../Images/S6_Example_call_values.png" alt="Call Values"/>

We will determine <img src="https://render.githubusercontent.com/render/math?math=D_{0}"> using the risk neutral distribution.

First, we must calculate the risk neutral probabilities. Recall, they are

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = \frac{1 %2B r - d}{u -d} \: \: \text{and} \: \: \tilde{q} = \frac{u - 1- r}{u -d}">
</p>

where _u_ and _d_ are such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{1} \( %2B ) = uS_{0} \:\: \text{and} \:\: S_{1} \( - ) = dS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\rightarrow u = \frac{S_{1} \( %2B )}{S_{0}} \:\: \text{and} \:\: d = frac{S_{1} \( - )}{S_{0}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\rightarrow u = \frac{65}{50} \:\: \text{and} \:\: d = frac{40}{50}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\rightarrow u = 1.3 \:\: \text{and} \:\: d = 0.8">
</p>

Plugging our date into the expressions for the risk neutral probabilities:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\tilde{p} = \frac{1 %2B 0.08 - 0.8}{1.3 - 0.8} \: \: \text{and} \: \: \tilde{q} = \frac{1.3 - 1- 0.08}{1.3 - 0.8}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\rightarrow \tilde{p} = 0.56 \: \: \text{and} \: \: \tilde{q} = 0.44"><br>
</p>

From the last lecture, we know the call premium should be the expectation, in the risk neutral distribution of the discounted call payoff: 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\tilde{p}} \[ \frac{D_{1}}{ 1 %2B e} ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \tilde{p} \frac{D_{1} \( %2B )}{1 %2B r} %2B \tilde{q} \frac{D_{1} \( - ) }{1 %2B r}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \( 0.56 ) \frac{10}{1.08} %2B \( 0.44 ) \frac{0}{1.08} = 5.19"><br>
</p>

confirming our previous calculation.
