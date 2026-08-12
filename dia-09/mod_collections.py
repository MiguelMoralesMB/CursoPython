from collections import Counter, defaultdict, namedtuple

'''
Funcionalidad de la clase Counter del módulo collections, que permite contar 
elementos en un iterable y devolver un diccionario con los
 elementos y sus respectivas cantidades.
'''
numeros = [9, 10, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "Al pan, pan, y al vino, vino"
print(Counter(numeros))
print(Counter(frase.split()))
print(Counter("Parangaricutimiricuaro"))

serie = Counter([1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,5,5,5,5,5,5])

#Listas
print(serie.most_common(3))  # Devuelve los 3 elementos más comunes y sus cantidades
print(serie.items())  # Devuelve un iterable con los elementos y sus cantidades
print(serie.pop(3)) # Devuelve la cantidad del elemento 3 y lo elimina del contador


#Diccionario
mi_diccionario = {"uno": "verde", "dos": "azul", "tres": "rojo"}
mi_diccionario = defaultdict(lambda: "No existe", mi_diccionario)
print(mi_diccionario["cuatro"])
print(mi_diccionario)

#Tuplas
Persona = namedtuple("Persona", ["nombre", "edad", "peso"])
andres = Persona("Andrés", 24, 74)

print(andres.nombre)
print(andres.edad)
print(andres.peso)
print(andres[0])  # Acceso por índice
