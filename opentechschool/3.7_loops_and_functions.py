#!/usr/bin/env python

from turtle import *
import math


def square(side):
    for i in range(4):
        forward(side)
        right(90)


def house(side):
    square(side)
    right(45)
    hypotenuse = math.sqrt(2 * (side ** 2))
    forward(hypotenuse)
    right(135)
    forward(side)
    right(135)
    forward(hypotenuse)
    for i in range(2):
        left(90)
        forward(hypotenuse / 2)


def village(number):
    for i in range(number):
        house(100)
        penup()
        setx(xcor() - 150)
        pendown()
        left(135)


if __name__ == '__main__':
    penup()
    setx(300)
    pendown()
    village(5)
    exitonclick()