#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# Import everything from the turtle module to the current namespace
from turtle import *

# Declare a speed variable (/!\ cannot be called: speed)
turtleSpeed = 'fast' # Default - “fastest”: 0 - “fast”: 10 - “normal”: 6 - “slow”: 3 - “slowest”: 1

# Set the Speed of the Turtle
speed(turtleSpeed)

# Tint the line Red and the fill Yellow
color('red', 'yellow')

# Make sure our end result is filled
begin_fill()
while True:
  # Move the Turtle 200px forward
  forward(200)
  # Turn 170 degrees left
  left(170)
  # If the absolute position is strictly below 1, exit loop
  if abs(pos()) < 1:
    break
# Once loop is done, do the fill
end_fill()

# End Turtle session
done()