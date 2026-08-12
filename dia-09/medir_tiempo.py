import timeit, time
# modulo time sirve para medir el tiempo de ejecución de un programa o una función en Python.

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

print(prueba_for(10))
print(prueba_while(10)) 

inicio = time.time()  # * Get the current time in seconds since the epoch
prueba_for(1000000) # * Call the function to measure its execution time 
final = time.time()  # * Get the current time in seconds since the epoch
print(final - inicio)  # * Calculate the time taken for the function to execute

inicio = time.time()  
prueba_while(1000000) 
final = time.time()  
print(final - inicio, "\n" + "-" * 60)  

declaracion_for = '''prueba_for(10)'''

mi_setup_for = ''' 
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''
duracion_for = timeit.timeit(declaracion_for, mi_setup_for , number=100000)
print(duracion_for)

declaracion_while = '''prueba_while(10)'''

mi_setup_while = ''' 
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

'''

duracion_while = timeit.timeit(declaracion_while, mi_setup_while , number=100000)
print(duracion_while)
