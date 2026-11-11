# Regole del progetto ITS MAKER

Queste regole valgono per la creazione e la revisione dei materiali del corso. Le nuove richieste esplicite dell'utente prevalgono sulle scelte precedenti; le scelte di una variante non si estendono automaticamente a tutte le lezioni.

## Presentazioni: modello obbligatorio

- Applicare sempre il modello PowerPoint ufficiale fornito dall'utente. Non partire da una presentazione vuota per poi imitare la grafica e non proporre un tema alternativo senza richiesta.
- Il riferimento originale è `Lezione1_AI_processi_ITS_MAKER.pptx`, attualmente disponibile anche in `~/Downloads/`. Il modello è già incorporato nei PowerPoint approvati del repository, per esempio `lezione 2 - 28 ottobre 2026/Lezione2_Prompting_e_Pratica_ITS_MAKER.pptx`.
- Se il file originale non è disponibile, recuperare il modello da una presentazione approvata o dallo storico del progetto. Non sostituirlo silenziosamente con una grafica ricreata.
- Conservare fondali, loghi, colori, caratteri, proporzioni e tipi di pagina. Il modello corrente è 16:10 e comprende COPERTINA, CONTENUTO, SEZIONE e CHIUSURA.
- Aggiornare i testi variabili, compresi i riferimenti al programma usato, senza alterare l'identità grafica del modello.
- Mantenere testo e tabelle modificabili nel PowerPoint. Non trascinare nel nuovo file slide, note o contenuti della vecchia lezione usata come base.
- La versione HTML deve usare gli stessi fondali e la stessa identità grafica, non una seconda grafica indipendente. Deve restare utilizzabile senza file temporanei esterni.

## Materiali destinati agli studenti

- Scrivere in italiano comune, con frasi brevi e istruzioni concrete. Il pubblico è composto da studenti tecnici alle prime armi: attività semplici, comprensibili e coinvolgenti.
- Niente gergo, anglicismi superflui, sigle non spiegate o nomi di comandi da imparare inutilmente. Preferire parole come istruzioni, richiesta, risposta, registro, tabella, nuova conversazione e controllo. Conservare i nomi reali dei prodotti; spiegare al primo uso le estensioni necessarie, come `.md`.
- Usare nomi concreti per attività e ruoli. Spiegare al primo uso eventuali termini nuovi o metafore, senza presentarli come funzioni del programma. Nelle consegne indicare chi compie ogni azione, dove scrive e in quale ordine procede. Presentare ogni istruzione e tabella nel passaggio in cui va usata, non dopo.
- Dire chiaramente quale programma aprire, che cosa scrivere o copiare, che cosa controllare, che cosa salvare e che cosa consegnare.
- Non inserire note sulla progettazione della lezione, giudizi sul livello degli studenti, riferimenti alle soluzioni o alla loro collocazione, né altre informazioni riservate al docente.
- Un registro usato come fonte deve raccontare i fatti. Evitare suggerimenti che anticipino la soluzione o annuncino artificialmente quali dati mancano.
- Non inserire tempi di completamento: niente durata complessiva prevista, minuti assegnati agli esercizi, tabelle delle durate o formule come «se resta tempo». La regola vale anche per la guida docente, salvo richiesta esplicita contraria. La stima dei tempi della revisione didattica resta nel rapporto del revisore e non entra nei materiali.
- Conservare invece date, orari e durate che sono dati del caso, per esempio gli orari e i minuti del fermo macchina.

## Scrittura e diapositive: devono sembrare scritte da una persona

Valgono per slide, consegne, guide e per ogni testo del corso. Le slide in particolare non devono sembrare l'output di uno script: il generatore le impagina, ma il testo lo si scrive e lo si rilegge come lo scriverebbe un docente.

