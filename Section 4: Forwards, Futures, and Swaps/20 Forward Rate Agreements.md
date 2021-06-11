# Forward Rate Agreements
A __forward rate agreement__ or __FRA__ is a contract that mandates that a certain principal amount can be either borrowed or lent over some term in the future at an interest rate agreed upon at origination. It is similar to a forward contract on a CD (Certificate of Deposit), but is probably best thought of as a contract that locks in a future interest rate. FRAs are cash settled OTC products, and as a result, we can reduce their payout details even more. We will analyze FRA contracts from a perspective that is similar to forward contracts.

First we consider the economics of the FRA from the borrower's perspective, whose position is closet to the buyer or long in a general forward contract. The underying asset the borrower acquires is the right to borrow money at some future date, and the contracted price is the interest rate agreed to. 
- Denote the contracted rate by _K_, and the contracted principal by _N._
- Supposing the loan term is from times <img src="https://render.githubusercontent.com/render/math?math=T_1\:\:TO\:\:T_2">, the borrower is agreeing to pay on date <img src="https://render.githubusercontent.com/render/math?math=T_2"> total interest

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K \times (T_2 - T_1) \times N">
</p>

- The economic value of the FRA contact, at expiration, is the difference between the market value of the asset at expiration and the contracted price.
- If <img src="https://render.githubusercontent.com/render/math?math=L(T_1, T_2)"> is the spot LIBOR rate on the expiration date, the market value of the "asset" (the right to borrow money) is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L(T_1, T_2) \times (T_2-T_1) \times N">
</p>

- For instance, after borrowing at the contracted rate _K_, the borrower could immediately lend the money at market rates and receive this amount in revenue. Thus, the payoff for thr borrower is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L(T_1, T_2) \times (T_2-T_1) \times N - K \times (T_2 - T_1) \times N"><br>
<img src="https://render.githubusercontent.com/render/math?math=(T_2-T_1)N (L(T_1, T_2) - K)"><br>
</p>

- In essence the borrower is trading a fixed interest payment for a floating interest payment. For the lender, it is opposite, a floating payment is being traded for a fixed payment.
- In practice, FRAs are cash settled, and no borrowing takes place. The counterparties simply exchange the interest payments implicit in the contract payoff. As described, the exchange would take place at the maturity of the hypothetical loan, <img src="https://render.githubusercontent.com/render/math?math=T_2">, but in real FRA, the exchange happens at contract expiration, <img src="https://render.githubusercontent.com/render/math?math=T_1">
- Thus, what is exchanged on date <img src="https://render.githubusercontent.com/render/math?math=T_1"> is the discounted value. This, on <img src="https://render.githubusercontent.com/render/math?math=T_1"> the borrwer's account is credited

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{(T_2-T_1)N (L(T_1, T_2) - K)}{1 %2B (T_2 - T_1)L(T_1, T_2)}">
</p>

- Thus lender then receives the negative of this on date <img src="https://render.githubusercontent.com/render/math?math=T_1"> :

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{(T_2-T_1)N (K - L(T_1, T_2))}{1 %2B (T_2 - T_1)L(T_1, T_2)}">
</p>

- NOTE: The purpose of an FRA is not to borrow or lend money. It is to control interest rate exposure and risk.

### Example
Suppose I enter into an FRA, expiring in 1 year, on a 3 month loan with a $5 Million dollar principal, for a contracted interest rate of 3%, as the lender. If, on the expiration date, the 3 month spot LIBOR rate is 2.1%, how much will I receive (or have to pay) as a counterparty in the FRA?

- We have a contracted rate of _K_ = 3%
- The realized spot LIBOR rate for a 3 month loan is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L(1, 1.25) = 0.021">
</p>

- Payoff for borrrower
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{(T_2-T_1)N (L(T_1, T_2) - K)}{1 %2B (T_2 - T_1)L(T_1, T_2)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\frac{(0.25)(5000000) (0.021 - 0.03)}{1 %2B (0.25)(0.021)} = -11191"><br>
</p>

- Payoff for lender
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{(T_2-T_1)N (K - L(T_1, T_2))}{1 %2B (T_2 - T_1)L(T_1, T_2)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\frac{(0.25)(5000000) (0.03 - 0.021)}{1 %2B (0.25)(0.021)} = 11191"><br>
</p>
