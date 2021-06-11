# Forward Rate Agreements Valuation
- The payoff in an FRA, to the borrower, at contract expiration <img src="https://render.githubusercontent.com/render/math?math=T_1"> is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{(T_2-T_1)N (L(T_1, T_2) - K)}{1 %2B (T_2 - T_1)L(T_1, T_2)}">
</p>

- This payoff, by design, is the discounted value of exchange of interest payments effectively made at time <img src="https://render.githubusercontent.com/render/math?math=T_2">. To find the fair value of an FRA, using arbitrage principles, it is sufficient to construct a portfolio replicating these effective <img src="https://render.githubusercontent.com/render/math?math=T_2"> payments.
- From the borrower's perspective, this time <img src="https://render.githubusercontent.com/render/math?math=T_2"> payoff is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=((T_2-T_1)\times N \times L(T_1, T_2)) - (K \times N \times (T_2 - T_1))">
</p>

- The payment <img src="https://render.githubusercontent.com/render/math?math=(T_2 - T_1)KN"> is a fized payment which may be replicated by borrowing its discounted value. This contributes a term of (below) to the replicating portfolio.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-P(t, T_2)(T_2 - T_1)KN">
</p>

- The floating lef of the payoff (below) is received by the borrower. It is based on the spot LIBRO rate <img src="https://render.githubusercontent.com/render/math?math=L(T_1, T_2)"> which is observed on date <img src="https://render.githubusercontent.com/render/math?math=T_1"> and is unknown at the time _t_.
- To replicate the floating portfolio cosider the following portfolio:
  <ol>
  <li>A long position in a zero coupon boond expiring at time <img src="https://render.githubusercontent.com/render/math?math=T_1"> with a face valeu of _N_.</li>
  <li>A short position in a zero coupon bond expiring at time <img src="https://render.githubusercontent.com/render/math?math=T_2"> with a face value of _N_. Note: "shorting" a bond means borrowing; that is, at time _t_ we borrow the discounted value of the face value _N_ witht he obligation to pay back _N_ at <img src="https://render.githubusercontent.com/render/math?math=T_2"></li>
  </ol>

- Assume we enter into ths portfolio at time _t_ and follow the followingg replication strategy.
  - At time <img src="https://render.githubusercontent.com/render/math?math=T_1">, bond 1 matures, and we will receive the face value, _N_ as payment.
  - Invest this sum at the prevailing spot LIBOR rate <img src="https://render.githubusercontent.com/render/math?math=L(T_1, T_2)"> from time <img src="https://render.githubusercontent.com/render/math?math=T_1"> to time <img src="https://render.githubusercontent.com/render/math?math=T_2">.
  - At time <img src="https://render.githubusercontent.com/render/math?math=T_2"> this investment matures, and pays out

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B (T_2 - T_1) L(T_1, T_2))N">
</p>

  - Also, at time <img src="https://render.githubusercontent.com/render/math?math=T_2"> bond 2 matures and we are obligated to pay the face value of _N_.
  - We pay this out of our LIBOR investment, leaving (below) exactly the floating payment in the FRA

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B (T_2 - T_1) L(T_1, T_2))N - N = (T_2 - T_1) L(T_1, T_2) N">
</p>

So our bond portfolio replicates the floating payment of the FRA. It follows that we can replicate the borrower's payoff in an FRA with the following portfolio: 
  - A long on a zero coupon bond, maturing at <img src="https://render.githubusercontent.com/render/math?math=T_1"> with a face value of _N_.
  - A short on a zero couponbond, maturing at <img src="https://render.githubusercontent.com/render/math?math=T_2"> with a face value of _N_.
  - A debt of <img src="https://render.githubusercontent.com/render/math?math=P(t, T_2)(T_2-T_1)KN">.

The cost to construct this portfolio at time _t_ must, by the Law of One Price, be the value of the borrower's position in the FRA. The price of the FRA, for the borrower, is thus

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{FRA}(t) = P(t, T_1)N - P(t, T_2)N - P(t, T_2)(T_2 - T_1)KN">
</p>

For the lender, simply take a negative of this value. 

The forward rate is the value of _K_ such that <img src="https://render.githubusercontent.com/render/math?math=V_{FRA}(t) = 0">. To find it, set the above expression to 0 and solve for _K_.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K = \frac{P(t, T_1) - P(t, T_2)}{(T_2 - T_1) P(t, T_2)}">
</p>

### Example
Suppose that the 5 year LIBOR spot rate is 3.5%, and the 6 year LIBOR spot rate is 4% (both simply compounded). What is the market value today of an FRA (from the borrower's perspective) for a 1 year term, expiring in 5 years, on a principal of $2,000,000 and with a contracted rate of 6%? If you were to enter into such a contract today, what contrat rate would set the contract value to 0 at origination?

We have
- 
