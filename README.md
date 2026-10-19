# ITS MAKER Bologna: costruire e verificare un assistente documentale RAG

Corso pratico di 6–8 ore: partire da una domanda d'officina, cercare nei documenti, controllare le risposte, aggiornare le fonti e collaudare un documento nuovo. **Il RAG è il filo conduttore; Git conserva le evidenze.** Nessuna installazione o programmazione nel percorso studente base. Confronto modelli e OpenCode sono facoltativi.

Il prodotto finale è corpus aggiornato, prove documentate e report; non un sistema di controllo macchina. Si usano solo dati sintetici.

## 1. Materiali

- [Proposta didattica](PROPOSTA_DIDATTICA_ITS_MAKER.md) e [PDF](PROPOSTA_DIDATTICA_ITS_MAKER.pdf): obiettivi, tempi, valutazione e condizioni di erogazione.
- [Quaderno studenti](materiali_aula/DISPENSA_OPERATIVA_STUDENTI.md) e [PDF](materiali_aula/DISPENSA_OPERATIVA_STUDENTI.pdf): percorso operativo B1–B6, prove e consegna.
- [Slide docente](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.md), [presentazione HTML offline](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.html) e [PDF](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.pdf).
- [Guida docente](laboratorio/docente/SOLUZIONI.md): preparazione unica dell'ambiente, risposte, scheda di qualifica e appendici facoltative.

I Markdown sono i sorgenti; HTML/PDF didattici si rigenerano con `scripts/build_materiali.py`. I PDF non sono byte-identici tra compilazioni. `report.html` è invece un prodotto del laboratorio.

### Kit operativo

- `laboratorio/corpus/`: cinque documenti sintetici, leggibili integralmente per verificare le fonti.
- `laboratorio/starter/risultati.csv`: T01–T06 inizialmente NON_ESEGUITO; la coppia aggiunge T07–T09 durante il corso.
- `laboratorio/starter/genera_report.py`: report HTML offline delle valutazioni umane, nessuna chiamata AI e nessuna modifica richiesta.
- `laboratorio/prepara_laboratorio.py`: crea il workspace senza soluzioni.
- `laboratorio/preflight.py`: registra CLI e hash del corpus; le verifiche OpenCode sono facoltative e non bloccano il base. Non certifica inferenza o RAG.
- `laboratorio/avvia_studio.py`: launcher per l'ambiente preparato dal docente.
- `laboratorio/docente/`: rev2 da consegnare in B4 e soluzione filtro del solo approfondimento OpenCode. Repository pubblico: la separazione evita copie accidentali, non rende segrete le soluzioni.

## 2. Programma delle sei ore

| Blocco | Minuti | Risultato |
| --- | ---: | --- |
| B1 · Problema e fondamenti | 40 | T01 senza fonti subito; modello, contesto e plausibilità. |
| B2 · Primo RAG guidato | 65 | Corpus associato, T01 con passaggi e fonti verificati. |
| B3 · Prove e diagnosi | 75 | T02–T06 e T07 autonoma; recupero e risposta separati. |
| B4 · Aggiornare le fonti | 40 | Catalogo rev2 e storico; evidenze prima/dopo conservate. |
| B5 · Git sulle evidenze | 25 | Salvataggi di corpus e risultati, lettura delle differenze. |
| B6 · Autonomia e restituzione | 70 | Nuova DOC-T10, T08/T09, peer review e report finale. |
| Pause e margine | 45 | Totale 360 minuti, 315 netti. |

Valutazione: 40% fonti/diagnosi, 25% revisioni/storico, 20% autonomia/test negativo, 10% tracciabilità/Git, 5% collaborazione. Non si valuta lo studente con la percentuale di risposte corrette del modello.

I chiarimenti su indice/interrogazione, contesto dei passaggi e semantica/codici esatti sono integrati nei blocchi esistenti. Box su contesto esteso e qualità delle fonti completano il quaderno; metadati/filtri, score e rapporto fra RAG e agenti restano note docente. Nessun modulo, strumento o test aggiuntivo.

