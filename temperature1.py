'''
Assignment 1: Temperature
'''

keepAsking = True
while keepAsking:
    fahrenheit = int(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * (5/9)
    print(fahrenheit, "fahrenheit =", celsius, "celsius")
    repeat = input("Do you want to convert another temperature? [y/n]: ")
    if (repeat.lower() != "y"):
        again = False
