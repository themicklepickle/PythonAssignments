# Assignment - Data Structures and Functions
# Michael Xu
# May 22, 2020


# Q1 - [2] Write a function to return the largest element of a list
def largest_element(input_list):
    largest = input_list[0]
    for element in input_list:
        if element > largest:
            largest = element
    return largest


# Q2 - [2] Write a function find_pos() which takes a list, along with one additional element, as arguments.
# The function should search the list for an element matching the additional element and return the index.
# If there is no match, it should return -1.
# find_pos([1, 2, 3, 4, 5], 3) → 2
# find_pos([1, 2, 3, 4, 5], 8) → -1
def find_pos(input_list, target):
    for index in range(len(input_list)):
        if input_list[index] == target:
            return index
    return -1


# Q3 - [2] Write a function that tests whether a string is a palindrome (same forwards and backwards; e.g.‘kayak’ or 12321).
def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


# Q4 - [2] Write a function that ‘rotates’ a list by k elements. e.g. [1, 2, 3, 4, 5, 6] → [5, 6, 1, 2, 3, 4] is a rotation by 2.
def rotate(input_list, k):
    new_list = input_list.copy()
    for i in range(k):
        new_list.insert(0, new_list.pop(-1))
    return new_list


# Q5 - [3] Write a function that implements the ‘bubble sort’ algorithm to sort a list. The algorithm is as follows:
# 1. Consider each pair of adjacent elements:
# 2. If they are in the correct (ascending) order, move on to the next pair
# 3. If they are not, swap them
# 4. Continue until the list is sorted (no swap operations occurred)
# This function should modify the argument.
def bubble_sort(input_list):
    for i in range(len(input_list) - 1):
        for index in range(len(input_list) - i - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
    return input_list


# Q6 - [2] Write a function that takes a list of strings and prints them all in a frame large enough to hold
# all of the words. For example, [‘‘Hello’’, ‘‘World’’, ‘‘in’’, ‘‘a’’, ‘‘box’’] would be printed as
# *******
# *Hello*
# *World*
# *in   *
# *a    *
# *box  *
# *******
def frame(words):
    width = 0
    for word in words:
        if len(word) > width:
            width = len(word)
    print("*" * (width + 2))
    for word in words:
        word = list(word)
        word.append(" " * (width - len(word)))
        word.insert(0, "*")
        word.append("*")
        word = "".join(word)
        print(word)
    print("*" * (width + 2))


# Q7 - [4] Look up the difference between a shallow copy and a deep copy of a list. Clearly explain the
# difference. Use your new found understanding to re-write the increase by one function so that it no
# longer modifies the argument.
def increase_by_one(some_list):
    new_list = some_list.copy()
    for i in range(len(some_list)):
        new_list[i] += 1
        return new_list


# Q8 - [3] What is sequence unpacking? How can it be used in function arguments? In particular, explain what is going on with
# def a_function(*args, **kwargs):
#   body
"""
Sequence unpacking is a way to assign list, tuple, or dictionary elements to individual variable names. 

List and tuples:
Here is an example of sequence unpacking: a, b, *c = [1, 2, 3, 4, 5]. In this example, 1 is assigned to a, 
2 is assigned to b and the rest of the list elements are assigned to c (as a list). This is particularly 
useful with an arbitrary number of function arguments (*args in the example function). If one were to make
a function that takes an arbitrary number of arguments, the arbitrary number of arguments can be managed
using sequence unpacking. For instance, a function that takes the school name followed by the number of 
students that attend the school followed by the grades of all those students would take an arbitrary number
of arguments, as the number of grades varies depending on the number of students that attend the school. 
When an arbitrary number of arguments are passed into a function, it is taken as a tuple of the individual 
parameters. However, in order to manage the data and differentiate between the school name, number of students,
and the various grades of the students, sequence unpacking can come in handy. As shown in the example of 
sequence unpacking, 3 variables can be used to refer to each of the parts of the arguments.

Dictionaries:
Unlike lists or tuples, dictionary values are referred to in terms of a keyword. So in order to utilize
arbitrary arguments with dictionaries, the ** keyword must be used (**kwargs in the example function).
This passes a dictionary into the function, which is created by assigning values to keys when recalling
the function. For instance, a_function(test=3, greeting="hi", age=15) --> {"test": 3, "greeting":"hi",
"age": 15} This information can be used in the same manner as with lists and tuples, with the added 
benefit of being able to refer to values by keyword rather than index.
"""
