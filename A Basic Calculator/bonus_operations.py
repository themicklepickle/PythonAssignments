# Assignment - A Basic Calculator
# Add, subtract, multiply, divide, modulus, gcd, prime
# Bonus operations module (gcd, prime)
# Michael Xu
# March 22, 2020

# import basic operations module
from basic_operations import *
# import successor module
from successor import *


# gcd
def gcd(a, b):
    """Finds the gcd of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The gcd of a and b.

    Examples:
        >>> print(gcd(10, 25))
        5
        >>> print(gcd(25, 25))
        25
    """
    a_factors = []
    b_factors = []
    shared_factors = []

    for i in range(s(0), s(a)):
        if modulus(a, i) == 0:
            a_factors.append(i)

    for i in range(s(0), s(b)):
        if modulus(b, i) == 0:
            b_factors.append(i)

    for factor in a_factors:
        if factor in b_factors:
            shared_factors.append(factor)

    return shared_factors[subtract(0, s(0))]


# prime
def prime(a):
    """Determines whether or not whole number a is prime.

    Args:
        a (int): A whole number.

    Returns:
        str: "neither prime nor composite" if a is 1, "prime" if a is prime, "composite" otherwise.

    Examples:
        >>> print(prime(16))
        composite
        >>> print(prime(17))
        prime
        >>> print(prime(1))
        neither prime nor composite
    """
    if a == s(0):
        return "neither prime nor composite"
    if a == s(s(0)):
        return "prime"
    for i in range(s(s(0)), a):
        if modulus(a, i) == 0:
            return "composite"
    return "prime"
