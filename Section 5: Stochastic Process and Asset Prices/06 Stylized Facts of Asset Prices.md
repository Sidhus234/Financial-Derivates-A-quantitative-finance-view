<h1>The Stylized Facts of Asset Prices</h1>

The following "stylized facts" hold for series of prices and returns for a wide range of asset classes.

<ol>
  <li><b>Volatility Clustering</b>: Asset pricees exhibit distinct regimes of low, intermediate, and high volatility.</li>
  <li><b>Raw returns series exhibit little to no autocorrelation</b>: Correlation between returns at different times is virtually 0.</li>
  <li><b>Absolute values of returns exhibit considerable autocorrelation</b>: The absolute value of returns at different times show considerable correlation which decays in time very slowly. This means that successive returns are uncorrelated but they are not independent.</li>
  <li><b>Fat Tails</b>: Asset returns have much fatter tails than Gaussian, excess kirtosis, etc.</li>
</ol>

Furhter, we will study the daily log returns from the price time series of 3 different assets: the S&P 500 index, the pound sterling/USD exchange rate, and soyabeans.

For each series we will analyze the log daily returns (continuously compounded returns)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r \( t ) = log \( \frac{P \( t )}{P \( t - 1 )} )">
</p>

We study these returns as a daily time series

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=r \( t_{1} ), r \( t_{2} ), r \( t_{3} ), \cdots r \( t_{k} )">
</p>

with the <img src="https://render.githubusercontent.com/render/math?math=t_{i}"> representing successive business days. First lets look at the raw prices.

<img src="../Images/S6_RawSP500_series.png" alt="S&P 500 raw series"/>

<img src="../Images/S6_Pound_Sterling_USD_ExchangeRate.png" alt="Pound Sterling / USD exchange rate"/>

<img src="../Images/S6_Soyabeanprices.png" alt="Soyabean Prices"/>


