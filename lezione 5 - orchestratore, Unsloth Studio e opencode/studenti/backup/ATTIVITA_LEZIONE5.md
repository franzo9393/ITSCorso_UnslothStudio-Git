# Lezione 5 · Chi controlla che cosa?

**ITS MAKER Bologna · 19 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

## Da dove partiamo

Il titolare di Ruota Libera ha provato il vostro agente e vuole che sappia fare tutti e tre i lavori: fuori servizio, guasti e passaggio di turno. Oggi completate l'agente e controllate che scelga il lavoro giusto.

Ognuno lavora da solo sul proprio computer. Nella parte 1 partite dal file della lezione 4: `istruzioni_agente_noleggio.txt`. Non avete il file? Chiedete il testo di partenza, poi salvatelo con quel nome: ha già i tre lavori. Non ci sono file da consegnare: il risultato si guarda sullo schermo. Salvate solo il file delle istruzioni, aggiornato.

Oggi usate tre strumenti:

- Microsoft Copilot: il vostro agente con più lavori.
- Unsloth Studio, nel computer virtuale: un modello che gira sul vostro computer.
- opencode, nel computer virtuale: un programma che lavora sui file.

## Riaprite il vostro agente

1. Aprite Blocco note e il file `istruzioni_agente_noleggio.txt`.
2. Aprite Microsoft Copilot, con l'account scolastico, e il vostro agente. Se non c'è, usate una conversazione normale: scrivete un solo messaggio con prima le vostre istruzioni, poi registro, regole, guida e richiesta.
3. Scaricate da Teams i tre testi del noleggio: registro, regole del noleggio e guida ai guasti.
4. In una nuova conversazione scrivete un solo messaggio: registro, regole del noleggio e in fondo la richiesta: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»
5. Controllate gli orari con il registro.

## Parte 1 · Un agente con più lavori

### 1A · Le due parti dell'agente

Il testo del vostro agente ha due parti: l'**elenco delle richieste**, che dice a quale lavoro va ogni richiesta, e i **lavori**, ognuno con le sue regole. Aprite `istruzioni_agente_noleggio.txt` e cercatele. Non avete il file? Chiedete il testo di partenza: ha già i tre lavori. Un esempio dal testo di partenza (i tagli sono segnati con […]):

| L'elenco dice | Il lavoro dice |
| --- | --- |
| «Quanto è stata fuori servizio una bici, minuti senza bici, rimborso per un guasto → FUORI SERVIZIO» | «Quando: serve la durata di un fuori servizio, i minuti senza bici di un cliente o un rimborso. […]» |

### 1B · Il lavoro che manca

Nel vostro file ci sono FUORI SERVIZIO e un secondo lavoro. Scrivete quello che manca: GUASTI se avete PASSAGGIO, PASSAGGIO se avete GUASTI. Avete solo FUORI SERVIZIO? Scrivete prima PASSAGGIO, poi GUASTI. Servono una voce nell'elenco e il lavoro, nel file `istruzioni_agente_noleggio.txt`. Accanto all'esempio di FUORI SERVIZIO, le domande a cui rispondete voi:

| Che cosa scrivete | Esempio: FUORI SERVIZIO | Il lavoro che manca |
| --- | --- | --- |
| Voce nell'elenco | «Quanto è stata fuori servizio una bici, minuti senza bici, rimborso per un guasto → FUORI SERVIZIO» | Quali parole della richiesta la fanno scegliere? |
| Quando serve? | «serve la durata di un fuori servizio, i minuti senza bici di un cliente o un rimborso» | Che cosa serve a chi chiede? |
| Che testo usa? | «le regole del noleggio e il registro» | Quale testo? |
| Come risponde? | «i due orari usati, la sottrazione e il risultato in minuti» | In quale forma? |

Salvate il file. Nelle istruzioni del vostro agente, in Copilot, cancellate il testo vecchio, incollate tutto il file e salvate l'agente. Poi controllate che l'ultima riga sia la stessa nel file e in Copilot: se coincide, il testo è entrato tutto.

