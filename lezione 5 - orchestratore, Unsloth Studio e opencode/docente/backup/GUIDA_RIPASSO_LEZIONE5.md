# Ripasso per il docente · Lezione 5 · giovedì 19 novembre 2026

Documento riservato al docente. Serve a capire bene i concetti prima di entrare in aula. Non sostituisce `backup/GUIDA_DOCENTE.md`, che resta la guida di conduzione con le tabelle di controllo pre-aula. Qui c'è la versione corta e in parole semplici.

## 1. La lezione in una pagina

Il filo è una domanda: **chi fa che cosa?**

| Strumento | Dove gira il modello | Chi tocca i file | Che cosa vedono gli studenti |
| --- | --- | --- | --- |
| Microsoft Copilot (parte 1) | in rete, da Microsoft | nessuno: gli studenti copiano e incollano | un agente con più lavori che sceglie il lavoro giusto |
| Unsloth Studio (parte 2) | sul computer virtuale dello studente | nessuno: è solo una chat | un modello che risponde anche senza Internet, e le sue impostazioni |
| opencode (parte 3) | in rete (modello Big Pickle) | il programma, con il permesso dello studente | un programma che legge e scrive file e si ferma a chiedere |

Messaggio finale da portare a casa, in una frase: **il modello decide che cosa chiedere; il programma agisce; il permesso decide se può farlo; il contenuto lo controlli tu.**

Ogni studente lavora da solo sul proprio computer. Niente giro tra i banchi, niente file da consegnare, niente voto. Prima si fa provare, poi si mostra il criterio.

## 2. I concetti, spiegati semplici

Per ognuno: l'idea, un'immagine (le immagini sono metafore: dichiarale come tali), la frase da dire.

### 2.1 Agente con più lavori e il suo orchestratore (l'elenco)

- **L'idea.** Nella lezione 4 gli studenti hanno scritto un testo di istruzioni per Copilot. Ora quel testo ha due parti: un **elenco** («se la richiesta parla di minuti fuori servizio, usa il lavoro FUORI SERVIZIO») e i **lavori**, ognuno con le sue regole e i suoi testi da usare.
- **L'immagine.** Un attore solo sul palco: a ogni richiesta rilegge tutto il copione e recita la parte che l'elenco gli indica. Non ci sono uffici separati.
- **Cosa significa «orchestratore».** Il pezzo che sceglie quale lavoro usare, in quale ordine, e che cosa passa dall'uno all'altro. Compare sulla slide 13, dopo la domanda, con la voce dei due lavori insieme come esempio. Sulle slide e nella consegna per il resto si dice «lavoro» ed «elenco delle richieste».
- **Cosa succede davvero in Copilot.** Il modello legge **tutto il testo ogni volta**. I lavori non sono caricati separatamente. La riga «Lavoro usato:» è scritta dal modello **dopo**: è un'etichetta, non una prova di come ha ragionato.
- **Dove si corregge.** Se una richiesta va al lavoro sbagliato, si corregge la voce nell'**elenco**, non il lavoro. Se il lavoro è giusto ma la risposta è sbagliata (per esempio {{MINUTI_FUORI_SERVIZIO}} minuti invece di {{MINUTI_SENZA_BICI}}), si corregge il lavoro: si aggiunge a FUORI SERVIZIO la definizione dei minuti senza bici.
- **Frase da dire.** «Se la richiesta va nel posto sbagliato, quasi mai è sbagliato il lavoro: è l'elenco che non è abbastanza chiaro.»

### 2.2 Modello e programma: due cose diverse

È il concetto più importante della lezione, perché la parte 3 si capisce solo con questo.

- **Il modello** è il «cervello»: riceve testo e produce testo. Non apre file, non scrive file, non vede la cartella.
- **Il programma** (Unsloth Studio, opencode, Copilot) è ciò che sta attorno al modello: mostra la chat, manda il testo al modello e, se è costruito per farlo, **esegue** azioni.
- **L'immagine.** Il modello è un consulente che sta in un'altra stanza e riceve solo bigliettini scritti. Il programma è l'assistente che porta i bigliettini avanti e indietro e, se il consulente scrive «portami il faldone 3», va a prenderlo.
- **In pratica.** Quando opencode «legge un file», è il modello che scrive «leggi inventario.csv» e il **programma** che apre il file e rimanda il testo al modello. Lo studente deve vedere questa differenza con i suoi occhi (le righe «Explored: 3 reads» della slide 30).

