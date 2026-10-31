# Lezione 3 — Dal diario della P03 allo sportello che consulta le fonti

**Canovaccio per il docente · ITS MAKER Bologna · Microsoft Copilot Basic e Copilot Blocchi appunti**

Progettazione sviluppata nel confronto con Gemini 4 Argon. Questo documento definisce la regia della prossima lezione: non è una scheda da distribuire agli studenti e non contiene istruzioni complete da incollare in Copilot.

**Stato:** canovaccio di progettazione, non attestazione di collaudo del tenant scolastico. Le fonti web, il documento di magazzino e i materiali studenti descritti sotto devono essere predisposti e verificati prima dell'erogazione. Questo lavoro non attiva GitHub Pages e non modifica le presentazioni esistenti.

## 1. Missione e perimetro

Le coppie riprendono gli agenti P03 effettivamente creati in aula e li trasformano in uno **sportello documentale per un collega del reparto**: consultare il diario, il catalogo e una situazione di magazzino, distinguendo fatti storici, informazioni valide a una certa data e dati non documentati.

**Data di riferimento proposta per lo scenario: 19 ottobre 2026.** «Catalogo corrente» e «disponibilità» vanno sempre riferiti ai documenti del caso, non alla data reale della lezione o a sistemi aggiornati in tempo reale.

- **Blocchi appunti:** ambiente in cui la coppia studia e controlla le fonti per progettare il servizio.
- **Agente:** servizio riutilizzabile che un'altra coppia può interrogare senza conoscere in anticipo tutti i documenti.
- **Persona:** sceglie il perimetro, verifica le evidenze, decide quali conclusioni sono autorizzate e controlla le proposte.

Non si ricompila la tabella dei 24 eventi, non si progetta manutenzione e non si impartiscono istruzioni per usare o riparare la pressa. Nessun acquisto, aggiornamento di magazzino o modifica di documenti viene eseguito dall'agente. Le eventuali proposte restano «PROPOSTA DA CONTROLLARE» o «SERVE UN CONTROLLO».

### Risultati da osservare

Alla fine ogni studente deve saper:

1. individuare il documento e il passaggio che sostengono un'affermazione;
2. distinguere evento storico, catalogo successivo e disponibilità documentata;
3. motivare una modifica alle istruzioni dell'agente, oppure spiegare perché una regola già valida viene conservata;
4. inventare una richiesta che metta alla prova un confine del servizio, senza suggerire la risposta;
5. riconoscere un'informazione non sostenuta dai documenti, anche quando la risposta di Copilot è plausibile.

## 2. Materiali: riuso e preparazione necessaria

| Materiale | Situazione di partenza | Preparazione docente |
| --- | --- | --- |
| Agente P03 e `istruzioni_P03.txt` della coppia | Lavoro già svolto in aula; non presumere che coincida con ogni variante nel repository | Verificare accesso e possibilità di modificare il proprio agente; conservare il testo iniziale delle istruzioni |
| `registro_P03.md` della coppia | Prodotto della lezione precedente | Usarlo nei Blocchi appunti solo dopo aver verificato i 24 appunti e l'identità dei fatti con la fonte pubblicata; in caso di tagli o dati alterati usare il file integrale docente, senza ripetere la conversione in Markdown |
| Diario originale P03 | [Sorgente docente esistente](../../lezione%202%20-%2028%20ottobre%202026/ipotesi%202%20-%20system%20prompt%20e%20agenti/docente/REGISTRO_FERMO_P03_SORGENTE.md) | Preparare una versione documentale integrale, senza soluzioni, identica nei fatti al file fornito e alla pagina pubblica |
| Catalogo ricambi rev2 del 18/10/2026 | [Documento docente esistente](../../laboratorio/docente/03_catalogo_ricambi_rev2.md) | Ricavare una fonte con identificativo, revisione, data e associazioni macchina-filtro; escludere le istruzioni didattiche e le note sulle soluzioni |
| Situazione di magazzino al 19/10/2026 | **Nuovo documento sintetico da predisporre** | Includere i codici FLT-992, FLT-993 e FLT-229, disponibilità datate e movimenti comprensibili; dichiarare se le quantità comprendono già i movimenti riportati |
| Fonti per gli agenti | **Tre pagine HTML pubbliche da predisporre e collaudare** | Pubblicare soltanto le fonti, non la guida docente o le risposte; congelare il contenuto prima della lezione |
| Fonti per i Blocchi appunti | **File con lo stesso contenuto delle pagine da predisporre** | Usare un formato effettivamente accettato dall'account studente; file e HTML devono avere gli stessi fatti, date e revisioni |
| Scheda di lavoro di coppia | **Da ricavare da questo canovaccio** | Un solo documento Word o testo semplice per progetto, evidenze e collaudi; niente istruzioni dell'agente già compilate |

