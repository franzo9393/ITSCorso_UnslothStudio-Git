## Slide 01 – Possiamo fidarci di questa risposta?

**ITS MAKER Bologna · Costruire e verificare un assistente documentale**

> Nel catalogo didattico corrente, quale filtro è associato alla P03?

- Chiederlo subito in una chat pulita, senza documenti.
- Annotare la risposta: dato, astensione o invenzione.
- Senza il catalogo, come possiamo verificarla?
- Questa è una baseline, non ancora una prova RAG.

> **Regia docente · B1:** Studio già avviato, workspace già distribuiti. Nessuna installazione. Non imporre che il modello sbagli e non caricare ancora il corpus.

---

## Slide 02 – Il progetto delle sei ore

| Blocco | Minuti | Risultato |
| --- | ---: | --- |
| B1 · Problema e fondamenti | 40 | Plausibilità non è evidenza |
| B2 · Primo RAG guidato | 65 | T01 con fonti controllate |
| B3 · Prove e diagnosi | 75 | T02–T07, due giudizi |
| B4 · Aggiornare le fonti | 40 | Corrente distinto dallo storico |
| B5 · Git sulle evidenze | 25 | Risultati conservati |
| B6 · Autonomia | 70 | Documento nuovo e collaudo |
| Pause/margine | 45 | Totale 360 minuti |

> **Regia docente:** 315 minuti netti, spiegazioni comprese. Il RAG è il filo conduttore. Confronto modelli e OpenCode non sono richiesti nelle sei ore.

---

## Slide 03 – Due ruoli, una verifica

- **Operatore:** usa Studio e registra i risultati.
- **Collaudatore:** apre le fonti, controlla dati e giudizi.
- Scambio a ogni blocco; revisione finale con la coppia vicina.
- Solo dati sintetici: nessun collegamento a macchine o PLC.
- Il prodotto finale è un assistente documentale collaudato, non un controllo macchina.

> **Regia docente:** Far formulare a ogni coppia la domanda «dove è scritto?». Il risultato non è ottenere sempre una risposta corretta, ma saperla valutare.

---

## Slide 04 – Contesto non significa addestramento

- Inserire: «Il codice colore inventato del turno è BLU-17».
- Chiedere il codice nella stessa chat.
- Ripetere in una chat pulita, senza memorie o allegati.
- **Contesto:** informazioni disponibili in quella richiesta.
- **Addestramento:** modifica i pesi; non lo facciamo nel corso.

> **Regia docente · B1:** Osservare gli esiti senza imporli. Una cronologia salvata dall'applicazione non è un aggiornamento dei pesi. Riavviare il modello non cancella necessariamente la chat.

---

## Slide 05 – Le parole necessarie, senza configurazioni

- **LLM:** genera testo a partire dal contesto.
- **Token:** unità di testo elaborate dal modello.
- **Embedding:** rappresentazione utile a confrontare domanda e passaggi.
- **Studio:** ambiente per chat e ricerca documentale.
- Fluidità e somiglianza non sono prove di correttezza.

> **Regia docente:** Spiegazione qualitativa breve. Niente benchmark obbligatorio, scelta dei modelli o calcolo della RAM: servono al tecnico che prepara, non a questa prima attività.

---

## Slide 06 – RAG: cercare prima di rispondere

1. **Corpus:** documenti da consultare.
2. **Indice:** passaggi preparati per la ricerca.
3. **Recupero:** passaggi pertinenti alla domanda.
4. **Generazione:** risposta con quei passaggi nel contesto.
5. **Verifica:** lettura delle fonti da parte nostra.

**Aggiornare i documenti non riaddestra il modello.**

> **Regia docente · B2:** Usare questo schema durante tutta la lezione. I documenti sono piccoli per rendere la verifica praticabile, non per dimostrare scalabilità industriale.

---

## Slide 07 – Cinque documenti, un caso leggibile

