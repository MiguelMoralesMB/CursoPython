#Areas de atención: perfumería, farmacia y cosmética.

#Generador de turnos para cada área de atención

'''
Generadores para cada área de atención
'''
def generador_turno_perfumeria():
    prefijo = "P-"
    turno = 1
    while True:
        yield prefijo + str(turno)  
        turno += 1

mi_turno_perfumeria = generador_turno_perfumeria()
# print(next(mi_turno_perfumeria))  # Imprime: P-1

def generador_turno_farmacia():
    prefijo = "F-"
    turno = 1
    while True:
        yield prefijo + str(turno)  
        turno += 1

mi_turno_farmacia = generador_turno_farmacia()


def generador_turno_cosmetica():
    prefijo = "C-"
    turno = 1
    while True:
        yield prefijo + str(turno)  
        turno += 1
    
mi_turno_cosmetica = generador_turno_cosmetica()
# print(next(mi_turno_cosmetica))  # Imprime: C-1

'''
Función para mostrar el turno actual de cada área de atención
'''
def mostrar_turno(generador):
    print(next(generador))

# mostrar_turno(mi_turno_perfumeria)  # Imprime: P-1


'''
Decorador para agregar un saludo antes de mostrar el turno
'''
def decorador_turno(funcion):

    def agregar_saludo_a_turno(turno):
        print("*" * 50 )
        print("Su turno es:")
        funcion(turno)
        print("Aguarde y será atendido")
        print("*" * 50 + "\n" )

    return agregar_saludo_a_turno

turno_perfumeria = decorador_turno(mostrar_turno)
turno_farmacia = decorador_turno(mostrar_turno)
turno_cosmetica = decorador_turno(mostrar_turno)

# turno_perfumeria(mi_turno_perfumeria)  # Imprime: Su turno es: P-1 Aguarde y será atendido
# turno_farmacia(mi_turno_farmacia) # Imprime: Su turno es: F-1 Aguarde y será atendido
# turno_cosmetica(mi_turno_cosmetica) # Imprime: Su turno es: C-1 Aguarde y será atendido

