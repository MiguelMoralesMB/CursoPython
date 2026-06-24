from random import *

def lanzar_moneda():
    resultado = ["Cara", "Cruz"]
    moneda = choice(resultado)
    
    return moneda


lista_numeros = [2, 5, 10, 20, 7, 9]

def probar_suerte(resultado_tiro, lista):
    if resultado_tiro == "Cara":
        lista.clear()
        return f"La lista se autodestruirá. Aquí está tu lista: {lista}"
    elif resultado_tiro == "Cruz":
        return f"La lista fue salvada. Esta es la lista: {lista}"
        
lanzamiento = lanzar_moneda()
intento = probar_suerte(lanzamiento, lista_numeros)
print(intento)
    