#!/usr/bin/env python3

"""
Draw stuff
"""

from turtle import *
import random


def draw_star(x=0, y=0):
    '''
        Draw a star
    '''
    penup()
    setpos(x, y)
    endx, endy = pos()
    pendown()
    color('red', 'yellow')
    while True:
        forward(100)
        left(170)
        if distance(endx, endy) < 1:
            break


def draw_stars(nb=2):
    '''
        Draw a bunch of stars
    '''

    r = random.Random()
    for i in range(nb):
        begin_fill()
        x = r.randint(-200, 200)
        y = r.randint(-200, 200)
        draw_star(x, y)
        end_fill()
    done()


def say_bye(x, y):
    bye()


if __name__ == '__main__':

    onclick(say_bye)
    draw_stars(2)
