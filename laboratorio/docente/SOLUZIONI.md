# Guida docente: preparazione, soluzioni e collaudo

Materiale docente, da non importare nel RAG. Il repository è pubblico: la separazione delle cartelle evita la copia accidentale nello starter, non è un controllo di accesso. Distribuire agli studenti soltanto la cartella prodotta da `prepara_laboratorio.py`, non questo file né la revisione 2 prima della prova.

## 1. Cosa viene consegnato e cosa richiede un collaudo d'aula

Il kit comprende cinque documenti sintetici, sei domande, CSV iniziale NON_ESEGUITO, report Python funzionante e soluzione del filtro. Non comprende pesi LLM o embedding, né certifica un numero di richieste simultanee. Il docente prepara e congela l'ambiente prima della lezione; nessuna installazione è richiesta agli studenti.

La verifica locale della CLI Unsloth 2026.10.6 conferma la presenza dei comandi, non certifica inferenza, indicizzazione o funzionamento su VMware. Non interpretare questa versione come release RAG già qualificata per la scuola.

### Sequenza di preparazione nella root del repository

```text
python laboratorio/preflight.py --output ambiente.json
python laboratorio/prepara_laboratorio.py --dest ../officina-collaudo
cd ../officina-collaudo
python genera_report.py
```

`preflight.py` non sovrascrive un manifesto esistente: per una nuova rilevazione scegliere un nuovo nome con `--output`. Registra versioni CLI, controlli dei flag e SHA256 del corpus. Non legge credenziali e non modifica configurazioni globali. Il manifest va conservato dal docente fuori dal workspace studente.

Verificare che la destinazione contenga solo `corpus/`, `genera_report.py`, `risultati.csv` e `parametri_cnc.html`. Aprire `report.html`: tutte le prove devono risultare non eseguite. Il report non chiama un modello e non giudica automaticamente le risposte.

## 2. Golden Image e configurazione da congelare

- Scegliere sistema operativo e shell; assicurare `python` 3.10+ nel PATH. Su Linux, se l'interprete si chiama `python3`, predisporre l'alias prima del corso o sostituire coerentemente il comando nelle istruzioni d'aula.
- Installare Git, Unsloth Studio, OpenCode e un editor; annotare versioni effettive di CLI, Studio e runtime. Non aggiornare l'immagine durante la lezione.
- Scegliere un modello instruct che superi le sei prove in italiano con latenza accettabile, documentando anche gli errori. La taglia in parametri non certifica tool calling o correttezza. Eseguire B3 con al massimo due configurazioni; per isolare la quantizzazione usare stessa revisione del modello e stessi prompt, contesto, impostazioni e carico.
- Scaricare prima LLM, tokenizer, runtime e modello di embedding. Il core usa Markdown testuale: OCR, PDF scansiti e modelli multimodali non sono necessari.
- In **Settings → General → Documents & RAG** scegliere un embedding multilingue e verificarne le prescrizioni, ad esempio eventuali prefissi query/documento. La scelta va provata sulle domande italiane e annotata con identificativo e revisione; il predefinito inglese non è una scelta automaticamente adeguata. Se si cambia embedding, reindicizzare i documenti.
- Registrare in una scheda d'ambiente: file GGUF, quantizzazione, SHA256/revisione, embedding, lunghezza contesto, parametri di generazione, numero thread, memoria assegnata e numero postazioni concorrenti. Conservare anche il risultato delle sei prove e il tempo osservato; non riempire la scheda con stime spacciate per misure.

### Avvio RAG senza confondere allegati e recupero

Dalla root del repository, in un terminale dedicato:

```text
python laboratorio/avvia_studio.py --offline
```

Con cartella GGUF preparata dal docente:

```text
python laboratorio/avvia_studio.py --offline --models-dir "PERCORSO_CARTELLA_MODELLI"
```

Sostituire il percorso con una directory reale. Il launcher imposta **solo nel processo figlio** `RAG_THREAD_WHOLE_DOC=0`: è il controllo presente nel sorgente upstream per non inserire integralmente i piccoli allegati della chat. Non modifica le preferenze globali. Con `--offline` imposta anche `HF_HUB_OFFLINE=1` e `TRANSFORMERS_OFFLINE=1`.

Queste variabili non sono un firewall: disattivare web search, provider remoti e connessioni esterne. La compatibilità del controllo RAG dipende dalla release: osservare realmente passaggi selezionati e fonti. Se la release lo ignora o non mostra il recupero, correggere/qualificare l'ambiente prima dell'aula; non dichiarare RAG riuscito solo perché la chat risponde.

### Procedura nativa documentata

