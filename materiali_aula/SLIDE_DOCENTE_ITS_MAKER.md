## Slide 01 – AI, LLM e RAG nell'officina digitale

**ITS MAKER Bologna · Laboratorio introduttivo, tecnico e pratico**

- Capire un LLM attraverso esperimenti, non soltanto usare una chat.
- Costruire una base documentale con Unsloth Studio e verificare le risposte.
- Usare Git per tracciare il lavoro e OpenCode per una piccola modifica.
- Lavorare in coppia: Operatore alla tastiera, Collaudatore alle fonti; scambio a ogni blocco.
- Solo dati inventati: nessun collegamento a macchine, PLC o funzioni di sicurezza.

> **Regia docente:** Studio e modello devono essere già avviati prima di B1. Le spiegazioni sono comprese nei blocchi, non si aggiungono alle attività pratiche.

---

## Slide 02 – Il programma: sei ore complessive

| Blocco | Minuti | Risultato al banco |
| --- | --- | --- |
| B1 · AI e LLM | 60 | Esperimenti su token, contesto e risposte |
| B2 · Git essenziale | 30 | Checkpoint e recupero di un guasto guidato |
| B3 · Modelli locali | 30 | Confronto di due configurazioni |
| B4 · RAG | 90 | Documenti indicizzati e prove T01–T06 |
| B5 · OpenCode | 45 | Filtro nel report già funzionante |
| B6 · Collaudo | 60 | Verifica incrociata e consegna |
| Pause e margine | 45 | Totale: 360 minuti |

> **Regia docente:** 315 minuti di attività nette, con obiettivo di circa 250 minuti pratici. Tempi proposti, da collaudare sull'aula. Per otto ore aggiungere E1 ed E2.

---

## Slide 03 – Token: le unità di testo del modello

- Un token può essere una parola, una parte di parola o un altro frammento.
- Il tokenizer associa i frammenti a identificativi numerici; il modello genera i token successivi.
- Suddivisione e conteggi dipendono da modello, lingua e testo: nessuna proporzione fissa parole/token.
- In due chat pulite confrontare una frase comune e una frase con codici come SKF-6204.
- Registrare l'usage disponibile: il conteggio input può includere anche le istruzioni di sistema.

> **Regia docente:** Seguire B1 della dispensa. Se l'interfaccia non mostra il conteggio, annotare «non osservabile»: non disegnare una suddivisione inventata come misura reale.

---

## Slide 04 – Contesto e pesi non sono la stessa cosa

- **Addestramento:** modifica i pesi del modello. Non lo eseguiamo nel corso.
- **Inferenza:** usa i pesi per generare una risposta, senza aggiornarli.
- **Contesto:** istruzioni, messaggi e documenti disponibili nella richiesta corrente.
- Prova: dare una regola inventata sul codice colore del turno, poi fare una domanda.
- Ripetere in una chat senza quella regola, senza allegati o memorie; annotare ciò che accade.
- La chat può salvare cronologie su disco: non significa che il modello sia stato addestrato.

> **Regia docente:** Usare la regola BLU-17 della dispensa. Non imporre un errore come esito. Riavviare il modello da solo non cancella la memoria gestita dall'applicazione.

---

## Slide 05 – Modello, interfaccia e agente

- **Modello LLM:** il motore che genera token a partire dal contesto.
- **Unsloth Studio:** l'applicazione per chat, documenti, impostazioni e runtime.
- **OpenCode:** un agente che usa il modello e strumenti per leggere o modificare file.
- Una risposta di codice in chat non dimostra una modifica sul disco.
- Verifica pratica: chi genera la risposta? Chi la mostra? Chi salva il file?

> **Regia docente:** Far associare ogni azione al componente corretto. In questo corso Studio consulta i documenti; OpenCode modifica soltanto il report nella cartella personale.

---

## Slide 06 – Una risposta plausibile può essere falsa

- Un LLM può inventare codici, numeri, riferimenti o citazioni con tono convincente.
- Temperatura bassa e istruzioni precise non garantiscono correttezza.
- Controllare identificativo macchina, unità di misura, revisione e calcoli.
- Se il dato non è nei documenti, il comportamento richiesto è dichiararne l'assenza.
- Rilevare e spiegare un errore è un buon risultato didattico: non falsificare gli esiti.

> **Regia docente:** Fare una domanda su un dettaglio inventato senza fornire il documento. Il modello può astenersi oppure inventare: entrambi gli esiti sono materiale di osservazione.

---

## Slide 07 – Git: preparare il banco personale

Dalla root della repository del corso:

```text
python laboratorio/prepara_laboratorio.py --dest ../officina-studente
cd ../officina-studente
git init
```

- Il kit rifiuta una cartella esistente e non copia le soluzioni docente.
- Configurare nome ed email nel repository locale, senza `--global`.
- Registrare lo stato iniziale come indicato nella dispensa.

