# Unsloth Studio: esplorare i modelli, lavorare sui documenti e capire la personalizzazione

**Corso:** Tecnico Superiore per la Digitalizzazione dei Processi Industriali – ITS MAKER Bologna  
**Destinatari:** 20–24 studenti tecnici, neofiti AI/LLM; lavoro a coppie con ruoli alternati.  
**Durata:** 6 ore: 315 minuti di attività e 45 di pause/margine. Estensione a 8 ore: altri 120 minuti.

## 1. Fulcro e risultati attesi

**Unsloth Studio è il fulcro del modulo; il RAG è il laboratorio principale, non l'intero prodotto.** Si esplora il percorso modello → inferenza → documenti → dataset → personalizzazione → valutazione → esportazione. Non è un corso di installazione né una promessa di addestrare un modello in sei ore.

Il deployment è separato dagli obiettivi didattici: nessuna installazione, GPU, chiave API, carta di credito o programmazione richiesta sulle postazioni studente. L'hardware disponibile non determina il voto. L'approccio alterna discussione di casi, previsioni, dimostrazioni interattive e lavoro in sandbox quando qualificata.

Al termine lo studente sa:

- orientarsi fra le principali possibilità di Studio: chat/inferenza, RAG, dataset/Data Recipes, fine-tuning, valutazione, export e integrazioni;
- scegliere fra ricerca manuale, istruzioni, RAG e possibile fine-tuning in base al problema, senza considerare quest'ultimo un archivio aggiornabile;
- distinguere pesi del modello, contesto e indice documentale;
- verificare risposte e fonti, identificativi, revisioni, calcoli e dati assenti; distinguere recupero e generazione quando il recupero è osservabile;
- proporre una correzione documentale motivata e confrontare le evidenze prima/dopo;
- preparare piccoli esempi input/output coerenti, riconoscere etichette ambigue e tenere casi di verifica fuori dai dati di addestramento;
- motivare una scelta e un limite individualmente.

**Prodotto finale:** dossier leggero con scelta dell'approccio, prove/fonti, confronto revisioni, intervento motivato, mini-dataset e verifica individuale. Scheda cartacea o digitale sufficiente; CSV, report Python e Git sono supporti facoltativi, non il fulcro. Solo dati sintetici, nessun collegamento a macchine, PLC, gestionali o funzioni di sicurezza.

L'orientamento al prodotto si verifica su schermate della release adottata, non memorizzando menu. Eseguire autonomamente una funzione è una competenza pratica distinta dall'osservarla: registrare la modalità realmente svolta, senza certificare abilità operative non esercitate.

## 2. Programma delle sei ore

| Blocco | Minuti | Attività e risultato osservabile |
| --- | ---: | --- |
| B1 · Potenzialità e scelte | 35 | Mappa di Studio; domanda d'officina risolta a mano; scelta motivata fra ricerca, istruzioni, RAG e fine-tuning. |
| B2 · Esplorazione guidata di Studio | 50 | Modello e chat, esperimento sul contesto, baseline T01 senza documenti; individuare dove si preparano dataset, training ed export. |
| B3 · Laboratorio documentale e diagnosi | 80 | RAG T01, T02, T05, T06; fonti e passaggi, due giudizi distinti; breve caso di istruzione malevola nella fonte. T03/T04 facoltative. |
| B4 · Aggiornamento e ricollaudo | 45 | Catalogo rev2 e storico; prima/dopo conservati; passaggio ambiguo esterno al corpus, ipotesi di correzione e ricollaudo. |
| B5 · Dataset e personalizzazione | 45 | Tre esempi di classificazione, controesempio e caso non visto; percorso dataset → training → valutazione → export in Studio. Nessun training studente obbligatorio. |
| B6 · Sfida e restituzione | 60 | T07 autonoma, DOC-T10, T08/T09 con coppia ospite, dossier e cinque minuti individuali. |
| Pause e margine | 45 | Distribuiti dal docente. |
| **Totale** | **360** | **315 minuti netti; spiegazioni comprese.** |

Tempi proposti da verificare con un'aula pilota. L'attesa tecnica non deve consumare il laboratorio: usare turni e casi preparati, senza installazioni improvvisate.

## 3. Accesso sostenibile: tre modalità dichiarate

