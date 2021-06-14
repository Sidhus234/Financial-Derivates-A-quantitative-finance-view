# Pricing Swaps
A swap consists of two payment streams: the fixed interest payments and the floating payments. To value a swap contract, value each stream and take the appropriate difference. 
The stream of fixed payments is called the fixed leg of the swap. Its value is denoted <img src="https://render.githubusercontent.com/render/math?math=V_{fixed}">.
The stream of floating payments is called the floating leg. Its value is denoted by <img src="https://render.githubusercontent.com/render/math?math=V_{float}">.
Let <img src="https://render.githubusercontent.com/render/math?math={t_j}_{j=0}^J"> be the origination and payment dates of a swap, _S_ the fixed rate, <img src="https://render.githubusercontent.com/render/math?math=L_j"> the floating interest rate set at time <img src="https://render.githubusercontent.com/render/math?math=t_j">, _N_ the notional. Let _m_ be the frequency of swap payments, ie there are _m_ payments per year. By default, we would assume <img src="https://render.githubusercontent.com/render/math?math=t_j = \frac{j}{m}">.
Let _d(t)_ be the discount factor for time _t_. Recall: this means _d(t)_ is the value (today) of a payment of $1 at time _t_. 

### Fixed Leg Valuation
We will value the fixed leg first.<img src="https://render.githubusercontent.com/render/math?math=V_{fixed}"> is then the sum of the values of all the fixed payments (or the present value of the stream of fixed payments). The fixed payment each cycle is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{S}{m}N">
</p>

so that the discounted value of the _jth_ fixed payment is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(t_j)\frac{S}{m}N">
  </p>

Then <img src="https://render.githubusercontent.com/render/math?math=V_{fixed}"> is then the sum of the values of all the fixed payments:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{fixed} = \sum_{j=1}^{J} d(t_j)]frac{S}{m}N"><br>
<img src="https://render.githubusercontent.com/render/math?math==\frac{SN}{m} \sum_{j=1}{J}d(t_j)"><br>
</p>

### Floating Leg Valuation
The _jth_ floating payment is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{L_{j-1}}{m}N">
</p>

But we donot know <img src="https://render.githubusercontent.com/render/math?math=L_{j-1}"> at contract origination.
To determine <img src="https://render.githubusercontent.com/render/math?math=V_{float}">, the value of the floating leg, we apply a replication arguement to determine the value, at contract origination, of the _jth_ floating payment. Our replicating portfolio will consist of 2 components:
- a loan maturing at time <img src="https://render.githubusercontent.com/render/math?math=t_j"> with face value _N_
- an investment maturing at time <img src="https://render.githubusercontent.com/render/math?math=t_{j-1}"> also with a face value of _N_, both initiated when the swap is originated. 

This is equivalent to a portfolio consisting of:
- a short position on an _N_ face value zero coupon bond maturing at <img src="https://render.githubusercontent.com/render/math?math=t_j">.
- a long position on an _N_ face value zero coupon bond maturing at <img src="https://render.githubusercontent.com/render/math?math=t_{j-1}">

We will see that this portfolio replicates the _jth_ floating payment in the swap contract. Invoking the Law of One Price it follows that the cost of entering this portfolio is the (Arbitrage) value of the _jth_ floating payment. 
At time <img src="https://render.githubusercontent.com/render/math?math=t_{j-1}"> the investment maturing, and we receive a cash payout of _N_.
Immediately invest these proceeds from <img src="https://render.githubusercontent.com/render/math?math=t_{j-1}\:\:until\:\:t_j">, at the interest rate of <img src="https://render.githubusercontent.com/render/math?math=L_{j-1}">.
At time <img src="https://render.githubusercontent.com/render/math?math=t_j"> our investment is now worth (simply compounding)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B \frac{L_{j-1}}{m})N">
</p>

At this time we pay _N_ to retire the debt now due. Thus the position has finally yielded

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=(1 %2B \frac{L_{j-1}}{m})N - N = \frac{L_{j-1}}{m}N = jth\:\:floating\:\:payment">
</p>

