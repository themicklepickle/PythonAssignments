number = float(input("Please enter a number: "))

while number <= 1 or number % 1 != 0:
    number = int(input("Sorry, your number must be an integer greater than 1, please enter a number: "))

number = int(number)

prime = True

for i in range(2, number):
    if number % i == 0:
        prime = False

if prime == True:
    print(number, "is a prime number.")

if prime == False:
    print(number, "is not a prime number.")
