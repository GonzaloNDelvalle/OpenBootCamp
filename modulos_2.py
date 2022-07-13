import time

def horaTrabajo():
    horaActual = time.localtime()[3]
    if horaActual >= 7:
        print("Es hora de ir a casa")
    else:
        print(f"faltan {7 - horaActual} horas para ir a casa")

horaTrabajo()