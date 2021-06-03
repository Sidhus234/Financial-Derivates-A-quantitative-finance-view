# Bootstrapping Spot Curves from Bonds
- Bootstrapping is the main technique forbuilding a yield curve from real market data.
- We assume we have a collection of _N_ bonds with maturities

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=T_1 < T_2 < T_3 < \cdots < T_N">
</p>

  and observable markets prices <img src="https://render.githubusercontent.com/render/math?math=P_1 < P_2 < P_3 < \cdots < P_N">.
- We first choose _d(T)_ for <img src="https://render.githubusercontent.com/render/math?math=T \le T_1"> to discount the coupons of bond 1 and recover <img src="https://render.githubusercontent.com/render/math?math=P_1">
- We then choose _d(T)_ for <img src="https://render.githubusercontent.com/render/math?math=T_1 \le T \le T_2"> s.t. together with the values already chosen for <img src="https://render.githubusercontent.com/render/math?math=T \le T_1">  we recover <img src="https://render.githubusercontent.com/render/math?math=P_2"> for bond2.
- We continue through all _N_ bonds until we have a discount factor _d(T)_ for <img src="https://render.githubusercontent.com/render/math?math=T \le T_N">.

## Example
- __Bond 1:__ A zero coupon bond with a $1000 face value maturing in 6 months.
- __Bond 2:__ A bond with a 5% coupon, with semiannual payments, a $10,000 face value, and  maturing in 1 year.
- __Bond 3:__ A bond with a 7% coupon, with annual payments, a $10,000 face valuue and maturing in 2 years.
- And we suppose the bonds are currently trading at prices:

<p align="left">
  <ol>
    <li><img src="https://render.githubusercontent.com/render/math?math=P_1 = 985"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=P_2 = 10124"></li>
    <li><img src="https://render.githubusercontent.com/render/math?math=P_3 = 10507"></li>
    </ol>
  </p>
  
  - For these bonds, since we have 3 prices, we will be able to bootstrap the yield curve at 3 tenors, the maturities of the 3 bonds:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=T_1 = 0.5, T_2 = 1, T_3 = 2">
</p>

- The bond prices allow us to calibrate the dicount factors <img src="https://render.githubusercontent.com/render/math?math=d(T_1), d(T_2), d(T_3)">, or , equivalently, the yields <img src="https://render.githubusercontent.com/render/math?math=y(T_1), y(T_2), y(T_3)">
- Using bond 1, we will calculate the first discount factor. As bond 1 is a pure discount bond, we must have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_1 = d(0.5)(1000)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=d(0.5) = \frac{P_1}{1000} = \frac{985}{1000} = 0.985">
</p>

- From discount factor, we can compute the yield _y(0.5)_ from the general relationship

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(T) = - \frac{log(d(T))}{T}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Y(0.5) = -\frac{log(0.985)}{0.5} = 0.030">
</p>

- Bond 2 involves a payment in 6 months (time 0.5) and a payment in 1 year.
- We can use the discount factor we have so far _d(0.5)_ to discount the coupon payment in 6 months, and then use the bond price to calibrate the discoint factor _d(1)_.
- This leads to the calculation:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_2 = d(0.5)(250) + d(1)(10250)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=d(1) = \frac{P_2 - d(0.5) \times 250}{10250} = \frac{10124 - 0.985 \times 250}{10250} = 0.9637">
</p>

- We may now solve the yield _y(1)_ as for _y(0.5)_

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(1) = - \frac{log(0.9637}{1} = 0.037"><br>
</p>

- Finally we use bond 3 to determine the discount factor _d(2)_

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P_3 = d(1)(700) + d(2)(10700)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=d(2) = \frac{P_3 - d(1) \times 700}{10700} = \frac{10507 - 0.9637 \times 700}{10700} = 0.9189">
</p>

- We may now solve the yield _y(2)_ 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(2) = - \frac{log(0.9189}{2} = 0.042"><br>
</p>

- Based on 3 points, we plot and extrapolate to get values for points in between. There are many possible methods for building a yield curve. The piecewise linear method is the simplest and, in practice, is the default method.
- Whichever interpolation method is used, the result is a continuous function defined over a range of maturities.
- The resulting yield curve may now be used to produce discount factors, price bonds etc.

<img src="../Images/S2-Bootstrapping linear interpolation.PNG" alt="Linear Interpolation of Yield curve"/>


### Example
- Using the constructed yield curve, compute the discount factors _d(0.5)_, _d(1)_, and _d(2)_. Price a 2 year bond with a $100,000 face value with a 7% coupon semiannualy.

  - In the construction process for the yield curve, we have already calculated _d(0.5), d(1), d(2)_. They are
  <ol>
  <li> d(0.5) = 0.985)</li>
  <li> d(1) = 0.9637</li>
  <li> d(2) = 0.9189</li>
  </ol>

  - This leaves only the discount factor d(1.5) still to calculate.
  - We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(1.5) = e^{-y(1.5) (1.5)}"><br>
</p>

  - The yield _y(1.5)_ must be calculated from interpolation of the values _y(1)_ and _y(2)_. We have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=y(1.5) = \frac{y(1) %2B y(2)}{2} = \farc{0.037 %2B 0.042}{2} = 0.0395">
</p>

  - Thus the discount factor is
 
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(1.5) = e^{-0.0395 \times 1.5} = 0.942"><br>
</p>

  - Pricing the bond is now a matter of applying the discount factors we have computed. The bond makes a $3500 coupon payment in eachof the 6 months, 1 year and 1.5 years, and make a final coupon payment together with $100,000 face value in 2 years. The price is therefore

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=P = d(0.5)\times c(0.5) %2B d(1)\times c(1) %2B d(1.5)\times c(1.5) %2B d(2)\times c(2)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=P = 0.985\times 3500 %2B 0.9637\times 3500 %2B 0.942\times 3500 %2B 0.9189\times 103500 = 105224">
</p>
