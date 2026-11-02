# Lezione 3 — Dal diario P03 allo sportello con fonti e calcolo

**Canovaccio docente · ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot Basic**

Questa versione sviluppa la lezione sul caso P03 con documenti distribuiti tramite Teams e forniti alla conversazione. Non richiede recupero autonomo di fonti pubbliche. I materiali operativi sono la scheda studenti, il fascicolo delle fonti, le slide e la guida docente con riscontri riservati.

**Stato delle prove di piattaforma:** l'utente ha osservato esecuzione Python e creazione di un CSV scaricabile nel proprio agente. Lettura del nuovo fascicolo, disponibilità dei Blocchi appunti e comportamento sulle postazioni studente richiedono ancora collaudo con account scolastico. I controlli documentali non equivalgono a prove sul tenant.

## 1. Missione e perimetro

Le coppie riprendono le proprie istruzioni P03 e progettano uno sportello per un collega del reparto: consultare diario, catalogo e situazione di magazzino; distinguere dati storici e datati; verificare una richiesta di materiale con Python; presentare un risultato controllabile.

La situazione di riferimento è il **19 ottobre 2026 alle ore 08:00**. Non è la data reale della lezione e non è un collegamento al magazzino aggiornato.

- Copilot Blocchi appunti: studio e riscontro delle fonti complete, se effettivamente disponibile.
- Agente o conversazione indicata dal docente: comportamento del servizio e uso dello strumento di calcolo.
- Persone: destinatario, perimetro, scrittura delle istruzioni, scelta dei casi e controllo dei risultati.

Non si ricompilano i 24 eventi e non si ripete la conversione del registro. Nessuna manutenzione, istruzione d'intervento sulla pressa, autorizzazione di montaggio, ordine o aggiornamento reale del magazzino. Le etichette `PROPOSTA DA CONTROLLARE` e `SERVE UN CONTROLLO` sono testo, non azioni collegate a un gestionale.

## 2. Risultati da osservare

Ogni studente deve saper:
1. collegare una frase al documento, al passaggio e alla data che la sostengono;
2. distinguere evento storico, catalogo successivo e disponibilità documentata;
3. motivare una regola delle istruzioni conservata, modificata o eliminata;
4. inventare una richiesta pertinente che metta alla prova un confine del servizio senza suggerire la risposta;
5. distinguere dati della fonte, input del calcolo, esecuzione dello strumento e risultato;
6. spiegare una conclusione che i documenti o il calcolo non autorizzano.

## 3. Materiali pronti e modalità di distribuzione

| Materiale | Uso |
| --- | --- |
| Scheda `studenti/ATTIVITA_LEZIONE3` in Word/PDF | Un solo documento di coppia per progetto, evidenze, prove e risposte individuali |
| Fascicolo `studenti/01_FONTI_SPORTELLO_P03` in testo, Word e PDF | Diario completo dei 24 appunti, catalogo rev2 e nuova situazione di magazzino |
| Istruzioni P03 della coppia | Punto di partenza da rivedere, non testo da sostituire con una soluzione pronta |
| Presentazione ufficiale in PowerPoint, HTML e PDF | Appoggio al lavoro delle coppie, non lezione frontale preliminare |
| Guida docente e fonti canoniche in `docente/` | Preparazione, riscontri e rigenerazione; non distribuire come consegna |

Teams serve a distribuire e raccogliere i file. La coppia allega il fascicolo completo nella conversazione. Il formato viene scelto dopo la verifica con account studente; non caricare tutte le versioni insieme.

Ogni nuova conversazione riceve di nuovo il fascicolo. Nessun trasferimento automatico dai Blocchi appunti e nessuna memoria permanente dei file sono presunti. Se si fornisce il testo completo anziché l'allegato, annotare quella modalità: non è una prova di lettura del file.

## 4. Fonti e invarianti del caso

Il diario originale racconta 24 appunti del 13–15 ottobre 2026. La riparazione del 14/10 usa FLT-992; la produzione riprende alle 15:05 dopo il fermo delle 14:20. Il catalogo DOC-RICAMBI rev2 del 18/10 associa P03 a FLT-993 e P30 a FLT-229. La revisione successiva non riscrive l'evento e non dimostra incompatibilità o obblighi di sostituzione.

Il nuovo documento DOC-MAG-20261019 rev1 riporta, al 19/10 ore 08:00, 5 pezzi FLT-992, 8 pezzi FLT-993 e 4 pezzi FLT-229. I movimenti descritti sono già compresi nei saldi. Queste quantità e registrazioni sono nuovi dati sintetici del caso, non informazioni dedotte dal solo diario.

Non introdurre prezzi, soglie di riordino, priorità o regole manutentive. La difficoltà sta nel riconoscere significato e provenienza dei dati, non nel complicare la contabilità.

## 5. Verifiche prima dell'aula

