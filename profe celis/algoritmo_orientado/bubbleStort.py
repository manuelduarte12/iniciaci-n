# 1.- Comenzar a hacer comparaciones de elementos adyacentes
# 2. -Repetir buclear hasta tener un swap


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        print(array)
        for j in range(0, n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [190, 120, 12, 3, 124, 5, 12, 220, 4565, -21, -54]
bubble_sort(array)

print("El arreglo ordenado de forma accenden es de : ")
for i in range(len(array)):
    print("%d" % array[i]),
