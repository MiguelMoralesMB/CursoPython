'''
La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar
toda la complejidad que algo puede tener por dentro, ofreciendo una interfaz con funciones de alto nivel, por lo general
sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.
'''

class MaquinaDeCafe:
    # Estos métodos son complejos y privados (el "cómo lo hace")
    def __calentar_agua(self):
        print("Calentando agua a 90°C...")
        
    def __moler_granos(self):
        print("Moliendo granos de café colombiano...")
        
    # Este es el único método público (la abstracción / "qué hace")
    def hacer_cafe(self):
        print("Iniciando preparación...")
        self.__calentar_agua()
        self.__moler_granos()
        print("☕ ¡Tu café está listo!")

cafetera = MaquinaDeCafe()
# El usuario de la clase tiene una vida fácil gracias a la abstracción:
cafetera.hacer_cafe()