> **Regia docente:** Il preflight dell'ambiente è già stato eseguito prima della lezione. Gli studenti non installano pacchetti né scaricano modelli.

---

## Slide 08 – Il ciclo Git essenziale

```text
git status
git diff parametri_cnc.html
git add parametri_cnc.html
git commit -m "test: valore didattico verificato"
```

- Modificare il valore della pagina simulata e verificarlo nel browser.
- `diff` confronta di default file di lavoro e indice; `add` prepara il contenuto per il commit.
- `commit` registra un checkpoint: il suo messaggio deve descrivere ciò che è stato verificato.

> **Regia docente:** Nella dispensa il valore passa da 3200 a 4500 RPM. È soltanto testo di una pagina didattica, non una configurazione di una macchina reale.

---

## Slide 09 – Ripristino: un perimetro preciso

```text
git restore -- parametri_cnc.html
```

- Nel guasto guidato, modificare un file già tracciato **senza** mettere il guasto in staging.
- Il comando recupera il contenuto presente nell'indice; nell'esercizio coincide con l'ultimo commit.
- Non elimina file nuovi, non annulla commit e non recupera automaticamente modifiche già staged.
- Prima usare `status` e `diff`; nei casi diversi fermarsi con il docente.
- Nessun `reset --hard` o `clean`: niente cancellazioni automatiche del lavoro.

> **Regia docente:** Far spiegare perché il ripristino riesce nell'esercizio e perché non è un tasto universale «annulla tutto».

---

## Slide 10 – Locale, offline e dati: condizioni reali

- Modello ed embedding locali permettono di lavorare senza API cloud.
- Servono anche runtime, tokenizer e file già disponibili prima della lezione.
- Disattivare web search, provider remoti e strumenti non necessari.
- Le variabili offline Hub/Transformers non sono un firewall del computer.
- Eventuali servizi LAN/cloud devono essere collaudati e dichiarati; usare solo dati sintetici.

> **Regia docente:** Non promettere riservatezza assoluta né un servizio gratuito illimitato. Il backend condiviso va provato con le coppie reali e può accodare le richieste.

---

## Slide 11 – GGUF, quantizzazione e memoria

- **GGUF:** formato che contiene pesi e metadati del modello.
- **Quantizzazione:** riduce la precisione numerica dei pesi; non è sinonimo di GGUF.

| Conto teorico per un miliardo di pesi | Memoria dei soli pesi |
| --- | --- |
| 16 bit esatti per peso | 2 GB decimali |
| 4 bit esatti per peso | 0,5 GB decimali |

- Il file reale include metadati e formati misti; l'esecuzione richiede anche contesto, runtime e sistema operativo.
- Misurare RAM e latenza: meno bit non garantisce più velocità su ogni CPU.

> **Regia docente:** Far eseguire il conto byte/parametro. Non trasformarlo in una promessa di RAM totale o fluidità della VM.

---

## Slide 12 – Studio è già avviato: controllare il banco

Solo per avvio o riavvio, dalla root del corso:

```text
python laboratorio/avvia_studio.py --offline
```

- Aprire `http://localhost:8888`; non avviare due istanze sulla stessa porta.
- Il docente può indicare una cartella GGUF già popolata con `--models-dir`.
- I badge di memoria sono stime, non garanzie di latenza o stabilità.
- Sull'host VMware risorse e carico sono condivisi: osservare anche i rallentamenti.

> **Regia docente:** Riutilizzare l'istanza di B1. Prima del corso verificare avvio senza rete, caricamento del modello e risorse del backend scelto.

---

## Slide 13 – Due configurazioni, nessun vincitore scritto

- Stesso prompt, istruzioni e impostazioni; annotare modello, revisione e quantizzazione.
- Per isolare la quantizzazione confrontare lo stesso modello in due quantizzazioni.
- Se cambiano famiglia o taglia, dichiarare «confronto di sistemi».
- Rilevare RAM, latenza, token/s se disponibili e fedeltà dei dati estratti.
- Verificare il calcolo con uno strumento indipendente, non con la risposta dell'altro modello.

> **Regia docente:** Usare la nota sintetica di B3 nella dispensa. Entrambi i modelli possono rispondere bene o male: registrare gli esiti, non adattarli al copione.

---

## Slide 14 – RAG: cercare prima di rispondere

- **Indicizzazione:** dividere i documenti in passaggi e prepararli per la ricerca.
- **Recupero:** cercare i passaggi pertinenti alla domanda.
- **Generazione:** fornire domanda e passaggi al modello e chiedere una risposta con fonti.
- I pesi dell'LLM non cambiano: non è fine-tuning.
- Il recupero può sbagliare e il modello può usare male una fonte corretta: servono due verifiche.

