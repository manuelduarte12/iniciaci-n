# -*- coding: utf-8 -*-

import turtle


def main():
    windows = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)
    turtle.mainloop()


def make_square(dave):
    length = int(input("tamaño de cuadrado:"))

    for i in range(5):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(520)


if __name__ == "__main__":
    main()
