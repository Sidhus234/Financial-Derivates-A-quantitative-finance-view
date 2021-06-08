
- Forward prices may be deduced from two arbitrage strategies:
  - The cash and carry arbitrage
  - The reverse cash and carry arbitrage

- This is a more direct arguement that the application of the Law of One Price and replication as in the previous lecture.
- The formula for the forward price we derived is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = e^{rT}S(0)">
</p>
  where _S(t)_ is the underlying spot price, _r_ is the risk free rate and _T_ is the expiration date of the forward contract.
  
- Now we will derive the forward price from a direct arbitrage arguement.
- We will show that if below holds, then we can construct an arbitrage (and thus this is impossible).

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \gt e^{rT}S(0)">
</p>

- Similarly, we will show that if below holds, the this as well leads to an arbitrage.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \lt e^{rT}S(0)">
</p>

- The only possibility is that the forward price is as given above.

- Step 1: Suppose

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \gt e^{rT}S(0)">
</p>

- Then construct an arbitrage portfolio as follows:
  - Take the short position (seller's position) in the forward contract, which costs nothing.
  - Borrow S(0) (in cash) at the risk free rate.
  - Purchase the underlying witht he proceeds.
  - Our Portfolio now consists of:
    - the short forward position
    - the underlying asset
    - a debt of S(0)<img src="https://render.githubusercontent.com/render/math?math=e^{rt}">  at time _t_

  - Now we hold this portfolio untim time _T_.
  - At time _T_, under the obligations of the forward contract, we provide the underlying to the long position holder, receiving the contract price <img src="https://render.githubusercontent.com/render/math?math=K_T">.
  - With these proceeds, retire the debt, currently worth <img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT}"> netting a profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T - e^{rT}S(0) \gt 0">
</p>

  - It costs nothing to enter this portfolio and it yields a certain and positive profit. So it is an arbitrage. This strategy is called a __cash and carry arbitrage.__

- Step 2: Suppose

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \lt e^{rT}S(0)">
</p>

- Then construct an arbitrage portfolio as follows:
  - Take the long position (buyer's position) in the forward contract.
  - Short the underlying yielding a cash payment of _S(0)._
  - Invest the cash at the risk free rate.
  - Our Portfolio now consists of:
    - the LONG forward position
    - the short position in underlying asset
    - a cash holding of S(0)<img src="https://render.githubusercontent.com/render/math?math=e^{rt}">  at time _t_

  - Now we hold this portfolio untim time _T_.
  - At time _T_, our cash holding is worth <img src="https://render.githubusercontent.com/render/math?math=S(0) e^{rT} \gt K_T">. Thus we may liquidate a cash value of <img src="https://render.githubusercontent.com/render/math?math=K_T">. Under the obligations of the forward contract, we pay this to the short position holder, who provides us with the underlying in return.
  -  We may now exit the short position in the underlying. We have retained a cash holding of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT} - K_T \gt 0 ">
</p>

  - It costs nothing to enter this portfolio and it yields a certain and positive profit. So it is an arbitrage. This strategy is called a __reverse cash and carry arbitrage.__

### Summary:
- What we have shown so far is that if either of below holds, then we can construct an arbitrage.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \gt e^{rT}S(0) ">
</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \lt e^{rT}S(0) ">
</p>

- Since by assumption, arbitrages cannot exist, the only possibility left is below, which verifies our forward pricing formula.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = e^{rT}S(0) ">
</p>

- The notion of the __cost of carry__ is the cost to hold an asset. In this case, the only cost to hold the asset is the finance charge, so Cost of Carry = _r_
- The cost of carry generally includes costs such as financing charges, storage costs, transportation costs, and other holding costs, net of any income the holder of the asset receives such as dividends or convenience yields.
- We will see more general examples of the cost of carry appearing in pricing formulas for more general assets such as income bearing assets and commodities.
- The resverse cash and carry arbitrage used in step 2 to rule out below is the exact reverse of the cash and carry arguement. We short the underlying, and receive the carry charge as income instead of paying it.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \lt e^{rT}S(0) ">
</p>


## Zero Coupon Bond Example
Imagine you are a bond trader looking at forward contracts on zero coupon bonds maturing in 1 year. Suppose the risk free rate is 3.5%. Suppose one particular bond you are looking at is currently priced at $925 on the market. What is the forward price for a 6 month forward contract on this bond? Suppose a dealer offers you a forward price of $950. How could you take advantage of this? Suppose another dealer offers a forward price of $935. How could you take advantage of this?
Now suppose you enter a short position in the contract using the computed forward price. Suppose at contract expiration in 6 months the bond is trading for $960. What are the cashflows that occur and what is the payoff to your position? What if the price at expiration is $930?

- We have a continously compounded risk free rate _r_ =3.5% = 0.035
- Value today (t=0) of the underlying: _S(0) = $925_
- Contract expiration date will be in 6 months: _T=6 months = 0.5 year_
- Forward price 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K = e^{rT}S(0) = E^{0.035/2}(925) = 941.33">
</p>

- First dealer offered forward price $950 > $941.33 = K
- Too high : want to sell.
- To realize a riskless prift:
  - Enter the short (seller) position in the forward.
  - Borrow $925 at the risk free rate.
  - Buy the bond
  - We now have a portfolio consisting of:
    - the short forward position
    - the bond
    - a debt valued at <img src="https://render.githubusercontent.com/render/math?math=e^{0.035t}(925)"> at time _t_

  - We hold these positions for 6 months, when the forward expires. At that time the debt is worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{0.035/2}(925) = 941.33">
</p>
  - We now fulfil ourobligations under the forward: sell the bond and receive the contracted forward price: $950
  - With this cash, retire the debt.
  - We clear a profit of:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=950 - 941.33 = 8.67">
</p>

  - This is an arbitrage (riskless) profit.

- Now consider the second dealer: we were offered a forward price of $935 < $941.33 = K
- To realize a riskless profit:
  - Enter the long (buyer) position in the forward.
  - Sell the bond at $925
  - Invest the cash proceeds at risk free interest rate.
  - We now have a portfolio of:
    - the long forward position
    - the short position on the bond
    - a cash investment valued at <img src="https://render.githubusercontent.com/render/math?math=e^{0.035t}(925)"> at time _t_

  - We hold this portfolio until the forward expires in 6 months. the cash invesment is now worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=925 e^{0.035/2} = 941.33">
</p>

  - We now liquidate the cash investment and fulfill the forward contract: purchase the bond for the contracted price of $935.
  - We can now close out the short position in the bond
  - We have cleared a profit of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=941.33 - 935 = 6.33">
</p>

  - This is a riskless arbitrage profit.

- Now suppose we enter the short position in the forward contract at the fair forward price of _K = $941.33_ that  we have calculated.
- Recall the payoff, at expiry, to the short is _K - S(T)_
- At contract expiration, the short receives the forward price (the _K_ term, and in return provides the asset (in this case the bond) represented by the -_S(T)_ term.
- If at expiration the bond is trading at _S(T)_ = $960 then the value of this payoff is $941.33 - $960 = -18.67 < 0
- The payoff is negative because we receive less than the asset worth.
- If at expiration the bond is trading at _S(T)_ = $930 then the value of this payoff is $941.33 - $930 = $11.33 > 0. The payoff is positive because we have been paid more than the bond is worth.
