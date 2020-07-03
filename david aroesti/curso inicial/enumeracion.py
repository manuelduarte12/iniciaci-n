objetivo = int(input("por favor elige un numero: "))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f"la raiz cuadrada de {objetivo}  es {respuesta}")
else:
    print(f"el {objetivo} no tiene una raiz cuadrada")