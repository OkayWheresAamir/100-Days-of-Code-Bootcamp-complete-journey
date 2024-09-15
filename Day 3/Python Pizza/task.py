print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size.upper() == "S":
    cost = 15
    if pepperoni.upper() == "Y":
        cost += 2

elif size.upper() == "M":
    cost = 20
    if pepperoni.upper() == "Y":
        cost += 3
elif size.upper() == "L":
    cost = 25
    if pepperoni.upper() == "Y":
        cost += 3



if extra_cheese.upper() == "Y":
    cost +=1

print(f"Your final bill is: ${cost}")