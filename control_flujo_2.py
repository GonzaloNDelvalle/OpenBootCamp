inicio = int(input("Ingrese un numero de inicio: "))
fin = int(input("Ingrese un numero de fin: "))
lista_impares = []

for i in range(inicio, fin + 1):
    if i % 2 != 0:
        lista_impares.append(i)
    
print(lista_impares)
