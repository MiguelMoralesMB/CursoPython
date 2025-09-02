mi_set = set({1,2,3,4,5})# los sets son inmutables
#Listas y diccionario no se pueden juntar con los sets, pero las tuplas si pueden
print(3 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
#print(s1) #python no agrega otro 3 porque los elementos iguales los elimina dejando uno nomas 
#s1.add(4)
#s1.remove(3)
#s1.discard(3)
#sorteo = s1.pop()
s1.clear()
print(s1)