Con account studente provare accesso all'ambiente, lettura del fascicolo, richiesta documentale con dati non suggeriti, Python nella stessa conversazione, osservabilità dell'esecuzione e apertura del risultato scaricato. Provare separatamente i Blocchi appunti. Registrare richiesta, risposta, file/revisione e data senza raccogliere credenziali.

Non presumere funzionalità da un nome di licenza. Nessuna attivazione a pagamento. Un risultato scritto in chat non dimostra esecuzione di Python; uno script eseguito non dimostra input corretti o logica corretta.

Se si usa una normale chat, le istruzioni nel primo messaggio sono istruzioni dell'utente, non veri messaggi di sistema. Distinguere questa modalità dalla modifica di un agente realmente configurato.

## 6. Sequenza operativa

### Avvio e destinatario

Il docente presenta la missione e fa aprire i materiali. La coppia sceglie il destinatario, il risultato utile e un confine. Uno studente usa il computer e l'altro controlla; i compiti si scambiano durante il lavoro.

### Studio delle evidenze

La coppia individua a mano un fatto e poi usa i Blocchi appunti per esplorare relazioni con richieste proprie. Compila la mappa con passaggi, date e limiti. Conserva una richiesta e una risposta reali, verificate. Non delega al modello tutta la mappa e non richiede un nuovo riassunto del diario.

### Progettazione delle istruzioni

Si confrontano regole conservate, cambiate/eliminate e nuove se necessarie. Le istruzioni sono scritte dagli studenti; i fatti restano nelle fonti. Le domande di chiarimento servono solo quando cambia davvero ciò che è possibile verificare, non come passaggio obbligatorio. Una richiesta su un codice esplicito può non richiedere l'identità della macchina.

### Prima prova e uso di Python

In una conversazione nuova, con fascicolo completo, la coppia formula una richiesta propria che richieda l'incrocio tra documenti. Per una prova numerica fa eseguire Python e conserva il risultato realmente prodotto. Prima del confronto annota dati e risultato attesi. Controlla fonte, input, operazione ed esecuzione osservata. Il prospetto è un'ipotesi documentata, non un prelievo effettuato.

### Preparazione del collaudo ospite

Gli studenti inventano casi nelle famiglie: incrocio di fonti; storia e documento successivo; richiesta incompleta; informazione non documentata. Le famiglie possono sovrapporsi. Non ricevono frasi complete da copiare e non devono aspettarsi un errore del modello.

### Scambio e decisione motivata

Ogni coppia ospita e collauda. Il proprietario apre una conversazione nuova e fornisce le fonti; gli ospiti inviano la richiesta e verificano senza ricevere prima la risposta. Le evidenze restano nella scheda dei proprietari, con attribuzione degli ospiti. Nessuno scambio di credenziali o modifica dell'agente altrui.

I proprietari correggono solo se sanno motivare il cambiamento. Se la risposta è corretta conservano la regola e provano un altro confine. Una modifica deve essere generale, non contenere la risposta alla singola domanda; la nuova prova avviene con fonti nuovamente fornite.

### Restituzione individuale

Ogni studente, senza Copilot, spiega una fonte e la sua data, un input del calcolo e un limite del risultato, una scelta sulle istruzioni. La scheda distingue il contributo individuale dal prodotto della coppia.

## 7. Consegna e valutazione

La consegna comprende scheda compilata, `istruzioni_sportello_P03.txt` e prospetto reale prodotto con Python. Le evidenze coprono studio delle fonti, prova propria, collaudo ospite, decisione e contributi individuali. Non duplicare prove che coprono più aspetti.

Valutare comprensione delle fonti, progetto, qualità delle richieste inventate, controllo e revisione motivati, autonomia individuale. Non valutare velocità, grafica, quantità di codice o percentuale di risposte giuste del modello.

Le modalità `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE` e `ANALISI_CASO` indicano provenienza, non correttezza. Non richiedere screenshot, esportazioni automatiche o scrittura di Python come condizione di consegna.

## 8. Ostacoli senza false equivalenze

Se i Blocchi appunti non sono disponibili, usare lettura diretta senza attestare quella competenza. Se il file non è leggibile, usare un formato già provato o testo completo, registrando la modalità. Se l'agente non è configurabile, una chat con istruzioni iniziali non dimostra creazione dell'agente. Se Python non è disponibile o non osservabile, usare soltanto dimostrazioni realmente eseguite o analisi dichiarate: l'obiettivo di esecuzione autonoma non è raggiunto.

Un'astensione deve essere verificata nei documenti. Un errore non permette da solo di diagnosticare un passaggio interno non osservabile. Una prima risposta corretta non richiede né una correzione artificiale né dati più complicati.

## 9. Regole di produzione

Separare studenti e docente. Conservare i 24 appunti, le date e i fatti. Italiano comune, istruzioni concrete e nessuna durata didattica. Presentazione nel modello ITS MAKER ufficiale 16:10, con testi e tabelle modificabili e HTML coerente. Aggiornare tutti i formati interessati senza modificare altre lezioni. Verificare documenti e presentazioni nei programmi reali e distinguere tale controllo dal collaudo della piattaforma scolastica.
