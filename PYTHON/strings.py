# Methods and type of functions that can be used to define strings
# len(string) = length of string including spaces 
# string.find(" ") = finds after how many char is the given char/symbol (space here) located
# string.rfind("w") = reverse find( if no char/symbols then returns -1)
# string.capitalize() = 1st letter of string capital
# string.upper() = ALL CAPS
# string.lower() = all lower case
# string.isdigit() = if all digits then returns true else false (boolean)
# string.isaplha() = if all aplhabets
# string.count("-") = cout total char in string
# string.replace("-","_") = replace - with _ and give output

# for more such shortcuts use : print(help(str))

name = input("Enter your name:")

a = len(name)
b = name.find(" ")
c = name.isdigit()
d = name.replace("a","@")
print(f"Length of string is: {a}")
print(f"There is a space after {b} characters ")
print(f"{c}")
print(d)
