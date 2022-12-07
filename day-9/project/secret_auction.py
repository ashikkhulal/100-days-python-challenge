# from replit import clear
import os
def clear():
    os.system('cls')
# HINT: You can call clear() to clear the output in the console.

# importing auction logo from art
from art import logo
print(logo)

# welcome statement
print("Welcome to the secret auction program.")

# bid entry dictionary to hold bid data
bid_entry = {}
def bid_data(name, amount):
    bid_entry[name] = amount

# restart flag
is_over = False

# logic
while not is_over:
    name = input("What is your name?: ")
    bid = float(input("What's your bid? :$"))
    dollar_bid = "{:.2f}".format(bid)
    bid_data(name=name, amount=dollar_bid)
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if restart == "no":
        is_over = True
        count = 0
        for key in bid_entry:
            count += 1
            max_bid = bid_entry[list(bid_entry)[0]]   # first_key = list(bid_entry)[0]
            total_bidders = len(list(bid_entry))
            if total_bidders == 1:
                clear()
                print(f"The winner is {key} with a bid of ${max_bid}.")
            elif total_bidders >= 2:
                if bid_entry[key] > max_bid:
                    max_bid = bid_entry[key]
                    if total_bidders == count:
                        clear()
                        print(f"The winner is {key} with a bid of ${max_bid}.")
    else:
        clear()