### 1C · Una richiesta per lavoro

Una nuova conversazione per ogni richiesta: registro, regole del noleggio, guida ai guasti e in fondo la richiesta. Le tre richieste, una per conversazione:

- «Bici 12, sabato: per quanti minuti è rimasto senza bici il cliente?»
- «Che cosa significa freni che non tengono?»
- «Scrivi la nota per il turno dopo, sabato.»

Dopo le tre prove, guardate la prima riga di ogni risposta: «Lavoro usato:». Le tre richieste vanno, nell'ordine, a FUORI SERVIZIO, GUASTI e PASSAGGIO. Controllate il nome e il contenuto: FUORI SERVIZIO deve mostrare l'ora in cui il cliente segnala il guasto, l'ora in cui riceve un'altra bici (nelle regole del noleggio, «Minuti senza bici») e i minuti, GUASTI le parole della guida, PASSAGGIO la nota con i titoli scritti nel vostro PASSAGGIO e gli orari del registro. Lavoro sbagliato? Correggete nel file la voce dell'elenco: la vostra richiesta somiglia alle sue parole? Lavoro giusto ma risposta sbagliata? Correggete il lavoro: il testo da usare o come rispondere. Poi aggiornate l'agente e riprovate in una nuova conversazione. Se l'agente vi fa una domanda, rispondete nella stessa conversazione. Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.

### 1D · Dove sono finiti i dati?

In Copilot avete incollato un registro inventato. Se fosse stato il registro vero di un’azienda, dove sarebbero finiti quei dati? Rispondete a voce. Più avanti vi farete la stessa domanda per Studio e per opencode.

### 1E · Due lavori in catena

Richiesta: «Bici 12, sabato: per quanti minuti è stata fuori servizio? Scrivi la nota per il turno dopo.»

Nel vostro elenco deve esserci una voce per FUORI SERVIZIO e PASSAGGIO insieme: prima FUORI SERVIZIO, poi il risultato entra nella nota. Non c'è? Scrivetela e aggiornate l'agente. Poi inviate la richiesta, in una nuova conversazione con registro, regole e guida.

Confrontate la vostra risposta con il numero e gli orari proiettati, calcolati dal registro. La sottrazione usa quei due orari? La nota, dove parla del fuori servizio della bici 12, riporta lo stesso numero? Se i minuti sono già sbagliati nella sottrazione, correggete il lavoro FUORI SERVIZIO. Se sono giusti lì e sbagliati nella nota, correggete la voce dei due lavori insieme. Se tutto torna, va bene così; se avete corretto, aggiornate l'agente e riprovate.

### Salvate il file

Controllate che il file `istruzioni_agente_noleggio.txt` abbia: le regole per tutti i casi, l'elenco delle richieste con le vostre correzioni, i tre lavori e lo stile. Studio e opencode usano altri testi, ma salvatelo: serve anche nelle prossime lezioni.

### Chi ha controllato il numero?

Copilot ha scelto il lavoro e ha scritto la nota. E il numero: chi l'ha confrontato con il registro? Nel testo di partenza la voce «PASSAGGIO e FUORI SERVIZIO insieme: prima FUORI SERVIZIO, poi il risultato entra nella nota di PASSAGGIO» dice quale lavoro usare, in che ordine e che cosa passa dall'uno all'altro. Un elenco così si chiama orchestratore. Con opencode, più avanti, un programma vi chiederà il permesso prima di agire: è un altro controllo, sulle azioni.

## Parte 2 · Un modello sul vostro computer

Passate al computer virtuale: un computer dentro il computer, con il suo Windows e i suoi programmi. Ognuno ha il suo. Unsloth Studio è il programma che carica un modello e vi lascia parlarci.

### Da dove viene il modello

