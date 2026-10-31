# 2nd version

username = input("Enter your username:")

if len(username) > 12:
    print("Username should be less than 12 char")
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
elif not username.isalpha()  :
    print("Username should only contain aplhabets")
else :
    print(f"Welcome {username}!")