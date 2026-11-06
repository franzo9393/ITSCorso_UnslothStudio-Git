# Lezione 4 · Un assistente sul computer del reparto

**ITS MAKER Bologna · 12 novembre 2026 · Unsloth Studio nella macchina virtuale**

## Il caso

Il responsabile del reparto presse vi scrive:

> «I registri della pressa P03 non devono uscire dal reparto. Vorrei un assistente che lavori sul nostro computer, senza mandare i testi a un servizio esterno.»

Oggi installate Unsloth Studio, un programma che fa girare un modello di intelligenza artificiale dentro la vostra macchina virtuale. Poi scoprite quanta memoria occupa, come se ne regolano le risposte e come si scrivono le sue istruzioni.

Il testo di lavoro è il registro della P03 del 13–15 ottobre, che già conoscete: `Registro_P03_13-15_ottobre_2026.txt`. L'estensione `.txt` indica un file di testo semplice, che si apre con Blocco note.

## Come lavorate

- Siete in coppia, ma ognuno lavora sulla propria macchina virtuale e sul proprio computer reale.
- Il **computer reale** è quello fisico sul banco. La **macchina virtuale** è il computer simulato che si apre dentro una finestra, con Windows e Unsloth Studio.
- Unsloth Studio gira nella macchina virtuale. I siti internet della parte 2 si aprono nel browser del computer reale, per non togliere memoria alla macchina virtuale.
- Non consegnate nessun file. Scrivete tre file di testo come appunti vostri: `misure_VM.txt`, `istruzioni_assistente_P03.txt`, `casi_di_prova.txt`. Li scrivete con Blocco note **dentro la macchina virtuale** e li lasciate aperti: li riempite man mano durante la lezione. Salvate con Ctrl+S ogni volta che scrivete qualcosa.
- Mentre lavorate il docente passa tra i banchi: vi chiede di mostrare lo schermo e di raccontare che cosa avete fatto e perché.
- Il registro lo trovate su Teams. Scaricatelo sul computer reale, per la parte 2. Per la macchina virtuale lo trovate anche sulla chiavetta, insieme allo zip del modello; se non c'è, scaricatelo da Teams aprendolo nel browser della macchina virtuale. Se il copia e incolla tra i due computer funziona potete usarlo, ma non è necessario.

## Parte 1 · Installate Unsloth Studio

Lavorate nella macchina virtuale.

Aprite **PowerShell**: menu Start, scrivete `PowerShell`, premete Invio. Si apre una finestra, blu o nera, in cui si scrivono comandi.

Incollate questa riga e premete Invio. Se nella macchina virtuale non si incolla, scrivetela a mano, carattere per carattere, dalla slide proiettata. Dice a Windows di scaricare e avviare il programma di installazione di Unsloth Studio.

`$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex`

- Lasciate la finestra aperta. L'installazione scarica molti file e può metterci a lungo.
- Se compare un messaggio di errore in rosso, non chiudete la finestra: chiamate subito il docente, che deve leggerlo prima che sparisca.
- Mentre l'installazione procede, copiate dalla chiavetta sul Desktop della macchina virtuale lo zip del modello e il registro: il docente vi mostra come (chiavetta collegata alla macchina virtuale, oppure file trascinato nella sua finestra). Restituite subito la chiavetta. Se non avete la chiavetta o il registro non c'è, aprite Teams nel browser della macchina virtuale e scaricate il registro.
- Aprite Blocco note e salvate nella cartella Documenti tre file vuoti: `misure_VM.txt`, `istruzioni_assistente_P03.txt`, `casi_di_prova.txt`. Poi passate alla parte 2 sul computer reale.

## Parte 2 · Come risponde un modello

Lavorate nel browser del computer reale. Quello che scrivete va nei file di Blocco note della macchina virtuale.

### A · Come sceglie la parola successiva

1. Aprite Transformer Explainer: `poloclub.github.io/transformer-explainer`. È un modello molto piccolo che completa frasi in inglese. Non è un assistente: non risponde a domande.
2. Scrivete una frase breve in inglese e guardate quali parole propone dopo, con le loro probabilità.
3. Prima di toccare il cursore della **temperatura**, scrivete in `misure_VM.txt`, sotto il titolo «Previsioni»: che cosa pensate che succeda alle probabilità se la alzate? E se la abbassate? Dite la previsione a voce al compagno.
4. Provate. Scrivete sotto la previsione che cosa avete visto davvero e spiegatelo al compagno.

