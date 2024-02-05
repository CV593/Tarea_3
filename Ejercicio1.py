class Numeros:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def set_a(self, a):
        if isinstance(a, (int, float)):
            self.__a = a
        else:
            print("Error: El valor de 'a' debe ser un número.")
    def set_b(self, b):
        if isinstance(b, (int, float)):
            self.__b = b
        else:
            print("Error: El valor de 'b' debe ser un número.")
    def sumar(self):
        return self.get_a() + self.get_b()
    def restar(self):
        return self.get_a() - self.get_b()
    def multiplicar(self):
        return self.get_a() * self.get_b()
    def dividir(self):
        try:
            if self.get_b() == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return self.get_a() / self.get_b()
        except ZeroDivisionError as e:
            print(f"Error: {e}")
hijo = Numeros()
hijo.set_a(float(input("Ingrese un numero a: ")))
hijo.set_b(float(input("Ingrese un numero b: ")))   

print(f"\n\nResultados\nValor de a: {hijo.get_a()}")
print(f"Valor de b: {hijo.get_b()}")
print(f"Suma: {hijo.sumar()}")
print(f"Resta: {hijo.restar()}")
print(f"Multiplicación: {hijo.multiplicar()}")
print(f"División: {hijo.dividir()}")         
            
                    