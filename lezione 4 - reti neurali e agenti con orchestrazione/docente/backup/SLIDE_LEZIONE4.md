# Slide 01 — Un agente, più lavori
<!-- layout: COPERTINA -->

Reti neurali da esplorare. Un agente da costruire.

ITS MAKER · 12 novembre 2026 · Microsoft Copilot e giochi nel browser

---

# Slide 02 — La stessa richiesta, la stessa risposta?
<!-- layout: CONTENUTO -->

> Se chiedete due volte la stessa cosa all’AI, deve rispondere allo stesso modo?

---

# Slide 03 — Come continuereste questa frase?
<!-- layout: CONTENUTO -->

> «La visualizzazione dei dati permette agli utenti di…»

Transformer Explainer usa la frase inglese «Data visualization empowers users to».

---

# Slide 04 — Spostate la probabilità
<!-- layout: CONTENUTO -->

## Prima sopra il 90%. Poi sotto il 30%.

https://poloclub.github.io/transformer-explainer/

Portate la barra più lunga sui due bersagli, cambiando solo Temperature. Primo esempio, k = 5.

---

# Slide 05 — La parola più probabile non è l’unica
<!-- layout: CONTENUTO -->

> Alzando la temperatura, le probabilità si distribuiscono di più.

Una barra alta non garantisce quale parola uscirà. E non garantisce che una frase sia vera.

---

# Slide 06 — Quanti neuroni servono per circondare il cerchio?
<!-- layout: CONTENUTO -->

## 0 · 1 · 2 · 3 · 10

I punti blu stanno al centro, quelli arancioni attorno. Quanti neuroni servono per separarli? Alzata di mano.

---

# Slide 07 — Provate. Un neurone in più alla volta.
<!-- layout: CONTENUTO -->

## Test loss sotto 0,05

https://playground.tensorflow.org/

Partite da zero neuroni, poi uno, due, tre, quattro. Fermatevi a 1.500 giri (Epoch).

Test loss: l'errore sui punti di prova. Più è basso, meglio è.

---

# Slide 08 — Che cosa disegna ogni neurone?
<!-- layout: CONTENUTO -->

> Nel disegno di un neurone: una linea o un cerchio?

Passate il mouse su un neurone: il suo disegno compare in grande a destra.

Ogni linea ha un numero, il peso: lo vedete passando il mouse. Mentre la rete impara, le linee cambiano spessore e colore.

---

# Slide 09 — Continuare è sempre meglio?
<!-- layout: CONTENUTO -->

| Guardiamo i punti… | Il sito scrive… |
| --- | --- |
| usati per addestrare | Training loss |
| tenuti da parte per la prova | Test loss |

Aggiungiamo disturbo (Noise). Prima di proseguire, scommettete: miglioreranno entrambi?

---

# Slide 10 — Cinquanta flappy birds, una rete ciascuno
<!-- layout: CONTENUTO -->

> Nessuno corregge queste reti. Si tengono le migliori.

Ogni flappy bird ha una piccola rete che decide quando saltare. A ogni generazione restano le migliori, con piccole variazioni.

xviniette.github.io/FlappyLearning

---

# Slide 11 — Adesso cambiamo le istruzioni
<!-- layout: SEZIONE -->

Microsoft Copilot legge il testo che scrivete voi.
In Playground e in Flappy cambiavano i pesi. Qui cambiate il testo.

---

# Slide 12 — Che cosa costruite oggi
<!-- layout: CONTENUTO -->

> Un assistente per il noleggio di biciclette Ruota Libera.

Il titolare ne vuole uno solo: calcola da quanto tempo una bici è fuori servizio e fa anche un secondo lavoro.

## Esempio → fuori servizio → secondo lavoro → prove → confronto

---

# Slide 13 — Prima, un esempio già fatto: la pizzeria
<!-- layout: CONTENUTO -->

> «La pizza è arrivata fredda e dopo un'ora. Mi ridate anche i soldi?»

