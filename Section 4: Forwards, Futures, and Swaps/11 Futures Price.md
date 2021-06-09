# Futures Prices
- The futures price associated with a futures contract is the contracte dprice.
- We done by <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> the futures price for a contract originated at time _t_ and expiring at time _T_.
- Like forward prices, <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> is the contract price that makes a futures contract entered at time _t_ have 0 value.
- <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> are prices negotiated on futures markets, the outcome of supply and demand forces on futures markets.
- Thus the notation <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> does not denote the price contracted in any particular futures contract. It represents a market price observed on markets at time _t_. It is market's assessment of the fair futures price for contract originated at time _t_ and expiring at time _T_.
- Clearly the forces acting on futures markets are linked to activity on the underlying cash market.
- At base level, futures are expected to represent market expectations of future spot prices.
- One quantitative implementation of this principle is espressed as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = E(S(T)|\mathcal{F}_t)\:\:\:\:(1)">
</p>
  where the notation <img src="https://render.githubusercontent.com/render/math?math=E(.|\mathcal{F}_t)"> represents an expectation conditional on the knowledge available at time _t_.
  
- This principle is justified by arbitrage considerations: if the futures price systematically underestimated or overestimated the spot price at expiration, arbitrage oppurtunities would exist by taking an appropriate futures position and holding until expiry.
- If we interpret equation (1) as stating that the futures price is an unbiased estimator of future spot prices, this is, empirically, rarely observed in practice.
- It is standard to attribute deviation from (1) to the existence of a risk premium. Hedgers are willing to pay for the price protection afforded by locking in a future price by accepting a less favorable futures price.
- This may lead to either over or under estimates of the future spot price depending on whether hedgers are net long or short.
- The consensus view in finance is that these are the primary market forces influencing futures prices: expectations of future spot prices and risk premia.
- __Remark:__ The futures price <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> will generally be the price of some natural unit of the underlying. This is not necessarily the same as the contract size-usually it isn't. Eg. For a crude oil futures contract, the natural unit is 1 barrel of oil, and the quoted futures price <img src="https://render.githubusercontent.com/render/math?math=K_T(t)"> will be for 1 barrel of oil. But the contract size for NYMEX oil futures is 1000 barrels. Thus working with a concrete example of an actual futures position, we must multiply by the contract size and the number of contracts.


# Forward and Futures Prices: 
Although the basic financial structure of forwards and futures are the same, the institutional differences between them are impactful enough that their prices will diverge. Consider a forward contract on some underlying asset, contracted at time _t_, expiring at time _T_. Let the contracted forward price be <img src="https://render.githubusercontent.com/render/math?math=F_T(t)">. Both the forward and futures contracts are agreements to trade the underlying asset at time _T_ for the contracted price. Why isn't <img src="https://render.githubusercontent.com/render/math?math=K_T(t) = F_T(t)">?

It is because of the differences in the ways forwards and futures markets function and how they are administered. Forward prices are negotiated on OTC markets, which operate as "shop around" markets. Price transparency is comparatively weak on OTC markets. In contract, futures prices are negotiated on exchanges, where there is absolute price transparency. Another difference: counterparty credit risk is a significant concern for forward contracts but is effectively a nonissue for futures. After a futures contract is negotiated between two counterparties and originated, the exchange immediately steps into the role of counterparty to both the long and the short, thus ensuring that the obligations will be met.

The most important difference of all: futures position are __marked to market__, or settled up, every day. In a forward contract there are no cashflows between the counterparties until the expiration of the contract. In contrast, in a futures contract the counterparties settle up on a daily basis, resulting in cash flows back and forth between the counterparties daily. The marking to market process for futures will be treated in the following lectures. In practice, in most markets, futures prices usually do not deviate far from forward prices. This is due, in part, to the fact that the same arbitrage forces are at work in futures markets as forward markets.



