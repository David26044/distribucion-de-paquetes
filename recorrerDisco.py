import os

def guardar_tamanos_archivos(ruta, archivo_salida):
    with open(archivo_salida, 'w') as f:
        for ruta_actual, directorios, archivos in os.walk(ruta):
            for archivo in archivos:
                ruta_completa = os.path.join(ruta_actual, archivo)
                try:
                    tamaño = os.path.getsize(ruta_completa)
                    f.write(f"{tamaño}\n")
                except Exception as e:
                    print(f"No se pudo obtener el tamaño de {ruta_completa}: {e}")

ruta_disco = "C:\\"  # Ruta del disco C en sistemas Windows
archivo_salida = "tamanos.txt"
guardar_tamanos_archivos(ruta_disco, archivo_salida)
print(f"Se ha guardado el tamaño de los archivos en '{archivo_salida}'.")


