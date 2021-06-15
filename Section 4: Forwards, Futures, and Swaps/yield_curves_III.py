"""
     A yield curve object can be created following the procedure for building a 
     LIBOR curve.   To do this, one must have 4 lists, one consisting of maturity 
     dates, and one each containing LIBOR interest rates, Eurodollar futures
     prices, and swap rates.  The length of the list of dates must equal the sum
     of the lengths of the other three.  The signature to follow to invoke the 
     curve_factory function to build a curve from money market instruments is
 """
import fixedincome as fi
# yield_curve = fi.curve_factory(dates, libor, futures, swaps)

"""
    The method assumes that the earliest dates in the dates list correspond to
    the libor rates, etc.

    Please note that, as for building curves from bond prices, at present the
    only interpolation method available when building a yield curve from money
    market rates, is the piecewise linear method.  Developing and implementing
    the algorithms for using cubic spline interpolation methods when building 
    the curve from money market rates, or from bond prices, is work in progress.

    Yield curve objects are able to return forward interest rates, using the
    forward_rate method, similar to the way the spot_rate function produces
    spot interest rates.  For forward rates, 2 times must be specified, t1<t2,
    specifying a loan term from time t1 to time t2.  Apart from that it works
    similar to the spot_rate function, and the compounding convention is 
    specified in the same way.  For a simply compounded 2 year rate, 2 years
    forward, make the call
"""

# yield_curve.forward_rate(2.0, 4.0, compounding=0)

"""
    If the compounding argument is a positive integer, that integer will be
    taken as the compounding frequency, in the same way as the spot_rate 
    function.  So, for an annually compounded interest rate, make the call
"""

# yield_curve.forward_rate(2.0, 4.0, compounding=1)

"""
    and for monthly compounding, call the method like
"""

# yield_curve.forward_rate(2.0, 4.0, compounding=12)

"""
    You may specify continuous compounding using a value compounding=inf where
    inf is the infinity object from the standard python math module. 
    For instance, if you have imported the math module by calling
"""

import math

"""
    you can calculate a continuously compounded forward rate with the call
"""

# yield_curve.forward_rate(2.0, 4.0, compounding=math.inf)

"""
    However, one may also specify continuous compounding using the string 
    "continuous" as
"""

# yield_curve(2.0, 4.0, compounding="continuous")

"""
    Either one works the same, and the second is maybe a bit more convenient.
"""

"""
    EXAMPLE: As was the case for the facility for bootstrapping from bonds, a 
    basic example is  to build a curve from money market data using the same 
    data as was used in the lectures on building LIBOR curves.  We invoke the 
    curve_factory as follows:
"""

tenors = [1/12, 2/12, 3/12, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 4.0]
deposits = [0.8, 1.0, 1.3]
futures_prices = [98.4, 98.0, 97.6, 97.3, 97.0]
swap_rates = [2.3, 2.7]
yc = fi.curve_factory(dates = tenors, libor = deposits, 
                      futures = futures_prices, swaps = swap_rates)

"""
    Note that the curve built this way will not in general be the same as
    would result from following the procedure in lecture because the python 
    version interpolates the spot rates not the swap rates.  But it should be
    close, and you can check the by evaluating a few yields from this curve:
"""
yc.get_yield(1/12)
yc.get_yield(0.25)
yc.get_yield(0.5)
yc.get_yield(0.75)
yc.get_yield(1)
yc.get_yield(3)

"""
    for example, should all agree reasonably closely with the curve we 
    built in lecture.
"""