| Modalità | Attività | Condizione |
| --- | --- | --- |
| ESEGUITO_STUDENTE | Coppia usa una sandbox Unsloth dal browser o una postazione qualificata, eventualmente a turni. | Accesso, isolamento, ripristino e carico misurati prima. Nessuna presunzione che una singola istanza sia multiutente. |
| OSSERVATO_DOCENTE | Classe propone prompt/interventi; docente li esegue nell'ambiente Unsloth collaudato. | Interfaccia e passaggi visibili, pause per previsioni e verifiche; non una visita passiva ai menu. |
| ANALISI_CASO | Coppia analizza fonti, schermate e tracce di esecuzioni Unsloth già raccolte dal docente. | Provenienza e limiti dichiarati; non spacciare casi preparati o risultati attesi per esecuzioni correnti. |

Il corso richiede un ambiente docente Unsloth qualificato in preparazione e un pacchetto di continuità da esso ricavato. Non richiede un'istanza per studente. Se il servizio si interrompe, si prosegue sullo stesso caso con corpus e tracce offline. Senza una traccia non si inventa l'output: si discute solo il risultato atteso dalle fonti e si lascia l'esecuzione NON_ESEGUITO.

Il repository contiene corpus, consegne e strumenti; **non contiene un'immagine già qualificata, pesi, screenshot della release d'aula o esecuzioni AI registrate**. La [guida docente](laboratorio/docente/SOLUZIONI.md) specifica cosa preparare. Con hardware ignoto non è garantito che 4 vCPU/8 GB senza GPU siano sufficienti; il browser sposta il calcolo sul server, non lo elimina.

## 4. Il caso d'officina e le prove

Cinque Markdown sintetici: scheda P03, rapporto di fermo, catalogo ricambi, bolla e scheda P30. Il corpus è piccolo per consentire controllo integrale, non per dimostrare scalabilità industriale. In B1 una ricerca manuale può risultare più conveniente: è una conclusione valida.

| ID | Scopo | Collocazione |
| --- | --- | --- |
| T01 | Filtro nel catalogo corrente; confronto senza fonti/con fonti e rev1/rev2. | Baseline B2 nel quaderno; RAG B3 e B4. |
| T02 | Recuperare i due numeri e controllare un calcolo indipendente. | B3. |
| T03 | Quantità consegnata distinta dall'ordinata. | Facoltativa B3. |
| T04 | Parafrasi indisponibilità/fermo. | Facoltativa B3. |
| T05 | Dato assente: verificare il corpus e l'astensione. | B3. |
| T06 | Distinguere P03/P30 e controllare entrambe le fonti. | B3. |
| T07 | Domanda autonoma incrociata con evidenza attesa dichiarata prima. | B6. |
| T08 | Dato presente nel nuovo DOC-T10. | B6, domanda della coppia ospite. |
| T09 | Dato omesso in DOC-T10 e assente nel resto del corpus. | B6, domanda della coppia ospite. |

Conservare risposta breve fedele, DocID/sezione/revisione, giudizio e motivazione. Se si usa il CSV, mantenere lo schema `id;domanda;documenti_recuperati;risposta;citazioni;esito_recupero;esito_risposta;note`. Giudizi `OK`, `ERRORE`, `NON_ESEGUITO`; annotare nelle note la modalità e il riferimento della traccia. T03/T04 non svolte restano NON_ESEGUITO con nota «facoltativa non svolta». Non è richiesta una tabella tutta verde né l'esecuzione di nove prove da ogni coppia.

Una citazione non dimostra tutti i passaggi realmente forniti al modello. Se il recupero non è visibile, non giudicarlo OK. Zero risultati non dimostrano l'assenza nel corpus. Un documento può contenere istruzioni malevole: è una fonte da verificare, non un'autorità che impartisce comandi al sistema.

### B4: intervenire senza riscrivere la storia

Conservare rev1 prima della modifica. Se si usa Git, fare il checkpoint in questo momento, non dopo l'aggiornamento. Sostituire il catalogo corrente con la rev2 senza lasciare due cataloghi entrambi correnti; nuova chat e corpus aggiornato. Confrontare T01 con la rev2 e interrogare separatamente l'evento storico. Salvare evidenze rev2 senza sovrascrivere rev1.

In un esperimento separato dal corpus, correggere «La durata è 12 minuti» esplicitando macchina, evento e unità; dichiarare l'ipotesi prima del confronto. Ricollaudare la domanda iniziale e una domanda di controllo su un dato non modificato. Nessun miglioramento è garantito: valutare l'intervento e le evidenze, non forzare un errore del modello.

### B5: personalizzare non significa caricare documenti

