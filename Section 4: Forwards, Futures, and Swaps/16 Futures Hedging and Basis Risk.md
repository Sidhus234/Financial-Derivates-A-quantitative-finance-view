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

## Example 1:
Suppose you run a US based exporting company. It is May, and you know you will be receiving a payment in November of 1 million Euros. How can you manage the risk of adverse moves in the EUR/USD exchange rate using futures? Suppose you take on a full, unitary hedge of your cash position using futures. Suppose the current spot EUR/USD rate is $1.15/Euro and the current futures rate on the December EUR/USD futures contract is $1.18/Euro. And suppose that in November, the spot rate is $1.02/Euro and the futures rate is $1.03/Euro. What is the gain or loss of the total position? Has the hedge been effective?

The CME EUR/USD futures contrat has a contract size of $125,000 Euro, and they are sold for the delivery month of December. You can take a short position on 8 EUR/USD contracts expiring in December to fully hedge your risk. 

- Now suppose you take this short position in EUR/USD futures. 
- From May to november, the cash position has declined from $1.15/Euro to $1.02/Euro. Therefore your long cash position in Euro has suffered a loss of (1,000,000) (1.15-1.02) = $130,000
- The futures basis in May is $1.15-$1.18 = -0.03 and in November the basis is $1.02-1.03 = -$0.01
- Therefore your combined position (long cash, short futures) has profited by $20000. tHE HEDGE HAS PROTECTED YOU FROM A LOSS OF $130000. It has been effective.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1000000)(-0.01 - (-0.03)) = 20000">
</p>


## Example 2:
It is April, and a copper miner, anticipating a volatile copper market, wants to hedge his price risk for the fall. He projects producing about 15,000 metric tons of copper in October and November and wants coverage for about 10,000 tons. The CME copper futures contract has a contract size of 25,000 pounds (about 11 metric tons) and trades for delivery in every month for the next year. How should the miner manage his price risk??

To cover 10,000 tons, he would need to take a short position in approximately 10,000/11, or about 900, contracts, expiring no earlier than December.

Suppose the miner decides to take ashort position in 900 copper futures contracts expiring in December. Suppose that the current spot price for copper is $3.05/pound and the futures price for the December contract is $3.11/pound. And suppose in November, when the miner has produced 16,000 tons of copper in the last 2 months, the spot price is #3.15 and the futures price is $3.16. How has the position fared?

- On the cash postion, the miner has gained. The cash price has increased from $3.05/pound to $3.15/pound, so the miner's cash position has profited by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=16000 \times 2204.62 \times (3.15 - 3.05) = 3527392">
</p>
  (NOTE: 1 metric ton = 2204.62 pounds)
  
- However, he has lost money on the futures position. the miner was short 900 contracts, and the futures price increased from $3.11 to #3.16

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=900 \times 25000 \times (3.16-3.11) = 1125000">
</p>

- So the futures position has dimished the miner's gain to $2,402,392

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=3527392 - 1125000 = 2402392">
</p>

- In general, when the cash market moves in a market participants favor, the effect of the futures hedge is to reduce the benefit. 
