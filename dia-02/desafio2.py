nombre = input("¿Cual es tu nombre? ")
ventas = int(input("¿Cuantas ventas haz tenido?"))
calculo_ventas = round(ventas * 13 /100,2)
print(f"Muy bien {nombre}, este mes ganaste de comisión ${calculo_ventas}")

