# Time value of Money
- Idea that $1 received in future is not worth $1 today (It is worth less than $1)
- is used to justify the existance of interest rates

# Present Value
- The __present value__ of _X_ is the amount that should be invested today at prevailing interest rates so that at time _t_ the investment will be worth exactly _X_
- Denote the present value of _X_ by _PV_. Then _X_ is the future value of _PV_.
  - Let _r_ be the prevailing risk free annually compounded interest rate.
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B r)^t PV = X">
  </p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV = \frac{X}{(1 %2B r)^t}">
</p>
- Present values can be expressed in terms of other interest rates with different compounding conventions.
  - Suppose _(r_m)_ is periodically compounded interest rate, with compounding frequency _m_.
  - The future value relation
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B \frac{r_m}{m})^{mt} PV = X">
</p>
  - implies the present value of X is
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV = \frac{X}{(1 %2B \frac{r_m}{m})^{mt}}">
</p>
- If _(r_c)_ is continously compounded then we have
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{r_ct} PV = X">
</p>
  - which implies
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=PV = e^{-r_ct}X">
  </p>

# Discount Factors
- Present value can be writted as
<p align="centre">
  <img src="https://render.githubusercontent.com/render/math?math=PV = d(t)X">
  </p>
where
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=d(t) = \frac{1}{(1 %2B r)^t}">
  </p>
  - d(t) is called a __discount factor__
  - d(t) = the value today of receiving $1 at time t. Discount factors reflect the time value of money
  - Discount factors are in one to one correspondence with interest rates. If we know one we can compute the other.
  - Future values can also be expressed in terms of discount factors. Note that the future value at time _t_ of $1 investment today is simply the reciprocal of d(t)
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{d(t)} = (1 %2B r)^t">
  </p>
  - Thus the future value of investment of _P0_ = _X_ dollars today is
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=P(t) = \frac{1}{d(t)} X = (1 %2B r)^t X">
  </p>
- Discount factors may be expressed in terms of interest rates with different compounding conventions. In terms of _m_-times compunded rates
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=d(t) = \frac{1}{(1 %2B \frac{r_m}{m})^{mt}}">
  </p>
- In terms of continuous compounding
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=d(t) = e^{-r_ct}">
  </p>

## Primacy of Discount Factors:
It is discount factors, not interest rates, that represent most directly the fundamental information: the value today of $1 paid at time _t_.
- The reciprocal is perhaps even more direct:
<p align="centre">
<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{d(t)}">
  </p>
= Value of $1 Investment in t Years = Gross Retrun Realized at Time t

- No investment in the economy can offer lower return than risk free return
- Different interest rates, for instance with different compounding conventions, are similar to different choices of units for measuring the same fundamental quantity.
- 
