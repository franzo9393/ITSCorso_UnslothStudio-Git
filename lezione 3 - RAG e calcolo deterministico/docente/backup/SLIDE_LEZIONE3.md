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
| 1. Gli agenti della lezione 2 | Copilot e scheda Word | Che cosa ha funzionato e che cosa no |
| 2. Cercare nei documenti | Blocco appunti di Copilot | Risposte con citazioni e scheda di passaggio |
| 3. Contare e calcolare | Agente di Copilot con Python | Numeri controllati e proposta |

Lavorate in coppia: uno usa Copilot, l'altro controlla i documenti. Scambiatevi i compiti a ogni parte.

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

Scrivete le risposte nella scheda. Alcune coppie mostreranno il proprio agente alla classe.

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

Scrivete voi le domande per il Blocco appunti. Dovete scoprire:

- che cosa significano gli allarmi della P03 e chi interviene;
- come il reparto calcola i numeri del riepilogo mensile;
- un'informazione che si ottiene solo unendo due documenti;
- quanti fault ci sono in un mese scelto da voi, controllando a mano.

Per ogni risposta annotate il documento citato e se è giusta.

---

# Slide 10 — La scheda di passaggio
<!-- layout: CONTENUTO -->

L'agente della Parte 3 non vede il vostro Blocco appunti: conosce solo quello che gli consegnate.

La scheda di passaggio è il testo che scrivete per lui:

- la domanda a cui rispondere;
- le definizioni che servono, con il documento da cui vengono;
- i dati necessari e dove si trovano;
- i controlli da fare e la forma della risposta.

Salvatela con Blocco note come scheda_passaggio_P03.txt.

---

# Slide 11 — Contare e calcolare
<!-- layout: SEZIONE -->

Un agente di Copilot che usa Python.

---

# Slide 12 — Perché passiamo a Python
<!-- layout: CONTENUTO -->

Il Blocco appunti cerca le parti utili dei documenti: per contare centinaia di righe può saltarne qualcuna.

Python è un linguaggio di programmazione. L'agente scrive il codice, lo esegue e legge tutte le righe del file Excel con le stesse regole.

Python però calcola solo quello che gli chiedete: con una regola sbagliata, anche il numero è sbagliato.

---

# Slide 13 — Progettate il vostro agente
<!-- layout: CONTENUTO -->

Avete già creato un agente nella lezione 2. Questa volta l'agente deve contare e calcolare con Python.

1. Su carta: compito, che cosa riceve, che cosa non deve fare, come controlla i risultati, come risponde.
2. Scrivete le istruzioni in istruzioni_agente_P03.txt.
3. In Copilot create l'agente, incollate le istruzioni e attivate la funzione che esegue Python: Interprete di codice, oppure Code interpreter se compare in inglese.

---

# Slide 14 — Due prove con lo stesso agente
<!-- layout: CONTENUTO -->

| Prova | Che cosa consegnate all'agente | Che cosa controllate |
| --- | --- | --- |
| A | Solo la scheda di passaggio | Quali numeri può davvero calcolare e da dove li prende |
| B | Scheda di passaggio e Diari_P03_gennaio_giugno_2026.xlsx | Che Python sia stato eseguito e che ogni mese torni con il suo riepilogo |

Usate una nuova conversazione per ogni prova e fate la stessa richiesta.

---

# Slide 15 — Che cosa si perde nel passaggio
<!-- layout: CONTENUTO -->

Confrontate le due prove:

- righe dei diari che non sono mai arrivate all'agente;
- definizioni dimenticate o cambiate lungo la strada;
- numeri copiati come se fossero certi, senza controllo.

La scheda porta la domanda, le definizioni e i controlli. I dati si prendono dal file originale.

---

# Slide 16 — Confrontate con il nostro esempio
<!-- layout: CONTENUTO -->

Dopo la Prova B trovate su Teams il file ESEMPIO_ISTRUZIONI_AGENTE_P03.txt.

- Che cosa c'è nell'esempio che manca nelle vostre istruzioni?
- Che cosa avete previsto voi e l'esempio no?
- Quale versione tenete?

Provatela in una nuova conversazione con la scheda e il file Excel.

---

# Slide 17 — La proposta al responsabile
<!-- layout: CONTENUTO -->

Scrivete nella scheda una proposta di al massimo otto righe:

- il problema o la parte della macchina da affrontare per primo;
- almeno due numeri controllati e da dove vengono;
- almeno un documento citato a sostegno;
- che cosa resta da decidere al responsabile.

Poi caricate su Teams i file indicati nella scheda.

---

# Slide 18 — Che cosa avete verificato?
<!-- layout: CHIUSURA -->

Che cosa sa fare il Blocco appunti e che cosa sa fare Python?

Che cosa deve contenere una scheda di passaggio?

Quale numero avete controllato, e con che cosa?