Qui non c'è una risposta sbagliata da trovare: si guardano le probabilità.

### B · Quanto pesa il testo

Un modello non legge le parole intere: le divide in pezzi chiamati **token**. Più token ci sono, più lavoro deve fare.

1. Aprite The Tokenizer Playground: `huggingface.co/spaces/Xenova/the-tokenizer-playground`.
2. Aprite `Registro_P03_13-15_ottobre_2026.txt`, copiate tutto il testo e incollatelo nella pagina. Il **tokenizzatore** è il metodo con cui un modello divide il testo in token: si sceglie dal menu in alto nella pagina. Scrivete in `misure_VM.txt`, sotto il titolo «Token», il nome del tokenizzatore che avete scelto e quanti token risultano.
3. Scrivete voi una versione più breve del registro, che tenga gli stessi fatti importanti: cancellate il testo incollato e riscrivetelo più breve direttamente nella casella della pagina. Scrivete in `misure_VM.txt` il nuovo numero di token.
4. Leggete la versione breve del compagno sul suo schermo. Quale fatto importante ha tolto? Scrivetelo sotto «Token».

Se l'installazione non è finita quando avete terminato la parte 2, avvisate il docente.

## Parte 3 · Il modello sul vostro computer

Tornate nella macchina virtuale.

### A · Primo avvio

1. Quando l'installazione finisce, PowerShell chiede se avviare Unsloth Studio. Scrivete `Y` e premete Invio. Non chiudete questa finestra: se la chiudete, Studio si ferma.
2. Nel browser della macchina virtuale aprite `http://127.0.0.1:8888`. Al primo avvio vi chiede di creare una password di almeno 8 caratteri. Scrivetela su un foglio: serve ogni volta che riaprite Studio.
3. Se avete aperto Teams nel browser della macchina virtuale, chiudete la scheda. Aprite **Gestione attività** con i tasti Ctrl+Maiusc+Esc, scheda **Prestazioni**, voce **Memoria**. Scrivete in `misure_VM.txt`, sotto il titolo «Misure», la memoria in uso **prima** di caricare il modello.
4. Se avete lo zip del modello sul Desktop, aprite Esplora file e scrivete `%USERPROFILE%\.cache\huggingface\hub` nella barra dell'indirizzo. Se la cartella non esiste, createla un passo alla volta: `.cache`, poi `huggingface`, poi `hub`. Estraete lo zip dentro `hub`: se Windows propone una sottocartella con il nome dello zip, toglietela dal percorso. Controllate che dentro `hub` compaia la cartella `models--unsloth--Qwen3.5-2B-GGUF`.
5. Tenete aperta Gestione attività. **Context Length** è il numero massimo di token che il modello tiene presenti (lo trovate in Run settings, vedi 3B). Prima di cliccare **Select model** aspettate l'indicazione del docente.
6. Cliccate **Select model**. Se avete estratto lo zip, aprite **On Device**. Se non avete lo zip, aspettate il docente: il modello si scarica dalla rete solo su alcune macchine virtuali, perché la rete è la stessa per tutti.
7. Quando il modello si carica, se la memoria arriva quasi al massimo o la finestra non risponde, chiudete la finestra di PowerShell in cui gira Studio, scrivete «bloccato» nella prima riga della tabella di 3B, al posto della stima e della memoria, e avvisate il docente. Non cliccate di nuovo **Select model**: aspettate le sue indicazioni.
8. Nella casella dove scrivete i messaggi ci sono **Search** e **Tools**: all'inizio sono attivi (verdi). Cliccateli: devono diventare grigi. L'assistente deve usare solo i testi che gli date.

Per riaprire Studio, quando il docente ve lo dice: aprite una nuova finestra di PowerShell, scrivete `unsloth studio -p 8888` e premete Invio. Poi, nel browser, aprite `http://127.0.0.1:8888` e aspettate l'indicazione del docente prima di **Select model**. Con la sua indicazione: **Select model**, **On Device**, il modello. In **Run settings** portate **Context Length** a 8192 e cliccate **Reload model**.

### B · Che cosa occupa il modello

Aprite **Run settings** (icona in alto a destra): sotto **Estimated Memory Usage** Studio scrive una stima della memoria. Scrivete in `misure_VM.txt`, sotto «Misure», quello che trovate:

