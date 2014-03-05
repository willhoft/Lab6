# sinTaylor.py
# Calculate an approximate value for the sine function
#   using a Taylor series.
# RG Willhoft, 2013

import math

def main():
    print( "Calculate sin(x) using a Taylor Series" )
    print( "  (evaluate terms 0 to n)" )
    x = eval( input( "Value of x: " ) )
    n = eval( input( "Value of n: " ) )

    # DESIGN

    # Accumulator variable: result
    # Initial accumulator value: 0 
    # Define loop: for i in range( 0, n+1 )
    # Modification of loop variable: none
    # How is the accumulator value modified:
    #   add (-1)**i / factorial( 2*i+1 ) * x**( 2*i+1 ) to existing value

    # CODE
    result = 0

    for i in range( 0, n+1 ):
        result = result + (-1)**i / math.factorial( 2*i+1 ) * x**( 2*i+1 )

    print( "Approximate value of sin(", x, ") = ", round(result,4), sep=" " )    

main()
