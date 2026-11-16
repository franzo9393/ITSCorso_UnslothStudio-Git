# Lezione 5 · Chi controlla che cosa?

**ITS MAKER Bologna · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

## Da dove partiamo

Il titolare di Ruota Libera ha provato il vostro agente e vuole che sappia fare tutti e tre i lavori: fuori servizio, guasti e passaggio di turno. Oggi completate l'agente e controllate che scelga bene.

Ognuno lavora da solo sul proprio computer. Nella parte 1 partite dal file della lezione 4: `istruzioni_agente_noleggio.txt`. Non avete il file? Ve ne diamo uno di partenza, che ha già i tre lavori. Non ci sono file da consegnare: il risultato si guarda sullo schermo. Salvate solo il file delle istruzioni, aggiornato.

Il percorso è questo:

| Passo | Dove | Che cosa succede |
| --- | --- | --- |
| 1 | Microsoft Copilot | il vostro agente ha più lavori: chi sceglie quale usare? |
| 2 | Unsloth Studio, nel computer virtuale | un modello nel computer virtuale: serve la rete? |
| 3 | opencode, nel computer virtuale | un programma accanto ai file: chi li apre? |

## Riaprite il vostro agente

1. Aprite Blocco note e il file `istruzioni_agente_noleggio.txt`.
2. Aprite Microsoft Copilot, con l'account scolastico, e il vostro agente. Se non c'è, usate una conversazione normale: nel primo messaggio incollate le istruzioni.
3. Scaricate da Teams i tre testi del noleggio: registro, regole del noleggio e guida ai guasti.
4. In una nuova conversazione scrivete un solo messaggio: registro, regole del noleggio e in fondo la richiesta: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»
5. Controllate gli orari con il registro.

## Parte 1 · Un elenco e dei lavori

### 1A · Come è fatto un agente con più lavori

Il testo del vostro agente ha due parti: l'**elenco delle richieste**, che dice a quale lavoro va ogni richiesta, e i **lavori**, ognuno con le sue regole. Due pezzi dell'agente di una pizzeria d'asporto, proiettati (i tagli sono segnati con […]):

| L'elenco dice | Il lavoro dice |
| --- | --- |
| «Pizza fredda o in ritardo, pizza sbagliata → RECLAMO» | «Quando: la pizza è fredda, sbagliata o in ritardo. […] Come rispondere: tre punti.» |
| «Che cosa c'è in una pizza, glutine, allergeni → INFORMAZIONI» | «Quando: il cliente chiede gli ingredienti. Testo da usare: solo la scheda degli ingredienti. […]» |

### 1B · Quale lavoro sceglie?

L'agente della pizzeria ha cinque lavori: ORDINE, RECLAMO, RIMBORSO, INFORMAZIONI, ORARI. Nel Blocco note scrivete, per ogni richiesta, il lavoro che vi aspettate. Può essere uno, due o nessuno. Poi le proviamo una per una in Copilot dal proiettore.

| Richiesta | Il vostro pronostico |
| --- | --- |
| «Vorrei due Margherite per le 20:00.» | |
| «La Diavola ha il glutine?» | |
| «La pizza è arrivata fredda e voglio i soldi indietro.» | |
| «A che ora aprite il sabato?» | |
| «Mi prenoti un tavolo per sabato?» | |

Guardate la prima riga di ogni risposta: «Lavoro usato:». Alla richiesta con due lavori: perché in quest'ordine? Che cosa deve passare dal primo lavoro al secondo? Se il secondo lavoro usasse un numero d'ordine diverso dal primo, chi se ne accorge?

### 1C · Il lavoro che manca

Nel vostro file ci sono FUORI SERVIZIO e un secondo lavoro. Scrivete quello che manca: GUASTI se avete PASSAGGIO, PASSAGGIO se avete GUASTI. Servono una voce nell'elenco e il lavoro, nel file `istruzioni_agente_noleggio.txt`. A destra le domande a cui rispondete voi:

| Domanda | Pizzeria: INFORMAZIONI | Noleggio |
| --- | --- | --- |
| Quando scatta? | «il cliente chiede ingredienti, glutine o allergeni» | Per quali richieste? |
| Che testo usa? | «solo la scheda degli ingredienti» | Quale testo del noleggio? |
| Se manca un dato? | «Non lo so: chiedi al banco.» | Che cosa fa? |
| Come risponde? | in una riga | In quale forma? |

Avete ricevuto il testo di partenza? Ha già tutti e tre i lavori: leggetelo e passate alla prova.

Salvate il file. In Copilot incollate tutto il testo nelle istruzioni del vostro agente. L'ultima riga del file è anche l'ultima in Copilot?

### 1D · Provate: una richiesta per lavoro

