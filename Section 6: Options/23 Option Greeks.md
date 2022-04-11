<h1>Option Greeks</h1>
The "greeks" for an option (or more generally for any asset or portfolio) are a collection of calculas derivatives of the option price with respect to a variety of risk factors. As such, they are measures of the sensitivity of the option value to the corresponding risk factor. They are of critical importance for the (nonlinear) hedging and risk management of option positions. For definiteness, we will focus on the greeks for a call option, but they are defined in the same basic way for the puts and other derivatives and portfolios.

Let <img src="https://render.githubusercontent.com/render/math?math=C = C \( S, t %3B K, T, \sigma, r)"> be the price of a call (it does not need to be the Black-Scholes price). The most important greeks are:

<li>The <b>delta</b> of the call is</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta = \frac{\partial C}{\partial S}">
</p>

<li>The <b>gamma</b> of the call is</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Gamma = \frac{\partial^{2} C}{\partial S^{2}}">
</p>

<li>The <b>vega</b> of the call is</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{V} = \frac{\partial C}{\partial \sigma}">
</p>

It is a standard practice to use the Black-Scholes theory to approximate the Greeks. One reason for this is that the Black-Scholes theory is one of the few models that yield analyticsl formulae for the greeks. Probably of most importance is that Blakc-Schole sis the option pricing model with the longest history, the simplest, and the one practitioners are comfortable with - inspite of its recognized flaws. In recent years it is becoming more common for traders to use newer models viewed as more accurate, such as stochastic volatility models.

<h3>Black-Scholes Greeks</h3>
(notation from the general statement of the Black-Scholes formula):

<li>The Black-Scholes delta:</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta = N \( d _{%2B} )">
</p>

<li>The Black-Scholes gamma:</li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Gamma = \frac{N^{'} \( d _{%2B} )}{S \( t ) \sigma \sqrt{T - t}}">
</p>

<li>The Black-Scholes vega: </li>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{V} = S \( t ) \sqrt{T - t} N^{'} \( d _{%2B} )">
</p>

The greeks provide quanititative measures of the exposures an option positions bears. As such they provide an option position bears. As such they provide a precise and concrete picture of the risks in an option or option portfolio. They are thus of critical importance for trading, hedging, and risk managing option positions. From an investor's point of view, the exposures of a position are of primary importance, at least as important as the assets used to realize the exposures. Thus the greeks are central to investing in and managing portfolios of options, derivatives, cash products, and other assets. 
