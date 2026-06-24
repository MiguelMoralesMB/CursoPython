class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color  
        self.especie = especie
        pass
    
    def piar(self):
        print("pio, mi color es {}".format(self.color))
        
    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros")
        

piolin = Pajaro("amarillo", "gorrión")

piolin.piar()
piolin.volar(50)

'''Los métodos de las clases son funciones que están vinculadas a nuestra clase en cuestión (Pajaro) '''