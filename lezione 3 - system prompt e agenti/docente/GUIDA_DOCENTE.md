# Guida docente — L'assistente di reparto della P03

**ITS MAKER Bologna · Lezione 3 · 4 novembre 2026 · Microsoft Copilot Basic**

Documento riservato al docente: regia, preparazione, riscontri e limiti delle prove. Agli studenti si distribuiscono soltanto i materiali della cartella `studenti/` e le slide.

## 1. Scopo e decisione operativa

Le coppie trasformano il lavoro P03 precedente in un assistente di reparto realizzato con Microsoft Copilot: consultare tre documenti, chiedere un chiarimento quando serve e verificare con Python una richiesta di materiale. «Assistente di reparto» è il nome del lavoro svolto con Copilot, non una funzione aggiuntiva o un altro programma da costruire.

Teams distribuisce i documenti. Copilot riceve il file completo come allegato nel formato collaudato, oppure come testo integrale se questa è la scelta del docente. Ogni conversazione nuova deve ricevere di nuovo i documenti. Se si usa una normale chat, vanno inviate di nuovo anche le istruzioni iniziali. I Blocchi appunti non trasferiscono automaticamente i documenti all'agente.

La data della situazione di magazzino è **19 ottobre 2026, ore 08:00**, non il giorno della lezione. Non si rifà la tabella dei 24 appunti e non si insegna a intervenire sulla pressa.

## 2. Che cosa è osservato e che cosa resta da provare

Nella prova preparatoria il docente ha osservato nel proprio agente l'esecuzione di Python e la produzione di `prova_python.csv` scaricabile. Questo non dimostra ancora la lettura degli allegati, l'uso della nuova raccolta di documenti, l'accesso ai Blocchi appunti o la disponibilità sulle postazioni degli studenti.

Prima dell'aula usare un vero account studente. Non attivare acquisti o fatturazione a consumo. Registrare data, formato, richiesta, risposta e comportamento effettivamente osservato.

| Verifica pre-aula | Che cosa controllare | Esito e data |
| --- | --- | --- |
| Apertura dell'agente o ambiente indicato | Accesso senza acquisti; possibilità di salvare le proprie istruzioni | |
| Lettura dei documenti forniti | Codici, quantità e date ricavati dal file, non suggeriti nella domanda | |
| Python nello stesso ambiente | Dettagli che mostrino il calcolo eseguito, i numeri usati e il risultato | |
| Salvataggio del risultato | File realmente scaricabile, aperto e confrontato con i dati originali | |
| Copilot Blocchi appunti | Apertura, aggiunta del fascicolo e richiesta verificata sulle fonti | |
| Nuova conversazione | Fonti fornite di nuovo e prova che non dipende dalla risposta precedente | |
| Teams e postazioni | Scaricamento dei materiali e consegna della scheda e dei file | |

Prima delle prove, mostrare dove leggere i dettagli del calcolo nell'interfaccia disponibile, senza fornire una richiesta già risolta. Se non permettono di verificare l'esecuzione, registrare il limite: un blocco di codice scritto in chat non basta. Non chiedere screenshot come condizione di consegna; basta descrivere ciò che è stato effettivamente osservato.

## 3. Materiali e distribuzione

Distribuire tramite Teams:

- `studenti/ATTIVITA_LEZIONE3.docx`, da compilare; il PDF è la copia stampabile.
- `studenti/01_DOCUMENTI_P03.txt`, raccolta completa dei tre documenti, con equivalenti Word e PDF.
- Le slide `Lezione3_Assistente_Reparto_P03_ITS_MAKER.pptx`, oppure HTML autosufficiente o PDF.

Scegliere prima dell'aula un solo formato effettivamente accettato da Copilot. Non far allegare tutte le versioni della stessa raccolta. Il `.txt` è testo semplice; il `.csv` prodotto dal calcolo è una tabella apribile in Excel o LibreOffice Calc. La scheda `ATTIVITA_LEZIONE3.docx` si compila in Word o LibreOffice Writer, non nella chat.

La raccolta contiene il diario originale completo, il catalogo DOC-RICAMBI rev2 e la situazione DOC-MAG-20261019 rev1. I file di partenza sono in `docente/fonti/`.

## 4. Regia basata sul lavoro delle coppie

### Avvio e scelta del collega

Spiegare che l'assistente è Copilot con le istruzioni progettate dagli studenti. Presentare che cosa deve fare e che cosa non deve fare, poi far aprire i materiali. Le slide sono appoggi durante il lavoro, non un blocco di spiegazione frontale iniziale. La coppia sceglie chi userà l'assistente e quale risposta gli sarà utile. Nessun acquisto, prelievo o aggiornamento reale viene eseguito.

