import os
from PIL import Image
import shutil

# Percorsi delle directory
source_dir = r"D:\image-filter"
ok_dir = os.path.join(source_dir, "ok")

# Crea la directory ok se non esiste
if not os.path.exists(ok_dir):
    os.makedirs(ok_dir)

# Funzione per controllare le dimensioni delle immagini e copiare
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)

    # Controlla se il file è un'immagine
    if os.path.isfile(file_path):
        try:
            with Image.open(file_path) as img:
                width, height = img.size

                # Controlla se entrambi i lati sono uguali o superiori a 512px
                if width >= 512 and height >= 512:
                    dest_path = os.path.join(ok_dir, file_name)
                    shutil.copy(file_path, dest_path)
                    print(f"Copiata: {file_name} ({width}x{height})")

        except Exception as e:
            print(f"Errore con il file {file_name}: {e}")

print("Operazione completata.")
