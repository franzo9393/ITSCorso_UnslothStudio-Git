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

# Slide 12 — Che cosa legge Copilot
<!-- layout: CONTENUTO -->

| Che cosa legge | Chi lo scrive | A che cosa serve |
| --- | --- | --- |
| Le istruzioni | voi | come deve comportarsi |
| I testi | sono già pronti | i fatti del noleggio |
| La richiesta | chi usa l’agente | che cosa vuole sapere |

Copilot legge le tre cose insieme e risponde. Un agente è un assistente con istruzioni salvate: Copilot le rilegge a ogni richiesta.

---

# Slide 13 — Che cosa costruite oggi
<!-- layout: CONTENUTO -->

> Un agente per il noleggio di biciclette Ruota Libera.

Il titolare lo vuole con due lavori: calcolare da quanto tempo una bici è fuori servizio, più un secondo lavoro a vostra scelta.

## Esempio → primo lavoro → secondo lavoro → prove → confronto

---

# Slide 14 — Prima un esempio: la pizzeria
<!-- layout: CONTENUTO -->

> «La pizza è arrivata fredda e dopo un'ora. Mi ridate anche i soldi?»

È il messaggio di un cliente a una pizzeria d’asporto. Il docente ha già scritto le istruzioni del suo agente.

Alzata di mano: l’agente deve rispondere prima alla pizza fredda o ai soldi?

---

# Slide 15 — Le istruzioni dell’agente della pizzeria
<!-- layout: CONTENUTO -->

| Parte | Che cosa c’è scritto (estratti) |
| --- | --- |
| Regole per tutti i casi | «Se la pizza è fredda, sbagliata o in ritardo, scrivi prima “Mi dispiace” e proponi di rifarla, […]» |
| Elenco delle richieste | «Pizza fredda o in ritardo, pizza sbagliata → RECLAMO. Soldi indietro, conto sbagliato → RIMBORSO.» |
| Un lavoro, per esempio RECLAMO | «[…] chiedi il numero dell’ordine e che cosa non va. […] pizza fredda o sbagliata: proponi di rifarla.» |
| Stile delle risposte | «Frasi brevi. Prima il dato, poi la spiegazione.» |

È solo testo. Copilot lo legge prima di ogni richiesta.

---

# Slide 16 — Il docente prova la richiesta
<!-- layout: CONTENUTO -->

> Quale riga delle istruzioni ha guidato la risposta?

Il docente invia all’agente il messaggio della pizza. Guardate la risposta.

La prima riga dice «Lavoro usato:». L’ha scritta il modello: controllate voi che la risposta faccia davvero quel lavoro.

---

# Slide 17 — Adesso tocca a voi: il noleggio
<!-- layout: CONTENUTO -->

| Parte | Pizzeria | Noleggio |
| --- | --- | --- |
| Regole per tutti i casi | «Mi dispiace» se la pizza è fredda | le scrivete voi |
| Elenco delle richieste | pizza fredda: RECLAMO | lo scrivete voi |
| I lavori | ORDINE, RECLAMO, RIMBORSO | FUORI SERVIZIO e un altro a scelta |
| Stile delle risposte | frasi brevi | due esempi vostri |

Stesse quattro parti. Il contenuto lo scrivete voi.

---

# Slide 18 — Che cosa aprire
<!-- layout: CONTENUTO -->

| Programma | Che cosa ci fate |
| --- | --- |
| Teams | scaricate i tre testi del noleggio: registro, regole del noleggio, guida ai guasti |
| Blocco note | aprite i tre testi e scrivete le istruzioni, da salvare come istruzioni_agente_noleggio.txt |
| Microsoft Copilot | con l'account scolastico, salvate l'agente e lo provate |

I tre testi contengono i fatti: non vanno copiati nelle istruzioni.

---

# Slide 19 — Gli appunti del banco: la bici 5
<!-- layout: CONTENUTO -->

Il registro è un quaderno: data, ora e che cosa è successo. Due appunti (estratti):

| Quando | Appunto |
| --- | --- |
| 07/11/2026 · 12:35 | La bici 5 viene tolta dal noleggio e portata nel retro. Il banco toglie la gomma e trova un chiodo nel copertone. |
| 07/11/2026 · 13:00 | La bici 5 torna in fila con le altre. […] |

Per quanti minuti è stata fuori servizio la bici 5?

---

# Slide 20 — Un esempio svolto: la bici 5
<!-- layout: CONTENUTO -->

Fuori servizio: da quando la bici è tolta dal noleggio a quando torna in fila.

