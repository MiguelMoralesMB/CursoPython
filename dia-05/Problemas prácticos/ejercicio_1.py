#Crear función que tenga como parámetros 3 números intergers

def devolver_distintos(int1, int2, int3):
    entero_1 = int(int1)
    entero_2 = int(int2)
    entero_3 = int(int3)
    
    lista_numeros = [entero_1, entero_2, entero_3]
    
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    lista_numeros.sort()
    intermedio = lista_numeros[1]
    
    suma = entero_1 + entero_2 + entero_3
    
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    elif suma >= 10 and suma <= 15:
        return intermedio
    
    
print(devolver_distintos(10,1,2))