Una persona usa il computer; l'altra legge le fonti e registra le scelte. Invertire i compiti nella progettazione e nelle prove. Se il file precedente delle istruzioni manca, farlo ricostruire dalla coppia a partire dal proprio progetto: non distribuire un nuovo testo risolto.

### Studio delle fonti

Far scegliere un fatto da individuare a mano prima dell'uso di Copilot. Se disponibili, far aprire ora i Blocchi appunti, aggiungere i documenti e formulare richieste proprie. Altrimenti usare lettura diretta. Le coppie compilano subito entrambe le tabelle della sezione 2 della scheda, mentre stanno controllando i documenti; solo dopo passano alle istruzioni. Non far compilare tutta la tabella automaticamente dal modello.

Domande del docente alla coppia: quale passaggio sostiene questa frase? A quale data vale? Quale conclusione ulteriore non è documentata? Non suggerire una frase da copiare nel programma e non assegnare un altro riassunto del fermo.

### Revisione delle istruzioni

La scheda distingue regola conservata, cambiata/eliminata e nuova se necessaria. Una vecchia restrizione al solo diario o la risposta obbligatoria nella tabella dei 24 eventi possono impedire il nuovo servizio: la coppia deve motivare la propria scelta, non riscrivere tutto per obbligo.

I vincoli del compito sono criteri di qualità, non un prompt già formulato. Le coppie decidono come trattare richieste complete e incomplete e come spiegare il risultato. Non possono invece cambiare i fatti delle fonti. Se il codice identifica già l'articolo, una domanda sulla macchina può essere superflua; se lo scopo è scegliere un codice da catalogo, l'identità della macchina può essere decisiva.

Se si usa l'agente, il testo va nel campo delle istruzioni realmente disponibile. Se si usa una normale chat, il primo messaggio contiene istruzioni dell'utente: non chiamarlo vero messaggio di sistema e non dichiarare creato un agente configurato.

### Fonte e calcolo nella stessa prova

La coppia inventa una richiesta che richieda il collegamento fra catalogo e magazzino. Prima dell'invio scrive nella scheda i dati scelti, la loro provenienza e il risultato atteso. Fa eseguire il calcolo con Python e salva il file con la tabella dei risultati. Non consegnare codice o richieste complete: gli studenti scrivono le proprie istruzioni.

Il valore di Python non è rendere difficile una sottrazione. Si osserva il passaggio da interpretazione dei documenti a esecuzione di uno strumento. Il programma esegue il codice, ma lo script può applicare una regola sbagliata o usare valori sbagliati: non presentarlo come infallibile.

Far distinguere tre controlli: documento e data; numeri usati e significato delle quantità; operazione eseguita e risultato. Una differenza negativa indica quanto la richiesta supererebbe il saldo documentato. Non è una nuova quantità reale in magazzino, perché nessun prelievo è avvenuto.

### Prova dei compagni e revisione

Ogni coppia deve provare l'assistente altrui e ricevere una prova sul proprio. La coppia B inventa la richiesta e annota prima dell'invio il risultato atteso e i documenti da controllare. Non inserisce la soluzione nella domanda a Copilot.

La coppia A apre una conversazione nuova, fornisce i documenti e, se usa una chat normale, invia anche le proprie istruzioni. B usa il computer di A senza cambiare account: una persona invia la richiesta, l'altra controlla e compila la scheda di A. A osserva senza suggerire risposte. Poi si invertono i ruoli. Nessuno scambio di credenziali o modifica delle istruzioni altrui.

Proporre tipi di verifica, non frasi pronte: uso di più documenti; evento e documento successivo; richiesta incompleta; dato non documentato. Se si toglie un dato per provare le domande di chiarimento, deve essere davvero necessario.

La coppia che ha creato l'assistente spiega che cosa conserva o cambia. Se la prima risposta è corretta, prova un altro tipo di richiesta senza inventare errori. Se cambia una regola, ne scrive una valida anche per altre richieste e riprova con una conversazione nuova, fornendo di nuovo documenti e istruzioni necessarie.

### Restituzione individuale

Ogni studente, senza Copilot, collega una frase al passaggio e alla data che la confermano, spiega i numeri usati nel calcolo e una decisione rimasta alla persona, motiva una regola conservata o cambiata. Non proclamare vincitore il modello con meno errori: valutare le scelte e i controlli degli studenti.

## 5. Riscontri riservati sulle fonti

