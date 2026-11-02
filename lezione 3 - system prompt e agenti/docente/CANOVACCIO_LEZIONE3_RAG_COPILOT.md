# Lezione 3 — L'assistente di reparto della P03

**Canovaccio docente · ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot Basic**

La lezione usa il caso P03 con documenti distribuiti tramite Teams e forniti nella conversazione. «Assistente di reparto» indica Microsoft Copilot con le istruzioni progettate dagli studenti, non un altro programma. I materiali sono la scheda da compilare, la raccolta dei documenti, le slide e la guida docente.

**Prove di piattaforma:** il docente ha osservato esecuzione Python e creazione di un CSV scaricabile nel proprio agente. Lettura dei nuovi documenti, Blocchi appunti e comportamento sulle postazioni degli studenti richiedono ancora collaudo con account scolastico. Le verifiche dei file non dimostrano il funzionamento con quegli account.

## 1. Scopo e limiti dell'attività

Le coppie riprendono le proprie istruzioni P03 e progettano un assistente per un collega: consultare diario, catalogo e magazzino; distinguere dati storici e datati; verificare una richiesta di materiale con Python; produrre una tabella dei risultati da controllare.

La situazione di riferimento è il **19 ottobre 2026 alle ore 08:00**. Non è la data reale della lezione e non è un collegamento al magazzino aggiornato.

- Copilot Blocchi appunti: studio e riscontro delle fonti complete, se effettivamente disponibile.
- Agente o conversazione indicata dal docente: comportamento del servizio e uso dello strumento di calcolo.
- Persone: scelta di chi userà l'assistente e di che cosa dovrà fare, scrittura delle istruzioni, casi di prova e controllo dei risultati.

Non si ricompilano i 24 eventi e non si ripete la conversione del registro. Nessuna manutenzione, istruzione d'intervento sulla pressa, autorizzazione di montaggio, ordine o aggiornamento reale del magazzino. Le etichette `PROPOSTA DA CONTROLLARE` e `SERVE UN CONTROLLO` sono testo, non azioni collegate a un gestionale.

## 2. Risultati da osservare

Ogni studente deve saper:
1. collegare una frase al documento, al passaggio e alla data che la sostengono;
2. distinguere evento storico, catalogo successivo e disponibilità documentata;
3. motivare una regola delle istruzioni conservata, modificata o eliminata;
4. inventare una richiesta che verifichi una capacità o un limite dell'assistente senza suggerire la risposta;
5. distinguere dati del documento, numeri usati nel calcolo, esecuzione di Python e risultato;
6. spiegare una conclusione che i documenti o il calcolo non autorizzano.

## 3. Materiali e distribuzione

| Materiale | Uso |
| --- | --- |
| Scheda `studenti/ATTIVITA_LEZIONE3` in Word/PDF | Documento della coppia per progetto, controlli, prove e risposte individuali; da compilare in Word o LibreOffice Writer |
| Raccolta `studenti/01_DOCUMENTI_P03` in testo, Word e PDF | Diario completo dei 24 appunti, catalogo rev2 e nuova situazione di magazzino |
| Istruzioni P03 della coppia | Punto di partenza da rivedere, non testo da sostituire con una soluzione pronta |
| Presentazione ufficiale in PowerPoint, HTML e PDF | Appoggio al lavoro delle coppie, non lezione frontale preliminare |
| Guida docente e fonti canoniche in `docente/` | Preparazione, riscontri e rigenerazione; non distribuire come consegna |

Teams distribuisce e raccoglie i file. La coppia allega la raccolta completa nella conversazione. Il formato viene scelto dopo la verifica con account studente; non caricare più versioni dello stesso file.

Ogni nuova conversazione riceve di nuovo i documenti. Se si usa una chat normale, si inviano di nuovo anche le istruzioni iniziali. Nessun trasferimento automatico dai Blocchi appunti o memoria permanente dei file è presunto. Se si incolla il testo completo anziché allegare il file, annotare la differenza.

## 4. Documenti e dati da conservare

Il diario originale racconta 24 appunti del 13–15 ottobre 2026. La riparazione del 14/10 usa FLT-992; la produzione riprende alle 15:05 dopo il fermo delle 14:20. Il catalogo DOC-RICAMBI rev2 del 18/10 associa P03 a FLT-993 e P30 a FLT-229. La revisione successiva non riscrive l'evento e non dimostra incompatibilità o obblighi di sostituzione.

Il nuovo documento DOC-MAG-20261019 rev1 riporta, al 19/10 ore 08:00, 5 pezzi FLT-992, 8 pezzi FLT-993 e 4 pezzi FLT-229. I movimenti descritti sono già compresi nei saldi. Queste quantità e registrazioni sono nuovi dati sintetici del caso, non informazioni dedotte dal solo diario.

Non introdurre prezzi, soglie di riordino, priorità o regole manutentive. La difficoltà sta nel riconoscere significato e provenienza dei dati, non nel complicare la contabilità.

## 5. Verifiche prima dell'aula

Con account studente provare accesso a Copilot, lettura della raccolta di documenti, richiesta con dati non suggeriti nella domanda, Python nella stessa conversazione e apertura del file dei risultati. Controllare che sia possibile vedere i dettagli del calcolo e mostrare agli studenti dove trovarli. Provare separatamente i Blocchi appunti. Registrare richiesta, risposta, file/revisione e data senza raccogliere credenziali.

