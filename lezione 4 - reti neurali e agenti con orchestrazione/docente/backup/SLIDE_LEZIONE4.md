# Slide 01 — Un agente, più lavori
<!-- layout: COPERTINA -->

Reti neurali da esplorare. Un agente da costruire.

ITS MAKER · 12 novembre 2026 · Microsoft Copilot e giochi nel browser

---

# Slide 02 — La stessa richiesta, la stessa risposta?
<!-- layout: CONTENUTO -->

> Se chiedete due volte la stessa cosa all’AI, deve rispondere allo stesso modo?

Scegliete: sempre, qualche volta, mai.

---

# Slide 03 — Come continuereste questa frase?
<!-- layout: CONTENUTO -->

> «La visualizzazione dei dati permette agli utenti di…»

Transformer Explainer usa la frase inglese «Data visualization empowers users to».

Il docente vi aiuta a leggere le parole proposte. Non è una prova d’inglese.

---

# Slide 04 — Spostate la probabilità
<!-- layout: CONTENUTO -->

## Prima sopra il 90%. Poi sotto il 30%.

Portate la barra più lunga sui due bersagli, cambiando solo Temperature.

poloclub.github.io/transformer-explainer · primo esempio, k = 5

---

# Slide 05 — La parola più probabile non è l’unica
<!-- layout: CONTENUTO -->

> Alzando la temperatura, le probabilità si distribuiscono di più.

Una barra alta non garantisce quale parola uscirà. E non garantisce che una frase sia vera.

---

# Slide 06 — Quanto piccola può essere una rete?
<!-- layout: CONTENUTO -->

## Test loss sotto 0,05

Sul cerchio, entro 1.500 Epoch. Con meno neuroni nascosti possibile.

Test loss: errore sui punti di prova. Epoch: giri di addestramento.

playground.tensorflow.org

---

# Slide 07 — Togliete un neurone. Funziona ancora?
<!-- layout: CONTENUTO -->

> Il vostro record è la rete più piccola che avete visto riuscire.

Partite da 4 e 2 neuroni. Cambiate una scelta alla volta, sugli stessi punti.

Poi provate con la spirale: lo stesso criterio è ancora raggiungibile?

---

# Slide 08 — Continuare è sempre meglio?
<!-- layout: CONTENUTO -->

| Guardiamo i punti… | Il sito scrive… |
| --- | --- |
| usati per addestrare | Training loss |
| tenuti da parte per la prova | Test loss |

Il docente aggiunge rumore. Prima di proseguire, scommettete: miglioreranno entrambi?

---

# Slide 09 — Chi arriva a 10.000?
<!-- layout: CONTENUTO -->

## Score almeno 10.000

In quale fascia di Generation lo vedrete: 1–10, 11–30, 31–60, oltre 60?

Score misura i passi della simulazione, non i tubi superati.

xviniette.github.io/FlappyLearning

---

# Slide 10 — Stesso gioco. Stessa generazione?
<!-- layout: CONTENUTO -->

> Ricaricate una volta. Cambiereste la vostra previsione?

Restano le reti con i risultati migliori, con variazioni e nuove reti casuali.

Non state guidando gli uccellini: osservate una selezione. Un volo lungo non è un volo infinito.

---

# Slide 11 — Adesso cambiamo le istruzioni
<!-- layout: SEZIONE -->

Microsoft Copilot legge il testo che scrivete voi.
Non state addestrando i suoi pesi.

---

# Slide 12 — Prima, un altro caso: il noleggio di biciclette
<!-- layout: CONTENUTO -->

Non è la P03. Serve a vedere come un agente sceglie tra più lavori, senza darvi un testo da copiare.

> «La bici 12 ha i freni che non tengono. Mi ridate anche i soldi?»

Quale lavoro viene prima? Quale dato deve chiedere l’agente?

---

# Slide 13 — Un indice per scegliere il lavoro
<!-- layout: CONTENUTO -->

| Se la richiesta riguarda… | L’agente usa… |
| --- | --- |
| prenotare o cambiare orario | PRENOTAZIONE |
| una bici rotta | GUASTO |
| soldi indietro | RIMBORSO |

Ogni competenza è una parte delle istruzioni. Orchestrare significa scegliere quali usare e in quale ordine. Non sono tre programmi separati.

---

# Slide 14 — Adesso torniamo alla pressa P03
<!-- layout: CONTENUTO -->

Il vostro agente deve calcolare un fermo.

Poi, a vostra scelta: spiegare un allarme oppure scrivere una nota di turno.

> Le biciclette erano un esempio. Il testo dell’agente lo scrivete voi.

---

# Slide 15 — Costruite il primo pezzo
<!-- layout: CONTENUTO -->

## Un agente che calcola il fermo.

Scrivete voi le istruzioni e provatelo subito. Non serve completare l’agente prima di vedere se funziona.

