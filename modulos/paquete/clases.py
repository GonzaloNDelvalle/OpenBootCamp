class Alumno:
    nombre = ""
    nota = ""

    def __init__(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.nota = input("Ingrese la nota del alumno: ")
    
    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de {self.nota}")
        if self.nota >= '7':
            print("El alumno esta aprobado")
        else:
            print("El alumno esta desaprobado")