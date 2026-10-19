# Progettazione modulo: costruire e verificare un assistente documentale RAG

**Corso:** Tecnico Superiore per la Digitalizzazione dei Processi Industriali – ITS MAKER Bologna  
**Destinatari:** 20–24 studenti tecnici, neofiti AI/LLM; lavoro a coppie con ruoli Operatore e Collaudatore alternati a ogni blocco.  
**Durata:** 6 ore: 315 minuti di attività e 45 di pause/margine. Estensione a 8 ore: altri 120 minuti.  
**Prodotto finale:** corpus aggiornato, prove documentate e report di un piccolo assistente documentale. Nessun collegamento a macchine, PLC o funzioni di sicurezza.

## 1. Principio didattico e obiettivi

**Semplificare gli strumenti, non il ragionamento.** Il corso parte da una domanda concreta e insegna a decidere se una risposta è sostenuta dalle fonti. Unsloth Studio è l'ambiente, non l'oggetto principale della valutazione. Non servono installazioni, programmazione o scelta dei modelli durante il percorso base.

Al termine lo studente sa:

- distinguere modello, contesto e documenti; spiegare perché interrogare o aggiornare un RAG non modifica i pesi dell'LLM;
- associare un corpus alla chat e aprire i passaggi recuperati;
- valutare separatamente recupero e risposta, verificando citazioni, identificativi e calcoli;
- riconoscere un dato assente e una confusione fra macchine simili;
- aggiornare la fonte corrente senza riscrivere un evento storico;
- applicare il metodo a un documento nuovo, con una domanda rispondibile e una su un dato omesso;
- conservare evidenze e revisioni con pochi comandi Git.

Token ed embedding si spiegano qualitativamente: unità di testo e rappresentazioni utili alla ricerca. Quantizzazione, formati dei pesi e benchmark non sono prerequisiti. Un errore del modello riconosciuto e spiegato è un risultato didattico valido.

## 2. Percorso base: sei ore

| Blocco | Minuti | Attività e risultato osservabile |
| --- | ---: | --- |
| B1 · Il problema e i fondamenti | 40 | T01 senza fonti nei primi minuti; esperimento sul contesto; distinguere plausibilità ed evidenza. |
| B2 · Primo RAG guidato | 65 | Associare i cinque documenti, osservare recupero e fonti, ripetere T01. |
| B3 · Prove e diagnosi | 75 | T02–T06, domanda autonoma T07, doppio giudizio recupero/risposta. |
| B4 · Aggiornare le fonti | 40 | Conservare rev1, sostituire catalogo, nuova chat con corpus aggiornato, verificare corrente e storico. |
| B5 · Git sulle evidenze | 25 | Salvare corpus e risultati; leggere stato, differenze e cronologia. Nessun esercizio separato su codice macchina. |
| B6 · Autonomia e restituzione | 70 | Scrivere un documento nuovo, prove T08/T09 con coppia vicina, report e spiegazione finale. |
| Pause e margine | 45 | Distribuiti dal docente. |
| **Totale** | **360** | **315 minuti netti; spiegazioni comprese nei blocchi.** |

Tempi proposti da provare sull'aula reale. Il docente prepara workspace e avvia Studio prima di B1; non si sottrae tempo al RAG per configurare l'ambiente.

## 3. Il caso d'officina e le prove

Il corpus iniziale contiene cinque Markdown sintetici: scheda P03, rapporto di fermo P03, catalogo ricambi, bolla di consegna e scheda P30. Il corpus piccolo rende leggibili tutte le fonti: non dimostra capacità su archivi industriali di grandi dimensioni.

| Caso | Competenza da osservare |
| --- | --- |
| T01 · Catalogo | Identificare il filtro nel catalogo corrente, con revisione; non dedurlo dal rapporto storico. |
| T02 · Calcolo | Recuperare temperatura e soglia, controllare la differenza con un calcolo indipendente. |
| T03 · Quantità | Distinguere quantità ordinata e consegnata. |
| T04 · Parafrasi | Trovare la durata del fermo chiedendo dell'indisponibilità. |
| T05 · Dato assente | Verificare l'assenza nel corpus e riconoscere astensione o invenzione. |
| T06 · Distrattore | Distinguere P03 e P30 e verificare entrambe le fonti. |
| T07 · Domanda della coppia | Formulare una domanda incrociata sui documenti iniziali e motivare il giudizio. |
| T08 · Documento nuovo | Verificare un dato presente in DOC-T10, scritto durante B6. |
| T09 · Test negativo autonomo | Chiedere un dato intenzionalmente omesso in DOC-T10 e controllare l'astensione. |

### Evidenze leggere, giudizi rigorosi

Usare `risultati.csv` con lo schema esistente: `id;domanda;documenti_recuperati;risposta;citazioni;esito_recupero;esito_risposta;note`. Il docente predispone un foglio elettronico/editor tabellare con importazione ed esportazione UTF-8, separatore `;`, verificata prima dell'aula. Gli studenti non devono gestire manualmente virgolette e righe CSV.

Registrare una risposta osservata breve ma fedele, fonte/sezione/revisione e una nota solo quando serve. Non copiare conversazioni intere. Stati ammessi: `OK`, `ERRORE`, `NON_ESEGUITO`; mai trasformare un errore dell'AI in successo per completare la consegna. Se il recupero non è osservabile, lasciare il relativo giudizio NON_ESEGUITO e dichiarare il limite. Per T05/T09 un risultato di ricerca vuoto non prova da solo che il dato sia assente: controllare anche il corpus.

