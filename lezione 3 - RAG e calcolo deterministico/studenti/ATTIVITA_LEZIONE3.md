# Lezione 3 — L'assistente di reparto della P03

**ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot Basic**

## Che cosa costruite

In questa attività, **assistente di reparto** significa **Microsoft Copilot** con le istruzioni che progettate voi. Aiuta un collega del banco ricambi a consultare i documenti delle presse, identificare i codici corretti e preparare con **Python** la tabella delle confezioni da ordinare. Non è un nuovo programma da installare.

L'assistente prepara risposte e tabelle da verificare: non ordina materiale, non modifica il magazzino e non autorizza riparazioni sulle macchine. Le etichette `PROPOSTA DA CONTROLLARE` e `SERVE UN CONTROLLO` sono indicazioni scritte per una persona, non comandi collegati a un gestionale. I saldi di magazzino descrivono il **19 ottobre 2026 alle ore 08:00**, non il giorno della lezione.

## Che cosa aprire

1. In **Teams**, scaricate `ATTIVITA_LEZIONE3.docx` e `01_DOCUMENTI_P03.txt`.
2. Aprite questa scheda in **Word o LibreOffice Writer** per compilare le tabelle. Il file PDF serve per leggere o stampare la stessa scheda.
3. Aprite `01_DOCUMENTI_P03.txt` con un programma di testo semplice, per esempio **Blocco note** (l'estensione `.txt` indica un file di solo testo). Se il docente indica la versione Word o PDF, usate quella: non caricate più versioni dello stesso fascicolo in Copilot.
4. Aprite **Microsoft Copilot** con l'account scolastico nell'ambiente indicato dal docente.

Lavorate in coppia: una persona usa la tastiera e Copilot, l'altra controlla i documenti e annota i riscontri sulla scheda. Scambiate i compiti tra la preparazione, la prova numerica e il collaudo con i compagni.

## 1. Controllate i documenti e progettate le istruzioni

Il fascicolo `01_DOCUMENTI_P03.txt` riunisce tre documenti con date e funzioni diverse:

- **Documento 1 — Registro della pressa P03 (13–15 ottobre 2026):** i 24 appunti del reparto; il 14 ottobre durante il fermo viene montato il filtro `FLT-992`.
- **Documento 2 — Catalogo dei ricambi ed estratto del manuale della pressa Fervi P001/75:** associa la P03 al filtro `FLT-993` (Revisione 2 del 18 ottobre 2026) e riporta la tabella problemi comuni (pag. 26) e la distinta reale dei **68 ricambi** della pressa `P001/75` (pag. 28, Revisione 1, settembre 2013).
- **Documento 3 — Situazione di magazzino e confezioni di riordino (19 ottobre 2026, ore 08:00):** riporta i pezzi già disponibili a scaffale (saldi chiusi), quanti pezzi contiene una confezione del fornitore e il prezzo di ogni confezione.

Prima di usare Copilot, scegliete **6 ricambi** presenti sia nel Documento 2 sia nel Documento 3 per preparare la dotazione di più presse: **1 filtro** e **5 componenti della pressa P001/75** (includete almeno due componenti che nel manuale hanno nomi ripetuti su più codici, come `O-ring`, `Vite`, `Rondella elastica`, `Rondella` o `Anello di nylon`).

Compilate la tabella leggendo direttamente i documenti: fate attenzione a non confondere le **tre quantità diverse** (pezzi montati su una macchina, pezzi già in magazzino, pezzi dentro una confezione acquistabile).

**Nomi dei due componenti della coppia:** _________________________________________________

| Codice completo | Descrizione e altri codici con lo stesso nome (Doc. 2) | Pezzi su 1 macchina (Doc. 2) | Disponibilità al 19/10 (Doc. 3) | Pezzi per confezione e prezzo (Doc. 3) |
| --- | --- | --- | --- | --- |
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |
| 4. | | | | |
| 5. | | | | |
| 6. | | | | |

### Scrivete le vostre istruzioni in `istruzioni_assistente_P03.txt`

Scrivete con parole vostre le regole di comportamento dell'assistente e salvatele nel file `istruzioni_assistente_P03.txt` (non fate scrivere le istruzioni a Copilot e non ricopiate le tabelle dei documenti dentro le istruzioni). Progettate le regole in modo che l'assistente:

1. **Identifichi i codici e i documenti corretti:** distingua il filtro montato il 14 ottobre nel diario (`FLT-992`) dal filtro previsto dal catalogo del 18 ottobre (`FLT-993`), citando documento e data.
2. **Gestisca le richieste incomplete o ambigue senza indovinare:** nel manuale della pressa `P001/75` la tabella problemi parla genericamente di «tenute» e nella tabella ricambi compaiono più codici con lo stesso nome (`O-ring`, `Vite`, `Rondella elastica`, `Rondella`, `Anello di nylon`). Se un collega chiede un pezzo solo per nome senza indicare il codice esatto, oppure non specifica per quante presse serve il materiale, l'assistente deve fermarsi, elencare i codici omonimi trovati nel Documento 2 e chiedere quale riferimento serve. Se invece la richiesta contiene già codici e quantità, deve procedere subito senza domande inutili.
3. **Esegua il calcolo con Python e produca un file `.csv`:** quando i codici e il numero di presse sono chiari, l'assistente deve usare **Python** (in un ambiente separato chiamato *sandbox*) per calcolare su ogni riga e salvare in un file `.csv` scaricabile:
   - `Fabbisogno = numero di presse × pezzi su 1 macchina (dal Documento 2)`;
   - `Pezzi mancanti = fabbisogno − disponibilità in magazzino (dal Documento 3; zero se la scorta basta)`;
   - `Confezioni da ordinare = pezzi mancanti divisi per i pezzi per confezione, arrotondati per eccesso all'intero successivo`;
   - `Pezzi acquistati = confezioni da ordinare × pezzi per confezione`;
   - `Costo in euro = confezioni da ordinare × prezzo per confezione (IVA esclusa)`.
4. **Indichi che cosa resta da decidere alla persona:** concluda con `PROPOSTA DA CONTROLLARE` quando tutti i dati sono verificati, oppure `SERVE UN CONTROLLO` quando mancano dati, c'è un'ambiguità sui codici o viene chiesta un'autorizzazione tecnica non presente nei testi.

<!-- pagebreak -->

## 2. Provate la vostra richiesta e controllate il file `.csv`

1. Aprite una **nuova conversazione** in Microsoft Copilot. Se usate una chat normale, inviate nel primo messaggio le vostre istruzioni (`istruzioni_assistente_P03.txt`): sono istruzioni inviate dall'utente e vanno rimandate in ogni nuova chat. Se usate un agente, incollatele nel campo **Istruzioni**.
2. Allegate `01_DOCUMENTI_P03.txt` (o inviate il testo integrale dei tre documenti, secondo l'indicazione del docente). Ogni nuova conversazione deve ricevere di nuovo i documenti.
3. Scegliete un numero di presse (per esempio **2, 3 o 4 macchine**) e chiedete all'assistente di verificare la dotazione dei vostri **6 codici** e preparare con Python la tabella `.csv` delle confezioni da ordinare. **Non scrivete nella domanda le quantità del manuale, le scorte o i prezzi:** l'assistente deve ricavarli dal file allegato.
4. Controllate nell'interfaccia di Copilot (come mostrato dal docente) che **Python sia stato realmente eseguito**: vedere codice scritto nel messaggio senza esecuzione non basta.
5. Scaricate il file `.csv` (una tabella di testo apribile con **Excel o LibreOffice Calc**) e controllate a mano almeno **una riga con pezzi mancanti** nella tabella qui sotto.

| Controllo della prova con Python | Da compilare |
| --- | --- |
| Richiesta inviata e numero di presse scelto | |
| Come abbiamo verificato che Python è stato eseguito e nome del file `.csv` scaricato | |
| **Controllo manuale di 1 riga:** codice scelto, fabbisogno (`presse × pezzi su 1 macchina`), scorta (Doc. 3) e pezzi mancanti | |
| **Controllo confezioni e costo della stessa riga:** pezzi per confezione, confezioni arrotondate per eccesso e costo in euro confrontati col `.csv` | |
| Se un numero non tornava, quale errore abbiamo trovato (documento letto male, quantità confusa, formula sbagliata)? | |

## 3. Collaudo incrociato con un'altra coppia e revisione

Ora scambiate i compiti: ogni coppia mette alla prova l'assistente di un'altra coppia con una conversazione in **due mosse**:

- **Mossa 1 (richiesta ambigua su pezzi omonimi):** chiedete di preparare il materiale per un certo numero di presse nominando almeno un ricambio solo con la descrizione generale ripetuta nel manuale (per esempio *«gli O-ring e le rondelle elastiche»*, oppure *«le tenute per una perdita d'olio e le viti»*), **senza scrivere il codice `P001/75/...`**. Controllate se l'assistente si ferma, mostra i codici omonimi del Documento 2 e chiede quale riferimento intendete.
- **Mossa 2 (precisazione dei codici e ricalcolo Python):** rispondete nella stessa conversazione indicando i codici completi scelti da voi (diversi da quelli già provati dai compagni) e cambiando il numero di presse. Controllate che l'assistente esegua di nuovo Python e aggiorni la tabella `.csv`.

La **coppia A** apre sul proprio computer una conversazione nuova con le proprie istruzioni e `01_DOCUMENTI_P03.txt`. La **coppia B** si siede al computer di A (senza cambiare account), esegue le due mosse e compila la tabella qui sotto nella scheda di A, mentre A osserva senza suggerire. Poi invertite i ruoli sul computer di B.

| Collaudo svolto dai compagni (da compilare nella scheda di chi ha creato l'assistente) | Da compilare |
| --- | --- |
| Nomi della coppia che ha svolto il collaudo | |
| **Mossa 1 (richiesta ambigua inviata):** come ha risposto l'assistente davanti al nome generico senza codice? | |
| **Mossa 2 (codici precisati e nuovo numero di presse):** verifica di una riga calcolata da Python (fabbisogno, scorta, confezioni, costo) | |
| **Decisione della coppia progettista dopo il collaudo:** quale regola di `istruzioni_assistente_P03.txt` conserviamo o modifichiamo, e perché? | |

*Se modificate una regola delle istruzioni, scrivete una regola generale (non la risposta pronta alla singola domanda) e riprovate aprendo una conversazione nuova con istruzioni e documenti.*

## 4. Risposta individuale, senza Copilot

Ciascuno risponde da solo, con parole proprie e senza usare Copilot, facendo riferimento alle prove svolte.

| Primo componente | Risposta |
| --- | --- |
| Nome | |
| Quale codice avete controllato nei documenti? Perché la sola parola «O-ring», «Vite» o «filtro» non basta e quali date/revisioni contano? | |
| Spiega con un esempio della vostra prova la differenza tra le tre quantità (manuale, magazzino, confezione) e quale decisione resta a una persona. | |

| Secondo componente | Risposta |
| --- | --- |
| Nome | |
| Quale codice avete controllato nei documenti? Perché la sola parola «O-ring», «Vite» o «filtro» non basta e quali date/revisioni contano? | |
| Spiega con un esempio della vostra prova la differenza tra le tre quantità (manuale, magazzino, confezione) e quale decisione resta a una persona. | |

## Che cosa consegnare su Teams

Caricate su Teams:

1. questa scheda `ATTIVITA_LEZIONE3.docx` compilata in tutte le tabelle;
2. il file `istruzioni_assistente_P03.txt` con le vostre istruzioni finali;
3. il file `.csv` con la tabella dei risultati prodotta da Python e verificata da voi.

Indicate nella scheda se ogni passaggio è stato eseguito direttamente da voi, osservato nella dimostrazione del docente o controllato sui documenti. Un risultato calcolato a mano non va dichiarato come esecuzione di Python.