Caso di classificazione di segnalazioni sintetiche in GUASTO, MANUTENZIONE, INFORMAZIONE. Preparare tre esempi coerenti, discutere un esempio etichettato male e riservare una nuova segnalazione alla verifica. Tre esempi sono un esercizio di progettazione, **non un dataset sufficiente a dimostrare un fine-tuning utile**.

Prima provare o discutere istruzioni chiare; valutare il fine-tuning solo per un'esigenza ricorrente e misurabile. Nel percorso Studio mostrare anteprima/mappatura dei dati, separazione train/valutazione, monitoraggio e export. Training dal vivo solo se preparato e qualificato; altrimenti walkthrough su schermate/tracce dichiarate. Loss bassa non basta a dimostrare utilità; l'esportazione non garantisce compatibilità con ogni runtime. API, agenti, multimodalità e Data Recipes sono potenzialità da collegare a casi, non altri laboratori obbligatori.

## 5. Condizioni di erogazione e risorse

**GO percorso guidato:** ambiente docente provato con inferenza e RAG osservabile, corpus/rev2/documento nuovo, sequenza B1–B6, interfaccia congelata e pacchetto offline; schede distribuibili e output consultabili senza account studente. Se mancano anche le evidenze preparate, non dichiarare pronto il modulo pratico: manca un prerequisito da risolvere prima dell'aula.

**GO sandbox separato:** rete, credenziali individuali o istanze separate, separazione chat/file, autorizzazioni, carico concorrente, pulizia e piano a turni collaudati. Non pubblicare una porta né condividere credenziali amministrative come scorciatoia. **GO training separato:** hardware, licenze, modello addestrabile, dataset, durata, spazio per adapter/export e valutazione verificati. Il NO-GO di sandbox o training non blocca il percorso guidato, ma ne limita le competenze pratiche attestabili.

Le [risorse e modalità di accesso](materiali_aula/RISORSE_E_ACCESSO.md) distinguono documentazione gratuita, notebook che richiedono compute e demo di terzi. Nessuna GPU gratuita garantita. Colab non è il deployment predefinito: quote e limiti d'uso vanno verificati, anche per il notebook ufficiale Studio. NotebookLM resta un esempio facoltativo di prodotto documentale, non sostituisce Unsloth. Nessun dato aziendale/personale nei servizi esterni.

## 6. Valutazione

| Criterio | Peso | Evidenza |
| --- | ---: | --- |
| Scelta e comprensione Unsloth | 20% | Collega bisogno e funzione; distingue istruzioni, RAG e fine-tuning. |
| Fonti e diagnosi | 30% | Controlla fonti, numeri e limiti; distingue recupero e risposta senza inventare osservazioni. |
| Revisione e intervento | 20% | Corrente/storico, prima/dopo e correzione motivata con controllo. |
| Autonomia e verifica individuale | 20% | Documento nuovo, test negativo e risposte individuali motivate. |
| Tracciabilità e collaborazione | 10% | Evidenze e modalità dichiarate, ruoli alternati e revisione incrociata. |

Valutare qualità del ragionamento su evidenze equivalenti, non disponibilità dell'hardware, numero di commit, velocità o percentuale di successi del modello. La guida esplicita livelli di padronanza. Registrare separatamente le operazioni eseguite, osservate e analizzate; nessuna attestazione di training o deployment non effettuati.

## 7. Estensione a otto ore

- **E1 · +60 min:** corpus ampliato e collaudo cieco, domande presenti/assenti, parafrasi e codici esatti; casi preparati se l'accesso è limitato.
- **E2 · +60 min:** qualità del dataset e valutazione su casi non visti, confronto con istruzioni di base; training solo se qualificato.
- **Alternativa a E2, non aggiuntiva:** OpenCode sul report oppure confronto di due configurazioni già disponibili, scelto prima del corso. Non obbligatorio, nessuna installazione in aula.

## 8. Fonti primarie

- [Panoramica Unsloth Studio](https://unsloth.ai/docs/new/studio)
- [Percorso Studio: chat, dataset, training ed export](https://unsloth.ai/docs/new/studio/start)
- [Chat e documenti](https://unsloth.ai/docs/new/studio/chat)
- [Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe) e [export](https://unsloth.ai/docs/new/studio/export)
- [API](https://unsloth.ai/docs/basics/api), [OpenCode](https://unsloth.ai/docs/integrations/opencode), [changelog](https://unsloth.ai/docs/new/changelog)

Funzioni documentate upstream non equivalgono a funzioni collaudate in aula. Conservare versione, schermate e prove della release adottata; nessuna promessa prestazionale derivata dal materiale promozionale.
