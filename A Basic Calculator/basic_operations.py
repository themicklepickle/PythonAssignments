# Assignment - A Basic Calculator
# Add, subtract, multiply, divide, modulus, gcd, prime
# Basic operations module (add, subtract, multiply, divide, modulus)
# Michael Xu
# March 22, 2020

# import successor module
from successor import *


# add
def add(a, b):
    """Finds the sum of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The sum of a and b.

    Example:
        >>> print(add(10, 25))
        35
    """
    sum = 0
    for i in range(a):
        sum = s(sum)
    for i in range(b):
        sum = s(sum)
    return sum


# subtract
def subtract(a, b):
    """Finds the difference of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The difference of a and b.

    Examples:
        >>> print(subtract(25, 10))
        15
        >>> print(subtract(10, 25))
        -15
    """
    if a == b:
        return 0
    else:
        difference = 0
        for i in range(b, a):
            difference = s(difference)
        if difference == 0:
            for i in range(a, b):
                difference = s(difference)
            difference = ["-", str(difference)]
            difference = int("".join(difference))
            return difference
        else:
            return difference


# multiply
def multiply(a, b):
    """Finds the product of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The product of a and b.

    Example:
        >>> print(multiply(10, 25))
        250
    """
    product = 0
    for i in range(a):
        for i in range(b):
            product = s(product)
    return product


# divide
def divide(a, b):
    """Finds the quotient of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The quotient of a and b.

    Example:
        >>> print(divide(25, 10))
        3
    """
    if a == b:
        return 1
    elif b == s(0):
        return a
    else:
        quotient = 0
        count = s(0)
        test = 0
        while True:
            for i in range(count, a):
                test = s(test)
            if test == 0:
                break
            test = 0
            for i in range(b):
                count = s(count)
            quotient = s(quotient)
        return quotient


# modulus
def modulus(a, b):
    """Finds the modulus of whole numbers a and b.

    Args:
        a (int): The first whole number.
        b (int): The second whole number.

    Returns:
        int: The modulus of a and b.

    Example:
        >>> print(modulus(25, 10))
        5
        >>> print(modulus(10, 25))
        10
    """
    if a == b:
        return 0
    else:
        modulus = 0
        count = 0
        test = 0
        while True:
            for i in range(count, a):
                test = s(test)
            if test == 0:
                break
            test = 0
            for i in range(b):
                count = s(count)
        if count == a:
            return 0
        for i in range(b):
            a = s(a)
        for i in range(count, a):
            modulus = s(modulus)
        return modulus
