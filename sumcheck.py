# sumcheck.py
# Sum the numbers from 1 to n
# RGW, 2013

def main():
    print( "Check sum of all integers from 1 to n" )
    n = int( input( "What value of n? " ) )
    total = 0
    for i in range( 1, n+1 ):
        total = total + i
    print( "The actual sum is", total )
    print( "The formula gives", n*(n+1)/2 )

main()
