# Python Tools

<p> The fixed income module contains tools for bonds and yield curves. To use it, import it into a python interactive environment: </p>

      import fixedincome as fi

<p>
  In the situation where one has specific coupons and payment dates in mind for a bond, one may create a bond object by directly calling the bond factory function, using two python lists, one for the payment values, and one for the dates those payments are made as:
</p>

    bond = fi.bond_factory(dates = [0.5, 1.0, 1.5], rates = [5, 5, 105])

<p>
Very Important Remark: The payment dates must all be floating point numbers, or the function will abort.  This is so as to allow for as of yet unimplemented features which will require overloading of the bond_factory function.
  </p>
  
  <p> This returns a bond object for a bond making payments in 6 months, 1 year, and 18 months of $5, $5, and $105.  Most of the time, though, a user will likely want to create a bond object with a given face value and coupon rate, as well as payment frequency.  For this the create_coupon_bond function can be used:
  </p>
  
    bond = fi.create_coupon_bond(maturity = 5, face = 1000, rate = 6, frequency = 2)


<p>This creates a bond object for a 5 year bond with a $1000 face value paying a 6% coupon rate with semiannual payments.
  
You can see what the payments and payment dates are for a bond object with the getter methods:
  </p>
  
    print(f'Bond dates (in years): {bond.get_dates()}')
    print(f'Bond Coupons: {bond.get_coupons()}')


<p> You may also display the maturity of the bond with </p>

    print(f'Bond Maturity: {bond.get_maturity()} years')

<p> You can see the number of payments a bond pays using the len function: </p>
    
    print(f'# of coupon payments: {len(bond)}')

<p>
  There is a facility for saving a market price for a bond.  This is not required, as the bond is defined by its coupons and payment dates, whereas its price is matter of market conditions.  But if one wants to save a price for the bond (and there are applications that require it) one may save it as an attribute of a bond object by 
  </p>
  
    bond.set_price(100)

<p> which saves a market price of $100 for the bond.  The saved market price can be retrieved by </p>

    print(f'Bond Market Price: {bond.get_price()}')

<p> There are methods for pricing a bond.  This is independent of the saved market price of a bond and requires a curve object for pricing.As a convenience, the create_coupon_bond function has been extended to allow easy production of zero coupon bonds.  This can be done simply by choosing a frequency of 0.  So for instance
  </p>
  
    zero = fi.create_coupon_bond(maturity=10, face=1000, rate=0, frequency=0)

<p> will populate the variable zero with a zero coupon bond, with maturity 10 years and a par value of $1000.  Try this and check the dates and coupons. Note that in this instance the value for the rate argument is irrelevant, and can be excluded altogether. There is also a method for calculating the yield to maturity.  Either a price must be provided when the method is called, or the bond object must have a saved market price attribute:
  </p>
  
    print(f'Bond dates (in years): {zero.get_dates()}')
    print(f'Bond Coupons: {zero.get_coupons()}')

    bond.YTM(price = 1000)

<p> If the price parameter is omitted, the method uses any stored market price, and aborts with an error message if no price is stored and no price is given in the function call. There is some visualization functionality for the bond class as well.  For this invoke the plot_payments method of a bond object.  For instance, something like
  </p>
  
    bond = fi.create_coupon_bond(maturity=3.0, face=10000, rate=8, frequency=2)
    bond.plot_payments()

<p> produces a bar chart illustrating the semiannual coupon payments and the final payment including the principal, helping to visualize the bond as a concrete object.
  
EXAMPLES: Work through the following examples in a Python shell to learn the ins and outs of the bond functionality in the fixed income module.
  
#1: Try creating a bond object for a particular coupon bond.  For example, for a 3 year bond with a $10,000 face value paying a 7% coupon with semiannual payments, you can use the create_coupon_bond function:
  </p>
  
    bond1 = fi.create_coupon_bond(maturity = 3, face = 10000, rate = 7, frequency = 2)

<p>
  # To check that the object is what we expect, check the payment dates and coupons: </p>
  
    print(f'Bond dates (in years): {bond1.get_dates()}')
    print(f'Bond Coupons: {bond1.get_coupons()}')

<p>
  Make sure the dates and coupons are what you expect.  Note that we could create this bond directly using the bond_factory, perhaps in the following way:
  </p>
  
    paydates = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    coupons = [350, 350, 350, 350, 350, 10350]
    bond2 = fi.bond_factory(dates = paydates, rates = coupons)

<p> The 2 bond objects should be, for practical purposes, identical.  You should make sure of this by viewing the payment dates and payments of bond2: </p>

    print(f'Bond dates (in years): {bond2.get_dates()}')
    print(f'Bond Coupons: {bond2.get_coupons()}')

<p> To within some idiosyncrasies of machine arithmetic, these should output the same as bond1. </p>

<p> #2: The bond functionality in this module provides a laboratory for exploring the relationship between the prices and yields of bonds.  You can just create some coupon bonds and then compute the yield to maturity for different prices.  To get started, let's make a 10 year bond with a 9% coupon:
  </p>
  
    bond9 = fi.create_coupon_bond(maturity = 10, face = 10000, rate = 9, frequency = 2)

<p> It's good practice to always check that the bond we've created is what we expect by viewing the payment dates and coupons:
  </p>
    
    print(f'Bond dates (in years): {bond9.get_dates()}')
    print(f'Bond Coupons: {bond9.get_coupons()}')

<p> Make sure this is what you are expecting.  Now, to explore the relationship between yield and price, the first thing to check is the yield of a par bond:
  </p>
    
    bond9.YTM(10000)

<p> In other words, enter the face value of the bond as the price argument of the YTM method.  Is the result what you were expecting?  Now, explore the relationship between price and yield by computing some yields:
  </p>
  
    bond9.YTM(9000)
    bond9.YTM(9500)
    bond9.YTM(10000)
    bond9.YTM(10500)
    bond9.YTM(11000)

<p> A well known principle of bonds is that yield is in inverse relationship to price:  If the price goes up, the yield goes down if the price goes down, the yield goes up.  Does your exploration of price and yield seem to confirm this?  By instantiating different coupon bonds with different coupons and different maturities, and for each of them exploring the relationship between price and yield you can also investigate how yield is related to these other bond parameters.
  </p>
