# Interest Rates and Future Values
- Interest rate is annually compuded if once per year the interest is added to the principal so that future interest is additionally charged on the interest earned to date.
- The compounding convention refers to this rate of interest rate capitalization.

- Suppose we invest _X_ for 2 years at interest rate _r(2)_ which is annually compounded interest rate. Then after 1 year, our total investment is _(1+r(2))X_
- This is the principal on which interest will be charged for a second year. Therfore, after 2 years, our investment has grown to _(1+r(2))(1+r(2))X_

# Future Value:
- If we invest a sum of money at some fixed interest rate for some term the final value of this investment, assuming all returns are invested at the same interest rate, is the future value of the intitial investment.
  - Let _r(t)_ be the available annual and annually compounded interest rate for a loan term of _t_ years.
  - Let _P0_ be the initial investment.
  - Then the future value if _P0_, at time _t_ is:
 <p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t) = (1 %2B r(t))^t P_0">
</p>
# Compounding Conventions
- __Periodic Compouding:__ Interest is said to be compounded with frequency m if interest is reinvested with principal m times per year. Once interest is added to the principal, future interest charges are levied on the interest accrued so far as well as the initial principal.
- _m_ times per year compounded interest rate is denoted by _(r_m(t))_
  - Suppose we initially invest X at this interest rate.
  - Because _(r_m(t))_ is an annual interest rate, in each compounding period, the earned interest is _((r_m(t))/m)X_
  - The value of investment after 1 period is:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=({1 %2B \frac{r_m(t)}{m}})X">
</p>
  - This is now the effective principal or the second compouding period, and so on.
  - The Investment after m periods is
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=({1 %2B \frac{r_m(t)}{m}})^{mt} X">
</p>
