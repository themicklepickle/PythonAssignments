# Assignment - Slicing and Comprehension
# Michael Xu
# May 5, 2020

# Q1 - Given
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# find values for <1>, <2>, and <3> such that
# x[<1>:<2>:<3>] = [4, 6, 8]
# <1>: 3
# <2>: 9
# <3>: 2


# Q2 - Create a list of all the numbers from 1-100
x = [i for i in range(1, 100)]
print(x)


# Q3 - Create a list of all of the even numbers from 1-100
x = [i for i in range(1, 100) if i % 2 == 0]
print(x)


# Q4 - Create a list of the perfect squares from 1-100
x = [i ** 2 for i in range(1, 100) if i ** 2 < 100]
print(x)


# Q5 - Given a number x, use list comprehension to make a list of all of the divisors of x
x = 30  # example value for x
divisors = [num for num in range(1, x + 1) if x % num == 0]
print(divisors)


# Q6 - Create a list that contains all of the numbers between 2000 and 3200 which are divisible by 7 but not by 5
x = [i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0]
print(x)


# Q7 - Create a list of all the non-space characters in a string s
s = "Hello World !"  # example value for s
x = [letter for letter in s if letter != " "]
print(x)


# Q8 - Create a list of all numbers 1-1000 that have a 3 in them
x = [i for i in range(1, 1000) if "3" in str(i)]
print(x)


# Q9 - Use a nested list comprehension to find all the numbers 1-1000 that are divisible by any single digit number apart from 1
x = [[i for i in range(1, 1000) if i % j == 0] for j in range(2, 10)]
print(x)


# BONUS - Write a single-line list comprehension to implement the Sieve of Eratosthenes to create a list of all of the prime numbers 1-1000
primes = [i for i in range(2, 10000) if i not in [j*k for j in range(2, 10000) for k in range(2, 10000//j+1)]]
print(primes)
