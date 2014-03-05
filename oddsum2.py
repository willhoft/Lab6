# oddsum2.py
# Sums all the odd numbers up to (and including) a given number
# RGW, 2013

def main():
    print( "Sum all the odd values" )
    start = int( input( "Enter the starting value (must be odd): " ) )
    end = int( input( "Enter the ending value (should be odd): " ) )
    total = 0
    count = 0
    for i in range( start, end+1, 2 ):
        total = total + i
        count = count + 1
    print( "This program summed", count, "values" )
    print( "  and the total is", total )

main()
