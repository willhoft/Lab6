# expTaylor.py
# Calculate an approximate value for the exponent function
#   using a Taylor series.
# RG Willhoft, 2012

# Factorial function

def factorial(x):
    result = 1
    for i in range(x,1,-1):
        result = result * i
    return result

def main():
    print( "Calculate exp(x) using a Taylor Series" )
    print( "  (evaluate terms 0 to n)" )
    x = eval( input( "Value of x: " ) )
    n = eval( input( "Value of n: " ) )

    # DESIGN

    # Accumulator variable: result
    # Initial accumulator value: 0 
    # Define loop: for i in range( 0, n+1 )
    # Modification of loop variable: none
    # How is the accumulator value modified:
    #   add x**i / factorial(i) to existing value

    # CODE
    result = 0

    for i in range( 0, n+1 ):
        result = result + x**i / factorial(i)

    print( "Approximate value of exp(", x, ") = ", result, sep=" " )    

main()
