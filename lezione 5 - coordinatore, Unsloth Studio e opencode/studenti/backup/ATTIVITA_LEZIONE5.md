# Lezione 5 · Un agente che fa il piano

**ITS MAKER Bologna · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

## Da dove partiamo

Il titolare di Ruota Libera ha provato il vostro agente e chiede due cose:

> «Quando ti chiedo due cose insieme, voglio vedere il piano prima della risposta. E accanto a ogni numero voglio sapere da quale riga viene.»

Ognuno lavora da solo sul proprio computer. Nella parte 1 partite dal file della lezione 4: `istruzioni_agente_noleggio.txt`. Non avete il file? Ve ne diamo uno di partenza. Non ci sono file da consegnare: il risultato si guarda sullo schermo. Salvate solo il file delle istruzioni, aggiornato.

Il percorso è questo:

| Passo | Dove | Che cosa succede |
| --- | --- | --- |
| 1 | Microsoft Copilot | al vostro testo aggiungete il piano e il controllo |
| 2 | Unsloth Studio, nel computer virtuale | un modello nel computer virtuale: serve la rete? |
| 3 | opencode, nel computer virtuale | un programma accanto ai file: chi li apre? |

## Riaprite il vostro agente

1. Aprite Blocco note e il file `istruzioni_agente_noleggio.txt`.
2. Aprite Microsoft Copilot, con l'account scolastico, e il vostro agente. Se non c'è, usate una conversazione normale: nel primo messaggio incollate le istruzioni.
3. Scaricate da Teams i tre testi del noleggio: registro, regole del noleggio e guida ai guasti.
4. In una nuova conversazione scrivete un solo messaggio: registro, regole del noleggio e in fondo la richiesta: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»
5. Controllate gli orari con il registro.

## Parte 1 · Due cose nuove per il vostro agente

### 1A · Il piano prima della risposta

Il titolare vuole vedere che cosa farà l'agente prima che lo faccia. Un **piano** è l'elenco dei lavori, nell'ordine in cui l'agente li userà, con i dati che mancano. Dopo il piano l'agente si ferma e aspetta.

La regola di una pizzeria d'asporto, proiettata:

> «Se la richiesta ha due o più lavori, scrivi prima "Piano:" con i lavori nell'ordine in cui li usi e i dati che mancano. Poi fermati e aspetta la parola "Procedi".»

La richiesta alla pizzeria: «La pizza è arrivata fredda e voglio i soldi indietro.» Per alzata di mano: dopo il piano, l'agente si ferma? Poi si risponde al piano: «Procedi, ma solo il reclamo.» Che cosa deve fare adesso? Che cosa non deve fare?

Ora scrivete la regola del piano per il noleggio, nelle **regole per tutti i casi**. A destra le domande a cui rispondete voi:

| Domanda | Pizzeria | Noleggio |
| --- | --- | --- |
| Quando scatta? | «due o più lavori» | Per quali richieste? |
| Che cosa contiene? | lavori in ordine, dati che mancano | E i testi che userà? |
| Dove si ferma? | dopo il piano | Qual è il segno? |
| Che parola lo fa ripartire? | «Procedi» | La scegliete voi |
| E «Lavoro usato:»? | Dopo il piano | Il piano viene prima: correggete la regola della prima riga. |

Salvate il file e aggiornate l'agente. Poi, in una nuova conversazione, registro, regole del noleggio e in fondo la richiesta che corrisponde al vostro secondo lavoro. Siete partiti dalle istruzioni di partenza? Scegliete voi GUASTI o PASSAGGIO.

| Il vostro secondo lavoro | Richiesta |
| --- | --- |
| GUASTI (aggiungete anche la guida ai guasti) | «Bici 12, sabato: quanto è stata fuori servizio, e che cosa significa freni che non tengono?» |
| PASSAGGIO | «Bici 12, sabato: quanto è stata fuori servizio? Scrivi la nota per il turno dopo.» |

Prima di inviare, decidete che piano vi aspettate. Poi controllate: il piano viene prima di qualsiasi risposta ai lavori? I lavori sono nell'ordine che avevate deciso? Dice quali testi usa? Si ferma? Dopo «Procedi» risponde?

Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.

### 1B · Ogni numero, la sua riga

Il titolare vuole sapere da dove viene ogni numero. La regola della pizzeria, proiettata:

> «In fondo alla risposta scrivi "Controllo:" e, per ogni numero della risposta, la riga delle istruzioni da cui viene. Se non la trovi, scrivi "Non trovato".»