| Fonte | Contenuto |
| --- | --- |
| DOC-P03 | Scheda e soglia della P03 |
| DOC-FERMO | Evento storico della P03 |
| DOC-RICAMBI | Catalogo corrente dei filtri |
| DOC-BOLLA | Quantità ordinate e consegnate |
| DOC-P30 | Un'altra macchina, non la P03 |

- Associare solo i cinque file di `corpus/`.
- Non caricare CSV, quaderno o soluzioni.

> **Regia docente · B2:** Mostrare titolo, DocID e revisione di una fonte prima di interrogarla. Ogni coppia lavora sulla propria cartella già pronta.

---

## Slide 08 – Il primo ciclo completo, insieme

- Aprire una chat pulita e associare i cinque file.
- Attendere l'indicizzazione.
- Chiedere di usare passaggi e citare DocID, sezione, revisione.
- Se manca evidenza, chiedere di dichiararlo.
- Ripetere T01 e aprire passaggi recuperati e fonte.

> **Regia docente · B2:** Mostrare il percorso della release congelata; quello documentato è + → Chat with Files → Add files to chat with. Non far configurare embedding o parametri. Il prompt completo è nel quaderno.

---

## Slide 09 – Due verifiche indipendenti

| Recupero | Risposta | Diagnosi possibile |
| --- | --- | --- |
| OK | OK | Evidenza trovata e usata correttamente |
| OK | ERRORE | Fonte giusta, interpretazione sbagliata |
| ERRORE | OK | Risposta corretta per caso, processo non provato |
| ERRORE | ERRORE | Cercare prima il problema nelle fonti recuperate |

- Se il recupero non è osservabile: **NON_ESEGUITO** e nota.
- Una citazione scritta dal modello va aperta, non soltanto contata.

> **Regia docente:** Le combinazioni sono possibilità da comprendere, non esiti da fabbricare. Un allegato letto per intero non dimostra ricerca selettiva.

---

## Slide 10 – Poche annotazioni, evidenze precise

- Aprire `risultati.csv` nella tabella predisposta.
- Registrare risposta breve e fedele, non tutta la conversazione.
- Fonte: DocID, sezione e revisione.
- Due giudizi: **OK / ERRORE / NON_ESEGUITO**.
- Una nota utile per spiegare errore, controllo o limite.

> **Regia docente · B2:** Compilare T01 insieme. Il foglio è già predisposto per CSV UTF-8 con separatore ; e otto colonne invariate. La baseline B1 resta nel quaderno, distinta dalle prove RAG.

---

## Slide 11 – T02 e T03: i numeri vanno controllati

- **T02:** di quanti gradi la temperatura supera la soglia del rapporto?
- Recuperare entrambi i numeri e calcolare la differenza indipendentemente.
- **T03:** quanti cuscinetti sono stati consegnati, non ordinati?
- Leggere la fonte: numeri vicini possono descrivere fatti diversi.

> **Regia docente · B3:** Usare le domande esatte del quaderno/CSV. Non usare un secondo modello come prova del calcolo. Non mostrare le soluzioni prima delle osservazioni.

---

## Slide 12 – T04 e T06: parole simili, oggetti diversi

- **T04:** quanto è durata l'indisponibilità della P03?
- La fonte può parlare di «fermo»: la ricerca deve trovare il fatto.
- **T06:** soglia P03 e macchina a cui si riferiscono 55 °C.
- P03 e P30 non sono intercambiabili.
- Controllare entrambe le parti della risposta sulle rispettive schede.

> **Regia docente · B3:** Far indicare il passaggio prima di assegnare OK. Il recupero per similarità può confondere codici quasi uguali.

---

## Slide 13 – T05: saper dire «non disponibile»

> Qual è la coppia di serraggio dei bulloni della testata P03?

- Verificare nel corpus che il dato non sia presente.
- Passaggi simili non sostengono un numero inventato.
- Zero risultati non dimostrano da soli l'assenza del dato.
- Risposta corretta: astensione senza valori o citazioni fabbricate.
- Se inventa: **ERRORE**, con spiegazione; non correggere la misura.

