import turtle
from turtle import *
turtle.shape("arrow")
turtle.lt(90)

#original assignment
length = 100

for x in range(3):

    turtle.setpos(0, 0)
    turtle.lt(x * 30)
    
    for y in range(3):
        turtle.fd(length)
        turtle.rt(90)

    turtle.fd(length)
    turtle.rt(90 + x * 30)


'''
#small and big squares with color fill
length = 100

for x in range(3):

    turtle.setpos(0, 0)
    turtle.lt(x * 30)

    color('red')
    begin_fill()
    
    for y in range(3):
        turtle.fd(length)
        turtle.rt(90)

    end_fill()
        
    turtle.fd(length)
    turtle.rt(90)

    color('yellow')
    begin_fill()
    
    for z in range(3):

        turtle.fd(length/4)
        turtle.rt(90)

    end_fill()
        
    turtle.rt(90 + x * 30)
'''

'''
#alternating squares
for x in range(11):

    if x % 2 == 0:
        length = 100
    else:
        length = 25

    turtle.setpos(0, 0)
    turtle.lt(x * 30)

    for y in range(3):
        turtle.fd(length)
        turtle.rt(90)
        
    turtle.fd(length)
    turtle.rt(90 + x * 30)
'''
