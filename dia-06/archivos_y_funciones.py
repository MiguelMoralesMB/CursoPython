from pathlib import Path

#Ejercicio 1
def abrir_leer(archivo):
    archivo = open(archivo, "r")
    return archivo.read()

mi_archivo = abrir_leer("prueba.txt")
print(mi_archivo)

#Ejercicio 2

def sobreescribir(archivo):
    archivo = open(archivo, "w")
    
    return archivo.write("Contenido eliminado")

mi_archivo = sobreescribir("prueba1.txt")

#Ejercicio 3

def registro_error(archivo):
    archivo = open(archivo, "a")
    return archivo.write("se ha registrado un error de ejecución")
    
print(registro_error("prueba.txt"))


ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)