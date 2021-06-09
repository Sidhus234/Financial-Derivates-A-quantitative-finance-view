# Futures Prices and Spot Prices
- The central distrinction between forward contracts and futures contracts:
  - The long positionin a forward contract is the right, and obligation, to receive at the expiration date _S(T) - K_. "Obligation" emphasizes that, in the case where this payoff is negative, the long is obligated to pay. Thus the forward payoff may be regarded as a cashflow at expiry, with the implication that if it is negative, the long position holder must pay.
  - The long position in a futures contract is the right, and obligation, to receive the stream of cashflows on each successive day during the contract's life.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) - K_T(t_1),"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(t_3) - K_T(t_2),"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\cdots,"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(T) - K_T(t_{N-1}),"><br>
</p>

  - Since the vast majority of futures contracts are terminated before delivery, a futures positionis in effect a contract to receive, or pay, this sequence of daily cash flows, though one which can be terminated at any time.
  - This is mpt tje same thing as a forward where no money changes hands until expiry when the transaction takes place at the contracted forward price.
  - The cash and carry and replication arguements used to derive the forward price and forward contract value are invalid for marked to market futures positions.
  - Thus the results for forward prices and contract values do not, in principle, hold for futures.

- In practice, futures prices are close to forward prices in most markets. There are theoretical arguements that futures prices agree closely with forward prices under realistic assumptions.For example, if interest rates are constant, or uncorrelated with the underlying price, theoretical arbitrage arguements imply that forward and futures prices agree. Secondly, it is observed empirically that futures prices track spot prices in a manner consistent with relations of the form (where _c_ is the applicable cost of carry)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_t(T) = e^{c(T-t)}S(t) \:\:\:\:\:(1)">
</p>

__Remark:__ Relation (1) is an arbitrage relation not a statement of cause and effect. It does not mean that the spot price determines the futures price. It may be that forward prices are what drive the spot prices. This prevailing view for commodity markets.

### Convergence between Spot and Future Price

<img src="../Images/S4_ConvergingbetweenSpotFutreprice.PNG" alt="Converging between Spot and Future Prices"/>

- If the 2 prices deivate too far from it, arbitrage activity will bring them in alignment.
