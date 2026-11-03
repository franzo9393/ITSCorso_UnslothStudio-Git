# Guida docente — Dai diari della P03 a numeri controllati

**ITS MAKER Bologna · Lezione 3 · 4 novembre 2026 · Microsoft Copilot con account scolastico**

Documento riservato al docente: preparazione, regia, riscontri sui dati e gestione dei problemi. Agli studenti si distribuiscono soltanto i materiali della cartella `studenti/` e le slide.

## 1. Scopo e struttura

Le coppie rispondono a una domanda del responsabile di reparto: su quale problema della P03 intervenire per primo. Per farlo usano due strumenti di Microsoft Copilot con ruoli diversi:

- il **Blocco appunti** per trovare, spiegare e collegare informazioni nei documenti, con citazioni;
- un **agente con Python**, cioè con l'Interprete di codice attivo, per contare e calcolare su tutte le righe dei diari e confrontare i risultati con i riepiloghi mensili.

Il passaggio dal primo al secondo strumento avviene con la **scheda di passaggio**, un testo scritto dagli studenti. Nel Blocco appunti non esiste una funzione che consegni il lavoro a un agente: il passaggio è manuale (copia del testo o file `.txt`).

La lezione ha tre parti:

1. **Gli agenti della lezione 2.** Nella lezione 2 le coppie hanno creato in aula un proprio agente in Copilot, dopo la dimostrazione del docente, ma non c'è stato tempo per vederli. Oggi li riaprono, li provano con una domanda e alcune coppie li mostrano. Viene per prima perché introduce il tema del giorno: istruzioni scritte da noi e controllo dei risultati.
2. **Blocco appunti.** Domande scritte dagli studenti, controllo delle citazioni, conteggio di un mese a mano, stesura della scheda di passaggio.
3. **Agente con Python.** Progetto delle istruzioni, Prova A (solo scheda), Prova B (scheda e file Excel), analisi di che cosa si perde nel passaggio, confronto con le istruzioni di esempio, proposta al responsabile.

## 2. Il rischio didattico centrale: che cosa si perde nel passaggio

Questo è il contenuto da far emergere ed esplicitare in chiusura.

- **Perdita di dati.** Il Blocco appunti risponde recuperando le parti dei documenti più pertinenti alla domanda: non è fatto per trascrivere o contare in modo completo circa 770 righe di eventi. Una scheda di passaggio che contiene conteggi o estratti del Blocco appunti può contenere righe mancanti o numeri riassunti. Se all'agente arriva solo la scheda (Prova A), Python può al massimo rielaborare quei numeri: non può ricontrollarli.
- **Perdita di definizioni.** Il fermo per fault si misura dal FAULT al **primo AVVIO successivo** (documento `Regole di calcolo degli indicatori`, PR-IND-03). Se la scheda non riporta la definizione, l'agente tende a sceglierne una plausibile, per esempio dal FAULT al RIPRISTINO. Con quella scelta i minuti scendono da 1.339 a 1.108 nel semestre, e nessun mese torna con il riepilogo.
- **Numeri presentati come certi.** Un numero copiato dal Blocco appunti nella scheda, senza l'annotazione «da verificare», viene trattato dall'agente come un dato.

Regola da far formulare agli studenti: **la scheda di passaggio trasporta la domanda, le definizioni e i controlli; i dati si prendono dal file originale.** I riepiloghi mensili, calcolati con le regole PR-IND-03, sono il punto di controllo esterno.

Non presentare la perdita come certa: se in Prova A il Blocco appunti aveva riportato numeri corretti, il risultato è valido. Conta che gli studenti sappiano dimostrare con che cosa lo hanno verificato.

## 3. Preparazione con un account studente

Le funzioni di Copilot cambiano con la licenza e con le impostazioni della scuola. Prima dell'aula verificare tutto con un vero account studente, senza attivare acquisti o consumi a pagamento. Secondo la documentazione Microsoft, il Blocco appunti (Copilot Notebooks) è disponibile anche agli utenti Copilot Chat idonei, con funzioni e limiti ridotti; l'Interprete di codice degli agenti è disponibile agli utenti Copilot Chat che non hanno attiva la fatturazione a consumo.