- Una slide, un'idea. Il titolo esprime un punto o una domanda concreta, non un'etichetta generica. Niente numerazione nei titoli visibili. Preferire «Togliete un neurone. Funziona ancora?» a «L'attività pratica».
- La slide proietta ciò che si guarda o si decide insieme: una domanda, un numero, una schermata, una scelta, una regola in una riga. Le istruzioni passo per passo stanno nella consegna, dove servono. Non riportare sulla slide lo stesso testo della consegna.
- Poche parole, leggibili dal fondo dell'aula. In genere bastano una domanda e poche righe. Le eccezioni devono servire al confronto, non a comprimere la consegna in una slide. Se servono sei passaggi, non sono una slide.
- Variare la forma da una slide all'altra: domanda a tutto schermo, un solo numero grande, una frase del responsabile, una scelta tra due, un confronto in tabella. La tabella si usa solo quando ci sono davvero dati da confrontare, non per ogni elenco. Non aprire tutte le slide con la stessa struttura (titolo, tre punti, frase finale).
- Parlare agli studenti come in aula: «voi», frasi dirette e concrete. Il docente racconta il resto a voce; non spiegare sulla slide ciò che si dice meglio parlando.
- Evitare i segni di un testo prodotto in serie: elenchi sempre di tre elementi, frasi simmetriche («non solo X, ma Y»), aggettivi enfatici, formule di apertura e di chiusura che riassumono («In sintesi», «Come abbiamo visto»), titoli e blocchi ripetuti identici, grassetto sparso, punti elenco di una sola parola, ripetizione della stessa frase di avviso in più slide.
- Frasi di una riga che dicono un fatto battono frasi lunghe che dicono un valore. Se una frase può essere tolta senza che si perda nulla, toglierla.
- Prima di consegnare slide o consegne, rileggerle per intero come le leggerebbe uno studente. Se suonano come un modulo o un manuale, riscriverle. Il prefisso «Slide NN —» nel Markdown sorgente serve solo al generatore e non deve comparire sulla slide.
- Per nuove lezioni e riprogettazioni leggere e applicare `FLUSSO_SVILUPPO_DIDATTICO.md`: progettazione dell'esperienza, prova concreta, redazione distinta per slide e consegna, revisione indipendente. La revisione didattica obbligatoria resta quella definita più sotto.

## Programma di intelligenza artificiale e funzioni effettive

- Nominare esplicitamente il prodotto scelto dall'utente. Non parlare genericamente di «assistente» senza spiegare a quale programma ci si riferisce.
- Non presumere disponibili funzioni, autorizzazioni o servizi a pagamento sulla sola base del nome di una licenza.
- Distinguere le istruzioni inviate in un normale messaggio dalle vere istruzioni di sistema. Distinguere una proposta testuale da un'azione eseguita da un programma.
- Non dichiarare aggiornato un documento, creato un agente o eseguita un'operazione se l'attività produce soltanto testo da controllare e copiare.
- Non dichiarare collaudata l'esercitazione sulla piattaforma della scuola se sono stati verificati soltanto i documenti. Separare le verifiche dei materiali dalle prove effettive con l'account studente.

## Progettazione degli esercizi

- Privilegiare un approccio pratico basato sul fare da parte degli studenti, riducendo al minimo la spiegazione frontale iniziale.
- Progettare attività che suscitino interesse con una scelta, una scoperta o un oggetto da costruire e un risultato riconoscibile. Scrivere appunti e farli controllare non basta. Il riscontro deve essere leggibile nello strumento o basato su criteri chiari discussi collettivamente; non usare il giro tra i banchi come meccanismo principale. Evitare punti, classifiche e personaggi aggiunti solo per decorare una procedura. Non premiare la fortuna nelle risposte del modello.
- Evitare esercizi che si risolvano in pochi minuti o si riducano a una sequenza passiva di «copia, incolla e verifica» in cui il lavoro progettuale è già stato svolto nella scheda e l'intelligenza artificiale esegue tutta l'analisi al primo tentativo.
- Fornire agli studenti l'obiettivo del caso, i vincoli e i risultati attesi, ma non consegnare istruzioni complete già pronte da copiare e incollare: devono essere gli studenti a ideare, scrivere, provare e correggere per tentativi le istruzioni per l'assistente.
- Prevedere spazi di creatività e decisione autonoma: per esempio progettare assistenti che pongono domande prima di produrre una risposta, incrociare più informazioni o regole (appunti, listini, priorità, vincoli operativi) e prendere decisioni motivate.
- Nelle fasi di verifica e confronto tra coppie non fornire solo frasi di prova precompilate: chiedere agli studenti di inventare i casi critici e i tranelli con cui mettere alla prova l'assistente dei compagni e di correggere poi le proprie istruzioni dove emergono falle.
- Per sintesi ed estrazione usare una fonte sufficientemente lunga e ricca di eventi, non un testo già ridotto ai pochi dati della risposta.
- Mantenere semplici e coerenti dati e consegne. La difficoltà deve stare nel riconoscere, ordinare e controllare le informazioni, non nel conoscere termini tecnici complessi.
- Le annotazioni ordinarie e le ripetizioni contestuali possono essere parte dell'esercizio: non eliminarle come se fossero note organizzative inutili.
- Non fondare l'attività sull'aspettativa che il modello sbagli. Un buon risultato con una richiesta semplice è valido; valutare la capacità degli studenti di verificarlo sul documento.
- Eventuali difficoltà aggiuntive devono essere realistiche, poche e leggibili. Non complicare progressivamente il caso soltanto per ottenere un errore dell'intelligenza artificiale.
- Non presentare testi o risposte preparati a mano come vere esecuzioni del modello.
- Distinguere le decisioni approvate dalle idee discusse: non applicare automaticamente proposte di modifica che l'utente non ha richiesto di eseguire.
- Prima di richiamare una lezione precedente, verificare con l'utente che cosa è successo davvero in aula (consegne, agenti creati, attività saltate). I materiali di una lezione descrivono il progetto, non quello che è stato svolto.
- Quando un'attività passa informazioni da uno strumento all'altro (per esempio dal Blocco appunti a un agente), rendere esplicito che cosa si può perdere nel passaggio e dare un controllo esterno per verificarlo, come un riepilogo calcolato con regole note.
- Le istruzioni di esempio per un assistente si consegnano solo dopo il tentativo degli studenti e stanno in una cartella separata, con il momento della consegna nel nome, per esempio `da_pubblicare_dopo_prova_B/`.

