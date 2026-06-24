#Mi solución es esta, pero está equivocada porque devulve solos los numeros impares
#Y no los PRIMOS.
def contar_primos(numero):
    cantidad_primos = 0

    for i in range(0,numero):
        if (i % 2 != 0):
            cantidad_primos +=1
            print(f'El número {i} es primo')
        else:
            continue
    
    
    return f"Esta es la cantidad de números primos {cantidad_primos}"
        
contar_primos(10)

def contar_primos2(numero):
    
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return False
    
    while iteracion <= numero:
        
        for n in range(3,iteracion,2):
            
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
            
    print(primos)            
    return len(primos)
        

contar_primos2(20)