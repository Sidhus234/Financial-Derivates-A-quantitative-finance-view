# Swaps
Swaps are derivatives with 2 counterparties in which the 2 counterparties agree to exchange cash flows with each other.
__Interest Rate Swaps:__ In an interest rate swap a fixed interest payment, on some notational value, is exchanged for a floating interest payment on the same notional value.
__Currency Swaps:__ In a currency swap an interest payment in one currency is exchanged for an interest rate in another currency. 
__Other Swap Types:__ In an __Equiy swap__ a fixed payment is exchanged for the return on some stock or stock index. __Commodity swaps__ exchange a fixed payment for a payment related to a commodity price.
The swap market has, historically been an OTC market. Linke other OTC products, we can divide the participants in swap markets into these classes: dealers (investment banks, broker/dealers, etc.) and end users (nonfinancial business and individuals). As OTC products counterparty credit risk has been a major concern for swaps. The swap market is changing: since the 2008 financial crisis, there has been a global regulatory effort to move standardized swaps into a more exchange traded environments. 2 examples:
- Many swaps are now centrally cleared.
- A significant fraction of swap trading now take splace on _ swap execution facilities_.

## Interest Rate Swaps
__Interest Rate Swaps__ are swaps by far the most prevalent swap contract, with the great majority of outstanding notional in swaps attributable to interest rate swaps. In an interest rate swap a floating interest payment (e.g. a LIBOR rate) is paid by one party to the other, who in turn pays the first party an interest rate fixed at contract origination. We distinguish the counterparties b referring to the party paying the fixed rate as the __payer__ and the party paying the floating rate (and thus receiving the fixed rate) as the __receiver.__ 
When an interest rate swap is originated, a notaional value is contracted, representing the principal that interest payments will be based on (Even though no principal is ever exchanged between the counterparties).
- Denote the notional value by _N_.
- The contract specifies a series of payment dates <img src="https://render.githubusercontent.com/render/math?math={t_i}_{i=1}^I"> usually spaced by 3 month of 6 month increments.
- In addittion <img src="https://render.githubusercontent.com/render/math?math=t_0"> denotes the contract origination date.
- A particular fixed interest rate is contracted, which we denote by _S_. _S_ is called the swap rate.
- A particular market interest rate is chosen for the floating payment. Denote this floating interest rate level <img src="https://render.githubusercontent.com/render/math?math=L_i"> for the value of the floating rate set on date <img src="https://render.githubusercontent.com/render/math?math=t_i">. __NOTE:__ <img src="https://render.githubusercontent.com/render/math?math=L_i"> is not the floating rate paid on date <img src="https://render.githubusercontent.com/render/math?math=t_i">
