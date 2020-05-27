import turtle

sides = int(input("Please enter the number of sides: "))

angle = 180 * (sides - 2) / sides

for x in range(1, sides + 1):
    turtle.fd(50)
    turtle.rt(180 - angle)
