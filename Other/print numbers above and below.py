number = int(input("Please enter a number (-100 - 100): "))

while number < -100 or number > 100:
    number = int(input("The number must be between -100 and 100, please enter another number: "))

uOrD = input("Please enter either 'u' or 'd': ")

while not uOrD == "u" and not uOrD == "d":
    uOrD = input("The letter must be either 'u' or 'd', please enter another letter: ")

if uOrD == "u":
    count = 0
    while count < 10:
        number += 1
        print(number)
        count += 1

if uOrD == "d":
    count = 0
    while count < 10:
        number -= 1
        print(number)
        count += 1
