#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

from turtle import *

print("Click on the main window and press the up arrow key :)")

def f():
  forward(50)
  left(60)

onkey(f, "Up")
listen()
mainloop()