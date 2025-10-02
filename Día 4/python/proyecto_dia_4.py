from random import *
#Nombre de jugador
nombre = input("¿Cuál es tu nombre? ")
print(f"Ok, {nombre}, he pensado un número entre el 1 y el 100, y tienes solo 8 intentos para adivinar. ¿cuál crees que es el número?")

intentos = 8
contador_intentos = 0
numero = range(1,101)
numero_secreto = choice(numero)

while intentos > 0:
    numero_usuario = int(input("ingresa un número: "))
    intentos -=1
    contador_intentos +=1
    if (numero_usuario < 1) or (numero_usuario > 100) :
        print(f"El número que eligió no está permitido. Te quedan {intentos} intentos")
    elif (numero_usuario < numero_secreto):
        print(f"Incorrecto, es mayor el número. Te quedan {intentos} intentos")
    elif (numero_usuario > numero_secreto ):    
        print(f"Incorrecto, es menor el número. Te quedan {intentos} intentos")
    elif (numero_usuario == numero_secreto):
        print(f"Haz acertado el número secreto, con {contador_intentos} intentos")
        break  
else:
    print(f"Se te acabaron los intentos, el número secreto era: {numero_secreto}. Juega de nuevo!")             

        
'''
if numero_usuario != numero_secreto:
        intentos -=1
        print(intentos)
        print(numero_secreto)
        if (numero_usuario < 1) or (numero_usuario > 100) :
            print("El número que eligió no está permitido")
        elif (numero_usuario < numero_secreto):
            print("Incorrecto, es mayor el número")
        elif (numero_usuario > numero_secreto ):    
            print("Incorrecto, es menor el número")
        elif (numero_usuario == numero_secreto):
            print(f"Haz acertado el número secreto, con {intentos} intentos")
            break
'''

'''
match numero_usuario == numero_secreto:
            case (numero_usuario < 1) or (numero_usuario > 100):
                print("El número que eligió no está permitido")
            case numero_usuario < numero_secreto:
                print("Su respuesta es incorrecta, su número es menor al número secreto")    
            case numero_usuario > numero_secreto:
                print("Su respuesta es incorrecta, su número es menor al número secreto")
'''