| Fonte | Fatti da controllare | Limite |
| --- | --- | --- |
| Diario P03, 13–15/10/2026 | FLT-992 montato il 14/10; sostituzione completata alle 14:42; prove alle 14:52; produzione ripresa alle 15:05 | Non certifica stato reale attuale, nome del tecnico o prezzo |
| DOC-RICAMBI, rev2, 18/10/2026 | P03 associata a FLT-993; P30 a FLT-229 | Non riscrive l'evento del 14/10 e non autorizza un montaggio |
| DOC-MAG-20261019, rev1, 19/10 ore 08:00 | FLT-992: 5; FLT-993: 8; FLT-229: 4 pezzi | Non è disponibilità in tempo reale e non prova che cosa sia montato |

Il fermo dura 45 minuti, dalle 14:20 alle 15:05. Alle 14:42 la macchina è ancora ferma, alle 14:52 è in prova. I 2.480 del contatore sono pezzi prodotti, non cicli di manutenzione.

Le registrazioni di magazzino e le quantità sono nuovi dati sintetici del documento preparato per questa lezione. L'uscita del 14/10 e gli altri movimenti sono già compresi nei saldi: non vanno applicati una seconda volta.

Una richiesta esplicita sul codice FLT-992 può ricevere una verifica di disponibilità. Non va bloccata soltanto perché il catalogo successivo associa P03 a un altro codice. Resta distinta l'eventuale domanda di autorizzazione tecnica, fuori dal servizio.

## 6. Esempi numerici per il docente, non da assegnare come frasi di prova

Le quantità richieste qui sotto sono ipotesi di controllo, non movimenti della fonte. Le coppie inventano i propri casi.

| Oggetto della verifica | Disponibilità documentata | Richiesta ipotetica | Differenza | Interpretazione |
| --- | --- | --- | --- | --- |
| Codice a catalogo per P03 | 8 | 3 | 5 | Richiesta coperta nella situazione datata |
| Codice a catalogo per P03 | 8 | 10 | -2 | Carenza teorica di 2 pezzi |
| Codice esplicito FLT-992 | 5 | 2 | 3 | Verifica lecita del codice storico, senza autorizzazione tecnica |
| Codice a catalogo per P30 | 4 | 6 | -2 | Carenza teorica di 2 pezzi |

Se la quantità richiesta coincide con la disponibilità documentata, la differenza è zero: la richiesta è esattamente coperta, non c'è carenza.

Una proposta documentata resta `PROPOSTA DA CONTROLLARE`. Una carenza, un dato indispensabile non documentato o una richiesta di autorizzazione non supportata richiedono `SERVE UN CONTROLLO`. Non usare le etichette come se fossero comandi collegati a un gestionale.

## 7. Ostacoli e limiti da registrare

| Situazione osservata | Prosecuzione possibile | Limite da dichiarare |
| --- | --- | --- |
| Blocchi appunti non disponibili | Lettura diretta e mappa delle fonti | Non è stata esercitata quella funzione |
| Formato allegato non accettato | Altro formato già collaudato o testo completo fornito nella conversazione | Prova su testo fornito, non su allegato |
| Agente configurabile non disponibile | Normale conversazione con istruzioni proprie nel primo messaggio | Non è stato creato o modificato un agente configurato |
| Python non disponibile o esecuzione non osservabile | Progetto, controlli manuali e confronto con una dimostrazione realmente svolta | Non certificare esecuzione autonoma di Python |
| File non scaricabile | Registrare la risposta reale e il problema, senza inventare un file | Tabella dei risultati non consegnata |
| Risposta subito corretta | Spiegazione della regola conservata e prova di un'altra richiesta | Nessuna correzione artificiale |

Riutilizzare le modalità del corso: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`. Sono provenienze della prova, non giudizi di correttezza. Non attribuire automaticamente un errore a recupero interno, istruzioni o piattaforma se il passaggio non è osservabile.

## 8. Valutazione e consegna

Valutare comprensione dei documenti, progetto dell'assistente, qualità delle richieste inventate, controlli e correzioni spiegati, contributo individuale. Non valutare velocità, estetica della tabella, quantità di codice o percentuale di risposte corrette del modello.

Consegna minima su Teams: scheda compilata, `istruzioni_assistente_P03.txt`, file con la tabella prodotta da Python. La scheda raccoglie controlli sui documenti, prova propria, prova dei compagni, decisione sulle istruzioni e risposte individuali. Niente screenshot obbligatori o esportazioni automatiche presunte.

## 9. Rigenerazione e riferimenti

`genera_materiali.py` genera presentazione, HTML autosufficiente, PDF e documenti Word dalle fonti testuali della lezione. Il modello PowerPoint ripulito conserva l'identità grafica ufficiale ITS MAKER 16:10. Non distribuire il generatore o questa guida come scheda studenti.

- [Microsoft — Interprete di codice per gli agenti](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter).
- [Microsoft — Licenze di Copilot Blocchi appunti](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-licensing).

La documentazione descrive capacità del prodotto; non sostituisce il collaudo dell'account scolastico.
