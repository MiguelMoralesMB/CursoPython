
#Ejercicio 1
def abrir_leer(archivo):
    archivo = open(archivo, "r")
    return archivo.read()

mi_archivo = abrir_leer("prueba.txt")
print(mi_archivo)

#Ejercicio 2

