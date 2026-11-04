# Guida docente — Dai diari della P03 a numeri controllati

**ITS MAKER Bologna · Lezione 3 · 4 novembre 2026 · Microsoft Copilot con account scolastico**

Documento riservato al docente: preparazione, regia, riscontri sui dati e gestione dei problemi. Agli studenti si distribuiscono soltanto i materiali della cartella `studenti/` e le slide.

## 1. Scopo e struttura

Le coppie rispondono a una domanda del responsabile di reparto: su quale problema della P03 intervenire per primo. Per farlo usano due strumenti di Microsoft Copilot con ruoli diversi:

- il **Blocco appunti** per trovare, spiegare e collegare informazioni nei documenti, con citazioni;
- un **agente con Python**, cioè con l'Interprete di codice, per contare e calcolare su tutte le righe dei diari e confrontare i risultati con i riepiloghi mensili.

Il passaggio dal primo al secondo strumento avviene con la **scheda di passaggio**, un testo scritto dagli studenti. Nel Blocco appunti non esiste una funzione che consegni il lavoro a un agente: il passaggio è manuale (copia del testo o file `.txt`).

La lezione ha tre parti:

1. **Gli agenti della lezione 2.** Nella lezione 2 le coppie hanno creato in aula un proprio agente in Copilot, dopo la dimostrazione del docente, ma non c'è stato tempo per vederli. Oggi li riaprono, li provano con una domanda e alcune coppie li mostrano al proiettore, senza scrivere nulla. Viene per prima perché introduce il tema del giorno: istruzioni scritte da noi e controllo dei risultati.
2. **Blocco appunti.** Domande scritte dagli studenti, controllo delle citazioni, conteggio di un mese a mano.
3. **Agente con Python.** Scheda di passaggio e istruzioni dell'agente scritte nello stesso momento e corrette insieme, Prova A (solo scheda) e Prova B (scheda e file Excel) svolte nello stesso momento con la stessa richiesta (fault e minuti di fermo per tipo, gennaio–giugno), confronto con i riepiloghi, discussione in classe di che cosa si perde nel passaggio e delle istruzioni di esempio, proposta al responsabile.

Ogni studente lavora sul proprio computer con il proprio account. All'inizio la coppia decide chi segue gli **allarmi** e chi segue i **numeri**, e i compiti non cambiano durante la lezione: chi segue gli allarmi interroga il Blocco appunti su allarmi e documenti del reparto, scrive le istruzioni dell'agente e svolge la Prova A; chi segue i numeri ricava le regole di calcolo, conta il mese scelto, scrive la scheda di passaggio e svolge la Prova B. Scheda e istruzioni nascono nello stesso momento; poi ognuno legge il testo dell'altro e la coppia li corregge insieme. La proposta si scrive insieme.

Gli studenti non compilano un documento Word. Scrivono con Blocco note tre file di testo: `scheda_passaggio_P03.txt`, `istruzioni_agente_P03.txt` e `proposta_P03.txt`, con il confronto dei numeri, l'informazione mancata nel passaggio e la proposta.

## 2. Il rischio didattico centrale: che cosa si perde nel passaggio

Questo è il contenuto da far emergere ed esplicitare in chiusura.

- **Perdita di dati.** Il Blocco appunti risponde recuperando le parti dei documenti più pertinenti alla domanda: non è fatto per trascrivere o contare in modo completo le {{righe_eventi}} righe di eventi dei diari. Una scheda di passaggio che contiene conteggi o estratti del Blocco appunti può contenere righe mancanti o numeri riassunti. Se all'agente arriva solo la scheda (Prova A), Python può al massimo rielaborare quei numeri: non può ricontrollarli.
- **Perdita di definizioni.** Il fermo per fault si misura dal FAULT al **primo AVVIO successivo** (documento `Regole di calcolo degli indicatori`, PR-IND-03). Se la scheda non riporta la definizione, l'agente tende a sceglierne una plausibile, per esempio dal FAULT al RIPRISTINO. Con quella scelta i minuti scendono da {{fermo_totale}} a {{fermo_totale_ripristino}} nel semestre, e nessun mese torna con il riepilogo.
- **Numeri presentati come certi.** Un numero copiato dal Blocco appunti nella scheda, senza l'annotazione «da verificare», viene trattato dall'agente come un dato.

