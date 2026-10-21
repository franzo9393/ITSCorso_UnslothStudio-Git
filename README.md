# ITS MAKER Bologna · Unsloth Studio

**Esplorare i modelli, lavorare sui documenti e capire la personalizzazione.** Modulo di 6–8 ore per studenti tecnici neofiti: Unsloth Studio è il prodotto al centro; il RAG è il laboratorio principale, affiancato da chat/contesto, scelta dell'approccio, dataset, valutazione ed export.

**Nessun deployment obbligatorio sui PC studenti.** Ambiente docente qualificato, sandbox Unsloth nel browser solo se collaudate, eventuali turni di gruppo e casi offline ricavati da esecuzioni reali. Non si presume potenza delle macchine, GPU gratuita o multiutenza sicura. NotebookLM è soltanto un confronto facoltativo.

## 1. Materiali

- [Proposta didattica](PROPOSTA_DIDATTICA_ITS_MAKER.md) · [PDF](PROPOSTA_DIDATTICA_ITS_MAKER.pdf): obiettivi, tempi, modalità e valutazione.
- [Quaderno studenti](materiali_aula/DISPENSA_OPERATIVA_STUDENTI.md) · [PDF](materiali_aula/DISPENSA_OPERATIVA_STUDENTI.pdf): esperimenti, scheda risultati, mini-dataset e verifica individuale.
- [Slide docente](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.md) · [HTML offline](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.html) · [PDF](materiali_aula/SLIDE_DOCENTE_ITS_MAKER.pdf).
- [Guida docente](laboratorio/docente/SOLUZIONI.md): regia, risposte, preparazione e GO distinti per percorso guidato, sandbox e training.
- [Risorse e accesso](materiali_aula/RISORSE_E_ACCESSO.md): documentazione ufficiale, risorse gratuite, limiti cloud e checklist di selezione.

Markdown come sorgente; `scripts/build_materiali.py` rigenera HTML delle slide e tre PDF didattici. I PDF non sono byte-identici fra compilazioni.

## 2. Programma delle sei ore

| Blocco | Minuti | Risultato |
| --- | ---: | --- |
| B1 · Potenzialità e scelte | 35 | Mappa di Studio, ricerca manuale e scelta istruzioni/RAG/fine-tuning. |
| B2 · Esplorazione guidata di Studio | 50 | Chat, contesto, baseline T01 senza documenti, orientamento nel prodotto. |
| B3 · Laboratorio documentale e diagnosi | 80 | T01, T02, T05, T06; fonti e recupero/risposta. T03/T04 facoltative. |
| B4 · Aggiornamento e ricollaudo | 45 | Rev2 e storico; intervento su fonte ambigua separata e controllo prima/dopo. |
| B5 · Dataset e personalizzazione | 45 | Esempi input/output, controesempio, caso non visto; training/valutazione/export spiegati in Studio. |
| B6 · Sfida e restituzione | 60 | T07, nuova DOC-T10 e T08/T09, dossier e verifica individuale. |
| Pause e margine | 45 | Totale 360 minuti, 315 netti. |

**Otto ore:** E1 +60 su corpus ampliato e collaudo cieco; E2 +60 su dataset e valutazione. OpenCode oppure confronto modelli può sostituire E2 se preparato prima, non sommarsi alle otto ore.

Valutazione: scelta e comprensione Unsloth 20%, fonti/diagnosi 30%, revisione/intervento 20%, autonomia e verifica individuale 20%, tracciabilità e collaborazione 10%. Non si valuta l'accesso all'hardware o la percentuale di risposte corrette del modello.

## 3. Accesso e continuità

