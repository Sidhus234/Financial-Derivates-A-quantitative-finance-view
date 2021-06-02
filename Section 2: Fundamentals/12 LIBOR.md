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
- LIBOR interest rate reflect the borrowing costs banks pay for unsecured borrowing from other banks for loan terms ranging from overnight to 1 year.
- LIBOR rates thus have term structure reflecting market negotiated for terms to maturity up to 1 year.
- As such, LIBOR rates include a premium for credit risk (the chance the bank will not pay back the loan).
- All together, the LIBOR rates measure banks borrowing costs and provide a gauge of the overall health of the banking sector.

## Flaes of LIBOR
- Financial crisis of 2008 revealed that LIBOR is a flawed instrument vulnerable to abuse (as seein in the [LIBOR scandal](https://www.investopedia.com/terms/l/libor-scandal.asp))
- It has deteriorted further sicne the financial crisis as the (US) interbank lending market is estimated to have dropped from $100 billion in daily transactions before the financial crisis to less than $5 billion in 2018.
- The panel banks thus base their submissions on models and expert judgement, not market transactions, making LIBOR a poor representative of the market.
- As a result, LIBOR is being phased out, and is not scheduled to be replaced with new alternative reference rates _(ARRs)_ for all non-USD currencies by year end 2021, and for USD by June 2023.

## Other IBORs:
- There are other "interbank offered rates" beside LIBOR used in global financial system
- The two most significant are:
  - EURIBOR: in Eurozone
  - TIBOR: in Japan

- They are both similar to LIBOR in that they are term rates measuring banks' interbank borrowing costs, and are constructed using a similar methodology.
- Bot EURIBOR and TIBOR were reformed in recent years to make them more representative of markets and more robust.
- Currently, there is no plan for either of these rates to be discontinued, and their future remains uncertain. They may continue to exist alongside ARRs in other currencies.

## Timeline for LIBOR Decomissioning:
- As of March, 2021, the Financial Conduct Authority of the UK has announced the timeline for the termination of LIBOR.
- 12/31/2021: After this date, panel banks will not be compelled to submit LIBOR rates for GBP, EUR, JPY, CHF, and the 1 week and 2 month tenor for USD.
- 6/30/2023: All remaining USD LIBOR tenors will not be compelled beyond this date.
- Synthetic LIBOR: The FCA may compel IBA, the current LIBOR administrator, to publish a "synthetic" version of LIBOR for certain tenors for GBP and JPY beyond 12/31/2021, and for USD beyond 06/30/2023. These rates will be deemed "nonrepresentative".

