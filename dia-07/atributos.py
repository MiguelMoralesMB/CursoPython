class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):#Estos son los  parámetros
        self.color = color  #'self.color' este es el atributo que quiero que sea igual a mi parametro color
        self.especie = especie
        pass
    
mi_pajaro = Pajaro("Rojo", "Tucan")

'''Estos son los atributos de instancia, porque los
atributos pueden cambiar según el valor que le agregues'''

print(mi_pajaro.color)
print(mi_pajaro.especie)

'''
Todos los objetos comparten los mismos atributos de clase 
'''
print(Pajaro.alas)
print(mi_pajaro.alas)


