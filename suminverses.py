# suminverses.py
# Sum the values of 1/i for i from 1 to n (inclusive)
# RGW, 2013

def main():
    print( "Sum the values of 1/i for i from 1 to n (inclusive)" )
    n = int( input( "Enter the value for n: " ) )
    total = 0
    for i in range( 1, n+1 ):
        total = total + 1/i
    print( "The sum is", total ) 

main()
