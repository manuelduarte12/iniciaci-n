objetivo = int(input("escoje un numero: "))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontro la raiz cuadrada del {objetivo}")
else:
    print(f"la raiz cuandrada de {objetivo} es {respuesta}")
