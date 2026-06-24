#Estructura de manejo de errores en python 

#try: intenta esto...

#except: si sale mal, haz esto...

#finally: pase lo que pase, haz esto...

def suma():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    print(num1 + num2)
    
    print("Gracias por utilizar nuestro código!" + num1)


try:
    #Código que queremos probar
    suma()
except TypeError: #Tipo de error en consola por tipos de datos distintos
    #Código a ejecutar SI hay un error
    print("Estás concatenado tipos de datos distintos")
except ValueError:
    print("Ese no es un número")
else:
    #Código a ejecutar si NO hay un error.
    print("Hiciste todo bien :)")
finally:
    #Código que se ejecutará de todos modos
    print("Aquí finalizamos!")