Obiettivi, testi da usare e passaggi sono nella consegna.

---

# Slide 16 — Un messaggio dal reparto
<!-- layout: CONTENUTO -->

> «Quanto è durato il fermo del 14 ottobre? Mostrami gli orari.»

Date all’agente il registro e le regole degli indicatori.

Prima di inviare: quale risultato vi aspettate?

---

# Slide 17 — Gli orari devono tornare
<!-- layout: CONTENUTO -->

## {{MINUTI_FERMO}} minuti

{{ORA_FERMO}} → {{ORA_RIPARTENZA}}

Il fermo finisce quando riprende la produzione, non quando finiscono le prove.

Trovate le due note nel registro. Sono questi gli orari usati dal vostro agente?

---

# Slide 18 — Il responsabile insiste
<!-- layout: CONTENUTO -->

> «E quanti pezzi abbiamo perso?»

Continuate nella stessa conversazione.

Un numero, una domanda o un limite dichiarato: che cosa vi aspettate?

---

# Slide 19 — Qui serve un dato in più
<!-- layout: CONTENUTO -->

> La cadenza non è nel registro.

Per calcolare i pezzi teorici persi, l’agente deve chiederla.

Dire che manca è corretto. Scegliere un numero al posto vostro non lo è.

---

# Slide 20 — Dategli un secondo mestiere
<!-- layout: CONTENUTO -->

Spiegare un allarme dalla guida, oppure preparare una nota dal registro?

Scegliete voi. Aggiungete la competenza e l’indice delle richieste.

> Se una richiesta serve a due lavori, quale viene prima?

---

# Slide 21 — Come deve parlare il vostro agente?
<!-- layout: CONTENUTO -->

> Scrivete due esempi vostri di risposta, nello stile che volete.

Aggiungeteli alle istruzioni. La prova userà una richiesta diversa dagli esempi.

Le istruzioni restano nel vostro file istruzioni_assistente_P03.txt.

---

# Slide 22 — Servono tutte e due le competenze
<!-- layout: CONTENUTO -->

> Inventate una richiesta che obblighi l’agente a usare entrambi i lavori.

Decidete prima l’ordine e che cosa deve comparire nella risposta.

Poi provate, con i documenti necessari. La riga «Competenza usata» è una dichiarazione: conta la risposta.

---

# Slide 23 — Il vostro caso più scomodo
<!-- layout: CONTENUTO -->

Inventate una richiesta con un dato mancante, una fonte insufficiente o un lavoro fuori dall’indice.

> Deve rispondere, chiedere o fermarsi?

Decidetelo prima. Poi confrontate la risposta con i testi: nessun diario da compilare.

---

# Slide 24 — Ultimo messaggio dal reparto
<!-- layout: CONTENUTO -->

> «Come si chiama il tecnico che ha cambiato il filtro?»

Nuova conversazione, con il registro.

---

# Slide 25 — Il registro non fa nomi
<!-- layout: CONTENUTO -->

> «Non è scritto» è una risposta utile.

Anche dichiarare che la richiesta è fuori dalle proprie competenze è accettabile. Inventare un nome no.

---

# Slide 26 — Quale regola tenete?
<!-- layout: CONTENUTO -->

Correggete dove serve e riprovate il caso.

Se funzionava già, trovate la regola che ha aiutato. Sapete inventare un’altra richiesta che la metta alla prova?

Poi confrontiamo le vostre istruzioni con un altro esempio.

---

# Slide 27 — Due risposte vere. Quale preferite?
<!-- layout: CONTENUTO -->

Stessa richiesta, stessi documenti: una nuova risposta del vostro agente e una di Copilot senza agente.

Conservate anche la prima risposta dell’agente.

> Tra le due risposte dell’agente, sceglietene una e difendetela con due motivi.

---

# Slide 28 — Avete scelto. Non avete addestrato.
<!-- layout: CONTENUTO -->

Le preferenze tra risposte possono diventare dati per un addestramento.

Qui avete cambiato il testo letto da Copilot, non i suoi pesi.

Se le risposte sono uguali, è un risultato valido: il confronto non permette di vedere i pesi del modello.

---

# Slide 29 — Se Copilot si ferma
<!-- layout: CONTENUTO -->

L’agente non è disponibile? Conversazione normale: prima le vostre istruzioni, poi documenti e richiesta. Non sono vere istruzioni di sistema.

Copilot non risponde? Applichiamo le vostre regole a una richiesta dal proiettore. È una prova a secco, non una risposta del modello.

---

# Slide 30 — Che cosa avete cambiato?
<!-- layout: CHIUSURA -->

In Playground cambiavano i pesi. In Copilot, che cosa avete modificato voi?

Quale richiesta ha messo davvero alla prova il vostro indice?
