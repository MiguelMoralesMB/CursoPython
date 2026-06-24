def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(10,90)
#resultado = multiplicar("Hola", "9")
print(resultado, '\n')

dolares = 1200

def usd_a_eur(dolares):
    return dolares * 0.90
    

palabra = "Hola Mundo"

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra


def chequear_3_palabras(lista):
    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
        
    return lista_3_cifras
    


resultado_chequear = chequear_3_palabras([21,772,800])
print(resultado_chequear)
    
    
#Ejercicio 1

#lista_numeros = [-8, 10, 15, -18, 23, -4, -1]

def todos_positivos(lista):
    
    for num in lista:
        if num <= 0:      
            return False
    
    return True
        

        
resultado = todos_positivos([10,19,12])
print(resultado)

# Ejercicio 2

# lista_numeros_2 = [5, 10, 15, 10, 20, -100]

# def suma_menores(lista):
    
#    for numero in lista_numeros_2:
#        suma = suma + numero
#        while numero > 0 and numero < 1000:
#            return lista
       

# print(suma_menores(lista_numeros_2))        

lista_numeros_2 = [1,50,500,5000,750,600]
 
def suma_menores(lista_numeros_2):
    suma = 0 
    for numero in lista_numeros_2:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma

print(suma_menores(lista_numeros_2))

# def suma_menores(lista):
    
#    for numero in lista_numeros:
#        suma = suma + numero
#        while numero > 0 and numero < 1000:
#            return lista
       
# Ejercicio 3
'''
Crea una función (cantidad_pares) que cuente la 
cantidad de números pares que existen en una lista
(lista_numeros), y devuelva el resultado de dicha 
cuenta.
'''     

lista_numeros = [8, 17, 15, 19, 10, 4, 5, 3]

def cantidad_pares(lista_numeros):
    cantidad_numero = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad_numero += 1
        else: 
            pass
    
    return cantidad_numero

numeros_pares = cantidad_pares(lista_numeros)
print(numeros_pares)


