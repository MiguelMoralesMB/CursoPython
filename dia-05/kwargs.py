'''
**kwargs significa "Key word args", "palabra clave". 
Es similar a ocupar *args solo que este está asociado a los diccionários 

'''


def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor 
        
    return total
    
    

print(suma(x=3, z=2, y=1))


def prueba_args(num1, num2, *args, **kwargs):
    
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}")


    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        
    

prueba_args(21, 20, #argumento num1 y num2
            100, 100, 200, 1000, #Estos son los *args
            nombre="Miguel", # Y estos son los **kwargs
            edad = 21,
            situacion_sentimental = "Soltero (No por mucho)",
            trabajo = False)

args = [100, 100, 200, 1000]
kwargs = {"nombre": "Miguel",
          "edad": 21,
          "situacion_sentimental": "Soltero (No por mucho)",
          "trabajo": False}
    
prueba_args(21, 20, *args, **kwargs)