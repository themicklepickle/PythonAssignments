#Assignment - Introduction to Functions
#Q4-Program that asks the user for a pair of numbers and decides whether the first is
#   a factor of the second.
#Michael Xu

######### FUNCTIONS #########
def factor(factor_, number_):
    if number_ % factor_ == 0:
        return True
    else:
        return False

######## MAIN PROGRAM ########
first_num = int(input("Please enter the first integer: "))
second_num = int(input("Please enter the second integer: "))

if factor(first_num, second_num) == True:
    print(first_num, "is a factor of", str(second_num) + ".")
else:
    print(first_num, "is not a factor of", str(second_num) + ".")
