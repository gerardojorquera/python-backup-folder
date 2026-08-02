import shutil
from datetime import datetime
import os

# 1. Generamos el nombre con la fecha y hora actual
nombre_zip_respaldo = f"respaldo_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# 2. Modificamos los parámetros para incluir la carpeta contenedora
shutil.make_archive(
    base_name=nombre_zip_respaldo,  # Nombre del archivo ZIP resultante
    format='zip',                   # Formato de compresión
    root_dir='.',                   # Directorio raíz desde donde se busca (el directorio actual)
    base_dir='myfiles'              # Carpeta específica que se incluirá junto con su nombre
)

print(f"Respaldo creado: {nombre_zip_respaldo}.zip")
