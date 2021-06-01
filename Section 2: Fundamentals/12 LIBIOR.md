# LIBOR: London Interbank Offered Rate
- Future of LIBOR is uncertain, and may have a reduced rule in finance in future
- It is a measure of the rate at which large and secure London-based banks can secure funding, in different currencies from other such banks
- Historically it emerged from the Eurodollar market in London in the late 1960s, with London based banks issuing loans to businesses and governments from their holdings of US dolars.
- __Eurodollar__ refers to United States currency that is held outside of United States, hence outside of purview of United States regulators. 
- As the LIBOR rates grew in influence, eventually the British Bnaker's association took responsibility for administering it.


# Construction of LIBOR:
- LIBOR is now adminstered by the Intercontinental Exchange conglomerate of exchages
- For each of the 5 currencies for which LIBOR is produced (USD, EUR, GBP, JPY, CHF), there are 16 member banks which are asked to submit quotes of the rate they could secure unsecured funding from other banks. This is done for loan terms ranging from overnight to 1 year.
- The top 4 and bottom 4 of the submissions are dropped, and the remaining 8 are averaged to obtain the final published LIBOR rate.
- This estimation procedure is known as taking a _trimmed mean_
- The typical money market asset we think os as linked to LIBOR is a __certificate of deposit (CD):__ a deposit of cash for a predetermined duration and at a fixed interest rate.
- A __CD__ is usally a short term investment (up to 1 year).
- If _L_ is the simply compounded interest rate for a _CD_, then if we invest _$1_ in the _CD_, with a loan term of _T_, then at maturity the investment is worth:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=1 %2B TL">
</p>

- As LIBOR is a simply compounded rate,by the above description, the average interest rate _L_ for a _CD_ in the interbank market will be the corresponding LIBOR rate.

### Discount factor for LIBOR
  - Let _L(T)_ be the LIBOR rate for a loan maturing at time _T_.
  - Then a loan for a principal amount _N_ due at date _T_, at the LIBOR rate _L(T)_ will accumulate to a total outstanding amount at time _T_ of

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=N(1 %2B TL(T))">
</p>

  - Alternatively, we may write a corresponding discount factor as:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=d(T) = \frac{1}{1 %2B TL(T)}">
</p>

# Meaning of LIBOR:
- LIBOR interest rate reflect the borrowin
