'''
nombre = "Miguel"
nombre[0] = "m" # Esto es un error debido a que se está modificando el String
print(nombre)
'''
#Los String´s son INMUTABLES, no puede 
# cambiar su contenido y orden
#El contenido de la variable puede variar, 
# pero el String en si no puede variar 
primer_nombre = "Miguel"
segundo_nombre = "Ángel"
apellidos = "Morales Basualto"
print(primer_nombre + segundo_nombre + apellidos)
print(apellidos*3)

cadena = """ Esta es una 
    cadena de texto mas 
    grande de lo 
    normal debido a que estoy ocupando 
    3 cochetes en vez de 1 """
print("porque" not in cadena)
print(len(cadena))
