<h1>Brownian Motion</h1>
To develop a more realistic model for asset prices, which still retains the properties of random walks we ant to keep, is to derive a continuous time model from random walks. One way to do this is to take the limit as the time step in the random walks get infinitely small, or in other words, take the limit as the number of jumps in any unit of time goes to infinity. If we do this, we must scale down, or shrink the size of the jumps. Otherwise, for instance, the variance will go to infinity. Let 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\sigma^{2} = Var \( X_{j} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\lim_{m \rightarrow \infinity } Var \( S_{m} ) = \lim_{m \rightarrow \infinity} Var \( \sum_{j=1}^{m} X_{j} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math={by independence} = \lim_{m \rightarrow \infinity } \sum_{j=1}^{m} Var \( X_{j} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\lim_{m \rightarrow \infinity} m \sigma^{2}"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\infinity"><br>
</p>

The jumps <img src="https://render.githubusercontent.com/render/math?math=X_{j}"> of size 1 must be scaled down for the limit to be sensible. The jumps should be reduced by dividing by some factor:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{X_{j}}{\alpha}">
</p>

The cental limit theorem suggest that <img src="https://render.githubusercontent.com/render/math?math=\alpha = \sqrt{m}">. Below derivaiton suggests that  <img src="https://render.githubusercontent.com/render/math?math=\alpha = \sqrt{m}"> is the right scaling.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\lim_{m \rightarrow \infinity} Var \( \sum_{j=1}^{m} \frac{X_{j}}{\sqrt{m}} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\lim_{m \rightarrow \infinity} \sum_{j=1}^{m} Var \( \frac{X_{j}}{\sqrt{m}} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math={ using Var \( \alpha X ) = \alpha^{2} Var \( X ) }"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\lim_{m \rightarrow \infinity} \sum_{j=1}^{m} \frac{1}{m} Var \( X_{j} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\lim_{m \rightarrow \infinity} \frac{1}{m} \sum_{j=1}^{m} \sigma^{2}"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\lim_{m \rightarrow \infinity} \frac{1}{m} m \sigma^{2}"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\sigma^{2} \lt \infinity"><br>
</p>

We wish to consider the limit as the number of timesteps _m_ per unit time gets large. For any real time _t >= 0_ the number of jumps will be some integer close to _mt_. So we consider the scaled random walks

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{t}^{ \( m )} = \sum_{j=1}^{ \lfloor m t \rfloor} \frac{X_{j}}{\sqrt{m}}">
</p>

<img src="../Images/S5_Scaled_randomwalk.png" alt="Working Capital Days">

__Explanation:__ Above chart shows 100 jumps scaled random walk.

<img src="../Images/S5_Scaled_randomwalk_10000.png" alt="Working Capital Days">

<h2>Definition</h2>
__Brownian motion__ is a continuous time stochastic process, conventionally denoted _W(t)_ with following properties:

<li> W(0) = 0 with probability 1.</li>
<li>The sample paths of W(t) are continuous with probability 1.</li>
<li>For t< s < r W(s) - W(t) is independent of W(r) - W(s).</li>
<li>For any t, s >= 0, W(t) - W(s) is normally distributed with mean 0 and variance |t-s|.</li>

<img src="../Images/S5_Brownianpath.png" alt="Brownian Motion">

It is consequence of the central limit theorem that the distribution of any increment <img src="https://render.githubusercontent.com/render/math?math=S_{t_{2}}^{ \( m )} - S_{t_{1}}^{ \( m )}"> converges to a normal as <img src="https://render.githubusercontent.com/render/math?math=m \rightarrow \infinity">. The independence of jumps in the random walk passes to independence of increments in the limit. And it is intuitively clear, from observing the limiting behavior of the sample paths, that the random walk converges, as a stochastic process, to Brownian motion. In fact, the random walk converges to Brownian motion in a very precise sense:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{t}^{ \( m ) } \rightarrow W \( t ) as m \rightarrow \infinity">
</p>

in the sense of "weak convergence of stochastic processes".
