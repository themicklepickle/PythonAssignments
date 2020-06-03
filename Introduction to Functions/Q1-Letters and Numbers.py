# Assignment - Introduction to Functions
# Q1-Program that asks the user for a letter and a number and prints out a line of that
#   many of that character in a line.
# Michael Xu

######### FUNCTIONS #########
def line_of_letters(number_, letter_):
    print(number_ * letter_)


######## MAIN PROGRAM ########
number = int(input("Please enter a positive integer: "))
letter = input("Please enter a letter: ")

line_of_letters(number, letter)