Regola da far formulare agli studenti: **la scheda di passaggio trasporta la domanda, le definizioni e i controlli; i dati si prendono dal file originale.** I riepiloghi mensili, calcolati con le regole PR-IND-03, sono il punto di controllo esterno.

Non presentare la perdita come certa: se in Prova A il Blocco appunti aveva riportato numeri corretti, il risultato è valido. Conta che gli studenti sappiano dimostrare con che cosa lo hanno verificato.

## 3. Preparazione con un account studente

Le funzioni di Copilot cambiano con la licenza e con le impostazioni della scuola. Prima dell'aula verificare tutto con un vero account studente, senza attivare acquisti o consumi a pagamento. Secondo la documentazione Microsoft, il Blocco appunti (Copilot Notebooks) è disponibile anche agli utenti Copilot Chat idonei, con funzioni e limiti ridotti; l'Interprete di codice degli agenti è disponibile agli utenti Copilot Chat che non hanno attiva la fatturazione a consumo.

| Verifica pre-aula | Che cosa controllare | Esito e data |
| --- | --- | --- |
| Postazioni | Ogni studente ha un computer, accede a Copilot con il proprio account e ha Word desktop e Blocco note; i file `.txt` si inviano nella chat di Teams | |
| Creazione del Blocco appunti | Pulsante disponibile con l'account studente; nome mostrato dall'interfaccia italiana. Microsoft indica che Copilot Notebooks è diventato Copilot Workspaces, con un rilascio graduale: se compare il nome nuovo, aggiornare slide, consegna e guida con quel nome | |
| Caricamento dalla cartella compressa | La cartella scaricata da Teams arriva come `.zip`; i file estratti si caricano dal computer | |
| Caricamento dei riferimenti | Tutti i file di `Documenti_P03_Blocco_appunti` accettati; nessun avviso sul numero o sulla dimensione | |
| Citazioni | Le risposte indicano il documento; il collegamento apre il punto giusto | |
| Creazione dell'agente | Campo istruzioni; presenza o assenza di un interruttore per Interprete di codice o Code interpreter e nome mostrato. La documentazione Microsoft dice: «Code interpreter is always enabled in Agent Builder. This capability is automatically included for all agents» | |
| Python nella conversazione con l'agente | Il file `.xlsx` allegato viene letto; il pulsante `</> Code`, indicato dalla stessa documentazione, mostra il codice eseguito: è il punto da mostrare agli studenti per il controllo della Prova B | |
| Classe intera | Comportamento con più coppie collegate insieme: rallentamenti o limiti d'uso | |
| Agente dimostrativo | Un agente del docente con istruzioni brevi diverse dall'esempio, da usare al proiettore se gli studenti non possono creare l'agente; si prova con la scheda di passaggio di una coppia. Preparare anche una conversazione già eseguita con Python su una richiesta diversa da quella delle prove, per mostrare il pulsante del codice senza attese e senza anticipare risultati o una scheda modello | |
| Consegna | Compito su Teams per i tre file `.txt` di ogni coppia | |

Prima delle prove mostrare, nella conversazione già eseguita, dove si leggono i dettagli dell'esecuzione di Python: un blocco di codice soltanto scritto nel messaggio non dimostra l'esecuzione.

## 4. Materiali e distribuzione

Pubblicare su Teams all'inizio della lezione:

- `studenti/ATTIVITA_LEZIONE3.docx`, la consegna dell'attività: gli studenti la leggono, non la compilano;
- la cartella `studenti/Documenti_P03_Blocco_appunti/` con tutti i file;
- `studenti/Diari_P03_gennaio_giugno_2026.xlsx`;
- le slide `Lezione3_Blocco_appunti_e_agente_Python_P03_ITS_MAKER.pptx`.

Pubblicare **soltanto dopo la Prova B** `studenti/da_pubblicare_dopo_prova_B/ESEMPIO_ISTRUZIONI_AGENTE_P03.txt`: se arriva prima, gli studenti la copiano invece di progettare le proprie istruzioni.

Le cartelle `backup/` non vanno pubblicate. `studenti/backup/` contiene il sorgente Markdown e il PDF della consegna, utile per stamparla. `docente/backup/` contiene i sorgenti Markdown di guida e slide, le versioni PDF e HTML delle slide, il PDF della guida e le fonti da cui il generatore ricava i documenti per gli studenti.

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

