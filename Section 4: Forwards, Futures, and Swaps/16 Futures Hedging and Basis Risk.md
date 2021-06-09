# Futures Hedging and Basis Risk
Basis is the difference between spot and futures prices. The _basis_ for _T_-expiring futures is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=b(t) = b_T(t) = Basis = S(t) - K_T(t)">
</p>

- Previously we set the cost of carry to _0_. This implied that <img src="https://render.githubusercontent.com/render/math?math=S(t) = K_T(t)"> and thus tha basis was 0. More realistically, if <img src="https://render.githubusercontent.com/render/math?math=c \neq 0">, we have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = e^{c(T-t)}S(t)">
</p>

- We would have 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=b(t) = S(t) - e^{c(T-t)}S(t) = (1 - e^{c(T-t)})S(t)">
</p>

- To breakdown the basis, apply Taylor approximation (error small if c is small or for short dated contracts)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=e^{c(T-t)} = 1 %2B c(T-t) %2B error">
</p>

- Then we may write the basis

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=b(t) = = [1 - (1 %2B c(T-t)]S(t) = -c(T-t)S(t)">
</p>

- To break this down further we consider the special cose of a commodity. The basis concept is especially important for commodities. The analysis is instructuve for other asset classes.
- For a commodity _c = r + s - y_ with _r_ = interest rate, _s- = storage cost, _y_ =  convenience yield. Thus

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=b(t) = -r(T-t)S(t) -s(T-t)S(t) %2B y(T-t)S(t)"><br>
  <img src="https://render.githubusercontent.com/render/math?math== finance \:\:%2B\:\:storage\:\:%2B\:\:convenience"><br>
</p>

- In the real world the arbitrage relationship (below) only holds approximately. It will fluctuate around this base level, influenced by supply and demand forces. Thus the basis should be regarded as a price differential with a base level determined by the cost of carry, about which there will be supply and demand driven fluctuations, mediated by the activities of arbitrageurs.
 
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = e^{c(T-t)}S(t)">
</p>

- Based on these general considerations, we may adopt a theory of the forces that determine the basis. We note that some of these are locally determined and vary geographically. This indicates that the spot price will also vary geographically. For commodities futures the main factors influencing the basis are:
  - Interest charges
  - Local storage and transportation costs
  - Locally determined convenience yields
  - Supply and demand driven fluctuations.

- Similar analysis are possible for other asset classes

## Futures hedging in presence of nonzero basis
- Suppose we have a long position in _N_ units of an asset hedged with a short futures positions in _N_ units, and denote the value of our combined position as _W(t)_. From time <img src="https://render.githubusercontent.com/render/math?math=t_1\:\:to\:\:t_2"> our position's value change is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Delta W(t) = \Delta [Cash\:\:Value] %2B \Delta[Futures\:\:Value]"><br>
  <img src="https://render.githubusercontent.com/render/math?math== N\Delta S - N\Delta K_T"><br>
  <img src="https://render.githubusercontent.com/render/math?math==N(S(t_2) - S(t_1)) - N(K_T(t_2) - K_T(t1))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== N(S(t_2) - K_T(t_2))- N(S(t_1) - K_T(t1))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== Nb(t_2)- Nb(t_1)"><br>
  <img src="https://render.githubusercontent.com/render/math?math== N(b(t_2)- b(t_1))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== Position\:\:Size\:\:\times\:\:Basis\:\:Change"><br>
</p>

- So in the case of a unitary hedge, ie a hedge where one purchases an amount of futures contracts to offset the cash position completely, price risk is replaced with basis risk. This is a good tradeoff from a risk management point of view because basis risk is much smaller than price risk. 
- Perfect hedges are not usually possible due to the price complexities of real world markets, like the existence of a futures basis. But futures hedging is still an effective tool for controlling and reducing risk.

