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

## Foreign Currencies:
- Foreign currencies are a famialiar asset in soceity. It is simply the cash unit used in foreign nations.
- We take _S(t)_ to be the exchange rate between our home currency and some foreign currency at time _t_.
- _S(t)_ is simply the price, in the home currency, of one unit of the foreign currency.
- A holding in a portfolio of <img src="https://render.githubusercontent.com/render/math?math=\alpha"> units of the foreign currency at _t = 0_ would be represented in a portfolio's value by a term (assumption: foreign currency is earning foreign risk free interest rate)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\alpha S(0)">
</p>

- We need notation for interest rates in different currencies. We denote the interest rate in a foreign currency by <img src="https://render.githubusercontent.com/render/math?math=r_f">
- When we need to be explicity about the interest rate in home currency, we will denote it <img src="https://render.githubusercontent.com/render/math?math=r_d">
- Using this notation, a holding of _N_ units of domestic currency is represented by <img src="https://render.githubusercontent.com/render/math?math=Ne^{r_dt}">
- Similarly, we assume that holdings of foreign currency are invested at the foreign risk free rate. So a holding of _K_ units of a foreign currency is worth <img src="https://render.githubusercontent.com/render/math?math=Ke^{r_ft}">
- when accounted in the foreign currency, and so, when accounted in the home currency is represneted by a term <img src="https://render.githubusercontent.com/render/math?math=K e^{r_ft}S(t)">

### Example 4:
Suppose we hold a portfolio consisting o 100 shares of GE, 25000 Euros, and a debt of USD $30,000 at time t=0. Write down the expression for the value of this portfolio at any time _t_. Suppose that the continously compounded risk free rate is 7% in Euros and 4% in USD. Suppose that in 1 year GE stock is $15/share. And suppose that in 1 year the Euro/USD exchange rate of $1.25/Euro.What is the value of portfolio in 1 year?
- Let <img src="https://render.githubusercontent.com/render/math?math=r_d"> be the domestic USD interest rate, <img src="https://render.githubusercontent.com/render/math?math=r_f"> be the Eurozone interest rate, <img src="https://render.githubusercontent.com/render/math?math=S_{GE}(t)"> the share price fo GE, and _F(t)_ the Euro/USD exchange rate.
- 
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 100 \times S_{GE}(t) %2B 25000 \times F(t) e^{r_ft} - 30000 e^{r_dt}">
</p>

- To evaluate the portfolio value in 1 year:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 100 \times 15 %2B 25000 \times 1.25 \times e^{0.07} - 30000 e^{0.04} = 3791">
</p>

## Dividends
- If a stock, with price _S(t)_, pays dividends, we have seen they can be measured as a dividend yield. 
- The dividend yield could be modelled as a continously compounded yield _y_, acting like an interest rate.
  - Suppose we start at time _t_ = 0 with an initial allocation of <img src="https://render.githubusercontent.com/render/math?math=\alpha"> to the stock.
  - Suppose all dividends are reinvested into the stock holdings.
  - Then, in analogy with the foreign exchange case, the allocation at time _t_ grows to 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\alpha e^{yt}">
</p>
  - and the investment is worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\alpha e^{yt} S(t)">
</p>

- Modelling dividends for individual stocks this way is sometimes done for convenience, especially in derivate models.
- Modelling dividends with a continuous yield is most appropriate for stock indexes, or stock portfolios. For an individual stock a more accurate model is simply to model the dividend as a lump sum payment.
- The primary application of these models is to pricing forward and future contracts.

## Commodities:
  - Covience yields can be modelled as a continously compounded return _y_.
  - Storage costs might be modelled as a continuously compounded cost _s_.
  - So, an investment in <img src="https://render.githubusercontent.com/render/math?math=\alpha"> units of a commodity, with unit cost _C(t)_ could be modelled as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\alpha e^{(y-s)t}C(t)">
</p>

- We would never model a commodity asset as if the convenience yield were a dividend that could be reinvested in holdings of the asset.
- The primary application of these models is to pricing forward and future contracts.


## Long and Short Positions
- The idea of taking a long or short positions on an asset is a generalization of buying or selling an asset.
- In fact, the most straightforward way to take a long position is to buy it, and the easiest way to short an asset is to sell it - if you already own it.
- However, an innvestor can "short" as asset without owning it, though it is not always straightforward to do so.
- However it is implemented, taking a short positions means you will profit if the value of the asset declines. The time to take a short position in an asset is when you think the asset's price is going to fall.
- The cleanest and most definitive way to define long and short positions in an asset is in terms of exposures.
- __Long Positions__ on a particular asset if when the value of our portfolio goes up when the value of the asset goes up.
- __Short Positions__ on a particular asset is when the value of our portfolio goes down when the value of the asset goes up.
- With "long" and "short" so defined it is worth noting that it is often not very easy to take either position directly in the cash market, either practically or even in principle.
- It is often easies to take a long or short position on some asset using derivatives.
- But there are ways to effect such positions directly in the cash market.
- Long positions are most straightforward. The simplest way to take a long position in an asset is simply to buy it. This, however, can be very expensive.
- Short positions are more problematic. It may not be straighforward to short certain assets, but certain asset classes do accomodate short positions.

