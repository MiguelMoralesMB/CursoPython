# Ejercicio 1
def suma_cuadrados(*args):
    total = 0
    for numeros in args:
        total += numeros **2
        
    return total 
        

print(suma_cuadrados(2,4))

# Ejercicio 2

def suma_absolutos(*args):
    suma_absoluto = 0
    for numero in args:
        if numero >= 0:
            suma_absoluto += numero
        elif numero < 0:
            numero = abs(numero)

    
    return suma_absoluto + numero   
        
print(suma_absolutos(5,10,-10,-20))


# Ejercicio 3

def numeros_persona(nombre,*numeros):
    suma_numeros = 0
    for numero in numeros:
        suma_numeros += numero
    
    return f"{nombre}, la suma de tus números es {suma_numeros}"

print(numeros_persona("Miguel",2,3,4,20))