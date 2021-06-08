# Value of Forward COntract
Our previous formula for the forward contract value was valid for underlying assets that produce no income. We will now generalize it to income generating underlying assets. We will extend our notation for the value of a forward contract (long position) to _V(t; K,T)_. This shows explicitly the dependence on the forward price _(K)_ and the expiration date _(T)_. 
- Denote by <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> the fair forward price for forwards expiring at time _T_ that prevails in the market at time _t_
- This means <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> is exactly the forward price such that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t %3B K_T(t), T) = 0">
</p>

Note that <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> is just notation for a quantity we have already been computing, but usually at _t=0_. In particular <img src="https://render.githubusercontent.com/render/math?math=K_T = K_T(0)"> in our previous notation.

- It follows from our work so far that for an underlying that pays no incmome

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = e^{r(T-t)}S(t)">
</p>

- For underlying asset that pays a known income between _t_ and _T_ with present value _I_

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = (S(t) - I(t))e^{r(T-t)}">
</p>

__Remark:__ In our treatment of futures contracts this same notation will be used to denote the prevailing market futures price, which does not necessarily equal the forward price.

- We have the following general result for the forward contract value (below). The proof is by an arbitrage arguement. 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t %3B K, T) = (K_T(t) -K)e^{-r(T-t)}\:\:\:\:\:(1)">
</p>

- At time _t_ enter into 2 forward positions:
  - a long position in a forward contract expiring at time _T_ with contract price _K_
  - a short position on a forward contract also expiring at time _T_ and with contract price <img src="https://render.githubusercontent.com/render/math?math=K_T(t)">.

- So from time _t_ to _T_ we hold a portfolio of the two forward positions, which has the value at time <img src="https://render.githubusercontent.com/render/math?math=\tau (t \le \tau \le T)">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(\tau %3B K, T) - V(\tau %3B K_T(t), T)">
</p>

- Since both contracts expire at time  _T_ our portfolio value at time <img src="https://render.githubusercontent.com/render/math?math=\tau = T)"> is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(T %3B K, T) - V(T %3B K_T(t), T)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==S(T) -K -(S(T) - K_T(t))"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(t) - K"><br>
</p>

  which is a cash payment. By the Law of One Price the value of the portfolio at any earlier time must be equal to the discounted value of this payment.
  
- Thus

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t %3B K, T) - V(t %3B K_T(t), T) = (K_T(t) - K)e^{-r(T-t)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=as\:\: V(t %3B K_T(t), T) = 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V(t %3B K, T) - 0 = (K_T(t) - K)e^{-r(T-t)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V(t %3B K, T) = (K_T(t) - K)e^{-r(T-t)}"><br>
</p>

  where <img src="https://render.githubusercontent.com/render/math?math=V(t %3B K(t), T) = 0"> since <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> is the fair forward price for this contract. This establishes formula (1). 
  
- We now apply formula (1) to the case of a forward on an underlying generating a known income.
  - In the last lecture we derived the forward price

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = (S(t) - I(t)) e^{r(T-t)}">
</p>

  - Subsitituing this in formula (1) then gives

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = (K_T(t) - K) e^{-r(T-t)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V(t) = ((S(t) - I(t))e^{r(T-t) - K)e^{-r(T-t)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - I(t) - Ke^{-r(T-t)"><br>
</p>

  giving the value of the long position in the forward contract at time _t_.

</p>
