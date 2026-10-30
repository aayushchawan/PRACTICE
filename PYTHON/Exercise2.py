# Shopping carr program

item = input("What item would you like to buy? ")
quantity = int(input(f"How many {item}s would you like to buy? "))
price = float(input(f"What is the price of one {item}? "))

print(f"You have bought {item}s worth ${quantity*price} ")
