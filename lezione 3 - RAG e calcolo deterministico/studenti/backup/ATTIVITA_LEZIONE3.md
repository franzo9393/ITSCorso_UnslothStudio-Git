# Lezione 3 — Dai diari della P03 a numeri controllati

**ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot con l'account scolastico**

## La domanda del responsabile

Il responsabile del reparto presse vi chiede: **«Su quale problema della pressa P03 conviene intervenire per primo?»**

Avete i diari della P03 da gennaio a giugno 2026 e alcuni documenti del reparto. Alla fine della lezione scriverete una proposta motivata, con numeri controllati e documenti citati. La decisione finale resta al responsabile.

Nei diari un **fault** è un arresto automatico della pressa causato da un allarme.

Lavorate in coppia: una persona usa Copilot, l'altra controlla i documenti e compila questa scheda. Scambiatevi i compiti all'inizio di ogni parte.

**Nomi della coppia:** _________________________________________________

## Parte 1 — Le istruzioni della lezione 2

Aprite **Teams** e riaprite i file che avete consegnato il 28 ottobre: `istruzioni_P03.txt` e `verifica_P03.md`. Se avete creato un agente in Copilot, apritelo.

Rileggete le istruzioni e le prove che avete fatto, poi rispondete. Il docente chiederà ad alcune coppie di mostrare le risposte alla classe.

| Domanda | Risposta |
| --- | --- |
| Quale regola delle istruzioni ha funzionato? Da quale risposta di Copilot ve ne siete accorti? | |
| In quale caso Copilot non ha seguito le istruzioni o ha dato una risposta sbagliata? | |
| Che cosa cambiereste oggi nelle istruzioni, e perché? | |

<!-- pagebreak -->

## Parte 2 — Cercare nei documenti con il Blocco appunti

Il **Blocco appunti** è uno spazio di Microsoft Copilot in cui raccogliete i documenti di un lavoro. Quando fate una domanda, Copilot cerca le parti utili in quei documenti, risponde e indica da dove ha preso le informazioni.

### Preparate il Blocco appunti

1. In **Teams** scaricate la cartella `Documenti_P03_Blocco_appunti`. Contiene i sei diari della P03, la guida agli allarmi, le regole di calcolo degli indicatori, il registro del 13–15 ottobre 2026 e alcuni documenti pubblici su presse, sensori e sicurezza.
2. Aprite **Microsoft Copilot** con l'account scolastico e create un nuovo Blocco appunti chiamato `P03 diari e documenti`.
3. Aggiungete come riferimenti **tutti** i file della cartella. Controllate che nell'elenco del Blocco appunti compaiano tutti.
4. Aprite anche voi i documenti in Word: vi servono per controllare le risposte.

### Fate le vostre domande

Scrivete voi le domande. Con le risposte dovete scoprire:

- che cosa significano gli allarmi della P03 e chi interviene;
- come il reparto calcola i numeri del riepilogo che compare in testa a ogni diario;
- un'informazione che si ottiene solo mettendo insieme due documenti diversi;
- quanti fault di ogni tipo ci sono in **un mese scelto da voi**.

Per ogni risposta aprite il documento citato e controllate. Per il mese scelto contate i fault a mano nel diario Word e confrontate il totale con il riepilogo in testa al diario.

| La vostra domanda | Risposta in breve | Documento citato | Controllo sul documento: giusta, sbagliata o incompleta? |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

**Conteggio di un mese**

| Mese scelto | Fault secondo il Blocco appunti | Fault contati a mano nel diario | Fault nel riepilogo del diario |
| --- | --- | --- | --- |
| | | | |

Ora chiedete al Blocco appunti di contare i fault di tutti i sei mesi, divisi per tipo.

| Potete controllare questa risposta a mano in tempi ragionevoli? Perché? |
| --- |
| |

<!-- pagebreak -->

### Scrivete la scheda di passaggio

Nella Parte 3 lavorerete con un **agente**: una versione di Copilot con istruzioni salvate. L'agente **non vede** il vostro Blocco appunti. Conosce soltanto quello che gli consegnate.

La **scheda di passaggio** è il testo che scrivete per consegnargli il lavoro. Decidete voi che cosa metterci. Una persona che non ha visto il vostro Blocco appunti, leggendo la scheda, deve capire:

- a quale domanda rispondere e per quale periodo;
- quali definizioni usare per i calcoli, con il documento da cui vengono;
- quali dati servono e in quale file si trovano;
- quali controlli fare sui risultati;
- in che forma volete la risposta.

Potete copiare parti delle risposte del Blocco appunti, ma solo dopo averle controllate. Se riportate numeri trovati dal Blocco appunti, scrivete accanto «da verificare».

Aprite **Blocco note**, scrivete la scheda e salvatela come `scheda_passaggio_P03.txt`. L'estensione `.txt` indica un file di solo testo.

<!-- pagebreak -->

## Parte 3 — Contare e calcolare con un agente che usa Python

**Python** è un linguaggio di programmazione. L'agente di Copilot può scrivere codice Python, eseguirlo e leggere tutte le righe di un file Excel.

### Progettate l'agente

Prima di aprire Copilot, decidete come deve lavorare il vostro agente.

| Domanda di progetto | Le vostre decisioni |
| --- | --- |
| Che compito ha l'agente? | |
| Che cosa riceve dall'utente? | |
| Che cosa non deve fare? | |
| Come controlla i propri risultati? | |
| Come presenta la risposta? | |