Our portfolio has generated exactly the floating leg payment of the swap at time <img src="https://render.githubusercontent.com/render/math?math=t_j">.
The cost to construct this portfolio must be the fair value (ie the arbitrage price) of the _jth_ floating swap payment on the origination date of the swap.
Recall the portfolio consisted of a long position in a zero coupon bond maturing at time <img src="https://render.githubusercontent.com/render/math?math=t_{j-1}">, and short on a zero coupon bond maturing at time <img src="https://render.githubusercontent.com/render/math?math=t_{j}">, both with a face value of _N_. The cost to construct the portfolio is then

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Nd(t_{j-1} - Nd(t_j) = N(d(t_{j-1}) - d(t_j))">
</p>
This, then, is the value of the _jth_ floating leg payment at contract origination. <img src="https://render.githubusercontent.com/render/math?math=V_{float}"> is then the sum over all the floating leg payments of this value. Summing over all floating leg payments:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{float} = \sum_{j=1}^{J} N(d(t_{j-1}) - d(t_j))"><br>
<img src="https://render.githubusercontent.com/render/math?math=V_{float} = N\sum_{j=1}^{J} (d(t_{j-1}) - d(t_j))"><br>
<img src="https://render.githubusercontent.com/render/math?math=V_{float} = N(d(t_{0}) - d(t_J))"><br>
<img src="https://render.githubusercontent.com/render/math?math=V_{float} = N(d(1 - d(t_J))">
</p>

(<img src="https://render.githubusercontent.com/render/math?math=t_0 = 0"> is the date of contract origination)
We may finally value the swap from either the payer's or the receiver's point of view.
For the payer (the party paying fixed), the value of the swap is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V = V_{float} - V_{fixed}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V = N(1 - d(t_J)) - \frac{SN}{m} \sum_{j=1}^{J}d(t_j)">
</p>

and for the receiver (the party paying floating), the value of the swap contract is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=-V = V_{float} - V_{fixed}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V = \frac{SN}{m} \sum_{j=1}^{J}d(t_j) - N(1 - d(t_J))">
</p>

__Fair Swap Rate:__ The fair swap rate is the value of the fixed rate _S_ in an interest rate swap that sets the swap contract value to 0 at contract origination. From our computation of the swap value _V_ the fair swap rate _S_ satisfies

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V = 0"><br>
  <img src="https://render.githubusercontent.com/render/math?math=0 = N(1 - d(t_J)) - \frac{SN}{m} \sum_{j=1}^{J} d(t_j)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=N(1 - d(t_J)) = \frac{SN}{m} \sum_{j=1}^{J} d(t_j)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S = \frac{m(1 - d(t_J))}{\sum_{j=1}^{J} d(t_j)}">
</p>
giving the fair swap rate.


### Example 1:
Suppose we enter into a 1 year interest rate swap with quarterly payments on a notional value of $500,000 as the fixed payer. Suppose the term structure of the discount factors for the next year is given by
_d(0.25)_ = 0.982
_d(0.5)_ = 0.975
_d(0.75)_ = 0.965
_d(1)_ = 0.952
What fixed rate will be quoted? Suppose that in 3 months after the first payments have been made the term structure of discount factors is now
_d(0.25)_ = 0.979
_d(0.5)_ = 0.961
_d(0.75)_ = 0.955
What is the value of our position at this time?

Quarterly swap payments implies the frequency of payments is _m_ = 4. There will be a total of _J = 4_ fixed payments made in 1 year. The fair swap rate, from is
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=S = \frac{m(1 - d(t_J))}{\sum_{j=1}^{J} d(t_j)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S = \frac{4(1 - d(1))}{\sum_{j=1}^{4} d(t_j)} = \frac{4(1-0.952)}{0.982 %2B 0.975 %2B 0.965 %2B 0.952}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S = 0.0496">
</p>

The quoted fixed rate will be able to construct will be 4.956%.

Immediately after the first fixed and floating payments are made, 3 months after the origination of the swap, there are 3 payments left, 3, 6, and 9 months hence. 
From our point of view (the fixed payer) the value of the swap is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{float} - V_{fixed}">
</p>

With a notional value of _N_ = 500,000 the two legs are valued as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{float} = N(1 - d(0.75)"><br>
  <img src="https://render.githubusercontent.com/render/math?math=V_{float} = (500000)(1 - 0.955) = 22500"><br>
</p>

And

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V_{fixed} = \frac{SN}{m} \sum_{j=1}^{3} d(t_j) = \frac{SN}{m} \sum_{j=1}^{3}d(j/4)"><br>
  <img src="https://render.githubusercontent.com/render/math?math==\frac{0.04956 \times 500000}{4} (0.979 %2B 0.961 %2B 0.955) = 17935">
</p>

Hence, the value of our swap position after the first payment is $22,500 - $17,935 = $4565

### Example 2:
A corporation has previously issued a floating rate bond with a 5 million dollar face value paying 6 month LIBOR plus 200 bps which matures in a year. Concerned about interest rate increases, the company wants to protect against this risk. How can it do this with swaps? What market swap rate can it contract, assuming the term structure of the discount factos is
_d(0.5)_ = 0.996
_d(1)_ = 0.989
Suppose the 6 month LIBOR rate at the time the swap is originated is 0.8% and that 6 months after the 6 month LIBOR rate has risen to 1.7^. How effective has this risk management strategy been?

The company can enter an interest rate swap as payer, that is the party paying fixed , and thus convert the floating rate payments into fixed payments. For full coverage, the company must enter into a 1 year swap on a notional value of $5,000,000 and making semiannual payments, with 6 month LIBOR as the floating rate.
The fair swap rate the company can contract for this swap will be

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=S = \frac{m(1 - d(t_J))}{\sum_{j=1}^{m} d(t_j)}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=S = \frac{2(1 - d(1))}{\sum_{j=1}^{2} d(j/2)} = \frac{2(1-0.989)}{0.996 %2B 0.989}" = 0.01108>
</p>

Had the company not taken the swap position, the effective interest rate it would have paid would have been LIBOR + 200 bps in 6 and 12 months. Thus, the payments would have been

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=First\:\:Payment = \frac{0.008 %2B 0.02}{2} (5000000) = 70000"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Second\:\:Payment = \frac{0.017 %2B 0.02}{2} (5000000) = 92500"><br>
</p>

for a total of $162,500

After taking the swap position, the companies 2 payments will be

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=First\:\:Payment = \frac{0.01108 %2B 0.02}{2}(5000000) = 77700"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Second\:\:Payment = \frac{0.01108 %2B 0.02}{2}(5000000) = 77700">
</p>

for a total of $155,400

So putting on the swap position have been marginally effective (saving $7100). Over the long period, the effects might have been much larger. 
