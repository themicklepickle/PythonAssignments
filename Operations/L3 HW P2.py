number = int(input("Please enter a two-digit number: ")) #user input
tens = int(number / 10) #determines the tens by dividing by 10 and returning an integer value
ones = number - tens * 10 #deternmines the ones by substracting the tens value multiplied by 10

#print
print("Tens:", tens)
print("Units:", ones)
