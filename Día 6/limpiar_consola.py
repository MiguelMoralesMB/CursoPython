from os import system


nombre = input("Ingresa tu Nombre: ")
edad = input("Ingresa tu Edad: ")

#Método de os para limpiar la terminal
#En Windows se ocupa "cls" como argumento, pero en MacOs se ocupa "clear"
system("cls")

print(f"Tu nombre es: {nombre} y tienes {edad} años")

