<h1>Arbitrage Inequality #3</h1>

<h3>Call price greater than long forward position</h3>
We will prove arbitrage ineqaulity #3.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) \ge S \( t ) - e^{-r \( T - t )} K ">
</p>

We do this by assuming it is not true, and showing that this leads to an arbitrage. Suppose at time _t_,

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) < S \( t ) - e^{-r \( T - t )} K">
</p>

Rewrite this inequality as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) %2B e^{-r \( T - t )} K < S \( t )">
</p>

Take the following positions:
<ol>
  <li>A short position in the stock, yielding <i>S(t)</i> in cash. From the inequality this is sufficient to take positions:</li>
  <li>a long position on the call</li>
  <li><i>S(t) - C(t)</i> in cash invested at the risk free rate.</li>
</ol>

Rewrite the assumed inequality, which says the value of our cash investment at expiry exceeds the strike price.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K < e^{r \( T - t )} \( S \( t ) - C \( t ) )">
</p>

Thus, after holding until expiry, our position is:
<ol>
  <li>the long call position</li>
  <li>the short on the stock</li>
  <li>the cash investment worth</li>
  </ol>
  
  <p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t ) \( S \( t ) - C \( t ) )">
</p>

At the expiration date of the options, 2 events are possible: If _S(T) > K_: We exercise the call, spending _K_, receiving the stock. We close out the short position. We retain the profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t )} \( S \( t ) - C \( t ) ) - K > 0">
</p>

If _S(T) <= K_, we will let the call expire worthless. Purchase the stock from our cash investment. Close out the short position in the stock. We retain the profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t )} \( S \( t ) - C \( t ) ) - S \( T ) \ge e^{r \( T - t )} \( S \( t ) - C \( t ) ) - K">
</p>

In either case we clear the position, and still retain a positive and riskless profit. This is therefore an arbitrate portfolio. 

<h3>Summary</h3>
We have shown that if the inequality

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) < S \( t ) - e^{-r \( T - t )} K">
</p>

is ever observed, we can construct an arbitrage portfolio. THus this inequality is ruled out. So we must have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( t ) \ge S \( t ) - e^{-r \( T - t )} K">
</p>

which is the arbitrage inequality we set out to prove.
