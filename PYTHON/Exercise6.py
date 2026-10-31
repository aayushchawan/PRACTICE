# conditions while accepting user input
# 1. username less than 12 char 
# 2. No spaces 
# 3. No digits

print("# 1. username less than 12 char\n 2. No spaces\n 3. No digits")
username = input("Enter your username:")

a = len(username)
b = username.count(" ")
c = username.isalpha()

if a < 12 and b == 0 and c :
    print("Username available")
else :
    print("Enter a valid username as per rules")