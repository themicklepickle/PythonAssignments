#Assignment - More Functions
#Q10 - Function that converts percent grades to letter grades
#Michael Xu
#February 20, 2020

def grade_converter(percent):
    ''' Returns a letter grade (A,B,C,D,F) given a percentage

    Argument can be any positive float less than or equal to 100

    >>> grade_converter(89)
    B
    >>> grade_converter(90)
    A
    '''
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"