# LIBOR Spot Curve
LIBOR is a short term interest rate published every day for loan terms (tenors) up to 1 year. Various interest rate derivatives allow LIBOR interest rates to be extended beyond 1 year tenor. In particular, market prices of Eurodollar futures and interest rate swaps  can be used to bootstrap an interest rate curve up to about the 30 year tenor. The result is a spot rate curve known as thEe LIBOR curve.

- Fundamental data in a spot curve are implied discount factors.

In order to express interest rates, yield curves, and discount factos observed on the markets at other times than _t=0_ we use a notation and concept from earlier.
  - Denote by _P(t, T)_ the price, at time _t_ of a zero coupon bond maturing at time _T_.
  - A default assumption is,all zero coupon bonds have a face value of $1, then _P(t, T)_ is the present value, at time _t_ of $1 paid at time _T_. That is, _P(t, T)_ is a "forward starting" discount factor, the discount factor observed at time _t_ for a payment received at time _T_.
  - In particular, _P(0, T)_ is the discount curve observed today, and we may relate this to our previous notation as _P(0, T) = d(T)_ and the discount curve observed on date _t_ is denoted by _P(t, T)_. 
  - We will now use the notation _P(t, T)_ to denote both discount factors and zero coupon bond prices, always mindful that they are conceptually different, but numerically equal.
  - NOTE: with this notation, the tenor, time to maturiy, or term of the loan is _T - t_
  - We will, in particular, use the notation _P(t, T)_ to denote the LIBOR discount curve prevailing on markets at time _t_.

# LIBOR Discount Curve
It is the curve of discount factors implied by the spot LIBOR rates up to a 1 year tenor, together with market observed Eurodollar futures prices and swap rates. Eurodollar futures and (LIBOR) swaps are interest rate derivatives, linked to the current short term LIBOR rates which we will study over the coming lecture. They provide the linkage between short term LIBOR and longer term interest rates through arbitrage principles.

Along with the discount curve, there are associated spot interest rates. We will denote the continuously compounded spot LIBOR rates, associated with the discount curve _P(t, T)_ by _y(t, T)_. They are thus related by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t, T) = e^{-(T-t)y(t,T)}">
</p>

Due to the simple compounding property of LIBOR rates themselves, simply compounded LIBOR rates are commonly used. 
We denote by _L(t, T)_ the simply compounded spot LIBOR rates, related to the discount curve by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(t, T) = \frac{1}{1 %2B (T-t)L(t,T)}">
</p>

The most important LIBOR curve is the curve observed on the present date, represented by _P(0,T)._ For the current LIBOR rates we use the abbreviated notations

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T) = y(0, T)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=L(T) = L(0, T)"><br>
</p>

So,in particular

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(0, T) = e^{-Ty(T)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P(0, T) = \frac{1}{1 %2B TL(T)}"><br>
</p>

### Example
Suppose the 6 month LIBOR discount factor is 0.98. What are the continously compounded and simply compounded 6 month LIBOR spot rates?

From the relatons in the previous slide we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T) = -\frac{\log(P(0,T))}{T}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=L(T) = \frac{1 - P(0, T)}{TP(0,T)}"><br>
</p>

We are given P(0, 0.5) = 0.98, so

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(0.5) = -\frac{\log(0.98))}{0.5} = 0.404"><br>
  <img src="https://render.githubusercontent.com/render/math?math=L(0.5) = \frac{1 - 0.98}{0.5 \times 0.98} = 0.0408"><br>
</p>

