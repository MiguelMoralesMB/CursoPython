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
print("------------------------------------------------------")

dic3 = {1:"A", 2:"B",3:"C",}
print(dic3)

dic3[4] = "D"
print(dic3)

dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())
print("--------------------------------------------------")

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])
print("---------------------------------------------------------")

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)