## Fonti, dati e strumenti

- Le fonti pubbliche si usano solo con un permesso di riuso letto sul sito della fonte; registrare titolo, indirizzo, versione e licenza. Non usare come fonte pubblica una sintesi o traduzione scritta con l'intelligenza artificiale.
- I dati del caso si ricavano con uno script dai file originali, conservati intatti nel backup del docente. Lo script controlla la coerenza interna (per esempio i riepiloghi con le righe) e produce i valori di riferimento della guida: non trascrivere numeri a mano.
- Prima di aggiungere un documento al caso, controllare che sia coerente con gli altri: stessa macchina, date compatibili, quantità che tornano. Un'incoerenza non voluta diventa un falso indizio per gli studenti.
- Non indicare come certi i nomi dei comandi dell'interfaccia di Copilot o le funzioni disponibili con l'account studente se non sono verificati: citare la documentazione Microsoft e mettere la prova nella tabella di verifica pre-aula della guida docente.
- Ogni lezione ha un generatore autonomo nella propria cartella `docente/`: non legge file di altre lezioni e funziona su Windows con LibreOffice installato.

## Distribuzione e verifica

- Separare i documenti da distribuire in `studenti/` e le fonti complete, le risposte e le indicazioni riservate in `docente/`. In `studenti/` restano solo i file da pubblicare; sorgenti Markdown, copie in altri formati e fonti del generatore vanno in `studenti/backup/` o `docente/backup/`.
- Se gli studenti devono ricavare il registro in `.md`, non distribuire loro il registro già pronto in quel formato.
- Aggiornare tutti i formati e i riferimenti interessati da una modifica: Markdown, PowerPoint, HTML, Word e PDF quando pertinenti. Non lasciare versioni obsolete concorrenti o collegamenti ai vecchi nomi.
- Verificare apertura e impaginazione con i programmi reali, non soltanto leggendo il sorgente: PowerPoint o LibreOffice per le presentazioni e i documenti, navigazione e leggibilità per l'HTML.
- Controllare che siano conservati i dati del caso, le righe previste, le celle vuote da compilare e il modello grafico. Rimuovere copie e risorse temporanee dopo la verifica.
- Negli spazi da compilare usare tabelle con celle vuote, non righe di trattini bassi: nel Markdown convertito in Word spariscono.
- Prima di rigenerare chiudere i file aperti in PowerPoint o Word, che restano bloccati. L'avviso di Windows «Waiting for printer connection» durante le esportazioni di LibreOffice dipende dalla stampante predefinita non raggiungibile e non blocca la conversione.
- Nei commit, se un file contiene anche modifiche estranee dell'utente, includere solo le righe pertinenti al lavoro svolto.

## Revisione didattica delle nuove lezioni

