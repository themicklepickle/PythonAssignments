# Assignment - lists and tuples
# Q5 - Ask the user for a set of positive numbers and appends them to a lists
# Michael Xu
# 21 April 2020

# initiate list of numbers
num_list = []

while True:
    # user input
    num = float(input("Please enter a number (positive to add to list, negative to print list): "))

    # append num to list if num > 0
    if num > 0:
        num_list.append(num)

    # print num_list if num < 0
    elif num < 0:
        print(num_list)
        break
