# Guida docente — Lo sportello della P03

**ITS MAKER Bologna · Lezione 3 · 4 novembre 2026 · Microsoft Copilot Basic**

Documento riservato al docente: regia, preparazione, riscontri e limiti delle prove. Agli studenti si distribuiscono soltanto i materiali della cartella `studenti/` e le slide.

## 1. Scopo e decisione operativa

Le coppie trasformano il lavoro P03 precedente in un servizio per un collega del reparto: consultare tre documenti, chiarire una richiesta quando serve e verificare con Python una richiesta di materiale. La fonte viene fornita nella conversazione. Non si richiedono ricerca sul web, collegamenti a servizi aziendali o conoscenze persistenti su file.

Teams distribuisce i documenti. Copilot riceve il fascicolo completo come allegato nel formato collaudato, oppure come testo integrale se questa è la modalità scelta dal docente. Ogni nuova conversazione deve ricevere nuovamente le fonti. Lo studio nei Blocchi appunti non trasferisce automaticamente il fascicolo all'agente.

La data della situazione di magazzino è **19 ottobre 2026, ore 08:00**, non il giorno della lezione. Non si rifà la tabella dei 24 appunti e non si insegna a intervenire sulla pressa.

## 2. Che cosa è osservato e che cosa resta da provare

L'utente ha già osservato nel proprio agente l'esecuzione di Python e la produzione di `prova_python.csv` scaricabile. Questo non attesta ancora lettura degli allegati, uso del nuovo fascicolo, accesso ai Blocchi appunti o disponibilità su tutte le postazioni studente.

Prima dell'aula usare un vero account studente. Non attivare acquisti o fatturazione a consumo. Registrare data, formato, richiesta, risposta e comportamento effettivamente osservato.

| Verifica pre-aula | Evidenza richiesta | Esito e data |
| --- | --- | --- |
| Apertura dell'agente o ambiente indicato | Accesso senza acquisti; possibilità di salvare le proprie istruzioni | |
| Lettura del fascicolo fornito | Codici, quantità e date ricavati dal file, non suggeriti nella domanda | |
| Python nello stesso ambiente | Traccia osservabile dell'esecuzione, input controllabili e risultato pertinente | |
| Salvataggio del risultato | File realmente scaricabile, aperto e confrontato con i dati originali | |
| Copilot Blocchi appunti | Apertura, aggiunta del fascicolo e richiesta verificata sulle fonti | |
| Nuova conversazione | Fonti fornite di nuovo e prova che non dipende dalla risposta precedente | |
| Teams e postazioni | Scaricamento dei materiali e consegna della scheda e dei file | |

Se l'interfaccia non permette di osservare l'esecuzione, registrare che non è verificabile: un blocco di codice scritto in chat non basta. Non chiedere screenshot come condizione di consegna; una registrazione testuale dell'evidenza osservata è sufficiente.

## 3. Materiali e distribuzione

Distribuire tramite Teams:
- `studenti/ATTIVITA_LEZIONE3.docx`, da compilare; il PDF è la copia stampabile.
- `studenti/01_FONTI_SPORTELLO_P03.txt`, raccolta completa dei tre documenti, con equivalenti Word e PDF.
- Le slide `Lezione3_Sportello_P03_ITS_MAKER.pptx`, oppure HTML autosufficiente o PDF.

Scegliere prima dell'aula un solo formato effettivamente accettato da Copilot. Non far allegare tutte le versioni dello stesso fascicolo. Il `.txt` è testo semplice; il `.csv` prodotto dal calcolo è una tabella apribile in Excel o LibreOffice Calc.

Il fascicolo contiene il diario originale completo, il catalogo DOC-RICAMBI rev2 e la situazione DOC-MAG-20261019 rev1. Le fonti canoniche sono in `docente/fonti/`.

## 4. Regia basata sul lavoro delle coppie

### Avvio e destinatario

Presentare missione e confini, poi far aprire i materiali. Le slide sono appoggi da richiamare durante il lavoro, non un blocco di spiegazione frontale iniziale. La coppia sceglie un destinatario reale del servizio, la risposta utile per lui e un confine operativo. Nessun acquisto, prelievo o aggiornamento reale viene eseguito.

Una persona usa il computer; l'altra legge le fonti e registra le scelte. Invertire i compiti nella progettazione e nelle prove. Se il file precedente delle istruzioni manca, farlo ricostruire dalla coppia a partire dal proprio progetto: non distribuire un nuovo testo risolto.

### Studio delle fonti

Far scegliere un fatto da individuare a mano prima dell'uso di Copilot. Nei Blocchi appunti le coppie formulano richieste proprie per capire come i documenti si completano e controllano le risposte sui testi. La mappa delle evidenze è un ragionamento degli studenti, non una tabella delegata integralmente al modello.

