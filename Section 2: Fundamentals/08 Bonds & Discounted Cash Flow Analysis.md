# Bonds

## Introduction
- A bond is an asset, often regarded as a "debt instrument". One may think of "owning" a bond as the same thing as "owning" debt.
- Debt is an asset that is bought and sold on markets every day. It is the principal commodity of the bond and money markets
- A bond is created when a bond issuer first offers one on the market
- The bond is purchased by _bond holders_ or _bond buyers_
- The bond price paid by the bond holders to the bond issuer represents a loan or debt. In essence, the bond buyer is lending the bond price to the bond issuer.
- __NOTE:__ The standard terminology for bonds for what is generally called the principal of a loan is __par value__ or __face value__

## Bond Process:
<ol>
  <li> Bond holder pays bond price to bond issuer </li>
  <li> Bond Issuer pays interest payments to bond holders (for entire life of the bond/till maturity of bond) </li>
  <li> At maturity, Bond issuer pays the principal (face value or par value) to the bond holders </li>
  <li> Bond Price is not always equal to Par value or Face value of the bond</li>
  <li> For Treasury bonds (only exception) par value and bond price is equal</li>
  <li> For Treasury bills, par value is usually $1000 but bond price is discounted value of par value based on interest rates expected</li>
  </ol>
  
 ## Mathematical Model of a Bond
 - In a bond there are preset times when the payment is made


<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=t_1, t_2, ..., t_N">
</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_1, C_2, ... C_N">
</p>

<p align="center">
<img src="../Images/S2-bond payment schedules.PNG" alt="Bond Payment Schedule"/>
</p>

 - The price of bond is _Present Value_ of all the payments being paid over the life of bond
 - Value of bond, _P_, is the present value of the coupon and par value payments:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = \sum_{i=1}^{N} d(t_i)c_i">
</p>

- The bond price we have calculated in this lecture is what is known as the __dirty price__. On the secondary bond market, it is not the price that bonds trade at. It does not take into account the accrued interest from the earliest coupon payment.
