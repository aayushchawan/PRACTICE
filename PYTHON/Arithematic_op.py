# 3. Mathematical Operations & Expression Building
# Python handles arithmetic through standard operators and built-in math helper functions.

# Basic Arithmetic Operators
# 1. Addition (+) & Subtraction (-): increase or decrease values
#    10 + 5 gives 15
# 2. Multiplication (*) & Division (/): scale or divide values
#    Standard division (/) always returns a float
#    10 / 2 gives 5.0
# 3. Exponentiation (**): raises a base number to a power
#    5 ** 2 gives 25
# 4. Modulus (%): returns the remainder of a division
#    10 % 3 gives 1
#    Key use case: checking if a number is even or odd
#    An even number divided by 2 leaves remainder 0, an odd number leaves 1


import math


x = 3.14
y = -6
z = 19.99
a = 2
b = 10 

x = round(x) # rounds to nearest integer
print(f"Rounded value of x is {x}")

y = abs(y) # distance from zero, always positive
print(f"Absolute value of y is {y}")

a = pow(a,b)
print(f"Value of a raised to the power b is {a}")

max = max(x,y,z,a,b)
print(f"The max among all is:{max}")

#math module provides more advanced mathematical functions like square root, trigonometry, logarithms, etc.

import math

print(f"Square root of x is {math.sqrt(x)}")

# math module (needs: import math)
# math.pi          -> constant for Pi (3.14159...)
# math.e           -> constant for Euler's number (2.718...)
# math.sqrt(x)     -> square root of x
#                     math.sqrt(9) gives 3.0
# math.ceil(x)     -> always rounds a float UP to the next integer
#                     math.ceil(9.1) gives 10
# math.floor(x)    -> always rounds a float DOWN to the preceding integer
#                     math.floor(9.9) gives 9

# Performing arithmetic calculations allows software to evaluate inputs
# and determine dynamic pathways during execution.