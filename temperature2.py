'''
Assignment 2: Temperature Chart
'''

def toFahrenheit (celsius):
    return celsius * 1.8 + 32

for a in range (0, 101, 5):
    print (str(a) + " celsius = " + str(toFahrenheit(a)) + " fahrenheit") 