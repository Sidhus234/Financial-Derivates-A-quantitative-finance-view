# Discounted Cash Flow Analysis

- Suppose we own an asset or are a party to contraft that pays a sequence of payments

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=c_1, c_2, c_3, ... , c_N">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;at the corresponding times
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=t_1, t_2, t_3, ... , t_N">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(i.e the payment c_i is made at time t_i)

  - The payments c_i is called cash flows
  - The situation being described here is an asset which pays its holder a stream of cash flows
  - To value our asset, i.e. to value a stream of cash flows, we must follow what the present value of a stream of cash flows is.
  - The present value of any individual payment, say c_i is

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=d(t_i)c_i">
</p>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in terms of the disocunt factor d(t_i).

  - We may take as our definition of the present value of a stream of cash flows the natural generalization of the present value of just 1 cash flow. The total amount that needs to be invested today to replicate the stream of cash flows.
  - Since each cash payment is independent of all the others, the present value of the cash flow stream is just the sum of the cashflows of the individual payments.
  - Thus the PV of our cash flow stream is

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= d(t_1)c_1 %2B d(t_2)c_2 %2B d(t_3)c_3 %2B .... %2B d(t_N)c_N">
</p>

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= \sum_{i=1}^{N} d(t_i)c_i">
</p>

  - This expresses the present value of a cash flow stream in terms  of general discount factors, which is the most versatile way to write it
  - It is more familiar to see it expressed in terms of specific interest rates, so we present it for annual and continuous compounding

#### Discounted Cash Flow Analysis - Annual Compounding
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= \frac{c_1}{(1 %2B r(t_1))^t_1} %2B \frac{c_2}{(1 %2B r(t_2))^t_2} %2B ... %2B \frac{c_N}{(1 %2B r(t_N))^t_N}">
</p>

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= \sum_{i=1}^{N} \frac{c_i}{(1 %2B r(t_i))^t_i}">
</p>

#### Discounted Cash Flow Analysis - Continuous Compounding
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= e^{-\rho(t_1)t_1} c_1 %2B e^{-\rho(t_1)t_1} c_1 %2B ... e^{-\rho(t_N)t_N} c_N">
</p>

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=PV= \sum_{i=1}^{N} e^{-\rho(t_i)t_i} c_i">
</p>
