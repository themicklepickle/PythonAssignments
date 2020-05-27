#user inputs the number of eggs that they wish to buy
numberOfEggs = float(input("Please enter the number of eggs that you would like to buy: "))

#ensures that the number of eggs is a natural number
while numberOfEggs <= 0 or numberOfEggs % 1 > 0:
    numberOfEggs = float(input("Sorry, the number of eggs must be a natural number, please enter a new number: "))

#runs if the number of eggs is less than or equal to 12
if numberOfEggs <= 12:
    price = numberOfEggs * 0.5 #calculates price
    price = str("%0.2f" % price) #converts the float to a 2 decimal place number because that is how currency is represented
    print("Your price is $" + price + ".") #prints the price

#runs if the number of eggs is less than or equal to 24
elif numberOfEggs <= 24:
    price = 12 * 0.5 + (numberOfEggs - 12) * 0.4 #calculates price
    price = str("%0.2f" % price) #converts the float to a 2 decimal place number because that is how currency is represented
    print("Your price is $" + price + ".") #prints the price

#runs if the number of eggs is less than or equal to 36
elif numberOfEggs <= 36:
    price = 12 * 0.5 + 12 * 0.4 + (numberOfEggs - 24) * 0.3 #calculates price
    price = str("%0.2f" % price) #converts the float to a 2 decimal place number because that is how currency is represented
    print("Your price is $" + price + ".") #prints the price

#runs if the number of eggs is more than 36
else:
    price = 12 * 0.5 + 12 * 0.4 + 12 * 0.3 + (numberOfEggs - 36) * 0.2 #calculates price
    price = str("%0.2f" % price) #converts the float to a 2 decimal place number because that is how currency is represented
    print("Your price is $" + price + ".") #prints the price
