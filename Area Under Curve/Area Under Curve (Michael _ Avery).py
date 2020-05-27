# function for integer data sanitation
def integer(prompt, min, max):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            continue
        else:
            if min is None and max is None:
                return user_input
            if min is None:
                if user_input <= max:
                    return user_input
            if max is None:
                if user_input >= min:
                    return user_input


# input function [BONUS]
degree = integer("Please enter the degree of the function: ", 0, None)
function = []
for i in range(degree, -1, -1):
    if i == 0:
        constant = integer("Please enter the constant: ", None, None)
        function.append(constant)
    else:
        coefficient = integer("Please enter the coefficient of x^" + str(i) + ": ", None, None)
        function.append(coefficient)


# define function y
def y(x):
    result = 0
    for i in range(len(function)):
        result += function[i] * x ** (len(function) - i - 1)
    return result


# input integral parameters
lower_bound = integer("Please enter the lower bound: ", None, None)
upper_bound = integer("Please enter the upper bound: ", lower_bound, None)
num_iterations = integer("Please enter the number of iterations: ", 1, None)

# print integral
print()
print("∫" + "[" + str(lower_bound) + ", " + str(upper_bound) + "]", end=" ")
for i in range(len(function)):
    if i == 0:
        if function[i] == 1:
            print("x^" + str(len(function) - i - 1), end="")
        elif function[i] == -1:
            print("-" + "x^" + str(len(function) - i - 1), end="")
        elif function[i] != 0:
            print(str(function[i]) + "x^" + str(len(function) - i - 1), end="")
    else:
        if i == len(function) - 1:
            if function[i] == 0:
                print()
            elif function[i] < 0:
                print(" - " + str(function[i] * -1))
            else:
                print(" + " + str(function[i]))
        elif function[i] == 1:
            print(" + " + "x^" + str(len(function) - i - 1), end="")
        elif function[i] == -1:
            print(" - " + "x^" + str(len(function) - i - 1), end="")
        elif function[i] != 0:
            if function[i] < 0:
                print(" - " + str(function[i] * -1) + "x^" + str(len(function) - i - 1), end="")
            else:
                print(" + " + str(function[i]) + "x^" + str(len(function) - i - 1), end="")

# find the change in x
change_in_x = (upper_bound - lower_bound) / num_iterations

# riemann sums
area_under_curve = 0
x = lower_bound
for i in range(num_iterations):
    area_under_curve += change_in_x * y(x)
    x += change_in_x
print("Riemann sums:", area_under_curve)

# trapezoidal rule [BONUS]
area_under_curve = 0
x = lower_bound
for i in range(num_iterations):
    area_under_curve += change_in_x * ((y(x) + y(x + change_in_x)) / 2)
    x += change_in_x
print("Trapezoidal rule:", area_under_curve)

# simpson's rule [BONUS]
area_under_curve = 0
x = lower_bound
for i in range(num_iterations):
    area_under_curve += change_in_x * ((y(x) + y(x + change_in_x) + y((x + x + change_in_x) / 2) * 4) / 6)
    x += change_in_x
print("Simpson's rule:", area_under_curve)