### 2.3 Hugging Face, pesi, licenza (slide 15–16)

- **Hugging Face** è un sito pubblico dove si trovano modelli, come un negozio di file. Ogni modello ha una pagina.
- **Cosa si legge su una pagina, in quest'ordine:** chi l'ha pubblicato, la licenza (che cosa ci si può fare), quanto pesano i file (quanto spazio e memoria servono).
- **I «pesi».** Sono i numeri che il modello ha imparato in addestramento: il modello è, in sostanza, un grande file di numeri. «2B» in Qwen3.5-2B vuol dire **due miliardi di pesi**.
- **Attenzione alle parole.** I «parametri» di Studio (Temperature, Top K, Top P) sono un'altra cosa: sono le impostazioni con cui si fa rispondere il modello, non i pesi. Dillo a voce, perché sulla pagina di Hugging Face compare «2B params», che sono i pesi.
- **GGUF.** È il formato del file pensato per girare su un computer normale. Non serve approfondirlo: basta dire «è il formato adatto a girare sul vostro PC».
- **Per prepararti.** Apri la pagina `unsloth/Qwen3.5-2B-GGUF` e leggi tu stesso editore, licenza, file più piccolo e più grande. La licenza del modello (Apache 2.0) e del programma Studio (AGPL-3.0) sono indicate dalla guida, ma **controllale sui siti prima di dirle**. La dimensione del file del modello non è sicura (1,3 GB o 2,0 GB a seconda della fonte): leggila in Studio, non dirne una a memoria.

### 2.4 Un modello che gira sul PC (slide 18–20)

- **L'idea.** Il modello di Studio è un file sul computer virtuale. Per rispondere non chiede niente a nessuno in rete.
- **La prova.** Gli studenti fanno una domanda, tolgono la rete, rifanno la domanda: risponde lo stesso.
- **Che cosa NON dire.** Non dire che è «migliore» o «peggiore» di Copilot: non è stato misurato. Dì solo: gira sul processore del computer, quindi può essere lento; il modello legge il testo lì, anche senza rete.
- **Attenzione.** Il gesto per togliere la rete dentro la VM non è provato: scoprilo prima dell'aula. Se non c'è un gesto semplice per gli studenti, lo fai tu dal proiettore e dici com'è.
- **Il guadagno concreto.** Il modello legge i dati sul computer: per rispondere non servono la rete né un servizio esterno. È uno dei motivi per cui si usano i modelli locali.
- **Dove vanno i dati (slide 9 e 20).** In Copilot e in opencode il testo scritto viaggia in rete fino al servizio (Microsoft; chi offre Big Pickle, che nel periodo gratuito, secondo la documentazione di OpenCode, può usarlo per migliorare il modello); in opencode parte anche il contenuto dei file che legge, senza chiedere. In Studio il modello legge il testo sul computer, anche senza rete: che con Search spento non esca nulla non è provato. Non dire che cosa conserva Microsoft con l'account scolastico.
- **Perché è lento.** Il modello gira sul processore del PC, non su macchine grandi: per questo risponde piano. È piccolo perché possa girare lì. Non dire che «sbaglia più facilmente»: non è misurato. Vale come frase a voce e sta anche nella slide 20.
- **Confronto con Copilot (slide 20).** La stessa domanda del cacciavite, fatta a Copilot dal vivo dal tuo PC, accanto alla risposta di Studio. Non è una gara e non serve a parlare di velocità se la risposta è quella preparata.

### 2.5 Context Length: quanto testo il modello tiene insieme (slide 21)