#### Shorting Stocks:
 Stock exxchanges facilitate shorting individual stocks using the following mechanism:
   - The investor can borrow the stock from another investor, the stock's rightful owner.
   - The investor may then sell the stock on the market, receiving its current market value.
   - The investor is responsible for reimbursing the stock owner for any dividends earned while shorting.
   - The investor is obligated to return the stock to its rightful owner sometime in the future.
 - If we follow this procedure, we profit when the stock price falls, by the amount that it falls, since we will be able to buy it back for that much cheaper.
 - A few things to note abpout the stock shorting precedure just outlined:
  - Upon selling the stock when the position is entered we immediately receive the value of the stock in cash
  - For the life of the position, the obligation to return the stock to its rightful owner has the role of a liability, analogous to a debt (we are borrowing the stock).
  - The mechanisms for taking short positions in other asset classes are not necessarily the same, but we will assume generally that short positions have these properties for all other asset classes.


#### Short positions in portfolios:
Short positions in an asset can usually be represented in portfolios with a negative allocation.
- The mechnaisms for taking short positions in other asset classes vary.
- To take a short position in a foreign currency, one may simply borrow money in the currency.
- There are a variety of instruments with which one may short bonds. Reverse repos (repurchase agreements) is one of them.
- And there are a variety of vehicles available for taking long or short positions on interest rates (though one may simply borrow or lend money).
- Commodities are perhaps the most problematic asset class for taking cash short positions, but there are vehicles avaialblae for this for instance various ETF (exchange traded funds) products

### Example 5:
Suppose we have a portfolio that is long 500 shares of IBM and short 300 shares of GE. Whatis the value of this portfolio at time _t_ if <img src="https://render.githubusercontent.com/render/math?math=S_{IBM}(t)"> is the share price of IBM and <img src="https://render.githubusercontent.com/render/math?math=S_{GE}(t)"> is the share price of GE, both as a function of time?

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 500 \times S_{IBM}(t) - 300 \times (S_{GE}(0) - S_{GE}(t)">
</p>

### Example 6:
Suppose we are looking at 2 stock, Company A and Company B. Company A stock is currently trading at $50 per share and Company B stock is currently trading at $35 per share. Assume neither stock pays dividends. We believe that Company A is overpriced and Company B is underpriced, and so we want to short Company A and go long on Company B. Suppose we decide to short 80 shares of Company A and to go long, i.e. buy, 100 shares of Company B. Assume that any holdings of cash are invested at the risk free rate of 6^. Write down the value of this portfolio after we build it.

- Denote the share price of Company A and Company B by <img src="https://render.githubusercontent.com/render/math?math=S_A(t)\:\:and\:\:S_B(t)"> 
- Shorting the 8- shares of Company A will result in cash receipt of $50 per share, so the short position results in
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Cash Receipt = 80 \times 50 = 4000">
</p>

- Purchasing 100 shares of Company B requires an expenditure of %35 per share or

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Expenditure = 100 \times 35 = 3500">
</p>

- THis leaves a cash holding of $500 left over that will be invested at the risk free (continuously compounded) rate of _r_ = ^% = 0.06
- Thus, having built the portfolio, the value at time t is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 100 S_B(t) - 80 S_B(t) %2B 500 e^{0.06t}">
</p>

Now suppose it is 1 year later and our predictions have been vindicated. Company A stock is now trading at $20 per share and Company B is at $70 per share. Suppose we would like to now close out the short position by expect Company B to keep rising we would luke to put all available cash into the long position in Company B. Explain the operations we need to take to do this, and write down the value function for the new portfolio.
- To close out the short position we must return the 80 shares of Company A we shorted to their rightful owner. So we must purchase them on the market.
- With Company A shares trading at $20 purchasing back the 80 shares we need costs

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total cost = 80 \times 20 = 1600">
</p>

- Our cash holdings is now worth

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=500 e^{0.06t} = 531">
</p>

- which leaves an additional $1069 needed to buy back the Company A shares.
- We must liquidate enough of our holdings of Company B stock to raise these additional funds.
- Selling 16 shares of Company B at $70/share raises

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Cash Receipt = 16 \times 70 = 1120">
</p>

- Combining two sources of cash, we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total Cash = 531 %2B 1120 = 1651">
</p>

- From these funds we may take the $1600 necessary to buy back the 80 shares of Company A, leaving $51 left over.
- We repurchase the 80 shares of Company A from these funds, return to their rightfule owner, and so close out the short position. We retain 84 shares of Company B and the residual cash holdings of $51. We continue to invest the cash at the risk free rate, so after carrying out these transactions our portfolio now has value:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = 84 S_B(t)  %2B 51 e^{0.06(t-1)}\:\:for\:\:t\:\gt\:1">
</p>