Per ogni prova dichiarare una modalità: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`. Non confondere la provenienza dell'evidenza con il giudizio sul risultato. Analizzare correttamente una traccia non certifica di aver eseguito autonomamente la funzione.

Il minimo è un ambiente **Unsloth docente collaudato in preparazione**, con casi offline disponibili per proseguire in caso di interruzioni. Sandbox separate o turni su postazioni predisposte sono un'estensione dell'accesso, non un obbligo su ogni PC. Nessuna installazione, account esterno, carta di credito, chiave API o programmazione richiesta agli studenti nel percorso guidato.

**Il kit non include pesi, embedding, immagine qualificata, schermate d'aula o tracce AI registrate.** Prima dell'erogazione il docente deve produrre queste evidenze sull'ambiente scelto, secondo la guida. Non dichiarare il laboratorio pronto perché gli script di supporto funzionano. Senza una traccia, discutere solo il risultato atteso dalle fonti e non inventare output.

Il GO sandbox richiede verifica di rete, autenticazione, isolamento chat/file, autorizzazioni, pulizia e carico. Non basta esporre Studio sulla LAN o condividere un accesso amministrativo. Training e integrazioni agentiche hanno un GO aggiuntivo; non sono requisiti delle sei ore.

**Indirizzo operativo in valutazione:** Studio nelle VM locali degli studenti con risorse limitate, partendo dal collaudo di un RAG lessicale BM25. La scuola segnala anche Copilot Basic disponibile agli studenti: chat documentale, Copilot Notebooks e Agenti hanno requisiti distinti da provare con un vero account studente. Non presumere inclusi Notebooks o agenti con conoscenza su file/SharePoint, né attivare consumi a pagamento. Scelte, limiti e checklist sono nelle [sezioni 3.1 e 3.2 di Risorse e accesso](materiali_aula/RISORSE_E_ACCESSO.md#31-indirizzo-operativo-vm-locali-con-risorse-limitate); non costituiscono un collaudo già superato o una sostituzione implicita del percorso locale.

## 4. Kit operativo e consegna

- `laboratorio/corpus/`: cinque documenti sintetici leggibili integralmente. Non prova di scalabilità industriale.
- `laboratorio/starter/risultati.csv`: schema di otto colonne invariato; T01–T06 inizialmente NON_ESEGUITO. T03/T04 facoltative; T07–T09 si aggiungono in B6. Modalità e riferimento della traccia nelle note.
- `laboratorio/starter/genera_report.py`: supporto facoltativo per un report HTML offline dei giudizi umani; non interroga l'AI.
- `laboratorio/prepara_laboratorio.py`: prepara una cartella senza soluzioni, non installa Studio.
- `laboratorio/preflight.py`: registra CLI e hash; non certifica inferenza/RAG, isolamento o hardware. OpenCode facoltativo.
- `laboratorio/avvia_studio.py`: launcher per l'ambiente predisposto dal docente; non crea sandbox remote o utenti.
- `laboratorio/docente/`: guida, catalogo rev2 per B4 e soluzione dell'estensione OpenCode. Repository pubblico: separazione didattica, non controllo di accesso.

Consegna minima: scheda cartacea/digitale con scelta dell'approccio, prove/fonti e modalità, confronto rev1/rev2, ipotesi/intervento/ricollaudo, documento nuovo, mini-dataset con caso riservato e risposte individuali. CSV, Python/report e Git non obbligatori. Solo dati sintetici, nessun uso su macchine o PLC.

Se si usa il CSV: UTF-8 e separatore `;`, import/export verificato dal docente, risposte brevi fedeli, citazioni controllate e giudizi `OK`, `ERRORE`, `NON_ESEGUITO`. Recupero non osservabile resta NON_ESEGUITO; non è sufficiente una citazione. Conservare rev1 prima dell'aggiornamento e rev2 dopo. T03/T04 non svolte: nota «facoltativa non svolta». Non pretendere nove prove eseguite da ogni coppia.

## 5. Preparazione tecnica: solo docente

Dalla root, con destinazione e manifesto nuovi:

```bash
python laboratorio/preflight.py --output ambiente.json
python laboratorio/prepara_laboratorio.py --dest ../officina-studente
python laboratorio/avvia_studio.py --offline
```

Questi comandi non scaricano pesi né qualificano l'ambiente. Indirizzo locale previsto `http://localhost:8888`, da controllare nella release adottata; non è l'indirizzo delle eventuali sandbox remote. Salvare schermate reali dei menu, versione e risultati della prova completa.

Il launcher imposta `RAG_THREAD_WHOLE_DOC=0` e, con `--offline`, le modalità offline Hub/Transformers. Non è un firewall né una garanzia inter-versione. Osservare realmente il recupero; cambiare il file sul disco non aggiorna automaticamente vecchie chat/indici. Un endpoint di sola generazione non sostituisce il RAG.

Se si usa Git come supporto, fare il primo checkpoint **prima di B4**, con corpus rev1 e prove iniziali, e confrontare poi il catalogo aggiornato. Il docente può generare il report dal workspace con `python genera_report.py`; non far installare Python agli studenti per consegnare.

## 6. Compilazione dei materiali

Ambiente Python dedicato del docente, con Chrome/Chromium/Edge disponibile:

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_materiali.py
```

`--html-only` genera HTML senza browser; `--browser PERCORSO` sceglie l'eseguibile. HTML di stampa in `.build-materiali/`, slide HTML e tre PDF accanto ai sorgenti. Risorse e guida docente sono consultabili in Markdown.

## 7. Risorse ufficiali

Partire da [Unsloth Studio](https://unsloth.ai/docs/new/studio), dal [percorso guidato](https://unsloth.ai/docs/new/studio/start) e dalla [guida risorse del modulo](materiali_aula/RISORSE_E_ACCESSO.md). La documentazione descrive possibilità del prodotto, non una configurazione già qualificata sulle macchine dell'istituto. Nessuna promessa di velocità, training o GPU gratuita.
