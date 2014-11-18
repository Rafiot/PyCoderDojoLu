#!/usr/bin/env python

from turtle import *
color('magenta', 'blue')

def drawSquare(size):
	count = range(0,4)
	begin_fill()
	for step in count:
		print(step)
		forward(size)
		left(90)
	end_fill()
	done()

def main():
	drawSquare(100)

if __name__ == "__main__": main()