Domande del docente alla coppia: quale passaggio sostiene questa frase? A quale data vale? Quale conclusione ulteriore non è documentata? Non suggerire una frase da copiare nel programma e non assegnare un altro riassunto del fermo.

### Revisione delle istruzioni

La scheda distingue regola conservata, cambiata/eliminata e nuova se necessaria. Una vecchia restrizione al solo diario o la risposta obbligatoria nella tabella dei 24 eventi possono impedire il nuovo servizio: la coppia deve motivare la propria scelta, non riscrivere tutto per obbligo.

I vincoli del compito sono criteri di qualità, non un prompt già formulato. Le coppie decidono come trattare richieste complete e incomplete e come spiegare il risultato. Non possono invece cambiare i fatti delle fonti. Se il codice identifica già l'articolo, una domanda sulla macchina può essere superflua; se lo scopo è scegliere un codice da catalogo, l'identità della macchina può essere decisiva.

Se si usa l'agente, il testo va nel campo delle istruzioni realmente disponibile. Se si usa una normale chat, il primo messaggio contiene istruzioni dell'utente: non chiamarlo vero messaggio di sistema e non dichiarare creato un agente configurato.

### Fonte e calcolo nella stessa prova

La coppia inventa una richiesta che richieda il collegamento fra catalogo e magazzino. Per una verifica numerica usa Python e salva il prospetto effettivamente prodotto. Non consegnare il codice o la richiesta completa: gli studenti devono tradurre il bisogno del destinatario nelle proprie istruzioni.

Il valore di Python non è rendere difficile una sottrazione. Si osserva il passaggio da interpretazione dei documenti a esecuzione di uno strumento. Il programma esegue il codice, ma lo script può applicare una regola sbagliata o usare valori sbagliati: non presentarlo come infallibile.

Far distinguere tre controlli: fonte e data; input e significato dei numeri; operazione eseguita e risultato. Una differenza negativa indica quanto la richiesta supererebbe il saldo documentato. Non è una nuova giacenza reale, perché nessun prelievo è avvenuto.

### Collaudo ospite e revisione

Ogni coppia deve ricevere ed eseguire un collaudo. Gli ospiti inventano una richiesta senza dare prima la risposta attesa. I proprietari aprono una conversazione nuova e forniscono il fascicolo, poi osservano senza guidare la risposta. Non si scambiano credenziali e gli ospiti non modificano le istruzioni del servizio altrui.

Usare famiglie di prove, non frasi pronte: incrocio di fonti; storia e documento successivo; richiesta incompleta; dato non documentato. Possono sovrapporsi. Una variante completa/incompleta è utile solo se il dato tolto modifica davvero la verifica possibile.

Le evidenze ospiti restano nella scheda dei proprietari, con coppia ospite e ruoli. Se la prima risposta è corretta si motiva la regola conservata e si verifica un altro confine: non si inventano errori. Se si modifica, si formula un principio generale e si riprova in una conversazione nuova con le fonti di nuovo presenti.

### Restituzione individuale

Ogni studente, senza Copilot, collega una frase a un passaggio e una data, spiega un input del calcolo e un limite del risultato, motiva una regola conservata o cambiata. Non proclamare vincitore il modello con meno errori: valutare il ragionamento progettuale e la verifica.

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
| File non scaricabile | Registrare la risposta reale e il problema, senza inventare un file | Consegna del prospetto non eseguita |
| Risposta subito corretta | Conferma motivata e prova di un altro confine | Nessuna correzione artificiale |

Riutilizzare le modalità del corso: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`. Sono provenienze della prova, non giudizi di correttezza. Non attribuire automaticamente un errore a recupero interno, istruzioni o piattaforma se il passaggio non è osservabile.

## 8. Valutazione e consegna

Valutare comprensione delle fonti, progetto del servizio, qualità dei casi inventati, controllo e revisione motivati, contributo individuale. Non valutare velocità, estetica del prospetto, quantità di codice o percentuale di risposte corrette del modello.

Consegna minima su Teams: scheda compilata, `istruzioni_sportello_P03.txt`, prospetto effettivo prodotto con Python. La scheda documenta uso delle fonti, prova propria, collaudo ospite, decisione dei proprietari e risposte individuali. Niente screenshot obbligatori o esportazioni automatiche presunte.

## 9. Rigenerazione e riferimenti

`genera_materiali.py` genera presentazione, HTML autosufficiente, PDF e documenti Word dalle fonti testuali della lezione. Il modello PowerPoint ripulito conserva l'identità grafica ufficiale ITS MAKER 16:10. Non distribuire il generatore o questa guida come scheda studenti.

- [Microsoft — Interprete di codice per gli agenti](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter).
- [Microsoft — Licenze di Copilot Blocchi appunti](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-licensing).

La documentazione descrive capacità del prodotto; non sostituisce il collaudo dell'account scolastico.
