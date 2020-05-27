#General setup
import turtle
turtle.setup(width=500, height=500, startx=380, starty=100)
turtle.title("Tic Tac Toe")

from turtle import *
grid = Turtle()
grid.shape("blank")
grid.pensize(4)

#Functions
def f():
    print("enter")

def xProgram(turtleName, pos):
    entered = False
    turtleName = Turtle()
    turtleName.speed(0)
    turtleName.shape("blank")
    turtleName.pen(pensize=4, pencolor="red")
    turtleName.up()
    turtleName.setpos(-pos, pos)
    turtleName.pendown()
    turtleName.setpos(pos, -pos)
    turtleName.up()
    turtleName.setpos(pos, pos)
    turtleName.pendown()
    turtleName.setpos(-pos, -pos)
    while entered == False:
        turtle.onkeypress(f,"a")

#Grid
grid.speed(0)
grid.up()
grid.setpos(-250, 85)
grid.pendown()
grid.setpos(250, 85)
grid.up()
grid.setpos(-250, -83)
grid.pendown()
grid.setpos(250, -83)
grid.up()
grid.setpos(-86, 250)
grid.pendown()
grid.setpos(-86, -250)
grid.up()
grid.setpos(83, 250)
grid.pendown()
grid.setpos(83, -250)

#X1
xProgram("X1", 50)
