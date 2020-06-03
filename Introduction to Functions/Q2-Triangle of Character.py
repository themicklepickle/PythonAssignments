# Assignment - Introduction to Functions
# Q2-Program that asks the user for a character and a number and prints out a
#   left-justified triangle of that character with that number of levels.
# Michael Xu

######### FUNCTIONS #########
def line_of_letters(number_, letter_):
    print(number_ * letter_)


######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))
letter = input("Please enter a letter: ")

for i in range(1, number + 1):
    line_of_letters(i, letter)
