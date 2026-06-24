def decorador_saludo(funcion):
    
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")

    return otra_funcion



def mayuscula(texto):
    print(texto.upper())
    


def minuscula(texto):
    print(texto.lower())

#Aplicamos el decorador a las funciones mayuscula y minuscula
mayuscula_decorada = decorador_saludo(mayuscula)
minuscula_decorada = decorador_saludo(minuscula)    


mayuscula_decorada("Python")

minuscula_decorada("PYTHON")


# def cambiar_letras(tipo_funcion):
    
#     def mayuscula(texto):
#         print(texto.upper())

#     def minuscula(texto):
#         print(texto.lower())

    
#     if tipo_funcion == "may":
#         return mayuscula
#     elif tipo_funcion == "min":
#         return minuscula


# operacion = cambiar_letras("min")

# operacion("Palabra")







# def mayuscula(texto):
#     print(texto.upper())

#* Podemos asignar funciones a variables
# mi_funcion = mayuscula

# mi_funcion("Hola Mundo")

#* Podemos pasar funciones como argumentos a otras funciones
# def una_funcion(funcion):
#     return funcion

# una_funcion(mayuscula("Probando una función como argumento"))