| Verifica pre-aula | Che cosa controllare | Esito e data |
| --- | --- | --- |
| Creazione del Blocco appunti | Pulsante disponibile con l'account studente; nome del comando nell'interfaccia italiana | |
| Caricamento dei riferimenti | Tutti i file di `Documenti_P03_Blocco_appunti` accettati; nessun avviso sul numero o sulla dimensione | |
| Citazioni | Le risposte indicano il documento; il collegamento apre il punto giusto | |
| Creazione dell'agente | Campo istruzioni, funzione Interprete di codice o Code interpreter attivabile senza costi | |
| Python nella conversazione con l'agente | Il file `.xlsx` allegato viene letto; dettagli dell'esecuzione visibili; file `.csv` o `.xlsx` scaricabile | |
| Classe intera | Comportamento con più coppie collegate insieme: rallentamenti o limiti d'uso | |

Prima delle prove mostrare dove si leggono i dettagli dell'esecuzione di Python: un blocco di codice soltanto scritto nel messaggio non dimostra l'esecuzione.

## 4. Materiali e distribuzione

Pubblicare su Teams all'inizio della lezione:

- `studenti/ATTIVITA_LEZIONE3.docx`;
- la cartella `studenti/Documenti_P03_Blocco_appunti/` con tutti i file;
- `studenti/Diari_P03_gennaio_giugno_2026.xlsx`;
- le slide `Lezione3_Blocco_appunti_e_agente_Python_P03_ITS_MAKER.pptx`.

Pubblicare **soltanto dopo la Prova B** `studenti/da_pubblicare_dopo_prova_B/ESEMPIO_ISTRUZIONI_AGENTE_P03.txt`: se arriva prima, gli studenti la copiano invece di progettare le proprie istruzioni.

Le cartelle `backup/` non vanno pubblicate. `studenti/backup/` contiene il sorgente Markdown e il PDF della scheda, utile per stamparla. `docente/backup/` contiene i sorgenti Markdown di guida e slide, le versioni PDF e HTML delle slide, il PDF della guida e le fonti da cui il generatore ricava i documenti per gli studenti.

Contenuto della cartella per il Blocco appunti:

| File | Natura |
| --- | --- |
| `Diario_P03_01_Gennaio_2026.docx` … `Diario_P03_06_Giugno_2026.docx` | Diari simulati: eventi con data, ora, cadenza e dettaglio; riepilogo mensile in testa |
| `Guida_allarmi_P03_IO-P03-07.docx` | Documento di reparto inventato: allarmi divisi per parte della macchina, chi interviene, priorità del reparto |
| `Regole_indicatori_P03_PR-IND-03.docx` | Documento di reparto inventato: definizioni degli indicatori del riepilogo e dei pezzi teorici persi |
| `Registro_P03_13-15_ottobre_2026.docx` | Registro della lezione 2: fermo per temperatura dell'olio e filtro intasato |
| File che iniziano con `E0` | Documenti pubblici riutilizzabili; titoli, licenze e attribuzioni nella scheda studenti |

Il file Excel contiene gli stessi dati dei diari Word: un foglio per mese, con il riepilogo in alto e la tabella degli eventi più sotto. La posizione della tabella non è in prima riga: l'agente deve trovarla.

## 5. Regia

### Parte 1 — Gli agenti della lezione 2

Gli studenti non hanno consegnato file nella lezione 2: gli agenti sono salvati nei loro account Copilot. Le coppie aprono l'agente, rileggono le istruzioni, fanno una domanda di prova scelta da loro e compilano la prima tabella. Scegliere due o tre coppie con agenti diversi e farli mostrare al proiettore: istruzioni e una risposta.

Se una coppia non trova più l'agente (account diverso, agente non salvato), lavora con una coppia vicina.

Far emergere i punti che servono oggi:

- le istruzioni salvate in un agente valgono in ogni conversazione con lui;
- un'istruzione utile è verificabile su una risposta precisa; un'istruzione vaga non si può controllare;
- una risposta ben scritta non è per forza corretta: va confrontata con la fonte;
- nella Parte 3 creeranno un nuovo agente, questa volta con la funzione che esegue Python.

Domande utili: quale istruzione avete visto rispettata davvero? Quale avete scritto ma non sapete se funziona? Che cosa succede se fate all'agente una domanda fuori dal suo compito?

### Parte 2 — Blocco appunti

Mostrare una volta al proiettore la creazione del Blocco appunti e il caricamento dei file. Gli studenti scrivono da soli le domande: non dettare domande pronte.

Che cosa possono scoprire nei documenti:

