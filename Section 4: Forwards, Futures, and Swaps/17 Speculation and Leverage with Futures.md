# Speculation and Leverage with Futures
 Futures can be used for risk management activities. It can also be used for speculation.
 - In risk management, a market participant uses the future position to offset, and thus reduce, an exposure he already has in an existing portfolio. The purpose is to reduce risk.
 - A speculator's intent, on the other hand,is to obtain an exposure she does not already have. SO in contract to risk management, the purpose is to increase risk.
 - If an investor wants to have a long exposure to crude oil (because she expects the price to risk), there are at least 2 ways to do this:
  - Take the outright long position in the cash market (estentially buy oil)
  - Take a long futures position.

- The futures position provides the same exposure to the underlying price as the equivalent cash position. There are often many advantages to obtaining this exposure in futures markets rather than in the cash market. 
  - Futures markets are often much more liquid than cash markets
  - For commodities, there are considerable costs and logistical complications to taking cash positions, such as storage, insurance, and transportation.
  - Probably the biggest advantage of all is leverage futures provide.

## __Leverage:__ 
- __Leverage__ refers to the possibility for an investor to obtain a much larger exposure on the financial markets than the funds she invests. 
- Leverage is often thought of to mean borrowing. Margin accounts on the cash equity market are like this.
- Futures contracts provide a different form of leverage. An investor can take a futures position with only enough funds to satisfy the margin requirements.
- By posting margin, and investor can obtain an exposure on the underlying market with, typically 5-10% of the funds that would be required for the same exposiure on the cash market.
- Eg. Suppose you want to speculate on the crude oil market. One way to do this is to take a cash position. If one wanted the exposure of 1000 barrels of crude, with crude oil trading at $65/barrel, one would need to invest $65000 to realize this exposure. If instead, one took a long position in 1 NYMEX WTI futures contract (contract size 1000 barrels) one would need to post the margin, about $3000. In the futures market, an initial investment of $3000 realizes the same exposure to the crude oil market as investing $65000 in the cash market.

## Futures Speculating Example
Suppose you want to take a long speculative position on Japanese Yen. you want to go long 25 million Yen. The CME JPY/USD futures contract hasa contract size of 12.5 million yen. You are weighing the 2 possibilities of attaining this exposure through a cash position or by taking a long position in 2 futures contracts. Suppose the current JPY/USD rate is _S(0)_ =0.009 and the current futures rate is _K(0)_ = 0.0090895 for a 3 month contract. Also suppose that the initial margin requirements are $4000 per contract. Compare the 2 strategies. Consider further what happens if in 2 months later the spot rate has increased to _S(T)_ = 0.0097 and the futures rate has increased to _K(t)_ = 0.00970035.

__Case 1:__ Long Cash Position
- The long cash position requires the purchase of 25 million yen. Cost (0.009)(25,000,000) = $225,000
- Using the given data, the cash position has progfited by: (25,000,000) (0.0097 - 0.009) = $17,500
- Net return on cash position is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{17500}{225000} = 0.0778">
</p>


__Case 2:__ Long Futures position
- The futures position is for a long posiiton in 2 contracts, so the initial margin which must be posted is 2 x $4000 = $8000
- The futures position has profited by: (25,000,000) (0.00970035 - 0.00900895) = $17,486
- Net return on futures position is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{17486}{8000} = 2.19">
</p>

From the point of view of net return, the futures strategy is clear winner!. This is however, very misleading, because it completely ignores the risk in the futures position. If the JPY/USD had moved down as much as it moved up in this example, your initial investment would have been completely wiped out. Even with the final result give, many losses in Yen on the way there may have foreced you, through margin calls, to deposit vastly more cash than the initial investment. Nevertheless, the advantages , for a speculator, of the leverage offered by futures positions is clear.
