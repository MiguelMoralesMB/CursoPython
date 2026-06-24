# mi_lista = [1,1,1,1,1,1,1]
# print(len(mi_lista))

# class Objeto:
#     pass

# mi_objeto = Objeto()
# print(mi_objeto)

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado el CD")

        
class Disco(CD):
    
    def __init__(self, autor, titulo, canciones):
        super().__init__(autor, titulo, canciones)
        
    def __str__(self):
        return super().__str__
    
        
mi_cd = CD("pink floid", "The wall", 24)
print(mi_cd)
print(len(mi_cd))

mi_disco = Disco("Bruno Mars", "Uptown Funk up", 12)
print(mi_disco)


del mi_cd #del es para eliminar alguna instancia
# print(mi_cd)
print(CD.__class__)
print(CD.__base__)
print(CD.__dir__)
print(CD.__class__)