Scrivete le istruzioni dell'agente con parole vostre e salvatele con Blocco note come `istruzioni_agente_P03.txt`.

### Create l'agente

1. In Microsoft Copilot create un nuovo agente, nel modo mostrato dal docente.
2. Dategli un nome e incollate nel campo delle istruzioni il testo di `istruzioni_agente_P03.txt`.
3. Attivate la funzione che esegue Python: **Interprete di codice**, oppure **Code interpreter** se compare in inglese.
4. Salvate l'agente.

### Prova A — Solo la scheda di passaggio

1. Aprite una nuova conversazione con il vostro agente.
2. Incollate la scheda di passaggio. **Non allegate** altri file.
3. Chiedete il numero di fault, i minuti di fermo e i pezzi teorici persi per ogni tipo di fault, da gennaio a giugno 2026.
4. Annotate i risultati nella tabella dopo la Prova B.

### Prova B — La scheda di passaggio e il file Excel

1. Scaricate da **Teams** il file `Diari_P03_gennaio_giugno_2026.xlsx`. Contiene gli stessi dati dei sei diari Word, con un foglio per ogni mese.
2. Aprite una **nuova** conversazione con lo stesso agente.
3. Incollate la stessa scheda di passaggio, allegate il file Excel e fate la stessa richiesta della Prova A.
4. Controllate nell'interfaccia di Copilot, come mostrato dal docente, che Python sia stato **eseguito davvero**. Un codice soltanto scritto nel messaggio non basta.
5. Se l'agente produce un file Excel o `.csv`, scaricatelo e apritelo in Excel o LibreOffice Calc.

| Che cosa confrontate | Prova A | Prova B | Riepiloghi dei diari | Coincidono? |
| --- | --- | --- | --- | --- |
| Fault totali da gennaio a giugno | | | | |
| Minuti di fermo per fault da gennaio a giugno | | | | |
| Fault del mese scelto nella Parte 2 | | | | |
| Minuti di fermo dello stesso mese | | | | |
| Tipo di fault con più minuti di fermo | | | non presente | |

Per la colonna «Riepiloghi dei diari» sommate voi i valori stampati in testa ai sei diari.

<!-- pagebreak -->

### Che cosa si è perso nel passaggio

| Domanda | Risposta |
| --- | --- |
| Nella Prova A, quali numeri l'agente ha calcolato davvero e quali ha solo ripreso dalla scheda? | |
| Se un numero della Prova B non coincide con i riepiloghi: dove sta la differenza (righe mancanti, definizione diversa, file letto male)? | |
| Quale informazione mancava nella scheda di passaggio o nelle istruzioni? Come l'avete corretta? | |

Se correggete la scheda o le istruzioni, scrivete una regola generale, non la risposta a una sola domanda. Poi ripetete la Prova B in una nuova conversazione.

### Confronto con le istruzioni di esempio

Dopo la Prova B trovate su **Teams** il file `ESEMPIO_ISTRUZIONI_AGENTE_P03.txt`. Leggetelo e confrontatelo con le vostre istruzioni.

| Domanda | Risposta |
| --- | --- |
| Che cosa c'è nell'esempio che manca nelle vostre istruzioni? | |
| Che cosa avete previsto voi e l'esempio no? | |
| Quale versione tenete, o quali parti unite? Perché? | |

Provate la versione scelta in una nuova conversazione, con la scheda di passaggio e il file Excel.

### La proposta al responsabile

Scrivete qui una proposta di al massimo otto righe. Indicate:

- il problema o la parte della macchina da affrontare per primo;
- almeno due numeri controllati e da quale prova vengono;
- almeno un documento del Blocco appunti che sostiene la scelta;
- che cosa resta da decidere al responsabile.

| Proposta al responsabile di reparto |
| --- |
| |

<!-- pagebreak -->

## Risposta individuale, senza Copilot

Ciascuno risponde da solo, con parole proprie, facendo riferimento alle prove svolte.

| Primo componente | Risposta |
| --- | --- |
| Nome | |
| Perché la sola scheda di passaggio non basta per far calcolare l'agente? Fai un esempio dalla vostra prova. | |
| Quale numero dell'agente hai controllato, con che cosa l'hai confrontato e che cosa hai scoperto? | |

| Secondo componente | Risposta |
| --- | --- |
| Nome | |
| Perché la sola scheda di passaggio non basta per far calcolare l'agente? Fai un esempio dalla vostra prova. | |
| Quale numero dell'agente hai controllato, con che cosa l'hai confrontato e che cosa hai scoperto? | |

## Che cosa consegnare su Teams

1. Questa scheda `ATTIVITA_LEZIONE3.docx`, compilata.
2. `scheda_passaggio_P03.txt` nella versione finale.
3. `istruzioni_agente_P03.txt` nella versione finale.
4. Il file Excel o `.csv` prodotto dall'agente nella Prova B, se l'agente lo ha creato.

Prima di consegnare, indicate come è stato svolto ogni passaggio: eseguito da voi, osservato nella dimostrazione del docente oppure controllato solo sui documenti. Un conteggio fatto a mano non va dichiarato come risultato di Python.

| Passaggio | Come è stato svolto |
| --- | --- |
| Blocco appunti con tutti i documenti | |
| Agente creato con la funzione che esegue Python | |
| Prova A | |
| Prova B con Python eseguito | |

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
