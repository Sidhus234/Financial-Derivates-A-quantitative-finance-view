<h1>Dynamic Hedging and Delta Neutral Trading</h1>
The hedging procedures we have considered in previous modules were examples of static hedging. They involved taking positions in linear instruments, forward, futures and swaps, with exposures that offset existing exposures in our portfolio, and holding the position over some time period, possibly over our entire investment horizon. This was effective because the exposures in our portfolio to start with were static in time. This will not work with options, which have nonlinear exposures which change as markets variables change.

The exposure of an option to the underlying asset is expressed most directly by the delta:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta = \frac{\partial C}{\partial S} = N \( d_{%2B} )">
</p>

where we have used the Black-Scholes delta. The delta is a function of the stock price and thus changes in time as the stock price changes. In order to control the risk and exposures of option positions and portfolios, the hedging positions must be updated as the delta changes. The standard way to control the direc exposure to the underlying is to maintain a delta neutral portfolio consisting of the option and some allocation to the stock. 

We consider a portfolio consisting of a call option and some allocation to the underlying stock with value:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V \( t ) = C \( S \( t ), t ) - \delta S \( t )">
</p>

We say the portfolio is delta neutral if

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial V}{\partial S} = 0">
</p>

In other words, the delta of the portfolio is 0. This condition determines the allocation to the stocj:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial C}{\partial S} - \delta = 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\Rightarrow \delta = \frac{\partial C}{\partial S} = \Delta"><br>
</p>

In other words, to maintain a delta neutral portfolio, our allocation to the stock should be minus the delta of the option. Put differently: to maintain a delta neutral portfolio, for every call option we should short exactly <img src="https://render.githubusercontent.com/render/math?math=\Delta"> shares of the stock. 

Note: the Black-Scholes delta satisfies:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=0 \le \Delta \le 1">
</p>

Thus maintaining the delta neutrality of a call position will always involve allocating a fraction of the shares underlying the call positions to the short share position. 

<h3>Example</h3>
Suppose we have a 6 month call on a stock currently trading at $60 with a volatility of 20%. Suppose the strike price of the call is $50 and the risk free rate is 5%. What is the delta of the call? Suppose we have a call position on 200 shares of this stock. What position in the underlying stock must we take to have a delta neutral position? What is the P&L of this position 1 month later if the stock now has the same volatility and a price of $70? $50?

We have:
<li>spot price = S= $60</li>
<li>strike price = K = $50</li>
<li>time until expiration = T = 6 months = 0.5</li>
<li>volatility = 20% = 0.2</li>
<li>interest rate = r= 5% = 0.05</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d_{%2B} = \frac{1}{\sigma \sqrt{T}} \[ \log \( \frac{S}{K} ) %2B \( r %2B \frac{\sigma^{2}}{2} ) T ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \frac{1}{0.20 sqrt{6/12}} \[ \log \( \frac{60}{50} ) %2B \( 0.05 %2B \frac{0.2^{2}}{2} ) \( \frac{6}{12} ) ] = 1.536695">
</p>

The Black-Scholes delta is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta = N \(d_{%2B}) = n \( 1.536695 ) = 0.9378">
</p>

To hedge our option position, the formula for a delta neutral portfolio says we should short

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta x # \text{optioned shares}">
</p>

with <img src="https://render.githubusercontent.com/render/math?math=\Delta}"> = 93.78% the delta neutral position then consists of the call option on 200 shares and a short position in 0.9378 * 200 = 188 shares.

To compare this position to the proposed circumstances 1 month later, we must value the option position. For the initial option value we need <img src="https://render.githubusercontent.com/render/math?math=d_{-} \text{ and } d_{%2B}">:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d_{-} =\frac{1}{\sigma \sqrt{T}} \[ \log \( \frac{S}{K} ) %2B \( r - \frac{\sigma^{2}}{2} ) T ]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \frac{1}{0.2 \sqrt{6/12}} \[ \log \( \frac{60}{50} ) %2B \( 0.05 - \frac{0.2^{2}}{2} ) \( \frac{6}{12} ) ] = 1.395274">
</p>

Substituting into the Black-Scholes formula then gives the call price (for 1 share):

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C = SN \( d_{%2B} ) - K e^{-r \( T - t )}N \(d_{-} )"><br>
  <img src="https://render.githubusercontent.com/render/math?math=C = 60N \( 1.536695 ) - 50 e^{-0.05 \( 0.5 )}N \(1.395274 ) = 11.48">
</p>

We now compare the situation 1 month later under the 2 proposed scenarios. 

If the stock is now $70, then our short position has lost $10 per share, or a total of $1880. For the option, we must revalue, using Black-Scholes. We need

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=d_{%2B} = \frac{1}{0.20 sqrt{5/12}} \[ \log \( \frac{70}{50} ) %2B \( 0.05 %2B \frac{0.2^{2}}{2} ) \( \frac{5}{12} ) ] = 2.832227">
</p>

and

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=d_{-}= \frac{1}{0.2 \sqrt{5/12}} \[ \log \( \frac{70}{50} ) %2B \( 0.05 - \frac{0.2^{2}}{2} ) \( \frac{5}{12} ) ] = 2.703127">
</p>

The call price then is

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=C = 70N \( 2.832227 ) - 50 e^{-0.05 \( 5/12 )}N \( 2.703127 ) = 21.04">
</p>

The total P&L on the trade is then 200(21.04 - 11.48) - 1880 = $32.

For the other scenario, a stock price of $50, the short stock position has now gained by $1880.  For the option, we must revalue, using Black-Scholes. We need


<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=d_{%2B} = \frac{1}{0.20 sqrt{5/12}} \[ \log \( \frac{50}{50} ) %2B \( 0.05 %2B \frac{0.2^{2}}{2} ) \( \frac{5}{12} ) ] = 0.225924">
</p>

and

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=d_{-}= \frac{1}{0.2 \sqrt{5/12}} \[ \log \( \frac{50}{50} ) %2B \( 0.05 - \frac{0.2^{2}}{2} ) \( \frac{5}{12} ) ] = 0.09682458">
</p>

The call price then is

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=C = 50N \( 0.225924) - 50 e^{-0.05 \( 5/12 )}N \( 0.09682458 ) = 3.09">
</p>

The total P&L on the trade is then 200(3.09 - 11.48) + 1880 = $202. The delta hedge has protected us from loss whether the stock price moves up or down.
