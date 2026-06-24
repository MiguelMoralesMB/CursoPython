mi_archivo = open('prueba.txt')
print(mi_archivo.read()) #read() lee todo el contenido

# mi_archivo.readline() readline() lee la primera linea del archivo
# mi_archivo.readlines() readlines() imprime cada linea en una lista
#No utilizar readlines() con grandes archivos

'''
primera_linea = mi_archivo.readline()
print(primera_linea.upper())

primera_linea = mi_archivo.readline()
print(primera_linea.lower())

primera_linea = mi_archivo.readline()
print(primera_linea.capitalize())

primera_linea = mi_archivo.readline()
print(primera_linea.replace(":)", ":("))
'''
todas_las_lineas = mi_archivo.readlines()
print(todas_las_lineas)


primera_linea = mi_archivo.readline()

for linea in mi_archivo:
    print("Aquií dice: " + linea)





mi_archivo.close()