- Ogni nuova lezione, nuova variante o riprogettazione di un'attività passa dal revisore didattico definito in `.omp/agents/revisore-didattico.md`. Il revisore valuta efficacia, facilità di insegnamento, chiarezza, interattività e copertura delle 2 ore di lezione.
- Il revisore lavora sempre con Claude Opus 5.5 e livello di ragionamento alto, come fissato nel file dell'agente (`model: anthropic/claude-opus-5-5`, `thinking-level: high`). Non sostituirlo con un altro agente o un altro modello, non passare un modello diverso al momento dell'avvio e non aggiungere una voce `revisore-didattico` in `task.agentModelOverrides`. Se il modello non è disponibile, fermarsi e chiedere all'utente.
- Momento: dopo la generazione dei materiali e le verifiche di apertura e impaginazione, prima di dichiarare conclusa la lezione e prima del commit. Nell'incarico indicare la cartella della lezione o della variante, il programma usato e le decisioni dell'utente da rispettare.
- Il revisore non modifica i file: restituisce un rapporto con esito APPROVATA, DA CORREGGERE o DA RIPROGETTARE. L'agente principale applica le correzioni ai problemi bloccanti e importanti in tutti i formati interessati, rigenera i materiali e ripete la revisione finché l'esito è APPROVATA o l'utente decide diversamente.
- Le proposte che cambiano la struttura dell'attività o contraddicono decisioni approvate si presentano all'utente prima di applicarle.
- Riportare all'utente l'esito finale, la stima dei tempi e le verifiche che restano da fare in aula o con l'account studente.

## Contesto della variante attuale della lezione 2

- Cartella: `lezione 2 - 28 ottobre 2026/ipotesi 2 - system prompt e agenti/`.
- Programma: Microsoft Copilot Basic con account scolastico. Per questa attività si usano normali conversazioni, senza richiedere agenti, Blocchi appunti, Copilot dentro Word o acquisti.
- Le istruzioni sono inviate nel primo messaggio; il registro viene incollato in quattro parti nella stessa conversazione, poi si invia `REGISTRO COMPLETO`. Non richiedere l'allegato `.md` come condizione per svolgere il lavoro.
- Il caso P03 comprende quattro pagine e 24 appunti. La tabella Word ha le colonne N. evento, Giorno / data, Ora, Accadimento e Stato P03.
- Le due risposte per le proposte sono «PROPOSTA DA CONTROLLARE» e «SERVE UN CONTROLLO»: non sono strumenti collegati a un gestionale o alla pressa.
- Il resto del corso contiene anche Unsloth Studio: non sostituire quella piattaforma in altre lezioni senza una richiesta specifica.

## Contesto della lezione 3

- Cartella: `lezione 3 - RAG e calcolo deterministico/`. Generatore: `docente/genera_materiali.py`; dati e valori di riferimento: `docente/dati_p03.py`.
- Programma: Microsoft Copilot con account scolastico. Parte 1: le coppie riaprono e mostrano gli agenti creati in aula nella lezione 2 (non hanno consegnato file), senza scrivere nulla. Parte 2: Blocco appunti con i documenti della P03. Parte 3: agente creato dagli studenti con la funzione che esegue Python.
- Ogni studente lavora sul proprio computer. La coppia divide il lavoro per argomento, non per ruolo: chi segue gli allarmi e chi segue i numeri, per tutta la lezione, senza scambi di controllore e scrittore. Chi segue i numeri scrive la scheda di passaggio mentre chi segue gli allarmi scrive le istruzioni dell'agente; poi ognuno legge il testo dell'altro e li correggono insieme. Prova A e Prova B si svolgono nello stesso momento, una per persona, con la richiesta di fault e minuti di fermo per tipo (senza pezzi teorici persi); non si ripete la Prova B, non si scarica il file prodotto dall'agente e non si prova di nuovo dopo l'esempio. L'analisi di che cosa si è perso si scrive in una riga e si discute con tutta la classe insieme all'esempio. Niente risposta individuale.
- `studenti/ATTIVITA_LEZIONE3.docx` è la consegna da leggere: gli studenti non compilano un documento Word, ma consegnano `scheda_passaggio_P03.txt`, `istruzioni_agente_P03.txt` e `proposta_P03.txt`.
- I valori di riferimento della guida docente sono segnaposto fra doppie parentesi graffe in `docente/backup/GUIDA_DOCENTE.md`, riempiti da `dati_p03.py` durante la generazione.
- La macchina è la P03. I diari di gennaio–giugno 2026 derivano dallo zip originale in `docente/backup/fonti/`, dove la macchina era indicata come P-01.
- Il passaggio dal Blocco appunti all'agente è manuale, con la scheda di passaggio scritta dagli studenti. Il rischio di perdere dati e definizioni nel passaggio va reso esplicito: i dati si prendono dal file Excel originale e si confrontano con i riepiloghi mensili.
- Gli studenti progettano prima le proprie istruzioni dell'agente; `studenti/da_pubblicare_dopo_prova_B/ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` si pubblica solo dopo la Prova B.
- Le fonti pubbliche aggiunte al Blocco appunti devono avere una licenza di riuso verificata, registrata in `docente/backup/fonti_online/LICENZE_E_FONTI.md` e citata nella consegna per gli studenti.
- In `studenti/` restano solo i file da distribuire. Sorgenti Markdown, copie in altri formati (PDF, HTML) e fonti del generatore stanno in `studenti/backup/` o `docente/backup/`, che non si pubblicano.

