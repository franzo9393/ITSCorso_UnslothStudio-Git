# Guida docente: un percorso RAG pronto da insegnare

Materiale docente: non importare nel RAG. Distribuire solo il workspace studente, non soluzioni o rev2 anticipata. Il repository è pubblico: le cartelle non costituiscono controllo di accesso.

## 1. Preparare una volta, insegnare senza configurazioni

Il corso base richiede Studio, Python 3.10+, Git, un editor e un foglio elettronico/editor tabellare. **Non richiede OpenCode**, benchmark, database esterni, OCR o modifiche al codice. Il kit non comprende LLM o embedding e non certifica le VM dell'istituto.

Il responsabile tecnico congela una sola immagine locale con un modello instruct e un embedding multilingue provati sulle domande italiane. Non lasciare al docente d'aula la scelta fra backend durante la lezione. Scegliere prima anche sistema operativo e shell; tutti i comandi devono funzionare con `python` oppure essere adattati coerentemente a `python3` prima della distribuzione.

### Scheda della configurazione di riferimento

Compilare con dati misurati prima di dichiarare l'ambiente pronto; non è una configurazione già qualificata dal repository.

| Voce | Registrazione richiesta |
| --- | --- |
| Sistema, shell, Python, Git | Versioni effettive e comando Python disponibile. |
| Studio e runtime | Versioni/revisioni congelate, nessun aggiornamento in aula. |
| LLM locale | Identificativo, revisione/hash, file GGUF e quantizzazione. |
| Embedding locale | Identificativo e revisione multilingue; eventuali prefissi query/documento. |
| Impostazioni | Contesto, generazione, thread; nessuna modifica richiesta agli studenti. |
| Interfaccia | Schermate della release: allegare corpus, aprire passaggi/fonti, nuova chat. |
| Risorse | RAM e CPU effettive, carico simultaneo delle 10–12 coppie. |
| Prove | Risposte osservate, recupero, rev2, documento nuovo, tempi e anomalie. |
| Tavola risultati | Applicazione/versione, import/export UTF-8 con `;` verificato. |

4 vCPU e 8 GB RAM senza GPU sono un budget da provare, non una promessa di eseguibilità. Scaricare prima modello, embedding, tokenizer e runtime. Il predefinito inglese non è automaticamente adeguato al corpus italiano.

### Preparazione dei workspace prima di B1

Dalla root, usando percorsi nuovi per non sovrascrivere prove precedenti:

```bash
python laboratorio/preflight.py --output ambiente.json
python laboratorio/prepara_laboratorio.py --dest ../officina-collaudo
cd ../officina-collaudo
python genera_report.py
```

Il preflight registra CLI e hash del corpus, non prova inferenza o RAG. La mancanza di OpenCode non deve bloccare il percorso base. Conservare il manifesto fuori dai workspace studenti. La cartella generata contiene `corpus/`, `risultati.csv`, `genera_report.py`; nessuna soluzione. Preparare una cartella personale per coppia prima della lezione. Non inizializzare Git: verrà introdotto in B5 su evidenze già prodotte.

Predisporre l'apertura di `risultati.csv` come tabella (UTF-8, `;`, tutte le colonne come testo). Provare salvataggio, riapertura e `python genera_report.py` con una copia tecnica contenente accenti, virgolette e un punto e virgola in una cella. Non distribuire dati fittizi come risultati AI: lo starter rimane NON_ESEGUITO. Chiudere il foglio prima di generare il report e assicurarsi che l'estensione resti `.csv`.

## 2. Avvio e collaudo tecnico: solo prima dell'aula

```bash
python laboratorio/avvia_studio.py --offline
```

Dalla root del corso; eventualmente usare `--models-dir` con una directory già popolata. Avviare e caricare modello ed embedding prima di B1. Interfaccia prevista: `http://localhost:8888`; verificare l'indirizzo nella release adottata. Non aprire una seconda istanza sulla stessa porta.

Il launcher imposta nel processo figlio `RAG_THREAD_WHOLE_DOC=0` e, con `--offline`, `HF_HUB_OFFLINE=1` e `TRANSFORMERS_OFFLINE=1`. Queste variabili non sono un firewall né una garanzia inter-versione. Disattivare web search e provider remoti; provare senza rete. Se il controllo whole-doc non è rispettato o il recupero non è osservabile, correggere l'ambiente prima del corso: una risposta da allegato intero non dimostra ricerca selettiva.

