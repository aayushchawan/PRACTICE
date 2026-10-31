# Logical operators are used to combine conditional statements.
# -and, or, not are the logical operators in Python.

# or operator returns True if any of the conditions is True.
temp = float(input("Enter the temperature:"))
rain = input("Is it raining (yes/no):")

if temp < 10 or temp > 45 or rain =="yes":
    print("We should not go to play ")
else :
    print("We can go to play outside")

# and operator returns True if both the conditions are True.

temp = float(input("Enter the temperature:"))
sun = bool(input("Is it sunny (True/False):"))

if sun and 10 < temp < 35 :
    print("We can go to play")
else :
    print("We cant go to play")