Un agente è un assistente di Copilot con istruzioni salvate. Il docente ne mostra uno per una pizzeria d’asporto. Non è il vostro noleggio.

Alzata di mano: prima la pizza fredda o prima i soldi?

---

# Slide 14 — Com'è fatto
<!-- layout: CONTENUTO -->

| Parte delle istruzioni | Nella pizzeria | Nel vostro noleggio |
| --- | --- | --- |
| Regole per tutte le richieste (valgono sempre) | pizza fredda: prima «Mi dispiace» | le scrivete voi |
| Indice delle richieste (dice quale lavoro usare) | pizza fredda: RECLAMO. Soldi indietro: RIMBORSO | FUORI SERVIZIO e il secondo lavoro |
| Competenze (un lavoro ciascuna, con dati e regole) | ORDINE, RECLAMO, RIMBORSO | FUORI SERVIZIO, poi GUASTI o PASSAGGIO |
| Stile delle risposte (come deve parlare) | frasi brevi, il dato prima | due esempi vostri |

Sono parti dello stesso testo, non programmi separati. Scegliere quali usare e in che ordine si chiama orchestrare.

---

# Slide 15 — Che cosa aprire
<!-- layout: CONTENUTO -->

| Programma | Che cosa ci fate |
| --- | --- |
| Teams | scaricate i tre testi del noleggio: registro, regole del noleggio, guida ai guasti |
| Blocco note | aprite i tre testi e scrivete le istruzioni, da salvare come istruzioni_agente_noleggio.txt |
| Microsoft Copilot | con l'account scolastico, salvate l'agente e lo provate |

I tre testi sono le fonti: non vanno copiati nelle istruzioni.

---

# Slide 16 — Il primo lavoro: il fuori servizio
<!-- layout: CONTENUTO -->

## Scrivete le regole comuni e il lavoro FUORI SERVIZIO.

FUORI SERVIZIO: quando si usa, quali dati servono, come calcola i minuti, che cosa risponde se un dato manca.

La prima riga della risposta dice «Competenza usata:» e il nome del lavoro.

Scrivete voi, non Copilot.

---

# Slide 17 — Dove si salvano le istruzioni
<!-- layout: CONTENUTO -->

> Il docente vi mostra dove incollare le istruzioni dell’agente.

Poi aprite una nuova conversazione con il vostro agente.

Se l’agente non c’è: in ogni nuova conversazione inviate prima le vostre istruzioni; poi, in un secondo messaggio, testi e richiesta.

---

# Slide 18 — Un messaggio dal negozio
<!-- layout: CONTENUTO -->

> «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»

In un solo messaggio: il registro, le regole del noleggio e, in fondo, questa richiesta.

Prima di inviare: quale risultato vi aspettate?

---

# Slide 19 — Gli orari devono tornare
<!-- layout: CONTENUTO -->

## {{MINUTI_FUORI_SERVIZIO}} minuti

{{ORA_FUORI_SERVIZIO}} → {{ORA_DISPONIBILE}}

Il fuori servizio finisce quando la bici torna in fila, non quando finiscono la riparazione e la prova.

Trovate le due note nel registro. Sono questi gli orari usati dal vostro agente? Se no, correggete le istruzioni e riprovate in una nuova conversazione.

---

# Slide 20 — Il titolare insiste
<!-- layout: CONTENUTO -->

> «E quanto dobbiamo rimborsare al cliente?»

Continuate nella stessa conversazione.

Un numero, una domanda o un limite dichiarato: che cosa vi aspettate?

---

# Slide 21 — Qui serve un dato in più
<!-- layout: CONTENUTO -->

> Nel registro non c’è il tipo di noleggio.

Il rimborso conta i minuti senza bici: dalla segnalazione al cambio, non il fuori servizio della bici.

Il cliente può aver noleggiato a ore o per la giornata, e la tariffa oraria cambia. Per calcolare il rimborso, l’agente deve chiederlo.

