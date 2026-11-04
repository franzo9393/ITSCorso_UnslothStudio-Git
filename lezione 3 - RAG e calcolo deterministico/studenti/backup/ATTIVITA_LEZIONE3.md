# Lezione 3 — Dai diari della P03 a numeri controllati

**ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot con l'account scolastico**

## La domanda del responsabile

Il responsabile del reparto presse vi chiede: **«Su quale problema della pressa P03 conviene intervenire per primo?»**

Avete i diari della P03 da gennaio a giugno 2026 e alcuni documenti del reparto. Alla fine della lezione consegnerete una proposta motivata, con numeri controllati e documenti citati. La decisione finale resta al responsabile.

Nei diari un **fault** è un arresto automatico della pressa causato da un allarme.

## Come lavorate in coppia

Lavorate in coppia, ognuno sul proprio computer e con il proprio account scolastico. All'inizio decidete chi segue gli **allarmi** e chi segue i **numeri**. I compiti restano gli stessi per tutta la lezione:

- chi segue gli **allarmi** scopre che cosa significano gli allarmi della P03, chi interviene e che cosa dicono i documenti del reparto;
- chi segue i **numeri** scopre come il reparto calcola il riepilogo dei diari e controlla i conteggi.

Nella Parte 3 chi segue i numeri scrive la scheda di passaggio e chi segue gli allarmi le istruzioni dell'agente; poi le correggete insieme. La proposta finale la scrivete insieme.

In questo documento non c'è niente da compilare: quello che scrivete va nei file di testo indicati passo per passo.

## Parte 1 — Gli agenti della lezione 2

Chi ha creato l'agente nella lezione del 28 ottobre lo apre in **Microsoft Copilot** sul proprio computer, con l'account scolastico; il compagno guarda con lui. Rileggete insieme le istruzioni che gli avete dato.

Aprite una nuova conversazione con l'agente e fategli una domanda di prova scelta da voi. Preparatevi a dire alla classe quale istruzione ha funzionato, quale no e che cosa cambiereste oggi. Il docente chiederà ad alcune coppie di mostrare il proprio agente al proiettore.

Se non trovate l'agente, guardate quello di una coppia vicina, insieme a loro.

<!-- pagebreak -->

## Parte 2 — Cercare nei documenti con il Blocco appunti

Il **Blocco appunti** è uno spazio di Microsoft Copilot in cui raccogliete i documenti di un lavoro. Quando fate una domanda, Copilot cerca le parti utili in quei documenti, risponde e indica da dove ha preso le informazioni.

### Preparate il Blocco appunti, ognuno sul proprio computer

1. In **Teams** scaricate la cartella `Documenti_P03_Blocco_appunti`. Contiene i sei diari della P03, la guida agli allarmi, le regole di calcolo degli indicatori, il registro del 13–15 ottobre 2026 e alcuni documenti pubblici su presse, sensori e sicurezza. Teams la scarica come file compresso `.zip`: estraete i file sul computer.
2. Aprite **Microsoft Copilot** con l'account scolastico e create un nuovo Blocco appunti chiamato `P03 diari e documenti`.
3. Aggiungete come riferimenti **tutti** i file della cartella, caricandoli dal computer. Controllate che nell'elenco del Blocco appunti compaiano tutti.
4. Tenete aperti anche i documenti sul computer, in Word o come PDF: vi servono per controllare le risposte.

### Fate le vostre domande

Scrivete voi le domande al Blocco appunti, ognuno sul proprio argomento.

**Chi segue gli allarmi** deve scoprire:

- che cosa significano gli allarmi della P03 e chi interviene;
- un'informazione che si ottiene solo mettendo insieme due documenti diversi.

**Chi segue i numeri** deve scoprire:

- come il reparto calcola i numeri del riepilogo che compare in testa a ogni diario;
- quanti fault ci sono in **un mese scelto da voi**. Contateli nel diario Word con la ricerca (tasti Ctrl+F): cercate la parola FAULT e contate solo i risultati che stanno nella colonna Evento della tabella. Confrontate il totale con la risposta del Blocco appunti e con il riepilogo in testa al diario.

Per ogni risposta aprite il documento citato e controllate che dica davvero quella cosa. Prendete appunti come preferite, su carta o al computer: vi serviranno per la scheda di passaggio e non si consegnano.

Alla fine chi segue i numeri chiede al Blocco appunti di contare i fault di tutti i sei mesi, divisi per tipo. Discutete insieme: potete controllare questa risposta a mano? Che cosa vi servirebbe per farlo?