### Requisiti del nuovo documento di magazzino

Il documento deve essere una normale fonte di reparto, non un esercizio già risolto. Specificare identificativo, revisione e data della situazione descritta; distinguere quantità disponibili, movimenti e relativi riferimenti temporali. Usare poche voci coerenti e annotazioni ordinarie utili alla lettura, senza introdurre prezzi, soglie di riordino o regole manutentive per rendere il caso più complicato.

I valori numerici nuovi devono essere fissati dal docente nella fonte prima delle prove: non sono fatti già presenti nel diario e non devono essere inventati da studenti o modello. Non inserire avvisi artificiali del tipo «qui manca il dato da cercare». La fonte deve permettere almeno una domanda che richieda l'incrocio con il catalogo, senza ripetere in ogni riga quale macchina usa ogni codice.

### Indirizzi previsti, non fonti già attive

Usare pagine piatte come `registro-p03.html`, `catalogo-ricambi.html` e `magazzino-ricambi.html` alla radice del sito pubblicato. Per esempio:

```text
https://franzo9393.github.io/ITSCorso_UnslothStudio-Git/registro-p03.html
```

Il nome del repository occupa il primo livello del percorso; la pagina occupa il secondo. La cartella sorgente `docs/`, se scelta per la pubblicazione, non compare nell'indirizzo pubblico. Non aggiungere un livello `/rag/` e non usare i normali link GitHub `blob/main/...`.

## 3. Prima dell'aula: condizioni per usare entrambi gli strumenti

La documentazione descrive possibilità del prodotto, non dimostra che il tenant scolastico le abbia abilitate. Effettuare queste verifiche con un vero account studente e registrare data, account di prova non sensibile, documenti/revisioni, richiesta, risposta e riferimenti mostrati.

| Verifica | Evidenza da osservare |
| --- | --- |
| Accesso ai Blocchi appunti | Creazione o apertura di un blocco e aggiunta dei file nei formati scelti, senza acquisti o attivazioni a consumo |
| Uso documentale nel Blocco appunti | Risposta a una richiesta che richieda informazioni dei file, confrontata con i passaggi originali |
| Configurazione dell'agente Basic | Apertura/modifica dell'agente e inserimento delle tre fonti pubbliche, senza file incorporati o connettori a pagamento |
| Uso delle fonti web nell'agente | In una conversazione nuova, risposta con dati specifici del catalogo e del magazzino, non suggeriti nella domanda o nelle istruzioni, con riferimenti verificabili |
| Postazioni, rete e consegna | Accessi individuali, apertura delle fonti originali e salvataggio manuale del documento di lavoro e delle istruzioni |

### Limiti tecnici da tenere visibili al docente

