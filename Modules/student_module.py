# Assignment - custom
# Q1 - Module for prime factorization
# Michael Xu
# February 28 2020

def next_prime(current_prime):
    '''returns the next prime number after the given argument

    argument can be any positive integer

    >>> next_prime(30)
    31
    >>> next_prime(31)
    37
    '''
    i = current_prime + 1
    while True:
        is_prime = True
        for x in range(2, i):
            if i % x == 0:
                is_prime = False
        if is_prime == True:
            return i
        else:
            i += 1


def num_times_divisible(user_num_, prime_):
    '''returns the number of times that a number is divisble by another number

    arguments can both be any positive integer

    >>> num_times_divisible(24, 2)
    3
    >>> num_times_divisible(1250, 5)
    4
    '''
    count = 0
    while True:
        if user_num_ % prime_ == 0:
            count += 1
            user_num_ /= prime_
        else:
            return count