Unsloth Studio ha preso il modello da **Hugging Face**: un sito pubblico dove si pubblicano modelli, anche versioni di modelli fatti da altri. Prima di scaricarne uno, lì si legge chi l’ha pubblicato, con quale licenza (che cosa ne potete fare) e quanto pesano i file. Guardate sulla slide la pagina di un altro modello, `bartowski/Llama-3.2-1B-Instruct-GGUF`, con quattro punti cerchiati: chi l’ha pubblicato, la licenza, il file più piccolo e il più grande.

Poi cercate il vostro. Nel browser del computer virtuale scrivete l’indirizzo `https://huggingface.co/unsloth/Qwen3.5-2B-GGUF` e trovate le stesse quattro cose: chi l’ha pubblicato, la licenza, il file più piccolo e il più grande. I file sono nell’elenco a destra della pagina, sotto «Hardware compatibility». GGUF è il tipo di file che legge Studio.

Lo stesso modello ha tanti file, uno per dimensione.

### Aprite Studio

Chiudete la pagina di Hugging Face.

1. Fate doppio clic sul collegamento **Unsloth Studio** del desktop: si apre il browser.
2. In alto deve esserci il nome del modello, Qwen3.5-2B-GGUF. Se non c’è, scegliete Select model › On Device › Qwen3.5-2B-GGUF e aspettate che si carichi.
3. Accanto c’è una finestra nera con del testo che scorre: non chiudetela, o Studio si ferma. Se compare un avviso di aggiornamento, scegliete «Remind me later» o «Più tardi»: non aggiornate.

Il modello si chiama Qwen3.5-2B: «2B» vuol dire due miliardi di pesi, i numeri che ha imparato.

### 2A · Serve Internet?

1. Pensate: per rispondere, questo modello ha bisogno di Internet?
2. Con il pulsante **Nuova chat** (o **New Chat**), a sinistra, aprite una chat. Scrivete: «In una frase: a che cosa serve un cacciavite?» Leggete la risposta.
3. Togliete la rete al computer virtuale.
4. In una nuova chat rifate la stessa domanda. Risponde ancora?
5. Riattivate la rete: serve tra poco a opencode.

Ora guardate dove gira il modello:

| | Copilot | Studio |
| --- | --- | --- |
| Dove gira il modello | in rete, sui computer di Microsoft | sul vostro computer virtuale |
| Il programma | il codice non si può leggere | il codice è aperto: si può leggere |
| Dove vanno i dati che scrivete | in rete, al servizio di Microsoft | il modello li legge sul vostro computer, anche senza rete |
| Di chi è | di Microsoft | una copia sul vostro computer: la licenza che avete letto dice che cosa potete farne |

Il modello di Studio gira sul processore del vostro computer, non su macchine grandi: per questo può rispondere piano. Guardate poi sul proiettore la domanda sul cacciavite, fatta a Copilot: che cosa cambia rispetto alla vostra risposta?

### 2B · I parametri del modello

Il pannello delle impostazioni si apre con l’icona in alto a destra, nella figura della slide. Scorretelo: trovate **System Prompt**, **Temperature** e **Context Length** (la quantità di testo che il modello riesce a tenere insieme). Quale numero c’è accanto a Context Length? Non toccatelo. Guardate anche il valore di Temperature: alla fine lo rimettete com’era.

Temperature la conoscete: è un parametro, come in Transformer Explainer. Prima di guardare: con Temperature a 1,5, le tre risposte saranno uguali o diverse? Poi guardate sul proiettore una richiesta diversa dalla vostra: «Scrivi il nome di una pizza nuova, in poche parole.», tre volte.

Poi tocca a voi. Aprite una nuova chat. Portate Temperature a 1,5. Scrivete: «Continua con poche parole: Nel mio laboratorio ho trovato». Inviate e rigenerate la risposta due volte. Confrontate queste tre risposte: quante sono diverse?

