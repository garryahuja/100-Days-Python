from art import logo
print(logo)

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your price?: $ "))


    bids[name] = price
    print(bids)
    ask = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if ask == "yes":
        print("\n" * 100)
    elif ask == "no":
        continue_bidding = False
        score = max(bids.values())
        bidder = max(bids, key=bids.get)
        print(f"The winner is {bidder} with the bid of ${score}")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