Gli studenti non hanno consegnato file nella lezione 2: gli agenti sono salvati nei loro account Copilot. In ogni coppia chi ha creato l'agente lo apre sul proprio computer; la coppia rilegge le istruzioni e fa una domanda di prova scelta da loro, senza scrivere nulla. Scegliere due o tre coppie con agenti diversi e farli mostrare al proiettore: istruzioni e una risposta.

Se una coppia non trova più l'agente (account diverso, agente non salvato), lavora con una coppia vicina.

Far emergere i punti che servono oggi:

- le istruzioni salvate in un agente valgono in ogni conversazione con lui;
- un'istruzione utile è verificabile su una risposta precisa; un'istruzione vaga non si può controllare;
- una risposta ben scritta non è per forza corretta: va confrontata con la fonte;
- nella Parte 3 creeranno un nuovo agente, questa volta con la funzione che esegue Python.

Domande utili: quale istruzione avete visto rispettata davvero? Quale avete scritto ma non sapete se funziona? Che cosa succede se fate all'agente una domanda fuori dal suo compito?

### Parte 2 — Blocco appunti

Mostrare una volta al proiettore la creazione del Blocco appunti e il caricamento dei file, mentre gli studenti scaricano ed estraggono la cartella. Ogni studente crea il proprio Blocco appunti e scrive da solo le domande sul proprio argomento: non dettare domande pronte. Gli appunti presi durante le domande non si consegnano; quello che conta entra nella scheda di passaggio.

Che cosa possono scoprire nei documenti:

- la guida IO-P03-07 divide gli allarmi per parte della macchina (alimentazione dei grezzi, stampo ed espulsione, circuito idraulico, sicurezza) e indica chi interviene;
- la procedura PR-IND-03 definisce gli indicatori del riepilogo, compreso il fermo per fault, e i pezzi teorici persi;
- informazioni che uniscono due documenti: un tipo di fault dei diari letto con la guida; la sovratemperatura dell'olio nei diari di aprile e giugno letta insieme al fermo di ottobre per filtro intasato; la regola «la barriera non si esclude mai» letta accanto agli interventi della barriera nei diari;
- la guida elenca anche allarmi che nei diari non compaiono (Livello olio minimo, Arresto di emergenza): utile per vedere se il Blocco appunti distingue ciò che è scritto nella guida da ciò che è successo.

Il conteggio di un mese è fattibile: ogni mese ha da {{fault_mese_min}} a {{fault_mese_max}} fault. Lo svolge chi segue i numeri, con la ricerca di Word (Ctrl+F) sulla parola FAULT: è un controllo esterno all'intelligenza artificiale. La ricerca di Word non distingue maiuscole e minuscole e trova anche «Fault» e «fault» nella riga del riepilogo in testa al diario: per questo la consegna chiede di contare solo i risultati nella colonna Evento della tabella. Il conteggio di sei mesi, chiesto alla fine al Blocco appunti, apre il passaggio a Python.

### Parte 3 — Agente con Python

Chi segue i numeri scrive la scheda di passaggio; nello stesso momento chi segue gli allarmi scrive `istruzioni_agente_P03.txt`. Poi si mandano i file, ognuno legge quello dell'altro e la coppia corregge insieme: chi segue gli allarmi aggiunge alla scheda ciò che ha trovato su allarmi e documenti del reparto. La richiesta per le due prove sta in fondo alla scheda di passaggio, così è identica. Mostrare al proiettore la creazione dell'agente e dove si controlla l'Interprete di codice; poi ognuno crea l'agente sul proprio computer con le stesse istruzioni.

Sulla scheda di passaggio non fornire un modello. Se chi la scrive è bloccato, chiedere: «Se la desse a un compagno che non ha visto il vostro Blocco appunti, che cosa gli mancherebbe per fare i conti?»