Sulla slide c’è poi la tabella dei tre parametri: Temperature, Top K e Top P. Top K e Top P non li provate. Rimettete Temperature com’era.

### 2C · System prompt

Il campo **System Prompt** è il testo che il modello legge prima di ogni vostro messaggio: lo legge come regole, non come una richiesta. A sinistra un esempio; a destra le domande a cui rispondete voi:

| Domanda | Esempio | Voi |
| --- | --- | --- |
| Che cosa cambia? | il tono | Il tono, la lunghezza o la forma? |
| Che cosa scrivete? | «Sei un cuoco burbero. Rispondi in una frase.» | Le vostre due righe. |
| Che cosa chiedete? | «Quanto ci vuole per una pizza?» | Due domande diverse. |

1. Scrivete le vostre istruzioni nel campo System Prompt.
2. In una nuova chat fate le due domande, una dopo l’altra. Il modello segue le istruzioni anche alla seconda?
3. Se non le segue, correggete una frase e riprovate. Non peggiorate le istruzioni per far sbagliare il modello. Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.
4. Alla fine cancellate il testo dal campo System Prompt.

### 2D · Quanto testo tiene insieme il modello?

Il Context Length della vostra copia di Studio è 8192. Si misura in **token**: pezzetti di parola. Registro, regole e istruzioni del noleggio, insieme, ne occupano circa 3.700.

Prima di guardare: il messaggio supera 8192, che cosa farà Studio? Poi guardate il proiettore: un testo lungo e una domanda su una frase che sta all’inizio.

## Parte 3 · opencode

opencode è un programma che si usa nella finestra nera: scrivete una richiesta e guardate che cosa fa.

Sul desktop del computer virtuale c’è il collegamento **opencode**: fate doppio clic. Parte nella cartella `laboratorio`, dove ci sono tre file di lavoro e il file delle regole:

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

Scrivete: «Che file ci sono in questa cartella e di che cosa parlano?» Prima di inviare: chi apre i file, il modello o il programma?

Poi guardate i passaggi: le righe con una freccia che opencode scrive mentre lavora. Quante letture ha fatto?

### 3B · Una pagina fatta da opencode

Un esempio con un altro caso: «Crea listino.html con il listino delle pizze in una tabella. Titolo "Le nostre pizze", intestazione rossa.» (`.html` è il formato delle pagine web.)

Ora tocca a voi. Scrivete una richiesta per una pagina `inventario.html` con i dati di `inventario.csv` in una tabella. Scegliete voi il titolo, il colore dell’intestazione e una cosa da mettere in evidenza. Scrivetela nel campo di opencode, senza inviarla.

1. Premete Maiusc+Tab (sullo schermo si legge shift+tab): in basso compare **Plan**.
2. Prima di inviare, decidete: in Plan comparirà il file? Poi inviate la richiesta.
3. Premete Maiusc+Tab: torna **Build**.
4. Riscrivete la stessa richiesta e inviatela.
5. Compare «Permission required» per scrivere il file. Prima di scegliere, leggete il nome del file e il testo che vuole scrivere: c’è il titolo che avete scelto? Poi scegliete **Allow once**. Se dopo la scrittura chiede un comando, anche quello scritto all’inizio della parte 3, scegliete **Reject**: il file è già scritto e non serve inviare di nuovo la richiesta.
6. Aprite Esplora file, Documenti › laboratorio. Se vedete due file chiamati inventario, quello con la pagina web è `inventario.html`: doppio clic.
7. Contate le righe della tabella con un componente. Poi aprite `inventario.csv` (tasto destro › Apri con › Blocco note) e contate le righe con un componente. Sono le stesse? C’è quello che avete chiesto?

**Plan** guarda e propone, **Build** esegue: in Plan il programma non scrive nessun file.

### 3C · Dire di no

Scrivete in Build: «Crea riassunto.txt con i punti principali di appunti_riunione.txt.» Prima di inviare: dopo un Reject, opencode vi darà comunque il riassunto a parole? Quando compare il permesso, scegliete **Reject**. Non inviate di nuovo la richiesta: guardate che cosa succede.

