# -*- coding: utf-8 -*-


def suma_recursive(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursive(n-1)


def run():
    number = int(input("Por favor escribe un numero: "))
    result = suma_recursive(number)
    print("la suma del numero es {}". format(result))


hello = str(input("hello, esta listo"))

if __name__ == "__main__":
    run()
