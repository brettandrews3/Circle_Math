"""
This is a little "import math" practice. Using the math module, I set a short
elif loop to return the area or circumference of a cirle, using its user-defined
radius. While it doesn't loop back if the user enters improper feedback, it does
ask them to reset the program if they enter the wrong type of answers.
"""

import math

#PI = 3.14
r = float(input("Enter the radius of a circle: "))
area = math.pi * r * r
circumference = 2 * math.pi * r
outcome = input('\nWhich do you want to see: area of circle (a) or its circumference (c)? ')
if outcome.lower() == 'a':
    print("Area of a circle = %.2f" %area)
elif outcome.lower() == 'c':
    print('Circumference of a circle = %.2f' %circumference)
else:
    print("That input didn't work. Reset the program and try again.")