Una nuova conversazione per ogni richiesta: registro, regole del noleggio, guida ai guasti e in fondo la richiesta. Prima di inviare, scrivete quale lavoro vi aspettate.

| Il lavoro | La richiesta |
| --- | --- |
| FUORI SERVIZIO | «Bici 12, sabato: per quanti minuti è stata fuori servizio?» |
| GUASTI | «Che cosa significa freni che non tengono?» |
| PASSAGGIO | «Scrivi la nota per il turno dopo, sabato.» |

Guardate la prima riga di ogni risposta. È il lavoro che vi aspettavate? Se non lo è, non partite dal lavoro: leggete la voce dell'elenco. Dice abbastanza chiaramente quando usarlo? Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.

### 1E · Un caso che l'elenco non prevede

Nella pizzeria: «La Diavola ha il glutine e quanto costa?» Sono due lavori, INFORMAZIONI e ORDINE, e nell'elenco non c'è nessuna riga per questa coppia. Per alzata di mano: parte da INFORMAZIONI, parte da ORDINE, o ne usa uno solo? Poi si prova dal proiettore.

Ora inventate il vostro caso: una richiesta del noleggio che potrebbe andare a due lavori, o a nessuno. Scrivetela nel Blocco note e, prima di inviarla, scrivete dove la mandereste voi. Provatela. Se va dove non volevate, correggete la voce dell'elenco o aggiungete la riga che manca, poi riprovate.

### 1F · Due lavori in catena

Richiesta: «Bici 12, sabato: per quanti minuti è stata fuori servizio? Scrivi la nota per il turno dopo.»

Nel vostro elenco deve esserci una riga per FUORI SERVIZIO e PASSAGGIO insieme: prima FUORI SERVIZIO, poi il risultato entra nella nota. Se manca, scrivetela e aggiornate l'agente. Prima di inviare: quale numero comparirà nella nota?

Poi guardate il numero e gli orari proiettati, che sono quelli del registro per la bici 12, sabato. Nella vostra nota, sotto «Fuori servizio»: sono gli stessi?

### Salvate il file

Il file `istruzioni_agente_noleggio.txt` deve contenere tutto: regole per tutti i casi, l'elenco delle richieste con le vostre correzioni, i tre lavori, lo stile. Aggiornate l'agente in Copilot e controllate che il testo sia arrivato intero.

### Chi ha scelto? Chi ha controllato?

Copilot ha scelto il lavoro leggendo l'elenco che avete scritto voi. Il numero nella nota: chi l'ha controllato?

## Parte 2 · Un modello sul vostro computer

Passate al computer virtuale: un computer dentro il computer, con il suo Windows e i suoi programmi. Ognuno ha il suo. Unsloth Studio è il programma che carica un modello e vi lascia parlarci.

### Aprite Studio

1. Fate doppio clic sul collegamento **Unsloth Studio** del desktop: si apre il browser.
2. In alto deve esserci il nome del modello, Qwen3.5-2B-GGUF. Se non c’è, scegliete Select model › On Device › Qwen3.5-2B-GGUF e aspettate che si carichi.
3. Accanto c’è una finestra nera con del testo che scorre: non chiudetela, o Studio si ferma. Se compare «2 aggiornamenti del runtime», scegliete «Più tardi».

Il modello si chiama Qwen3.5-2B: «2B» vuol dire due miliardi di pesi, i numeri che ha imparato.

### 2A · Serve Internet?

1. Prima di provare, decidete: per rispondere, questo modello ha bisogno di Internet? Sì o no. Alzata di mano.
2. Con il pulsante **Nuova chat**, a sinistra, aprite una chat. Scrivete: «In una frase: a che cosa serve un cacciavite?» Leggete la risposta.
3. Togliete la rete al computer virtuale. Il docente vi fa vedere come.
4. In un’altra chat rifate la stessa domanda. Risponde ancora?
5. Riattivate la rete: serve tra poco a opencode.

Ora guardate dove gira il modello:

| | Copilot | il modello di Studio |
| --- | --- | --- |
| Dove gira | in rete, sui computer di Microsoft | sul vostro computer virtuale |
| Il codice | non si può leggere | aperto: si può leggere |
| Di chi è | di Microsoft | vostro: è un file sul vostro computer |

### 2B · Le manopole del modello

Il pannello delle impostazioni si apre con l’icona in alto a destra, nella figura della slide. Scorretelo: trovate **System Prompt**, **Temperature**, **Top P**, **Top K** e **Context Length** (la quantità di testo che il modello riesce a tenere insieme). Quale numero c’è accanto a Context Length? Non toccatelo. Guardate anche il valore di Temperature: alla fine lo rimettete com’era.

Temperature la conoscete: è la manopola di Transformer Explainer. Il docente la mostra dal proiettore con una richiesta diversa dalla vostra: «Scrivi il nome di una pizza nuova, in poche parole.», tre volte, con Temperature a 1,5. Prima di guardare, alzata di mano: le tre risposte saranno uguali o diverse?

