'''
Assignment 3: Quadratic
'''

print ("Welcome to the Program. Please enter the value of A, B, C, and X at the corresponding prompts.")
a = int(input("What is the value of A? "))
b = int(input("What is the value of B? "))
c = int(input("What is the value of C? "))
x = int(input("What is the value of X? "))


'''
So the following lines of code are only meant to prevent
the program from outputting "+-" on the quadratic equation
when the user inputs a negative number.
'''

quadratic="The following quadratic was entered: " + str(a) + "X^2"
if ( b >= 0):
    quadratic += ("+" + str(b) + "X")
else:
    quadratic +=  (str(b) + "X")
if (c >= 0):
    quadratic +=  ("+" + str(c))
else:
    quadratic +=  (str(c))

print (quadratic)
print("The value of the quadratic is: " + str((a*(x*x)) + (b*x) + c))