- **Prova A**, svolta da chi segue gli allarmi. Solo la scheda, nessun file. Osservare se l'agente calcola davvero, riprende i numeri della scheda o li inventa. Un buon agente dichiara che non può ricontrollare.
- **Prova B**, svolta nello stesso momento da chi segue i numeri. Stessa scheda e file Excel, in una nuova conversazione. Verificare l'esecuzione di Python e che i totali tornino con i riepiloghi.
- **Confronto.** Finita la Prova A, chi segue gli allarmi crea `proposta_P03.txt` e somma fault e minuti di fermo dei sei riepiloghi mentre la Prova B è ancora in corso. Poi, con i due computer affiancati, la coppia scrive i numeri delle due prove accanto ai riepiloghi e controlla che la somma dei valori per tipo della Prova B dia i totali dei riepiloghi. La somma controlla i totali, non la divisione per tipo: un fault assegnato al tipo sbagliato non la cambia. Nella proposta un numero per tipo vale come controllato solo per la somma, e gli studenti devono dirlo. In una riga la coppia scrive quale informazione mancava nella scheda o nelle istruzioni, oppure che cosa ha permesso all'agente di calcolare giusto. Le correzioni alla scheda o alle istruzioni vanno in fondo ai file sul computer di chi segue gli allarmi, sotto «Correzioni dopo le prove», come regole generali; non si ripete la Prova B.
- **Discussione con la classe.** Dopo la Prova B pubblicare `ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` e leggerlo al proiettore. Far raccontare ad alcune coppie quali numeri l'agente ha calcolato davvero nella Prova A e quali ha ripreso dalla scheda, e da dove vengono le eventuali differenze della Prova B: è il momento in cui emerge che cosa si perde nel passaggio (paragrafo 2). Poi una sola domanda sull'esempio: che cosa aggiungete alle vostre istruzioni? L'esempio non contiene le definizioni del fermo: le pretende dalla scheda e chiede se mancano. È un punto da far notare. Le coppie non modificano le istruzioni scritte prima: le aggiunte vanno sotto «Aggiunte dopo l'esempio», con il motivo, e non si fa una nuova prova.
- **Proposta.** Al massimo otto righe in `proposta_P03.txt`, con due numeri controllati (prova e controllo superato), un documento citato e la decisione lasciata al responsabile.

## 6. Valori di riferimento

Valori calcolati da `docente/dati_p03.py`, che applica le regole PR-IND-03 e confronta i risultati con i riepiloghi stampati: tutti i riepiloghi coincidono con i dati. Il generatore inserisce queste tabelle e i numeri citati nella guida direttamente dallo script; se un riepilogo non torna, la generazione si ferma.

### Valori mensili

{{tabella_riepiloghi}}

Le colonne da Giornate a Fermo per fault sono quelle stampate nel riepilogo di ogni diario. I pezzi teorici persi non compaiono nei riepiloghi: si calcolano con la regola del paragrafo 4 di PR-IND-03.

Con la definizione sbagliata (dal FAULT al RIPRISTINO) i minuti mensili diventano {{fermo_ripristino_mesi}}: totale {{fermo_totale_ripristino}}.

### Per tipo di fault, gennaio–giugno

{{tabella_tipi}}

### Per parte della macchina (raggruppamento della guida IO-P03-07)

{{tabella_parti}}

Le somme per gruppo sono calcolate sui valori non arrotondati: possono differire di un'unità dalla somma delle righe per tipo.

### Che cosa rende la decisione aperta

- Per numero di fault sono a pari merito il sensore presenza grezzo e la barriera ({{n_mancata_lettura_sensore_presenza_grezzo}} e {{n_intervento_barriera_di_sicurezza}}); per minuti di fermo la barriera scende al {{posto_min_intervento_barriera_di_sicurezza}}° posto.
- La richiesta alle prove riguarda fault e minuti di fermo, non i pezzi teorici persi. Se una coppia li porta nella proposta con la regola di PR-IND-03: per questo indicatore la pressione idraulica ({{persi_pressione_circuito_idraulico_sotto_soglia}}) supera la protezione stampo ({{persi_protezione_stampo_pezzo_non_espulso}}), perché si verifica a cadenze più alte.
- Per parte della macchina, stampo/espulsione e alimentazione sono quasi alla pari; il circuito idraulico è più basso nel totale ma passa da {{trim1_circuito_idraulico}} fault nel primo trimestre a {{trim2_circuito_idraulico}} nel secondo, e a ottobre la P03 si è fermata per sovratemperatura con filtro intasato.
- La guida mette la sicurezza al primo posto, ma un intervento della barriera indica che la barriera ha funzionato: la proposta deve spiegare come usa questa priorità.

Sono accettabili proposte diverse, se i numeri sono verificati e la scelta è motivata con i documenti.

## 7. Prove di controllo delle istruzioni di esempio

Da eseguire nell'ambiente qualificato prima dell'aula; non sono state eseguite in Copilot durante la preparazione dei materiali.

