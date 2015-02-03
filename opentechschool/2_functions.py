#!/usr/bin/env python3

from turtle import *
import math


def house(side):
    forward(side)
    right(90)
    forward(side)
    right(90)
    forward(side)
    right(90)
    forward(side)
    right(135)
    hypotenuse_center = math.sqrt(side ** 2 + side ** 2)
    forward(hypotenuse_center)
    right(135)
    forward(side)
    right(135)
    forward(hypotenuse_center)
    left(90)
    forward(hypotenuse_center / 2)
    left(90)
    forward(hypotenuse_center / 2)


if __name__ == '__main__':
    house(100)
    penup()
    setx(xcor() - 200)
    pendown()
    left(135)
    house(100)
    exitonclick()
