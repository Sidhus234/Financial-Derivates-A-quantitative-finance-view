# Law of One Price:
- Let A and B be two assets, with prices <img src="https://render.githubusercontent.com/render/math?math=P_A(t)\:\:\: and \:\:\:P_B(t)"> at time _t_. 
- Suppose the probability <img src="https://render.githubusercontent.com/render/math?math=Prob(P_A(T) = P_B(T)) = 1"> for some time _T > 0_.
- In that case one of two things have to be true:
  - Either <img src="https://render.githubusercontent.com/render/math?math=P_A(0) = P_B(0)"> or;
  - There is an arbitrage

## Justification: (Proof - Law of One Price)
- Suppose <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \ne P_B(0)">
- __NOTE__ <img src="https://render.githubusercontent.com/render/math?math=P_A(0)\:\:and\:\:P_B(0)"> are not random, and are known deterministic prices at time _t = 0._
- This measn <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \gt P_B(0)\:\: or \:\: P_B(0) \gt \P_A(0)."> Suppose <img src="https://render.githubusercontent.com/render/math?math=P_A(0)\gtP_B(0)">
- To construct an arbitrage:
  - Short position in _A_. Borrowed _A_ and immediately sold it on market.
  - Long position in _B_. Buy it from market.

- This implies following cash flows:
  - Receive <img src="https://render.githubusercontent.com/render/math?math=P_A(0)">
  - Spent <img src="https://render.githubusercontent.com/render/math?math=P_B(0)">
  - Left with <img src="https://render.githubusercontent.com/render/math?math=P_A(0) - P_B(0) \gt 0"> (as by assumption <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \gt P_B(0)">. This is invested at risk free rate for time _T_.

- Portfolio with following components:
  - 1. Short position in asset _A_ (with obligation to return to its rightful owner)
  - 2. Long position in asset _B_ (own _B_)
  - 3. Net cash invested at risk free rate <img src="https://render.githubusercontent.com/render/math?math=P_A(0) - P_B(0)"> for time _T_.

__NOTE:__ No cash was spent to build this portfolio.

- At time T to close out the position:
  - 1. Buy  _A_ at <img src="https://render.githubusercontent.com/render/math?math=P_A(T)"> and return to its rightful owner
  - 2. Sell _B_ at <img src="https://render.githubusercontent.com/render/math?math=P_B(T)">
  - Since cash from selling _B_ is used to buy _A_ as (<img src="https://render.githubusercontent.com/render/math?math=P_A(T) = P_B(T)">
  - 3. The net cash investment at risk free interest rate for time period _T_. This is riskless profit, and hence the portfolio was an arbitrage.
  - 4. The profit from the portfolio (Certain positive profit). This is an arbitrage.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(P_A(0) - P_B(0)) e^{rT} \gt 0">
</p>

## Extensions to Law of One price:
- An interesting extension of the Law as we have stated it:
  - If two securities, with certainity, pay the exact same cash flows then they should have the same price at any time during their lives.
  - This is a corollary to our first version of the Law of One Price.

- Another variant:
  - Of _A_ and _B_ are assets with prices <img src="https://render.githubusercontent.com/render/math?math=P_A(t)\:\:and\:\:P_B(t)"> and if at some time <img src="https://render.githubusercontent.com/render/math?math=T\gt 0"> we can say

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(T) \ge P_B(T)">
</p>

<p align="center">with probability 1, then we must have</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(t) \ge P_B(t)"> for any t < T
</p>
  
  - This can be proved with the exact same arguement that was used for the original version of the Law of One Price.
   
## Replication Arguements: 
The primary way the Law of One Price is applied is through replication arguements. 
 - Suppose _A_ is an asset we would like to price at some time _t_ (possibly right now, _t = 0_)
 - Denote the price of _A_ by <img src="https://render.githubusercontent.com/render/math?math=P_A(t)"> at any time _t_.
 - Suppose there is a portfolio we can construct, with value _V(t)_ that we are able to value, at least at some time _t_ when we want to know the price of <img src="https://render.githubusercontent.com/render/math?math=P_A(t)">.
 - Suppose we knoe that for some time _T > t_,
  
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob(V(T) = P_A(T)) = 1">
</p>

- Then, from law of One Price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(t) = V(t)">
</p>


## Law of One Price Examples:
We will look at some of our arbitrage examples from the point of view of the Law of One Price

### Example 1:
Consider the 3 stock example for arbitrage.
- Consider the portfolio consisting of 1 share of A and 2 shares of B as one asset. Call this asset 1 and denote it's value at time _t_ by <img src="https://render.githubusercontent.com/render/math?math=V_1(t):">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_1(t) = P_A(t) %2B P_B(t)">
</p>

- And asset 2 will be simply one share of stock C, with value denoted by <img src="https://render.githubusercontent.com/render/math?math=V_2(t):">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_2(t) = P_C(t)">
</p>

- Then our finding from the previous analysis of this problem was that at time _t = 1_ with probability 1

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_1(1) = V_2(1)">
</p>

- What we can therefore conclude from the Law of One Price is that our assets are wither equal in value at time 0, or there is an arbitrage.
- And this was exactly what we found in our previous study of this problem.
- We found, from our given data, that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_1(0) = 65 \lt 80 = V_2(0)">
</p>

- and from these facts, we constructed an explicit arbitrage portfolio.

### Example 2:
Now consider the final arbitrage example involving a bond. Can we use the Law of One Price to solve this problem?
- Recall that our final conclusion was that the bond, trading at par, was mispriced.
- We could have reached this conclusion as an application of the cash flow version of the Law of One Price
- The bond makes 3 coupon payments of %600 as well as a final face value payment of $10,000.
- Thus the bond is equivalent to a series of 3 cash flows, of $600, $600, and $10,600 in 1, 2, and 3 years respectively.
- The bond as an asset is nothing more thnt the right to receive the series of cash flows consisting of payments of $600 in 1st year, $600 in 2nd years, and $10600 in 3 years. Can we construct a portfolio that replicates this?

  - Such a portfolio is implicit in the way we treated the problem before.
  - Recall we detected the arbitrage by taking 3 loans, one for each cash flow made by the bond.
  - Equivalently, we shorted 3 zero coupon bonds.
  - This suggests a replicating portfolio consisting of 3 zero coupon bonds.
  - Let <img src="https://render.githubusercontent.com/render/math?math=Z_1"> be a zero coupon bond with a face value of $600 and 1 year maturity, <img src="https://render.githubusercontent.com/render/math?math=Z_2"> a zero coupon bond with a face value of $600 and 2 years, and <img src="https://render.githubusercontent.com/render/math?math=Z_3"> a zero coupon bond with a face value of $10,600 and a 3 year matrutiy.
  - A portfolio consisting of <img src="https://render.githubusercontent.com/render/math?math=Z_1, Z_2, Z_3"> has the same cash flow as the bond, and so, by the cash flow version of the Law of One Price, the price of the bond must agree with the value of this portfolio at any time during its life.
  - Recall that the risk free, annually compounded interest rates for 1, 2 and 3 year terms are 0.75%, 1.5% and 2% respectively. Thus

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Z_1(0) = \frac{600}{1.0075} = 595.53"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Z_1(0) = \frac{600}{1.015} = 582.40"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Z_1(0) = \frac{10600}{1.02} = 9988.62"><br>
</p>

  - Thus, by the Law of One Price the bond price is 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=B(0) = 595.53 %2B 582.40 %2B 9988.62 = 11166.55">
</p>
