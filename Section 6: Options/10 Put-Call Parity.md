<h1>Put-Call Parity</h1>
Put-call parity is the relation 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) = S \( t ) - e^{-r \( T - t )}K">
</p>

Where _K_ is the common strike price of both the call and the put. The put-call parity relation follows from the Law of One Price and our observations about the payoff of the call, put and forward. We will work through the arbitrage arguement explicitly. Suppose

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) > S \( t ) - e^{-r \( T - t )}K">
</p>

Rewrite the inequality

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) %2B e^{-r \( T - t )}K >  P \( t ) %2B S \( t )">
</p>

Take the following positions:
<ol>
  <li>Short position on the call</li>
  <li>A debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-r \( T - t )}K">. This yields <img src="https://render.githubusercontent.com/render/math?math=C \( t ) %2B e^{-r \( T - t )}K"> in cash so, from the inequality, we may also take the positions</li>
  <li>Long position on the put.</li>
  <li>Long position on the stock.</li>
  </ol>

And retain a cash holding of 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) %2B e^{-r \( T - t )}K -  P \( t ) - S \( t ) > 0">
</p>

Invest this at the risk free rate and hold until expiry. At expiry, the value of the debt is _K_. 

If _S(T) <= K_ the call expires worthless, we exercise the put, receive _K_ for the stock, and retire the debt. 

If _S(T) > K_ the put expires worthless, the call will be exercised, so we sell the stock and receive _K_ in cash, with which we can retire the debt. In either case all positions are cleared and we book the profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-r \( T - t ) } \( C \( t ) %2B e^{-r \( T - t )}K -  P \( t ) - S \( t ) ) > 0">
</p>


Now suppose 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) < S \( t ) - e^{-r \( T - t )}K">
</p>

Rewrite the inequality

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) %2B e^{-r \( T - t )}K <  P \( t ) %2B S \( t )">
</p>

Take the following positions:
<ol>
  <li>Short position on the put</li>
  <li>Short position on the stock. This yields <i>P(t) + S(t)</i> in cash with which we can also take the positions</li>
  <li>Long position on the call</li>
  <li>A cash investment <i>P(t) + S(t) - C(t) > exp(-r(T-t)) K</i></li>
</ol>

Now hold these positions until expiry. Rewrite the inequality

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t )} \( P \( t ) %2B S \( t ) - C \( t ) ) > K">
</p>

The LHS is the value of our cash investment. If _S(T) <= K_ the call expires worthless, the put will be exercised, so we pay _K_ from the cash investment and receive the stock in return.Then, clear the short position on the stock. If _S(T) > K_ the put expires worthless, we exercise the call, spending _K_ from our cash investment, receiving the stock in return, with which we close the short position in the stock. In either case, we have earned the riskless profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t ) } \( P \( t ) %2B S \( t ) - C \( t )) - K > 0">
</p>

This is a riskless profit. Hence, our portfolio is an arbitrage. We have shown that each of the inequalities

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) > S \( t ) - e^{-r \( T - t )}K"><br>
  <img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) < S \( t ) - e^{-r \( T - t )}K">
</p>

leads to an arbitrage. This rules both inequalities out, so the only possibility is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) - P \( t ) = S \( t ) - e^{-r \( T - t )}K">
</p>
