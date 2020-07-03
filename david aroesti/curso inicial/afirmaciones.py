def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f"{palabra} no es un frase"
        assert len(palabra) > 0, "no se permite st vacio"
        primeras_letras.append(palabras[0])

    return primeras_letras


lista_de_palabras = ["perro", "vaca", "gato"]
palabras = list(primera_letra(lista_de_palabras))
print(palabras)