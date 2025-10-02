from random import *
# Lista inicial
palitos = ["-", "--", "---", "----"]

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = ""
    
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un numero del 1 al 4: ")
    
    return int(intento)    


# Comprobar intento
def chequear_intento(lista, intento):

    if lista[intento -1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")    
        
    print(f"Te ha tocado {lista[intento -1]}")

    
# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)

# Ejercicio 1

'''
- Crea una función (lanzar_dados) que arroje 
dos dados al azar y devuelva sus resultados:

    La función debe retornar dos valores resultado,
    que se encuentren entre 1 y 6).

    Dicha función no debe requerir argumentos para 
    funcionar, sino que debe generar internamente 
    los valores aleatorios.

- Proporciona el resultado de estos dos dados a una función
que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) 
y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6: 
    "La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:
    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:
    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


Pistas: utiliza el método choice o randint de la biblioteca random
para elegir un valor al azar entre 1 y 6.
'''


# Función de arrojar_dados, que arrojará 2 dados al azar.
def lanzar_dados():
    return randint(1,6), randint(1,6)


# Función de evaluar_jugada.
def evaluar_jugada(dado_1, dado_2):
    suma_dados = dado_1 + dado_2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
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

#Función de reducir_lista()
lista_numeros = [9,2,7,4,7,5,2]
print(len(lista_numeros))

def reducir_lista(lista):
    """Devuelve la misma lista, eliminando los duplicados
    y eliminando el valor mas alto"""
    for n in lista:
        if n in lista[0] == max(lista):
            lista.pop

    
    
    