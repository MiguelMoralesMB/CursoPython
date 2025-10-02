lista = ['a', 'b', 'c', 'c']
indice = 0

#Sin método de enumerador:
for item in lista:
    print(indice, lista)
    indice +=1
print('\n')

#con método de numerador
for indice, item in enumerate(range(50,55)):
    print(indice, item)
print('\n')    
#También fuera de un loop 

mis_tuples = list(enumerate(lista)) 
print(mis_tuples[0][1])

#Ejercicio 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print('\n')

#Ejercicio 2

lista_indices = list(enumerate("Python"))
print(lista_indices)

#Ejercicio 3

lista_nombres2 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres2):
    if nombre[0] == "M":
        print(indice)
    else:
        continue

  
    
