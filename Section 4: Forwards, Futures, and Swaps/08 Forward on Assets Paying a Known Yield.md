# Forward on Assets Paying a Known Dividend Yield
Suppose the underlying asset with price _S(t)_, a known dividend yield _y_, and all dividends are reinvested in the asset. From our earlier study of the dividend yields we know that an initial allocation of <img src="https://render.githubusercontent.com/render/math?math=e^{-yT}"> implies a holding at time _t_ of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-yT}e^{yt}S(t) = e^{-y(T-t)}S(t)">
</p>

Thus, at time _T_ the investment is worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-(T-T)}S(T) = S(T)">
</p>

implying a total investment (below) replicates exactly the asset value _S(T)_ at time _T_.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-yT}S(0)">
</p>

We will now derive the forward price on an underlying asset producing a known income yield y. The forward price in this case is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = e^{(r-y)T}S(0)">
</p>

- We will derive this formula using the replicating portfolio method. In fact, we already know what the rpelicating assets are. Recall the forward payoff for the long position:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(T) - K_T">
</p>

- To replicate the first term _S(T)_ we have tjust deduced that we can do so with an allocation of <img src="https://render.githubusercontent.com/render/math?math=e^{-yT}"> in the underlying asset, which will be one component of a replicating portfolio.
- The cash payment <img src="https://render.githubusercontent.com/render/math?math=K_T"> can be replicated, as always, by a debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T"> borrowed at the risk free rate. Thus at time 0 our portfolio consists of:
  - an allocation of <img src="https://render.githubusercontent.com/render/math?math=e^{-yT}"> to the underlying
  - a debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T">

- At time _t_ these components are worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-y(T-t)}S(t) - e^{rt}e^{-rT}K_T">
</p>

- At time _t_ our portfolio is worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = e^{-y(T-t)}S(t) - e^{-r(T-t)}K_T">
</p>

- Checking the value at expiration, we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(T) = e^{-y(T-T)}S(T) - e^{-r(T-T)}K_T = S(T) -K_T">
</p>

  verifying that this portfolio replicates the forward payoff. By the Law of One Price it follows that _V(t)_ is the value of the forward contract at any time _t_ before expiration.
  
  <p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(0) = e^{-yT}S(0) - e^{-rT}K_T">
</p>

- Assuming now that the contract is originated at time _t_ =0 we set _V(0) = 0_ to determine the forward price:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=0 = e^{-yT}S(0) - e^{-rT}K_T"><br>
  <img src="https://render.githubusercontent.com/render/math?math=e^{-yT}S(0) = e^{-rT}K_T"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T = e^{(r-y)T}S(0)">
</p>

  verifying our stated expression for the forward price. We have used a replication arguement to derive the forward price <img src="https://render.githubusercontent.com/render/math?math=K_T = e^{(r-y)T}S(0)"> for an asset paying a known dividend yield _y_.
- This formula could also have been derived using a cash and carry arbitrage, as we have done for other examples. For the case of an asset bearing a known yield income _y_, we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=cost of carry = r- y">
</p>

- That is the cost of carry is the finance charge net the income paid by the asset.
- If the underlying asset were a commodity, one modelling approach would decompose the yiedl as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y = c -s">
</p>
  where _c_ is a convenience yield and _s_ is the rate of storage cost.
- For a commodity underlying then,

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Cost of Carry = r %2B s - c">
</p>

- and the forward price would be

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = e^{r %2B s - c)T}S(0)">
</p>

## Summary:
- Known Income: Forward Price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_t = (S(0) - I)e^{rT}">
</p>

- Known Income: Contract Value

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - I(t) -e^{-r(T-t)}K_T">
</p>

- Known Income: Forward Price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = e^{(r - y)T}S(0)">
</p>

- Known Income: Contract Value

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) =e^{-y(T-t)}S(t) - e^{-r(T-t)}K_T">
</p>

# Example Dividend Paying Stocks
Lauren owns unvested share in her former employer's company that will vest in 9 months. She plans to liquidate these shares when they vest but wants to protect against any drop in share price before vesting. Suppose the current stock price is $247/share. Suppose the stock pays dividend of $5 per share in 2, 5, and 8 months. Assume the risk free rate for all maturities is 1.5%. Lauren enters a short forward position on a 9 month contract on the stock. What is the forward price? Suppose in 3 months the stock price is $220/share. What is the value per share of Lauren's forward position? What if it is $270 in 3 months?

- Denote the share price at time _t_ by _S(t)_ so in particular _S(0) = $247_.
- Expiration is at _T = 9_ months _=0.75 years._
- The risk free rate is _r = 1.5% = 0.015_.
- To account for the 3 dividend payments the stock will pay during the life of the forward contracct, we need the _PV_ of the payment stream at _t = 0_.
- The dividends paid are $5 in 2,5 and 8 months so the PV is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV =e^{-0.015 \frac{2}{12}}5 %2B e^{-0.015 \frac{5}{12}}5 %2B e^{-0.015 \frac{8}{12}}5 = 14.91">
</p>

- We have all the elements needed to compute the forward price:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_t = (S(0) - I)e^{rT}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_t = (247 - 14.91)e^{0.015 (0.75)} = 234.72">
</p>

- The value of the short forward position for any time _t_ during the life of the contract is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V(t) = e^{-r(T-t)}K_T - S(t) %2B I(t)">
</p>

- _I(t)_ = _PV_ at time _t_ of the dividend payments remaining at time _t_ for the life of the contract.
- For _t_ = 3 months, there are 2 dividend payments left before the forward expires, at 5 months and 8 months from origination. The PV of these payments at _t = 3_ months is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I(0.25) =e^{-0.015 \frac{2}{12}}5 %2B e^{-0.015 \frac{5}{12}}5 = 9.96">
</p>

- Consider the assumption that the underlying share price in 3 months is $220. From the data we have computed, the value of Lauren's short position is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V(0.25) = e^{-r(T-t)}K_T - S(0.25) %2B I(0.25)"><br> 
  <img src="https://render.githubusercontent.com/render/math?math=-V(0.25) = e^{-0.015(0.75 - 0.25)}234.72 - 220 %2B 9.96 = 22.93"><br> 
</p>

  The positive value indicates that the short position has profited after 3 months. 
  
  - Consider the assumption that the underlying share price in 3 months is $270. From the data we have computed, the value of Lauren's short position is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V(0.25) = e^{-r(T-t)}K_T - S(0.25) %2B I(0.25)"><br> 
  <img src="https://render.githubusercontent.com/render/math?math=-V(0.25) = e^{-0.015(0.75 - 0.25)}234.72 - 270 %2B 9.96 = -27.07"><br> 
</p>

  The negative value indicates that the short position has lost money after 3 months.
