#Diccionarios en python son con {}.
#Estos tienen una clave y un valor asociado a dicha clave 
diccionario = {"Nombre":"Miguel","Edad":21}
print(diccionario)

busqueda = diccionario["Edad"]
print(busqueda)
print("--------------------------------------------------")

cliente = {"Nombre":"Manuel", "Edad":35, "Número":"+569 32415463", "Estado Civil":"Soltero"}
consulta = cliente["Número"]
print(consulta)
print("----------------------------------------------------")

dic = {"c1":100, "c2":[2,4,6,8], "c3":{"s1":5, "s2":10, "s3":15}}
print(dic["c3"]["s2"])
print("-----------------------------------------------------")

dic2 = {"c1":['a','b','c'], "c2":['d','e','f']}
print(dic2["c2"][1].upper())
print("---------------------------------------------------------------")



