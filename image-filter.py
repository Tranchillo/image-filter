
import os
from PIL import Image
import shutil
import concurrent.futures

# Rileva automaticamente la directory di origine
source_dir = os.getcwd()
ok_dir = os.path.join(source_dir, "ok")

# Crea la directory 'ok' se non esiste
if not os.path.exists(ok_dir):
    os.makedirs(ok_dir)

# Funzione per copiare i file che soddisfano i requisiti di dimensione
def fileCopy(file_name):
    file_path = os.path.join(source_dir, file_name)
    if os.path.isfile(file_path):
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                # Filtra immagini con larghezza e altezza >= 512 px
                if width >= 512 and height >= 512:
                    dest_path = os.path.join(ok_dir, file_name)
                    shutil.copy(file_path, dest_path)
                    print(f"Copied: {file_name} ({width}x{height})")
        except Exception as e:
            print(f"Error with file {file_name}: {e}")

# Esegui la copia in parallelo usando ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fileCopy, os.listdir(source_dir))

print("Operation completed.")
