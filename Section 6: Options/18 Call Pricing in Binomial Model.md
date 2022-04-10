<h1>Call Pricing in Binomial Model</h1>
We will derive the call premium in the full n-step binomial model. 

Let <img src="https://render.githubusercontent.com/render/math?math=C_{0}"> be the price at time 0 of a call option on the underlying asset with price <img src="https://render.githubusercontent.com/render/math?math=S_{j}"> in an n-step binomial model. Suppose the call expires at time _n_ with a strik price _K_. We found in the last lecture that the price of a call (or any derivative) at time 0 can be expressed as a risk neutral expectation:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{0} = E^{\text{bin} \( . %3B \tilde{p}, n )} \[ \frac{C_{n}}{ \( 1 %2B r)^{n}} ]">
</p>

where <img src="https://render.githubusercontent.com/render/math?math=C_{n} = \max \( S_{n} - K, 0 )"> is the call payoff. So explicitly:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{0} = E^{\text{bin} \( . %3B \tilde{p}, n )} \[ \frac{\max \( S_{n} - K, 0 )}{ \( 1 %2B r)^{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \sum_{j=0}^{n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} \frac{\max \( S_{n} - K, 0 )}{ \( 1 %2B r)^{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \sum_{j=0}^{n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} \frac{\max \( u^{j} d^{\( n - j )} S_{0} - K, 0 )}{ \( 1 %2B r)^{n}}">
</p>

Because of the max function, the termsin the seum are zero unless

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=u^{j} d^{ \( n - j ) } S_{0} - K > 0">
</p>

Isolating for _j_ this condition is equivalent to

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=j > \frac{\log \( \frac{K}{S_0} ) - n \log \( d )}{\lof \( \frac{u}{d} )} = M \( K , S_{0} ) = M">
</p>

We may thus write

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=C_{0} = \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} \frac{u^{j} d^{ \( n - j )} S_{0} - K}{ \( 1 %2B r)^{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} \frac{u^{j} d^{ \( n - j )} S_{0} }{ \( 1 %2B r)^{n}} - \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} \frac{K }{ \( 1 %2B r)^{n}}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\rightarrow C_{0} = \frac{S_{0}}{ \( 1 %2B r)^{n}} \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} u^{j} d^{ \( n - j )} - \frac{K }{ \( 1 %2B r)^{n}} \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} "><br>
  <img src="https://render.githubusercontent.com/render/math?math=\Rightarrow C_{0} = \frac{S_{0}}{ \( 1 %2B r)^{n}} \Phi_{1} - \frac{K }{ \( 1 %2B r)^{n}} \Phi_{2} "><br>
</p>

Where

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\Phi_{1} = \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} u^{j} d^{ \( n - j )}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=\Phi_{2} = \sum_{M < j \le n}  \frac{n!}{j! \( n - j)!} \tilde{p}^{j} \tilde{q}^{\( n - j )} "><br>
</p>

The sums  <img src="https://render.githubusercontent.com/render/math?math=\Phi_{1} \: \: \text{and} \: \: \Phi{2}"> are related to the cumulative probability distribution function of the binomial distribution. Writtent his way, the call price in the binomial model resembles the Black-Scholes formula. Some approaches to derive the Black-Scholes formula use this form. In above equation as <img src="https://render.githubusercontent.com/render/math?math=n \rightarrow \infinity"> we get the Black-Scholes formula. We will follow a somewhat different procedure.
