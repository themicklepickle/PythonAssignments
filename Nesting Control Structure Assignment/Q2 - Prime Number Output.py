# asks the user to input a positive integer
number = int(input("Please enter a positive integer: "))

# data sanitation: countinues to asks the user for a new number until it is a positive integer
while number < 0 or number % 1 != 0:
    # asks the user to input a positive integer
    number = input("Sorry, your number must be a positive integer. Please enter another number: ")

# for every value from 2 to the number entered + 1, it tests if the value is prime
for i in range(2, number + 1):

    # assumes that the value is prime
    prime = True

    # for every value from 2 to the value, it checks if the value is divisible by it
    for x in range(2, i):

        # does this if the value is divisible by the second value
        if i % x == 0:
            # records that the number is not prime
            prime = False

    # does this if by the end the number is recorded as being prime
    if prime == True:
        # prints the number
        print(i)
