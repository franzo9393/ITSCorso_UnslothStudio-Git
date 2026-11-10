# Slide 01 — Un agente che sa fare più cose
<!-- layout: COPERTINA -->

Lezione 4 · Reti neurali e agente con più competenze

12 novembre 2026 · Microsoft Copilot e giochi nel browser

---

# Slide 02 — La richiesta del responsabile
<!-- layout: CONTENUTO -->

«Per la pressa P03 mi serve un solo assistente che sappia fare più lavori: la nota per chi arriva al turno dopo, spiegare un allarme a un operatore nuovo, controllare quanto è durato un fermo.»

Un assistente solo, che capisce da solo quale lavoro gli chiedete.

Prima capiamo come impara un programma. Poi costruite l'agente.

---

# Slide 03 — Il percorso di oggi
<!-- layout: CONTENUTO -->

| Parte | Dove lavorate | Che cosa ottenete |
| --- | --- | --- |
| 1. Come sceglie la parola successiva | Browser | Previsioni scritte |
| 2. Una rete che impara | Browser | La rete più piccola che funziona |
| 3. Imparare dai risultati | Browser | Quando l'uccellino non muore più |
| 4. L'agente con più competenze | Copilot | Istruzioni e casi di prova |

Ognuno da solo, sul proprio computer. Tre file di testo con Blocco note: appunti vostri, non si consegnano. Il docente passa tra i banchi e vi chiede di raccontare.

---

# Slide 04 — Come impara un programma
<!-- layout: SEZIONE -->

Tre giochi nel browser.

---

# Slide 05 — Transformer Explainer
<!-- layout: CONTENUTO -->

Nel browser: poloclub.github.io/transformer-explainer

È un modello piccolo che completa frasi in inglese: non è un assistente. Scarica il modello (circa 650 MB): usate il menu Examples.

1. Scegliete un esempio e guardate le parole proposte, con le probabilità.
2. Prima di muovere Temperature, scrivete in appunti_reti.txt che cosa pensate che succeda alle probabilità.
3. Provate, scrivete che cosa avete visto e perché. Poi chiudete la scheda.

---

# Slide 06 — Una rete che impara
<!-- layout: CONTENUTO -->

Rete neurale: tanti piccoli calcoli collegati. Si addestra con esempi: i collegamenti cambiano finché la rete sbaglia meno. I numeri che cambiano si chiamano pesi.

Nel browser: playground.tensorflow.org

La rete deve dire se un punto è arancione o blu. Metà dei punti serve per addestrare, metà per provare.

---

# Slide 07 — Cercate la rete più piccola
<!-- layout: CONTENUTO -->

Prima il cerchio, poi la spirale.

1. Accendete solo X1 e X2, togliete gli strati nascosti (Hidden layers): riuscirà? Scrivete la previsione.
2. Scrivete il Test loss sotto il quale dite che la rete funziona.
3. Avviate, guardate, fermate.
4. Cambiate una cosa alla volta e cercate la rete più piccola che rispetta il criterio.
5. Cerchio, Noise a 50, rete da 4 e 2 neuroni, qualche migliaio di Epoch: che cosa fanno Training loss e Test loss col tempo?

---

# Slide 08 — Imparare dai risultati
<!-- layout: CONTENUTO -->

Nel browser: xviniette.github.io/FlappyLearning

Nessuno dice agli uccellini che cosa fare. Ognuno ha una piccola rete che guarda due numeri: la sua altezza e il varco. Chi muore presto esce; i migliori restano, con piccole variazioni.

1. Prevedete dopo quante generazioni un uccellino non muore più.
2. Con x5, scrivete la generazione in cui il punteggio sale senza fermarsi.
3. Ricaricate due volte: il numero è lo stesso?

---

# Slide 09 — L'agente con più competenze
<!-- layout: SEZIONE -->

Un solo assistente, più lavori.

---

# Slide 10 — Le parole da conoscere
<!-- layout: CONTENUTO -->

- Agente: un assistente di Copilot con le istruzioni che scrivete voi.
- Competenza: la parte delle istruzioni che spiega come fare un tipo di lavoro.
- Indice delle richieste: dice quale competenza usare per ogni tipo di richiesta.
- Orchestrazione: scegliere la competenza e l'ordine, anche quando una richiesta ne tocca due.

Le istruzioni sono testo che Copilot legge prima della vostra richiesta. Indice e competenze sono testo come gli altri: Copilot li legge e decide. Controllate sempre la risposta.

---

# Slide 11 — Un esempio: il noleggio di biciclette
<!-- layout: CONTENUTO -->

Caso diverso dalla P03, per vedere la struttura. Tre competenze: prenotazione, guasto, rimborso.

Le cinque parti dell'agente, in ordine: regole per tutte le richieste, indice delle richieste, una competenza per ogni lavoro, che cosa fare se la richiesta ne tocca due o nessuna, stile delle risposte.

Scrivete in casi_di_prova.txt, sotto «Esempio del docente»: quali richieste toccano più di una competenza? Come le gestisce?

---

# Slide 12 — Esempio: regole e indice
<!-- layout: CONTENUTO -->

Regola: prima di rispondere scegli la competenza guardando l'indice; scrivi in prima riga «Competenza usata:» e il nome.

Regola: se mancano dati, fai una sola domanda e aspetta.

Indice: prenotare o cambiare orario → PRENOTAZIONE. Bici rotta → GUASTO. Soldi indietro → RIMBORSO.

