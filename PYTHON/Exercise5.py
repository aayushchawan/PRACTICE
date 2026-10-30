# Hypotenuse of a triangle program

import math

a = float(input("Enter 1st side of your triangle:"))
b = float(input("Enter 2nd side of your triangle:"))

c = math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypotenuse of the triangle is : {round(c,3)}")