## Contesto della lezione 4

- Cartella: `lezione 4 - reti neurali e agenti con orchestrazione/`, giovedì 12 novembre 2026, 2 ore. Generatore: `docente/genera_materiali.py`. Fonti: `docente/backup/SLIDE_LEZIONE4.md`, `studenti/backup/ATTIVITA_LEZIONE4.md`, `docente/backup/GUIDA_DOCENTE.md`. Il percorso delle lezioni 4–7 è in `docente/backup/BOZZA_PERCORSO_LEZIONI_4-7.md` (lezione 5: 18 novembre; lezione 6: 25 novembre; lezione 7: 2 dicembre, 4 ore, lavoro di gruppo e test finale).
- Programma: Microsoft Copilot con account scolastico, più tre siti che elaborano nel browser (Transformer Explainer, TensorFlow Playground, Flappy Learning). Niente Unsloth Studio: la macchina virtuale con Studio e il modello la prepara il docente a casa e la consegna alla lezione 5. Ciò che resta valido di Studio è in `docente/backup/da_riprendere_lezione_5/NOTE_STUDIO_PER_LEZIONE_5.md`.
- Lavoro singolo: ogni studente lavora da solo sul proprio computer. Niente scambi di postazione né controlli incrociati tra studenti, coppie o gruppi (decisione del docente del 10 novembre 2026, per questa lezione). Niente giro tra i banchi: risultati sullo schermo, criteri rivelati dopo la prova e brevi confronti dal proiettore. Scelta approvata: nessun nuovo cruscotto o servizio.
- Rete: l'indirizzo pubblico della scuola è condiviso. Nella lezione 3 Copilot non ha risposto per circa 10 minuti (ipotesi: limite di richieste per indirizzo). Perciò: solo siti che elaborano nel browser; niente HackMerlin, Prompt Airlines o Gandalf. Transformer Explainer scarica circa 650 MB all'apertura.
- Nulla è stato provato in Copilot con l'account studente: non dichiarare provati la creazione e la modifica dell'agente, la lunghezza massima delle istruzioni o il comportamento degli esempi. L'esempio dell'agente del noleggio (`studenti/da_pubblicare_dopo_collaudo/`) si pubblica dopo il collaudo: non è provato in Copilot e non va presentato come soluzione.
- Lezione 3: svolta il 4 novembre, finita a 1 h 40 min (il revisore aveva stimato circa 141 minuti: le sue stime sono sovrastimate di circa il 30%).
- Caso della lezione 4 (decisione dell'11 novembre 2026): la pressa P03 è stata tolta dalla lezione 4. Gli studenti scrivono l'agente per il noleggio di biciclette Ruota Libera, con tre testi inventati (registro del 7–8 novembre, regole del noleggio, guida ai guasti) e valori di riferimento ricavati da `docente/genera_materiali.py`. La dimostrazione del docente usa una pizzeria d'asporto (`docente/ESEMPIO_DIMOSTRAZIONE_PIZZERIA.txt`). La lezione 3 e il corpus del laboratorio restano sulla P03.
- Il PowerPoint della lezione 4 è modificato a mano dal docente: non rigenerarlo con `genera_materiali.py` senza avvisare. Le slide 1–11 restano com'è; le slide dalla 12 si sostituiscono nel file esistente dopo una copia di sicurezza, a file chiuso.
- Resta un solo file personale: `istruzioni_agente_noleggio.txt`, senza diario delle prove. Primo riscontro dopo la competenza FUORI SERVIZIO, poi seconda competenza a scelta (GUASTI o PASSAGGIO), indice e due esempi di stile propri. Ogni studente inventa due casi critici. Non si consegnano file. Transformer: due bersagli sulle probabilità; Playground: quanti neuroni servono a separare il cerchio, con Test loss sotto 0,05 entro 1.500 Epoch; Flappy: solo dimostrazione del docente, mai «uccellino immortale».

## Perimetro delle modifiche e Git

- Non modificare lezioni o varianti non richieste per uniformarle a una scelta locale.
- Quando l'utente richiede commit e push, includere il lavoro pertinente. Lasciare intatte e fuori dal commit le modifiche estranee non prodotte durante il lavoro, salvo richiesta esplicita di includerle.
- Non ripristinare modifiche dell'utente e non usare push forzati senza autorizzazione.
