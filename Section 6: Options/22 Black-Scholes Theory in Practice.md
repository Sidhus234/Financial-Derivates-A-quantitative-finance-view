<h1>The Black-Scholes Theory in Practice</h1>

If the underlying asset price evolves under a log-normal distribution with drift <img src="https://render.githubusercontent.com/render/math?math=\mu \: \: \text{and volatility} \: \: \sigma"> then the fair price of a call is:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C \( S, t %3B K, T, \sigma, r ) = SN \( d_{%2B} ) - K e^{ - r \( T - t )} N \( d_{-} )">
</p>

where

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d_{\pm} = \frac{1}{\sigma \sqrt{ \( T - t )}} \[ \log \( \frac{S}{K} ) %2B \( r \pm \frac{\sigma^2}{2} ) \( T - t)]">
</p>

and N(x) is the normal cumulative distribution function:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=N \( x ) = \frac{1}{\sqrt{2 \pi}} \int_{- \infinity}^{x} e^{-z^{2}/2} dz">
</p>

Here, we are evaluating the call price at time _t_ and:
<ol>
  <li>S is the price of the underlying (at time t).</li>
  <li>K is the strike price.</li>
  <li>T is the expiration date.</li>
  <li><img src="https://render.githubusercontent.com/render/math?math=\sigma"> is the volatility (ie standard deviation) of the log-normal process of the underlying.</li>
  <li>r is the risk free rate.</li>
</ol>

Note we have adapted the formula from last lecture for a general time _t_ during the life of the option.

As a basic application of put-call parity, note that having derived a formula for pricing a call, we do not need to derive a new "Black-Scholes" formula for the put premium. From put-call parity we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P \( S \( t ), t)= C \( S \( t ), t) - S %2B e^{-r \( T - t )} K"><br>
  <img src="https://render.githubusercontent.com/render/math?math== e^{-r \( T - t )} K N \( - d_{-} ) - S \( t ) N \( - d_{%2B} )">
</p>

It is not hard to derive the put price directly from first principles. 

In the last lecture we discussed the many assumptions required to derive the Black-Scholes option priceing formula. We saw that many of these assumptions are at odds with how real markets work. Yet the Black-Scholes formula is used universally in option trading and finance by traders, quants, risk managers, and portfolio managers. How can that be if we know the formula can at best produce approximate option prices?

In the hands of an experienced trader, who understands, the deficiencies of the model and thus knows how to adjust or tweak the formula, the black-Scholes theoru can be a useful tool. In fact it has numerous uses besides pricing.In spite of its flaws pricing is still one of the main used of the Black-Scholes theory. An experienced practitioner understands that the Black-Scholes formula is not the final word on an option's correct price. But the theory get's enough right to still be a useful prcing tool. An experienced pricer can start from the Black-Scholes price and make adjustments to correct it. For vanilla calls and puts , though, which ar egenerally fairly liquid exchange traded instruments, the actual prices are set on markets, the outcome of supply and demand forces. For these most important instruments, Black-Scholes is used more as an interpretive mechanism.

For these instruments, the primary application of the Black-Scholes formula is to calculate the implied volatility: the value of the volatility parameter  <img src="https://render.githubusercontent.com/render/math?math=\sigma"> such that the Black-Scholes formula yields the observed market price. The implied volatility is for many purposes more useful data than the price itself. Outside of pricing, there are major applications of the Black-Scholes theory to hedging and risk managing option positions. We will see these while discussing option greeks (sensitivities) and dynamic hedging.