La richiesta alla pizzeria: «Quanto costa una Diavola con la consegna?» Dove cercate la riga che il controllo cita? Poi, dal proiettore, le istruzioni della pizzeria.

Scrivete la regola per il noleggio:

| Domanda | Pizzeria | Noleggio |
| --- | --- | --- |
| Che cosa controlla? | «ogni numero della risposta» | Solo i numeri, o anche gli orari? |
| Che cosa scrive? | «la riga delle istruzioni» | Quale testo? Con quale data e ora? |
| E se non trova la riga? | «Non trovato» | Che cosa fa? |

Poi la prova: aggiornate l'agente e aprite una nuova conversazione, con gli stessi testi e la stessa richiesta con due lavori della prova del piano. Prima di inviare: quale riga citerà il controllo per i minuti di fuori servizio? Quando l'agente scrive il piano, rispondete «Procedi». Se per PASSAGGIO chiede il turno: «La nota è per chi inizia il pomeriggio di sabato.»

Poi controllate gli orari e i minuti di fuori servizio proiettati. Scegliete un numero della risposta e cercate nel registro o nelle regole del noleggio la riga che l'agente cita: esiste davvero? Dice quello che l'agente dice? Un controllo con una riga inventata è peggio di nessun controllo.

### Salvate il file

Aggiornate l'agente in Copilot e controllate che il testo sia arrivato intero. Il file `istruzioni_agente_noleggio.txt` deve contenere tutto: regole per tutti i casi con piano e controllo, i lavori, l'elenco delle richieste, lo stile.

### Chi ha fatto che cosa

Scegliere i lavori, decidere l'ordine, fermarsi a chiedere, controllare: questo lavoro si chiama **coordinare**. Il vostro agente ha un coordinatore. Dove sta?

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

Quando compare **Permission required**, opencode vuole il vostro permesso. Se chiede di eseguire un comando (un’istruzione per Windows), un comando che può comparire è questo:

`Get-ChildItem -Force | Select-Object Mode, Length, Name`

Scegliete così:

| Che cosa chiede | Che cosa scegliete |
| --- | --- |
| di scrivere un file con il nome che avete chiesto voi | **Allow once** |
| di eseguire il comando scritto sopra, con le stesse parole e gli stessi simboli, nello stesso ordine (gli spazi non contano) | **Allow once** |
| qualunque altro comando | **Reject** |

Non scegliete mai «Always allow»: salva la regola e il programma non chiede più. Se dopo un Reject opencode si ferma, inviate di nuovo la richiesta aggiungendo: «Senza comandi, leggi i file.» Se compare di nuovo un comando diverso, alzate la mano.

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
5. Compare «Permission required» per scrivere il file: scegliete **Allow once**. Se dopo la scrittura chiede un comando di controllo, scegliete **Reject**: il file è già scritto.
6. Aprite Esplora file, Documenti › laboratorio. Se vedete due file chiamati inventario, quello con la pagina web è `inventario.html`: doppio clic.
7. Contate le righe della tabella con un componente. Poi aprite `inventario.csv` (tasto destro › Apri con › Blocco note) e contate le righe con un componente. Sono le stesse? C’è quello che avete chiesto?

**Plan** guarda e propone, **Build** esegue: in Plan il programma non scrive nessun file.

### 3C · Dire di no

Scrivete in Build: «Crea riassunto.txt con i punti principali di appunti_riunione.txt.» Prima di inviare, decidete: dopo un Reject, opencode vi darà comunque il riassunto a parole? Quando compare il permesso, scegliete **Reject**.

Che cosa scrive opencode? Aprite Esplora file: `riassunto.txt` c’è?

### 3D · Una richiesta vostra

Ora decidete voi che cosa chiedere a opencode. Usate due dei file della cartella e fatevi creare un file nuovo. Esempi di un altro caso, una pizzeria:

| Che cosa | Nella pizzeria |
| --- | --- |
| mettere insieme due file | «Leggi listino.txt e ordine.txt e scrivi in conto.txt quanto costa l'ordine.» |
| scegliere e riordinare | «Da listino.txt scrivi in economiche.txt le pizze sotto 8 euro, dalla più cara.» |
| mettere a confronto | «Confronta note_serata.txt e ordine.txt e scrivi in mancanti.txt gli ingredienti che mancano.» |

1. Scrivete la richiesta nel campo di opencode. Prima di inviare, decidete: che cosa deve contenere il file nuovo?
2. Inviate. Quando compare il permesso, leggete che file vuole scrivere: se è quello che avete chiesto, scegliete **Allow once**. Se chiede un comando, valgono le regole scritte sopra.
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