Poi tocca a voi. Aprite una nuova chat. Portate Temperature a 1,5. Scrivete: «Continua con poche parole: Nel mio laboratorio ho trovato». Inviate e rigenerate la risposta due volte: il docente vi fa vedere dove. Confrontate queste tre risposte: quante sono diverse?

Altre due manopole le mostra il docente dal proiettore, sempre con la pizza. Prima di ogni prova, alzata di mano: con **Top K a 1** (Temperature resta a 1,5), le tre risposte saranno uguali o diverse? E con **Top P a 0,1**?

Che cosa fa ogni manopola lo dice il docente dopo le prove, con una tabella proiettata. Poi rimettete Temperature com’era.

### 2C · Le istruzioni di sistema

Il campo **System Prompt** è il testo che il modello legge prima di ogni vostro messaggio. Sono vere istruzioni di sistema: il modello le legge come regole, non come una richiesta. A sinistra un esempio; a destra le domande a cui rispondete voi:

| Domanda | Esempio | Voi |
| --- | --- | --- |
| Che cosa cambia? | il tono | Il tono, la lunghezza o la forma? |
| Che cosa scrivete? | «Sei un cuoco burbero. Rispondi in una frase.» | Le vostre due righe. |
| Che cosa chiedete? | «Quanto ci vuole per una pizza?» | Due domande diverse. |

1. Scrivete le vostre istruzioni nel campo System Prompt.
2. In una nuova chat fate le due domande, una dopo l’altra. Il modello segue le istruzioni anche alla seconda?
3. Se non le segue, correggete una frase e riprovate. Non peggiorate le istruzioni per far sbagliare il modello. Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.
4. Alla fine cancellate il testo dal campo System Prompt.

## Parte 3 · opencode

opencode è un programma che si usa nella finestra nera: scrivete una richiesta e guardate che cosa fa.

Sul desktop del computer virtuale c’è il collegamento **opencode**: fate doppio clic. Parte nella cartella `laboratorio`, dove ci sono quattro file:

| File | Che cosa contiene |
| --- | --- |
| `inventario.csv` | i componenti del laboratorio, uno per riga; `.csv` vuol dire che i valori sono separati da virgole |
| `appunti_riunione.txt` | le note di una riunione |
| `da_fare.txt` | cinque cose da fare questa settimana |
| `opencode.jsonc` | le regole dei permessi di opencode: non modificatelo |

Il modello di opencode è Big Pickle: risponde dalla rete, attraverso il servizio di chi fa opencode. Non scrivete dati personali. Sotto il logo può comparire un avviso di aggiornamento: ignoratelo.

Quando compare **Permission required**, opencode vuole il vostro permesso. Se vuole eseguire un comando (un’istruzione per Windows), leggete il comando che opencode mostra e confrontatelo con questo, l’unico che potete approvare:

`Get-ChildItem -Force | Select-Object Mode, Length, Name`

Confrontate tutto il comando, dall’inizio alla fine, lettera per lettera. Contano anche i simboli: i trattini (-), la barra verticale (|) e le virgole. Non deve esserci niente in più, né prima né dopo. Uno spazio in più o in meno non conta: «Mode,Length,Name» va bene come «Mode, Length, Name».

Scegliete così:

| Che cosa chiede | Che cosa scegliete |
| --- | --- |
| di scrivere un file con il nome che avete chiesto voi | **Allow once** |
| di eseguire il comando qui sopra, uguale lettera per lettera | **Allow once** |
| qualunque altro comando, anche se cambia un solo simbolo o c’è qualcosa in più | **Reject** |

Non scegliete mai «Always allow»: salva la regola e il programma non chiede più. Se avete rifiutato un comando e opencode si ferma senza rispondere, inviate di nuovo la richiesta aggiungendo: «Senza comandi, leggi i file.» Se compare di nuovo un comando diverso, alzate la mano.

### 3A · Chi apre i file?

Scrivete: «Che file ci sono in questa cartella e di che cosa parlano?» Prima di inviare, decidete: chi apre i file, il modello o il programma? Alzata di mano.

Poi guardate i passaggi: le righe con una freccia che opencode scrive mentre lavora. Quante letture ha fatto?

### 3B · Una pagina fatta da opencode

Un esempio con un altro caso: «Crea listino.html con il listino delle pizze in una tabella. Titolo "Le nostre pizze", intestazione rossa.» (`.html` è il formato delle pagine web.)

Ora tocca a voi. Scrivete una richiesta per una pagina `inventario.html` con i dati di `inventario.csv` in una tabella. Scegliete voi il titolo, il colore dell’intestazione e una cosa da mettere in evidenza. Scrivetela nel campo di opencode, senza inviarla.

