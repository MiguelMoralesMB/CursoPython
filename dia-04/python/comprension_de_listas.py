#Este es una forma de agregar la palabra python letra por letra en una lista
#Pero es deficiente y ocupa muchas lineas de código 
palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
 
print(lista, '\n')    
#Esta sería una forma mejor.

lista_mejorada = [ letra for letra in 'python']
print(lista_mejorada)
print(type(lista_mejorada))

#Con valores numéricos 
lista_numerica = [ numero for numero in range(3,31,3)]
print(lista_numerica)
#Aplicando una operación antes
lista_numerica = [ numero / 1.5 for numero in range(3,31,3)]
print(lista_numerica)
#Aplicando una codición 
lista_numerica = [ numero for numero in range(3,31,3) if numero *2 > 20 ]
print(lista_numerica)
#Incluyendo una exepción, si no se cumple esa condición agrega un 'no'
lista_numerica = [ numero if numero *2 > 20 else 'no' for numero in range(3,31,3)]
print(lista_numerica)

#Otro tipo de usos 

pies = [10,20,30,40,50]
metros = [ n / 3.281 for n in pies ]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n **2 for n in valores]
print(valores_cuadrado)

valores_2 = [1,2,3,4,5,6,9.5]
valores_pares = [n for n in valores_2 if n % 2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temp -32)* (5/9) for temp in temperatura_fahrenheit ]
print(grados_celsius)

comunas = ["Quilicura", "Las Condes", "La Pintana", "El Bosque", "Santiago", "San Miguel"]
poblacion = [122, 222, 290, 309, 145, 559]
listado_comunas = [comuna for comuna in comunas]
print(listado_comunas)