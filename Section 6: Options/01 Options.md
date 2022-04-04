<h1>Options</h1>
Options are contracts between two counterparties that give one of the counterparties the right (but not the obligation) to buy or sell a particular asset to or from the other counterparty at a price agreed to upon entering the contract. 

<li>An option to buy is called a <b>call</b>.</li>
<li>An option to sell is called a <b>put</b>.</li>
<li>The counterparty with the option is the option <b>buyer</b> or option <b>holder</b>. They buyer <b>exercises</b> the option if she chooses to buy or sell.</li>
<li>The other counterparty, who must accept the choice of the option buyer is called the option <b>seller</b> or the option <b>writer</b>.</li>

<h2>Specification of Option Contracts</h2>

To define an option contract, the underlying asset, the quantity of the asset, the type (call or put), the strike price, and the expiration date or expiry must be specified. Options are written on stocks and stock indexes, currencies, commodities, interest rate products, and on futures. The __strike price__ is the price at which the underlying will be bought or sold if the option is exercised. The __expiry__ is the time of termination of the option. In addition, the exercise tupe must be specified.
<li>A <b>European Option</b> is an option that can only be exercised at the expiration date.</li>
<li>An <b>American option</b> is one that may be exercised any time between the contract origination and expiry.</li>

In addition, like forwards and futures, options may be settled either by physical delivery of the underlying or may be cash settled. Options trade in both OTC and exchange traded markets. Like forward contracts, counterparty credit risk is a major risk source for OTC traded options. And like futures contracts, exchange-traded options are margined and marked to market so that counterparty credit risk is a very minor issue for options on exchanges.

<h3>Option Positions</h3>
The option holder is said to have the long position in the option. The option writer is said to have the short position. There are then, 4 basic positions for an investor:
<ol>
  <li>A long call position.</li>
  <li>A long put position.</li>
  <li>A short call position.</li>
  <li>A short put position.</li>
</ol>

<h3>Moneyness</h3>
Terminology denoting the status of an option when the spot (underlying) price is above, below, or equal to the strike price:
<li>An option is <b>in the money</b> if a call and spot > strike or a put and spot < strike.</li>
<li>An option is <b>out of money</b> if a call and spot < strike or a put and spot > strike.</li>
<li>An option is <b>at the money</b> if spot=strike (for both calls and puts).</li>

<h3>Option Premium</h3>

Once an option holder owns an option, they have no downside risk. The lowest possible payout will occur if the option expires out of the money, worthless. The option would be an arbitrage unless the option holder had to pay to own it. Thus, an investor must pay a price to enter a long position in a call or a put. The price for an option is called the __option premium__.

<h3>Option Assumptions</h3>
<li>Unless otherwise stated, we will only treat European options.</li>
<li>Unless otherwise stated, we will only consider options on underlying assets that pay no income. </li>
<li>The default underlying asset can be taken to be a stock paying no dividents throughout our treatment of options.</li>

__Remark__: In the following axamples, assume interest rates are 0 so that future and present values of any payment equals the cash value of the payment when made. 

<h3>Example 1</h3>
Suppose an investor paid a $10 premium for a European call with a strike price of $60. Under what circumstances should the option be exercised? If the spot price of the underlying asset is $75 at expiry, how much does the investor profit or lose? What if it is $40?

<li><b>Case 1</b>: The call gives the option holder the right ti purchase the asset for $60 at expiry. If, at expiry, the asset value is <= $60 the option will not be exercised, since it can be purchased cheaper on markets. If the asset value is > $60 at expiry then the option will be exercised.</li>
<li><b>Case 2</b>: In the case that the asset is worth $75 at expiration, the option gives the option holder the right to purchase it for $60. The option holder will exercise the option, buy the asset for $60, and can immediately sell it on the market for $75, profiting by $15. Subtracting from this the $10 premium paid at contract origination, the investor's net profit is $5.</li>
<li><b>Case 3</b>: In the second case, because the market price of the asset is $40 < $60, the option will not be exercise, and expires worthless. The investor then suffers a loss of the initial $10 premium.</li>
