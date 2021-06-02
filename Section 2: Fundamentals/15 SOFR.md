# SOFR: Secured Overnight Financing Rate
- is the alternative reference rate that has been selected to replace LIBOR for USD denominated products.
- It is established and published by the Federal Reserve and, like SONIA, it is an overnight rate based on actual transactions in money markets.
- SOFR is based on financing rates paid in the overnight US Treasury Repo market.
- Repo is shorthand for repurchase agreements, and the US Treasury repo market in particular refers to those repo agreements collaterallized by US Treasury securities.

### Repurchase Agreements (repo):
- __Repurchase Agreements:__ (repo) are short term deals between 2 parties to exchange cash for an asset, with an agreement to reverse the exchange at some future date.
- In a __repurchase agreement__ one counterparty sells an asset to the other, with the obligation to buy it back at a later date at a preset price.
- The essence of a repo is a collateralized loan. The initial purchaser of the asset is lending money to the seller, and taking the asset as collateral.
- At the termination of the contract, the seller (cash borrower) buys the asset back for the original price + interest which is levied at the __repo rate.__

<img src="../Images/S2 - Repurchase agreements.PNG" alt="Repurchase agreements"/>

- The flows in a repo: 
  - At contract origiation the lender supplies the borrower with cash ("buys" the security), and in turn receives the security from the borrower
  - On the termination date of the contract, the borrower pays the lender the original cash lent + interest ("repurchase" the security), and the lender returns the security to the borrower.

- __Overnight Repo__ refers to those repo agreements where the termination date of the repo is the next day, and __term repo__ corresponds to those repos with a longer duration than 1 day.
- Market for overnight repo is much larger than that for term repo.
- SOFR is based on the repo rates paid in the market for overnight Treasury repo, those overnight repo contracts where the traded security is a US Treasury security.
- The daily transaction volume in overnight US Treasury repo market is estimated at about $1 trillion.
- The size of the market is the main reason SOFR was chosen as the USD LIBOR replacement.

# SOFR Construction:
- The US Treasury repo market is large and consists of various segments, including bilateral deals and tri0party repo with a third intermediary party (usually the Bank of New york Mellon).
- In includes a "general collateral" component, where counterparties are indifferent to the particular security used as collateral, and a "special collateral" where the cash lender seeks a specific security.
- The Federal Reserve Bank of New York collects data on repo rates across these different market segments and calculates SOFR as the volume weighted median of these rates.
- SOFR is published the day after collection, the day the overnight transactions underpinning it mature.

# Compound SOFR:
- As an overnight rate, SOFR, like SONIA, must be converted to a term rate in some way to use it for products with any term to maturity longer than 1 day.
- For most products, regulators have recommended some version of either SOFR compounded in arrears or SOFR compounded in advance.
- The basic construction of either of these is the same and is the same as the construction of SONIA in arrears.
- The difference is that an "in advance" calculation is done before the loan term using the SOFR rates that prevailed prior to the start date.
- As "in arrears" rate is calculated at maturity using the SOFR rates in effect during the actual loan term.
- To calculate anu compound SOFR rate, there is a SOFR index _I(t)_ for business date _t_ defined recursively as:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I(t %2B m) = I(t) \times \product_{j=0}^{m-1}{(1 %2B \frac{S(t %2B j) \tau(t %2B j)}{360})}">
</p>
<p align="center">
where S(t) is the overnight SOFR rate for date t and <img src="https://render.githubusercontent.com/render/math?math=\tau(t)"> is the number of calendar days between business dates t, and t+1
</p>

- The compound SOFR rate from dates _T_ to _U_ is then

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(T, U) = (\frac{I(U)}{I(T)} - 1) \times \frac{360}{d}">
</p>

- These differ from the SONIA formulas only in the Act/360 day count convention (for USD money markets).

### Example:
Suppose that on Monday we are about to initiate a 1 week loan with a counter party to be charged SOFR in advance. If last week's SOFR rates, Monday through Friday respectively were 1.42, 1.44, 1.41, 1.38, and 1,36, calculate SOFR in advance for the 1 week loan to be entered into today.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{I(6)}{I(1)} = (1 %2B \frac{0.0142}{360}) \times (1 %2B \frac{0.0144}{360}) \times (1 %2B \frac{0.0141}{360}) \times (1 %2B \frac{0.0138}{360}) \times (1 %2B \frac{0.0136(3)}{360}) = 1.00027030048022143">
</p>

The 1 week compound SOFR rate is then

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(1,6) = (1.00027030048022143 - 1) \times \frac{360}{7} = 0.0139014">
</p>

A SOFR calculator and data is available at the [website](nwm.realisedrate.com/SOFR)

## SOFR in Arrears:
- Note that if the agreement had been to charge the SOFR in arrears we would have calculated compound SOFR based on the next week of rates. Thus the interest charge for the loan would not have been known until the end of the loan term.
- With compounding in arrears, the interest charged for loan products will not be determined until the end of the loan period, when the payment is due.
- This last minute determination of the interest charge causes difficulty for some borrowers and is a barrier to SOFR adoption in some cash markets.
- Regulators have thus recommended variations on the basic compounding structures.
- Some of these variations include "lookbakc" structures, where the rates used for computing the compound rates are lagged some number of days.
- Another strategy is to allow a delay between fixing date of the rate and the settlement date when payment is due.


## Credit Sensitive Alternatives to SOFR:
- SOFR;s lack of credit senstivity has been an impediment to its adoption.
- It's adoption for certain loan products, such as bilateral business loans has been very slow.
- Banks have stated that SOFR is an unsuitable rate for loan products, where a rate that naturally adjusts to changing credit conditions in markets if required.
- Thus banks, and other cash market participants, habe called for credit senstive alternatives to SOFR to replace LIBOR.
- In November, 2020, US regulators (the Fed, the OCC, the FDIC) issued a statement that they were not endorsing SOFR or any other particular rate as the replacement for LIBOR.
- Banks this have the freedpm to replace LIBOR with rates they deem appropriate for different markets, and many are seeking credit sensitive alternatives.
- One such credit sensitive rate is AMERIBOR, a USD rate somewhat similar to SONIA in being based on unsecured transactions.
- Other credit sensitive alternatives include:
  - [ICE Bank Yield Index](https://www.theice.com/iba/bank-yield-index)
  - [BSBY (Bloomberg)](https://www.bloomberg.com/professional/introducing-the-bloomberg-short-term-bank-yield-index-bsby/)
  - [IHS Markit Credit Spread Adjustment](https://ihsmarkit.com/research-analysis/publish-daily-credit-spread-adjustment-for-sofr-from-Q2-2021.html)

# Present and Future of USD LIBOR:
- __Transition:__ Due to difficulties like the ones noted above, SOFR adoption in markets has been slow.
- For many cash products (eg. bilateral business loans) transition to SOFR has been anemic, with banks still offering LIBOR as their only floating rate option
- It has in turn been very slow in derivative markets with SOFR linked products (futures, swaps) still being a small percentage of LIBOR linked products.
- As of spring 2021, it is not clear what the USD rate world will finally transition to.
- One possibility is a multi-rate world, with SOFR sharing the space with alternatices like AMERIBOR


