# import os

# # ruta = os.getcwd() #Muestra en la ruta que uno está trabajando
# ruta = os.chdir("C:\\Users\\gambi\\OneDrive\\Escritorio\\practica_python")

# archivo = open("archivo.txt")
# print(archivo.read())

# ruta = "C:\\Users\\gambi\\OneDrive\\Escritorio\\practica_python\\archivo.txt"

# elemento = os.path.basename(ruta)#nombre del archivo
# print(elemento + "\n")

# elemento = os.path.dirname(ruta) #Nombre del directorio
# print(elemento + "\n")

# elemento = os.path.split(ruta)# nombre de ambos en un tupla
# print(elemento)

# os.rmdir('C:\\Users\\gambi\\OneDrive\\Escritorio\\practica_python')
# #Elimina alguna carpeta 

from pathlib import Path

carpeta = Path('C:/Users/gambi/OneDrive/Escritorio/practica_python')
archivo = carpeta / 'archivo.txt'   

mi_archivo = open(archivo)
print(mi_archivo.read())    