#Analizador de texto
'''
TEXTO DE PRUEBA 
Un río es una corriente de agua que fluye con continuidad
por un cauce, ya sea en la superficie terrestre o de forma
subterránea, pudiendo ser tanto naturales como artificiales.  
'''
#1
texto = input("ingresa un texto de tu elección: \n")
print("Ingresa 3 letras a elección: ")

letra1 = input('Primera letra: ').lower()
letra2 = input('Segunda letra: ').lower()
letra3 = input('Tercera letra: ').lower()
print('\n')

lista = [letra1, letra2, letra3]
#2
print("Cantidad de letras en texto.")
print(f"Cantidad de letras {letra1}, es de: {texto.count(letra1)}")
print(f"Cantidad de letras{letra2}, es de: {texto.count(letra2)}")
print(f"Cantidad de letras{letra3}, es de: {texto.count(letra3)}\n")

largo_texto = texto.split()
print(f"La cantidad de palabras que hay en el texto es de {len(largo_texto)}")
#3
print(f"Esta es la primera letra del texto: {texto[0]} y la última es: {texto[-1]}\n")

#4
texto_invertido = texto[::-1]
union_texto = " ".join(largo_texto)
print(f"Así se ve el texto invertido:\n{texto_invertido}\nY así se ve con separador: \n{union_texto}")
#5
busqueda = texto.find("Python")
print(busqueda)
print(f"It´s that {"Python" in texto} is found int text ")
print("río" in texto)