- **L'idea.** Il modello legge un testo alla volta fino a un limite: è il **Context Length**, misurato in **token** (pezzi di parola; una parola italiana è fatta di uno o più token).
- **L'immagine.** La scrivania: più è grande, più fogli ci stanno aperti insieme. Che cosa succede ai fogli in più lo mostra la dimostrazione della slide 26.
- **Nei numeri della lezione.** La VM ha 8192. Un messaggio con registro, regole e istruzioni del noleggio misurava circa 3.665 token il 15 novembre: ci stava. Controlla prima dell'aula, con il contatore di Studio, che con le istruzioni nel System Prompt si arrivi a circa 3.700.
- **Il costo.** Più contesto vuol dire più memoria. In Studio con 8192 la memoria stimata è 3,33 GiB; con «Auto» sale a 6,48 GiB e Studio avvisa che supera la RAM. Perciò gli studenti **non lo toccano**: lo cambi tu (serve «Reload model»).
- **Domanda da studenti.** «Perché Copilot non ha questo problema?» Risposta onesta: ce l'ha anche lui, ma con un limite molto più grande, che non vediamo.
- **Che cosa succede oltre il limite (slide 26).** Studio potrebbe scartare l'inizio, rifiutare il messaggio o rispondere in un altro modo: non lo so, non è provato. Mostralo com'è, con il contatore del contesto. È il motivo per cui nella lezione 6 serve il RAG.

### 2.6 Temperature, Top K, Top P (slide 22–24)

Il modello, a ogni passo, calcola una **probabilità per ogni parola possibile** e poi ne sceglie una. Le tre impostazioni cambiano **come sceglie**. Gli studenti hanno già visto le probabilità in Transformer Explainer (lezione 4).

| Parametro | Spiegazione semplice | Immagine (metafora) |
| --- | --- | --- |
| Temperature | Bassa: sceglie quasi sempre la parola più probabile. Alta: dà più possibilità alle parole improbabili. | Un dado truccato che a poco a poco diventa un dado normale |
| Top K | Il modello guarda solo le K parole più probabili e ignora le altre. | Una lista della spesa ridotta ai primi K prodotti |
| Top P | Il modello prende le parole più probabili, dall'alto, finché le loro probabilità sommate arrivano a P. | Si riempie il bicchiere finché si arriva alla linea P |

- **Cosa fanno gli studenti.** Solo Temperature: Temperature a 1,5, richiesta «Continua con poche parole: Nel mio laboratorio ho trovato», tre risposte (invio e due rigenerazioni), quante sono diverse. Top K e Top P restano solo nella tabella della slide 24 e non si provano.
- **Cosa aspettarsi.** Con Temperature alta le risposte dovrebbero essere diverse tra loro. Non è provato nella VM: se identiche, cerca un campo Seed fisso (è nella tabella di controllo della guida). Non fondare la lezione sull'errore del modello: va bene qualunque esito.
- **Regola importante.** «Non esiste una Temperature giusta: dipende dal compito.» Per un conteggio in un registro si vuole bassa; per inventare un nome di pizza si può alzare.
- **Alla fine.** Gli studenti rimettono Temperature com'era.

### 2.7 System prompt, messaggio normale e RAG (slide 25 e richiamo a voce)

Tre modi diversi di dare testo al modello, da tenere separati:

| Che cosa | Quando il modello lo legge | Esempio |
| --- | --- | --- |
| System prompt | **prima di ogni** messaggio, sempre | «Sei un cuoco burbero. Rispondi in una frase.» |
| Messaggio normale | solo in quella conversazione | la domanda dello studente |
| RAG (visto nella lezione 3) | il programma **sceglie dai documenti**, in base alla domanda, e aggiunge solo i passaggi che c'entrano | un manuale da cui si pesca la pagina giusta |

- **Frase da dire a voce dopo la slide 26** (nessuna slide, nessuna attività): «Prima il testo fisso, nel System prompt; con il RAG il testo viene scelto ogni volta dalla domanda.» L'immagine del bibliotecario che porta sul banco solo la pagina che serve è una metafora: dichiarala.
- **In Studio il System prompt è un vero testo di sistema.** In Copilot, nella lezione 2, con una normale conversazione, le istruzioni nel primo messaggio **non** lo erano. Se qualcuno lo ricorda, è una buona differenza da far notare.
- **Il testo resta dopo «Nuova chat»** (provato su VMware): fai cancellare il testo alla fine dell'attività.
- **Un modello da 2 miliardi può non seguire una regola.** Non è un errore dello studente: la correzione fa parte dell'esercizio, e una prova riuscita subito vale quanto una corretta.
- **Il cuoco burbero non è provato** con il modello da 2B: provalo prima dell'aula sulla tua VM.

### 2.8 opencode: il programma che agisce (parte 3)

