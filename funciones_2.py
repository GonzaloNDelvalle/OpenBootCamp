def num_primo(numero):
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    if numero == 1 or divisores == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")