Percorso documentato, da congelare con schermate reali:
1. Embedding in **Settings → General → Documents & RAG**: già configurato; non farlo scegliere agli studenti.
2. Chat pulita: **+ → Chat with Files → Add files to chat with**; scegliere solo i cinque Markdown di `corpus/`.
3. Attendere indicizzazione e aprire passaggi restituiti o chiamata `search_knowledge_base`, poi le fonti. Non basta contare le citazioni.
4. Per ogni nuova chat riassociare il corpus corrente. Non presumere un indice globale fra conversazioni.
5. Cambiare embedding richiede reindicizzazione: non farlo nel percorso base.

Lo store nativo combina ricerca testuale e vettoriale in SQLite: non serve un server aggiuntivo. Nei documenti piccoli il controllo whole-doc è importante per osservare il recupero; non presentare il corpus didattico come prova di scalabilità industriale.

### Note tecniche: chiarire senza aggiungere strumenti

- **Metadati testuali e filtri non coincidono.** DocID, macchina, data e revisione nell'intestazione aiutano la verifica umana. Diventano filtri software solo se acquisiti come campi strutturati e usati effettivamente dal motore: non presumere che Studio lo faccia automaticamente. Nessun esercizio su filtri o nuova funzione dell'interfaccia nel percorso base.
- **Uno score non è una percentuale di correttezza.** Se la release mostra punteggi, verificarne il significato prima di commentarli: una similarità di solito cresce con l'affinità, una distanza diminuisce. Non fissare soglie universali né dedurre la verità del dato dal numero; leggere il passaggio resta il controllo decisivo.
- **RAG e comportamento agentico sono dimensioni diverse.** Il RAG porta evidenze documentali nel contesto; un agente può scegliere ed eseguire strumenti, anche di recupero. Possono coesistere. Questo chiarimento non introduce azioni su macchine o gestionali né un nuovo laboratorio obbligatorio.

### GO / NO-GO base

Prima dell'erogazione provare: avvio offline, indicizzazione e passaggi osservabili, sei domande, aggiornamento rev2 e storico, aggiunta di un documento nuovo con dato omesso, roundtrip del foglio risultati, report HTML, salvataggi Git e carico concorrente sull'aula. Documentare tempi ed errori. Un modello che sbaglia può essere istruttivo; un sistema che non permette di osservare il recupero non realizza il laboratorio dichiarato.

OpenCode e il suo tool calling sono fuori dal GO base. Un'API LAN/cloud di sola generazione non sostituisce il RAG. Un eventuale ambiente alternativo deve essere qualificato per l'intero percorso prima della lezione; niente installazioni o cambio provider improvvisato in aula. Usare esclusivamente dati sintetici.

## 3. Regia delle sei ore

| Blocco | Minuti | Regia e controllo di uscita |
| --- | ---: | --- |
| B1 | 40 | T01 senza documenti subito; annotazione nel quaderno, non nel CSV RAG. Regola BLU-17 nella stessa chat e poi chat pulita: distinguere contesto e pesi. |
| B2 | 65 | Distinguere preparazione (corpus, chunk, embedding, indice) e interrogazione (ricerca, contesto, risposta), poi verificare la fonte. Ripetere T01 e compilare insieme una riga. |
| B3 | 75 | Coppie su T02–T06, poi T07 propria. Chiarire contesto dei chunk e semantica/codici esatti sui casi esistenti. Confrontare fonte pertinente/risposta errata o discuterne il rischio se non osservato. |
| B4 | 40 | Copia risultati rev1; consegna rev2; nuova chat col corpus aggiornato; T01 e domanda sullo storico; copia rev2. |
| B5 | 25 | Git sui file del laboratorio: inizializzazione, checkpoint, diff e conservazione. Non insegnare un secondo caso sugli RPM. |
| B6 | 70 | 15 min documento nuovo, 15 indicizzazione e T08/T09, 15 revisione vicina, 15 report/consegna, 10 restituzione. |
| Pause/margine | 45 | Distribuire. Totale 360, attività nette 315. |

Scambiare Operatore/Collaudatore a ogni blocco. Le spiegazioni sono incluse, non aggiuntive. Se una risposta sbaglia, non correggere il CSV per farlo sembrare un successo.

In B2 il box sul contesto esteso risponde a «perché non incollare tutto?»: capacità, rumore e lavoro di elaborazione, senza promettere che il RAG sia sempre più rapido o corretto. In B3 usare l'esempio su carta dei 12 minuti per distinguere dato isolato e contesto necessario; non modificare il corpus per provocare un errore e non aggiungere prove al CSV. Per T04/T06 distinguere somiglianza di significato e identità dei codici, senza presentare la ricerca ibrida come garanzia. Questi chiarimenti sostengono le attività esistenti, non aggiungono blocchi o minuti.

