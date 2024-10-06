# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print("Welcome to the auction!")
other = 'y'

bidders = {}
max_bid = 0
while other.lower() == 'y':
    name = input("Enter your name : ")
    bid = int(input("What's your bid? : $"))
    other = input("Are there any other bidders? (y/n)")
    bidders[name] = bid
    if max_bid < bid:
        max_bid = bid
    print("\n" * 20)


print(f"And the max bid is ${max_bid}")