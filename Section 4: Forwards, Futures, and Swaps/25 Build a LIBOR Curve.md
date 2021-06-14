# Building a LIBOR Curve
Bootstrapping a LIBOR curve. LIBOR curve is a spot rate curve based on inputs from money market instruments. 
- We use cash LIBOR rates for tenors up to 3 months. We may compute discount factors directly from these rates and from the discount factors can compute the spot rates.
- For tenors between 3 months and about 2 to 5 years we use forward LIBOR rates derived from Eurodollar futures rates. 
- For the rest of the curve, we use market swap rates. We use the pricing formula for swaps to back out the discount factors and hence the spot rates.

## Example: 
Assuming the followung market rates, build the LIBOR curve.

<img src="../Images/S4_LIBOR_RATE_example.PNG" alt="LIBOR Rate example"/>

### Building the short end of LIBOR curve: Cash LIBOR rates
It is customary to use LIBOR interest rates directly to build the LIBOR curve for tenors up to 3 months. We are given cash LIBOR rates for 1, 2, and 3 months as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L\big(\frac{1}{12}\big) = 0.008"><br>
  <img src="https://render.githubusercontent.com/render/math?math=L\big(\frac{2}{12}\big) = 0.01"><br>
  <img src="https://render.githubusercontent.com/render/math?math=L\big(\frac{3}{12}\big) = 0.013"><br>
</p>

Recall that LIBOR rates are simply compounded rates. SO the relationship between LIBOR rates and discount factors is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P(0, T) = \frac{1}{1 %2B TL(T)}">
</p>

The bond prices/discount factors are thus:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P\big(0, \frac{1}{12}\big) = \frac{1}{1 %2B \frac{1}{12}(0.008)} = 0.99933"><br>
<img src="https://render.githubusercontent.com/render/math?math=P\big(0, \frac{2}{12}\big) = \frac{1}{1 %2B \frac{2}{12}(0.01)} = 0.99834"><br>
<img src="https://render.githubusercontent.com/render/math?math=P\big(0, \frac{3}{12}\big) = \frac{1}{1 %2B \frac{3}{12}(0.013)} = 0.99676">
</p>

For very short tenors, keep 5 to 6 digits of precision (as interest rates are very close to 1). From discount factors, spot rates <img src="https://render.githubusercontent.com/render/math?math=y(T_i)"> can be determined by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T_i) = -\frac{\log{(P(0, T_i))}}{T_i}">  
</p>

Thus, from the above computed discount factors, we may compute spot rates:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y\big(\frac{1}{12}\big) = -\frac{\log{0.99933}}{\frac{1}{12}} = 0.00804"><br>
<img src="https://render.githubusercontent.com/render/math?math=y\big(\frac{2}{12}\big) = -\frac{\log{0.99834}}{\frac{2}{12}} = 0.009968"><br>
<img src="https://render.githubusercontent.com/render/math?math=y\big(\frac{3}{12}\big) = -\frac{\log{0.99676}}{\frac{3}{12}} = 0.01298">
  </p>
  
 ### Building the Midrange of LIBOR curve: Eurodolar futures
 __The middle: Eurodollar futures.__ It is appropriate to use forward LIBOR rates to extend the LIBOR curve further. For this, we should use FRAs.
But as OTC contracts, FRAs are not transparent and not sufficiently liquid to use for curve building. 
So it is customary to use Eurodollar futures rates instead, which are amongst the most liquid futures contracts in the flobal capital markets. 
This could be compensated for using a convexity adjustment. In practice, it is usally acceptable to substitute the futures rates for forward rates.
Recall the forward price for a _T_-forward bond maturing at <img src="https://render.githubusercontent.com/render/math?math=T %2B \tau"> is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{P(0, T %2B \tau}{P(0, T)} = \frac{1}{1 %2B \tau L(0, T, T %2B \tau)}">
</p>

Here _L_ is the forward LIBOR rate. We substitute the futures rate, 
