# Corso ITS MAKER Bologna: AI, LLM e RAG con Unsloth Studio

Corso introduttivo tecnico e pratico di 6–8 ore: esperimenti per capire gli LLM, consultazione di documenti con RAG nativo in Unsloth Studio, Git essenziale e una modifica guidata con OpenCode. Il prodotto finale è un assistente documentale collaudato e un report delle prove, non un sistema di controllo macchina.

---

## 1. Mappa dei Materiali del Repository

### Progettazione e Materiali Didattici
- [`PROPOSTA_DIDATTICA_ITS_MAKER.md`](./PROPOSTA_DIDATTICA_ITS_MAKER.md) – Sorgente autorevole del piano didattico, architettura 3 livelli, checklist Golden Image e cronoprogramma.
- [`PROPOSTA_DIDATTICA_ITS_MAKER.pdf`](./PROPOSTA_DIDATTICA_ITS_MAKER.pdf) – Documento derivato per consultazione/stampa.
- [`materiali_aula/DISPENSA_OPERATIVA_STUDENTI.md`](./materiali_aula/DISPENSA_OPERATIVA_STUDENTI.md) – Quaderno di laboratorio operativo per lo studente.
- [`materiali_aula/DISPENSA_OPERATIVA_STUDENTI.pdf`](./materiali_aula/DISPENSA_OPERATIVA_STUDENTI.pdf) – Documento derivato stampabile.
- [`materiali_aula/SLIDE_DOCENTE_ITS_MAKER.md`](./materiali_aula/SLIDE_DOCENTE_ITS_MAKER.md) – Sorgente Markdown delle diapositive con note di regia docente.
- [`materiali_aula/SLIDE_DOCENTE_ITS_MAKER.html`](./materiali_aula/SLIDE_DOCENTE_ITS_MAKER.html) e [`.pdf`](./materiali_aula/SLIDE_DOCENTE_ITS_MAKER.pdf) – Presentazione 16:9 offline e versione PDF derivata.

> **Ruolo dei File Derivati:** solo i documenti didattici (`PROPOSTA_DIDATTICA_ITS_MAKER`, `DISPENSA_OPERATIVA_STUDENTI`, `SLIDE_DOCENTE_ITS_MAKER`) possiedono versioni HTML/PDF compilate a partire dai Markdown sorgente tramite `scripts/build_materiali.py`. I file derivati riflettono il contenuto del Markdown ma non producono output byte-identici tra rigenerazioni diverse. File come `parametri_cnc.html` e `report.html` appartengono invece al laboratorio pratico.

### Laboratorio e File Operativi (`laboratorio/`)
- [`laboratorio/avvia_studio.py`](./laboratorio/avvia_studio.py) – Avvia Studio con `RAG_THREAD_WHOLE_DOC=0` nel processo figlio; con `--offline` imposta anche le modalità offline Hub/Transformers. Il recupero effettivo va verificato sulla release adottata: il launcher non è un firewall.
- [`laboratorio/preflight.py`](./laboratorio/preflight.py) – Verifica comandi CLI (`git`, `unsloth`, `opencode`), interprete Python (>= 3.10) e hash SHA256 del corpus.
- [`laboratorio/prepara_laboratorio.py`](./laboratorio/prepara_laboratorio.py) – Allestisce la cartella di lavoro pulita per lo studente.
- **Corpus Officina (`laboratorio/corpus/`):** `01_scheda_P03.md`, `02_rapporto_fermo_P03.md`, `03_catalogo_ricambi.md`, `04_bolla_consegna.md`, `05_scheda_P30.md`.
- **File Starter Studente (`laboratorio/starter/`):** `risultati.csv` (matrice T01–T06 con esiti iniziali `NON_ESEGUITO`), `genera_report.py` (esportazione HTML), `parametri_cnc.html` (esercizio Git).
- **Materiali Docente (`laboratorio/docente/`):** `03_catalogo_ricambi_rev2.md`, [`SOLUZIONI.md`](./laboratorio/docente/SOLUZIONI.md) e `genera_report_soluzione.py`. La repository è pubblica: la separazione evita copie accidentali, non rende segrete le soluzioni.

### Script di Compilazione Documentale (`scripts/`)
- [`scripts/build_materiali.py`](./scripts/build_materiali.py) – Compilatore Markdown -> HTML e PDF (dipendenze in [`requirements-docs.txt`](./requirements-docs.txt), uso docente).

---

## 2. Comandi Operativi di Laboratorio (PowerShell e Bash)

### 2.1 Verifica Ambiente e Setup Studente
Il docente esegue il preflight dalla root e conserva il manifesto; il comando rifiuta di sovrascrivere un file esistente. Per gli studenti distribuire soltanto la cartella generata, non la repository con le soluzioni.
```bash
python laboratorio/preflight.py --output ambiente.json
python laboratorio/prepara_laboratorio.py --dest ../officina-studente
cd ../officina-studente
```

