archivo = open("prueba.txt", "a") 
# 'r' de read, solo muestra el contenido
# 'w' de write, sobreescribe los datos eliminando los anteriores
# 'a' de ?, escribe al final del archivo sin eliminar el contenido previo.

# archivo.write("Hola, soy Miguel Morales") 

# archivo.write('''
# Hola, esta es una 
# forma de incorporar
# el salto de linea sin 
# colocar "n" ''')

# archivo.writelines(['Hola','Mundo', 'Esta', 'Es',
                    # 'una', 'practica'])

# lista = ['Hola','Mundo', 'Soy', 'Chileno']


# for p in lista:
    # archivo.write(p + "\n") # también sirve con writelines()
    
archivo.write("\nBienvenido")  
    


archivo.close()



