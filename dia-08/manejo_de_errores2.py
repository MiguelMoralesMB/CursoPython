def pedir_numero():
    
    while True:
        try:
            numero = int(input("dame un número: "))
        except:
            print("Eso no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    
    print("Gracias")
    
pedir_numero()