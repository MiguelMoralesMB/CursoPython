
#*El encapsulamiento es guardar métodos y atributos de una clase para que no sean vistos desde el exterior
#*Y se hace agregando dos "_" antes del nombre


class Persona:
    atributo_publico = "Mostrar"   # Accesible desde el exterior
    __atributo_privado = "Oculto"  # No accesible
    
    # No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este método está oculto")
        self.__variable = 0
        
    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__metodo_oculto()
        
alumno = Persona()
# alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
alumno.metodo_normal()      # Este método es accesible

#?Truco para acceder a atributos y métodos ocultos.
#?Con esta sintaxis: instancia + _ + NombreClase + método/atributo oculto
alumno._Persona__metodo_oculto()
print(alumno._Persona__atributo_privado)
print("*" * 50, "\n")

#*Otro ejemplo de encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # El doble guion bajo "__" protege la variable
        self.__saldo = saldo_inicial 

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
            
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro exitoso.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

mi_cuenta = CuentaBancaria("Ana", 100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(100)
# mi_cuenta._CuentaBancaria__saldo()
print(mi_cuenta._CuentaBancaria__saldo) #Se pudo vulnerar para ver el saldo.
# print(mi_cuenta.__saldo) <-- ESTO DARÁ ERROR. El saldo está oculto y protegido.