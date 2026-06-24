#Operaciones de cuenta bancaria
class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_de_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance
        
    def __str__(self):
        return f"Nombre completo: {self.nombre} {self.apellido}\nTu Número de Cuenta es: {self.numero_de_cuenta}\nTu balance es: ${self.balance}"
    
    def depositar(self, cantidad):
        self.balance = self.balance + cantidad
        return self.balance
    
    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("No puedes retirar mas dinero del que tienes en la cuenta")
        else:
            self.balance = self.balance - cantidad
        

def crear_cliente():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    numero_de_cuenta = input("Escribe tu número de cuenta: ")
    balance_inicial = int(input("Escribe tu balance inicial: "))
    
    nuevo_cliente = Cliente(nombre, apellido, numero_de_cuenta, balance_inicial)
    
    return nuevo_cliente
    


def inicio_cuenta():
    print("*" * 50 )
    print("*" * 12 + " Bienvenido a tu Cuenta Bancaria " + "*" *13)
    print("*" * 50 + "\n" )
    
    cliente = crear_cliente()
    
    inicializar_cuenta = False
    while not inicializar_cuenta:
        print("Elige el número de los que desearas hacer: ")
        print('''
              [1] - Depositar Dinero
              [2] - Retirar Dinero
              [3] - Mostrar Balance
              [4] - Salir de la cuenta ''')
        
        eleccion_usuario = int(input())
        
        if eleccion_usuario == 1:
            monto_deposito = input("Monto a depositar: ")
            cliente.depositar(int(monto_deposito))
            print("Monto depositado correctamente :)")
        elif eleccion_usuario == 2:
            monto_retiro = input("Monto a retirar: ")
            cliente.retirar(int(monto_retiro))
        elif eleccion_usuario == 3:
            print(f"Tu balance es de: {cliente.balance}")
        elif eleccion_usuario == 4:
            print("Gracias por contar con nosotros!")
            inicializar_cuenta = True
        

inicio_cuenta()            
# cliente_pedro = Cliente("Miguel", "Morales", "001", 250)
# print(cliente_pedro)
# cliente_pedro.depositar(50)
# print(cliente_pedro)
# cliente_pedro.retirar(100)
# print(cliente_pedro)

