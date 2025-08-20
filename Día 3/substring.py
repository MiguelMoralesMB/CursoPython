#Slicing, concepto de 
texto = "ABCDEFGHIJKLMN"
fragmento = texto[::-2]
print(fragmento)

'''
Toma cada tercer caracter empezando desde el 
noveno hasta el final de la frase, e imprime el resultado.
"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
'''

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[10:10:3]
print(fragmento)

frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento2 = frase2[::-1]# Dándole un valor negativo, se invierte la cadena de caracteres 
print(fragmento2)

