# Assignment - Introduction to Functions
# Q5-Program that asks the user for a number and outputs the number of factors that
#   number has.
# Michael Xu

######### FUNCTIONS #########
def number_of_factors(number_):
    factors = 0
    for i in range(1, number_ + 1):
        if number_ % i == 0:
            factors += 1
    return factors


######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))

print(number, "has", number_of_factors(number), "factors.")
