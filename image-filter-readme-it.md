# Image Size Filter Script

Questo script Python è stato sviluppato per automatizzare il processo di selezione delle immagini durante la preparazione di dataset per l'addestramento di modelli LoRA. Filtra automaticamente le immagini in base alle loro dimensioni, copiando solo quelle che soddisfano i requisiti minimi in una cartella separata.

## Problema risolto

Durante la raccolta di immagini per l'addestramento di modelli LoRA, spesso si scaricano intere gallerie di immagini che contengono file di dimensioni diverse. Il processo manuale di verifica e selezione delle immagini che soddisfano i requisiti minimi (512x512 pixel) può essere dispendioso in termini di tempo. Questo script automatizza completamente questo processo.

## Funzionalità

- Analizza tutte le immagini nella cartella specificata
- Verifica che entrambe le dimensioni (larghezza e altezza) siano >= 512 pixel
- Crea automaticamente una sottocartella "ok" per le immagini valide
- Copia (non sposta) le immagini che soddisfano i requisiti nella cartella "ok"
- Mantiene intatta la cartella originale
- Fornisce feedback in tempo reale sulle operazioni eseguite

## Requisiti

- Python 3.x
- Pillow (PIL) library
- Sistema operativo: Windows/Linux/MacOS

## Installazione

1. Assicurarsi di avere Python installato
2. Installare la libreria Pillow se non presente:
```bash
pip install Pillow
```

## Utilizzo

1. Posizionare lo script nella cartella contenente le immagini da filtrare
2. Modificare il percorso nella variabile `source_dir` con il percorso della propria cartella:
```python
source_dir = r"C:\image-filter"  # Modificare questo percorso
```
3. Eseguire lo script:
```bash
python image_filter.py
```

Lo script creerà automaticamente una sottocartella "ok" e copierà al suo interno tutte le immagini che soddisfano i requisiti di dimensione.

## Output

Durante l'esecuzione, lo script mostrerà:
- Nome e dimensioni di ogni immagine copiata
- Eventuali errori riscontrati durante il processo
- Messaggio di completamento dell'operazione

## Note

- Lo script non modifica o elimina i file originali
- Le immagini vengono copiate, non spostate, permettendo di mantenere l'archivio originale intatto
- In caso di file con lo stesso nome nella cartella di destinazione, verranno sovrascritti

## Suggerimenti

- Prima di procedere con il captioning del dataset, è consigliabile verificare il contenuto della cartella "ok"
- Per modificare la dimensione minima richiesta, modificare il valore `512` nel controllo delle dimensioni