1. Aprire `http://localhost:8888`, accedere e caricare il modello locale già disponibile.
2. In una chat pulita aprire **+ → Chat with Files**, poi **Add files to chat with** e scegliere soltanto i cinque `.md` della cartella studente `corpus/`.
3. Attendere il completamento dell'indicizzazione. Questa è una base di conoscenza associata alla chat, salvata dallo store di Studio; non presumere un menu universale per creare una KB nominata o condividerla tra account.
4. Attivare il recupero documentale e osservare i passaggi restituiti o la chiamata `search_knowledge_base`, quindi aprire le fonti. Il nome del controllo può cambiare: conservare schermate e percorso effettivo della release qualificata.
5. Inviare il prompt della dispensa e le domande. Non abilitare esecuzione terminale o altri strumenti non necessari per consultare il corpus.
6. Per una conversazione nuova riassociare il corpus corrente: non assumere che i documenti di un'altra chat siano già disponibili.

La ricerca nativa combina testo e vettori nello store SQLite (FTS5 e sqlite-vec). È sufficiente per il laboratorio: nessun server vettoriale esterno. Un embedding restituisce candidati simili, non prove di verità.

## 3. Sei casi di collaudo iniziali: chiave docente

Non precompilare il CSV studente con questi esiti: l'osservazione potrebbe essere diversa. Tutte le citazioni vanno aperte e controllate, non soltanto contate.

| ID | Risposta sostenuta dal corpus iniziale | Fonte e criterio di recupero |
| --- | --- | --- |
| T01 | Nel catalogo corrente iniziale P03 è associata a FLT-992. | DOC-RICAMBI rev1, sezione Associazioni macchina-filtro. Non basta citare il rapporto storico. |
| T02 | Il superamento è 13 °C: 78 − 65. | DOC-FERMO, Nota dell'operatore; verificare il calcolo indipendentemente. |
| T03 | Sono stati consegnati 45 cuscinetti SKF-6204, non 50. | DOC-BOLLA, Messaggio del fornitore o Riepilogo verificabile; distinguere ordine e consegna. |
| T04 | L'indisponibilità della P03 nell'evento è durata 45 minuti. | DOC-FERMO, Durata dell'evento. La domanda è una parafrasi di fermo macchina. |
| T05 | La coppia di serraggio non è disponibile nel corpus. Non inventare un valore o una procedura. | Nessuna fonte contiene il dato. Passaggi su bulloni o P03 possono essere recuperati ma non rispondono alla domanda. Nessuna citazione fabbricata. |
| T06 | La soglia didattica della P03 è 65 °C; 55 °C riguarda la P30. | DOC-P03 e DOC-P30, Soglia didattica di temperatura; entrambi gli identificativi devono essere corretti. |

### Giudizi separati

- `esito_recupero=OK`: i passaggi necessari sono disponibili e correttamente identificati. Per T05, OK significa riconoscere che non è stata trovata evidenza pertinente, anche se il motore mostra candidati simili.
- `esito_recupero=ERRORE`: manca una fonte necessaria o si scambia macchina/revisione. Se non si riesce a osservare cosa è stato recuperato, lasciare NON_ESEGUITO e annotare il limite, non inventare un giudizio.
- `esito_risposta=OK`: risposta corretta e sostenuta dalle fonti; per T05 astensione esplicita, senza valori inventati. Un errore di recupero può coesistere con una risposta numericamente corretta ottenuta per caso: registrare entrambi.
- `esito_risposta=ERRORE`: dato, identificativo, calcolo, revisione o citazione sbagliati; anche una risposta sicura su un dato assente è errore.
- `NON_ESEGUITO`: nessuna prova o giudizio ancora disponibile. Non equivale a OK e non equivale a errore osservato.

Registrare risposta effettiva, documento/sezione/revisione, giudizio umano e nota. Usare un editor CSV con separatore `;` e UTF-8; le celle con punto e virgola, virgolette o a capo richiedono la quotatura CSV standard. Non inserire credenziali.

## 4. Aggiornamento controllato della conoscenza

Dopo il collaudo iniziale, il docente consegna `03_catalogo_ricambi_rev2.md`.

1. Salvare il risultato iniziale prima di riprovare: conservare una copia del CSV, senza sovrascrivere l'evidenza rev1.
2. Sostituire nella cartella di lavoro `corpus/03_catalogo_ricambi.md` con il contenuto della revisione 2; non mantenere due cataloghi entrambi correnti.
3. Creare una nuova chat e associarvi i cinque documenti aggiornati, attendendo l'indicizzazione. Se si riusa una KB gestita dalla release, rimuovere anche la vecchia revisione dall'indice: cambiare soltanto il file sul disco non garantisce l'aggiornamento della chat.
4. Ripetere T01: deve risultare FLT-993 con citazione di DOC-RICAMBI rev2.
5. Chiedere quale filtro era stato usato nell'evento storico: DOC-FERMO continua a registrare FLT-992.
6. Spiegare perché il cambiamento riguarda indice e contesto, non i pesi del modello. Se la risposta resta vecchia, ispezionare fonte recuperata, revisione e contesto prima di attribuire il problema al modello.

## 5. OpenCode: filtro piccolo, collaudo reale

