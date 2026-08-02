# Automatización de Respaldos en ZIP con Marca de Tiempo

## 📝 Descripción
Este script de automatización está diseñado para empaquetar de forma segura el contenido de un directorio local en un archivo comprimido `.zip`. Cada copia de seguridad generada incluye automáticamente la fecha y hora exacta de su creación en el nombre del archivo, evitando la sobreescritura y garantizando un historial de versiones ordenado.

## 🎯 Objetivo
El objetivo principal es simplificar y asegurar la continuidad digital de tus proyectos mediante copias de seguridad rápidas. Para su correcto funcionamiento, el script requiere la siguiente estructura interna:
* **Directorio origen:** Dentro de la carpeta de la aplicación, debe existir una carpeta llamada `myfiles` que contenga los archivos que deseas respaldar.
* **Procesamiento automatizado:** El script detecta la carpeta `myfiles`, comprime su contenido en formato `.zip` y le asigna una marca de tiempo única (ej. `respaldo_2026-08-02_13-22.zip`).

## 🚀 Aplicación y Casos de Uso
Esta herramienta actúa como una solución de respaldo local para prevenir la pérdida de información crítica. Su mayor potencial se alcanza al integrarse con los programadores de tareas del sistema operativo, permitiendo que el proceso se ejecute en segundo plano sin intervención humana.

**Casos de uso principales:**
* **Tareas programadas:** Configuración en el Programador de Tareas de Windows o mediante `cron` en Linux/Mac para ejecuciones diarias o semanales.
* **Respaldos de bases de datos locales:** Almacenamiento rápido de respaldos generados por otros sistemas (como archivos `.sql` o `.db`).
* **Control de versiones manual:** Resguardo rápido del estado de un proyecto antes de realizar cambios estructurales importantes.

**Impacto:** Elimina por completo el tiempo invertido en copiar, pegar y renombrar archivos manualmente. Minimiza el riesgo de olvidos o errores humanos, asegurando que siempre exista un punto de restauración actualizado de tus archivos más importantes.