class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad 
        self.color = color
        
        
    def nacer(self):
        print("Este animal a nacido")
        
    
    def hablar(self):
        print("Este animal emite un sonido")
        
    
class Pajaro(Animal):
    
    def  __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print("pio")
        
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(2, "Amarillo")
piolin.nacer()
print(piolin.color)
print("-" *100)
# print(Animal.__subclasses__())

#? Herencia extendida
piolin = Pajaro(2, "Amarillo")
piolin.hablar()

piolin.volar(10)

mi_animal = Animal(4, "Negro")



    
    
