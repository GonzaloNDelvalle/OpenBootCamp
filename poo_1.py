class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

miAuto = Coche()
miAuto.cilindrada = 2
miAuto.velocidad = 210
miAuto.puertas = 5
miAuto.color = "Rojo"
miAuto.ruedas = 4

print(f"Caracteristicas del auto: Cilindrada: {miAuto.cilindrada} litros\nVelocidad maxima: {miAuto.velocidad}\nCantidad de puertas: {miAuto.puertas}\nCantidad de ruedas: {miAuto.ruedas}\nColor: {miAuto.color}")