> **Regia docente · B3:** Recupero OK solo con osservazione dei passaggi e conferma dell'assenza nel corpus; altrimenti NON_ESEGUITO. Il dato omesso è un test necessario, non un incidente.

---

## Slide 14 – T07: ora la domanda è vostra

- Formulare una domanda che incroci i documenti iniziali.
- Indicare prima quali evidenze servono per giudicarla.
- Inviarla, aprire i passaggi e assegnare i due giudizi.
- Aggiungere T07 alla tabella con le stesse colonne.
- Discutere: manca la fonte o la risposta la usa male?

> **Regia docente · B3:** Se non emerge un errore reale, discutere un rischio motivato senza inventare un'osservazione. Il metodo conta più del successo del modello.

---

## Slide 15 – Prima di aggiornare: conservare

- Salvare e chiudere la tabella.
- Copiare `risultati.csv` in `risultati_rev1.csv`.
- Ricevere il catalogo rev2 dal docente.
- Sostituire il contenuto del catalogo corrente, senza duplicarlo.
- Non sovrascrivere le evidenze iniziali.

> **Regia docente · B4:** In questo blocco bastano copie esplicite: Git arriva in B5. Il file corrente resta corpus/03_catalogo_ricambi.md; cambia il contenuto e la revisione.

---

## Slide 16 – Il presente cambia, il passato no

- Nuova chat: associare i cinque file aggiornati e attendere l'indice.
- Ripetere T01 e verificare fonte e revisione corrente.
- Chiedere anche quale filtro fu usato nell'evento storico.
- Conservare la risposta storica e la sua fonte nelle note di T01.
- Salvare `risultati_rev2.csv` dopo il confronto.

> **Regia docente · B4:** Controllo atteso: catalogo rev2 FLT-993, storico FLT-992. Se la risposta resta vecchia, registrare l'errore e controllare fonte/contesto. Cambiare solo il file sul disco non aggiorna la vecchia chat.

---

## Slide 17 – Git salva le nostre evidenze

Dalla cartella personale:

```text
git init
git config user.name "Nome Cognome"
git config user.email "nome.cognome@studenti.itsmaker.it"
git status
git add corpus risultati.csv risultati_rev1.csv risultati_rev2.csv genera_report.py
git commit -m "test: conserva prove RAG e confronto revisioni"
```

> **Regia docente · B5:** Identità solo locale. Non ricostruiamo una storia Git precedente: conserviamo stato attuale e copie delle prove. Niente esercizio separato sugli RPM.

---

## Slide 18 – Capire una modifica, poi salvarla

- Aggiungere una motivazione reale nelle note di T07 e salvare.

```text
git diff risultati.csv
git add risultati.csv
git commit -m "docs: motiva la verifica delle fonti T07"
git log --oneline
```

- `diff`: lavoro rispetto all'indice; `add`: prepara; `commit`: salva.
- Niente `reset --hard` o `clean`; dubbi sul ripristino al docente.

> **Regia docente · B5:** Non conta il numero di commit. Chiedere di mostrare una differenza e spiegare quale evidenza è stata conservata.

---

## Slide 19 – Documento nuovo: trasferire il metodo

- Creare `corpus/06_scheda_macchina_T10.md`.
- Titolo, DocID **DOC-T10**, revisione e data.
- Due dati inventati verificabili, un dato intenzionalmente omesso.
- Il dato omesso deve mancare anche dagli altri documenti.
- Nessuna procedura reale né istruzione rivolta al modello.

> **Regia docente · B6:** 15 minuti. Annotare il dato omesso separatamente, senza caricarlo nel RAG. La prima prova su documento nuovo è obbligatoria nelle sei ore, non rinviata all'estensione.

---

## Slide 20 – T08 e T09: il vicino fa il collaudo

- Nuova chat con il corpus corrente e il sesto file.
- **T08:** domanda su un dato presente nella nuova scheda.
- **T09:** domanda sul dato omesso.
- Coppia vicina: aprire le fonti, controllare e motivare i due giudizi.
- Aggiungere le due righe al CSV, senza cambiarne le colonne.

