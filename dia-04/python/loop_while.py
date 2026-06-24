'''
monedas = 10

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

'''

'''
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir ?? (s/n)")
else:
    print("Gracias")
    
'''

#Palabras clave: pass
#El pass sirve para no dejar vacío el bucle con el cual uno está trabajando

#break: sirve para interrumpir el bucle con la condición que le pongamos
'''
nombre = input("Tu nombres es: ")

for letra in nombre:
    if letra == 'g':
        continue
    print(letra)

'''
    
#continue: este al igual que el break detiene el código pero después de cumplir la 
#condición este sigue con el bucle
'''
nombre = input("Tu nombres es: ")

for letra in nombre:
    if letra == 'g':
        continue
    print(letra)
'''

#Práctica 
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1
    
    
number = 50

while number >= 0:
    if number % 5 == 0:
        print(f"El numero {number} Sí es divisible por 5")
        number -=1
    else:
        number -=1

#Práctica 3

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for element in lista_numeros:
    if element >= 0:
        print(element)
    else:
        break    