Dire che manca è corretto. Scegliere una tariffa al posto vostro non lo è.

---

# Slide 22 — Il secondo lavoro: scegliete voi
<!-- layout: CONTENUTO -->

| Lavoro | Che cosa fa | Fonte |
| --- | --- | --- |
| GUASTI | spiega un guasto: significato, primo controllo, chi interviene | guida ai guasti |
| PASSAGGIO | prepara una nota per il turno dopo: fatti, interventi, controlli da fare | registro |

Aggiungete al vostro file il lavoro che preferite.

---

# Slide 23 — L’indice: quale lavoro, in che ordine
<!-- layout: CONTENUTO -->

> Se una richiesta serve a due lavori, quale viene prima? E se non serve a nessuno?

Scrivete nel file l’indice delle richieste: quale richiesta va a quale lavoro. Poi decidete questi due casi.

---

# Slide 24 — Come deve parlare il vostro agente?
<!-- layout: CONTENUTO -->

> Scrivete due esempi vostri di risposta, nello stile che volete.

Aggiungeteli alle istruzioni. La prova userà una richiesta diversa dagli esempi.

Le istruzioni restano nel vostro file istruzioni_agente_noleggio.txt.

---

# Slide 25 — Un caso che usa tutti e due i lavori
<!-- layout: CONTENUTO -->

> Inventate una richiesta che obblighi l’agente a usare entrambi i lavori.

Decidete prima l’ordine e che cosa deve comparire nella risposta.

Poi provatela in una nuova conversazione, con i testi che servono. La riga «Competenza usata» è una dichiarazione del modello: conta la risposta.

---

# Slide 26 — Il vostro caso più scomodo
<!-- layout: CONTENUTO -->

Inventate una richiesta con un dato che manca, un testo che non basta o un lavoro che l’agente non ha.

> Deve rispondere, chiedere o dire che non può?

Decidetelo prima. Poi confrontate la risposta con i testi: nessun diario da compilare.

---

# Slide 27 — Ultimo messaggio dal negozio
<!-- layout: CONTENUTO -->

> «Come si chiama il meccanico che ha cambiato le pastiglie?»

Nuova conversazione, con il registro.

---

# Slide 28 — Il registro non fa nomi
<!-- layout: CONTENUTO -->

> «Non è scritto» è una risposta utile.

Anche dichiarare che la richiesta è fuori dalle proprie competenze è accettabile. Inventare un nome no.

---

# Slide 29 — Quale regola tenete?
<!-- layout: CONTENUTO -->

Correggete dove serve e riprovate il caso.

Se funzionava già, trovate la regola che ha aiutato. Sapete inventare un’altra richiesta che la metta alla prova?

Nell’esempio del docente: c’è una regola che a voi manca?

---

# Slide 30 — Due risposte vere. Quale preferite?
<!-- layout: CONTENUTO -->

Scegliete una richiesta già provata. Stessi documenti per tutte e tre le risposte.

| Risposta | Dove la prendete |
| --- | --- |
| la prima del vostro agente | la prova già fatta |
| Copilot senza agente | nuova conversazione, senza le vostre istruzioni |
| il vostro agente, di nuovo | nuova conversazione con l’agente |

> Tra le due risposte dell’agente, sceglietene una e difendetela con due motivi.

---

# Slide 31 — Avete scelto. Non avete addestrato.
<!-- layout: CONTENUTO -->

Le preferenze tra risposte possono diventare dati per un addestramento.

Qui avete cambiato il testo letto da Copilot, non i suoi pesi.

Se le risposte sono uguali, è un risultato valido: il confronto non permette di vedere i pesi del modello.

---

# Slide 32 — Che cosa avete cambiato?
<!-- layout: CHIUSURA -->

In Playground cambiavano i pesi. In Copilot, che cosa avete modificato voi?

Quale richiesta ha messo davvero alla prova il vostro indice?
