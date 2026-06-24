
def mi_funcion():
    lista = []
    
    for n in range(1, 5):
        lista.append(n *10)

    return lista


def mi_generador():
    for n in range(1, 5):
        yield n * 10


print(mi_funcion())
print(mi_generador())

num_de_generador = mi_generador()
print(next(num_de_generador))
print(next(num_de_generador))
print(next(num_de_generador))



def mi_generador_1():
    num_inicio = 0
    while True:
        num_inicio += 1
        yield num_inicio
    

generador_1 = mi_generador_1()

def generador_multiplos_de_7():
    num_base = 7

    while True:
        if num_base % 7 == 0:
            yield num_base
        num_base += 1

generador_2 = generador_multiplos_de_7()
# print(next(generador_2))
# print(next(generador_2))
# print(next(generador_2))
# print(next(generador_2))
# print(next(generador_2))

def resta_vidas():
    vidas = 3

    while vidas >= 0:
        if vidas == 3:
            yield "Te quedan 3 vidas"
        elif vidas == 2:
            yield "Te quedan 2 vidas"
        elif vidas == 1:
            yield "Te queda 1 vida"
        elif vidas == 0:
            yield "Game Over"
        vidas -= 1

perder_vida = resta_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
