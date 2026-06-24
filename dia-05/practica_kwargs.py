#Ejercicio 1
def cantidad_atributos(**kwargs):
    cantidad_params = len(kwargs)
    
    return cantidad_params

#Ejercicio 2

def lista_atributos(**kwargs):
    return list(kwargs.values())
    

print(lista_atributos(nombre= "Miguel", color_ojos= "Cafés", estatura= 1.70), "\n")

#Ejercicio 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    
    for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")
        
        
        
describir_persona("Marcelo", color_ojos= "Verdes", color_pelo= "Café")    
        
    
    