#Assignment - Introduction to Functions
#Q8-Program that determines if a given number is perfect.
#Michael Xu

######### FUNCTIONS #########
def factors(number_):
    factors_list = []
    for i in range(1, number_ + 1):
        if number_ % i == 0:
            factors_list.append(i)
    return factors_list

def total(factors_list_):
    sum_total = 0
    for n in factors_list_:
        sum_total += n
    return sum_total

######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))

if total(factors(number)) == 2 * number:
    print(number, "is perfect.")
else:
    print(number, "is not perfect.")
