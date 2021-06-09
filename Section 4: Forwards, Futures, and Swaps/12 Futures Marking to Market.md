# Futures Marking to Market Process
- Assume the days of a futures contract's life are given by <img src="https://render.githubusercontent.com/render/math?math=t_1, t_2, t_3, \cdots , t_N = T">.
- From day 1 to day 2 the futures price changes from <img src="https://render.githubusercontent.com/render/math?math=K_T(t_1) \:to\:K_T(t_2)">.
- Consider how this impacts the value of the short position.
  - __Case 1:__ Suppose the futures price declines: <img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) \lt K_T(t_1)">
    - Then the seller has a contracted price, namely <img src="https://render.githubusercontent.com/render/math?math=K_T(t_1)"> that is superior (from the seller's point of view) to what is available on the markets on day 1
    - That is, if the seller contracted on day 2, the contracted price would be less and therefore inferioir (for the seller).
    - In the marking to market pricess, the short position would be considered to have gained by <img src="https://render.githubusercontent.com/render/math?math=K_T(t_1) - K_T(t_2) \gt 0">
    - Thus at the end of day 2, the exchange would make a cash payment ot the short's account in the amount of <img src="https://render.githubusercontent.com/render/math?math=K_T(t_1) - K_T(t_2)">

  - __Case 2:__Suppose the futures price declines: <img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) \gt K_T(t_1)">
    - Then the seller has a contracted price, namely <img src="https://render.githubusercontent.com/render/math?math=K_T(t_1)"> that is inferior (from the seller's point of view) to what is available on the markets on day 1
    - In the marking to market pricess, the short position would be considered to have lost by <img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) - K_T(t_1) \gt 0">
    - Thus at the end of day 2, the exchange will charge this amount to the short <img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) - K_T(t_1)">

  - For the long position, the buyer, these position are reversed:
    - The long loses money if the futures price decreases, and will be charged the amount of the loss.
    - If the futures price increases, the long's position has improved and the long's account will be credited.
    - All of the above remains the same if we considering the price increment from day _i_ to day _i + 1_

- When calculating the cashflows for an actual futures position, we must multiply by the contract size and by the number of contracts. So for the long, from day _i_ to day _i+1_ the value of the position changes by {#Contracts} x {Contract Size} x <img src="https://render.githubusercontent.com/render/math?math=(K_T(t_{i+1}) - K_T(t_i))">. The long will be credited this amount if positive, and charged its absolute value if negative. Same for the short, expect the gain or loss is minus the long's.

## Example 1:
Suppose we decide to take a long position in silver futures contracts. The COMEX 5000 silver futures contract has a contract size of 5000 ounces. Suppose we take a long position in 2 contracts. Trakc the cash flows we will receive over 3 days if:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=K_T(t_1) = 16.20"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(t_2) = 16.50"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(t_3) = 16.15"><br>
  <img src="https://render.githubusercontent.com/render/math?math=K_T(t_4) = 16.00"><br>
</p>

We have long position in these futures contracts, the contract size is 5000 ounces, and we hold 2 contracts. Thus our daily gain or loss is given by below from day _i_ to _i+1_
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2 \times 5000 \times (K_T(t_{i+1}) - K_T(t_i))">
</p>
- __Day 2:__
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2 \times 5000 \times (16.50 -16.20) = 3000">
</p>

- __Day 3:__
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2 \times 5000 \times (16.15 -16.50) = -3500">
</p>

- __Day 4:__
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2 \times 5000 \times (16.00 -16.15) = -1500">
</p>

# Margin Accounts
__Margins:__ When a new futures position is opened, the investor must post an __initial margin__ in cash in a __margin account__ with the exchange. On any day when the investor's position profits, the proceeds owed to the investor under the daily settlement process are deposited in the margin account. When the daily settlement process requires the investor to post losses for the day, the charges is deducted from the margin account. 

The balance in the margin account must be maintained above the __maintenance margin__ requirement, which is a smaller than the intial margin requirement. Whenever the balance goes below the maintenance margin requirement, the exchange notifies the investor with a __margin call.__ The investor must then deposit funds in the margin account to bring the balance up to the initial margin level. The main purpose of the margin account is to provide collateral to ensure the futures investor is able to meet the daily settlement requirements. 

## Example 2:
In a silver futures example from the previous lecture, suppose the initial margin for the COMEX 5000 silver contract is $3500 and the maintenance margin is $3000. Track the flows into and out of the margin account.

- On day 1 we enter into a long position in 2 contracts and must deposit the initial margin: 2 x $3500 = $7000 
- On day 2 we gained $3000. Hence our margin account has: $7000 + $3000 = $10000
- On day 3, we lost $3500. Hence our margin account has: $10000 - $3500 = $6500. Maintenance margin is $3000 per contract (total $6000 as we have 2 contracts). $6500 > $6000 (maintenance margin), hence no margin call.
- On day 4, we lost $1500,. Hence our margin account has $6500 - $1500 = $5000. This is less then maintenance margin requirement of $6000. If we want to keep the position open, we must deposit $2000 in the margin account to bring the balance back to initial margin level of $7000.
- 
- 
- On day 4, we lost 
