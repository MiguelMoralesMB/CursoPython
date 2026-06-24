'''
Primero importamos las funciones decoradas desde el módulo numeros, para luego utilizarlas en el programa principal.
'''
from numeros import turno_farmacia, turno_cosmetica, turno_perfumeria, mi_turno_farmacia, mi_turno_cosmetica, mi_turno_perfumeria

    
def inicio_turnero():
    print("*" * 50 )
    print("*" * 12 + " Bienvenido al Turnero " + "*" *13)
    print("*" * 50 + "\n" )

    inicializador_turnero = False

    while not inicializador_turnero:
        '''
        Función para mostrar el turno actual de cada área de atención
        '''
        print("Elige el número del Area de Atención que deseas consultar: ")
        print('''
              [1] - Perfumería
              [2] - Farmacia
              [3] - Cosmética
              [4] - Salir ''')

        eleccion_usuario = int(input("Ingrese su elección: "))

        if eleccion_usuario < 1 or eleccion_usuario > 4:
            print("Opción inválida. Por favor, elige un número entre 1 y 4.")

        if eleccion_usuario == 1:
            turno_perfumeria(mi_turno_perfumeria)
        elif eleccion_usuario ==2:
            turno_farmacia(mi_turno_farmacia)
        elif eleccion_usuario == 3:
            turno_cosmetica(mi_turno_cosmetica)
        elif eleccion_usuario == 4:
            inicializador_turnero = True

inicio_turnero()
            