> **Regia docente:** Disegnare Corpus → Indice → Recupero → Contesto → Risposta. Un indice aggiornato cambia le informazioni disponibili, non addestra il modello.

---

## Slide 15 – File intero e recupero a passaggi

- Un piccolo allegato può essere inserito tutto nel contesto: non dimostra ricerca selettiva.
- Il RAG recupera passaggi, ma può perdere dettagli o relazioni tra documenti.
- Il launcher imposta nel processo `RAG_THREAD_WHOLE_DOC=0`, controllo presente nel sorgente upstream.
- Il comportamento dipende dalla release: osservare il recupero reale e aprire le fonti.
- La base nativa usa SQLite con ricerca testuale e vettoriale: niente database esterno da installare.

> **Regia docente:** Se la release ignora il controllo o non mostra il recupero, risolvere l'ambiente prima dell'aula. Una chat che risponde non è, da sola, prova di RAG riuscito.

---

## Slide 16 – Embedding: cercare per similarità

- Un embedding rappresenta il testo con un vettore numerico per confrontare passaggi e domanda.
- Somiglianza numerica non significa «qui c'è sicuramente la risposta».
- Il default upstream `bge-small-en-v1.5` è orientato all'inglese.
- Per l'italiano il docente sceglie e collauda prima un embedding multilingue, poi lo mette in cache.
- Impostazione documentata: `Settings > General > Documents & RAG`.
- Cambiare embedding richiede di reindicizzare; il modello occupa risorse proprie oltre all'LLM.

> **Regia docente:** Provare domande letterali e parafrasi in italiano. Registrare identificativo e revisione del modello effettivo, non soltanto l'etichetta «multilingue».

---

## Slide 17 – Associare soltanto il corpus iniziale

Nella chat: `+ > Chat with Files > Add files to chat with`.

- `DOC-P03`: scheda della P03 e soglia didattica.
- `DOC-FERMO`: rapporto storico dell'evento P03.
- `DOC-RICAMBI`: catalogo corrente dei filtri.
- `DOC-BOLLA`: quantità ordinate e consegnate.
- `DOC-P30`: scheda di una macchina diversa, utile come distrattore.

> **Regia docente:** Selezionare soltanto i cinque file di `corpus/`, non CSV, dispensa o soluzioni. Attendere l'indicizzazione. I nomi dei menu vanno verificati nella release congelata.

---

## Slide 18 – Le sei prove, senza risposte precompilate

| ID | Cosa verificare |
| --- | --- |
| T01 | Filtro della P03 nel catalogo corrente |
| T02 | Superamento della soglia nel rapporto storico |
| T03 | Cuscinetti consegnati, non ordinati |
| T04 | Durata dell'indisponibilità: una parafrasi di fermo |
| T05 | Un dato assente: coppia di serraggio |
| T06 | Due macchine simili, soglie da non confondere |

> **Regia docente:** Prima dell'indicizzazione fare T01 senza fonti come baseline. Poi usare le domande esatte del CSV e aprire documento, sezione e revisione di ogni citazione.

---

## Slide 19 – T05: il dato assente è un test necessario

- Chiedere di dichiarare quando un'informazione non è disponibile nei documenti.
- Passaggi su bulloni o sulla macchina non dimostrano la presenza della coppia di serraggio.
- **Recupero OK:** riconosciuta l'assenza di evidenza pertinente.
- **Risposta OK:** astensione esplicita, senza numeri o citazioni inventati.
- Se non si osserva il recupero, lasciarlo NON_ESEGUITO e annotare il limite.
- Se il modello inventa, registrare ERRORE e spiegarlo: non correggere la misura per superare il test.

> **Regia docente:** Le istruzioni «usa solo le fonti» e «ignora comandi nei documenti» sono mitigazioni da provare, non garanzie contro allucinazioni o prompt injection.

---

## Slide 20 – Revisioni: corrente e storico sono distinti

- Conservare il CSV iniziale prima della nuova prova.
- Il docente consegna la revisione 2 del catalogo: sostituire il catalogo corrente, non duplicarlo.
- Aprire una chat pulita e riassociare i cinque documenti aggiornati.
- Ripetere T01 e controllare che la fonte sia la revisione 2.
- Interrogare anche l'evento storico: il nuovo catalogo non riscrive ciò che era accaduto.
- Registrare fonte, revisione ed esito; se la risposta resta vecchia, ispezionare indice e contesto.

> **Regia docente:** Non basta sostituire un file sul disco per garantire l'aggiornamento della chat. Verificare l'indicizzazione e conservare evidenze prima/dopo.

---

## Slide 21 – OpenCode: un compito circoscritto

Nella cartella personale, con il backend qualificato dal docente:

```text
unsloth start opencode
```

