import os
import pyminizip
from datetime import datetime

# 1. Definimos las variables de configuración
nombre_zip_respaldo = f"respaldo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
carpeta_origen = "myfiles"
CONTRASENA_ZIP = "qwerty"  # <--- Define aquí la contraseña del ZIP

# 2. Obtenemos todas las rutas de los archivos dentro de 'myfiles'
lista_archivos = []
prefijos_carpetas = []

for raiz, directorios, archivos in os.walk(carpeta_origen):
    for archivo in archivos:
        ruta_completa = os.path.join(raiz, archivo)
        lista_archivos.append(ruta_completa)
        
        # Guardamos la estructura interna para que mantenga el nombre de la carpeta
        # 'pyminizip' necesita saber el prefijo relativo de cada archivo en el ZIP
        ruta_relativa = os.path.relpath(raiz, os.path.dirname(carpeta_origen))
        prefijos_carpetas.append(ruta_relativa)

# 3. Creamos el archivo ZIP protegido con contraseña
# El nivel de compresión va de 1 (más rápido) a 9 (máxima compresión)
nivel_compresion = 5 

pyminizip.compress_multiple(
    lista_archivos,
    prefijos_carpetas,
    nombre_zip_respaldo,
    CONTRASENA_ZIP,
    nivel_compresion
)

print(f"Respaldo encriptado creado con éxito: {nombre_zip_respaldo}")
