import fixedincome as fi

"""
    Yield curves may be built from bonds, as described in the lectures.  To do
    this, invoke the curve_factory function in the following way:
"""
# yield_curve = fi.curve_factory(bondlist = bonds)

"""
    Here bonds should be a list of bond objects.  For instance, one could 
    build a set of coupon bonds, pack them into a list, and build a yield 
    curve following the basic algorithm described in class. Note that the bonds 
    used must store a market price (which will be used in building the curve) 
    or an exception will be thrown.
"""
bond1 = fi.create_coupon_bond(maturity = 2, face = 1000, rate = 4, frequency = 1)
bond2 = fi.create_coupon_bond(maturity = 4, face = 10000, rate = 7, frequency = 2)
bond3 = fi.create_coupon_bond(maturity = 6, face = 100000, rate = 9, frequency = 2)
bond1.set_price(1000)
bond2.set_price(10000)
bond3.set_price(100000)
list_of_bonds = [bond1, bond2, bond3]
yield_curve = fi.curve_factory(bondlist = list_of_bonds)

"""
    In this case I have assumed all bonds are trading at par, and used the 
    face value as the market price, but any price can be used.  The yield curve
    will be built following the basic procedure described in lecture, but with 
    the nonlinear rootfinding invoking whatever interpolation procedure is
    specified.  Note that, at present, when building a yield curve from bond 
    prices, only the piecewise linear interpolation method is available. 

    EXAMPLE: As a basic example, use the facility for constructing curves from
    bonds to reproduce the results from the example of bootstrapping curves 
    from bonds covered in lecture.  Recall that we used 3 bonds to bootstrap
    a curve:

    > A zero coupon bond with a $1000 face value maturing in 6 months with a 
    current price of $985.
    > A bond paying a semiannual coupon with a $10,000 face value, a 5% coupon,
    and maturing in 1 year and with a current price of $10,124.
    > A bond paying an annual coupon with a $10,000 face value, a 7% coupon 
    and maturing in 2 years and with a current price of $10,507

    We instantiate these 3 bonds using the bond factory and create_coupon_bond functions:
"""
bond1 = fi.bond_factory(dates = [0.5], rates = [1000])
bond2 = fi.create_coupon_bond(maturity = 1, face = 10000, rate = 5, frequency = 2)
bond3 = fi.create_coupon_bond(maturity = 2, face = 10000, rate = 7, frequency = 1)

"""
    We enter the given market prices for these bonds:
"""
bond1.set_price(985)
bond2.set_price(10124)
bond3.set_price(10507)

"""
    Now pack up the 3 bonds in a list:
"""
bonds = [bond1, bond2, bond3]

"""
    Now we can build the curve:
"""
yc=fi.curve_factory(bondlist = bonds)

"""
    Since we are expecting to reproduce the results we reached in class, check 
    that our yield curve produces the yields we expect:
"""
print(f'Yield (Tenor: 0.25): {yc.get_yield(0.25)}')
print(f'Yield (Tenor: 0.25): {yc.get_yield(0.5)}')
print(f'Yield (Tenor: 0.25): {yc.get_yield(1.0)}')
print(f'Yield (Tenor: 0.25): {yc.get_yield(1.5)}')
print(f'Yield (Tenor: 0.25): {yc.get_yield(2.0)}')
print(f'Yield (Tenor: 0.25): {yc.get_yield(2.5)}')

"""
    These results should agree closely with what was found in lecture.  Of 
    course another basic exercise is to use this curve to price the very bonds
    we used to build the curve:
"""
print(f'Bond1 Price: {bond1.price(yc)}')
print(f'Bond2 Price: {bond2.price(yc)}')
print(f'Bond3 Price: {bond3.price(yc)}')

""" These should produce unsurprising results."""