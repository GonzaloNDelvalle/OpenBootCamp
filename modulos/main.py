from paquete import operaciones

def main():
    sumar = operaciones.suma(3, 5)
    restar = operaciones.resta(7, 2)
    multiplicar = operaciones.mult(4, 5)
    dividir = operaciones.div(15, 3)
    print(f"suma: {sumar}\nresta: {restar}\nmultiplicacion: {multiplicar}\ndivision: {dividir}")

main()
