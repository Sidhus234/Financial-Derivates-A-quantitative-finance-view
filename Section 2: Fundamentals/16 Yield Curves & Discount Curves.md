# Yield Curves:
- __Yield Curve__ quantifies the relationship between return of a fixed income security and term or maturity, the term structure of interest rates.
- Explicitly it is a function which evaluates to the yield or return or interest rate earned on an instrument as a function of its maturity.
- On any single yield curve the different instruments should be "equivalent" and only differ by the maturity.
- Roughly speaking, "equivalent" means the instruments have the same credit quality.
- For instance: it would not make sense to have a yield curve which gave yields on US Treasury bonds for some maturities and yields on highly distressed corporate bonds for others.

<img src="../Images/S2 - Typical Yield curve.PNG" alt="Typical Yield curve"/>

- If we had a set of US Treasury bonds for a continuum of maturities _T_ over some range, say for years 0 < _T_ < 30 years, and _y(T)_ is the yield or return a bond holder would earn on the bond that matures in _T_ years.
- The obvious problem with this idea: there do not exist bonds (or any other traded instruments) for a continuum of maturities.


# Discount Curves:
- A primary application of yield curves in finance is to produce discount curves.
- A __discount curve__ is a function _d(T)_ which for any _T_ is a discount factor corresponding to discounting back from time _T_.
- A special kind of yield curve is a spot rate curve. If _y(T)_ is a yield curve, and a discount curve is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(T) = e^{-y(T)T}">
</p>

- then _y(T)_ is a (continuously compounded) __spot rate curve__.
- This is the formula for the discount factor for a continuously compounded interest rate _y(T)_ but here the relation holds for a continuum of values _T_.
- For an arbitrary term _T_, _d(T)_ is the present value, today, of $1 paid at time _T_
- Equivalently, define a spot rate _y(T)_ as the interest rate an issuer of a particular credit quality could negotiate for a loan with a term _T_ - even if there is not presently any such instrument trading on the markets.
- The spot rate curve would then be related to the discount curve by the relation

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(T) = e^{-y(T)T}">
</p>

- Or by inversion, given a discount curve _d(T)_, we can define the corresponding spot rate curve by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T) = - \frac{log(d(T))}{T}">
</p>


## How Yield Curve is built
- Suppose we have a set of _N_ traded fixed income securities, with maturities <img src="https://render.githubusercontent.com/render/math?math=T_1, T_2, ... T_N">. 
- From their market prices, we are able to compute yields

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T_1), y(T_2), y(T_3), .... , y(T_N)">
</p>

- The times <img src="https://render.githubusercontent.com/render/math?math=T_i"> are called __tenors__ and are usually maturities or expiration dates of the traded calibration instruments. 
- To extend the yield curve from the finite set of tenors to an entire interal <img src="https://render.githubusercontent.com/render/math?math=T[T_1, T_N]">, we carry out some kind of interpolation procedure. 

<img src="../Images/S2 - Market observed yields for traded instruments.PNG" alt="Market observed yields for traded instruments"/>

## Examples:
- Two primary example sof spot rate curves are what are known as government spot rate curves and the LIBOR curve. 
- Government spot rate curves are constructed from the yields on government bonds.
- The LIBOR curve is a spot rate curve built from money market rates: LIBOR rates, interest rate futures, and swaps.
- __Remark:__ There are many kinds of yield curves besides spot rate curves. For instance, the US Treasury yield curve is constructed using yields to maturity, and is not a spot rate curve.

