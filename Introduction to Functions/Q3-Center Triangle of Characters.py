# Assignment - Introduction to Functions
# Q3-Program that asks the user for a character and a number and prints out a centered
#   triangle of that character with that number of levels.
# Michael Xu

######### FUNCTIONS #########
def line_of_letters(number_, letter_):
    print(number_ * letter_)


def space(number_, row_):
    print((number_ - row_) * " ", end="")


######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))
letter = input("Please enter a letter: ")

for i in range(1, number + 1):
    space(number, i)
    line_of_letters(2 * i - 1, letter)
