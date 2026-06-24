x = 10
y = 20
'''
print("Mis numeros son: " + str(x) + " y " + str(y) ) #Forma con Casting, cambiando tipos de datos 

print("Mis numeros son: {} y {} ".format(x,y))#Formateo de Strings
print("La suma de los numeros: {} y {} es: {} ".format(x,y,x+y))#Otra operación con .format
'''
#Esta es la forma más fácil y legible para formatear cadenas 
color = 'verde'
matricula = 164281
print(f"El auto es {color} y su matricula es {matricula}")