> **Regia docente · B6:** 15 minuti indicizzazione/prove e 15 revisione. Non esigere che il modello passi: esigere una diagnosi fondata e onesta.

---

## Slide 21 – Un report, senza scrivere codice

Dalla cartella personale:

```text
python genera_report.py
```

- Aprire `report.html` nel browser.
- Verificare T01–T09, risposte e giudizi rispetto alla tabella.
- Il report visualizza valutazioni umane, non certifica il modello.
- Non serve OpenCode e non è richiesto un filtro interattivo.

> **Regia docente · B6:** Salvare/chiudere prima il foglio. Se Python si chiama python3, il comando deve essere già adattato nell'immagine d'aula.

---

## Slide 22 – Consegna e restituzione

- Corpus corrente, compresa DOC-T10.
- `risultati_rev1.csv`, `risultati_rev2.csv`, `risultati.csv` finale.
- `report.html`, coerente con T01–T09.
- Note: almeno un errore o rischio con la sua evidenza.
- Salvataggio Git finale; nessuna credenziale o soluzione docente.

> **Regia docente · B6:** 15 minuti report/consegna e 10 restituzione. Usare i comandi espliciti del quaderno. Chiedere una risposta affidabile, un limite e perché il catalogo aggiornato non riscrive lo storico.

---

## Slide 23 – Valutiamo il vostro metodo

| Criterio | Peso |
| --- | ---: |
| Fonti e diagnosi recupero/risposta | 40% |
| Revisioni e storico | 25% |
| Autonomia e test negativo | 20% |
| Tracciabilità delle evidenze e Git | 10% |
| Collaborazione | 5% |

**Un errore AI correttamente diagnosticato è un buon risultato.**

> **Regia docente:** Non valutare con il tasso di successo del modello o il numero di commit. Benchmark e OpenCode non cambiano la rubrica del percorso base.

---

## Slide 24 – Se abbiamo otto ore

- **E1 · +60 min:** stessa domanda in forma letterale, con sinonimi e in gergo.
- Stesso corpus/configurazione; confrontare i passaggi, non modificare parametri.
- **E2 · +60 min:** corpus ampliato e sfida cieca fra coppie.
- Domande su dati presenti e assenti, con diagnosi delle evidenze.
- Le appendici possono sostituire E2, non aggiungersi alle otto ore.

> **Regia docente:** Scegliere eventuale alternativa prima del corso. Non sacrificare la prova autonoma B6 per una dimostrazione di strumenti.

---

## Slide 25 – Appendice docente: preparare, non improvvisare

**Fuori dal percorso studente: prima dell'aula.**

- Una release, un LLM, un embedding multilingue, schermate dei menu.
- Provare offline, passaggi osservabili, rev2 e documento nuovo.
- Verificare foglio CSV, report, Git e carico delle 10–12 coppie.
- Il launcher usa `RAG_THREAD_WHOLE_DOC=0`: verificarne l'effetto nella release.
- Le variabili offline non sono un firewall; il preflight non certifica il RAG.

> **Regia docente:** Scheda e GO/NO-GO in laboratorio/docente/SOLUZIONI.md. La configurazione non è già qualificata dal repository. Un endpoint di sola generazione non è un fallback del recupero documentale.

---

## Slide 26 – Appendice facoltativa: agente o confronto modelli

**Una sola alternativa a E2, preparata prima del corso.**

- **OpenCode:** modifica controllata di `genera_report.py` per il filtro «Solo da rivedere».
- Diff, report rigenerato, filtro acceso/spento e conteggi invariati.
- Fixture separata dai risultati AI; backend e permessi già verificati.
- **Oppure confronto modelli:** due configurazioni pronte, stesso prompt e misure reali.
- Per isolare la quantizzazione: stesso modello e revisione.

> **Regia docente:** Dettagli nelle appendici della guida. Nessuna dipendenza aggiuntiva nel GO base. Niente configurazioni, chiavi o download da risolvere durante la lezione.