<!-- pagebreak -->

## Parte 3 — Contare e calcolare con un agente che usa Python

**Python** è un linguaggio di programmazione. L'agente di Copilot può scrivere codice Python, eseguirlo e leggere tutte le righe di un file Excel.

Lavorerete con un **agente**: una versione di Copilot con istruzioni salvate. L'agente **non vede** il vostro Blocco appunti. Conosce soltanto quello che gli consegnate.

### Due testi, scritti nello stesso momento

Ognuno scrive un testo sul proprio computer con **Blocco note**, il programma di Windows per i file di solo testo (da non confondere con il Blocco appunti di Copilot). L'estensione `.txt` indica un file di solo testo.

**Chi segue i numeri scrive la scheda di passaggio** e la salva come `scheda_passaggio_P03.txt`. È il testo che consegna il lavoro all'agente. Decidete voi che cosa metterci. Una persona che non ha visto il vostro Blocco appunti, leggendo la scheda, deve capire:

- a quale domanda rispondere e per quale periodo;
- quali definizioni usare per i calcoli, con il documento da cui vengono;
- quali dati servono e in quale file si trovano;
- quali controlli fare sui risultati;
- in che forma volete la risposta.

Potete copiare parti delle risposte del Blocco appunti, ma solo dopo averle controllate. Se riportate numeri trovati dal Blocco appunti, scrivete accanto «da verificare». In fondo alla scheda scrivete la richiesta che farete all'agente nelle due prove: il numero di fault e i minuti di fermo per ogni tipo di fault, da gennaio a giugno 2026.

**Chi segue gli allarmi scrive le istruzioni dell'agente**, con parole proprie, e le salva come `istruzioni_agente_P03.txt`. Le istruzioni dicono:

- che compito ha l'agente;
- che cosa riceve dall'utente;
- che cosa non deve fare;
- come controlla i propri risultati;
- come presenta la risposta.

### Leggete il testo del compagno e correggete insieme

Mandatevi i due file nella chat di Teams. Ognuno legge il testo dell'altro:

- chi segue gli allarmi aggiunge alla scheda quello che ha trovato su allarmi e documenti del reparto e controlla che si capisca senza aver visto il Blocco appunti;
- chi segue i numeri controlla che le istruzioni facciano lavorare l'agente con le definizioni e i controlli scritti nella scheda.

Correggete insieme e salvate la versione finale dei due file. Alla fine ognuno deve avere entrambi i file sul proprio computer.

### Create l'agente, ognuno sul proprio computer

1. In Microsoft Copilot create un nuovo agente, nel modo mostrato dal docente.
2. Dategli un nome e incollate nel campo delle istruzioni il testo di `istruzioni_agente_P03.txt`.
3. Controllate che sia attiva la funzione che esegue Python: **Interprete di codice**, oppure **Code interpreter** se compare in inglese. Se non trovate un interruttore, la funzione è già inclusa nell'agente.
4. Salvate l'agente.

### Le due prove, nello stesso momento

Chi segue gli allarmi fa la Prova A, chi segue i numeri fa la Prova B. Ognuno usa il proprio agente e la stessa richiesta, quella scritta in fondo alla scheda di passaggio.

**Prova A — Solo la scheda di passaggio.** La fa chi segue gli allarmi.

1. Aprite una nuova conversazione con il vostro agente.
2. Incollate la scheda di passaggio, con la richiesta in fondo, e inviatela. **Non allegate** altri file.
3. Osservate quali numeri l'agente calcola davvero, quali riprende dalla scheda e quali dice di non poter dare.
4. Finita la prova, aprite **Blocco note**, create il file `proposta_P03.txt` e scrivete in cima i vostri nomi. Poi sommate i fault e i minuti di fermo per fault stampati in testa ai sei diari: sono i riepiloghi, il vostro punto di controllo. Scrivete i due totali nel file.

**Prova B — La scheda di passaggio e il file Excel.** La fa chi segue i numeri.

1. Scaricate da **Teams** il file `Diari_P03_gennaio_giugno_2026.xlsx`. Contiene gli stessi dati dei sei diari Word, con un foglio per ogni mese.
2. Aprite una **nuova** conversazione con il vostro agente.
3. Incollate la stessa scheda di passaggio, allegate il file Excel e inviate.
4. Controllate nell'interfaccia di Copilot, come mostrato dal docente, che Python sia stato **eseguito davvero**. Un codice soltanto scritto nel messaggio non basta.

