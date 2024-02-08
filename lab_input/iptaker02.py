#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    # get 'vendor name' with device
    vendor =input("Input vendors name: ")
    print(vendor)

    # Vendor name of your device
    device = input("What is the name of your device?" )
    print(device)

    # amount of gigs on device?
    space = input("How many gigs are on your device?" )
    print(space)

    # color of device
    color = input("what color is the device?")
    print("You told me the color is:", color)

main()