Non presumere funzioni da un nome di licenza. Nessuna attivazione a pagamento. Un risultato scritto in chat non dimostra esecuzione di Python; un programma eseguito non dimostra che numeri e operazione siano corretti.

Se si usa una normale chat, le istruzioni nel primo messaggio sono istruzioni dell'utente, non veri messaggi di sistema. Distinguere questa modalità dalla modifica di un agente realmente configurato.

## 6. Sequenza operativa

### Avvio e scelta del collega

Il docente spiega che cosa farà l'assistente e fa aprire i materiali. La coppia sceglie chi lo userà, quale risposta sarà utile e che cosa non deve fare. Uno studente usa il computer, l'altro controlla; i compiti si scambiano durante il lavoro.

### Controllo dei documenti

La coppia trova a mano un fatto e poi, se indicato, usa i Blocchi appunti per fare domande proprie. Compila subito entrambe le tabelle della sezione 2 della scheda: dati e passaggi controllati, richiesta effettiva e risposta verificata oppure controllo in lettura diretta. Non delega tutta la tabella al modello e non rifà il riassunto del diario.

### Progettazione delle istruzioni

Si confrontano regole conservate, cambiate/eliminate e nuove se necessarie. Le istruzioni sono scritte dagli studenti; i fatti restano nelle fonti. Le domande di chiarimento servono solo quando cambia davvero ciò che è possibile verificare, non come passaggio obbligatorio. Una richiesta su un codice esplicito può non richiedere l'identità della macchina.

### Prima prova e uso di Python

In una conversazione nuova, con tutti i documenti, la coppia inventa una richiesta che usi almeno due testi e un calcolo. Prima dell'invio annota numeri scelti, documento di provenienza e risultato atteso. Fa eseguire Python, scarica e apre la tabella prodotta. Controlla documenti, numeri e operazione. Il risultato descrive un'ipotesi, non un prelievo effettuato.

### Preparazione della prova dei compagni

Gli studenti inventano richieste per verificare uso di più documenti, rapporto fra un evento e un documento successivo, mancanza di un dato necessario o informazione non documentata. Annotano risultato atteso e documenti da controllare prima di inviare la domanda. Non ricevono frasi pronte e non devono aspettarsi un errore del modello.

### Scambio e scelta sulle istruzioni

Ogni coppia prova l'assistente altrui e riceve una prova sul proprio. A apre una nuova conversazione, fornisce i documenti e le istruzioni iniziali se usa una chat normale. B usa il computer di A senza cambiare account: invia la richiesta, controlla e compila la scheda di A. A osserva senza suggerire risposte. Poi si invertono i ruoli. Nessuno scambio di credenziali o modifica delle istruzioni altrui.

Si corregge soltanto con un motivo chiaro. Se la risposta è corretta si conserva la regola e si prova un'altra richiesta. Una modifica deve valere anche per altri casi, non contenere la risposta a una singola domanda; si riprova fornendo di nuovo documenti e istruzioni necessarie.

### Restituzione individuale

Ogni studente, senza Copilot, spiega quale documento e data confermano una frase, quali numeri sono stati usati e quale decisione resta alla persona, perché una regola è stata conservata o cambiata. La scheda distingue il contributo individuale dal lavoro della coppia.

## 7. Consegna e valutazione

La consegna comprende scheda compilata, `istruzioni_assistente_P03.txt` e file della tabella prodotta con Python. La scheda registra controlli sui documenti, prova propria, prova dei compagni, decisione sulle istruzioni e risposte individuali. Non duplicare prove che coprono più aspetti.

Valutare comprensione delle fonti, progetto, qualità delle richieste inventate, controllo e revisione motivati, autonomia individuale. Non valutare velocità, grafica, quantità di codice o percentuale di risposte giuste del modello.

Le modalità `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE` e `ANALISI_CASO` indicano provenienza, non correttezza. Non richiedere screenshot, esportazioni automatiche o scrittura di Python come condizione di consegna.

## 8. Ostacoli senza false equivalenze

Se i Blocchi appunti non sono disponibili, usare lettura diretta senza attestare quella competenza. Se il file non è leggibile, usare un formato già provato o testo completo, registrando la modalità. Se l'agente non è configurabile, una chat con istruzioni iniziali non dimostra creazione dell'agente. Se Python non è disponibile o non osservabile, usare soltanto dimostrazioni realmente eseguite o analisi dichiarate: l'obiettivo di esecuzione autonoma non è raggiunto.

Un'astensione deve essere verificata nei documenti. Un errore non permette da solo di diagnosticare un passaggio interno non osservabile. Una prima risposta corretta non richiede né una correzione artificiale né dati più complicati.

## 9. Regole di produzione

Separare studenti e docente. Conservare i 24 appunti, le date e i fatti. Italiano comune, istruzioni concrete e nessuna durata didattica. Presentazione nel modello ITS MAKER ufficiale 16:10, con testi e tabelle modificabili e HTML coerente. Aggiornare tutti i formati interessati senza modificare altre lezioni. Verificare documenti e presentazioni nei programmi reali e distinguere tale controllo dal collaudo della piattaforma scolastica.
