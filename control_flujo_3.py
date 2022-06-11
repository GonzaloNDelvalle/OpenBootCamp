numeros = []

for i in range(1, 101):
    numeros.append(i)

numeros_reverso = sorted(numeros, reverse=True)
print(numeros_reverso)