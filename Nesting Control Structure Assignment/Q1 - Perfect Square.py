# asks the user for a positive number
number = float(input("Please enter any positive number: "))

# data sanitation: ensures that the number entered is positive
while number < 0:
    # asks the user for another number until it is positive
    number = input("Sorry, your number must be positive. Please enter another number: ")

# does this if the number is a decimal
if number % 1 != 0:

    # sets the number of trailing digits after the decimal to 0
    trailingDecimals = 0

    # multiplies the number by 10 until it is an integer
    while number % 1 != 0:
        number *= 10

        # for each time it needs to multiply the number by 10, it records that number in
        # order to determine the amount of trailing digits later
        trailingDecimals += 1

        # truncates the float to make it an int
    number = int(number)

    # assumes that the number is not a perfect square
    perfectSquare = False

    # for every value from 0 to the number entered, it checks if the square of that value
    # is equal to the number
    for x in range(number):

        # does this if the square of the value is equal to the number entered
        if x * x == number:
            # records that the number is a perfect square
            perfectSquare = True

            # if by the end, the number is recorded as being a perfect square, it prints the number
    # and that it is a perfect square
    if perfectSquare == True:

        # gets the original number by multiplying it by 10 to the power of the number of
        # trailing digits
        print(number / 10 ** trailingDecimals, "is a perfect square.")

    # if by the end, the number is recorded as not being a perfect square, it prints the
    # number and that it is not a perfect square
    else:

        # gets the original number by multiplying it by 10 to the power of the number of
        # trailing digits
        print(number / 10 ** trailingDecimals, "is not a perfect square.")

    # does this if the number is an integer
else:

    # truncates the float to make it an int
    number = int(number)

    # assumes that the number is not a perfect square
    perfectSquare = False

    # for every value from 0 to the number entered, it checks if the square of that value
    # is equal to the number
    for x in range(number):

        # does this if the square of the value is equal to the number entered
        if x * x == number:
            # records that the number is a perfect square
            perfectSquare = True

            # if by the end, the number is recorded as being a perfect square, it prints the number
    # and that it is a perfect square
    if perfectSquare == True:
        print(number, "is a perfect square.")

    # if by the end, the number is recorded as not being a perfect square, it prints the
    # number and that it is not a perfect square
    else:
        print(number, "is not a perfect square.")
