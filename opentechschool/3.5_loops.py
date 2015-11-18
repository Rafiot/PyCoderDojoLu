#!/usr/bin/env python3

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

if __name__ == '__main__':
    house(100)
    exitonclick()
