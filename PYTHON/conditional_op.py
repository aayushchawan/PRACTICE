# conditional expression (Ternary operator like)
# 1 line staatement for if else statement 
# formuala:  "(X)" if (Condition) else "(Y)""

num = float(input("Enter your number:"))

print("Positive" if num >= 0 else "Negative")

a = float(input("Enter your number:"))
result = "Even" if a % 2 ==0 else "Odd"
print(f"Your answer is: {result}")


x = 10
y = 20
max = x if x > y else y
print(f"Your max number is : {max}")

access_level = input("What is your level:(admin,worker)")

access = "You can enter" if access_level == "admin" else "Get lost"
print(f"{access}")