| Quando | Che cosa scrivete |
| --- | --- |
| Con il modello caricato, **Context Length** su Auto | Stima di Studio e memoria in uso |
| Con **Context Length** portato a 8192 | Stima di Studio e memoria in uso |
| Una domanda breve nella chat | Secondi dal tasto Invio alla prima parola della risposta, contati con l'orologio del telefono, e velocità in tok/s |
| Il registro intero e, sotto, una domanda, in un solo messaggio | Secondi, tok/s e token usati |

**tok/s** significa token scritti al secondo: Studio lo mostra sotto la risposta. In alto Studio mostra quanti token ha usato la conversazione: **k** significa mille, quindi 1.5k sono circa 1.500 token.

**Context Length** è il numero massimo di token che il modello può tenere presenti. Per cambiarlo scrivete 8192 nel riquadro, premete Invio e poi cliccate **Reload model**: il modello si ricarica con il nuovo valore.

Se la macchina virtuale rallenta molto o si blocca con Context Length su Auto, chiudete la finestra di PowerShell in cui gira Studio, scrivete «bloccato» nella prima riga della tabella, al posto della stima e della memoria, e avvisate il docente. Per riaprire Studio seguite le indicazioni in 3A.

Confrontate le misure con il compagno. Il numero di token di Studio è uguale a quello del Tokenizer Playground? Da che cosa dipendono le differenze di memoria e di tempo? Scrivete la vostra spiegazione in due righe in `misure_VM.txt`, sotto il titolo «Spiegazione».

### C · Regolare le risposte

Qui lavorate in coppia: i criteri li scrivete insieme, le prove le dividete.

1. Decidete insieme come giudicherete una risposta. Ognuno scrive in `misure_VM.txt`, sotto il titolo «Criteri», l'elenco dei dati che l'assistente deve trovare nel registro sul fermo del 14 ottobre e come li controllerete. Scrivete anche la richiesta che farete a Studio.
2. Aprite **Run settings**. Trovate tre regolazioni:
   - **Temperature**: con un valore basso le risposte sono più prevedibili, con uno alto più varie.
   - **Top P** e **Top K**: limitano le parole tra cui il modello può scegliere.
3. Dividetevi il lavoro: uno prova la Temperature, l'altro prova Top P oppure Top K, a scelta.
4. I valori di partenza li prova chi segue la Temperature, senza cambiarli. Se la richiesta che avete scritto qui al punto 1 è uguale a quella di 3B, controllate con i vostri criteri la risposta che avete già ottenuto. Se è diversa, inviate il registro e la richiesta del punto 1 e controllate quella risposta. Scrivete i valori di partenza in `misure_VM.txt`, sotto il titolo «Scelta».
5. Poi ognuno prova un valore basso e uno alto della propria regolazione: per esempio Temperature 0.2 e 1.0, oppure Top P 0.5 e 1.0, oppure Top K 5 e 100. Se Studio non accetta il punto, scrivete la virgola. Decidete voi i valori. Per ogni prova aprite una nuova conversazione, impostate il valore in Run settings e controllate che sia quello prima di inviare il registro e la richiesta in un solo messaggio. Cambiate una sola regolazione alla volta.
6. Controllate ogni risposta sul registro, con i vostri criteri. Scrivete sotto «Scelta» una riga per prova: valore usato, dati trovati, dati mancanti o sbagliati. Scambiatevi i risultati.
7. Scegliete insieme l'impostazione che userete e scrivete in «Scelta» quale valore avete scelto e perché.

## Parte 4 · Le istruzioni dell'assistente

### A · Scrivete le istruzioni

In Run settings c'è la casella **System Prompt**. Le istruzioni scritte lì valgono per tutta la conversazione. Il messaggio che scrivete nella chat è un'altra cosa: riguarda la singola domanda.

1. Scrivete con Blocco note le istruzioni per un assistente di reparto della P03 e salvate il file come `istruzioni_assistente_P03.txt`. Decidete voi come scriverle, ma devono dire:
   - che cosa deve fare e da quali testi può ricavare le risposte;
   - quando deve farvi una domanda prima di rispondere, perché mancano dei dati;
   - che cosa non deve fare;
   - come deve scrivere la risposta.
2. Incollate le istruzioni in **System Prompt** e usate l'impostazione che avete scelto in 3C.
3. Aprite una nuova conversazione, controllate in Run settings che ci siano le istruzioni e l'impostazione scelta, e incollate in un solo messaggio il registro e, sotto, la vostra domanda.
4. Controllate se la risposta rispetta le vostre istruzioni; se no, correggetele prima di mandarle al compagno.

### B · Mettete alla prova l'assistente del compagno

