# Futures Contracts and Cash Exposures
Futures prices are strongly linked to the spot prices of their underlying assets. The ultimate ramification: one may obtain exposure to the cash market by taking on futures positions. In this lecture we make the simplifying assumption that the cost of carry is 0: _c = 0_. Then 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t) = S(t)">
</p>

Thus , taking a position in futures results in direct exposure to the underlying price. For futures contracts, this exposure has an immediate impact, due to the marking to market mechanism. On the day after we enter into a long futures position, the value of our position changes by 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) - K_T(t_1) = S(t_2) - S(t_1)">
</p>

per unit. If the contract size is _C_ units,  and if we hold _J_ contracts, then the monetary change in our position value scales up:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=JC(K_T(t_2) - K_T(t_1)) = JC(S(t_2) - S(t_1))">
</p>
 
Day by day, the marking to market mechnaism ensures that we will continue to be exposed to these changes in the cash price. These are the exact same P&Ls (profit and loss) an outright long position (ie outright ownership) in _JC_ units of the underlying would expose us to. A short position in _J_ contracts would expose us to a similar, but reversed, sequence of P&Ls.

__The main import:__
We can realize the same exposure to the underlying asset, and its cash market price, using futures contracts as we could with an outright cash position.