| Inizio | Fine | Minuti |
| --- | --- | --- |
| 12:35 | 13:00 | 25 |

Lo stesso conto, per un’altra bici, lo farà il vostro agente.

---

# Slide 21 — Prima le regole che valgono sempre
<!-- layout: CONTENUTO -->

## Scrivete le regole per tutti i casi.

Nella pizzeria cominciano così: «Sei l’assistente della pizzeria d’asporto Da Gino. Rispondi in italiano, con frasi brevi. Usi solo le informazioni che trovi in queste istruzioni e nel messaggio del cliente.»

Voi: chi è l’agente e a chi risponde (al titolare e al banco), la lingua, i testi che può usare. Scrivete in Blocco note, nel file istruzioni_agente_noleggio.txt.

---

# Slide 22 — Il primo lavoro: FUORI SERVIZIO
<!-- layout: CONTENUTO -->

| Riga | Pizzeria, lavoro RECLAMO (in breve) | Voi, lavoro FUORI SERVIZIO |
| --- | --- | --- |
| Quando si usa | «la pizza è fredda, sbagliata o in ritardo» | Per quali richieste del titolare? |
| Dati che servono | «il numero dell’ordine e che cosa non va» | Quale bici? Quali orari? |
| Regole del lavoro | «pizza fredda o sbagliata: proponi di rifarla» | Da quando a quando contano i minuti? |
| Come risponde | «tre punti: che cosa hai capito, che cosa fare ora, chi se ne occupa» | Che cosa mostra? E se un dato manca? |

La prima riga della risposta dice «Lavoro usato:» e il nome. Scrivete voi, non Copilot.

---

# Slide 23 — Dove si salvano le istruzioni
<!-- layout: CONTENUTO -->

> Il docente vi mostra dove incollare le istruzioni dell’agente.

Poi aprite una nuova conversazione con il vostro agente.

Se l’agente non c’è: in ogni nuova conversazione inviate prima le vostre istruzioni; poi, in un secondo messaggio, testi e richiesta.

---

# Slide 24 — Il messaggio da inviare
<!-- layout: CONTENUTO -->

| Nel messaggio | Che cosa incollate |
| --- | --- |
| Prima | il registro |
| Poi | le regole del noleggio |
| In fondo | la richiesta del titolare |

Tutto in un solo messaggio, in una nuova conversazione con il vostro agente.

---

# Slide 25 — La prima richiesta del titolare
<!-- layout: CONTENUTO -->

> «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»

Prima di inviare: quale risultato vi aspettate?

---

# Slide 26 — Gli orari devono tornare
<!-- layout: CONTENUTO -->

## {{MINUTI_FUORI_SERVIZIO}} minuti

{{ORA_FUORI_SERVIZIO}} → {{ORA_DISPONIBILE}}

Il fuori servizio finisce quando la bici torna in fila, non quando finiscono la riparazione e la prova.

Trovate le due note nel registro. Sono questi gli orari usati dal vostro agente? Se no, correggete le istruzioni e riprovate in una nuova conversazione.

---

# Slide 27 — Il titolare insiste
<!-- layout: CONTENUTO -->

> «E quanto dobbiamo rimborsare al cliente?»

Continuate nella stessa conversazione.

Un numero, una domanda, oppure «non posso calcolarlo»: che cosa vi aspettate?

---

# Slide 28 — Quanto è rimasto senza bici il cliente
<!-- layout: CONTENUTO -->

## {{MINUTI_SENZA_BICI}} minuti

{{ORA_SEGNALAZIONE}} → {{ORA_CAMBIO}}

Alle {{ORA_SEGNALAZIONE}} il cliente della bici 12 torna al banco: è la segnalazione. Alle {{ORA_CAMBIO}} riceve un’altra bici: è il cambio.

Il rimborso conta questi minuti, non i {{MINUTI_FUORI_SERVIZIO}} di fuori servizio della bici.

---

# Slide 29 — Qui serve un dato in più
<!-- layout: CONTENUTO -->

> Nel registro non c’è il tipo di noleggio.

Il cliente può aver noleggiato a ore o per la giornata, e la tariffa oraria cambia. Per calcolare il rimborso, l’agente deve chiederlo.

Dire che manca è corretto. Scegliere una tariffa al posto vostro non lo è.

---

# Slide 30 — Il secondo lavoro: scegliete voi
<!-- layout: CONTENUTO -->

| Lavoro | Che cosa fa | Testo da usare |
| --- | --- | --- |
| GUASTI | spiega un guasto: significato, primo controllo, chi interviene | guida ai guasti |
| PASSAGGIO | prepara una nota per il turno dopo: fatti, interventi, controlli da fare | registro |

