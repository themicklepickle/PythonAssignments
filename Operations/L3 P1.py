import turtle
turtle.shape("arrow")

length = float(input("What is the length: "))
width = float(input("What is the width: "))

length += 10
width *= 5

turtle.forward(length)
turtle.lt(90)
turtle.forward(width)
turtle.lt(90)
turtle.forward(length)
turtle.lt(90)
turtle.forward(width)
