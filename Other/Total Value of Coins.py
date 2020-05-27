pennies = int(input("Pennies: "))
dimes = int(input("Dimes: ")) * 10
quarters = int(input("Quarters: ")) * 25

totalValue = (pennies + dimes + quarters) / 100
totalValue = str("%0.2f" % totalValue)

print("Value of money in dollars: $" + totalValue)
