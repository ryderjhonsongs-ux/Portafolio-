import os
import shutil

def organizar_carpeta(ruta_directorio):
    if not os.path.exists(ruta_directorio):
        print(f"La ruta '{ruta_directorio}' no existe.")
        return

    # Extensiones y sus respectivas carpetas
    extensiones = {
        'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Código': ['.py', '.c', '.cpp', '.js', '.html', '.css', '.sh'],
        'Comprimidos': ['.zip', '.rar', '.tar', '.gz'],
        'Videos': ['.mp4', '.mkv', '.avi']
    }

    archivos = os.listdir(ruta_directorio)
    movidos = 0

    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_directorio, archivo)
        
        if os.path.isdir(ruta_archivo):
            continue

        _, ext = os.path.splitext(archivo)
        ext = ext.lower()

        movido = False
        for categoria, exts in extensiones.items():
            if ext in exts:
                carpeta_destino = os.path.join(ruta_directorio, categoria)
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                print(f"Movido: {archivo} -> {categoria}/")
                movidos += 1
                movido = True
                break
        
        if not movido:
            # Si no entra en ninguna categoría conocida, va a 'Otros'
            carpeta_otros = os.path.join(ruta_directorio, 'Otros')
            os.makedirs(carpeta_otros, exist_ok=True)
            shutil.move(ruta_archivo, os.path.join(carpeta_otros, archivo))
            print(f"Movido a Otros: {archivo}")
            movidos += 1

    print(f"\n¡Listo! Se organizaron {movidos} archivos con éxito.")

if __name__ == "__main__":
    # Cambia esto por la ruta que quieras ordenar (ej: '/sdcard/Download' en Termux)
    ruta = input("Ingresa la ruta de la carpeta a organizar: ").strip()
    organizar_carpeta(ruta)
    