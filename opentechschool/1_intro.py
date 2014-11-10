#!/usr/bin/env python

from turtle import *
from time import sleep


speed(1)

forward(300)
sleep(2)

left(30)
sleep(2)

forward(200)
sleep(2)

right(50)
sleep(2)

backward(400)


# Let's make it a turtle
input()

clear()
shape("turtle")
sleep(2)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)


# The line is a bit small
input()
pensize(5)
backward(300)
left(30)

input()

color('red', 'yellow')
sleep(2)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)

penup()


# let's draw a bit more
input()

forward(500)
pendown()

begin_fill()
left(20)

forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
forward(50)
left(90)

left(30)

forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)

left(40)

forward(75)
left(90)
forward(75)
left(90)
forward(75)
left(90)
forward(75)
left(90)

# ... And fill it
input()
end_fill()


exitonclick()