- **Che cos'è.** Un programma che parla con un modello e, a differenza di una chat, può **leggere e scrivere file nella cartella** dove parte. Qui parte in `laboratorio`, con tre file inventati: `inventario.csv`, `appunti_riunione.txt`, `da_fare.txt` (più `opencode.jsonc`, il file con le regole).
- **Gli altri programmi come opencode (slide 27).** Una slide, una domanda a voce, poche frasi. Claude Code (Anthropic, 24 febbraio 2025) è il primo di un grande laboratorio di IA e ha reso popolare questo modo di lavorare; non è il primo in assoluto (Aider, maggio 2023; Goose, gennaio 2025). Codex CLI (OpenAI) e Gemini CLI (Google) sono aperti; Claude Code e GitHub Copilot CLI no. opencode: aperto (MIT), molti modelli, il più seguito su GitHub tra i programmi aperti (non dire «il più usato»). Dettaglio e fonti nella guida docente, parte 3.
- **Immagini a voce (dal podcast, metafore da dichiarare, sempre dopo la prova o la dimostrazione).** Copilot: un attore solo (dopo la slide 13). Temperature: un dado (dopo la slide 23). Context Length: una scrivania (dopo la dimostrazione della slide 26). RAG: un bibliotecario (richiamo dopo la slide 26). Modello e programma: un consulente chiuso in una stanza e un assistente fuori che porta i file (dopo la slide 30). Stanchezza da permessi: una frase dopo la domanda finale. Elenco in guida docente, «Immagini dal podcast».
- **Il modello è Big Pickle**, uno dei modelli gratuiti di opencode. Risponde **dalla rete**, quindi serve la rete dalla VM (ecco perché la rete va riattivata dopo la 2A). Dalla documentazione, nel periodo gratuito i dati possono servire a migliorare il modello: ecco perché agli studenti si dice di non scrivere dati personali. Non è provato come si comporti con tutte le VM sullo stesso indirizzo della scuola.
- **Chi apre i file (slide 29–30).** Il modello chiede, il programma esegue. «Explored: N reads» dice **quante** letture ha fatto il programma. Per la richiesta «Che file ci sono...», il numero può cambiare da studente a studente: è normale.
- **Plan e Build (slide 32–33).**
  - **Plan** = «prima pensa e proponi»: il programma **non** scrive.
  - **Build** = «ora esegui».
  - Si cambia con Maiusc+Tab; in basso si legge quale è attivo.
  - Lo studente scrive la stessa richiesta in tutte e due: in Plan il file non compare, in Build sì (dopo il permesso).
- **I permessi (slide 34 e 39).** Per ogni azione il file `opencode.jsonc` dice una di tre cose:

| Regola | Significato | Esempio nel file |
| --- | --- | --- |
| allow | fa senza chiedere | leggere un file |
| ask | si ferma e chiede a te | scrivere un file in Build; eseguire un comando |
| deny | rifiuta | scrivere un file in Plan |

- **«Allow once» o «Always allow».** Una volta sola, oppure per sempre. **Sempre «Allow once»:** «Always allow» trasforma ask in allow per sempre e la richiesta sparisce. Dillo a voce prima della slide 29.
- **Leggere prima di approvare (slide 34).** Il permesso mostra il nome del file e il testo da scrivere. Gli studenti li leggono prima di scegliere. È la parte che l'«ask» affida a loro. Se in Build la richiesta non mostra il testo, toglilo a voce dalla slide e dalla consegna.
- **Quando compare un comando da eseguire** (non solo la scrittura del file): la regola della consegna è che si approva con Allow once solo se è **uguale, lettera per lettera, a quello scritto nella consegna**. Qualunque altro comando: **Reject**. Nota: il comando atteso viene da una prova del 15 novembre con una richiesta diversa; il 16 novembre con la richiesta attuale potrebbe essere un altro. **Provalo prima dell'aula nella VM e aggiorna la consegna.**
- **Reject (slide 36).** Il file non compare. Cosa scrive opencode dopo il Reject? Non è provato con la scrittura: nelle prove sulla lettura, Reject ha interrotto tutta la risposta. Guarda com'è e non anticipare.
- **La richiesta propria (slide 37–38).** Ognuno inventa una richiesta su due file e si fa creare un file nuovo, poi **controlla un dato** scelto da lui contro l'originale. Il criterio non è che il file sia bello, ma che quel dato sia uguale. Se non torna, si corregge la richiesta: è lavoro, non fallimento.