- Per il percorso Basic considerato: fino a quattro URL pubblici, massimo due livelli di percorso e niente parametri di ricerca. Non sono necessari tutti e quattro gli URL.
- Gli agenti dichiarativi con ricerca limitata ai siti configurati usano l'indice di Bing: la pubblicazione o la modifica di una pagina non ne garantisce l'uso immediato. La ricerca web può anche essere limitata dall'amministratore.
- Un dato non restituito non dimostra, da solo, un problema di indicizzazione: non attribuire una causa tecnica certa senza evidenze.
- I Blocchi appunti per utenti Copilot Chat idonei supportano file, ma la documentazione della licenza non include URL come riferimenti nel percorso senza componente aggiuntivo. Non collegare il Blocco appunti all'agente come se fosse una funzione disponibile.
- Dare priorità alle fonti configurate non garantisce il blocco della conoscenza generale del modello. Controllare le affermazioni, non soltanto la presenza di citazioni.
- Non presumere esportazioni, collegamenti di condivisione, ricaricamenti immediati o visibilità dei passaggi interni di recupero. Si può copiare manualmente una risposta effettiva nel documento di lavoro.

**Obiettivo pieno:** gli studenti devono praticare l'uso documentale in entrambi gli strumenti. Una dimostrazione del docente o un testo incollato in chat non certificano la stessa esperienza.

## 4. Sequenza della lezione

### Fase 1 — Riaprire il lavoro e dare uno scopo allo sportello

**Docente.** Presenta la missione, la data dello scenario e i confini documentali. Fa aprire l'agente precedente e il testo delle istruzioni, senza distribuire un nuovo testo da copiare. Richiama soltanto la distinzione fra istruzioni, richiesta e fonti. Spiega RAG come «cercare nelle fonti e usare ciò che si trova per costruire una risposta da controllare».

**Coppia.** Sceglie un destinatario concreto, per esempio un collega del turno successivo o chi prepara una richiesta al magazzino. Scrive a cosa servirà lo sportello e una cosa che non dovrà fare. Individua nelle vecchie istruzioni una regola da conservare e una da riesaminare, come il limite al solo registro o la tabella obbligatoria.

**Evidenza e passaggio.** Nel documento di lavoro sono scritti destinatario, servizio e confine. La coppia sa spiegare perché aggiungere fonti non equivale a ordinare un ricambio.

**Ruoli.** Uno studente usa il computer, l'altro controlla i documenti e annota le decisioni.

### Fase 2 — Costruire una base di evidenze con i Blocchi appunti

**Docente.** Fa aprire i documenti originali e il Blocco appunti. Il registro personale può essere usato solo se i 24 appunti e i dati coincidono con la versione pubblicata; altrimenti fornisce il file integrale docente. Mostra solo i passaggi dell'interfaccia necessari ad aggiungere i file. Prima di interrogare Copilot, chiede alla coppia di individuare manualmente un fatto e il suo passaggio nella fonte.

**Coppia.** Aggiunge i file e formula richieste proprie per capire come i documenti si completano. Costruisce una breve mappa delle evidenze: affermazione controllata, documento/sezione, data o revisione, conclusione consentita e limite. Non chiede un nuovo riassunto del diario, non lascia che Copilot compili la mappa senza controllo umano e non gli delega la scrittura delle istruzioni dell'agente.

**Evidenza e passaggio.** Conserva almeno una richiesta e una risposta effettive del Blocco appunti, verificate sul testo originale. La mappa distingue un fatto storico da un dato di catalogo e individua una questione che richiede più fonti. «Copilot non lo trova» non basta a dimostrare che un dato sia assente: occorre controllare i documenti pertinenti.

**Domande guida del docente.** «Quale passaggio sostiene questa frase?»; «A quale data vale?»; «Che cosa non puoi concludere da questo documento?». Sono domande alla coppia, non richieste complete da incollare nel programma.

### Fase 3 — Riprogettare le istruzioni del proprio agente

**Docente.** Fa scambiare i ruoli della coppia. Chiede di usare la mappa delle evidenze per definire il comportamento dello sportello, non per copiare tutti i fatti dentro le istruzioni.

