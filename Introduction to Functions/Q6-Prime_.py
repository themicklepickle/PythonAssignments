#Assignment - Introduction to Functions
#Q6-Program that asks the user for a number and deides whether that number is prime or
#   not.
#Michael Xu

######### FUNCTIONS #########
def prime(number_):
    factors = 0
    for i in range(2, number_):
        if number_ % i == 0:
            factors += 1
    if factors == 0:
        return True
    else:
        return False

######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))

if prime(number) == True:
    print(number, "is prime.")
else:
    print(number, "is composite.")
