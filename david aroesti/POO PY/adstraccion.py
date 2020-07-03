# -*- coding: utf-8 -*-
import random


def run():
    number_found = False
    random_number = random.randint(0, 451)

    while not number_found:
        number = int(input("Intenta un número: "))

        if number == random_number:
            print("Felicidades ¡encontrastes el número")
            number_found = True
        elif number > random_number:
            print("El número es mas pequeño ")
        else:
            print("El número es mas grande ")


if __name__ == "__main__":
    run()
