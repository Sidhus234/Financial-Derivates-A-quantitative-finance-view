# Arbitrage adn Discounted Cash Flow Analysis
- Arbitrage is what justifies the whole notion of the time value of money and of the idea of present value.
- The definition of present value (in which the time value of money concept is implicit):
  - The present value, today, of payment _X_ to be received at time _t_ is the amount of money that would need to be invested today, at prevailing interest rates, to equal the payment when it is made at time _t_. Mathematically this is (where r = risk free rate):

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV = e^{-rt}X">
</p> 

- Now consider this situation from the point of view of the Law of One Price:
  - If we invest the PV today, this asset will be equal in value to the payment at time _t_.
  - That is, the PV is the value of the and asset, today, that will be equal in value to the payment when it is made.
  - The Law of One Price then tells us that either the PV is the price today of any asset paying _X_ at time _t_, or else there is an arbitrage.
  - So the present value of the payment is exactly the value determined by arbitrage considerations.

## Example 1:
Suppose the prevailing interest rate for a 3 year term is 6%. Suppose a contract paying $10,000 in 3 years is currently trading for $9000. Is there an arbitrage opportunity and if so, how can you exploit it. What if this contract is trading for $7000?
- __Remark:__ This contract is equivalent to a zero coupon bond.
- Our previous discussion suggests that the present value of the $10000 payment is the arbitrage price of this contract, and any deviation from it suggests an arbitrage opportunity is available.
- The PV os the payment is:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV = e^{-0.06 \ times 3}(10000) = 8353">
</p>

- __Case 1:__
  - If the contract is trading for $9000, then comparison with the PV suggests this contract is overpriced. So we would like to sell this contract. Doing so yields a $9000 cash payment which we can invest at the risk free rate. Then in 3 years our investment is worth:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{0.06 \times 3}(9000) = 10775">
</p>

  - We may then, at this time, pay out our $10,000 obligation, clearing of a profit of $10,775 - $10,000 = $775. This is riskless profit.

- __Case 2:__
    -In this case of the offered price of $7000, comparison with the PV suggests this is underpriced, so we want to buy this contract. We borrow $7000 at the risk free rate and purchase the contract. 3 years later, our debt has accumulated to 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{0.06 \times 3}(7000) = 8381">
</p>

  - We receive $10,000 payment from the contract, pay off the debt and retain $10000 - $8381 = $1619 as a riskless arbitrage profit.

- In fact, the use of discounted cash flow analysis as a valuation procedure generally is an example of arbitrage pricing.
- The form of the arbitrage principle that is closed to the circumstances of discounted cash flow analysis is the cash flow version of the Law of One Price.
- Recall the definition of the present value of a stream of cash flows: the total amount of cash that needs to be invested today to exactly replicate the cash flow stream.
- The language clearly suggessts an implicit invocation of the Law of One Price.
- __Remark:__ The second arbitrage example from this section is a special case of the general analysis in this lecture
  - Recall the context of discounted cash flow analysis: we have a security making payments

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=c_1, c_2, \cdots , c_n">
</p>

  - at times

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=t_1, t_2, \cdots , c_n">
</p>

  - Each payment can be replicated by a zero coupon bond maturing at the time of the payment and with face value the amount of the payment.
  - A portfolio consisting of all _n_ of these zero coupon bonds exactly replicates the cash flow.
  - By the cash flow version of the Law of One Price, the value of this portfolio must equalt the value of the cash flow.
  - The value of the portfolio at time _t_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = \sum_{i=1}^{n} Z_i(t)">
</p>

  - For the ith zero coupon bond we thus have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Z_i(t) = c_i">
</p>

  - and so its value at time 0 is simply the discounted value today of the payment, which can be written in terms of discount factors as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Z_i(0) = d(t_i)c_i">
</p>

  - Let _P(t)_ be the value of the cash flow (in particular _PV = P(0)_). From Law of One Price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(0) = V(0)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\sum_{i=1}{n}Z_i(0)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\sum{i=1}{n}d(t_i)c_i">
</p>

  - which reproduces the formula for discounted cash flow analysis. This arguement shows that both discounted cash flow analysis and the bond pricing formula from section 1 are special cases of arbitrage pricing.

