serie = "N-03"

match serie:
    case "N-01":
        print('Samsung')
    case "N-02":   
        print('Nokia')
    case "N-03":
        print('Huawei')
    case _:
        print("No existe ese producto")
        
cliente = {"Nombre": "Miguel",
           "Edad": 21,
           "Ocupación": "Estudiante"}

pelicula = {"Título": "Matrix",
            "Ficha_técnica": {"Protagonista": "Keanu Reeves",
                              "Director": "Lana y Lilly Wachowski"}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'Nombre': nombre,
              "Edad": edad,
              "Ocupación": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"Título": titulo,
              "Ficha_técnica": {"Protagonista": protagonista,
                                "Director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No tengo idea que es esto.")                

        
               