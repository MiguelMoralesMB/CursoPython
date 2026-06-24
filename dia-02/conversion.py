#Conversiones Implícitas dentro de python 
'''
num1 = 15
num2 = 20.4
text = "Mi nombre es Miguel Ángel Morales Basuato"

num1 = num1 + num2

print(type(text))
print(type(num1))
print(type(num2))
print(num1)
'''
#Conversiones Explícitas dentro de python 

'''
num3 = 45.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))
'''

'''
num5 = 21
print(num5)
print(type(num5))

num6 = float(num5)
print(num6)
print(type(num6))
'''

edad = input('Dime tu edad: ')
print(type(edad))

edad = int(edad)

print(type(edad))
nueva_edad = 1 + edad 
print(nueva_edad)