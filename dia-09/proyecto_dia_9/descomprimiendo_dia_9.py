from pathlib import Path
import shutil

# Obtiene la ruta absoluta de la carpeta donde está este script
base_dir = Path(__file__).parent

archivo_zip = base_dir / "Proyecto_Dia_9.zip"
print(archivo_zip)
destino = base_dir / "Proyecto_Dia_9"
print(destino)

# Pasa el formato dentro de la función
# shutil.unpack_archive(archivo_zip, destino, "zip")

# archivo_zip.unlink()  # Elimina el archivo zip después de descomprimirlo