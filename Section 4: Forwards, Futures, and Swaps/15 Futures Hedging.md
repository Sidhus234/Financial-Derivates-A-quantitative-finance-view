# Futures Hedging
__NOTE:__ assumption cost of carry _c_ = 0 and thus <img src="https://render.githubusercontent.com/render/math?math=K_T(t) = S(t)">

Suppose we have a long or short position in some asset, whose cash price per unit is _S(t)_ and we are long or short _N_ units. Eg. _S(t)_ could be the price per share of a company and we own _N_ shares, or _S(t)_ could be the price per barrel of crude oil and we are short _N_ barrels of oil. We can control price risk in the asset by hedging with futures due to the cash exposure that can be realized through futures. A long cash position can be hedged with a short futures position. The short cash exposure implicit in futures position offsets the long exposure in the cash position. Similarly, a short position in cash can be hedged or offset with a long futures position. If the contract size is _C_ units of the asset, then an equivalent position in futures can be built with

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=J = \frac{N}{C}">
</p>

contracts. Them we will hedge our outright position in _N_ units of the underlying by taking the opposite position in _J_ futures contracts (assume _J = N/C_ is an integer). If _J_ is not an integer we would use the smallest whole number of contracts greater than this. Throughout these notes we will assume _J_ is an integer. A futures position that fully hedges our cash position is called __unitary hedge__.

- Let _W(t)_ = value of the portfolio of the cash and futures positions for a unitarily hedged position. So if we are long cash (_N_ units) and short _J_ futures contracts.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W(t) = NS(t) %2B Short Futures Position Value">
</p>

- The 1 day change in the combined position value is:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta W(t) = \Delta Cash %2B \Delta Futures"><br>
  <img src="https://render.githubusercontent.com/render/math?math== N\Delta S(t) - JC\Delta K_T(t)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==N\Delta S(t) - N\Delta K_T(t)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==N(S(t_2) - S(t_1)) - N(K_T(t_2) - K_T(t_1))"><br>
  <img src="https://render.githubusercontent.com/render/math?math==N(S(t_2) - S(t_1)) - N(S(t_2) - S(t_1)) = 0"><br>
</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Longrightarrow Perfect\:\:\:Hedge">
</p>