- la guida IO-P03-07 divide gli allarmi per parte della macchina (alimentazione dei grezzi, stampo ed espulsione, circuito idraulico, sicurezza) e indica chi interviene;
- la procedura PR-IND-03 definisce gli indicatori del riepilogo, compreso il fermo per fault, e i pezzi teorici persi;
- informazioni che uniscono due documenti: un tipo di fault dei diari letto con la guida; la sovratemperatura dell'olio nei diari di aprile e giugno letta insieme al fermo di ottobre per filtro intasato; la regola «la barriera non si esclude mai» letta accanto agli interventi della barriera nei diari;
- la guida elenca anche allarmi che nei diari non compaiono (Livello olio minimo, Arresto di emergenza): utile per vedere se il Blocco appunti distingue ciò che è scritto nella guida da ciò che è successo.

Il conteggio di un mese a mano è fattibile: ogni mese ha da 5 a 8 fault. Il conteggio di sei mesi apre il passaggio a Python.

Sulla scheda di passaggio non fornire un modello. Se una coppia è bloccata, chiedere: «Se la desse a un compagno che non ha visto il vostro Blocco appunti, che cosa gli mancherebbe per fare i conti?»

### Parte 3 — Agente con Python

Mostrare al proiettore la creazione dell'agente e dove si attiva l'Interprete di codice. Gli studenti progettano prima su carta, poi scrivono `istruzioni_agente_P03.txt`.

- **Prova A.** Solo la scheda, nessun file. Osservare se l'agente calcola davvero, riprende i numeri della scheda o li inventa. Un buon agente dichiara che non può ricontrollare.
- **Prova B.** Stessa scheda e file Excel, in una nuova conversazione. Verificare l'esecuzione di Python e il confronto mese per mese con i riepiloghi.
- **Analisi.** Compilare la tabella «Che cosa si è perso nel passaggio». Le correzioni alle istruzioni devono essere regole generali.
- **Esempio.** Dopo la Prova B pubblicare `ESEMPIO_ISTRUZIONI_AGENTE_P03.txt`. L'esempio non contiene le definizioni del fermo: le pretende dalla scheda e chiede se mancano. È un punto da far notare.
- **Proposta.** Al massimo otto righe, con due numeri controllati, un documento citato e la decisione lasciata al responsabile.

## 6. Valori di riferimento

Valori calcolati con `docente/dati_p03.py`, che applica le regole PR-IND-03 e confronta i risultati con i riepiloghi stampati: tutti i riepiloghi coincidono con i dati.

### Riepiloghi mensili

| Mese | Giornate | Ore di produzione | Pezzi teorici | Fault | Fermo per fault (min) | Pezzi teorici persi |
| --- | --- | --- | --- | --- | --- | --- |
| Gennaio | 20 | 155,3 | 21.076 | 7 | 252 | 569 |
| Febbraio | 20 | 157,4 | 19.398 | 5 | 131 | 264 |
| Marzo | 22 | 171,4 | 20.747 | 6 | 266 | 554 |
| Aprile | 21 | 163,8 | 20.550 | 6 | 217 | 452 |
| Maggio | 20 | 155,7 | 19.531 | 6 | 181 | 396 |
| Giugno | 21 | 162,9 | 21.402 | 8 | 292 | 643 |
| **Totale** | **124** | **966,4** | **122.705** | **38** | **1.339** | **2.877** |

I pezzi teorici persi non compaiono nei riepiloghi: si calcolano con la regola del paragrafo 4 di PR-IND-03.

Con la definizione sbagliata (dal FAULT al RIPRISTINO) i minuti mensili diventano 221, 104, 235, 170, 143, 235: totale 1.108.

### Per tipo di fault, gennaio–giugno

| Tipo di fault | N. | Minuti di fermo | Pezzi teorici persi |
| --- | --- | --- | --- |
| Mancata lettura sensore presenza grezzo | 7 | 253 | 552 |
| Protezione stampo: pezzo non espulso | 6 | 230 | 469 |
| Pressione circuito idraulico sotto soglia | 5 | 223 | 493 |
| Allarme fine corsa espulsore | 6 | 187 | 407 |
| Intervento barriera di sicurezza | 7 | 186 | 387 |
| Anomalia alimentatore vibrante | 4 | 162 | 352 |
| Sovratemperatura olio idraulico | 3 | 98 | 216 |

### Per parte della macchina (raggruppamento della guida IO-P03-07)

| Parte della macchina | N. | Minuti di fermo | Pezzi teorici persi | Fault gennaio–marzo | Fault aprile–giugno |
| --- | --- | --- | --- | --- | --- |
| Stampo ed espulsione | 12 | 417 | 877 | 5 | 7 |
| Alimentazione dei grezzi | 11 | 415 | 905 | 7 | 4 |
| Circuito idraulico | 8 | 321 | 709 | 1 | 7 |
| Sicurezza | 7 | 186 | 387 | 5 | 2 |

