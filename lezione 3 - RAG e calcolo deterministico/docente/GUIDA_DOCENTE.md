# Guida docente — L'assistente di reparto della P03

**ITS MAKER Bologna · Lezione 3 · 4 novembre 2026 · Microsoft Copilot Basic**

Documento riservato al docente: regia, preparazione, riscontri sulle fonti e calcoli di riferimento. Agli studenti si distribuiscono soltanto i materiali della cartella `studenti/` e le slide.

## 1. Scopo e struttura dell'attività

Le coppie progettano e collaudano un assistente per il banco ricambi del reparto presse usando **Microsoft Copilot**: consultare tre documenti con date e funzioni diverse, gestire le omonimie reali di una distinta ricambi senza tirare a indovinare e far calcolare a **Python** il fabbisogno, i pezzi mancanti, le confezioni intere da ordinare e la spesa in euro, esportando una tabella `.csv`.

Rispetto alla versione precedente, il fascicolo `01_DOCUMENTI_P03.txt` conserva integralmente i 24 appunti della P03 e il catalogo filtri (`FLT-992` storico del 14/10, `FLT-993` e `FLT-229` a catalogo rev. 2 del 18/10), ma integra nel Documento 2 l'**estratto autentico del Manuale d'uso e manutenzione della Pressa idraulica Fervi Art. P001/75** (Revisione 1, settembre 2013, pagg. 26 e 28: tabella problemi comuni e distinta dei 68 ricambi) e nel Documento 3 la **situazione di magazzino al 19 ottobre 2026 ore 08:00** con scorte, pezzi per confezione e prezzi per confezione.

L'attività è organizzata in **tre passaggi operativi** più la risposta individuale finale:

1. **Esplorazione delle fonti e progettazione delle istruzioni:** le coppie scelgono 6 ricambi (1 filtro + 5 voci della pressa `P001/75`, includendo almeno due voci con descrizioni ripetute su più codici), verificano i tre diversi significati di quantità (pezzi montati su 1 macchina, disponibilità a magazzino, pezzi per confezione) e scrivono `istruzioni_assistente_P03.txt`.
2. **Esecuzione del calcolo con Python e verifica del `.csv`:** in una conversazione nuova allegano `01_DOCUMENTI_P03.txt`, chiedono il calcolo per più presse sui 6 codici scelti, verificano che Python sia stato realmente eseguito nella *sandbox*, scaricano il `.csv` e controllano a mano almeno una riga completa.
3. **Collaudo incrociato in due mosse e revisione:** la coppia B prova l'assistente della coppia A prima con una richiesta ambigua priva di codice (per esempio nominando solo «O-ring», «rondelle elastiche» o «tenute per perdita d'olio») e poi fornendo i codici completi e un nuovo numero di presse per verificare il ricalcolo in Python.

## 2. Che cosa è osservato e che cosa resta da provare

Nella prova preparatoria il docente ha osservato nel proprio agente l'esecuzione di Python e la produzione di un file `.csv` scaricabile. Questo non dimostra ancora la lettura degli allegati con il nuovo fascicolo, né la disponibilità sulle postazioni degli studenti.

Prima dell'aula usare un vero account studente senza attivare acquisti o consumi a pagamento.

| Verifica pre-aula | Che cosa controllare | Esito e data |
| --- | --- | --- |
| Apertura dell'ambiente indicato | Accesso con account studente senza acquisti; invio istruzioni | |
| Lettura del fascicolo `01_DOCUMENTI_P03` | Codici, quantità per macchina, scorte e confezioni ricavati dal file allegato | |
| Risposta su voce omonima (`O-ring`, `Vite`, `Rondella elastica`) | Elenco dei codici omonimi presenti nel Documento 2 e richiesta di chiarimento | |
| Esecuzione di Python nello stesso ambiente | Dettagli ispezionabili del codice eseguito, arrotondamento per eccesso delle confezioni | |
| Salvataggio del file `.csv` | File realmente scaricabile, apribile in Excel o LibreOffice Calc e coerente coi dati | |
| Nuova conversazione | Documenti e istruzioni forniti di nuovo per il collaudo incrociato | |

Prima delle prove mostrare dove leggere i dettagli dell'esecuzione di Python nell'interfaccia: un blocco di codice soltanto scritto nel messaggio non dimostra che Python sia stato eseguito.

## 3. Materiali, distribuzione e nota sui diritti

