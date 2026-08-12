from datetime import datetime, date, time

modulo_datetime = '''El módulo datetime de Python proporciona clases para manipular fechas y horas de manera sencilla.
Algunas de las clases más importantes del módulo datetime son: datetime, date y time'''

header = "||Clases del módulo datetime||"
mi_hora = time(17, 35, 20)
print(header, "\n", mi_hora)  # Output: 17:35:20
print(type(mi_hora))  # Output: <class 'datetime.time'>

mi_dia = date(2026, 11, 4)
print(mi_dia)  # Output: 2026-11-04
print(mi_dia.ctime()) # Output: 2026-11-04 00:00:00
print(type(mi_dia))  # Output: <class 'datetime.date'>

mi_dia_2 = date.today()
print(mi_dia_2)  # Output: Current date
minutos = datetime.now().minute
print(minutos)  # Output: Current minute

fecha_larga = datetime(2026, 11, 4, 18, 45, 30, 300000) # output: 2026-11-04 18:45:30.003000
fecha_larga = fecha_larga.replace(month=7)
print(fecha_larga)  # Output: 2026-07-04 18:45:30.003000
print("*" * 60)


#Ejercicio
nacimiento = date(1995, 3, 15)
defuncion = date(2095, 3, 14)

vida = defuncion - nacimiento
print(f"Vida: {vida} días")  # Output: Vida: 365

#Ejercicio 2
despertar = datetime(2026, 10, 2, 7, 30, 0)
duerme = datetime(2026, 10, 2, 23, 0, 0)
diferencia = duerme - despertar
print(f"Diferencia: {diferencia}")  # Output: Diferencia: 16:00:00
print(diferencia.seconds)

