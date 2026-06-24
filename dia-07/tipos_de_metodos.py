class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    #*Métodos de instancias
    def piar(self):
        print("pio")    
        
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        self.piar()
    
    def pintar_negro(self):
        self.color = "negro"        
        print(f"Ahora el pajaro es {self.color}")
        
    #*Métodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)
        
    #*Métodos estaticos
    @staticmethod
    def mirar():
        print("El pajaro está mirando")
    
#*Métodos de instancias 
piolin = Pajaro("amarillo", "canario")
#?Acceden y modifican atributos de objetos
piolin.pintar_negro()
#?Acceden a otros métodos
piolin.volar(100)
#?Modifican el estado de la clase
piolin.alas = False
print(piolin.alas,"\n")
print("-" *100)

#*Métodos de clase
Pajaro.poner_huevos(3)
#! Pajaro.piar() #Errorr 
print("-" *100)

#*Métodos estaticos
Pajaro.mirar()

#Ejercicio


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas-1
        print(f"Catidad de flechas: {self.cantidad_flechas}")
        

robin_hood = Personaje(10)
robin_hood.lanzar_flecha()

#! DRY: DONT'T REPEAT YOURSELF  