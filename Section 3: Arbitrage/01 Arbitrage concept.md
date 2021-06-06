# Arbitrage
### Rough Idea
  - Risk less profit 
  - An Investment opportunity in which there is a positive chance of profiting, and no chance whatsoever of losing money.
  - Arbitrage in efficient markets should not exisit. But in real world, arbitrage does exist.
  - In economics, basic view is arbitrage are non-equilibrium phenemonen. They are transient, and when ever one pops up, some entity will exploit it to drive out the arbitrage.

### Formal Definition
- __Mathematical definition of Arbitrage:__ An_arbitrage is a portfolio with the value _V(t)_ satisfying <img src="https://render.githubusercontent.com/render/math?math=V(t) \le 0"> and, for some time _T > 0_ in the future

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob(V(T) > 0) = 0 \:\:\: and \:\:\:Prob(V(T) > 0) >0">
</p>

  - At time 0, we don't need to spend any money to enter the portfolio.
  - There is no chance of losing money if you held the potfolio till time _T_.
  - Usually arbitrages will be realized in the following way: a portfolio will be presented that can be entered without cost _(V(0) = 0)_ that yields a certain and positive profit at some time _t > 0._

#### To apply the arbitrage concept:
  - __Basic Principle:__ Arbitrages cannot exist
  - If we make assumptions and we can show those assumptions imply that an arbitrage portfolio exists, then we can rule those assumptions out.

#### To apply arbitrage concept for pricing:
  - Assume 2 assets do not have the same price.
  - Show that the assumption allows the construction of an arbitrage portfolio.
  - Conclude that the 2 assets must have the same price.

## Arbitrage Example 1:
Suppose we have 3 stocks, denote them as stocks _A, B, C_. Let the prices of the stocks at time _t_ be <img src="https://render.githubusercontent.com/render/math?math=P_A(t), P_B(t), \:\: and \:\: P_C(t)">. Suppose that right now _t = 0_ the prices of the stocks are:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(0) = 25"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_B(0) = 20"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_C(0) = 80"><br>
</p>

We assume that time is discrete, so the next time at which anything can happen is _t = 1._
At time _t = 1_ we suppose there are only 2 states of world, State I and State II. In each state of the world each of our stocks can only take ne value, as given below:
  - In State I:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(1) = 20"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_B(1) = 15"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_C(1) = 50"><br>
</p>

  - In State II:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(2) = 30"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_B(2) = 35"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P_C(2) = 100"><br>
</p>

Is there an arbitrage opportunity between these stocks?

- Hint: notice if we add the first row to 2 times the second row, we get the third row.
- In other words <img src="https://render.githubusercontent.com/render/math?math=P_A(1) %2B 2P_B(1) = P_C(1)"> in all states of the world.
- But this relation doesn't hold at _t = 0_. We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(0) %2B 2 \times P_B(0) = 25 %2B 2 \times 20 = 65 \lt 80 (P_C(0))">
</p>
- This indicates stock C is overpriced at time _t = 0._
- A mispriced asset is the red flag that an arbitrage opportunity may be present.


- The general procedure to construct an arbitrage when you suspenct 2 assets are mispriced relative to each other is:
  - Short the expensive asset.
  - Go long the cheap asset.

- We will follow this idea here:
  - The expensive asset is 1 share of stock C.
  - The cheap asset is a portfolio consisting of 1 share of stock _A_ and 2 shares of stock _B_.
  - So we will construct an arbitrage portfolio by going long 1 share of A, 2 shares of B and shorting a share of C.
  - To be explicit, we will, at time _t = 0_ enter a portfolio consisting of
    - 1 share of A
    - 2 share of B
    - a short position in 1 share of C.

  - The total cost to enter the 2 long positions is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(0) %2b 2P_B(0) = 25 %2B 2 \times 20 = 65">
  </p>
  - Shorting 1 share of _C_ results immediately in a receipt in cash of <img src="https://render.githubusercontent.com/render/math?math=P_C(0) = 80">.
  - This is enough cash to cover the cost of long position $65, and we are left with $15, which we may invest at the risk free interest rate.
  - We hold these positions until _t = 1._
  - At time _t = 1_ we have seen that in all states of the world we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_A(1) %2b 2P_B(1) = P_C(1)">
  </p>
  - We own 1 share of A, and 2 shares of B, and we are still short one share of C, which gives us the obligation to return that stock to its rightful owner.
  - We can fulfill that obligation now by:
    - Selling the shares of A and B we own which yields the price of 1 share of C in cash.
    - Purchasing a share of C
    - Close the short position in C 
    - Taking these steps closes out all our positions.
    - __But:__ we have retained the $15 profit we realized at _t = 0_
    - That profit is a riskless profit, and this portfolio is an arbitrage portfolio:
      - We spent nothing to enter into the portfolio
      - There is no possibility of losing money
      - With probability 1 (ie in all states of the world) we will earn the $15 profit (at t = 0).

## Arbitrage Example II:
Suppose there is a bond with a $10,000 face value trading at par right now (so current market price of the bond is $10,000). Suppose the bond matures in 3 years and pays an annual coupon of 6%. Suppose the current annually compounded risk free interest rates for the 1, 2, and 3 year terms are:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r(1) = 0.75"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r(2) = 1.5"><br>
  <img src="https://render.githubusercontent.com/render/math?math=r(3) = 2"><br>
</p>
Is there an arbitrage opportunity?

- The bond pays a $600 coupon in 1 and 2 years, and pays par value + coupon = $10,600 in 3 years.
- Fair value of the bond is:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=B = \frac{600}{1.0075} %2B \frac{600}{1.015^2} %2B \frac{10600}{1.02^3} = 11166.55">
</p>
- So the bond is underpriced (As it is trading for $10000). This suggests a potential arbitrage involving buying the bond.
- The corresponding discounted values of each of these payments, at the given interest rates are:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{600}{1.0075} = 595.53"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\frac{600}{1.015^2} = 582.40"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\frac{10600}{1.02^3} = 9988.62"><br>
</p>
- If we borrow these amounts of money for the corresponding terms then as each debt comes due it will be exactly matched by a payment from the bond.
- __Note:__ This is equivalent to selling 3 zero coupon bonds with the bond payments as the par values.
- We may thus construct an arbitrage as follows:
  - Borrow $595.53 FOR 1 YEAR, $582.40 for 2 years and  $9988.62 for 3 years. The net proceed are $595.53 + $582.40 + $9988.62 = $11.166.55
  - Purchase the bond for $10,000 and retain


<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=11166 - 10000 = 1166.55">
  </p>
  - Invest this cash holding at the risk free rate for 3 years.
  - Our portfolio has 3 components:
    - The bond
    - The 3 loans
    - A cash holding of $1166.55 invested at the risk free rate.
  - The cost to enter this portfolio is 0.
  - To prove that this is an arbitrage portfolio, we need to show that it yields a positive and certain profit.

- As each of the 3 debts comes due, a payment from the bond exactly matches the amount due, clearing the due.
- After 3 years, the bond has expired as have the 3 debts.
- We are left with our investment of cash which is now


<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1166.55) \times (1.02)^3 = 1237.95">
  </p>
- the futre value in 3 years of our initial cash investment.
- It costs nothing to enter into this portfolio and it yields a riskless and certain profit of $1237.95. This is an arbitrage
