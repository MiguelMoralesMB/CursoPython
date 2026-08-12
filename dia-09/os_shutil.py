import os, shutil

# print(os.getcwd())  #* Get the current working directory

# archivo = open("curso.txt", "w") # *Create a new file in write mode
# archivo.write("Este es un texto de prueba")
# print(os.listdir())

# archivo.close()

# nuevo_archivo = open("nuevo_archivo.txt", "w")
# nuevo_archivo.write("Este es un nuevo archivo de prueba")
# nuevo_archivo.close()

#shutil.move("curso.txt", "dia-09/curso.txt")  # *Move the file to a new location
# shutil.move("nuevo_archivo.txt", "dia-09/nuevo_archivo.txt") # *Move the file to a new location

#?Some forms to eliminate files and directories
#os.rmdir("dia-09*")  # *Remove the directory
#os.unlink("dia-09/curso.txt*")  #* Remove the file
# shutil.rmtree("C:\\Users\\Usuario\\Desktop\\Python\\dia-09\\nuevo_archivo.txt") #! Remove the directory and its contents


'''
Es mejor utilizar la librería
    send2trash
para eliminar archivos y directorios, ya que los envía a la papelera de reciclaje
'''

# print(os.walk("C:\\Workspace\\Estudio Programación\\practica_python\\dia-09"))  # Walk through the directory tree
ruta = "\\Workspace\\Estudio Programación\\practica_python\\dia-09\\carpeta_superior"

for carpeta, subcarpetas, archivos in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print("Las subcarpetas son: ")
    for subcarpeta in subcarpetas:
        print(f"\t{subcarpeta}")
    print("Los archivos son: ")
    for archivo in archivos:
        if archivo.startswith("2026"):
            print(f"\t{archivo}")
    print("\n")

