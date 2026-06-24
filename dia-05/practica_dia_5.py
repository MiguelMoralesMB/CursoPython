from random import choice

#lista con palabras para el ahorcado
mi_lista = ["Serrucho", "Pala", "Silla",
        "Escritorio", "Cepillo", "Pepino", 
        "Calcetín", "Auto", "Avión", "Botella",
        "Robot"]

contador_vidas = 6

#Función para elegir palabra secreta
def escoger_palabra(lista_palabras):
    return choice(lista_palabras)


#Función para transformar palabra a guiones según letra que contenga.
def transformar_palabra():
    
    palabra_secreta = escoger_palabra(mi_lista)
    palabra_transformada = []
    
    for letra in palabra_secreta:
        
        letra = "_"
        palabra_transformada.append(letra)
    
    
    return palabra_transformada



#Pedir al usuario una letra para jugar 
def pedir_letra():
    while True:
        letra = input("Ingresa una letra: ").lower()  # convierte a minúscula
        
        # Validar que sea una sola letra
        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue
        
        # Validar que sea una letra del alfabeto
        if not letra.isalpha():
            print("Por favor, ingresa una letra válida (sin números ni símbolos).")
            continue
        
        # Si pasa las validaciones, devolvemos la letra
        return letra
    
pedir_letra()

#Verificar si esa letra ingresada por el usuario se encuentra
def validar_letra(letra):
    pass
    
    

def chequear_letra():
    pass

def verificar_intento():
    pass

    