Scrivetelo con le stesse quattro righe: quando si usa, dati che servono, regole del lavoro, come risponde.

---

# Slide 31 — L’elenco delle richieste
<!-- layout: CONTENUTO -->

| Se il cliente della pizzeria… | L’agente usa… |
| --- | --- |
| dice che la pizza è fredda | RECLAMO |
| chiede soldi indietro | RIMBORSO |
| chiede le due cose insieme | prima RECLAMO, poi RIMBORSO |
| chiede altro | risponde «Per questo serve il banco» |

Scrivete l’elenco del noleggio. Due lavori insieme: quale viene prima? E se la richiesta non serve a nessuno?

---

# Slide 32 — Come deve parlare il vostro agente?
<!-- layout: CONTENUTO -->

> Scrivete due esempi vostri di risposta, nello stile che volete.

Nella pizzeria: «Lavoro usato: ORDINE. Due Margherite e una Diavola alle 20:00: 20 euro. Confermi?»

Aggiungeteli alle istruzioni. La prova userà una richiesta diversa dagli esempi.

---

# Slide 33 — Una richiesta che usa tutti e due i lavori
<!-- layout: CONTENUTO -->

> Inventate una richiesta che obblighi l’agente a usare entrambi i lavori.

Come nella pizzeria: «pizza fredda e soldi indietro». Decidete prima l’ordine e che cosa deve comparire nella risposta.

Poi provatela in una nuova conversazione, con i testi che servono: registro e regole; con GUASTI anche la guida ai guasti. La riga «Lavoro usato» è una dichiarazione del modello: conta la risposta.

---

# Slide 34 — Il vostro caso più scomodo
<!-- layout: CONTENUTO -->

| Tipo di richiesta | Nella pizzeria |
| --- | --- |
| un dato che manca | «Vorrei due pizze per stasera.» (quali? a che ora?) |
| un testo che non basta | «Quanto costa una birra?» (il listino non la dice) |
| un lavoro che l’agente non ha | «Mi prenoti un tavolo per sabato?» |

Inventatene una per il noleggio. Decidete prima: deve rispondere, chiedere o dire che non può? Poi confrontate la risposta con i testi.

---

# Slide 35 — Ultima richiesta dal negozio
<!-- layout: CONTENUTO -->

> «Come si chiama il meccanico che ha cambiato le pastiglie?»

Nuova conversazione, con il registro.

---

# Slide 36 — Il registro non fa nomi
<!-- layout: CONTENUTO -->

> «Non è scritto» è una risposta utile.

Anche dire che la richiesta non è un suo lavoro è accettabile. Inventare un nome no.

---

# Slide 37 — Correggete e riprovate
<!-- layout: CONTENUTO -->

Se una risposta non rispetta i testi: correggete il file, aggiornate l’agente e riprovate in una nuova conversazione.

Una prova riuscita dopo una correzione vale quanto una riuscita al primo invio.

Se funzionava già: trovate la regola che ha aiutato e inventate un’altra richiesta per metterla alla prova.

---

# Slide 38 — L’esempio del docente
<!-- layout: CONTENUTO -->

Il docente proietta le istruzioni di esempio per il noleggio.

> Avete una regola che fa la stessa cosa?

Guardate: due lavori insieme, dati che mancano, richieste che non sono un lavoro dell’agente. Se vi manca, scrivetela con parole vostre.

---

# Slide 39 — Tre risposte. Quale preferite?
<!-- layout: CONTENUTO -->

Scegliete una richiesta già provata. Stessi documenti per tutte e tre le risposte.

| Risposta | Dove la prendete |
| --- | --- |
| la prima del vostro agente | la prova già fatta |
| Copilot senza agente | nuova conversazione, senza le vostre istruzioni |
| il vostro agente, di nuovo | nuova conversazione con l’agente |

> Tra le due risposte dell’agente, sceglietene una e difendetela con due motivi.

---

# Slide 40 — Avete scelto. Non avete addestrato.
<!-- layout: CONTENUTO -->

Le preferenze tra risposte possono diventare dati per un addestramento.

Qui avete cambiato il testo letto da Copilot, non i suoi pesi.

Se le risposte sono uguali, è un risultato valido: il confronto non permette di vedere i pesi del modello.

---

# Slide 41 — Che cosa avete cambiato?
<!-- layout: CHIUSURA -->

In Playground cambiavano i pesi. In Copilot, che cosa avete modificato voi?

Quale richiesta ha messo davvero alla prova il vostro elenco?