1. Premete Maiusc+Tab (sullo schermo si legge shift+tab): in basso compare **Plan**.
2. Prima di inviare, decidete: in Plan comparirà il file? Poi inviate la richiesta.
3. Premete Maiusc+Tab: torna **Build**.
4. Inviate di nuovo la stessa richiesta.
5. Compare «Permission required» per scrivere il file: scegliete **Allow once**. Se dopo la scrittura chiede un comando, anche quello scritto all’inizio della parte 3, scegliete **Reject**: il file è già scritto e non serve inviare di nuovo la richiesta.
6. Aprite Esplora file, Documenti › laboratorio. Se vedete due file chiamati inventario, quello con la pagina web è `inventario.html`: doppio clic.
7. Contate le righe della tabella con un componente. Poi aprite `inventario.csv` (tasto destro › Apri con › Blocco note) e contate le righe con un componente. Sono le stesse? C’è quello che avete chiesto?

**Plan** guarda e propone, **Build** esegue: in Plan il programma non scrive nessun file.

### 3C · Dire di no

Scrivete in Build: «Crea riassunto.txt con i punti principali di appunti_riunione.txt.» Prima di inviare, decidete: dopo un Reject, opencode vi darà comunque il riassunto a parole? Quando compare il permesso, scegliete **Reject**. Non inviate di nuovo la richiesta: guardate che cosa succede.

Che cosa scrive opencode? Aprite Esplora file: `riassunto.txt` c’è?

### 3D · Una richiesta vostra

Ora decidete voi che cosa chiedere a opencode. Usate due dei file della cartella e fatevi creare un file nuovo. Esempi di un altro caso, una pizzeria:

| Che cosa | Nella pizzeria |
| --- | --- |
| mettere insieme due file | «Leggi listino.txt e ordine.txt e scrivi in conto.txt quanto costa l'ordine.» |
| scegliere e riordinare | «Da listino.txt scrivi in economiche.txt le pizze sotto 8 euro, dalla più cara.» |
| mettere a confronto | «Confronta note_serata.txt e ordine.txt e scrivi in mancanti.txt gli ingredienti che mancano.» |

1. Scrivete la richiesta nel campo di opencode. Prima di inviare, decidete: che cosa deve contenere il file nuovo?
2. Inviate. Quando compare il permesso, leggete che file vuole scrivere: se è quello che avete chiesto, scegliete **Allow once**. Se chiede un comando prima di scrivere il file, valgono le regole scritte all’inizio della parte 3. Se lo chiede dopo, scegliete **Reject** come nella 3B, senza inviare di nuovo la richiesta.
3. Aprite il file nuovo e confrontate un dato scelto da voi con il file originale: è uguale? Se non torna, correggete la richiesta e riprovate.

### Dove sono le regole?

Nel file `opencode.jsonc` della cartella. Il docente ve lo proietta e vi fa vedere queste righe:

| Dove | Che cosa | Regola | Che cosa fa il programma |
| --- | --- | --- | --- |
| Build | scrivere un file | ask | si ferma e chiede a voi |
| Build e Plan | eseguire un comando | ask | si ferma e chiede a voi |
| Plan | scrivere un file | deny | non esegue |
| sempre | leggere un file | nessuna regola | lo fa senza chiedere: è allow |

I permessi sono tre: **allow** esegue, **ask** si ferma e chiede a voi, **deny** non esegue. **Allow once** approva una volta sola; «Always allow» trasforma ask in allow per sempre.

### Che cosa avete visto

Quale dei tre risponde senza rete? Quale apre i file da solo? Pensateci: il docente proietta poi la tabella con Copilot, Studio e opencode.

Il modello decide che cosa chiedere; il programma agisce e chiede il permesso.

## Alla fine

Un programma come opencode potrebbe anche cancellare un file: allow, ask o deny? Perché? Prima di chiudere salvate `istruzioni_agente_noleggio.txt`. Non dovete consegnarlo.

## Se qualcosa non va

Se Copilot non è disponibile, usate una conversazione normale: nel primo messaggio incollate le vostre istruzioni, poi documenti e richiesta. Non sono vere istruzioni di sistema.

Se il computer virtuale non parte, Studio non risponde o opencode non risponde dalla rete, alzate la mano: il docente fa la prova dal proiettore e voi proponete la richiesta.

## I programmi usati

Unsloth Studio: licenza AGPL-3.0 (il testo è nella cartella `studio` dell’installazione, versione 2026.11.4). Qwen3.5-2B: licenza Apache 2.0, come dichiara la scheda del modello su Hugging Face. opencode: licenza MIT. Big Pickle è un modello gratuito di OpenCode, offerto per un tempo limitato: quello che scrivete arriva a chi offre il modello e può servire a migliorarlo. I documenti della cartella `laboratorio` sono inventati per questa esercitazione.