Le somme per gruppo sono calcolate sui valori non arrotondati: possono differire di un'unità dalla somma delle righe per tipo.

### Che cosa rende la decisione aperta

- Per numero di fault sono a pari merito il sensore presenza grezzo e la barriera (7); per minuti persi la barriera scende al quinto posto.
- Per pezzi teorici persi la pressione idraulica (493) supera la protezione stampo (469), perché si verifica a cadenze più alte.
- Per parte della macchina, stampo/espulsione e alimentazione sono quasi alla pari; il circuito idraulico è più basso nel totale ma passa da 1 fault nel primo trimestre a 7 nel secondo, e a ottobre la P03 si è fermata per sovratemperatura con filtro intasato.
- La guida mette la sicurezza al primo posto, ma un intervento della barriera indica che la barriera ha funzionato: la proposta deve spiegare come usa questa priorità.

Sono accettabili proposte diverse, se i numeri sono verificati e la scelta è motivata con i documenti.

## 7. Prove di controllo delle istruzioni di esempio

Da eseguire nell'ambiente qualificato prima dell'aula; non sono state eseguite in Copilot durante la preparazione dei materiali.

| Prova | Che cosa si consegna | Comportamento atteso |
| --- | --- | --- |
| 1 | Solo una scheda di passaggio con conteggi del Blocco appunti | Nessun nuovo calcolo; dichiara quali numeri non può ricontrollare e chiede il file Excel |
| 2 | File Excel e scheda senza la definizione del fermo | Chiede la definizione prima di calcolare i minuti |
| 3 | File Excel e scheda completa | Python eseguito; 38 fault e 1.339 minuti; tabella di confronto con i riepiloghi tutta coincidente |

## 8. Ostacoli possibili

| Situazione | Prosecuzione in aula | Limite da far annotare |
| --- | --- | --- |
| Blocco appunti non disponibile | Conversazione normale con i documenti allegati in più messaggi | Ricerca su allegati di una conversazione, non Blocco appunti |
| Agente non creabile o Interprete di codice non attivabile | Dimostrazione del docente al proiettore; gli studenti controllano i risultati sui riepiloghi | `OSSERVATO_DOCENTE`, non esecuzione autonoma |
| Il file Excel non viene letto | Verificare il caricamento; in alternativa dimostrazione del docente | Non dichiarare eseguito Python |
| Limiti d'uso con tutta la classe collegata | Alternare le coppie nelle prove con l'agente | Prove svolte da un'altra coppia osservate |

Richiamare le modalità del corso: `ESEGUITO_STUDENTE`, `OSSERVATO_DOCENTE`, `ANALISI_CASO`.

## 9. Valutazione e consegna

Valutare: qualità e controllo delle domande al Blocco appunti, completezza della scheda di passaggio, progetto delle istruzioni dell'agente, verifica dei numeri con i riepiloghi, comprensione di che cosa si perde nel passaggio, motivazione della proposta e risposte individuali. Non valutare la lunghezza delle istruzioni né la velocità del modello.

Consegna su Teams: scheda compilata, `scheda_passaggio_P03.txt`, `istruzioni_agente_P03.txt` e, se prodotto, il file dei risultati della Prova B.

## 10. Rigenerazione dei materiali

Dalla cartella `docente/`, con i pacchetti di `requirements_materiali.txt` e LibreOffice installato:

```bash
python genera_materiali.py
```

Lo script:

- converte i diari originali di `backup/fonti/Diari_pressa_gennaio_giugno_2026.zip` con la macchina P03;
- crea la cartella `studenti/Documenti_P03_Blocco_appunti/` con i documenti di reparto e le fonti pubbliche di `backup/fonti_online/`, e il file Excel;
- controlla che i riepiloghi tornino con i dati;
- genera scheda, guida e slide nei formati Word, PDF, PowerPoint e HTML, con il modello ufficiale ITS MAKER 16:10.

`python dati_p03.py` stampa i valori di riferimento di questa guida.

Fonti Microsoft consultate:

- Copilot Notebooks, licenze: <https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-licensing>
- Copilot Notebooks, riferimenti e limiti: <https://support.microsoft.com/en-us/microsoft-365-copilot/get-answers-and-insights-about-your-microsoft-365-copilot-notebook>
- Interprete di codice per gli agenti: <https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter>