1. Mandatevi il testo delle istruzioni: scrivetelo in un messaggio su Teams, dal browser della macchina virtuale oppure dal computer reale.
2. Aprite Teams nel browser della macchina virtuale, copiate il messaggio del compagno e incollatelo nel vostro System Prompt. Se non riuscite a copiarlo, riscrivetelo a mano leggendo il messaggio. Poi chiudete la scheda di Teams e controllate in Gestione attività che la memoria non sia vicina al massimo. Prima di provare, contate le regole incollate e leggete al compagno la prima e l'ultima: devono essere uguali al suo file.
3. Inventate voi almeno quattro casi di prova e tranelli: pensate a che cosa può sfuggire a un assistente che conosce solo questo registro.
4. Per ogni caso aprite una nuova conversazione, controllate in Run settings che **System Prompt** contenga le istruzioni del compagno, incollate il registro e, sotto, la domanda del caso. Scrivete in `casi_di_prova.txt`: la domanda, la risposta ricevuta, `OK` oppure `ERRORE`, e perché.

### C · Correggete le vostre istruzioni

1. Il compagno vi mostra il suo `casi_di_prova.txt` sullo schermo, oppure ve lo manda su Teams.
2. Per ogni `ERRORE` decidete che cosa correggere: le istruzioni, la domanda o il testo dato all'assistente.
3. Correggete o aggiungete le regole nel testo di `istruzioni_assistente_P03.txt`. In fondo, sotto «Correzioni dopo le prove», scrivete che cosa avete cambiato e il motivo.
4. Se tutti i casi sono `OK`, scrivete sotto «Correzioni dopo le prove» quale regola ha funzionato in ogni caso. Poi inventate un caso che le vostre istruzioni non coprono ancora, aggiungete al testo la regola che lo copre e scrivete il caso sotto «Correzioni dopo le prove».
5. Incollate in System Prompt solo le regole, corrette o confermate, senza la parte «Correzioni dopo le prove», e controllate in Run settings che ci siano. Riprovate ogni caso con `ERRORE` (oppure il caso nuovo) in una nuova conversazione. Scrivete sotto la correzione l'esito della nuova prova: `OK` oppure `ERRORE`.

## Se Unsloth Studio non parte

Avvisate subito il docente. Se l'installazione non è finita quando avete terminato la parte 2, avvisatelo comunque. Non restate fermi.

Se una sola macchina virtuale della coppia funziona, lavorate insieme su quella, a turno.

- **Memoria del modello:** aprite `octooai.com/llm-vram-calculator` nel browser del computer reale. Scegliete un modello piccolo, da circa 2 miliardi di parametri, a 4 bit, e provate prima con il contesto 8192 e poi con quello massimo. È una stima per schede grafiche, non una misura della vostra macchina virtuale: scrivetelo in `misure_VM.txt`.
- **Regolare le risposte:** usate Transformer Explainer. Scrivete insieme i criteri per estrarre i dati del fermo, scegliete una temperatura e scrivete perché. Segnate in «Scelta» che avete lavorato senza Studio.
- **Istruzioni:** scrivete `istruzioni_assistente_P03.txt` e provatele come primo messaggio in Microsoft Copilot, con il registro sotto. Non è la casella System Prompt, e così il registro esce dal reparto: scrivetelo in `casi_di_prova.txt`. Se Copilot non risponde o non accetta il messaggio, chi ha inventato i casi li pone e l'autore delle istruzioni risponde applicando alla lettera solo le regole che ha scritto; scrivete anche questo in `casi_di_prova.txt`.
- Gli appunti si scrivono come sempre.

## I vostri appunti

Non c'è niente da consegnare o da caricare: i file servono a voi, per ricordare e per raccontare a voce quello che avete fatto.

| File | Contenuto |
| --- | --- |
| `misure_VM.txt` | Previsioni, token, misure, spiegazione, criteri e scelta delle impostazioni |
| `istruzioni_assistente_P03.txt` | Istruzioni dell'assistente e correzioni dopo le prove |
| `casi_di_prova.txt` | I casi inventati per l'assistente del compagno e gli esiti |

## Prima di finire

- Nei vostri appunti ci sono le previsioni, i numeri di token e le misure?
- Le istruzioni dicono quando l'assistente deve fare una domanda?
- Ogni `ERRORE` ha una correzione, con il motivo e con l'esito della nuova prova?
- Sapete raccontare a voce che cosa avete provato e che cosa avete cambiato?
