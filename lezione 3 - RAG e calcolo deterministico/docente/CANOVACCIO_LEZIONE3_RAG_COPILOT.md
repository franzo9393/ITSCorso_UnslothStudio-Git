# Lezione 3 — L'assistente di reparto della P03

**Canovaccio docente · ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot Basic**

Sintesi operativa della lezione per il docente. «Assistente di reparto» indica Microsoft Copilot con le istruzioni progettate dagli studenti per il banco ricambi, non un programma separato.

**Stato delle prove:** l'esecuzione di Python e l'esportazione del file `.csv` sono state osservate nell'ambiente del docente; la lettura del nuovo fascicolo `01_DOCUMENTI_P03` e l'esecuzione sulle postazioni degli studenti vanno verificate con un account scolastico prima dell'aula.

## 1. Obiettivo e struttura in tre blocchi

Gli studenti progettano le istruzioni per un assistente che consulta il fascicolo `01_DOCUMENTI_P03.txt` (diario P03, catalogo filtri + estratto reale del manuale pressa Fervi `P001/75`, situazione di magazzino e confezioni al **19 ottobre 2026 ore 08:00**), riconosce i ricambi omonimi senza indovinare e usa **Python** per calcolare fabbisogno, pezzi mancanti, confezioni intere da ordinare e costo in euro, salvando il risultato in `.csv`.

Il lavoro in aula segue tre soli blocchi operativi più la verifica individuale:

1. **Blocco 1 — Esplorazione delle fonti e scrittura delle istruzioni:** scelta di 6 codici (1 filtro + 5 ricambi `P001/75` con almeno due omonimi), verifica manuale delle tre quantità (pezzi su 1 macchina, scorta a magazzino, pezzi per confezione) e stesura di `istruzioni_assistente_P03.txt`.
2. **Blocco 2 — Prova con Python e verifica del `.csv`:** invio della richiesta per $N$ presse in una nuova conversazione con `01_DOCUMENTI_P03.txt`, verifica dell'esecuzione reale di Python nella *sandbox*, scaricamento del `.csv` e controllo manuale di una riga completa.
3. **Blocco 3 — Collaudo incrociato in due mosse e revisione:** la coppia B prova l'assistente di A prima con una richiesta ambigua su voci omonime (`O-ring`, `Vite`, `Rondella elastica`, `tenute`) senza codice, poi fornendo i codici completi e cambiando il numero di presse per verificare il ricalcolo in Python. Seguono l'eventuale correzione della regola e le due risposte individuali senza Copilot.

## 2. Perché servono sia il recupero sui documenti sia Python

- **Recupero documentale (RAG):**
  - distinguere il filtro storico montato il 14/10 (`FLT-992`, Doc. 1) dal filtro previsto dal catalogo rev. 2 del 18/10 (`FLT-993`, Doc. 2);
  - nella distinta reale dei 68 ricambi della pressa `P001/75` (Doc. 2, pag. 28) compaiono più codici con la stessa descrizione (`O-ring`: `/08`, `/20`, `/45`; `Rondella elastica`: `/05`, `/18`, `/47`; `Rondella`: `/06`, `/19`, `/50`; `Vite`: 10 codici diversi; `Anello di nylon`: `/42`, `/61`), mentre la tabella problemi di pag. 26 parla genericamente di «tenute»;
  - distinguere i **tre significati di quantità**: pezzi montati su 1 macchina (Doc. 2), pezzi già in magazzino (Doc. 3, saldi chiusi al 19/10) e pezzi per confezione acquistabile (Doc. 3).
- **Calcolo deterministico (Python):**
  - calcolare su tutte le 6 righe: `Fabbisogno = N_presse × Pezzi_su_1_macchina`, `Mancanti = max(0, Fabbisogno − Scorta)`, `Confezioni = ceil(Mancanti / Pezzi_per_confezione)`, `Pezzi_acquistati = Confezioni × Pezzi_per_confezione`, `Costo = Confezioni × Prezzo_confezione`, esportando il `.csv`.

## 3. Consegna su Teams

1. `ATTIVITA_LEZIONE3.docx` compilata (tabella dei 6 codici, controllo di 1 riga del calcolo Python, esito del collaudo in 2 mosse, 2 risposte individuali per studente);
2. `istruzioni_assistente_P03.txt`;
3. file `.csv` generato da Python.
