# Assignment - More Functions
# Q11 - Function that takes in an int and determines whether or not it is a perfect square
# Michael Xu
# February 20, 2020


def perfect_square(num):
    """ Returns a True boolean if the argument is a perfect square, otherwise returns a False boolean

    Argument can be any integer (positive/negative)

    >>> perfect_square(81)
    True
    >>> perfect_square(83)
    False
    """
    if num ** 0.5 % 1 == 0:
        return True
    else:
        return False
