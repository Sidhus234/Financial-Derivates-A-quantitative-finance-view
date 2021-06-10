# Forward Interest Rates
A __forward interest rate__ is an interest rate that can be locked in now for some loan term starting in the future. We denote by <img src="https://render.githubusercontent.com/render/math?math=L(t, T_1, T_2)"> the (LIBOR) forward interest rate that can be secured at time _t_ for a loan held from time <img src="https://render.githubusercontent.com/render/math?math=T_1\:\:to\:\:time\:\:T_2">. 

<img src="https://render.githubusercontent.com/render/math?math=L(t, T_1, T_2)"> is simply compounded rate that can be locked in at time _t_ for a loan term <img src="https://render.githubusercontent.com/render/math?math=T_1\:\:to\:\:T_2"> from the prevailing spot LIBOR curve and arbitrage principles. Arbitrage principles act on tangible traded assets. Since interest rates are not assets themselves we must work with some equivalent collection of assets. We will therefore work directly with bonds, and it is simplest to use zero coupon bonds.

Now we will consider forward prices for bonds.
- Let <img src="https://render.githubusercontent.com/render/math?math=P(t, T_1, T_2)"> be the forward price for a bond maturing at time <img src="https://render.githubusercontent.com/render/math?math=T_2"> and on a forward contract expiring at time <img src="https://render.githubusercontent.com/render/math?math=T_1 \lt T_2">.
- Consider 2 different portfolios each replicating a $1 payment received at time <img src="https://render.githubusercontent.com/render/math?math=T_2">:
  - A zero coupon bond maturing at time <img src="https://render.githubusercontent.com/render/math?math=T_2">
  - A forward contract expiring at time <img src="https://render.githubusercontent.com/render/math?math=T_1"> on a bond maturing at time <img src="https://render.githubusercontent.com/render/math?math=_2"> and a <img src="https://render.githubusercontent.com/render/math?math=P(t, T_1, T_2)"> notional zero coupon bond expiring at time <img src="https://render.githubusercontent.com/render/math?math=T_1">

<img src="https://render.githubusercontent.com/render/math?math=P(t, T_1, T_2)"> is the cost paid at time <img src="https://render.githubusercontent.com/render/math?math=T_1"> for a zero coupon bond maturing at <img src="https://render.githubusercontent.com/render/math?math=T_2">. For replication, we must invest in a zero maturing at time <img src="https://render.githubusercontent.com/render/math?math=T_1"> with face value <img src="https://render.githubusercontent.com/render/math?math=P(t, T_1, T_2)">

By the Law of One Price the cost of the two portfolios should be the same:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t, T_1)P(t,T_1, T_2) = P(t, T_2)">
</p>

Solving this equation for the forward price gives

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t,T_1, T_2) = \frac{P(t, T_2)}{P(t, T_1)}">
</p>

We note that, as an alternative, we could have used our general formula for forward prices. The result would be the same.

Recall the relationship between a simply compounded spot interest rate _L(t, T)_ and a discount factor or zero coupon bond price:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t, T) = \frac{1}{1 %2B (T-t)L(t, T)}">
</p>

The forward interest rate is defined to have the same relationship to the forward price that the spot interest rate _L(t, T)_ has to the cash price.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Forward \:\:Price = \frac{1}{1 %2B (T_2 - T_1)L(t, T_1, T_2)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\Longarrowright \frac{P(t, T_2)}{P(t, T_1)} = \frac{1}{1 %2B (T_2 - T_1)L(t, T_1, T_2)}">
</p>

Solving for the interest rate in terms of bond prices gives

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=L(t, T_1, T_2) = \frac{P(t, T_1) - P(t, T_2)}{(T_2 - T_1)P(t, T_2)}">
</p>

Thus the forward interest rate can be determined at time _t_ in terms of observable bond prices at time _t_.

__Interpretation:__ The bond prices  <img src="https://render.githubusercontent.com/render/math?math=P(t, T_1)"> and  <img src="https://render.githubusercontent.com/render/math?math=P(t, T_2)"> which prevail on markets at time _t_ are reflections of the prevailing structure of interest rates at time _t_.

Arbitrage considerations thus allow us to determine the forward interest rate  <img src="https://render.githubusercontent.com/render/math?math=F(t, T_1, T_2)"> given the prevailing structure of interest rates at time _t_.

## Example:
Suppose the current spot LIBOR rat (simply compounded) for a 2 year tenor is 4% and for a 4 year tenor is 7%. What forward interest rate can be locked for a loan starting in 2 years and due in 4 years?

 - We are given prevailing spot interest rates of _L(0, 2) = 0.04_ AND _l(0, 4) = 0.07_. From these, we may compute zero coupon bond prices 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(0, 2)">
</p>
