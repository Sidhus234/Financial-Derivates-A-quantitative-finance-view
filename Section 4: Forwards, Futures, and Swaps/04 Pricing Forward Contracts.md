# Pricing Forward Contracts:
- To apply, the Law of One Price to value the long position, need to construct a replicating portfolio whose value at time _t = T_ agrees with the forward payoff

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(T) - K_T">
</p>

- For the first term S(T) this corresponds to simply holding the underlying asset. Thus, simply holding the asset in our portfolio will replicate this component.
- The term <img src="https://render.githubusercontent.com/render/math?math=-K_T"> simply represents a payment (a debt) of <img src="https://render.githubusercontent.com/render/math?math=K_T"> in cash. The discounted (absolute) value of this payment at _t = 0_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T">
</p>

- So the payment is replicated by a debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T"> (so comes with a - sign)
- To replicate the long forward payoff we canuse a portfolio consisting of 
  - the underlying asset (long)
  - a debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T"> entered at time _t = 0_

- Such a portfolio has value

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - e^{rt} e^{-rT}K_T = S(t) - e^{-r(T-t)}K_T">
</p>
  
  (the second term is the future value of the debt of <img src="https://render.githubusercontent.com/render/math?math=e^{-rT}K_T">)

- We check if this is a replicating portfolio by evaluating _V(T)_
- At expiration date _T_, the value of portfolio is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - e^{-r(T-T)}K_T = S(T) - K_T">
</p>

  which is the forward payoff, confirming this is a replicating portfolio.
- From the Law of One Price, the value of the forward contract at any time _t <T_ must be _V(t)_ the value of the replicating portfolio:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - e^{-r(T-t)}K_T">
</p>

- The short position value is then

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V(t) = e^{-r(T-T)}K_T - S(T)">
</p>

- In particular, the value of the forward contract today is _V(0)_. The forward price <img src="https://render.githubusercontent.com/render/math?math=K_{\tau}"> is set so that the value of the forward contract today is 0, ie by setting _V(0) = 0._

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(0) = S(0) - e^{-r(T-0)}K_T = 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S(0) = e^{-rT}K_T"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T = e^{rT}S(0)"><br>
</p>

  giving the forward price.
  
### Summary:
- The value of the long position in a forward contract at time _t_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V(t) = S(t) - e^{-r(T-t)}K_T">
</p>

- The value of the short position at tie _t_ is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V(t) = e^{-r(T-T)}K_T - S(T)">
</p>

- The forward price is (assuming we contract at time _t_ =0)
- 
<p align="center">
 <img src="https://render.githubusercontent.com/render/math?math=K_T = e^{rT}S(0)"><br>
</p>