Distribuire tramite Teams:

- `studenti/ATTIVITA_LEZIONE3.docx`, scheda snella da compilare in Word o LibreOffice Writer (il PDF è per lettura o stampa);
- `studenti/01_DOCUMENTI_P03.txt`, fascicolo unico dei tre documenti (con equivalenti `.docx` e `.pdf`);
- `Lezione3_Assistente_Reparto_P03_ITS_MAKER.pptx` (oppure versione HTML autosufficiente o PDF).

Scegliere prima dell'aula un solo formato del fascicolo accettato da Copilot e non far caricare più copie dello stesso documento. Non è richiesto un passaggio separato su Copilot Blocchi appunti: si lavora in un unico ambiente dall'inizio alla fine.

**Nota sulla provenienza delle fonti:** il Documento 1 è il diario didattico della P03; la tabella dei 68 ricambi e dei problemi comuni nel Documento 2 è un estratto testuale di dati fattuali dal manuale pubblico Fervi `Art. P001/75` (Rev. 1, settembre 2013, pagg. 26 e 28); il Documento 3 riporta saldi di magazzino, confezioni e prezzi simulati e dichiarati per l'esercitazione. Non presentare la P03 come se fosse una pressa Fervi P001/75 e non ridistribuire l'intero PDF commerciale del costruttore senza le verifiche della scuola.

## 4. Regia per i tre blocchi di lavoro

### Blocco 1 — Fonti, omonimie e scrittura delle istruzioni

Far aprire `ATTIVITA_LEZIONE3.docx` e `01_DOCUMENTI_P03.txt`. Prima di aprire Copilot, ogni coppia sceglie i propri 6 codici e compila la prima tabella leggendo i testi.

Guidare gli studenti a notare tre fatti documentali:

1. **Tre quantità con significato diverso:**
   - nel Documento 2 (`Quantità nella macchina`), il numero indica quanti pezzi sono montati su **una sola pressa** (per esempio `P001/75/05` ha 42 rondelle elastiche per macchina);
   - nel Documento 3 (`Disponibilità`), il numero indica quanti pezzi singoli sono già presenti **a magazzino** al 19 ottobre 2026 ore 08:00;
   - nel Documento 3 (`Pezzi per confezione`), il numero indica quanti pezzi contiene **una confezione venduta dal fornitore**.
2. **Omonimie nella distinta reale (pag. 28) e genericità della tabella guasti (pag. 26):**
   - a pag. 26, per «Perdita d'olio», il manuale prescrive «Sostituite le tenute» senza indicare alcun codice;
   - a pag. 28 compaiono più codici con la stessa descrizione (`O-ring`, `Vite`, `Rondella elastica`, `Rondella`, `Anello di nylon`, `Piastra connessione`, `Perno`, `Leva`, `Tubo dell'aria`, `Cavo`). Senza il codice completo l'assistente non deve indovinare quale pezzo calcolare.
3. **Filtro storico contro filtro a catalogo:**
   - il 14 ottobre sulla P03 è stato montato `FLT-992` (Documento 1), mentre il catalogo rev. 2 del 18 ottobre associa la P03 a `FLT-993` (Documento 2). Entrambi sono a magazzino nel Documento 3 (`FLT-992`: 5 pezzi; `FLT-993`: 8 pezzi).

Le coppie scrivono da sole `istruzioni_assistente_P03.txt`. Non distribuire prompt pronti.

### Blocco 2 — Calcolo con Python e controllo del `.csv`

Ogni coppia apre una conversazione nuova, fornisce `istruzioni_assistente_P03.txt` e `01_DOCUMENTI_P03.txt`, e invia la richiesta per i propri 6 codici su $N$ presse (per esempio 2, 3 o 4 macchine), senza scrivere nella domanda le quantità del manuale, le scorte o i prezzi.

Far verificare la catena del calcolo che Python deve eseguire per ogni riga:

- `Fabbisogno = N_presse × Quantità_nella_macchina`
- `Pezzi_mancanti = max(0, Fabbisogno − Disponibilità_magazzino)`
- `Confezioni_da_ordinare = arrotondamento per eccesso (Pezzi_mancanti / Pezzi_per_confezione)`
- `Pezzi_acquistati = Confezioni_da_ordinare × Pezzi_per_confezione`
- `Costo_euro = Confezioni_da_ordinare × Prezzo_per_confezione`