## 4. Risposte sostenute dal corpus e doppio giudizio

| ID | Risposta attesa dalle fonti | Controllo |
| --- | --- | --- |
| T01 | P03: FLT-992 nel catalogo iniziale. | DOC-RICAMBI rev1, Associazioni macchina-filtro; non basta il rapporto storico. |
| T02 | 13 °C, cioè 78 − 65. | DOC-FERMO, Nota dell'operatore; calcolo indipendente. |
| T03 | 45 cuscinetti SKF-6204 consegnati, non 50. | DOC-BOLLA, Messaggio del fornitore o Riepilogo verificabile. |
| T04 | 45 minuti. | DOC-FERMO, Durata dell'evento; riconoscere la parafrasi. |
| T05 | Coppia di serraggio non presente. | Controllare il corpus; candidati simili non sostengono un valore. |
| T06 | P03: 65 °C; 55 °C riguarda P30. | DOC-P03 e DOC-P30, Soglia didattica di temperatura. |
| T07 | Dipende dalla domanda della coppia. | Fonte e criterio esplicitati prima di giudicare. |
| T08/T09 | Dato presente/omesso della nuova DOC-T10. | Controllo indipendente sul documento scritto in B6. |

`esito_recupero=OK`: passaggi necessari disponibili e identificati; `ERRORE`: fonti mancanti o scambiate; `NON_ESEGUITO`: recupero non osservato o prova non svolta. Per T05/T09, OK richiede che i passaggi osservati non offrano evidenze del dato e che la verifica del corpus ne confermi l'assenza. Non attribuire al motore la capacità di provare l'assenza solo perché restituisce zero risultati.

`esito_risposta=OK`: risposta sostenuta dalle fonti, numeri/citazioni corretti; per dato assente, astensione senza invenzioni. ERRORE per dato o citazione infondati. Una risposta corretta per caso può coesistere con recupero errato: non fondere i due giudizi.

Raccogliere risposta breve fedele, DocID/sezione/revisione e nota motivata, non trascrizioni integrali. Il report non interroga un modello e non assegna i giudizi.

Non rieseguire finché compare una risposta favorevole cancellando gli esiti precedenti. Una riformulazione è un'osservazione distinta da conservare, anche in E1. Un'esecuzione senza errori software non misura la correttezza della risposta: valgono i due giudizi e le fonti verificate.

## 5. Revisioni e prova autonoma

### B4: non riscrivere la storia

1. Salvare `risultati_rev1.csv` prima di modificare risultati o corpus.
2. Consegnare `03_catalogo_ricambi_rev2.md`; sostituire il contenuto del file studente `corpus/03_catalogo_ricambi.md`, senza duplicare cataloghi correnti.
3. Nuova chat e associazione dei cinque file aggiornati; attendere indicizzazione. Cambiare il file sul disco non aggiorna automaticamente la vecchia chat.
4. Ripetere T01: confrontare con FLT-993 e DOC-RICAMBI rev2. Registrare la risposta effettiva anche se errata.
5. Chiedere quale filtro fu usato nel fermo storico: DOC-FERMO mantiene FLT-992. Conservare domanda, risposta e fonte nelle note di T01.
6. Salvare `risultati_rev2.csv`. Spiegare che cambiano indice/contesto, non pesi.

### B6: trasferire il metodo

Ogni coppia scrive `corpus/06_scheda_macchina_T10.md`: DocID DOC-T10, data e revisione, due dati inventati verificabili e un dato omesso anche dal resto del corpus. Usare titoli espliciti e mantenere vicino a ciascun dato macchina, unità quando applicabile e condizioni di validità; evitare rimandi ambigui. È un criterio redazionale della stessa scheda, non un esercizio di tuning. Non includere procedure reali o istruzioni rivolte all'assistente. Nuova chat con i sei documenti correnti. La coppia vicina verifica T08 (dato presente) e T09 (dato omesso), registrate come nuove righe nello stesso CSV. La prima esperienza autonoma resta obbligatoria nelle sei ore.

Consegna: `corpus/`, `risultati_rev1.csv`, `risultati_rev2.csv`, `risultati.csv` con T01–T09 e `report.html`; note con spiegazione di un errore/rischio e sua evidenza. Salvare tutto con Git dopo il collaudo. Nessuna credenziale e nessuna soluzione docente.