Il report base è già funzionante. L'agente modifica `genera_report.py` nella cartella personale, non Unsloth e non i dati osservati. Requisito: aggiungere il selettore **Solo da rivedere**; deve mostrare i casi con almeno uno dei due esiti diverso da OK, lasciando il riepilogo complessivo invariato.

La soluzione docente è eseguibile dal kit completo:

```text
python laboratorio/docente/genera_report_soluzione.py --input ../officina-collaudo/risultati.csv --output ../officina-collaudo/report_soluzione.html
```

Riusa il generatore base e aggiunge un controllo di lettura. Non modifica CSV né esiti. Non copiare la soluzione nel workspace prima che gli studenti abbiano tentato il requisito.

### Prove del filtro

Usare una **copia tecnica** del CSV, distinta dai risultati LLM: predisporre una riga con entrambi gli esiti OK e una risposta di fixture, una con ERRORE e una NON_ESEGUITO. Dichiarare che è una fixture del report, non una prova AI superata.

- Filtro spento: tutte le righe visibili.
- Filtro acceso: la riga con due OK sparisce; una riga con recupero OK e risposta ERRORE resta visibile, così come NON_ESEGUITO.
- Il riepilogo non cambia; disattivando il filtro ricompare tutto.
- Funziona senza rete e il CSV resta identico. Testi come `<script>` devono apparire come testo, non essere eseguiti.

### Backend OpenCode e credenziali

`unsloth start opencode` si collega all'istanza configurata secondo la versione installata. Prima della lezione provare creazione **e modifica** reali di un file; testo di codice in chat non è prova di tool calling riuscito.

Un endpoint docente dedicato a OpenCode può usare una porta distinta dal RAG:

```text
unsloth run --model unsloth/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M -H 0.0.0.0 -p 8889 --disable-tools
```

È un esempio da adattare al modello già scaricato e qualificato, non un requisito universale da 7B. Il flag è una scelta esplicita per evitare esecuzione di tool sul server quando gli strumenti devono agire nel workspace dello studente. Non applicarlo indiscriminatamente alla chat RAG. Configurare il provider OpenAI-compatible di OpenCode con URL `http://IP_DOCENTE:8889/v1` e una chiave reale generata in Settings → API; verificare modello selezionato e richiesta autorizzata. Non salvare chiavi in file tracciati, immagini VM condivise o slide pubbliche. Limitare accesso con firewall alla LAN didattica e revocare le chiavi al termine.

Il server condiviso può accodare richieste; verificarlo con il carico delle 10–12 coppie reali. Non confondere connettività LAN con capacità di generazione. Se si usa cloud, soltanto dati sintetici, quote e crediti verificati; nessun free tier garantisce la lezione.

## 6. Rubrica osservabile e decisione di erogazione

| Criterio | Evidenza richiesta |
| --- | --- |
| Comprensione | Lo studente distingue token/contesto/pesi, inferenza/addestramento, modello/UI/agente. |
| Recupero | Sa aprire le fonti, distinguere P03/P30 e identificare la revisione corrente. |
| Generazione | Verifica numeri, calcolo e citazioni; riconosce il dato assente senza inventare una misura. |
| Metodo | Registra ciò che ha osservato, separa recupero/risposta e conserva i risultati prima/dopo aggiornamento. |
| Autonomia | Formula un requisito proprio e un test negativo; giustifica una modifica invece di limitarsi a incollare prompt. |
| Tracciabilità | Usa diff e checkpoint prima della modifica; spiega il perimetro del ripristino senza comandi distruttivi. |

Un numero di commit non sostituisce queste evidenze. Un errore del modello correttamente individuato è un buon risultato didattico; non correggere i dati per far risultare la prova superata.

**GO** solo dopo avvio offline completo, indicizzazione e recupero osservati, prova dei sei casi, test del report e di OpenCode e carico concorrente accettabile misurato sull'aula. Il preflight CLI da solo non è GO. Se una dipendenza manca, risolverla prima di distribuire la Golden Image; non spacciare allegati interi, risposte preparate o copia-incolla del codice per il laboratorio dichiarato.

## Fonti e compatibilità

- [Studio Chat](https://unsloth.ai/docs/new/studio/chat) e [workflow Chat with Files / Documents & RAG](https://unsloth.ai/docs/models/embeddinggemma-2): interfaccia documentata; non occorre usare il modello grande della pagina per il corso.
- [Changelog](https://unsloth.ai/docs/new/changelog): introduzione sperimentale e cambiamenti di release.
- [Configurazione RAG](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/config.py): controllo whole-document e embedding predefinito; `main` è mobile, verificare il sorgente della release congelata.
- [Store](https://github.com/unslothai/unsloth/blob/main/studio/backend/core/rag/store.py): SQLite, FTS5 e sqlite-vec.
- [API](https://unsloth.ai/docs/basics/api), [OpenCode](https://unsloth.ai/docs/integrations/opencode), [quote cloud](https://openrouter.ai/pricing).
