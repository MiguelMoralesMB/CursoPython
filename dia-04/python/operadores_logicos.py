#Operadores lógicos: and, or y not
#and: todas tienen que ser verdaderas o sinó arrojará False
#mi_bool = (4 < 5) and (4 == 2+2)
#print(mi_bool)

mi_bool2 = (20 == 10) and ("Miguel" == "Miguel") and (10 > 9) and (23 < 28)
#print(mi_bool2)

#or: con que una condición sea verdadera contará, tienen que ser todas falsas para que arroje False

otro_bool = (10 == 10 ) or (3 == 51)
#print(otro_bool)

otro_bool2 = (10 == 10) or (3 == 51) or (32 > 80) 
#print(otro_bool2)

#Prueba en texto
#texto = 'Esta es una breve linea de texto para prueba'
#prueba_bool = ('frase' in texto) and ('breve' in texto)
#print(prueba_bool)

#Prueba de not:
#El not niega la condición a la que está apuntando 
otro_bool3 = not (10 == 10)
otra_comparacion = not ("Miguel" != "Felipe")
print(otro_bool3)# Este devuelve False aunque la condición es True
print(otra_comparacion)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool2 = (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool2)