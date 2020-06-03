# Assignment - Dictionaries
# Michael Xu
# May 15, 2020

# Q1 - Write a program that outputs the number less than or equal to the one the user entered with the longest Collatz sequence.
# [BONUS] - Make your program efficient enough that it can find the number less than one million in a non-ludicrous amount of time.

import time

sequence = {}  # initiate dict to contain i-sequence length pairs
num = int(input("Please enter a whole number: "))  # user input
start = time.time()  # record start time
for i in range(1, num + 1):
    n = i
    count = 1
    while n != 1 and n not in sequence:  # repeat until n is 1 or the sequence for n has already been determined
        if n % 2 == 0:  # even: n -> n/2
            n /= 2
            count += 1
        else:  # odd: n -> (3n + 1)/2
            n = (n * 3 + 1) / 2
            count += 2
    if n != 1:  # loop broken because the sequence for n has already been found
        sequence[i] = count + sequence[n] - 1  # set key i to count plus the value previously found for n
    else:  # loop broken because n reached
        sequence[i] = count  # set key i to count
longest_seq = sorted(sequence.values())[-1]  # find the longest sequence length by choosing the last element in the sorted list of values
for key in sequence:  # find the key for the longest sequence
    if sequence[key] == longest_seq:
        break
print(f"The number less than or equal to {num} with the longest Collatz sequence is {key}, with a sequence of length {longest_seq}")
print(f"Execution took {time.time() - start} seconds.\n")  # displays the time that the execution took to complete
