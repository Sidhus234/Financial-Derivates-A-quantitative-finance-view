A __Eurodollar Futures__ contract is a futures contract, traded on exchanges such as the Chicago Mercantile Exchange which can be thought of as a futures version of an FRA.
An interest rate derivative, e Eurodollar futures is closely linked witht eh 3 month spot LIBOR rate.
It is designed to mimic (to some approximate degree) a futures contract with a 3 month LIBOR CD as the underlying asset.
The main use of Eurodollar futures contracts is to hedge interest rate exposure, as is the case for all interest rate derivatives.
More specifically: the Eurodollar futures contract is designed to approximate a futures with underlying a $1,000,000 3 month LIBOR deposit. But this is something of a convenient fiction. The exact specifications of a Eurodollar futures contract are as follows:
- The contrac price is defined to be 100 minus the contracted futures interest rate.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = 100(1 - F(t, T, T %2B 0.25))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== 100 - Futures\:\:Rate\:\:as\:\:Percentage\:\:"><br>
</p>

- The linkage to the LIBOR curve is through the specified delivery condition. On the expiraition date _T_, the price of a Eurodollars futures is quoted as


<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = 100(1 - L(T, T, T %2B 0.25))"><br>
  <img src="https://render.githubusercontent.com/render/math?math== 100 - 3  month\:\:LIBOR\:\:on\:\:date\:\:T"><br>
</p>

- This delivery condition is a specification of the contract, and links the futures rate _F(t, T, T + 0.25)_ to LIBOR.

__NOTE:__ that "buying the contract" implies you are short interest rates, and "selling the contract" means you are long interest rates. "Buying" and "Selling" are just terms of convenience. The interest rate exposure is the whole point. And the price quoting mechanism is just a way to quote the futures rate, which is the essential datum.

The contract size is defined such that a 1 bps (=0.01% = 0.0001) change in the contracted rate implies a $25 change in the value of the contract. This is alos a contract specification. This is numerically equivalent to an underlying asset a $1,000,000 3 month deposit - assuming 3 months = 1/4 year.

From date _t_ to date _t+1_ the change in the mark to market of a long position on a Eurodollar futures is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\big((1000000) ( 1 %2B 0.25F(t %2B 1, T, T %2B 0.25))\big) - \big((1000000) ( 1 %2B 0.25F(t %2B 1, T, T %2B 0.25))\big)"><br>
<img src="https://render.githubusercontent.com/render/math?math=(1000000) (0.25) \times [F(t %2B 1, T, T%2B 0.25) - F(t, T, t %2B 0.25)]">
</p>

One may confirm from this formula that if the futures rate _F_ changes by 1 bps (=0.0001) the value of either position changes by $25 (1000000 x 0.25 x 0.0001 = 25).
For the contract buyer, who is short interest rates, a 1 bps increase in the futures rate implies a $25 loss in the position. For the seller, who is long interest rates, a 1 bps increase in the futures rate implies a $25 gain in the position. As a futures contract, trading on an exchange, Eurodollar futures are marked to market daily.

The delivery requirements of the contract are that it is cash settled with the futures price on the final trading day set to 100 minus the 3 month spot LIBOR rate on that date. Cash settlement plus marking to market means that "delivery" on the final date simply consists of one last marking to market on the last day.

### Example 1:
Suppose you have a Eurodollar futures contract with a price of 98.1 today, and suppose tomorrow the price declined to 97.8. What were the futures rates on these days?

To find the implied futures rate, in percentage terms, one can just subtract the price from 100.
- Rate Today = 100 - 98.1 = 1.9%
- Rate Tomorrow = 100 - 97.8 = 2.2%

### Example 2:
In the example considered previously, what would happen to the margin account of an investor who has sold a futures contract.

The contract seller profits when the futures interest rate increases and suffers a loss when the rate declines. The over day changes in the futures rate is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=F(t %2B 1, T, T, %2B 0.25) - F(t, T, t %2B 0.25) = 0.022 - 0.019 = 0.003">
</p>

The seller's position thus profits by (1000000) x 0.25 x 0.003 = $750. Hence, $750 will be deposited in his margin account.
