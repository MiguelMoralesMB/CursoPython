menor = min(18,23,49,88,22)
maximo = max(18,23,49,88,22)
print(menor, maximo, '\n')

lista = [58,21,54,12,99]
print(f"El menor es: {min(lista)} y el máximo es: {max(lista)}\n")

nombres = ['Miguel', 'Andrés', 'Carlos', 'Antonia']
nombre = "Miguel"
nombre_2 = "miguEl"

print(min(nombres))
print(max(nombre))
print(min(nombre_2.lower()))
print('\n')

#El método de min() en el caso de los diccionarios favorece los strings antes que los ints
dic = {"C1": 45, "C2":11}
print(min(dic.values()))#values() método de diccionarios
print(min(dic))
#Ejercicio 1

