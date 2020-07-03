# -*- coding: utf-2 -*-


def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_words = ''.join(reversed_letters)

    if reversed_words == word:
        return True

        return False


if __name__ == "__main__":
    word = str(input("Escribe una palabara:  "))

    result = palindrome(word)

if result is True:
    print("{} si es un palíndromo." .format(word))
else:
    print("{} no es un palíndromo. " .format)
