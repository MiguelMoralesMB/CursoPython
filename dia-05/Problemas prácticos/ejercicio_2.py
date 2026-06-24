#Delv
def devolver_palabra(*palabra):
    palabra = list(set(palabra))
    palabra.sort(key=str.lower) #Parámetros del método para poner los valores de menor a mayor o en orden alfabético
        
    return palabra
    
print(devolver_palabra("Catalina"))