Gli studenti scaricano il `.csv`, lo aprono in Excel o LibreOffice Calc e controllano a mano sulla scheda una riga con pezzi mancanti.

### Blocco 3 — Collaudo incrociato in due mosse e chiusura

Ogni coppia apre una nuova conversazione pulita con le proprie istruzioni e `01_DOCUMENTI_P03.txt`. La coppia vicina si siede alla postazione (senza cambiare account) ed esegue le due mosse:

1. **Mossa 1:** invia una richiesta con almeno un nome generico omonimo (per esempio *«Prepariamo i ricambi per 3 presse: servono gli O-ring, le rondelle elastiche e il filtro della P03»*) senza indicare i codici `P001/75/...`. Verifica se l'assistente si ferma, elenca i riferimenti omonimi del Documento 2 e chiede quale codice serve.
2. **Mossa 2:** risponde fornendo i codici completi e cambiando il numero di presse, poi verifica che Python ricalcoli e aggiorni la tabella `.csv`.

Chi ha progettato l'assistente osserva senza intervenire, poi decide quale regola conservare o correggere in `istruzioni_assistente_P03.txt`. Infine ciascuno studente compila da solo, senza Copilot, le due risposte individuali.

## 5. Riscontri riservati sulle fonti e sulle omonimie

### Gruppi di codici con la stessa descrizione nel Documento 2 (Fervi P001/75, pag. 28)

| Descrizione ripetuta nel manuale | Tutti i riferimenti presenti nel Doc. 2 (con quantità su 1 macchina) | Riferimenti presenti anche a magazzino nel Doc. 3 |
| --- | --- | --- |
| `O-ring` | `P001/75/08` (4), `P001/75/20` (8), `P001/75/45` (2) | Tutti e tre (`/08`, `/20`, `/45`) |
| `Rondella elastica` | `P001/75/05` (42), `P001/75/18` (4), `P001/75/47` (9) | Tutti e tre (`/05`, `/18`, `/47`) |
| `Rondella` | `P001/75/06` (42), `P001/75/19` (4), `P001/75/50` (4) | Tutti e tre (`/06`, `/19`, `/50`) |
| `Vite` | `/02` (14), `/10` (4), `/14` (24), `/22` (2), `/36` (4), `/38` (4), `/46` (9), `/51` (4), `/56` (2), `/66` (1) | `/02`, `/14`, `/46` (gli altri 7 non sono a magazzino nel Doc. 3) |
| `Anello di nylon` | `P001/75/42` (1), `P001/75/61` (1) | Entrambi (`/42`, `/61`) |
| `Perno` / `Perno del bancale` | `P001/75/07` Perno (2), `P001/75/35` Perno (2), `P001/75/12` Perno del bancale (4) | `P001/75/12` Perno del bancale |

Nota: il riferimento `P001/75/52` è vuoto nell'originale Fervi e non va trattato come quantità zero. I movimenti elencati in fondo al Documento 3 (uscite del 14/10 e 17/10, entrate del 18/10) sono **già compresi** nei saldi chiusi del 19/10 ore 08:00: non vanno sottratti o sommati una seconda volta.

## 6. Esempi numerici di riscontro per il docente (non da dettare come tracce pronte)
### Caso A — Dotazione per **2 presse** (`N = 2`) su 6 codici d'esempio

| Codice e descrizione | Q.tà su 1 pressa → Fabbisogno (2 presse) | Scorta (Doc. 3) → Mancanti | Confezione → Confezioni da ordinare (pezzi acquistati) | Prezzo/conf. → Costo riga (€) |
| --- | --- | --- | --- | --- |
| `FLT-993` — Filtro P03 (rev. 2) | 1 → **2** | 8 → **0** | da 2 pz → **0 conf.** (0 pz) | 38 € → **0 €** |
| `P001/75/05` — Rondella elastica | 42 → **84** | 50 → **34** | da 25 pz → **2 conf.** (50 pz) | 5 € → **10 €** |
| `P001/75/12` — Perno del bancale | 4 → **8** | 5 → **3** | da 2 pz → **2 conf.** (4 pz) | 18 € → **36 €** |
| `P001/75/13` — Coppiglia del perno | 8 → **16** | 10 → **6** | da 10 pz → **1 conf.** (10 pz) | 5 € → **5 €** |
| `P001/75/20` — O-ring | 8 → **16** | 10 → **6** | da 6 pz → **1 conf.** (6 pz) | 12 € → **12 €** |
| `P001/75/45` — O-ring | 2 → **4** | 3 → **1** | da 4 pz → **1 conf.** (4 pz) | 6 € → **6 €** |
| **Totale Caso A (2 presse)** | | | **7 confezioni** | **69 €** |

