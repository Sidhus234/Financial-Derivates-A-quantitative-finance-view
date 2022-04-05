<h1>Extensions and Applications of Option Bounds</h1>
The lower bounds for call and put prices considered in the previous notes can be improved by adding one additional consideration. The value of an option can never be negative, because once held, the worst possible outcome is that it expires worthless. You cannot lose money on an option. If an option ever had a negative value (which means you would profit just for taking a position in an option) there would be an immediate arbitrage.

It follows that, in addition to the lower bounds considered in the previous lectures, we also have the lower bounds

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ) , t ) \ge 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P \( S \( t ) , t ) \ge 0"><br>
</p>

We may combine our lower bound for each product together. For instance, for calls, since we have both

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ) , t ) \ge S \( t ) - e^{-r \( T - t ) } K"><br>
<img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ) , t ) \ge 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\text{combining above two}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ) , t ) \ge \max \( 0 , S \( t ) - e^{-r \( T - t ) } K )"><br>
  </p>
  
Similarly, we may deduce a similar combined lower bound for puts. Putting this together, we have the following improved set of upper and lower bounds for calls and puts.

<h3>Upper Bound for Calls</h3>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ), t ) \le S \( t )">
</p>

<h3>Upper Bound for Puts</h3>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P \( S \( t ), t ) \le e^{-r \( T - t )} K">
</p>

<h3>Lower Bound for Calls</h3>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( S \( t ), t ) \ge \max \( 0, S \( t ) - e^{-r \( T - t )} K )">
</p>

<h3>Lower Bound for Puts</h3>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P \( S \( t ), t ) \ge \max \( 0, e^{-r \( T - t )} K - S \( t )">
</p>

<h3>Example</h3>
Suppose there is a 1 year call on a stock currently trading at $64. Suppose the stike price is $45, and that the risk free rate is 3%. If the call premium is currently $75, is there an arbitrage opportunity, and of so how would you exploit it. 

We would first check the data we have been given against the arbitrate bounds presented in the previous slide. When we do this, we see that the upper bound for calls is violated. We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) = 75 \( < 65 = S \( t ) )">
</p>

violating the upper bound for calls. The call price is too expensive compared to the stock price, so we want to sell ( ie short) a call option, and use the proceeds to buy the stock. We will be left with the diffence _C(t) - S(t) = 75-65 = $10_ in cash. We can invest this cash at the risk fre rate for the next year, and hold the other positions for this time. 1 year later, the call will expire either in or out of the money. If it is in the money, it will be exercised, and we will have to sell it for the strik price of $45. If it is out of the money, it will not be exercised, and we will simply retain the stock. In either case, we will retain the cash investment, nor worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{0.03 \( 1 )} \( 10 ) = 10.30">
</p>

In addition we have either the strike price of $45 from selling the stock under the option, or simply the stock. Adding all this together we have total holdings worth at least $10.30, and this is a riskless profit.
