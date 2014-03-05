# suminvsq.py
# Sum the values of 1/2**n for i from 1 to n (inclusive)
# RGW, 2013

def main():
    print( "Sum the values of 1 + 1/2 + ... + 1/2**n" )
    n = int( input( "Enter the value for n: " ) )
    total = 0
    for i in range( 0, n+1 ):
        total = total + 1/2**i
    print( "The sum is", total ) 

main()
