# cosTaylor.py
# Calculate an approximate value for the cosine function
#   using a Taylor series.
# RG Willhoft, 2012

# Factorial function

def factorial(x):
    result = 1
    for i in range(x,1,-1):
        result = result * i
    return result

def main():
    print( "Calculate cos(x) using a Taylor Series" )
    print( "  (evaluate terms 0 to n)" )
    x = eval( input( "Value of x: " ) )
    n = eval( input( "Value of n: " ) )

    # DESIGN

    # Accumulator variable: result
    # Initial accumulator value: 0 
    # Define loop: for i in range( 0, n+1 )
    # Modification of loop variable: none
    # How is the accumulator value modified:
    #   add (-1)**i / factorial( 2*i ) * x**( 2*i ) to existing value

    # CODE
    result = 0

    for i in range( 0, n+1 ):
        result = result + (-1)**i / factorial( 2*i ) * x**( 2*i )

    print( "Approximate value of cos(", x, ") = ", round(result,4), sep=" " )    

main()
