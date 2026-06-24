from pathlib import Path

base = Path.home()
guia = Path(base, "Barcelona", "Sagrada_Familia.txt")
print(guia, "\n")
guia = Path(base,"Europa" , "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(guia, "\n")
# guia2 = guia.with_name("La_Pedrera.txt")
# print(guia2, "\n")


guia = Path(Path.home(), "Europa")
print(guia)

for txt in Path(guia).glob("**/*.txt"):
    print(txt)



# print(guia.parent.parent.parent)
# print(guia2)

# ruta = "C:\Workspace\Estudio Programación\Práctica python\Día 6\path.py"
# ruta_relativa = "Día 6\path.py"

'''
Ejercicio 1
Almacena en la variable ruta_base, un objeto Path 
que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y
utilizar el método home()
'''

from pathlib import Path 

ruta_base = Path.home()
#✅✅✅

'''
Ejercicio 2
Implementa y crea una ruta relativa que nos permita llegar
al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

Curso Python>Día 6>practicas_path.py

Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
'''

from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)
#✅✅✅

'''
Ejercicio 3
Implementa y crea una ruta absoluta que nos permita llegar al 
archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

home(directorio Base)"Curso Python">"Día 6">"practicas_path.py"

Almacena el directorio obtenido en la variable ruta. No olvides importar Path,
y de concatenar el objeto Path que refiere a la carpeta base del usuario.
'''
from pathlib import Path

base = Path.home()
ruta = Path(base, "Curso Python", "Día 6", "practicas_path.py")
print(ruta)
#✅✅✅