| Prova | Che cosa si consegna | Comportamento atteso |
| --- | --- | --- |
| 1 | Solo una scheda di passaggio con conteggi del Blocco appunti | Nessun nuovo calcolo; dichiara quali numeri non può ricontrollare e chiede il file Excel |
| 2 | File Excel e scheda senza la definizione del fermo | Chiede la definizione prima di calcolare i minuti |
| 3 | File Excel e scheda completa | Python eseguito; {{fault_totali}} fault e {{fermo_totale}} minuti; tabella di confronto con i riepiloghi tutta coincidente |

Nei riepiloghi dei diari e del file Excel i valori sono testo con l'unità e due usi del punto: «155.3 h» ha il punto decimale, «21.076» ha il punto delle migliaia. Se una scheda chiede di confrontare ore o pezzi teorici, un agente può leggere 21.076 come numero decimale e segnalare una differenza che non esiste. È un dato originale dei diari: non va corretto, va spiegato in aula se compare.

## 8. Ostacoli possibili

| Situazione | Prosecuzione in aula | Limite da far annotare |
| --- | --- | --- |
| Blocco appunti non disponibile | Conversazione normale con i documenti allegati in più messaggi | Ricerca su allegati di una conversazione, non Blocco appunti |
| Agente non creabile o Interprete di codice non disponibile | Dimostrazione del docente al proiettore con l'agente dimostrativo e la scheda di passaggio di una coppia; gli studenti controllano i risultati sui riepiloghi | «Osservato nella dimostrazione del docente», non esecuzione autonoma |
| Il file Excel non viene letto | Verificare il caricamento; in alternativa dimostrazione del docente con l'agente dimostrativo | Non dichiarare eseguito Python |
| Limiti d'uso con tutta la classe collegata | Alternare le coppie nelle prove con l'agente | Prove svolte da un'altra coppia osservate |
| Un solo computer per coppia | Un unico Blocco appunti e un unico agente; i due argomenti si dividono nella lettura dei documenti in Word e le prove A e B si fanno una dopo l'altra | Nessuno |
| Word desktop non disponibile | Conteggio del mese con la ricerca nel PDF o nel browser, contando solo le righe della colonna Evento | Nessuno |

Ricordare le tre modalità della consegna: eseguito da voi, osservato nella dimostrazione del docente, controllato solo sui documenti.

## 9. Valutazione e consegna

Valutare: domande al Blocco appunti (osservate in aula, perché gli appunti non si consegnano), completezza della scheda di passaggio, istruzioni dell'agente scritte prima delle prove, correzioni e aggiunte motivate, verifica dei numeri con i riepiloghi, comprensione di che cosa si perde nel passaggio (osservata nella discussione e nella riga scritta in `proposta_P03.txt`), motivazione della proposta. Non valutare la lunghezza delle istruzioni né la velocità del modello.

Consegna nel compito su Teams, caricata da chi segue gli allarmi: `scheda_passaggio_P03.txt`, `istruzioni_agente_P03.txt` e `proposta_P03.txt`.

## 10. Rigenerazione dei materiali

Dalla cartella `docente/`, con i pacchetti di `requirements_materiali.txt` e LibreOffice installato:

```bash
python genera_materiali.py
```

Lo script:

- converte i diari originali di `backup/fonti/Diari_pressa_gennaio_giugno_2026.zip` con la macchina P03;
- crea la cartella `studenti/Documenti_P03_Blocco_appunti/` con i documenti di reparto e le fonti pubbliche di `backup/fonti_online/`, e il file Excel;
- controlla che i riepiloghi tornino con i dati e ricava i valori di riferimento del paragrafo 6;
- genera consegna, guida e slide nei formati Word, PDF, PowerPoint e HTML, con il modello ufficiale ITS MAKER 16:10. Nel sorgente `backup/GUIDA_DOCENTE.md` i valori compaiono come nomi fra doppie parentesi graffe, sostituiti dallo script.

`python dati_p03.py` stampa gli stessi valori di riferimento.

Fonti Microsoft consultate:

- Copilot Notebooks, licenze: <https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-licensing>
- Copilot Notebooks, riferimenti e limiti: <https://support.microsoft.com/en-us/microsoft-365-copilot/get-answers-and-insights-about-your-microsoft-365-copilot-notebook>
- Interprete di codice per gli agenti: <https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter>
- Da Copilot Notebooks a Copilot Workspaces: <https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-to-copilot-workspaces>
