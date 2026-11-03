# Slide 01 — L'assistente di reparto della P03
<!-- layout: COPERTINA -->

Lezione 3 · Documenti, codici e calcolo con Python

4 novembre 2026 · Microsoft Copilot Basic

---

# Slide 02 — Che cosa costruite oggi
<!-- layout: CONTENUTO -->

L'assistente di reparto è Microsoft Copilot con le istruzioni che progettate voi. Aiuta il banco ricambi a consultare i documenti delle presse e a calcolare con Python le confezioni da ordinare.

- Prepara proposte e tabelle da verificare: non ordina materiale e non modifica il magazzino.
- Una persona usa Copilot; l'altra controlla i documenti e annota i riscontri nella scheda Word.
- Scambiate i compiti durante il lavoro.

---

# Slide 03 — Tre documenti nel fascicolo 01_DOCUMENTI_P03.txt
<!-- layout: CONTENUTO -->

| Documento | Contenuto e data di riferimento |
| --- | --- |
| Doc. 1 — Diario P03 | 24 appunti del 13–15 ottobre 2026 (il 14/10 viene montato FLT-992) |
| Doc. 2 — Catalogo e manuale P001/75 | Filtri rev. 2 (18/10/2026) + estratto manuale Fervi P001/75 (problemi e 68 ricambi) |
| Doc. 3 — Magazzino e confezioni | Saldi chiusi al 19 ottobre 2026, ore 08:00, pezzi per confezione e prezzi |

Aprite da Teams la scheda ATTIVITA_LEZIONE3.docx e il fascicolo 01_DOCUMENTI_P03.txt.

---

# Slide 04 — Esplorare i documenti e scrivere le istruzioni
<!-- layout: SEZIONE -->

Riconoscere i codici omonimi, distinguere le tre quantità e progettare le regole.

---

# Slide 05 — Perché non basta il nome del pezzo?
<!-- layout: CONTENUTO -->

Nel manuale reale della pressa P001/75 (Documento 2):

- la tabella problemi di pag. 26 dice solo «Sostituite le tenute», senza indicare il codice;
- nella tabella dei 68 ricambi di pag. 28 compaiono 3 codici diversi chiamati «O-ring», 3 chiamati «Rondella elastica» e 10 chiamati «Vite»;
- per il filtro della P03 bisogna distinguere il ricambio montato il 14/10 (FLT-992) da quello previsto dal catalogo del 18/10 (FLT-993).

Senza il codice completo, l'assistente non deve indovinare: deve mostrare i codici omonimi e chiedere quale serve.

---

# Slide 06 — Tre quantità con significati diversi
<!-- layout: CONTENUTO -->

| Dove si legge il numero | Che cosa significa |
| --- | --- |
| Doc. 2 — Quantità nella macchina | Quanti pezzi di quel codice sono montati su 1 sola pressa |
| Doc. 3 — Disponibilità | Quanti pezzi singoli sono già presenti in magazzino al 19/10 |
| Doc. 3 — Pezzi per confezione | Quanti pezzi contiene 1 confezione venduta dal fornitore |

Scegliete 6 codici (1 filtro + 5 ricambi della pressa P001/75, con almeno due nomi ripetuti) e compilate la prima tabella della scheda.

---

# Slide 07 — Scrivete istruzioni_assistente_P03.txt
<!-- layout: CONTENUTO -->

Scrivete con parole vostre le istruzioni per l'assistente (senza farle generare a Copilot):

- citare sempre documento, codice completo e data di riferimento;
- se il collega scrive un nome generico con più codici nel manuale («O-ring», «Vite», «Rondella elastica») o omette il numero di presse, fermarsi e chiedere chiarimento;
- se codici e numero di presse sono chiari, eseguire subito il calcolo con Python e creare il file .csv;
- chiudere con PROPOSTA DA CONTROLLARE oppure SERVE UN CONTROLLO.

---

# Slide 08 — Calcolo con Python e verifica del .csv
<!-- layout: SEZIONE -->

Dalla distinta della macchina alle confezioni da ordinare.

---

# Slide 09 — Che cosa deve calcolare Python
<!-- layout: CONTENUTO -->

Per ciascuno dei 6 codici richiesti per N presse, Python calcola:

- Fabbisogno = N presse × Pezzi su 1 macchina (dal Doc. 2)
- Pezzi mancanti = Fabbisogno − Disponibilità in magazzino (zero se la scorta basta)
- Confezioni da ordinare = Pezzi mancanti ÷ Pezzi per confezione (arrotondato per eccesso)
- Costo in euro = Confezioni da ordinare × Prezzo per confezione (dal Doc. 3)

Non si arrotonda il fabbisogno: si arrotondano all'intero superiore soltanto le confezioni da acquistare.

---

# Slide 10 — Eseguite la prova e controllate una riga a mano
<!-- layout: CONTENUTO -->

1. Aprite una nuova conversazione in Copilot, inviate le istruzioni e allegate 01_DOCUMENTI_P03.txt.
2. Chiedete il calcolo per i vostri 6 codici su più presse (senza scrivere scorte o prezzi nella domanda).
3. Verificate che Python sia stato realmente eseguito nella sandbox (codice solo scritto in chat non basta).
4. Scaricate il file .csv, apritelo in Excel o LibreOffice Calc e controllate a mano una riga completa nella scheda.

---

# Slide 11 — Collaudo incrociato in due mosse
<!-- layout: SEZIONE -->

Mettete alla prova l'assistente di un'altra coppia e verificate il ricalcolo.

---

# Slide 12 — Come si svolge il collaudo tra coppie
<!-- layout: CONTENUTO -->

La coppia A apre una conversazione nuova con le proprie istruzioni e 01_DOCUMENTI_P03.txt. La coppia B prova l'assistente sul computer di A in due mosse:

1. Mossa 1 (richiesta ambigua): chiede i ricambi per più presse usando almeno un nome generico senza codice («gli O-ring e le rondelle elastiche»). Verifica se l'assistente elenca i codici omonimi e chiede quale serve.
2. Mossa 2 (codici e ricalcolo): fornisce i codici completi e cambia il numero di presse. Verifica che Python aggiorni il .csv.

Poi invertite i ruoli sul computer di B.

---

# Slide 13 — Revisione e consegna su Teams
<!-- layout: CONTENUTO -->

Dopo il collaudo dei compagni, decidete quale regola delle vostre istruzioni conservare o migliorare.

Caricate su Teams:

- la scheda ATTIVITA_LEZIONE3.docx compilata (comprese le 2 risposte individuali svolte senza Copilot);
- il file istruzioni_assistente_P03.txt nella versione finale;
- il file .csv prodotto da Python e controllato.

---

# Slide 14 — Che cosa avete verificato?
<!-- layout: CHIUSURA -->

Perché il solo nome del ricambio non basta senza il codice del manuale?

Qual è la differenza tra pezzi sulla macchina, pezzi in magazzino e pezzi per confezione?

Quale decisione resta sempre a una persona?