**Coppia.** Conserva il testo iniziale e scrive la revisione: perimetro del servizio, uso delle fonti, attenzione a date e macchina, richiesta di chiarimenti, gestione delle informazioni non sostenute e controllo umano delle proposte. Mantiene le regole ancora utili e modifica quelle che impediscono la nuova funzione. Decide autonomamente forma e chiarezza delle risposte.

**Evidenza e passaggio.** Può spiegare una modifica motivata e una regola conservata. Le istruzioni non contengono il diario o le risposte ai collaudi: i fatti restano nelle fonti. Non è obbligatorio riscrivere da zero ciò che funziona.

### Fase 4 — Collegare le fonti e provare il servizio

**Docente.** Indica i tre indirizzi già collaudati e fa controllare quali fonti sono state configurate. Non presenta una spunta dell'interfaccia come garanzia di risposte corrette.

**Coppia.** Aggiorna l'agente, collega gli URL e apre una conversazione nuova, senza incollare registro, risposte del Blocco appunti o fatti risolutivi. Prima della prova annota quali documenti dovrebbe consultare per controllare il risultato. Invia una propria richiesta che abbia bisogno delle nuove fonti e verifica dati, riferimenti e limiti della risposta.

**Evidenza e passaggio.** Salva richiesta effettiva, estratto della risposta e riscontro sui documenti. Distingue una risposta verificata da una risposta soltanto plausibile. Se l'agente dichiara un dato assente o non risponde, controlla nei documenti originali se manca davvero oppure è presente ma non è stato usato nella risposta. Non giudica il recupero interno come corretto se non è osservabile.

### Fase 5 — Preparare il collaudo dei compagni

**Docente.** Presenta famiglie di prove, non frasi già scritte: incrocio fra documenti; rapporto fra evento storico e catalogo successivo; richiesta ambigua; informazione non documentata. Le famiglie possono sovrapporsi: non servono prove quasi identiche per riempire righe.

**Coppia.** Inventa richieste adatte al servizio e stabilisce prima quali evidenze permetterebbero di giudicare le risposte. Controlla di non scrivere già la risposta nella domanda. Sceglie un caso diverso da quello usato nell'analisi iniziale, così da non ripetere semplicemente lo stesso compito nei due strumenti.

**Evidenza e passaggio.** Le prove previste richiedono una decisione documentale, non conoscenze tecniche esterne. La coppia sa motivare quale confine sta verificando. La preparazione resta utile anche se la prima risposta dell'agente era corretta.

### Fase 6 — Collaudo ospite, confronto e nuova prova

**Docente.** Organizza lo scambio fra postazioni già aperte dai proprietari, senza scambiare credenziali o presumere collegamenti di condivisione. Avvia il confronto quando le coppie abbinate hanno salvato l'agente e verificato almeno una prova interna; chi è già pronto prepara le proprie richieste e i criteri di controllo, senza aumentare artificialmente la difficoltà. Gli ospiti usano l'agente in una conversazione nuova senza ricevere prima risposte o istruzioni del servizio. L'agente ospite non viene modificato dai visitatori.

**Coppia ospite.** Formula una richiesta propria, pertinente al servizio. Una persona invia la richiesta e copia la risposta effettiva nella sezione prove del documento di lavoro della coppia proprietaria, annotando chi ha svolto il collaudo; l'altra verifica i passaggi nelle fonti originali e formula il giudizio. Anche un'astensione deve essere controllata: il dato manca nei documenti oppure non è stato usato dall'agente? Poi le coppie invertono chi ospita e chi collauda: ogni coppia deve ricevere ed eseguire un collaudo. Tornando al proprio agente, i due studenti invertono i compiti di invio e verifica.

**Coppia proprietaria.** Osserva senza suggerire agli ospiti la risposta che l'agente non ha dato. Decide se cambiare le istruzioni, chiarire il perimetro o lasciare invariata una regola già adeguata, senza attribuire automaticamente ogni errore a una frase mancante. Se modifica, scrive un principio generale, non la risposta alla singola domanda; riprova in una conversazione nuova e conserva il prima/dopo. Se non modifica, documenta perché la risposta era già adeguata e verifica un diverso confine del servizio: non deve inventare un errore per giustificare il lavoro.

