# Yield
- A __yield__ for a bond, or other security, is a measure of the return of the investment
- There are many different measures of yield used in bond and fixed income calculations
- One simple measure is simply to use the interest rate or coupon rate paid by the security
- __Current yield__ of a bond is the annual coupon value divide by the bond price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Current Yield = \frac{Coupan Value}{Price}">
</p>

### Yield to Maturity:
- is defined as interest rate _y_ such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = \sum_{j=1}^{J}\frac{c_j}{1 %2B y}^{T_j}">
</p>

   where _P_ is the market price of the bond, the coupons are c_1, c_2, ... c_J which are paid at time T_1, T_2, .. T_J respectively (Last coupon also includes the principal payment)

- __yield to maturity__, _y_ is that interest rate such that the market price of the bond would be recovered if all payments were discounted by it (_y_ here refers to annually compounded interest rate).
- With periodic compounding with _m_ periods per year the yield to maturity is that _y_ such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = \sum_{j=1}^{J}\frac{c_j}{1 %2B \frac{y}{m}}^{mT_j}">
</p>

- There is no closed formula for _y_, unless _J_ = 1. A root fitting method must be used to compute _y_. It is an easy root finding problem. 
