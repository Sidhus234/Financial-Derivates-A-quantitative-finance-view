<h1>Arbitrage Inequality 1</h1>

<h3>Call price is less than underlying price</h3>
Here we will prove inequality #1 (ie _C(t) <= S(t) )

We do this by assuming that it is not true, and showing that it leads to an arbitrage. Support at time _t_ it holds _C(t) > S(t)_. We construct an arbitrage as follows:
<ol>
  <li>Sell or write the call, collecting cash <i>C(t)</i></li>
  <li>Buy the stock</li>
  <li>This yields a cash holding <i>C(t) - S(t) > 0</i></li>
  <li>Now invest this cash at the risk free rate and hold the position until the option expires.</li>
</ol>

At expiration, our portfolio consists of:
<ol>
  <li>a long posiiton on the stock,</li>
  <li>a short position on the call,</li>
  <li>a cash holding now worth</li>
</ol>

  <p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t )} \( C \( t ) - S \( t ) )">
</p>

Depending on the value of the stock at expiration, 2 events are possible. If _S(T) <= K_:

The call will not be exercised (it's out of the money). We retain our cash investment and the stock, realizing a profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r \( T - t )} \( C \( t ) - S \( t ) ) %2B S \( T ) > 0">
</p>

If _S(T) > K_:

The call will be exercised, we will sell the stock, and receiving a cash payment _K_. We now have a total cash holding of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K %2B e^{r \( T - t )} \( C \( t ) - S \( t ) ) > 0">
</p>

We have cleared all the positions and retained this as a profit. No matter what happens, we are certain to make a positive profit. This is therefore an arbitrage portfolio. We have shown that if the inequality _C(t) > S(t)_ is ever observed, we can construct an arbitrage. Thus this inequality is ruled out. So we must have _C(t) <= S(t)_ which is the arbitrage inequality we set out to prove.
