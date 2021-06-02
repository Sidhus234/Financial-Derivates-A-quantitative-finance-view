The fixed income module contains a class for yield curves.  Import the fixed income module with

    import fixedincome as fi
    import matplotlib
    %matplotlib qt

For creating a yield curve object, it is recommended to use the curve_factory function.  The most straightforward way to create a curve is to simply specify the spot rates and the corresponding tenors.  The signature for the curve_factory function to use in this case is

    #yield_curve = fi.curve_factory(dates, rates)

where dates is assumed to be a list of tenors specified by year fractions, and rates are a list of spot rates corresponding to those tenors which must be entered as percentages, and are assumed to be continuously compounded.  These lists must be the same length or an error message will be returned and the function will be aborted.

For instance, one could build a curve object as

    tenors = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
    spot_rates = [0.8, 0.95, 1.16, 1.4, 1.65, 2.1, 2.6. 3.0]
    yield_curve = fi.curve_factory(dates = tenors, rates = spot_rates)

This returns a curve object implementing a yield curve with a 0.8% spot rate at the 3 month tenor, a 0.95% spot rate at the 6 month tenor, a 1.16% spot rate at the 1 year tenor, etc.

Please note that the spot rates entered through the curve_factory function are treated as continuously compounded rates, which is also the internal representation of the rates in the curve object.  You will get surprising results if you enter rates corresponding to a different compounding convention.

It is also possible to specify in invoking the curve_factory an interpolation method for the curve.  In addition to the basic piecewise linear method, which is the default, there is now, available, 2 cubic spline methods, Hermite interpolation based on the Catmull-Rom procedure, and cubic splines with natural boundary conditions. These can be specified using the method argument in the curve_factory function.  To build the curve using Hermite interpolation, make the above function call as

    yield_curve = fi.curve_factory(dates = tenors, rates = spot_rates, method="hermite")

For a natural cubic spline interpolation, invoke the function as

    yield_curve = fi.curve_factory(dates = tenors, rates = spot_rates, method="natural")

One may also specify to build the curve with piecewise linear interpolation by calling the function as

    yield_curve = fi.curve_factory(dates = tenors, rates = spot_rates, method="pwlinear")

However, as this is the default method, one may simply leave this argument unspecified and the curve will be constructed with piecewise linear interpolation.

NOTE: At present the cubic spline interpolation methods are only available when building the curve from specified, continuously compounded, rates.

Yield curves may also be built by specifying either a list of bonds or from money market instruments (a LIBOR curve).  These curve building procedures will be discussed in separate articles.

Once built, the spot rates and tenors of a yield curve may be displayed by the getter functions:

    print(f'Rates: {yield_curve.get_rates()}')
    -- Rates: [0.8, 0.95, 1.16, 1.4, 1.6500000000000001, 2.1, 2.6, 3.0]
    print(f'Tenors: {yield_curve.get_tenors()}')
    -- Tenors: [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]

One may recover the implied spot interest rate, for an arbitrary maturity, with the get_yield method:

    time = 0.45 # tenor for which to calculate the yield
    print(F'Yield for 0.45 tenor: {yield_curve.get_yield(time)}')
    -- Yield for 0.45 tenor: 0.9199999999999999

where time is the desired maturity for the spot rate.  The rates returned by both the get_rates and get_yield methods are continuously compounded. The yield curve object can also return spot rates with arbitrary compounding convention using the spot_rate method.  The signature of this method is

    time = 0.45 # tenor for which to calculate the yield
    compounding = 1 # compunding once a year
    print(f'Spot rate for 0.45 tenor: {yield_curve.spot_rate(time, compounding)}')
    -- Spot rate for 0.45 tenor: 0.9242450080380493

where time, as before, is the maturity of the desired spot rate, and compounding is an integer specifying the compounding frequency.  In particular, set compounding=k to return a rate corresponding to k times per year compounding.  Specify compounding=0 for a simply compounded rate.  For instance, to return the semiannually compounded spot interest rate corresponding to a 5 year loan term, make the call

    interest_rate = yield_curve.spot_rate(5.0, compounding=2)
    print(f'semiannually compounded spot interest rate corresponding to a 5 year loan term: {interest_rate}')
    -- semiannually compounded spot interest rate corresponding to a 5 year loan term: 3.022612923143786

To return a simply compounded rate, the call is

    interest_rate = yield_curve.spot_rate(5.0, compounding=0)
    print(f'Annually compounded spot interest rate corresponding to a 5 year loan term: {interest_rate}')
    -- Annually compounded spot interest rate corresponding to a 5 year loan term: 3.236684854565661

