<h1>Full Binomial Model</h1>
Now we will consider the full binomial model for an arbitary number _(n)_ of steps. We will start, though, by extending our treatment for 1 and 2 steps to the 3 step binomial model. The work we have done up to the 2 step model extends in the natural way. Consider the general case of the stock price on the 3 step binomial model, as illustrated in the following binomial plot.

<img src="../Images/S6_Stock_Price_3_Step_BinomialModel.png" alt="Stock Price 3 Step BinomialModel"/>

At the 3rd timestep we have 4 states of the world corresponding to the values for the stock:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{3} \( %2B %2B %2B ) = u^{3}S_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{3} \( %2B %2B - ) = u^{2}dS_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{3} \( %2B - - ) = ud^{2}S_{0}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S_{3} \( - - - ) = d^{3}S_{0}">
</p>

Correspondingly, a derivative expiring at the last time step can be specified at the last time step by its payoff:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{3} \( %2B %2B %2B )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{3} \( %2B %2B - )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{3} \( %2B - - )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{3} \( - - - )">
</p>

With the same procedure as in the 2 step case the fair value of the derivative at time 0, <img src="https://render.githubusercontent.com/render/math?math=D_{0}">, can be computed:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \tilde{p}^{3} \frac{D_{3} \( %2B %2B %2B) }{ \( 1 %2B r )^{3}} %2B 3 \tilde{p}^{2} \tilde{q} \frac{D_{3} \( %2B %2B -) }{ \( 1 %2B r )^{3}} %2B 3 \tilde{p} \tilde{q}^{2} \frac{D_{3} \( %2B - -) }{ \( 1 %2B r )^{3}} %2B \tilde{q}^{3} \frac{D_{3} \( - - - ) }{ \( 1 %2B r )^{3}}"><br>
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = \text{bin} \( 3 %3B 3, \tilde{p} ) \frac{D_{3} \( %2B %2B %2B) }{ \( 1 %2B r )^{3}} %2B \text{bin} \( 2 %3B 3, \tilde{p} ) \frac{D_{3} \( %2B %2B -) }{ \( 1 %2B r )^{3}} %2B \text{bin} \( 1 %3B 3, \tilde{p} ) \frac{D_{3} \( %2B - -) }{ \( 1 %2B r )^{3}} %2B \text{bin} \( 0 %3B 3, \tilde{p} ) \frac{D_{3} \( - - - ) }{ \( 1 %2B r )^{3}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\text{bin} \( %3B 3, \tilde{p} ) } \[ \frac{D_{3}}{ \( 1 %2B r )^{3}} ]">
</p>

We may continue extending the number of steps. The basic results extend in the natural way. The notation we have used so far is unwieldy for a large number of steps, and so introduce a modified notation now. 

We preserve our notation using the "up" and "down" factors _u_ and _d_. Thus, we continue to model the forward evolution of the stock price one time step by multiplying by either _u_ or _d_. We now use the below notation for the underlying asset price.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{k} \( j ) = u^{j} d^{k-j} S_{0} \: \: \text{for} \: \: j = 0 \cdots k">
</p>

<img src="../Images/S6_Stock_Price_3_Step_BinomialModel_new.png" alt="New Notation for Asset Price"/>

The index _j_ equals the number of up jumps the stock has taken up to time _k_. The order the up and down jumps were taken in is immaterual. There are many paths that could be followed for the stock price to reach 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{k} = S_{k} \( j )">
</p>

As long as the total number up jumps is _j_, this same level will be realized at time _k_. A contingent derivative asset can be specified in this notation as well, with

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{k} \( j )">
</p>

the value the derivative takes in the state of the world at time _k_ when <img src="https://render.githubusercontent.com/render/math?math=S_{k} = S_{k} \( j )">.

The payoff of the derivative is then specified by its values at the endtime _n_:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{n} \( j ) \: \: \text{for} \:  \: j = 0, 1, \cdots n">
</p>

Following the same essential chain of logic that established the time 0 price of the derivative for the 1, 2 and 3 step cases, we can show

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{0} = E^{\text{bin} \( %3B n, \tilde{p} )} \[ \frac{D_{n}}{ \( 1 %3B r)^{n}} ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \sum_{j=0}^{n} \frac{n !}{j! \( n - j )!} \tilde{p}^{j} \tilde{q}^{ \( n - j )} \frac{D_{n} \( j )}{ \( 1 %2B r )^{n}}">
</p>
