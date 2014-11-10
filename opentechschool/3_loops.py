#!/usr/bin/env python

from turtle import *

def arrow(parts, progress=10):
    for i in range(parts):
        forward(progress + i)
        penup()
        forward(progress - i)
        pendown()


if __name__ == '__main__':
    arrow(7)
    exitonclick()
