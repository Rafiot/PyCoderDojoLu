#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

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