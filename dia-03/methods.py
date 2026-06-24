texto = "Este es el texto de Miguel Morales"
resultado = texto.split("t")
print(resultado)

'''
a = "Miguel"
b = "Ángel"
c = "Morales"
d = 'Basualto'
e = ' - '.join([a,b,c,d])
print(e)
'''
texto_find = "Este es el texto de Miguel Morales"
resultado_find = texto_find.find("Miguel")
print(resultado_find)

texto_replace = "Este es el texto de Miguel Morales"
resultado_replace = texto_replace.replace("e","@")
print(resultado_replace)

lista_palabras = ["La","legibilidad","cuenta."]
lista_palabras = " ".join(["La","legibilidad", "cuenta."])
print(lista_palabras)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
reemplazo = frase.replace("difícil", "fácil").replace("mala","buena")
print(reemplazo)