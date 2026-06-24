class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(self.nombre + " dice muuu")
        
class Oveja:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(self.nombre + " dice beee")
        

vaca1 = Vaca("Antonia")
oveja1 = Oveja("Alfonsa")

# vaca1.hablar()
# oveja1.hablar()
 
# animales = [vaca1, oveja1]       

# for animal in animales:
#     animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

#*Ejercicio 

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

def iterador(*args):
    for arg in args:
        print(len(arg))
    
iterador(palabra, lista, tupla)