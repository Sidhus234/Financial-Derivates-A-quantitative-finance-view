# Short term interest rates:
- 2 weeks, 3 days, 1 day or over-night loans
- Concept of compounding is not applicable
- __Simple Interest__ is levied only on original principal.
- No interest is charged on the accumulated interest at any time. There is no compounding.
- If we loan or invest a principal _F_ at a simple interest rate _r_ for a duration of _T_ years, the total interest paid will be

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total interest = rTF">
</p>

- The total value of the investment value at the end of period is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total investment value = (1 %2B r)TF">
</p>

- NOTE: _T_ doesn't have to be an integer and simple interest is most commonly used for loan or investment terms less than 1 year

# Day count conventions:
- In fixed income markets, there are different accounting conventions for the precise formula to use to calculate terms to maturity for investments or loans.
- In short term money markets, there are 2 major day count conventions followed, depending on the domicile: actual/360, and actual/365
- Under the __actual/360__ day count the loan term is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=term = \frac{actual number of days}{360}">
</p>

- Under the __actual/365__ day count the loan term is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=term = \frac{actual number of days}{365}">
</p>

- Actual/360 is followed in most money markets, including USD, but actual/365 is followed in Sterling (UK) markets, and in markets traditionally linked to it.

### Actual/360
- loan term is calculated as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=term = \frac{actual number of days}{360}">
</p>

- total interest is calculated as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=interest = \frac{actual number of days}{360} x rF">
</p>

- total investment is calculated as
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total investment value = (1 %2B r\frac{actual number of days}{360}) x F">
</p>


### Actual/365
- loan term is calculated as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=term = \frac{actual number of days}{365}">
</p>

- total interest is calculated as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=interest = \frac{actual number of days}{365} x rF">
</p>

- total investment is calculated as
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Total investment value = (1 %2B r\frac{actual number of days}{365}) x F">
</p>
