nombres = ['Miguel', 'Catalina', 'Andrés']
edades = [21, 20, 25]
ciudades = ['Lima', 'Madrid', "Santiago"]

combinados = zip(nombres, edades)
print(combinados) #No se puede así nomas, ántes hay que hacer un "Casting", osea meterlos dentre de una lista

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en : {ciudad}")

#Ejercicio 2
marcas = ["Nike", "Apple"]
productos = [["Nike air for one","Polera", "short"],["Iphone 16", "AirPods", "SmartWatch"]]
mi_zip = list(zip(marcas, productos))
print(mi_zip)

#Ejercicio 3
print('\n')

español = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

lista = list(zip(español, portugues, ingles))
print(lista)