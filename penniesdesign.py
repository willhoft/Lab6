# penniesdesign.py
# Use the accumulator design to create a program to calculate the number
#   of pennies you will have in a month if you double the number each day.
# RG Willhoft, 2013

def main():

    # DESIGN

    # Accumulator variable: pennies
    # Initial accumulator value: 1 
    # Define loop: range( 2, 31 )
    # Modification of loop variable: none
    # How is the accumulator value modified: pennies = pennies + pennies

    # CODE

    print( "Day 1 you have 1 penny" )
    pennies = 1
    for day in range( 2, 31 ):
        pennies = pennies + pennies
        print( "Day", day, "you have", pennies, "pennies" )    

main()