Note that if left unspecified the default compounding convention used for spot rates is simple.

Discount factors can be returned with

    time = 0.45 # time for which to calculate the discount factor
    print(f'Discount factors: {yield_curve.discount_factor(time)}')
    -- Discount factors: 0.9958685579859061

Also one may apply the len function:

    # len gives the number of observations used to build the curve
    print(f'Length: {len(yield_curve)}')
    -- Length: 8

which returns the number of specified rates.

The curve class includes a utility function for carrying out a parallel shift of the curve.  By entering a shift in percentage terms, the internally stored continuously compounded rates will be shifted by the given amount. So

    yield_curve2 = yield_curve.shift(1.0)

returns, into yield_curve2, a curve object where all the rates have been increased by 1 percentage point. Note that this function returns a new curve object, leaving the original curve object unchanged.

For instance, in the example above, the spot rates in yield_curve2, will be 1.8, 1.95, 2.16, 2.4, 2.65, 3.1, 3.6. and 4.0.

Yield curve objects can be used to price bonds.  If we have a bond object we may call its price method together with a yield curve object, to get the price implied by the yield curve:

    bond = fi.bond_factory(dates = [0.5, 1.0, 1.5], rates = [5, 5, 105])
    price = bond.price(curve = yield_curve)

The curve class also has methods for visualization.  These require that Numpy and Matplotlib be available.  invoking

    yield_curve.plot_yields()


<img src="../Images/S2_yield_curve.PNG" alt="Yield Curve"/>


will plot the continuously compounded yields and

    yield_curve.plot_discount_factors()

<img src="../Images/S2_discount_factors.PNG" alt="Discount Factors"/>

will plot the discount factors.

EXAMPLE: As an example of the basic usage of the yield curve functionality, try instantiating a flat yield curve.  To do this, simply build a yield curve using one tenor and one interest rate.  To create a flat yield curve with a 5% spot rate, call the curve factor function like this:

    yc = fi.curve_factory(dates = [10.0], rates = [5.0])

Note that the one tenor entered, 10 years in this case, can be any positive value at all, but it will be most convenient to use a value far enough out that any applications you have for the curve will not require a yield for any date beyond that.  Otherwise, the curve object will need to extrapolate beyond that date, and will produce a warning message.  This has no impact on any computations, but might be a bit annoying.

With our flat yield curve built, we can now do some computations.  As always, it's best to check that our object is what we think it is, so just check that the basic data is correct by viewing the tenors and rates:

    print(yc.get_tenors())
    -- [10.0]
    print(yc.get_rates())
    -- [5.0]

These should be what you expect.  Now, calculate some yields from this curve using different dates:

    print(yc.get_yield(1.0))
    -- 5.0
    print(yc.get_yield(5))
    -- 5.0
    print(yc.get_yield(10.0))
    -- 5.0
    print(yc.get_yield(15))
    -- Warning: extrapolating outside range
    -- 5.0

Note that the argument can be either an integer or a float.  In this case, all these calls should just confirm that this is a flat yield curve, as was our intention.  More instructive is to now calculate some discount factors:

    print(yc.discount_factor(1/12))
    -- 0.99584200184511
    print(yc.discount_factor(0.5))
    -- 0.9753099120283326
    print(yc.discount_factor(2))
    -- 0.9048374180359595
    print(yc.discount_factor(7))
    -- 0.7046880897187134
    print(yc.discount_factor(12))
    -- Warning: extrapolating outside range
    -- 0.5488116360940264


This gives some idea of the discounting effect of a 5% interest rate.

One may also see this by plotting the discount factors using the plotting function

    yc.plot_discount_factors()
    
<img src="../Images/S2_discount_factor_1_interestrate_only.PNG" alt="Only 1 interest rate"/>

One should invoke both this and the other plotting method

    yc.plot_yields()
    
<img src="../Images/S2_yields_one_interestrate_only.PNG" alt="Only 1 interest rate"/>

to get a feel for how yield curves really behave.

A final application to try with the yield curve object is pricing a bond.  For instance, try creating a bond paying a 5% coupon, and pricing it with our yield curve:

    bond5 = fi.create_coupon_bond(maturity = 5, face = 10000, rate = 5, frequency = 2)
    print(bond5.price(yc))
    -- 9972.465304609344

Is this result what you expect?  If it surprises you, remember the compounding convention implicit in our construction of a yield curve.
