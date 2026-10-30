# if else atatemnets 

age = int(input("Enter your age: "))

if age >=18:
    print("You are eligible to vote")
elif age<0:
    print("You havent been born yet")
else:
    print("You are not eligible to vote")

response = input("Would you like some food? (Y/N):")

if response =="Y":
    print("Here is some food for you")
elif response =="N":    
    print("Okay, have a good day")

name = input("Enter your name: ")

if name == "":
    print("You did not enter your name")
else :
    print(f"Hello {name}")
    
