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
