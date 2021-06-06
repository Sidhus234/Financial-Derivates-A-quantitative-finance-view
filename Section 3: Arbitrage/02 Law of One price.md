# Law of One Price:
- Let A and B be two assets, with prices <img src="https://render.githubusercontent.com/render/math?math=P_A(t)\:\:\: and \:\:\:P_B(t)"> at time _t_. 
- Suppose the probability <img src="https://render.githubusercontent.com/render/math?math=Prob(P_A(T) = P_B(T)) = 1"> for some time _T > 0_.
- In that case one of two things have to be true:
  - Either <img src="https://render.githubusercontent.com/render/math?math=P_A(0) = P_B(0)"> or;
  - There is an arbitrage

## Justification: (Proof - Law of One Price)
- Suppose <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \ne P_B(0)">
- __NOTE__ <img src="https://render.githubusercontent.com/render/math?math=P_A(0)\:\:and\:\:P_B(0)"> are not random, and are known deterministic prices at time _t = 0._
- This measn <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \gt P_B(0)\:\: or \:\: P_B(0) \gt \P_A(0)."> Suppose <img src="https://render.githubusercontent.com/render/math?math=P_A(0)\gtP_B(0)">
- To construct an arbitrage:
  - Short position in _A_. Borrowed _A_ and immediately sold it on market.
  - Long position in _B_. Buy it from market.

- This implies following cash flows:
  - Receive <img src="https://render.githubusercontent.com/render/math?math=P_A(0)">
  - Spent <img src="https://render.githubusercontent.com/render/math?math=P_B(0)">
  - Left with <img src="https://render.githubusercontent.com/render/math?math=P_A(0) - P_B(0) \gt 0"> (as by assumption <img src="https://render.githubusercontent.com/render/math?math=P_A(0) \gt P_B(0)">. This is invested at risk free rate for time _T_.

- Portfolio with following components:
  - 1. Short position in asset _A_ (with obligation to return to its rightful owner)
  - 2. Long position in asset _B_ (own _B_)
  - 3. Net cash invested at risk free rate <img src="https://render.githubusercontent.com/render/math?math=P_A(0) - P_B(0)"> for time _T_.

__NOTE:__ No cash was spent to build this portfolio.

- At time T to close out the position:
  - 1. Buy  _A_ at <img src="https://render.githubusercontent.com/render/math?math=P_A(T)"> and return to its rightful owner
  - 2. Sell _B_ at <img src="https://render.githubusercontent.com/render/math?math=P_B(T)">
  - Since cash from selling _B_ is used to buy _A_ as (<img src="https://render.githubusercontent.com/render/math?math=P_A(T) = P_B(T)">
  - 3. The net cash investment at risk free interest rate for time period _T_. This is riskless profit, and hence the portfolio was an arbitrage.
  - 4. The profit from the portfolio (Certain positive profit). This is an arbitrage.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(P_A(0) - P_B(0)) e^{rT} \gt 0">
</p>

