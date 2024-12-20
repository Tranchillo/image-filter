import os
from PIL import Image
import shutil
import concurrent.futures

# Percorsi delle directory
source_dir = os.getcwd()
ok_dir = os.path.join(source_dir, "ok")

# Crea la directory ok se non esiste
if not os.path.exists(ok_dir):
    os.makedirs(ok_dir)

# Funzione per controllare le dimensioni delle immagini e copiare
def fileCopy(f):
    file_path = os.path.join(source_dir, f)
    if os.path.isfile(f):
        try:
            with Image.open(f) as img:
                width, height = img.size
                if width <= 512 and height <= 512:
                    dest_path = os.path.join(ok_dir, f)
                    shutil.copy(file_path, dest_path)
                    print(f"Copiata: {f} ({width}x{height})")
        except Exception as e:
            print(f"Errore con il file {f}: {e}")

with concurrent.futures.ThreadPoolExecutor() as ex:
    results=ex.map(fileCopy,os.listdir(source_dir))
print("Operazione completata.")