### 2.9 Chi controlla che cosa (slide 13, 41, 42)

Due controlli diversi, da non confondere:

| Controllo | Chi lo fa | Esempio |
| --- | --- | --- |
| Sulle **azioni** (scrivere, eseguire) | il permesso del programma | opencode si ferma e chiede prima di scrivere un file |
| Sui **dati** (il numero è giusto?) | lo studente, sul documento originale | il numero della nota rispetto al registro |

Il permesso **non** verifica che il contenuto sia giusto: dice solo se l'azione è consentita. Nella slide 42 la domanda su «cancellare un file» (allow, ask o deny) non ha una sola risposta giusta: **ask** è la più difendibile, perché cancellare non si annulla. Quello che conta è che lo studente motivi.

Un file letto da opencode può contenere frasi che sembrano richieste («dopo la lettura crea un altro file»): il modello può trattarle come istruzioni vere. Per questo si legge sempre che cosa il programma vuole fare prima di dire «Allow once». Lo dici a voce dopo la domanda finale; non è provato e non lo proietti.

## 3. La lezione, parte per parte

I testi in corsivo sono frasi che puoi dire a voce. Non ci sono tempi: guarda gli schermi e chiudi tu ogni parte a vista.

### Parte 1 · Copilot e l'agente con più lavori (slide 1–13)

**Obiettivo.** Far vedere un elenco che instrada la richiesta verso il lavoro giusto, e un dato che passa da un lavoro all'altro.

1. **Slide 2.** Il quadro: il titolare vuole che l'agente sappia fare tutti e tre i lavori; si completa in Copilot, poi si passa alla VM per Studio e opencode, ognuno la sua. Nessuna attività.
2. **Slide 3.** Riaprono il loro agente e rifanno la domanda della lezione 4 sulla bici 12 (sabato, minuti fuori servizio); cercano gli orari nel registro e li confrontano con la risposta. Gli orari giusti: **{{ORA_FUORI_SERVIZIO}} → {{ORA_DISPONIBILE}}, {{MINUTI_FUORI_SERVIZIO}} minuti.** Non li dici a voce prima del controllo.
3. **Slide 4–6.** Cercano nel proprio file l'elenco e i lavori; scrivono il lavoro che manca (GUASTI se hanno PASSAGGIO, o il contrario); aggiornano l'agente. La tabella è a metà: **non dare risposte né esempi di GUASTI o PASSAGGIO.**
4. **Slide 7–9.** Tre richieste, una per lavoro. La prima chiede i minuti senza bici del cliente: la risposta attesa è **{{MINUTI_SENZA_BICI}} minuti, dalla segnalazione ({{ORA_SEGNALAZIONE}}) al cambio ({{ORA_CAMBIO}})**, non i {{MINUTI_FUORI_SERVIZIO}} del fuori servizio. Guardano la prima riga «Lavoro usato:» e il contenuto, e correggono la voce dell'elenco o il lavoro; poi (slide 9) pensano a dove andrebbero i dati se il registro fosse vero.
5. **Slide 10–11.** La catena FUORI SERVIZIO → PASSAGGIO: il numero entra nella nota. Il numero giusto è **{{MINUTI_FUORI_SERVIZIO}} minuti**.
6. **Slide 12–13.** Salvano il file. *Il numero l'avete controllato voi, non il programma.* Sulla slide 13 compare la parola «orchestratore», con la voce dei due lavori insieme come esempio. I numeri da controllare ({{MINUTI_FUORI_SERVIZIO}} e {{MINUTI_SENZA_BICI}}) sono nella tavola «Valori di riferimento» della guida docente.

**Chi non ha il file.** Dagli il file `da_pubblicare_a_chi_non_ha_il_file/ISTRUZIONI_DI_PARTENZA_NOLEGGIO.txt`. Non è una soluzione collaudata: ha già i tre lavori, quindi salta la scrittura (slide 5) e passa alla prova. Non presumere che tutti abbiano finito la lezione 4.

**Se Copilot non risponde** (il 4 novembre è mancato circa 10 minuti, ipotesi: limite di richieste per indirizzo): prova a secco dal proiettore su un testo di uno studente, dichiarando che non è una risposta del modello.