### Confrontate i numeri con i riepiloghi

Mettete i due computer uno accanto all'altro. Le prove danno i valori per tipo di fault: sommate i valori di ciascuna prova; se l'agente ha dato solo un totale, usate quello. In `proposta_P03.txt`, accanto ai totali dei riepiloghi, scrivete il totale della Prova A, il totale della Prova B e se coincidono:

- fault totali da gennaio a giugno;
- minuti di fermo per fault da gennaio a giugno.

La somma controlla i totali, non la divisione per tipo: un fault messo nel tipo sbagliato non la cambia. Se nella proposta usate un numero per tipo, scrivete accanto che ha superato solo il controllo della somma.

Se l'agente non ha dato un numero, scrivete «non dato». Se un numero non viene da una prova eseguita da voi, scrivetelo accanto: «osservato nella dimostrazione del docente» oppure «controllato solo sui documenti». Un conteggio fatto a mano non va dichiarato come risultato di Python.

### Che cosa si è perso nel passaggio

Scrivete in `proposta_P03.txt`, in una riga, quale informazione mancava nella scheda di passaggio o nelle istruzioni oppure, se i numeri tornano, quale parte della scheda ha permesso all'agente di calcolarli giusti. Del resto si parla con tutta la classe, insieme alle istruzioni di esempio.

Se correggete la scheda o le istruzioni, non cancellate il testo di prima: scrivete la correzione in fondo al file, sotto la riga «Correzioni dopo le prove», nei file sul computer di chi segue gli allarmi, che li consegna. Scrivete una regola generale, non la risposta a una sola domanda.

### Le istruzioni di esempio

Dopo la Prova B il docente pubblica su **Teams** il file `ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` e lo discute con tutta la classe.

Non cambiate quello che avete scritto prima. Se decidete di aggiungere qualcosa, scrivetelo in fondo a `istruzioni_agente_P03.txt`, sul computer di chi segue gli allarmi, sotto la riga «Aggiunte dopo l'esempio», con una frase che spiega perché.

### La proposta al responsabile

In `proposta_P03.txt`, dopo i numeri, scrivete una proposta di al massimo otto righe. Indicate:

- il problema o la parte della macchina da affrontare per primo;
- almeno due numeri controllati, con la prova da cui vengono e il controllo che hanno superato;
- almeno un documento del Blocco appunti che sostiene la scelta;
- che cosa resta da decidere al responsabile.

## Che cosa consegnare su Teams

Chi segue gli allarmi carica i file per la coppia, nel compito su Teams indicato dal docente:

1. `scheda_passaggio_P03.txt` nella versione finale;
2. `istruzioni_agente_P03.txt`, con le eventuali aggiunte dopo l'esempio;
3. `proposta_P03.txt`.

## Provenienza dei documenti

I diari della P03, la guida agli allarmi IO-P03-07, le regole PR-IND-03 e il registro di ottobre sono documenti inventati per l'esercitazione ITS MAKER.

I file che iniziano con `E0` sono documenti pubblici riprodotti senza modifiche. Spiegano principi generali, non la pressa P03:

| File | Titolo, autore e licenza |
| --- | --- |
| `E01_EU-OSHA_Manutenzione_Sicura.pdf` | *Manutenzione sicura — Lavoratori sicuri*, Facts 88, Agenzia europea per la sicurezza e la salute sul lavoro (EU-OSHA), 2010. Riproduzione autorizzata con citazione della fonte. |
| `E02_Wikipedia_Pressa.pdf` | *Pressa*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E03_Wikipedia_Oleodinamica.pdf` | *Oleodinamica*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E04_Wikipedia_Fluido_Idraulico.pdf` | *Fluido idraulico*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E05_Wikipedia_Pressostato.pdf` | *Pressostato*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E06_Wikipedia_Sensore_Fotoelettrico.pdf` | *Sensore fotoelettrico*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E07_Wikipedia_Sensore_di_Prossimita.pdf` | *Sensore di prossimità*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |
| `E08_Wikipedia_Scambiatore_di_calore.pdf` | *Scambiatore di calore*, autori di Wikipedia, it.wikipedia.org. Licenza CC BY-SA 4.0. |

Ogni file di Wikipedia riporta in fondo l'indirizzo della versione usata. Testo della licenza: https://creativecommons.org/licenses/by-sa/4.0/deed.it