La baseline senza fonti di B1 resta nel quaderno, distinta dai risultati RAG. Prima di aggiornare il catalogo salvare `risultati_rev1.csv`; dopo il confronto salvare `risultati_rev2.csv`. Usare le note di T01 per conservare anche la risposta osservata sul ricambio storico. In B6 aggiungere T08/T09 a `risultati.csv`, senza cambiare colonne.

## 4. Una sola configurazione di riferimento, preparata prima dell'aula

Il percorso base usa Studio locale già pronto, un solo LLM e un embedding multilingue collaudato sul corpus italiano. Nessun database esterno, OCR o PDF scansito. Nessuna scelta di provider o gestione di chiavi per gli studenti.

Il budget indicativo delle VM (4 vCPU, 8 GB RAM, nessuna GPU dedicata) **non è una garanzia di compatibilità o prestazioni**. Il responsabile tecnico deve qualificare l'immagine sull'host VMware con il carico delle 10–12 coppie prima dell'erogazione.

La [guida docente](laboratorio/docente/SOLUZIONI.md) contiene la scheda d'ambiente da completare con versioni effettive, modelli e revisioni, impostazioni e schermate dei menu. Il repository non include pesi o embedding e non fornisce una configurazione già qualificata per l'aula.

### Condizioni GO / NO-GO del percorso base

GO dopo prova reale di avvio offline, indicizzazione, passaggi recuperati osservabili, T01–T06, aggiornamento rev2, documento nuovo con dato assente, esportazione tabellare, report e Git, con carico concorrente e tempi accettabili misurati. Documentare gli errori: non occorre che ogni risposta del modello sia corretta, ma il laboratorio deve consentire di diagnosticarla.

`preflight.py` registra CLI e impronte del corpus: non certifica inferenza o RAG. OpenCode non è un requisito GO del corso base. Se il RAG non funziona, correggere l'ambiente prima del corso; un'API di generazione LAN/cloud non sostituisce il recupero e non è un fallback automatico. Un eventuale ambiente alternativo deve essere qualificato per lo stesso percorso completo.

## 5. Aggiornamento e autonomia: i due passaggi decisivi

In B4 il docente consegna la rev2: sostituire il contenuto di `corpus/03_catalogo_ricambi.md`, senza tenere due cataloghi entrambi correnti. Aprire una chat pulita e riassociare i cinque file aggiornati. T01 deve essere confrontata con DOC-RICAMBI rev2 (FLT-993); il rapporto storico conserva FLT-992. Se il sistema sbaglia, registrare e diagnosticare fonte, revisione e contesto. Non cambiare retroattivamente le prove rev1.

In B6 ogni coppia scrive `06_scheda_macchina_T10.md` con DocID DOC-T10, data, revisione, due dati sintetici e un dato intenzionalmente omesso, assente anche dagli altri documenti. Nuova chat con il corpus corrente e il sesto file. La coppia vicina esegue una domanda su un dato presente (T08) e una sul dato omesso (T09). Si valuta la capacità di controllare le fonti, non la coincidenza con un copione.

Il report si genera con `python genera_report.py`, senza modificare il codice e senza OpenCode. Consegna: corpus corrente, CSV rev1/rev2, CSV finale T01–T09, report e breve spiegazione nelle note di un errore o rischio diagnosticato. Git conserva questi materiali, non credenziali né soluzioni docente.

## 6. Valutazione coerente con il fulcro RAG

| Criterio | Peso | Evidenza |
| --- | ---: | --- |
| Fonti e diagnosi recupero/risposta | 40% | Citazioni aperte, dati e calcoli verificati, giudizi distinti e motivati. |
| Revisioni e storico | 25% | Confronto prima/dopo, fonte corrente distinta dall'evento passato. |
| Autonomia e test negativo | 20% | Documento nuovo, domanda presente/assente e controllo indipendente. |
| Tracciabilità delle evidenze e Git | 10% | Risultati conservati, differenze comprese, salvataggio finale. |
| Collaborazione | 5% | Alternanza dei ruoli e revisione tra coppie. |

Non valutare lo studente con la percentuale di risposte corrette del modello o il numero di commit. OpenCode e benchmark non modificano la rubrica base.

## 7. Otto ore e approfondimenti facoltativi

- **E1 · +60 minuti: diagnosi delle domande.** Stesso corpus e stessa configurazione; confrontare domanda letterale, sinonimi e gergo d'officina. Annotare passaggi recuperati e cambiamenti della risposta. Nessun tuning di chunk, overlap o embedding.
- **E2 · +60 minuti: sfida documentale ampliata.** Espandere il corpus con altri documenti sintetici, scambio fra coppie e collaudo cieco con dati presenti e assenti. È un approfondimento rispetto alla prima prova autonoma già obbligatoria in B6.

**Alternative facoltative a E2, scelte prima del corso:** un laboratorio OpenCode sul filtro del report, oppure un confronto guidato fra due configurazioni già disponibili. Occupano gli stessi 60 minuti di E2, non si sommano al programma di otto ore e non sono richiesti nelle sei ore. Per OpenCode servono qualifica aggiuntiva dell'agente e backend; per il confronto modelli, misure reali e variabili controllate. Dettagli nell'appendice docente.

## 8. Fonti primarie

- [Unsloth Studio Chat](https://unsloth.ai/docs/new/studio/chat)
- [Changelog](https://unsloth.ai/docs/new/changelog)
- [Configurazione RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/config.py)
- [Store RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/store.py)
- [API Studio](https://unsloth.ai/docs/basics/api)
- [OpenCode, solo approfondimento](https://unsloth.ai/docs/integrations/opencode)

I menu e i sorgenti upstream cambiano: fanno fede le prove e le schermate della release congelata per l'aula, non una compatibilità presunta.
