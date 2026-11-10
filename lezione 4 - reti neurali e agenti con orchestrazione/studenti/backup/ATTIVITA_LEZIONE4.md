# Lezione 4 · Un agente che sa fare più cose

**ITS MAKER Bologna · 12 novembre 2026 · Microsoft Copilot e giochi nel browser**

## Il caso

Il responsabile del reparto presse vi scrive:

> «Per la pressa P03 mi servirebbe un solo assistente che sappia fare più lavori: preparare la nota per chi arriva al turno dopo, spiegare un allarme a un operatore nuovo e controllare quanto è durato un fermo. Non voglio tre assistenti diversi: ne voglio uno che capisce da solo quale lavoro gli sto chiedendo.»

Prima capite, giocando nel browser, come impara un programma di intelligenza artificiale. Poi costruite in Microsoft Copilot un agente con più competenze e lo mettete alla prova.

I testi di lavoro sono tre file di testo semplice, che si aprono con Blocco note (l'estensione `.txt` indica questo tipo di file): `Registro_P03_13-15_ottobre_2026.txt` (il registro della P03 del 13–15 ottobre), `Guida_allarmi_P03.txt` (la guida agli allarmi della pressa) e `Regole_indicatori_P03.txt` (le regole di calcolo degli indicatori).

## Come lavorate

- Ognuno lavora da solo sul proprio computer.
- I siti dei giochi si aprono nel browser. Copilot si apre con l'account scolastico.
- Non consegnate nessun file. Scrivete tre file di testo come appunti vostri: `appunti_reti.txt`, `istruzioni_assistente_P03.txt`, `casi_di_prova.txt`. Li scrivete con Blocco note e li lasciate aperti: li riempite man mano durante la lezione. Salvate con Ctrl+S ogni volta che scrivete qualcosa.
- Mentre lavorate il docente passa tra i banchi: vi chiede di mostrare lo schermo e di raccontare che cosa avete fatto e perché.
- I tre testi di lavoro li trovate su Teams. Scaricateli sul vostro computer. Per usarli: aprite il file con Blocco note, premete Ctrl+A per selezionare tutto, Ctrl+C per copiare, poi incollate con Ctrl+V dove serve.

## Parte 1 · Come sceglie la parola successiva

Lavorate nel browser. Quello che scrivete va in `appunti_reti.txt`.

1. Aprite Transformer Explainer: `poloclub.github.io/transformer-explainer`. È un modello molto piccolo che completa frasi in inglese. Non è un assistente: non risponde a domande. La pagina scarica il modello (circa 650 MB): finché non ha finito non potete scrivere frasi vostre, quindi usate il menu **Examples**, che contiene frasi in inglese già pronte.
2. Scegliete un esempio e guardate, sotto **Probabilities**, quali parole il modello propone dopo la frase, con la probabilità di ciascuna.
3. Prima di muovere il cursore **Temperature**, scrivete in `appunti_reti.txt`, sotto il titolo «Parola successiva»: che cosa pensate che succeda alle probabilità se la alzate? E se la abbassate?
4. Provate. Scrivete sotto la previsione che cosa avete visto davvero e perché secondo voi.
5. Quando avete finito chiudete la scheda, così il browser non continua a scaricare.

Qui non c'è una risposta sbagliata da trovare: si guardano le probabilità. Il modello sceglie la parola successiva leggendo il testo che sta prima: tenetelo a mente per la parte 4.

## Parte 2 · Una rete che impara

Una **rete neurale** è un programma fatto di tanti piccoli calcoli collegati fra loro. Si **addestra**: le si mostrano esempi e i collegamenti tra i calcoli cambiano, un poco alla volta, finché la rete sbaglia meno. I numeri che cambiano si chiamano **pesi**.

Lavorate nel browser. Quello che scrivete va in `appunti_reti.txt`, sotto il titolo «Rete».

1. Aprite TensorFlow Playground: `playground.tensorflow.org`. A destra vedete punti arancioni e blu: la rete deve imparare a dire di che colore è un punto. Metà dei punti serve per addestrare la rete, l'altra metà per provarla: la prova usa punti che la rete non ha mai visto.
2. Cominciate dal cerchio: è il primo disegno nella colonna **Data** (punti blu al centro e arancioni attorno). Alla fine ripeterete la prova con la spirale.
3. La colonna **Features** contiene le informazioni che date alla rete: X1 e X2 sono le due coordinate di ogni punto. Lasciate accesi solo X1 e X2. Sopra la rete c'è **Hidden layers** (strati nascosti: le colonne di neuroni, i quadratini, tra le informazioni in ingresso e l'uscita). Con i pulsanti **−** togliete tutti gli strati nascosti, fino a zero.
4. Prima di premere il pulsante di avvio in alto a sinistra, scrivete: riuscirà a separare i punti? Perché?
5. Decidete come giudicherete la rete: scrivete il valore di **Test loss** sotto il quale dite che funziona. Il Test loss misura quanto la rete sbaglia sui punti di prova: più è basso, meglio è. Il **Training loss** è la stessa misura sui punti usati per addestrare.
6. Premete l'avvio, guardate Epoch, Training loss, Test loss e i colori dello sfondo, poi fermate. **Epoch** conta i giri di addestramento: a ogni giro la rete rivede i punti di addestramento. Scrivete che cosa è successo.
7. Cambiate **una cosa alla volta**: neuroni e strati (con i pulsanti **+** e **−**), Features, **Learning rate** (la velocità di apprendimento). Cercate la rete più piccola che rispetta il vostro criterio. Scrivete una riga per ogni prova: che cosa avete cambiato, Test loss, funziona sì o no.
8. Alzate **Noise** (il disturbo nei punti) a 50, usate la rete con 4 e 2 neuroni e lasciatela andare per qualche migliaio di **Epoch**. Guardate Training loss e Test loss mentre passa il tempo: che cosa fanno? Scrivete che cosa notate e una spiegazione.
9. Guardate le linee tra i neuroni: più sono spesse, più il peso è grande. Scrivete in due righe che cosa avete capito di come impara la rete.
10. Ripetete la ricerca della rete più piccola con la spirale (l'ultimo disegno nella colonna Data). Può anche non riuscire: scrivete fin dove siete arrivati.

## Parte 3 · Imparare dai risultati

Nel gioco di prima la rete riceveva esempi con il colore giusto. Qui nessuno dice agli uccellini che cosa fare: ognuno ha una piccola rete che decide quando saltare guardando due numeri (la sua altezza e la posizione del varco tra i tubi). Quando un uccellino colpisce un tubo, la sua partita finisce. Alla fine di ogni giro, chiamato **generazione**, restano i migliori, copiati con piccole variazioni.

Lavorate nel browser. Quello che scrivete va in `appunti_reti.txt`, sotto il titolo «Uccellini».

1. Aprite Flappy Learning: `xviniette.github.io/FlappyLearning`. Il gioco parte da solo con 50 uccellini. Sullo schermo: **Generation** (il numero del giro), **Max Score** (il punteggio migliore), **Alive** (quanti sono ancora vivi). I pulsanti **x1**–**MAX** cambiano la velocità.
2. Prima di guardare, scrivete: dopo quante generazioni pensate che un uccellino riesca a non morire più?
3. Avviate con **x5**. Scrivete la generazione in cui il punteggio comincia a salire senza fermarsi.
4. Ricaricate la pagina (ricomincia da zero) due volte e scrivete di nuovo la generazione. Il numero è lo stesso? Se no, che cosa è cambiato?
5. Scrivete: quali due numeri guarda ogni uccellino? Chi decide quali uccellini restano per il giro dopo?
6. Scrivete due righe: in che cosa questo gioco è diverso dal gioco della parte 2?

Un modo di insegnare a un programma a scrivere come piace a voi funziona in modo simile: si mostrano esempi di risposte buone e si premiano quelle che piacciono di più. Un vero addestramento cambia i numeri dentro il modello e richiede molti esempi e molta potenza di calcolo. Nella parte 4 farete una cosa diversa, più semplice: scriverete degli esempi dentro le istruzioni dell'agente. Alla fine vedrete la differenza.

## Parte 4 · L'agente con più competenze

Lavorate in Microsoft Copilot, con l'account scolastico.

Alcune parole:

- **Agente**: un assistente di Copilot con le istruzioni che scrivete voi. Ogni nuova conversazione con l'agente parte da quelle istruzioni.
- **Competenza**: la parte delle istruzioni che spiega come svolgere un tipo di lavoro.
- **Indice delle richieste**: l'elenco che dice all'agente quale competenza usare per ogni tipo di richiesta.
- **Orchestrazione**: scegliere la competenza giusta e l'ordine in cui usarle, anche quando una richiesta ne tocca più d'una.

Le istruzioni dell'agente sono testo che Copilot legge prima della vostra richiesta, come le parole che precedono quella da prevedere nel gioco della parte 1. Indice e competenze sono pezzi di testo come gli altri: Copilot li legge e decide da solo che cosa fare, il programma non li esegue come funzioni separate. La riga in cui l'agente scrive quale competenza ha usato è una sua dichiarazione: va controllata sulla risposta.

### A · Guardate un esempio

Il docente mostra al proiettore un agente con più competenze, su un caso diverso dalla P03: il noleggio di biciclette di una città. Intanto scrivete in `casi_di_prova.txt`, sotto il titolo «Esempio del docente»: quali richieste del noleggio toccano più di una competenza? Come le gestisce l'agente?

### B · I tre lavori da fare

Il responsabile vuole che l'agente sappia fare questi tre lavori. Per ognuno vi diciamo che cosa deve ottenere e quali limiti ha. Le istruzioni per ottenerlo le scrivete voi.

| Lavoro | Documento | Che cosa deve ottenere | Limiti |
| --- | --- | --- | --- |
| 1. Passaggio di turno | Registro P03 | Una nota per chi inizia il turno dopo: fermi, valori letti, interventi, cose ancora da controllare | Usa solo fatti scritti nel registro. Se non si capisce di quale giorno o turno si parla, chiede prima. |
| 2. Spiegare un allarme | Guida allarmi P03 | Una risposta breve per un operatore nuovo: che cosa significa, primo controllo, chi interviene | Non aggiunge istruzioni che la guida non contiene. Non suggerisce mai di escludere o aggirare una protezione. |
| 3. Durata del fermo | Regole indicatori P03 e registro | I minuti di fermo secondo la definizione scritta nelle regole, con gli orari usati, e i pezzi teorici persi | Usa la definizione del documento, non una sua. Se manca un dato per il calcolo, lo chiede invece di sceglierne uno. |

Valgono per tutti i lavori: l'agente usa solo i testi che gli date; ciò che nei testi non c'è, non lo inventa; la prima riga di ogni risposta dice «Competenza usata:» e il nome della competenza.

### C · Progettate l'agente

Scegliete **due lavori su tre**.

Scrivete voi il testo, con Blocco note: non chiedete a Copilot di scriverlo. Il file `istruzioni_assistente_P03.txt` contiene solo il testo dell'agente e, in fondo, «Correzioni dopo le prove». Il testo ha queste parti, nell'ordine:

1. **Regole per tutte le richieste**: chi è l'agente, in che lingua risponde, quali testi usa, che cosa non fa.
2. **Indice delle richieste**: per ogni tipo di richiesta, quale competenza usare.
3. **Una competenza per ogni lavoro scelto.**
4. **Che cosa fare** quando una richiesta tocca due competenze e quando non ne tocca nessuna.
5. **Stile delle risposte**: almeno due esempi che scrivete voi, di come volete che l'agente risponda (per esempio una nota di passaggio nello stile del reparto).

Le scelte sono vostre: come chiamarlo, quante competenze scrivere, con quali parole riconoscere una richiesta, quando deve farvi una domanda prima di rispondere, quale stile usare.

Prima di creare l'agente controllate che ogni competenza dica: quando si usa, quali documenti servono, che cosa chiedere se manca un dato, come scrivere la risposta.

### D · Create e provate l'agente

1. Aprite Copilot. Il docente vi mostra dove si crea un agente. Usate solo il campo delle istruzioni: se Copilot vi offre di scrivere le istruzioni al posto vostro, non usate quella funzione.
2. Copiate da `istruzioni_assistente_P03.txt` tutto il testo tranne «Correzioni dopo le prove», incollatelo nel campo delle istruzioni e salvate l'agente con un nome. Se Copilot non accetta tutto il testo, accorciate prima gli esempi di stile e le frasi ripetute: non togliete l'indice né la regola per le richieste che toccano due competenze. Scrivete in «Correzioni dopo le prove» che cosa avete tolto.
3. Aprite una nuova conversazione con il vostro agente. Incollate in un solo messaggio i documenti che servono alla richiesta, uno sotto l'altro (per la durata del fermo: le regole e il registro), e sotto la richiesta. Se Copilot non accetta tutto il testo, incollate solo i giorni del registro che servono alla richiesta.
4. Fate almeno una richiesta per ogni competenza scritta e una richiesta che ne tocca due. Ogni richiesta va in una nuova conversazione. Se l'agente vi fa una domanda, rispondete nella stessa conversazione: se mancava davvero un dato, è il comportamento richiesto.
5. Controllate la riga «Competenza usata» e la risposta, confrontandole con il documento. Se qualcosa non va, correggete il testo e riprovate.

### E · Mettete alla prova il vostro agente

1. Rileggete il vostro indice: che cosa non prevede? Dove due competenze si toccano?
2. Inventate cinque casi critici e tranelli. Non state cercando di far sbagliare l'agente: state cercando che cosa avete dimenticato di prevedere. Tra i cinque casi ci devono essere: una richiesta che il vostro indice non prevede; una che tocca due competenze; una a cui manca un dato; una che chiede un dato che il documento non contiene; una per la competenza che avete provato meno. Le richieste le inventate voi.
3. **Prima di provare**, scrivete in `casi_di_prova.txt`, una riga per caso: la richiesta, la competenza che vi aspettate e il dato che vi aspettate nella risposta (o la domanda che l'agente dovrebbe fare).
4. Per ogni caso aprite una nuova conversazione con il vostro agente, incollate i documenti che servono e, sotto, la richiesta. **Dopo la risposta** completate la riga: la competenza usata dall'agente, se il dato della risposta c'è nel documento (sì oppure no), `OK` oppure `ERRORE`, e perché. È `ERRORE` anche una competenza giusta con un dato che nel documento non c'è. Se manca un dato e l'agente fa una domanda, è la risposta attesa.

### F · Correggete le vostre istruzioni

1. Per ogni `ERRORE` decidete che cosa correggere: una regola generale, l'indice, una competenza, la richiesta o il documento incollato.
2. Correggete il testo in `istruzioni_assistente_P03.txt`. In fondo, sotto «Correzioni dopo le prove», scrivete che cosa avete cambiato e il motivo.
3. Se tutti i casi sono `OK`, scrivete sotto «Correzioni dopo le prove» quale regola ha funzionato in ogni caso. Poi inventate un caso che le vostre istruzioni non coprono ancora, aggiungete la regola che lo copre e scrivete il caso sotto «Correzioni dopo le prove».
4. Aggiornate il vostro agente con il testo corretto, senza la parte «Correzioni dopo le prove». Riprovate ogni caso con `ERRORE` (oppure il caso nuovo) in una nuova conversazione e scrivete sotto la correzione l'esito: `OK` oppure `ERRORE`.

### G · Istruzioni o addestramento

1. Scegliete una richiesta e i documenti che le servono.
2. Fate la stessa richiesta due volte, ognuna in una nuova conversazione: una con il vostro agente, una con Copilot normale, senza agente. Confrontate le due risposte: lunghezza, ordine delle informazioni, parole usate. Scrivete tre righe in `appunti_reti.txt`, sotto il titolo «Istruzioni o addestramento».
3. Ripetete la richiesta con il vostro agente, in un'altra nuova conversazione. Ora avete due risposte dell'agente alla stessa richiesta. Sono uguali? Perché? Ripensate alla parte 1. Scegliete la risposta che preferite e scrivete due motivi. Una scelta come questa, tra risposte migliori e peggiori, è il tipo di dato con cui si può addestrare uno stile. Quante scelte pensate che servirebbero? Che cosa cambierebbe dentro il modello? Scrivete due righe.
4. In Playground e in Flappy Learning cambiavano i numeri dentro la rete, i pesi. Nel vostro agente che cosa è cambiato: i numeri dentro Copilot o il testo che Copilot legge? Scrivete la risposta.

## Se Copilot non funziona

Avvisate subito il docente. Non restate fermi.

- **L'agente non si crea o non accetta il testo:** usate una conversazione normale. In ogni nuova conversazione incollate per prime le istruzioni, poi in un solo messaggio i documenti e la richiesta. Nella parte G confrontate una conversazione che comincia con le vostre istruzioni e una che comincia senza. Non sono vere istruzioni dell'agente: scrivetelo in `casi_di_prova.txt`.
- **Copilot non risponde:** lavorate sulla carta. Per ogni caso della parte E cercate nel vostro testo la riga dell'indice o della competenza che lo gestisce e copiatela accanto al caso, applicandola alla lettera senza aggiungere nulla: scrivete quale competenza userebbe l'agente e che risposta darebbe. Se non c'è nessuna riga che lo gestisce, è `ERRORE`. Segnatelo in `casi_di_prova.txt`.
- Gli appunti si scrivono come sempre.

## I vostri appunti

Non c'è niente da consegnare o da caricare: i file servono a voi, per ricordare e per raccontare a voce quello che avete fatto.

| File | Contenuto |
| --- | --- |
| `appunti_reti.txt` | Previsioni e osservazioni su Transformer Explainer, Playground e Flappy Learning; confronto tra istruzioni e addestramento (parte G) |
| `istruzioni_assistente_P03.txt` | Il testo dell'agente e, in fondo, le correzioni dopo le prove |
| `casi_di_prova.txt` | L'esempio del docente e i casi inventati per il vostro agente, con gli esiti |

## Prima di finire

- Nei vostri appunti ci sono le previsioni e le osservazioni dei tre giochi?
- Il testo dell'agente ha le cinque parti: regole, indice, competenze, richieste che ne toccano più d'una o nessuna, stile?
- Ogni `ERRORE` ha una correzione, con il motivo e con l'esito della nuova prova?
- Sapete raccontare a voce che cosa avete provato e che cosa avete cambiato?

## Da dove vengono i giochi

| Gioco | Indirizzo | Autori | Licenza |
| --- | --- | --- | --- |
| Transformer Explainer | `poloclub.github.io/transformer-explainer` | Georgia Tech, Polo Club of Data Science | MIT |
| TensorFlow Playground | `playground.tensorflow.org` | Daniel Smilkov e Shan Carter | Apache-2.0 |
| Flappy Learning | `xviniette.github.io/FlappyLearning` | xviniette | MIT |
