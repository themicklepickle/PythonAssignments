# Assignment - lists and tuples
# Q1 - Dice rolling
# Michael Xu
# 21 April 2020

# import module for random numbers
import random

# list for counting the number of times each number appears
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# user input for number of times to roll
rolls = int(input("Please enter the number of times that you wish to roll the dice: "))

# roll dice and count the number that appears
for i in range(rolls):
    dice1 = random.randint(0, 5)
    dice2 = random.randint(0, 5)
    counter[dice1 + dice2] += 1

# print results
for i in range(len(counter)):
    print(i + 2, ":", "*" * counter[i])