**Non provato:** nulla di questa parte è stato provato in Copilot con l'account studente (creazione e modifica dell'agente, lunghezza massima delle istruzioni con tre lavori).

### Parte 2 · Unsloth Studio, il modello sul computer (slide 14–26)

1. **Slide 14.** Passano al computer virtuale.
2. **Slide 15–16.** Pagina di un altro modello dal proiettore (`bartowski/Llama-3.2-1B-Instruct-GGUF`) con quattro punti cerchiati; poi ognuno apre la pagina di Qwen3.5-2B-GGUF e trova gli stessi quattro punti. *Prima il concreto, poi il nome.*
3. **Slide 17.** Aprono Studio dal collegamento. Se in alto manca «Qwen3.5-2B-GGUF», scelgono Select model › On Device › Qwen3.5-2B-GGUF (circa 50 secondi sul tuo PC; sui PC della scuola non misurato). **Dì a voce: la finestra nera con il testo non va chiusa, altrimenti Studio si ferma. «Remind me later» agli avvisi di aggiornamento.**
4. **Slide 18–19 · 2A.** *«Questo modello ha bisogno di Internet?»* Domanda a voce, nessuna conta. Prima domanda, poi rete tolta, poi stessa domanda; riattivare la rete.
5. **Slide 20.** La tabella «Dove gira?» arriva **dopo** che hanno visto la risposta; ha anche la riga su dove vanno i dati. Poi mostri la risposta di Copilot alla stessa domanda del cacciavite: si guarda che cosa cambia (lunghezza, tono, precisione), non quale è migliore.
6. **Slide 21.** Aprono il pannello, leggono Context Length (deve essere 8192) e Temperature. Non toccano nulla.
7. **Slide 22–24 · 2B.** Tu mostri dal vivo la pizza con Temperature 1,5, tre volte; poi provano loro; poi la tabella dei tre parametri. Rimettono Temperature com'era.
8. **Slide 25 · 2C.** Esempio del cuoco burbero dal vivo; poi due righe loro e due domande. Fai cancellare il System prompt alla fine.
9. **Slide 26 · Quanto testo tiene insieme il modello?** Domanda a voce: il messaggio supera 8192, che cosa farà Studio? Poi la tua dimostrazione dal proiettore, con il contatore del contesto nell'intestazione di Studio. Prima di passare a opencode: la finestra nera resta aperta, Search e Tools restano spenti (Search usa la rete), rimettere Temperature com'era, cancellare il System prompt. A voce, il richiamo al RAG: «Prima il testo fisso, nel System prompt; con il RAG il testo viene scelto ogni volta dalla domanda.»

**Se Studio è lento o non risponde:** 2B e 2C dal proiettore; la 2A dal proiettore se la rete spenta funziona.

### Parte 3 · opencode (slide 27–42)

1. **Slide 27–28.** Slide 27: la domanda a voce («Conoscete qualcuno di questi programmi? Lavorano sui file, come opencode.») e la tabella degli altri programmi; non è una rassegna. Slide 28: doppio clic sul collegamento opencode (parte da `laboratorio`, modalità Build, modello Big Pickle). Rete riattivata. Dati personali: no.
2. **Prima della slide 29, a voce a tutta la classe:** se compare «Permission required», si legge che cosa vuole fare; si sceglie **solo Allow once**, mai Always allow; un comando si approva solo se è identico a quello della consegna, altrimenti Reject.
3. **Slide 29–30 · 3A.** *«Chi apre i file: il modello o il programma?»* poi inviano e contano le letture.
4. **Slide 31–35 · 3B.** Scrivono la richiesta per `inventario.html` senza inviarla; la inviano **prima in Plan** (il file non compare); poi in Build; permesso «Edit» con Allow once; aprono la pagina e contano le righe con un componente rispetto al CSV. Nel CSV ci sono **15 righe di dati** (più la riga delle intestazioni; file `CARTELLA_LABORATORIO/inventario.csv`). Se lo studente chiede di evidenziare le quantità sotto 5, controlla nel CSV (nella guida: filamenti neri e saldatori).
5. **Slide 36 · 3C.** Richiesta su `riassunto.txt`, poi **Reject**; non reinviano. Guardano che cosa scrive opencode e se il file c'è.
6. **Slide 37–38 · 3D.** Richiesta propria su due file; prevedono il contenuto; Allow once; confronto di un dato.
7. **Slide 39.** Proietti le righe di `opencode.jsonc`, poi la tabella allow, ask, deny.
8. **Slide 40–42.** Domanda sui tre strumenti, **poi** la tabella; chiusura con «allow, ask o deny per cancellare un file?» e «il contenuto di un file nuovo, chi lo controlla?».

