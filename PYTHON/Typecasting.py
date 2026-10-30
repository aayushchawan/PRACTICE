# Converting one data type to another is called Typecasting in Python

name = "Corpse"
age = 18
price = 19.99
boolean_value = True

age=float(age) # converting integer to float makes it more accurate/ decimal value 

print(f"Your age is {age}")

price=int(price) # ( basically GIF ) converting float to integer makes it less accurate/ decimal value is lost 

print(f"Your price is {price}")

name=bool(name) # converting string to boolean makes it True if the string is not empty and False if the string is empty

print(f"Did you enter name?\n {name}")