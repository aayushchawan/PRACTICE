#input() function is used to take input from the user. It always takes input as string.
#to make it more accurate we can use typecasting to convert the input to the desired data type.

name = input("Enter your name: ")
print(f"Hello {name}")

age = input("Your age: ")
print(f"You are {age} years old")

age = int(age) # TO convert string to integer we use int() function

age +=1 
print(f"Next year you will be {age} years old!")

gpa = float(input("Enter your gpa: ")) # we can also use typecasting directly in the input() function

print(f"Your gpa is {gpa}")

