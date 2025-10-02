from random import *
'''
Importante que la librería que importamos NO tenga el 
mismo nombre que el archivo que estamos ocupando.
EJ:
    como ahora estamos ocupando la librería 'random', nosotros
    le colocamos 'Random' con mayúscula para que no ocurra 
    ningún error.
'''

aleatorio = randint(1,50) #numero  aleatorio entero desde el 1 al 50
aleatorio_2 = round(uniform(1, 5),2) #aleatorio con floats
nuevo_aleatorio = random()
print("Esto es utilizando el método randint()", aleatorio)
print("Esto es utilizando el método uniform()", aleatorio_2)
print("Esto es utilizando el método random()", nuevo_aleatorio)
print('\n')

# método choiche() escoge algo al azar.
colores = ['Azul', 'Morado', 'Verde', 'Amarillo']
aleatorio_3 = choice(colores)
print("Esto es utilizando el método choice() ",aleatorio ,'\n') # método choiche() escoge algo al azar.

#Shuffle() mezcla los valores
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
