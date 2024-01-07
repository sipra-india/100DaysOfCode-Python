print("Welcome to the tip calculator!")
print()
bill = input("What was the total bill? $ ")
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = (float(bill)/people)*tip/100
total = (float(bill)/people)+tip 
total1 = round(total, 2)
print()
print("Each person should pay: $", total1)
