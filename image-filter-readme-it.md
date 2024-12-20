# Script di Filtro Dimensioni Immagini

Questo script Python automatizza il processo di selezione delle immagini filtrando in base alle loro dimensioni. Copia automaticamente le immagini che soddisfano i requisiti minimi di dimensione in una cartella separata, rendendolo particolarmente utile per la preparazione di dataset per l'addestramento di modelli LoRA.

## Problema Risolto

Durante la raccolta di immagini per l'addestramento di modelli LoRA, spesso si scaricano intere gallerie contenenti file di dimensioni diverse. Questo script filtra automaticamente le immagini che soddisfano i requisiti minimi (512x512 pixel), eliminando la necessità di verifica manuale.

## Funzionalità

- Analizza automaticamente tutte le immagini nella directory di lavoro corrente
- Verifica che entrambe le dimensioni (larghezza e altezza) siano >= 512 pixel
- Crea automaticamente una sottocartella "ok" per le immagini valide
- Copia (non sposta) le immagini che soddisfano i requisiti nella cartella "ok"
- Mantiene intatta la cartella originale
- Fornisce feedback in tempo reale sulle operazioni
- Elabora i file in parallelo per migliori prestazioni

## Requisiti

- Python 3.x
- Libreria Pillow (PIL)
- Sistema operativo: Windows/Linux/MacOS

## Installazione

1. Assicurarsi di avere Python installato
2. Installare la libreria Pillow se non presente:
```bash
pip install Pillow
```

## Utilizzo

1. Posizionare lo script nella cartella contenente le immagini da filtrare
2. Eseguire lo script:
```bash
python image-filter.py
```

Lo script automaticamente:
- Creerà una sottocartella "ok" nella directory corrente
- Copierà tutte le immagini che soddisfano i requisiti di dimensione
- Elaborerà i file in parallelo per un'esecuzione più veloce

## Output

Durante l'esecuzione, lo script mostrerà:
- Nome e dimensioni di ogni immagine copiata
- Eventuali errori riscontrati durante il processo
- Messaggio di completamento dell'operazione

## Note

- Lo script non modifica o elimina i file originali
- Le immagini vengono copiate, non spostate, permettendo di mantenere l'archivio originale intatto
- I file con lo stesso nome nella cartella di destinazione verranno sovrascritti
- Lo script utilizza l'elaborazione parallela per migliorare le prestazioni

## Suggerimenti

- Prima di procedere con il captioning del dataset, è consigliabile verificare il contenuto della cartella "ok"
- Lo script utilizza automaticamente la directory di lavoro corrente, quindi non è necessaria alcuna configurazione del percorso
- La dimensione minima richiesta (512x512) è impostata nel codice - modificare il valore nello script se sono necessarie dimensioni diverse
