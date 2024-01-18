import os
import time

def clear(seconds = 0):
 time.sleep(seconds)
 os.system('clear')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bidders = {}


def add_bidder():
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid


add_bidder()


def highest_bidder():
    for key in bidders:
        maxi = 0
        winner = 0
        if bidders[key] > maxi:
            maxi = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${maxi}")


def new_bidder():
    nw = input("Are there any other bidders? Type 'yes' or 'no': ")
    if nw == "yes":
        clear()
        add_bidder()
        new_bidder()
    else:
        highest_bidder()
new_bidder()
