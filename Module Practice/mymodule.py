def num_factors(number_):
    '''Returns the number of factors that a number has

    Parameter can be any positive integer

    >>> num_factors(73)
    2
    >>> num_factors(72)
    12
    '''
    factors = 0
    for i in range(1, number_ + 1):
        if number_ % i == 0:
            factors += 1
    return factors

def is_prime(number_):
    '''Returns a True boolean if the number is prime, otherwise returns a False boolean

    Parameter can be any positive integer

    >>> is_prime(12)
    False
    >>> is_prime(7)
    True
    '''
    for i in range(2, number_):
        if number_ % i == 0:
            return False
    return True