**Evidenza e passaggio.** La scheda contiene almeno un collaudo ospite con richiesta, risposta, fonte e giudizio motivato, più la decisione dei proprietari e l'eventuale nuova prova.

### Fase 7 — Restituzione e verifica individuale

**Docente.** Fa confrontare scelte diverse, senza proclamare vincitore l'agente con meno errori. Riprende un risultato sostenuto dalle fonti e una conclusione che i documenti non autorizzano. Non chiede nuovi riassunti del fermo.

**Coppia.** Presenta il proprio destinatario, una scelta progettuale e un'evidenza che ne mostra utilità o limite.

**Ogni studente, senza aiuto di Copilot.** Spiega su una prova effettiva quale documento sostiene una frase, a quale data vale e quale conclusione ulteriore non è giustificata. Indica inoltre una modifica motivata alle istruzioni o una regola mantenuta con ragione.

**Evidenza conclusiva.** Il docente può distinguere il contributo individuale dal prodotto della coppia e l'uso effettivo dei due strumenti dalla sola osservazione.

## 5. Documento di lavoro e consegna minima

Usare un solo documento di coppia, in Word o testo semplice, con tre parti:

1. **Progetto:** destinatario, servizio, confini, breve mappa delle fonti e motivazione delle istruzioni.
2. **Prove:** strumento e modalità di partecipazione; richiesta realmente inviata; passaggio della risposta ricevuta; documento/sezione/data usati per controllarla; giudizio motivato; decisione ed eventuale nuova prova. Il collaudo ospite viene registrato nel documento dei proprietari dell'agente, con identificativo della coppia ospite, così resta disponibile per la loro revisione.
3. **Restituzione:** risultato del collaudo ospite e risposte individuali chiaramente attribuite.

Allegare il testo finale delle istruzioni, per esempio `istruzioni_sportello_P03.txt`, mantenendo nel documento di lavoro la traccia delle modifiche rispetto alla versione iniziale. Il docente osserva o fa riaprire l'agente configurato: il solo testo delle istruzioni non dimostra che l'agente sia stato aggiornato.

Le evidenze devono comprendere uso dei Blocchi appunti, prova propria dell'agente e collaudo ospite. Nel loro insieme devono coprire almeno un incrocio di fonti, un'ambiguità e un'informazione realmente non sostenuta dai documenti. Non occorre duplicare prove che coprono più aspetti.

