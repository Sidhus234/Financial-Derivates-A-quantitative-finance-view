# SONIA: The Sterling Overnight Index Average
- In use since the 1990s
- SONIA interest rate is the risk free rate recommended to replace LIBOR for products denominated in Pound Sterling (GBP)
- Like LIBOR, it is meant to measure the costs of short term borrowing for banks, in the sterling sector.
- Unlike LIBOR, it is based on actual transactions, and is supported by a market with daily transactions of £40 billion.
- Another difference from LIBOR is that SONIA has no term structure. It is an overnight rate only.
- The short loan term of SONIA makes it largely insensitive to credit risk (even though it is based on unsecured transactions) and this lack of a credit component is another fundamental difference with LIBOR.
- SONIA has been an actively published interest rate since 1997, making it the oldest and most established of the ARRs slated to replace LIBOR.
- In 2016, the Bank of England (BoE) took over responsibility for producing SONIA, and it is now calculated using the following reformed methodology.

## Methodology to calculate SONIA:
- __Definitions of SONIA by BoE:__ SONIA is a measure of the rate at which interest is paid on sterling short-term wholesale funds in circumstances where credit, liquidity and other risks are minimal.
- The Bank of England measures this rate by collecting data on the rates that banks are able to borrow funds from other financial institutions.
- For a transaction to be eligible to contribute to the benchmark calculation it must be at least £25 million.
- The eligible transactions are unsecured and have 1 day term to maturity.
- Once these rates are collected, SONIA is calculated as the _trimmed mean_ of these rates:
  - the hightest and lowest 25% of the rates are omitted, and the remaining "inner quartiles" are averages, weighted by volume, to produce the published SONIA number.


## SONIA Compounded Index:
- SONIA Compound in Arrears: SONIA is an overnight interest rate, so must be extended to a term rate to use with products with a term to matruity.
- The recommendation has been to use SONIA compounded in arrears as a term rate for most products requiring such a rate.
- __SONIA Compound Index__ on business date _t_, _I(t)_ by the equation

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I(t %2B 1) = I(t) \times (1 %2B \frac{S(t) \tau(t)}{365})">
</p>
<p align="center">
where S(t) is the SONIA rate for date t, and <img src="https://render.githubusercontent.com/render/math?math=\tau(t)"> is the number of calendar days that pass frombusiness dates t to t+1
</p>

- The SONIA compounded index measures the return on an investment made at overnight SONIA each business day, compounded daily.
- One may take any initial value of I(t) (or work with <img src="https://render.githubusercontent.com/render/math?math=\frac{I(U)}{I(T)}">), as all that matters is the implied return.
- Once _I(t+1)_ is calculated, _I(t+2)_ is calculated from _I(t+1)_ and the formula by substituting it in for _I(t)_, and so on iteratively.
- The result of the exercise is that:


<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I(t %2B m) = I(t) \times (1 %2B \frac{S(t) \tau(t)}{365}) \times ... \times (1 %2B \frac{S(t %2B m -1) \tau(t %2B m - 1)}{365})">
</p>

- From the index, we now calculate the __compounded SONIA rate__, from dates _T_ to _U_, denoted by _S(T, U)_ by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(T, U) = (\frac{I(U)}{I(T)} - 1) \times \frac{365}{d}">
  where <img src="https://render.githubusercontent.com/render/math?math=d"> is the number of calendar days between business dates T and U.
</p>

- This defines SONIA compounded in arrears as the simple term rate from date _T_ to date _U_ that would result in a return of _I(U)/I(T)_.
- In summary: SONIA compounded in arrears over a term from date _T_ to _U_ is the effective term rate (simply compounded) equivalent to rolling over an overnight loan at the overnight SONIA rate over this period.

## Term SONIA:
- SONIA compounded in arrears is a backward looking rate, unlike LIBOR which has a forward looking term structure.
- Some market participants have stated their preference for some form term SONIA with a similar forward looking term structure to LIBOR.
- In the UK, there is strong encouragement from regulators to use SONIA compounded in arrears for most financial products.
- For the small family of products that UK regulators are willing to entertain the use of term SONIA, there are providers currently publishing term SONIA numbers (Refinitiv, ICE) based on SONIA linked swaps and other derivatives.

## LIBOR Transition Timeline:
- The Bank of England has primulgated the following timeline for the final dissolution of sterling LIBOR:
<ol>
  <li>Q1 2021: Issue of new sterling LIBOR linked loans, bonds, securitizations, and linear derivatives (expiring after 2021) should cease. All legacy contracts referencing sterling LIBOR should be identified and their conversion accelerated.</li>
  <li>Q2 2021: Issue of new sterling LIBOR linked nonlinear derivatives (expiring after 2021) should cease</li>
  <li>Q3 2021: Complete active conversion of legacy sterling LIBOR products</li>
  <li>Q4 2021: Publication of sterling LIBOR (as a market representative rate) is halted immediately.</li>
  </ol>