### 2.2 Git Essenziale (Configurazione Locale e Salvataggi)
```bash
git init
git config user.name "Mario Rossi"
git config user.email "mario.rossi@studenti.itsmaker.it"
git status
git diff
git add parametri_cnc.html
git commit -m "Aggiornati RPM mandrino a 4500"
git log --oneline
# Ripristino di modifiche non staged su file tracciato:
git restore -- parametri_cnc.html
```

### 2.3 Avvio Unsloth Studio (Piano A: Locale)
Dalla root del repository:
```bash
python laboratorio/avvia_studio.py --offline
```
Interfaccia attiva su `http://localhost:8888`. Embedding in `Settings > General > Documents & RAG`; corpus associato via `+ > Chat with Files > Add files to chat with`.
Il docente può aggiungere `--models-dir "PERCORSO_CARTELLA_MODELLI"` per una cartella già popolata. Il RAG è associato alla chat: in una conversazione nuova riassociare il corpus corrente. I menu seguono la documentazione attuale e vanno verificati prima di congelare l'immagine d'aula. Il supporto CLI verificato non certifica inferenza, indicizzazione o capacità delle VM.

### 2.4 Avvio Server LAN OpenCode (Piano B: Docente)
Server dedicato su porta distinta (8889), one-line valida per PowerShell e Bash:
```bash
unsloth run --model unsloth/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M -H 0.0.0.0 -p 8889 --disable-tools
```
*Il flag `--disable-tools` è una scelta esplicita per il backend OpenCode, non per la chat RAG. Usare una chiave realmente generata in `Settings > API`; configurare il provider OpenAI-compatible di OpenCode con URL `http://IP_DOCENTE:8889/v1`, modello e chiave effettivi. Il comando di avvio locale da solo non seleziona automaticamente questo server. Limitare la porta alla LAN d'aula e non salvare credenziali nei file tracciati.*

### 2.5 Avvio OpenCode e Generazione Report
```bash
# Avvio agente OpenCode:
unsloth start opencode

# Generazione report dalla cartella studente (dopo aver compilato risultati.csv):
python genera_report.py
python genera_report.py --input risultati.csv --output report.html
```

---

## 3. Compilazione Documentazione Didattica (Solo Docente)

Usare un ambiente Python dedicato al docente. Le dipendenze includono Markdown, supporto ai blocchi di codice annidati e Playwright; gli studenti non ne hanno bisogno. Per i PDF serve un Chrome/Chromium/Edge già installato: lo script lo pilota senza scaricare un altro browser. `--html-only` non avvia il browser.

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_materiali.py
python scripts/build_materiali.py --html-only
python scripts/build_materiali.py --browser "C:\Program Files\Google\Chrome\Application\chrome.exe"
```

---

## 4. Sintesi Programma 6 Ore (360 min totali: 315 min attività, 45 min pause)

- **B1 (60 min):** Fondamenti AI/LLM attraverso token, contesto e verifica delle risposte. Il docente avvia Studio prima di B1.
- **B2 (30 min):** Git essenziale: setup locale, commit atomici, verifica `git restore --`.
- **B3 (30 min):** Unsloth Studio: confronto 2 quantizzazioni (4-bit vs 2-bit), rilievo empirico RAM/latenza.
- **B4 (90 min):** RAG nativo: indicizzazione corpus, query T01–T06 su `risultati.csv`, aggiornamento rev2 catalogo.
- **B5 (45 min):** OpenCode: modifica mirata a `genera_report.py` (filtro client-side "Solo da rivedere").
- **B6 (60 min):** Collaudo incrociato a ruoli alternati (operatore/collaudatore) e consegna.
*(Estensione 8h: E1 +60 min tuning RAG a variabili isolate; E2 +60 min corpus personalizzato e sfide tra banchi).*

Prima dell'erogazione seguire la [checklist docente e i criteri GO/NO-GO](./laboratorio/docente/SOLUZIONI.md): servono prove reali offline, di recupero, di tool calling e di carico concorrente. I tempi sono una proposta didattica, non una misura già effettuata sulle VM dell'istituto.

---

## 5. Fonti Primarie e Documentazione Ufficiale

- [Unsloth Studio Chat & UI](https://unsloth.ai/docs/new/studio/chat)
- [Unsloth Changelog](https://unsloth.ai/docs/new/changelog)
- [Unsloth Studio API](https://unsloth.ai/docs/basics/api)
- [Unsloth OpenCode Integration](https://unsloth.ai/docs/integrations/opencode)
- [Unsloth RAG Config (`config.py`)](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/config.py)
- [Unsloth RAG Store (`store.py`)](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/store.py)
- [OpenRouter Pricing & Limits](https://openrouter.ai/pricing)