Che cosa scrive opencode? Aprite Esplora file: `riassunto.txt` c’è?

### 3D · Una richiesta vostra

Ora decidete voi che cosa chiedere a opencode. Usate due dei file della cartella e fatevi creare un file nuovo. Esempi di un altro caso, una pizzeria:

| Che cosa | Nella pizzeria |
| --- | --- |
| mettere insieme due file | «Leggi listino.txt e ordine.txt e scrivi in conto.txt quanto costa l'ordine.» |
| scegliere e riordinare | «Da listino.txt scrivi in economiche.txt le pizze sotto 8 euro, dalla più cara.» |
| mettere a confronto | «Confronta note_serata.txt e ordine.txt e scrivi in mancanti.txt gli ingredienti che mancano.» |

1. Scrivete la richiesta nel campo di opencode. Prima di inviare, decidete: che cosa deve contenere il file nuovo?
2. Inviate. Quando compare il permesso, leggete il nome del file e il testo che vuole scrivere: c’è il dato che avete previsto? Poi scegliete **Allow once**. Se chiede un comando prima di scrivere il file, valgono le regole scritte all’inizio della parte 3. Se lo chiede dopo, scegliete **Reject** come nella 3B, senza inviare di nuovo la richiesta.
3. Aprite il file nuovo e confrontate un dato scelto da voi con il file originale: è uguale? Se non torna, correggete la richiesta e riprovate.

### Dove sono le regole?

Nel file `opencode.jsonc` della cartella. Ecco queste righe:

| Dove | Che cosa | Regola | Che cosa fa il programma |
| --- | --- | --- | --- |
| Build | scrivere un file | ask | si ferma e chiede a voi |
| Build e Plan | eseguire un comando | ask | si ferma e chiede a voi |
| Plan | scrivere un file | deny | non esegue |
| sempre | leggere un file | nessuna regola | lo fa senza chiedere: è allow |

I permessi sono tre: **allow** esegue, **ask** si ferma e chiede a voi, **deny** non esegue. **Allow once** approva una volta sola; «Always allow» trasforma ask in allow per sempre.

### Che cosa avete visto

Quale dei tre risponde senza rete? Quale apre i file da solo? Pensateci, poi guardiamo la tabella con Copilot, Studio e opencode.

Il modello decide che cosa chiedere; il programma agisce e chiede il permesso.

## Alla fine

Un programma come opencode potrebbe anche cancellare un file: allow, ask o deny? Perché? E il contenuto di un file nuovo: chi lo controlla? Prima di chiudere salvate `istruzioni_agente_noleggio.txt`. Non dovete consegnarlo.

## Se qualcosa non va

Se il vostro agente non è disponibile, usate una conversazione normale di Copilot: scrivete un solo messaggio con prima le vostre istruzioni, poi registro, regole, guida e richiesta. Le istruzioni in un messaggio non sono istruzioni dell'agente.

Se il computer virtuale non parte, Studio non risponde o opencode non risponde dalla rete, alzate la mano: la prova si fa dal proiettore e voi proponete la richiesta.

## I programmi usati

Unsloth Studio: licenza AGPL-3.0 (il testo è nella cartella `studio` dell’installazione, versione 2026.11.4). Qwen3.5-2B: la licenza è quella scritta nella pagina del modello su Hugging Face. opencode: licenza MIT. Big Pickle è un modello gratuito di OpenCode, offerto per un tempo limitato: quello che scrivete arriva a chi offre il modello e può servire a migliorarlo. I documenti della cartella `laboratorio` sono inventati per questa esercitazione.

Hugging Face: sito pubblico; le pagine dei modelli si leggono senza registrarsi. Ogni modello ha la sua licenza, scritta nella pagina: leggetela prima di usare un modello fuori da questa esercitazione.
