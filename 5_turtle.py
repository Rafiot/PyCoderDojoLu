#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

from turtle import *
color('magenta', 'blue')
count = range(0,4)
begin_fill()
for step in count:
  print(step)
  forward(200)
  left(90)
end_fill()
done()