**Otto ore:** E1 +60 minuti su domande letterali/sinonimi/gergo, senza tuning tecnico; E2 +60 su corpus ampliato e collaudo cieco. Un approfondimento OpenCode oppure confronto modelli può sostituire E2 se scelto e preparato prima; non si somma alle otto ore e non è obbligatorio nelle sei.

## 3. Preparazione: solo docente, prima dell'aula

Una sola configurazione locale con Studio, LLM ed embedding multilingue già disponibili; cartelle studente preparate e Studio avviato prima di B1. Nessun database esterno o OCR. La [guida](laboratorio/docente/SOLUZIONI.md) separa questa preparazione dal percorso studente e indica cosa registrare e collaudare.

Il repository non contiene pesi/embedding e non certifica prestazioni su VM da 4 vCPU/8 GB senza GPU. Qualificare l'ambiente e il carico delle 10–12 coppie reali prima dell'erogazione.

Dalla root del repository, con destinazione e manifesto nuovi:

```bash
python laboratorio/preflight.py --output ambiente.json
python laboratorio/prepara_laboratorio.py --dest ../officina-studente
python laboratorio/avvia_studio.py --offline
```

Interfaccia prevista `http://localhost:8888`. Embedding già scelto in `Settings > General > Documents & RAG`; documenti tramite `+ > Chat with Files > Add files to chat with`. Verificare menu e salvare schermate della release adottata. Per ogni nuova chat riassociare il corpus corrente.

Il launcher imposta `RAG_THREAD_WHOLE_DOC=0` e, con `--offline`, modalità offline Hub/Transformers. Non è un firewall né una garanzia inter-versione: osservare realmente i passaggi recuperati. Eventuale `--models-dir` indica una cartella già popolata.

**GO base:** prove reali offline, indicizzazione/recupero osservati, sei query, rev2/storico, documento nuovo, export CSV, report, Git e carico concorrente. OpenCode non è richiesto. Un endpoint di sola generazione LAN/cloud non sostituisce il recupero; nessun fallback improvvisato in aula.

## 4. Operazioni studente

Seguire il quaderno. Aprire `risultati.csv` nell'applicazione tabellare predisposta, conservando colonne, UTF-8 e separatore `;`. Risposte brevi fedeli, citazioni con sezione/revisione, due giudizi. Il docente verifica il roundtrip prima del corso.

In B4 conservare `risultati_rev1.csv` e `risultati_rev2.csv`. In B5, dalla cartella personale:

```bash
git init
git config user.name "Nome Cognome"
git config user.email "nome.cognome@studenti.itsmaker.it"
git status
git add corpus risultati.csv risultati_rev1.csv risultati_rev2.csv genera_report.py
git commit -m "test: conserva prove RAG e confronto revisioni"
git log --oneline
```

In B6, dopo DOC-T10 e T08/T09:

```bash
python genera_report.py
```

Aprire `report.html` e controllare la corrispondenza con le prove. Nessun filtro o modifica al codice richiesti. Salvare corpus, tre CSV e report con Git secondo la dispensa. Non tracciare credenziali.

## 5. Compilazione documenti: solo docente

Ambiente Python dedicato; gli studenti non hanno bisogno di queste dipendenze. Per i PDF occorre Chrome/Chromium/Edge già installato.

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_materiali.py
```

Opzioni: `--html-only` per solo HTML, `--browser PERCORSO` per un browser specifico. HTML di stampa in `.build-materiali/`, slide HTML e tre PDF accanto ai relativi sorgenti.

## 6. Approfondimenti e fonti

Backend, credenziali e collaudo dell'agente sono nell'appendice della [guida docente](laboratorio/docente/SOLUZIONI.md), non nel percorso base. Nessuna soglia magica di parametri o promessa di velocità; usare misure reali.

- [Unsloth Studio Chat](https://unsloth.ai/docs/new/studio/chat)
- [Changelog](https://unsloth.ai/docs/new/changelog)
- [Configurazione RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/config.py)
- [Store RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/store.py)
- [API Studio](https://unsloth.ai/docs/basics/api)
- [OpenCode, facoltativo](https://unsloth.ai/docs/integrations/opencode)
