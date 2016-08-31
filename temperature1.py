'''
Assignment 1: Temperature
'''

again = True
while again:
    temperature = int(input("Enter temperature in fahrenheit: "))
    celsius = (temperature - 32) * (5/9)
    print(str(temperature) + " fahrenheit = " + str(celsius) + " celsius")
    repeat = input("Do you want to convert another temperature? [y/n]: ")
    if (repeat != "Y" and repeat != "y"):
        again = False