Due competenze insieme: prima GUASTO, poi RIMBORSO; nella prima riga i due nomi nell'ordine.

---

# Slide 13 — Esempio: una competenza
<!-- layout: CONTENUTO -->

COMPETENZA GUASTO

Quando: la bici è rotta.

Dati necessari: numero della bici e che cosa non funziona. Se manca uno, chiedilo.

Regole: freni o sterzo, «Non usare la bici» e cambio bici. Gomma bucata o catena, cambio bici.

Come rispondere: tre punti. Che cosa hai capito, che cosa fare ora, chi se ne occupa.

---

# Slide 14 — I tre lavori da fare
<!-- layout: CONTENUTO -->

| Lavoro | Documento | Che cosa ottiene |
| --- | --- | --- |
| 1. Passaggio di turno | Registro P03 | Nota per chi arriva dopo |
| 2. Spiegare un allarme | Guida allarmi | Risposta breve per un operatore nuovo |
| 3. Durata del fermo | Regole indicatori e registro | Minuti di fermo e pezzi persi |

Limiti di ogni lavoro: nella consegna. In tutti: solo i testi che gli date, niente di inventato, prima riga «Competenza usata:».

---

# Slide 15 — Progettate il vostro agente
<!-- layout: CONTENUTO -->

Due lavori su tre, a vostra scelta.

Scrivete il testo voi in Blocco note, non chiedetelo a Copilot. In istruzioni_assistente_P03.txt, in ordine: regole per tutte, indice, una competenza per lavoro, che cosa fare con due competenze o nessuna, stile con almeno due vostri esempi.

Le scelte sono vostre: nome, quante competenze, parole dell'indice, quando fare una domanda, stile.

---

# Slide 16 — Create e provate
<!-- layout: CONTENUTO -->

1. In Copilot create l'agente: il docente vi mostra dove. Usate solo il campo delle istruzioni.
2. Incollate il testo, senza «Correzioni dopo le prove», e salvate.
3. Nuova conversazione: incollate i documenti che servono e, sotto, la richiesta.
4. Una richiesta per ogni competenza e una che ne tocca due, ognuna in una nuova conversazione. Se l'agente vi fa una domanda, rispondete.
5. Controllate la riga «Competenza usata» e la risposta sul documento. Correggete e riprovate.

---

# Slide 17 — Mettete alla prova il vostro agente
<!-- layout: CONTENUTO -->

Rileggete il vostro indice: che cosa non prevede? Dove due competenze si toccano?

Inventate cinque casi critici. Cercate che cosa avete dimenticato di prevedere. Ci devono essere: una richiesta fuori indice, una su due competenze, una a cui manca un dato, una che chiede un dato che il documento non contiene, una per la competenza provata meno.

Prima di provare, in casi_di_prova.txt: richiesta, competenza attesa, dato atteso.

Dopo la risposta: competenza usata, dato nel documento sì o no, OK o ERRORE, perché. ERRORE anche con la competenza giusta e un dato che nel documento non c'è.

---

# Slide 18 — Correggete
<!-- layout: CONTENUTO -->

Per ogni ERRORE decidete che cosa correggere: regola generale, indice, competenza, richiesta o documento.

Scrivete sotto «Correzioni dopo le prove» che cosa avete cambiato, il motivo e l'esito. Tutti OK? Scrivete quale regola ha funzionato e aggiungete la regola per un caso nuovo. Nell'agente mettete solo il testo, senza «Correzioni dopo le prove».

---

# Slide 19 — Istruzioni o addestramento
<!-- layout: CONTENUTO -->

Stessa richiesta e stessi documenti, tre conversazioni nuove:

1. Con il vostro agente.
2. Con Copilot normale, senza agente.
3. Ancora con il vostro agente: due risposte uguali? Perché? Scegliete la migliore e scrivete due motivi.

Scelte come questa sono il dato con cui si può addestrare uno stile: quante ne servirebbero? Che cosa cambierebbe dentro il modello?

In Playground e in Flappy cambiavano i pesi. Nel vostro agente: i numeri dentro Copilot o il testo che Copilot legge?

---

# Slide 20 — I vostri appunti
<!-- layout: CONTENUTO -->

Non c'è niente da consegnare o da caricare: i tre file .txt sono appunti vostri, per ricordare e raccontare a voce.

| File | Contenuto |
| --- | --- |
| appunti_reti.txt | I tre giochi; istruzioni o addestramento |
| istruzioni_assistente_P03.txt | Il testo dell'agente e le correzioni |
| casi_di_prova.txt | Esempio del docente e casi per il vostro agente |

---

# Slide 21 — Se Copilot non funziona
<!-- layout: CONTENUTO -->

Avvisate il docente.

- L'agente non si crea o non accetta il testo: conversazione normale. In ogni nuova conversazione incollate per prime le istruzioni, poi documenti e richiesta. Non sono vere istruzioni dell'agente. Scrivetelo nei casi.
- Copilot non risponde: sulla carta. Per ogni caso cercate nel vostro testo la riga che lo gestisce e copiatela accanto al caso. Nessuna riga: ERRORE.

---

# Slide 22 — Che cosa avete verificato?
<!-- layout: CHIUSURA -->

Che cosa cambia in un programma quando lo si addestra, e che cosa quando gli si scrivono istruzioni?

Quale regola dell'indice ha reso l'agente più affidabile?

Quale caso di prova vi ha fatto cambiare o confermare le istruzioni?
