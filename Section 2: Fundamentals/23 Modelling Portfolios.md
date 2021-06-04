# Portfolios:
- A portfolio is a collection of assets. We group assets in a portfolio when we want to consider them together as a unit.
- The value of the portfolio is the sume of the values of the component assets.
- For each of the assets in a portfolio there will usually be a natural base valution unit.
- For instance, for stocks the unit would be shares, for foreign currencies it would be one unit of currency (ef Euros, Yen)
- We will express our portfolio values in terms of the number of base units of each asset we want to include (called the allocation) times the value of the base units.

# Modelling Portfolios
- Denote the value at time _t_ of the base unit of the _ith_ asset by <img src="https://render.githubusercontent.com/render/math?math=S_i(t)">. 
- Denote the allocation of the _ith_ asset in our portfolio by <img src="https://render.githubusercontent.com/render/math?math=\alpha_i">.
- So, if asset 1 is IBM stock, and we hae 100 shares of IBM in our portfolio, then <img src="https://render.githubusercontent.com/render/math?math=\alpha_1 = 100">.
- If asset 2 is Japanese Yen and we have 100,000 Yen in ourportfolio, then <img src="https://render.githubusercontent.com/render/math?math=alpha_2 = 100,000">.
- The value of our portfolio at time _t_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = \sum_{i=1}^{N} \alpha_i S_i(t)">
</p>

### Example 1:
- Suppose we have a portfolio consisting of IBM shares, GE shares, and T-bills maturing in 9 months. Write down a general expression for the value of this portfolio at some time _t_. Now assume that our allocations are 500 shares of IBM, 1000 shares of GE, and 20 T-bills. Assume that at time _t_ the IBM share price s $150/share, the GE share priceis $15.00/share. and the T-bills are currently trading at a market price of $973. What is the value of our portfolio at time _t_?

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_1(t) = 500 \times 150 %2B 1000 \times 15 %2B 20 \times 973 = 109460">
</p>

## Lump sums of cash:
- Sometimes in a portfolio, we want to hold cash.
- We usually assume that cash in a portfoolio is invested at the risk free rate.
- Let _r_ be the continuously compounded risk free interest rate. A lump sum of cash of _X_, assuming it was brought into the portfolio at time 0 will be represented by a term (below) in a portfolio's value expression

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Xe^{rt}">
</p>

### Example 2:
Suppose we have a portfolio consisting of 100 shares of IBM stock and $10,000 of cash, invested at risk free rate _r_ (continuously compounded) at time _t_ = 0. Write down an expression for the value of this protfolio at any future time _t_.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 100 \times S_{IBM}(t) %2B 10000e^{rt}">
</p>


## Debts:
- A debt is represented in a portfolio exactly as a lump sum of cash, but with a negative allocation. 
- A debt of _X_, taken on at time _t_ =0, and borrowed at the risk free rate of interest _r_ would appear in our portfolio value expression with a term

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-Xe^{rt}">
</p>

### Example 3:
Suppose in the previous example that we wanted to include a debt of $7000 in our portfolio instead of an investment of $10,000.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 100 \times S_{IBM}(t) - 7000e^{rt}">
</p>

## Negative Portfolio Values:
- A portfolio containing debt implies the possibility of a negative portfolio value.
- What happens, for instance, if the debt exceeds the total value of all the assets in the portfolio?
  - Suppose a portfolio has _n_ assets, with values <img src="https://render.githubusercontent.com/render/math?math=S_i(t)"> for <img src="https://render.githubusercontent.com/render/math?math=i = 1 \cdots n"> and a debt of value <img src="https://render.githubusercontent.com/render/math?math=Xe^{rt}">. So it's value is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = \sum_{i=1}^{n} S_i(t) - Xe^{rt}">
</p>

  - if at some time _t_
  
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Xe^{rt} \gt \sum_{i=1}^{n} S_i(t)">
</p>

  - then <img src="https://render.githubusercontent.com/render/math?math=V(t) \lt 0">
  - In this case, the portfolio has a negative value because the obligations in the portfolio exceed the value of the assets.
  - If an investor held this portfoliom their net worth would increase if they got free of it.
  - If a portfolio's value _V(T) > 0_ then the value of the assets exceeds the value of the liabilities. An investor who owns the portfolio can sell it for _V(t)_ in cash.
  - I f_V(t) < 0_, then the liabilities in the portfolio exceed the assets, and the investor would have to pay someone else to take the portfolio.
