
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
