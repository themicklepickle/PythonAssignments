#Assignment - More Functions
#Q9 - Lambda function that takes in the lengths of two legs of a right triangle and returns the length of the hypotenuse
#Michael Xu
#February 20, 2020

hypotenuse = lambda leg_a, leg_b: (leg_a ** 2 + leg_b ** 2) ** 0.5

''' Returns the length of the hypotenuse of a right triangle, given the lengths of the other two legs

    Arguments can be any two positive floats

    >>> hypotenuse(10.5, 8)
    13.200378782444085
    >>> hypotenuse(3, 4)
    5.0
'''