## 6. Rubrica base

| Criterio | Peso | Evidenza |
| --- | ---: | --- |
| Fonti e diagnosi recupero/risposta | 40% | Fonti aperte, citazioni e calcoli verificati, giudizi distinti. |
| Revisioni e storico | 25% | Prima/dopo conservati; corrente distinto dal passato. |
| Autonomia e test negativo | 20% | Documento nuovo, T08/T09 e motivazione delle valutazioni. |
| Tracciabilità delle evidenze e Git | 10% | File conservati e differenze comprese. |
| Collaborazione | 5% | Alternanza e revisione incrociata. |

Valutare il metodo dello studente, non la percentuale di successi del modello né il numero di commit. Non penalizzare chi identifica correttamente un errore AI.

## 7. Estensione a otto ore

**E1 (+60):** tre formulazioni della stessa domanda (letterale, sinonimi, gergo); mantenere identici codici macchina e condizioni, variando solo l'espressione. Stesso corpus e configurazione: confrontare i passaggi e conservare le osservazioni, non cambiare chunk/overlap/embedding.

**E2 (+60):** sfida con corpus ampliato e collaudo cieco fra coppie, domande presenti/assenti e discussione degli errori. Non è la prima prova autonoma, già svolta in B6.

Una delle appendici seguenti può sostituire E2, se scelta e preparata prima del corso. Non aggiungerla alle otto ore e non farne un requisito della consegna base.

## Appendice A · OpenCode facoltativo (alternativa a E2)

Solo per gruppi interessati alla modifica del software. Qualificare prima creazione e modifica reali di un file tramite agente; installare OpenCode e verificare backend/permessi. Non basta codice mostrato in chat.

Dalla cartella studente: `unsloth start opencode`. Requisito: modificare `genera_report.py` per aggiungere un filtro inline/offline «Solo da rivedere», che nasconda i casi con doppio OK e mantenga visibile/invariato il riepilogo. Non cambiare CSV o giudizi. Ispezionare `git diff genera_report.py`, rigenerare e verificare nel browser filtro acceso/spento.

Per il collaudo usare una copia tecnica distinta dai risultati AI: doppio OK con risposta dichiarata fixture, una riga ERRORE e una NON_ESEGUITO. Controllare conteggi invariati, riapparizione dei casi e testi HTML mostrati come testo. In caso di modifica non staged errata, `git restore -- genera_report.py` recupera il file tracciato nell'indice; non annulla commit né rimuove file nuovi.

Soluzione docente, dal kit completo:

```bash
python laboratorio/docente/genera_report_soluzione.py --input ../officina-collaudo/risultati.csv --output ../officina-collaudo/report_soluzione.html
```

Un eventuale server LAN dedicato all'agente usa una porta distinta da Studio. Esempio da adattare al modello già qualificato:

```bash
unsloth run --model unsloth/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M -H 0.0.0.0 -p 8889 --disable-tools
```

Configurare realmente provider OpenAI-compatible, URL `http://IP_DOCENTE:8889/v1`, modello e chiave generata in Settings → API. `--disable-tools` riguarda questo backend, non la chat RAG. Il comando locale non seleziona da solo il server. Limitare accesso alla LAN, misurare concorrenza, revocare chiavi a fine corso e non tracciarle. Eventuale cloud: solo dati sintetici, quote e crediti verificati; non è un fallback RAG.

## Appendice B · Confronto modelli facoltativo (alternativa a E2)

Due configurazioni già pronte, stesso prompt con dati forniti, stesse istruzioni e carico comparabile. Annotare fedeltà, tempo e RAM osservati; token/s solo se disponibili. Per isolare la quantizzazione mantenere stesso modello e revisione. Se cambia famiglia/taglia, è un confronto di sistemi, non una prova causale sulla quantizzazione. Nessun vincitore prestabilito né promessa teorica sulle VM.

## Fonti e compatibilità

- [Studio Chat](https://unsloth.ai/docs/new/studio/chat)
- [Changelog](https://unsloth.ai/docs/new/changelog)
- [Configurazione RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/config.py)
- [Store RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/store.py)
- [API](https://unsloth.ai/docs/basics/api) e [OpenCode facoltativo](https://unsloth.ai/docs/integrations/opencode)

I sorgenti `main` e i menu cambiano: conservare versione, schermate e prove della release effettivamente congelata.
