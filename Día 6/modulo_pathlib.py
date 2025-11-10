from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/gambi/OneDrive/Escritorio/practica_python/archivo.txt')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


print(carpeta.read_text())
print(carpeta.name)
print(carpeta.stem)
print(carpeta.suffix)

if not carpeta.exists():
    print("Este archivo si existe")
else:
    print("no existe este archivo")