### Caso B — Stessi 6 codici ricalcolati per **3 presse** (`N = 3`)

| Codice e descrizione | Fabbisogno (3 presse) | Scorta → Mancanti | Confezione → Confezioni da ordinare (pezzi acquistati) | Prezzo/conf. → Costo riga (€) |
| --- | --- | --- | --- | --- |
| `FLT-993` — Filtro P03 (rev. 2) | **3** | 8 → **0** | da 2 pz → **0 conf.** (0 pz) | 38 € → **0 €** |
| `P001/75/05` — Rondella elastica | **126** | 50 → **76** | da 25 pz → **4 conf.** (100 pz) | 5 € → **20 €** |
| `P001/75/12` — Perno del bancale | **12** | 5 → **7** | da 2 pz → **4 conf.** (8 pz) | 18 € → **72 €** |
| `P001/75/13` — Coppiglia del perno | **24** | 10 → **14** | da 10 pz → **2 conf.** (20 pz) | 5 € → **10 €** |
| `P001/75/20` — O-ring | **24** | 10 → **14** | da 6 pz → **3 conf.** (18 pz) | 12 € → **36 €** |
| `P001/75/45` — O-ring | **6** | 3 → **3** | da 4 pz → **1 conf.** (4 pz) | 6 € → **6 €** |
| **Totale Caso B (3 presse)** | | | **14 confezioni** | **144 €** |
### Caso C — Filtro P03 quando si superano gli 8 pezzi a magazzino (per esempio richiesta di 11 pezzi `FLT-993`)

- Fabbisogno: `11`; Scorta: `8`; Mancanti: `3`; Confezioni da 2 pezzi: $\lceil 3/2 \rceil = \mathbf{2\text{ confezioni}}$ (`4` pezzi acquistati); Costo: `2 × 38 € = 76 €`.

## 7. Ostacoli possibili e gestione in aula

| Situazione osservata | Prosecuzione in aula | Limite da far annotare |
| --- | --- | --- |
| Formato allegato non accettato | Usare l'altro formato collaudato o incollare il testo integrale di `01_DOCUMENTI_P03.txt` | Prova su testo incollato, non su file allegato |
| Agente non disponibile | Usare una normale conversazione inviando le istruzioni nel primo messaggio | Istruzioni inviate come messaggio utente, non agente configurato |
| Python non disponibile o non osservabile | Eseguire il controllo sulle prime righe e confrontare con la dimostrazione del docente | Non dichiarare eseguita autonomamente la *sandbox* Python |
| Copilot sceglie un `O-ring` a caso nella Mossa 1 | Far individuare alla coppia quale regola delle istruzioni va precisata e far ripetere la prova | Correzione motivata nella sezione 3 della scheda |

Richiamare le modalità del corso per distinguere l'origine della prova: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`.

## 8. Valutazione, consegna e rigenerazione dei file

Valutare: correttezza nella distinzione delle tre quantità (manuale, magazzino, confezione), gestione delle omonimie nelle istruzioni, controllo critico del calcolo Python, qualità del collaudo incrociato e autonomia nelle risposte individuali. Non valutare la lunghezza del prompt o la velocità del modello.

Consegna su Teams: `ATTIVITA_LEZIONE3.docx` compilata, `istruzioni_assistente_P03.txt` e il file `.csv` prodotto da Python.

### Rigenerazione dei materiali

Dalla cartella `docente/`:

```bash
python3 genera_materiali.py
```

Lo script rigenera `01_DOCUMENTI_P03.{txt,docx,pdf}`, `ATTIVITA_LEZIONE3.{docx,pdf}`, `GUIDA_DOCENTE.{docx,pdf}` e le slide `Lezione3_Assistente_Reparto_P03_ITS_MAKER.{pptx,html,pdf}` mantenendo il modello ufficiale ITS MAKER 16:10.

Fonti esterne consultate:
- Manuale d'uso e manutenzione Fervi `Art. P001/75` (Rev. 1, settembre 2013, pagg. 26 e 28).
- [Microsoft — Interprete di codice per gli agenti](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter).
