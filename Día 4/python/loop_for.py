#Están los loops definidos y los indefinidos
#El for y el while 
'''
lista = ["a", "b", "c", "d", "e"]

for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"Letra {numero_letra}: {letra}")
'''
'''
lista = ['Miguel', 'Pedro', 'Pablo', 'Agustin', 'Levi']

for nombre in lista:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print("Nombre que no comienza con L")
'''


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero 
print(mi_valor)    

'''
palabra = 'Python'

for letra in palabra:
    print(letra)

for letra in 'Python': #Es lo mismo que arriba, sin asignar la variable 
    print(letra)
    
'''

'''
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)

''' 
dic = {"clave1": 1, "clave2":2, "clave3":3}

for item in dic.values():
    print(item)

#Ejercicio

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    elif numero % 2 == 1:    
        suma_impares = suma_impares + numero
