numeros = [9, 2, 1, 4, 6]

for item in range(len(numeros) - 1):
    j = item
    while j >= 0:
        if numeros[j+1] < numeros[j]:
            aux = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = aux
            j -= 1
        else:
            j = -1

mediana = len(numeros) // 2

print(numeros[mediana])