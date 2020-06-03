# imports the turtle graphics module to draw things
import turtle

# asks the user for an integer for the number of sides and the input is stored as n
n = int(input("Please enter an integer for the number of sides: "))

# asks the user for an integer for the number of repitition and the input is stored as r
r = int(input("Please enter an integer for the number of repititions: "))

# calculates the interior angle of the polygon with n number of sides
interiorAngle = ((n - 2) * 180) / n

# subtracts the interior angle from 180° to determine the amount to turn at each vertex
interiorAngle = 180 - interiorAngle

# draws the polygon r number of times
for i in range(r + 1):

    # draws each side of the polygon by repeating the same process n + 1 number of times
    for x in range(n):
        # goes straight to draw a side
        turtle.fd(100)

        # turns the proper amount as calculated above
        turtle.lt(interiorAngle)

    # offsets each polygon by 10°
    turtle.lt(10)
