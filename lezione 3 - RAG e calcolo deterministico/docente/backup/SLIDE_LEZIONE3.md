# Slide 01 — Dai diari della P03 a numeri controllati
<!-- layout: COPERTINA -->

Lezione 3 · Blocco appunti di Copilot e agente con Python

4 novembre 2026 · Microsoft Copilot con l'account scolastico

---

# Slide 02 — La domanda del responsabile di reparto
<!-- layout: CONTENUTO -->

«Su quale problema della pressa P03 conviene intervenire per primo?»

Avete sei mesi di diari della pressa e alcuni documenti del reparto.

Preparate una proposta motivata, con numeri controllati e fonti citate.

La decisione finale resta al responsabile.

---

# Slide 03 — Il percorso di oggi
<!-- layout: CONTENUTO -->

| Parte | Dove lavorate | Che cosa ottenete |
| --- | --- | --- |
| 1. Gli agenti della lezione 2 | Copilot | Che cosa ha funzionato e che cosa no |
| 2. Cercare nei documenti | Blocco appunti di Copilot | Risposte controllate sui documenti |
| 3. Contare e calcolare | Agente di Copilot con Python | Scheda di passaggio, numeri controllati e proposta |

In coppia, ognuno al proprio computer: uno segue gli allarmi, l'altro i numeri, per tutta la lezione.

---

# Slide 04 — Riprendiamo la lezione 2
<!-- layout: SEZIONE -->

I vostri agenti alla prova dei fatti.

---

# Slide 05 — Che cosa ci insegnano i vostri agenti
<!-- layout: CONTENUTO -->

Aprite in Copilot l'agente che avete creato il 28 ottobre e rileggete le sue istruzioni.

- Fategli una domanda di prova: risponde come volevate?
- Quale istruzione ha funzionato? Quale no, o era troppo vaga?
- Che cosa cambiereste oggi, e perché?

Alcune coppie mostreranno il proprio agente alla classe.

---

# Slide 06 — Cercare nei documenti
<!-- layout: SEZIONE -->

Il Blocco appunti di Copilot.

---

# Slide 07 — Che cos'è il Blocco appunti
<!-- layout: CONTENUTO -->

Uno spazio di Copilot in cui raccogliete i documenti di un lavoro.

Quando fate una domanda, Copilot cerca le parti utili in quei documenti, risponde e indica da dove ha preso le informazioni.

Serve per trovare, spiegare e collegare informazioni.

Ogni risposta va controllata aprendo il documento citato.

---

# Slide 08 — I documenti della P03
<!-- layout: CONTENUTO -->

| Documento | Che cosa contiene |
| --- | --- |
| Diari di produzione, gennaio–giugno 2026 (6 file) | Ogni evento della pressa con data e ora; un riepilogo in testa a ogni mese |
| Guida agli allarmi IO-P03-07 | Che cosa significa ogni allarme e chi interviene |
| Regole degli indicatori PR-IND-03 | Come si calcolano i numeri del riepilogo |
| Registro del 13–15 ottobre 2026 | Gli appunti del fermo di ottobre |
| Documenti pubblici | Presse, circuito idraulico, sensori e sicurezza |

---

# Slide 09 — Che cosa dovete scoprire
<!-- layout: CONTENUTO -->

Scrivete voi le domande per il Blocco appunti.

- Chi segue gli allarmi: che cosa significano e chi interviene; un'informazione che si ottiene solo unendo due documenti.
- Chi segue i numeri: come il reparto calcola il riepilogo mensile; quanti fault ci sono in un mese scelto da voi, contati con la ricerca di Word.

Per ogni risposta aprite il documento citato e controllate.

---

# Slide 10 — Contare e calcolare
<!-- layout: SEZIONE -->

Un agente di Copilot che usa Python.

---

# Slide 11 — Python e la scheda di passaggio
<!-- layout: CONTENUTO -->

Il Blocco appunti può saltare righe quando conta. Python legge tutte le righe del file Excel, ma calcola solo con le regole che gli date.

L'agente non vede il Blocco appunti. Chi segue i numeri scrive per lui la scheda di passaggio:

- domanda, definizioni e documento da cui vengono;
- dati necessari e dove si trovano;
- controlli, forma della risposta e, in fondo, la richiesta per le due prove.

Salvatela con Blocco note di Windows: scheda_passaggio_P03.txt.

---

# Slide 12 — Le istruzioni dell'agente
<!-- layout: CONTENUTO -->

Nello stesso momento chi segue gli allarmi scrive le istruzioni in istruzioni_agente_P03.txt: compito, che cosa riceve, che cosa non deve fare, come controlla i risultati, come risponde.

1. Mandatevi i due file e leggete quello del compagno.
2. Correggete insieme la scheda e le istruzioni.
3. Ognuno crea l'agente sul proprio computer, incolla le istruzioni e controlla che sia attivo Interprete di codice, o Code interpreter: se non c'è un interruttore, è già incluso.

---

# Slide 13 — Due prove, stesse istruzioni, stessa richiesta
<!-- layout: CONTENUTO -->

| Prova | Chi la fa | Che cosa consegna all'agente | Che cosa controlla |
| --- | --- | --- | --- |
| A | Chi segue gli allarmi | Solo la scheda di passaggio | Quali numeri può davvero calcolare e da dove li prende |
| B | Chi segue i numeri | Scheda di passaggio e Diari_P03_gennaio_giugno_2026.xlsx | Che Python sia stato eseguito e che i totali tornino con i riepiloghi |

Le due prove si fanno nello stesso momento, ciascuna in una nuova conversazione, con la stessa richiesta.

---

# Slide 14 — Che cosa si perde nel passaggio
<!-- layout: CONTENUTO -->

Confrontate le due prove:

- Quali numeri ha calcolato davvero l'agente nella Prova A?
- Quale definizione di fermo ha usato nella Prova B?
- Quale numero della scheda era scritto come certo?

---

# Slide 15 — Le istruzioni di esempio
<!-- layout: CONTENUTO -->

Il file ESEMPIO_ISTRUZIONI_AGENTE_P03.txt è ora su Teams: lo leggiamo insieme.

Che cosa aggiungete alle vostre istruzioni?

Scrivete le aggiunte, con il motivo, in fondo a istruzioni_agente_P03.txt sul computer di chi segue gli allarmi, sotto «Aggiunte dopo l'esempio».

---

# Slide 16 — La proposta al responsabile
<!-- layout: CONTENUTO -->

Scrivete in proposta_P03.txt, dopo il confronto dei numeri, una proposta di al massimo otto righe:

- il problema o la parte della macchina da affrontare per primo;
- almeno due numeri controllati, con la prova e il controllo superato (per i numeri per tipo: solo la somma);
- almeno un documento citato a sostegno;
- che cosa resta da decidere al responsabile.

Poi chi segue gli allarmi carica i tre file .txt nel compito su Teams.

---

# Slide 17 — Che cosa avete verificato?
<!-- layout: CHIUSURA -->

Che cosa sa fare il Blocco appunti e che cosa sa fare Python?

Che cosa deve contenere una scheda di passaggio?

Quale numero avete controllato, e con che cosa?
