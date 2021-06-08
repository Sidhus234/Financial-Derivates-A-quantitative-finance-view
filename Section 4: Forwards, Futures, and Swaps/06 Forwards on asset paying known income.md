# Forwards on Assets Paying a Known Income
So far we have only considered forward contracts on underlying assets that bear no income for the holder of the asset. Assets like dividend paying stocks or coupon bearing bonds were excluded. Now we extend our analysis to such assets.
- The asset pays a known income over the life of the forward contract.
- The asset pays a known dividend yield.

## Case 1: Known Income
Let _I_ be the present value, at the inception of the contract (_t_ = 0), of the known income paid by the asset during the life of the forward contract. Then arbitrage considerations lead to a forward price of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = (S(0) - I)e^{rT}">
</p>

We will establish this relaitonship directly using cash and carry and reverse cash and carry arbitrages.

__Notation:__ More generally we denote by _I(t)_ the present value at time _t_ of the income provided by the asset between _t_ and _T_.

### Subcase 1:
- First suppose <img src="https://render.githubusercontent.com/render/math?math=K_T \gt (S(0) - I)e^{rT}">.
- We construct an arbitrage portfolio as follows:
  - Take a short position in the forward contract
  - Borrow S(0) (in cash) at the risk free rate.
  - Purchase the underlying with these funds.
  - The portfolio now consists of:
    - the short forward position
    - the underlying asset
    - the debt valued at <img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT}"> at time _t_.

  - We now hold this portfolio until time _T_. The income paid by the asset will accure to us.
  - The future value of this income at time _T_ is <img src="https://render.githubusercontent.com/render/math?math=Ie^{rT}">
  - Thus, at _T_ the portfolio consists of:
    - the short forward position
    - the underlying
    - the debt now valued at <img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT}">
    - a cash holding of <img src="https://render.githubusercontent.com/render/math?math=Ie^{rT}">

  - We now fulfill our obligations under the forward and provide the underlying to the long position holder, receiving <img src="https://render.githubusercontent.com/render/math?math=K_T"> in cash for return.
  - Our total cash holding is now <img src="https://render.githubusercontent.com/render/math?math=K_T %2B Ie^{rT}"> and the assumed inequality can be written as

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T %2B Ie^{rT} \GT S(0)e^{rT}">
</p>

  - We may thus retinr the debt and retain a positive profit of <img src="https://render.githubusercontent.com/render/math?math=K_T %2B Ie^{rT} - S(0)e^{rT}">: An arbitrage profit.


### Subcase 2:
- First suppose <img src="https://render.githubusercontent.com/render/math?math=K_T \lt (S(0) - I)e^{rT}">.
- We construct an arbitrage portfolio as follows:
  - Take a long position in the forward contract
  - Short the underlying with these funds.
  - Invest the cash received at risk free rate
  - The portfolio now consists of:
    - the long forward position
    - the short position in the underlying asset
    - the cash valued at <img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT}"> at time _t_.

  - We now hold this portfolio until time _T_. 
  - Rewrite the assumed inequality as below. The right hand side of the inequality is the value of our cash holdings ar time _T_. We thus have sufficient funds to:
    - Pay the contract price in the forward contract, receiving the underlying which can be used to fulfil the obligation of the short position.
    - Pay the future value of the accured income <img src="https://render.githubusercontent.com/render/math?math=Ie^{rT}">, which is owed to the asset's owner.

  - These actions close out the short position, and we have retained a positive profit

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S(0)e^{rT} - K_T - Ie^{rT}">
</p>
  - This is the arbitrage as it cost nothing to enter the portfolio and we made a profit.

### Summary
Both of the below conditions lead to an arbitrage. Since by assumptions arbitrages cannot exist, neither inequality canbe true. 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T \gt (S(0) - I)e^{rT}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T \lt (S(0) - I)e^{rT}"><br>
  </p>
  
Hence only posibility left is

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T = (S(0) - I)e^{rT}">
  </p>



