# Ejercicio 2

'''
Crea una función llamada reducir_lista() que tome una 
lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados 
(dejando uno solo de los números si hay repetidos)
y eliminando el valor más alto.
El orden de los elementos puede modificarse.

    "Por ejemplo, si se le proporciona la lista [1,2,15,7,2]
    debe devolver [1,2,7]."

Crea una función llamada promedio() que pueda recibir 
como argumento la lista devuelta por la anterior función,
y que calcule el promedio de los valores de la misma.
Debe devolver el resultado, sin imprimirlo.
'''

# Lista de números 
lista_numeros = [9,2,7,4,7,5,2]
    
# Reducir la cantidad de números en la lista.

def reducir_lista(lista):
    """Devuelve la misma lista, eliminando los duplicados
    y eliminando el valor mas alto"""
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    
    return lista

#Calcular Promedio de números restantes en la lista

def promedio(lista):
    suma = 0
    for numeros in lista:
        suma = suma + numeros
        
    calcular_prom = suma / len(lista)
    
    return calcular_prom


lista_reducida = reducir_lista(lista_numeros)
calculo_prom = promedio(lista_reducida)
print(f"Tu promedio de la lista reducidad que era: {lista_reducida} fue de: {calculo_prom}")
