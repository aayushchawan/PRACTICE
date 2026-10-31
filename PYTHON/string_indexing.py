# string indexing = acessing elements of a index using [] indexing operator
#   [ start : end : stop]
# start: string starts from here
# end: string prints element before this address but not this address
# step: skips number of elements mentioned
#### -1 in step reverses the string 

card_num = "1234-5678-9012-3456"

print(card_num[4])  # starts from 0 just like c programming
print(card_num[0:9]) # you can leave 0 blnk if you want to get from inital of string
print(card_num[5:19]) # you can leave 19 blank if you wan to go till end of string

print(card_num[-1]) #starts from behind
print(card_num[::3]) # every 3rd nuumber after inital is counted

print(card_num[15:]) #last 4 digits
a = card_num[-4:]
print(f"XXXX-XXXX-XXXX-{a}")

# Exercise reversing strings 

print(card_num[::-1])
