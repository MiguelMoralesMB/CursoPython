lista_cafes = [("Capuccino", 2.000), ("Mocha", 2.500), ("Expresso", 1.500)]

# for cafe, precio in lista_cafes:
#     print(precio)

def cafe_mas_caro(lista_precios):
    
    precio_mayor = 0
    cafe_mas_caro = ""
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
        
    return (cafe_mas_caro, precio_mayor)

# print(cafe_mas_caro(lista_cafes))

cafe, precio = cafe_mas_caro(lista_cafes)