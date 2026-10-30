# Calculator using if statements 

op = input("Enter your operator:")

if op not in ["+", "-", "*", "/"]:
    print(f"{op} is invalid operator !")
    exit()

a = float(input("Enter 1st number:"))
b = float(input("Enter 2nd number:"))

if op == "+":
    print(f"Your answer is {round(a+b,3)}")
elif op == "-":
    print(f"Your answer is {round(a-b,3)}")
elif op == "*":
    print(f"Your answer is {round(a*b,3)}")
elif op == "/":
    print(f"Your answer is {round(a/b,3)}")