**Se Big Pickle non risponde** (rete o limite di richieste con tutte le VM insieme): scegli **una** alternativa e dichiarala.

| Alternativa | Come dichiararla |
| --- | --- |
| a · Qwen locale con `unsloth start opencode`: solo dimostrazione, è molto lento (provato: oltre 4 minuti a risposta) | «Qui il modello è piccolo e locale: è lento.» |
| b · opencode sul tuo PC con Big Pickle, proiettato (prova con l'hotspot del telefono se il guasto è la rete della scuola) | «Esecuzione reale sul computer del docente, non sulle VM.» |
| c · schema a secco su carta (`docente/SCHEMA_A_SECCO_PARTE3.md`) | «Non è un'esecuzione: è uno schema scritto a mano.» |

Chiedi di aspettare prima di riprovare: richieste ripetute peggiorano il limite (ipotesi).

## 4. Domande che gli studenti potrebbero farti

| Domanda | Risposta semplice |
| --- | --- |
| «Perché il modello nella VM è così lento?» | Gira sul processore del tuo PC, non su una grande macchina in rete. In cambio non esce dal computer. |
| «È lo stesso modello di Copilot?» | No. Copilot gira in rete su macchine di Microsoft. Questo è piccolo e si trova su Hugging Face. Non confronto la qualità: non l'abbiamo misurata. |
| «Perché Temperature 1,5 e non 100?» | Perché oltre un certo punto le parole diventano casuali. Si prova e si guarda: non esiste un valore giusto per tutto. |
| «Posso fidarmi di opencode che scrive un file?» | Il permesso dice se l'azione è consentita. Che il contenuto sia giusto lo controlli tu sull'originale. |
| «Perché non scelgo Always allow, così smette di chiedere?» | Perché trasforma ask in allow per sempre: poi non ti chiede più nemmeno quando vuole cambiare altro. |
| «Il modello ha davvero letto il file?» | Lo vedi nelle righe «Explored: N reads»: è il programma che mostra le letture. |
| «Questo agente di Copilot è lo stesso che fa opencode?» | No. In Copilot è un testo letto dal modello: nessun programma agisce al posto tuo. In opencode un programma esegue e si ferma a chiedere. |
| «Cos'è un token?» | Un pezzo di parola. Il modello legge e scrive a pezzi. Un messaggio con registro, regole e istruzioni del noleggio ne misura circa 3.665 (misura del 15 novembre; da rifare oggi con i soli registro e regole). |
| «Perché la parola "parametri" ha due significati?» | Vero, ed è un problema di nome. I «2B» di Qwen3.5-2B sono i pesi imparati; Temperature, Top K e Top P sono impostazioni di risposta. Usiamo «parametri» solo per le seconde. |

## 5. Che cosa NON dire (non è provato)

- Che la creazione o la modifica dell'agente in Copilot funzioni con l'account studente: **non provata**.
- Che lo studente possa togliere la rete nella VM con un gesto semplice, o che Studio risponda senza rete: **non provato**.
- Che Temperature 1,5 dia tre risposte diverse con Qwen 2B, o che il cuoco burbero sia seguito: **non provato**.
- Che il comando che opencode chiede di eseguire in 3A sia quello scritto nella consegna: **va verificato** nella VM.
- Che Reject interrompa la risposta anche con la scrittura: **non provato**.
- Che Big Pickle regga tutte le VM sullo stesso indirizzo della scuola: **non provato**; non dire che i modelli gratuiti restino gratuiti (il periodo è limitato).
- Che Copilot e Studio abbiano qualità diverse, o che Studio sia più sicuro: non misurato. Dì solo dove gira il modello.
- Un risultato scritto a mano come se fosse la risposta del modello: mai.
- Che opencode «capisca» o «decida» come una persona: dì che il modello **propone** e il programma **esegue**.
- Che cosa Microsoft conserva o non conserva dei dati con l'account scolastico: non è verificato. Dì solo che il testo viaggia in rete fino al servizio.
- Che cosa farà Studio con un testo più lungo del limite (slide 26): non è provato. Mostralo com'è.

## 6. Preparazione prima dell'aula, in ordine

Fai una volta sola, sulla tua copia della VM (o sulla VM che userai in aula), e cancella le prove prima di copiare.

1. **Copilot.** Apri il tuo agente con il testo di partenza e prova le tre richieste della slide 7 e la catena della slide 10. Controlla che il numero nella nota sia **{{MINUTI_FUORI_SERVIZIO}}** e che la lunghezza delle istruzioni sia accettata.
2. **Rete nella VM.** Trova il gesto per togliere e riattivare la rete in Windows dentro la VM. Con la rete tolta, Studio risponde?
3. **Studio.** Collegamento sul desktop (nome esatto?), modello caricato (intestazione «8.2k»), Search e Tools spenti. Prova Temperature 1,5: dove si scrive, virgola o punto, dov'è il pulsante per rigenerare, che cosa fa «Reset all». Prepara la dimostrazione della slide 26: un testo più lungo di 8192 token (il registro incollato più volte) con una frase distintiva all'inizio e una domanda su quella frase; guarda che cosa fa Studio. Prepara anche la risposta di Copilot alla domanda sul cacciavite (slide 20).
4. **System prompt.** Prova il cuoco burbero con due domande. Poi cancellalo.
5. **opencode.** Avvia dal collegamento con la rete attiva. Prova la richiesta della slide 29: quale comando chiede, se lo chiede? **Aggiorna la consegna se è diverso.** Poi la richiesta della slide 31 in Plan e in Build, e la richiesta della 36 con Reject.
6. **Pulizia.** Nella cartella `laboratorio` devono restare solo i tre file e `opencode.jsonc`: via `inventario.html`, `riassunto.txt`, conversazioni di prova, approvazioni salvate.
7. **Materiali da pubblicare su Teams:** `studenti/ATTIVITA_LEZIONE5.docx` e i tre testi del noleggio. **Non** pubblicare le cartelle di backup. Il file `ISTRUZIONI_DI_PARTENZA_NOLEGGIO.txt` lo dai solo a chi non ha il proprio file.
8. **Ramo di riserva.** Decidi **prima di entrare** quale usare se Big Pickle non risponde (di solito b, sul tuo PC con l'hotspot), e tieni pronto lo schema a secco.
9. **Proiettore.** Prepara la risposta alla pizza con Temperature 1,5 e il cuoco burbero. Se Studio non risponde, mostra le richieste e dichiara che non hai la risposta.
10. **Cartelle e rete.** Controlla che le VM partano e che la finestra nera dei log non venga chiusa.

## 7. Mini-glossario (per te)

| Parola | In una riga |
| --- | --- |
| Modello | Il programma che produce testo a partire da testo. Non agisce da solo. |
| Peso | Un numero imparato in addestramento. «2B» = due miliardi di pesi. |
| Token | Un pezzo di parola. Il modello legge e scrive a pezzi. |
| Context Length | Quanti token il modello tiene insieme. Nella VM: 8192. |
| Temperature, Top K, Top P | Impostazioni che cambiano come il modello sceglie la parola successiva. |
| System prompt | Testo che il modello legge prima di ogni messaggio, in Studio. |
| Hugging Face | Sito pubblico con le pagine dei modelli. |
| Orchestratore | Il pezzo che sceglie quali lavori usare, in che ordine e che cosa passare. |
| Plan / Build | In opencode: Plan non scrive, Build scrive (con il permesso). |
| allow / ask / deny | Fa senza chiedere / chiede / rifiuta. |
| Allow once | Approva questa volta sola. Mai Always allow. |
| RAG | Il programma cerca nei documenti i passaggi che c'entrano e li aggiunge alla richiesta. |

## 8. Dopo l'aula (per la lezione 6)

Conserva da quello che vedi dal proiettore: che cosa ha tenuto il modello piccolo nel System prompt, quale ramo della parte 3 hai usato, che cosa ha funzionato nella VM e che cosa no. Non raccogliere un'autovalutazione scritta. Il recupero di documenti (RAG) con Studio è rimandato alla lezione 6: i controlli già raccolti sono nel piano.
