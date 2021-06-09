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
- There is one further property of futures prices, a special case of (1). It is justified by an independent arbitrage arguement which is valid for futures contracts. As _t_ approaches the expiration date, the futures and spot prices come together. 
- The futures price must converge to the spot price as the expiration date is approached. During the delivery month, the futures price must equal (or be very close to) the spot price, Mathematically: <img src="https://render.githubusercontent.com/render/math?math=K_T(T) = S(T)">

- __Case 1:__ Suppose during the expiration month that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(T) \gt S(T)">
</p>

- An arbitrage can be realized by:

  - taking the short position in the futures contract.
  - purchasing the underlying
  - immediately making delivery
  - These actions realize an arbitrage profit of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(T) - S(T) \gt 0">
</p>

- __Case 2:__ Suppose during the expiration month that

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(T) \lt S(T)">
</p>

- An arbitrage can be realized by:

  - taking the long position in the futures contract.
  - purchasing the underlying at the futures price at delivery
  - immediately selling underlying on the spot market
  - These actions realize an arbitrage profit of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(T) - K_T(T) \gt 0">
</p>

- So at the expiration date of the contract we have <img src="https://render.githubusercontent.com/render/math?math=K_T(T) = S(T)">
- Then for times _t < T_ we expect that as _t_ approached _T_ that <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> and _S(t)_ should approach each other. This is approximately what is observed in markets. In general, there are deviations from it in different local cash markets. This is what is meant by futures basis.

## Summary:
The futures price is linked to the spot price.
- The arbitrage relation can be expected to hold, to some approximate degree, in most markets.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = e^{c(T-t)}S(t)">
</p>

- The convergence of futures to spot holds to within the basis

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(T) = S(T)">
</p>

- __Remark:__ Note the critical role the delivery process for these results.
