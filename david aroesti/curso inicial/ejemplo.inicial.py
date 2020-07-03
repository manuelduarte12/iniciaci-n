# -*- coding: utf-8 -*-

import tutle

def main():
    window = tutle.Screen()
    dave = turtle.Turtle()

    make_square(dave)


def make_square(dave):
    make_line_and_turn(dave, 100)

def make_line_and_turn(dave, lenth):
    dave.forward(length)
    dave.left(90)


if _name_ == "__main__":
  main