Per la provenienza delle prove riusare le modalità del corso: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`. Sono modalità, non giudizi di correttezza. Non chiedere screenshot, esportazioni automatiche o programmazione come condizione per consegnare.

## 6. Criteri di valutazione

| Criterio | Evidenza osservabile |
| --- | --- |
| Comprensione delle fonti | Collega affermazioni a passaggi e date pertinenti; non confonde diario, catalogo e magazzino |
| Progettazione del servizio | Definisce destinatario e limiti; motiva regole nuove, conservate o eliminate senza un testo fornito da copiare |
| Qualità delle prove | Inventa richieste pertinenti che non suggeriscono la risposta; verifica anche una prima risposta corretta |
| Controllo e revisione | Riconosce aggiunte non sostenute, motiva una correzione o una conferma e conserva l'evidenza dell'eventuale nuova prova |
| Autonomia individuale | Entrambi partecipano ai ruoli e spiegano una verifica senza affidarla nuovamente a Copilot |

Non valutare velocità, abbellimenti, percentuale di risposte giuste del modello o possibilità tecniche negate dal tenant. Un problema di piattaforma va distinto da una decisione progettuale sbagliata.

## 7. Appigli di verifica riservati alla regia docente

Questi sono fatti delle fonti esistenti, non risposte da mettere nelle istruzioni dell'agente o nella scheda studenti:

- Il 14/10/2026 viene montato FLT-992; il catalogo rev2 del 18/10 associa P03 a FLT-993 e P30 a FLT-229. Il catalogo successivo non riscrive l'evento e non dimostra incompatibilità o obbligo di sostituzione del filtro montato.
- Alle 14:42 la sostituzione è completata ma la macchina resta ferma; alle 14:52 è in prova; la produzione riprende alle 15:05. Il fermo dura 45 minuti, dalle 14:20 alle 15:05.
- Il contatore indica 2.480 pezzi prodotti: non convertirli in cicli di manutenzione.
- Il diario non indica nome del tecnico o prezzo del ricambio. Non dedurli da un ruolo, da un codice o da conoscenze generali; prima di usarli come prove di assenza, controllare che le nuove fonti non li abbiano introdotti.
- Il diario arriva al 15/10/2026: non certifica lo stato reale attuale della pressa. Il catalogo non certifica una giacenza; la giacenza datata non è una disponibilità in tempo reale e non dimostra cosa sia montato sulla macchina.

## 8. Gestione degli ostacoli senza fingere equivalenze

| Situazione osservata | Come proseguire | Limite da dichiarare |
| --- | --- | --- |
| Mancano i file personali precedenti | Usare una copia integra del diario e recuperare il testo delle istruzioni; non ripetere la conversione come nuova attività | La continuità viene ricostruita, non si finge di aver recuperato automaticamente la memoria dell'agente |
| Un passaggio dell'interfaccia blocca la coppia | Mostrare soltanto il passaggio necessario e far riprendere le decisioni agli studenti | Aiuto sul programma, non istruzioni progettuali già pronte |
| Il Blocco appunti non è disponibile | Analisi manuale delle fonti e attività sull'agente se funzionante; usare una traccia docente solo se realmente registrata | Nessuna pratica autonoma nei Blocchi appunti per chi non li ha usati |
| L'agente non usa le fonti web | Analisi nei Blocchi appunti e revisione ragionata delle istruzioni; registrare la richiesta e il risultato, senza attribuire una causa certa | Non è raggiunto l'obiettivo pieno con entrambi gli strumenti; incollare i testi non sostituisce il collaudo web |
| Entrambi gli strumenti non sono disponibili | Progetto su documenti originali ed eventuali tracce reali, distinguendo atteso e osservato | Attività di analisi e progettazione, non laboratorio RAG eseguito dagli studenti |
| Le risposte sono subito corrette | Estendere la copertura a un'altra famiglia di prove e motivare limiti e fonti | Non aggiungere tranelli artificiosi né pretendere correzioni inutili |

## 9. Regole per i materiali successivi

- Distribuire agli studenti solo consegne, fonti e spazi di lavoro: non questa regia, le risposte o istruzioni complete da incollare.
- Separare `studenti/` e `docente/`. Il repository è pubblico: la separazione è organizzativa, non una protezione di accesso alle soluzioni.
- Mantenere italiano comune, istruzioni concrete e nessuna durata didattica. Conservare date, orari e minuti che sono fatti del caso.
- Per eventuali slide applicare il modello PowerPoint ITS MAKER ufficiale 16:10, mantenendo testi e tabelle modificabili e HTML coerente. Verificare apertura e leggibilità nei programmi reali.
- Non cambiare altre lezioni o piattaforme del corso per uniformarle a questa scelta. Il presente canovaccio riguarda soltanto la prossima lezione Copilot.

## 10. Riferimenti tecnici

Da ricontrollare insieme alle funzioni effettivamente disponibili prima dell'aula:

- [Microsoft — Fonti di conoscenza in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge).
- [Microsoft — Ricerca web e fonti degli agenti dichiarativi](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/knowledge-sources).
- [Microsoft — Licenze e fonti supportate nei Blocchi appunti](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-licensing).
- [GitHub — Configurare la sorgente di pubblicazione di Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
