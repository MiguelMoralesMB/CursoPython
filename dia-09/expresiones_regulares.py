import re

# ==============================================================================
# 1. INTRODUCCIÓN A LAS EXPRESIONES REGULARES (REGULAR EXPRESSIONS)
# ==============================================================================
# Son una secuencia de caracteres que forman un patrón de búsqueda.
# Se utilizan para buscar y manipular texto (encontrar palabras, validar
# correos, números de teléfono, etc.). En Python se usa el módulo 're'.

# ------------------------------------------------------------------------------
# Caracteres Especiales
# ------------------------------------------------------------------------------
# .   Significa "cualquier carácter excepto nueva línea"
# \d  Significa "cualquier dígito"
# \D  Significa "cualquier carácter que no sea dígito"
# \s  Significa "cualquier carácter de espacio en blanco"
# \S  Significa "cualquier carácter que no sea espacio en blanco"
# \w  Significa "cualquier carácter alfanumérico"
# \W  Significa "cualquier carácter que no sea alfanumérico"

# ------------------------------------------------------------------------------
# Cuantificadores
# ------------------------------------------------------------------------------
# *      Significa "cero o más"
# +      Significa "una o más"
# ?      Significa "cero o una"
# {n}    Significa "exactamente n"
# {n,}   Significa "n o más"
# {,m}   Significa "hasta m"


# ==============================================================================
# 2. BÚSQUEDAS BÁSICAS (search, findall, finditer)
# ==============================================================================

# Nota (Enfoque antiguo sin 're'):
# palabra = "Juan" in texto
# print(palabra)  # Output: True

texto = "Hola, mi nombre es Juan y mi correo electrónico es user@hmundo.com"
patron = "user@hmundo.cl"
patron2 = "mi"  # Palabra 'mi' del texto

# Búsqueda individual con re.search
busqueda = re.search(patron, texto)
busqueda2 = re.search(patron2, texto)

print(busqueda)           # Output: None (no se encontró el patrón)
print(busqueda2)          # Output: <re.Match object; span=(38, 54)...
print(busqueda2.group())  # Output: user@hmundo.com
print(busqueda2.start())  # Índice de inicio
print(busqueda2.end())    # Índice de fin

# Búsqueda de todas las coincidencias
busqueda_de_coincidencias = re.findall(patron2, texto)
print(busqueda_de_coincidencias)  # Output: ['mi', 'mi']

# Iterar sobre las coincidencias encontradas
for hallazgo in re.finditer(patron2, texto):
    print(hallazgo.span())


# ==============================================================================
# 3. COMPILACIÓN DE PATRONES Y NÚMEROS DE TELÉFONO
# ==============================================================================
text = "Llama al 555-1234 para más información."

# Busca un patrón de número de teléfono (Sintetizado)
pattern = re.compile(r"\d{3}-\d{4}") 
# Forma alternativa directa:
# pattern = r"\d\d\d-\d\d\d\d"

result = re.search(pattern, text)
print(result)          # Output: <re.Match object; span=(9, 17), match='555-1234'>
print(result.group())  # Output: 555-1234


# ==============================================================================
# 4. VALIDACIÓN DE ENTRADAS DE USUARIO (ej. Contraseñas)
# ==============================================================================
# key = input("Ingrese su contraseña: ")

# La contraseña debe comenzar con una letra y tener al menos 8 caracteres alfanuméricos:
# patron_contrasena = r"\D{1}\w{7}" 

# resultado2 = re.search(patron_contrasena, key)
# resultado = re.fullmatch(patron_contrasena, key)
# print(resultado)   # Output: <re.Match object; span=(0, 9), match='A12345678'>
# print(resultado2)  # Output: <re.Match object; span=(0, 9...


# ==============================================================================
# 5. OTROS EJEMPLOS Y OPERADORES AVANZADOS (| , ^ , $ , [^ ])
# ==============================================================================
another_text = "No entendemos los lunes"

# Alternancia (|) -> Busca "lunes" o "martes"
search = re.search("lunes|martes", another_text)
print(search)  # Output: <re.Match object; span=(18, 24), match='lunes'>

# Comodín punto (.)
search2 = re.search(r"...demos...", another_text)  # 3 caracteres + "demos" + 3 caracteres
search3 = re.search(r"...demos", another_text)     # 3 caracteres + "demos"

# Anclas de inicio (^) y fin ($)
search4 = re.search(r"^\D", another_text)   # No dígito al principio del texto
search5 = re.search(r"^\D$", another_text)  # No dígito que ocupe TODA la cadena de inicio a fin

# Negación dentro de conjunto ([^ ])
search6 = re.search(r"[^\s]", another_text) # Primer carácter que NO sea espacio en blanco