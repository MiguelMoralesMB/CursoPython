edad = 16
calificacion = 6.5

if calificacion >= 6.0:
    print("Has aprobado el año escolar")
elif calificacion == 5.95:
    print("Has reprobado el año escolar")    
else:
    print("Has reprobado el año escolar")    
print("\n")

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 4.0:
        print("Aprobado")
    else:
        print("Rechazado")        
else:
    print("Eres mayor de edad")

#Ejercicios Udemy
#Ejercicio 1.
'''
num1 = int(input("Ingrese un número:"))
num2 = int(input("Ingrese otro número:"))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(num1, " es mayor que ", num2)
elif num2 > num1:
    print(num2, " es mayor que ",num1)   
elif num1 == num2:
    print(num1," y ", num2, " son iguales")    
'''    
#Ejercicio 2.
'''
edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if (edad >= 18) and (tiene_licencia == True):
    print("Puedes conducir")
elif (tiene_licencia == False) and (edad < 18):
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")      
elif (edad >= 16) or (tiene_licencia == True):
    print("No puedes conducir. Necesitas contar con una licencia")
'''
#Ejercicio 3.
habla_ingles = True
sabe_python = False

if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif (habla_ingles == False) and (sabe_python == False):    
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif (habla_ingles == False) or (sabe_python == True):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif (habla_ingles == True) or (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")


"Para postularte, necesitas saber programar en Python"
