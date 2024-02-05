class Estudiante:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__calificacion = 0

    def set_nombre(self, n):
        self.__nombre = n
    def get_nombre(self):
        return self.__nombre
    def set_edad(self, e):
        self.__edad = e
    def get_edad(self):
        return self.__edad
    def set_calificacion(self, c):
        self.__calificacion = c
    def get_calificacion(self):
        return self.__calificacion   
      
    def aprobado(self):
        return True if self.get_calificacion() >= 60 else False
e = Estudiante()
e.set_nombre(input("Ingrese su nombre: "))
e.set_edad(int(input("Ingrese su edad: ")))
e.set_calificacion(float(input("Ingrese su nota: ")))
if e.aprobado():
    print(f"{e.get_nombre()} esta aprovado con una nota de {e.get_calificacion()}")
else:
    print(f"{e.get_nombre()} no esta aprovado con una nota de {e.get_calificacion()}")



    