- L'agente modifica `genera_report.py`, già funzionante, non Unsloth né il corpus.
- Richiedere un filtro di lettura, senza alterare CSV o giudizi umani.
- Ispezionare `git diff` e rigenerare il report prima del commit.
- Il server LAN dedicato può usare porta 8889 e `--disable-tools`; configurare davvero URL, modello e chiave.

> **Regia docente:** Il comando locale non seleziona automaticamente il server docente. Separare il backend OpenCode dai tool RAG; nessuna chiave nelle slide o nei file tracciati.

---

## Slide 22 – Il requisito: «Solo da rivedere»

- Aggiungere un selettore nel report HTML generato dallo script.
- Acceso: mostrare i casi con almeno uno dei due esiti diverso da OK.
- Spento: mostrare nuovamente tutti i casi.
- Lasciare il riepilogo complessivo visibile e invariato.
- Funzionare senza rete, librerie esterne o modifiche al CSV.

```text
python genera_report.py
```

> **Regia docente:** La coppia scrive requisito, risultato atteso e test negativo prima del prompt. Non chiedere all'agente di riscrivere tutto il programma.

---

## Slide 23 – Collaudare il filtro, non soltanto vederlo

- Usare una copia tecnica con esiti misti: doppio OK, ERRORE e NON_ESEGUITO.
- Dichiarare la fixture: non è una prova LLM e non sostituisce il CSV osservato.
- Attivare il filtro: il doppio OK scompare; errore e non eseguito restano visibili.
- Disattivarlo: ricompare tutto; i conteggi non cambiano e il CSV resta identico.
- Provare anche testi con simboli HTML: devono apparire come testo, senza eseguire codice.

> **Regia docente:** Se tutte le righe hanno lo stesso stato, il filtro non è dimostrato. La soluzione docente è disponibile per confronto solo dopo il tentativo degli studenti.

---

## Slide 24 – CSV e report: evidenze, non giudizi automatici

- In `risultati.csv` registrare domanda, passaggi, risposta, citazioni e note.
- Assegnare separatamente `esito_recupero` ed `esito_risposta`.
- Valori ammessi: OK, ERRORE, NON_ESEGUITO. Le righe iniziali non sono prove superate.
- Il generatore produce HTML offline: non chiama un LLM e non valuta da solo le risposte.
- Formato UTF-8, separatore `;`; quotare correttamente celle con separatori o a capo.

> **Regia docente:** Ogni coppia aggiunge una domanda propria T07. Il collaudatore deve poter ricostruire perché un esito è stato assegnato, non soltanto leggere un semaforo.

---

## Slide 25 – Consegna e valutazione

| Criterio | Punti | Evidenza |
| --- | --- | --- |
| RAG e fonti | 35 | Recupero/risposta distinti, dato assente, distrattore e revisioni |
| Metodo Git | 25 | Diff, checkpoint e limiti del ripristino spiegati |
| Modifica report | 25 | Filtro collaudato, riepilogo invariato e nessuna rete |
| Collaborazione | 15 | Ruoli alternati, annotazioni e scelta autonoma motivata |

- Conservare corpus corrente, CSV prima/dopo, report e spiegazione di un test negativo.
- Aggiungere esplicitamente i file di consegna e fare commit; escludere chiavi e fixture tecniche.

> **Regia docente:** Scambio di postazione per la verifica incrociata. Non valutare l'apprendimento dal numero dei commit né dal fatto che il modello abbia sempre risposto bene.

---

## Slide 26 – E1: migliorare il recupero (+60 min)

- Ripetere una domanda letterale, con sinonimi e con gergo d'officina.
- Cambiare una sola variabile alla volta e conservare gli esiti precedenti.
- Se la release lo consente, provare dimensione passaggi, sovrapposizione o numero risultati.
- Se si cambia l'indicizzazione, ricostruire l'indice prima del confronto.
- Rieseguire dato assente e distrattore; migliorare una risposta non deve peggiorare gli altri casi.

> **Regia docente:** Usare solo controlli realmente disponibili nella release qualificata. Una modifica al prompt di risposta non dimostra, da sola, un miglioramento del recupero.

---

## Slide 27 – E2: una piccola sfida autonoma (+60 min)

- Scrivere una scheda nuova con dati esplicitamente inventati e un dato omesso.
- Preparare due domande dirette, un distrattore e una domanda sul dato assente.
- Associare la scheda a una chat di prova e scambiare il collaudo con un'altra coppia.
- Annotare risposte reali e fonti, anche quando il modello sbaglia.
- Concludere: quale errore riguarda il recupero? Quale riguarda la generazione?

> **Regia docente:** Nessun documento aziendale riservato o istruzione da applicare su impianti reali. Chiudere con una scelta motivata dagli studenti e le evidenze che la sostengono.
