# Slide 01 — Chi decide quale lavoro?
<!-- layout: COPERTINA -->

Un agente che fa il piano, chiede e controlla.

ITS MAKER · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode

---

# Slide 02 — Riaprite il vostro agente
<!-- layout: CONTENUTO -->

| Dove | Che cosa fate |
| --- | --- |
| Microsoft Copilot | aprite il vostro agente del noleggio, in una nuova conversazione |
| Messaggio | registro, regole del noleggio, e in fondo la richiesta |

> «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»

Non avete il file `istruzioni_agente_noleggio.txt`? Alzate la mano: il docente vi dà un punto di partenza.

---

# Slide 03 — Il percorso di oggi
<!-- layout: CONTENUTO -->

| Passo | Dove | Che cosa succede |
| --- | --- | --- |
| 1 | Copilot | al vostro testo aggiungete il piano, il rimborso e il controllo |
| 2 | il computer virtuale del gruppo | lo stesso testo, letto da un altro modello |
| 3 | opencode, sullo stesso computer | un programma apre i file e chiede il permesso; il modello decide che cosa chiedere |

Il testo che scrivete resta quello del noleggio. Cambia chi lo legge e chi lo esegue. Il passo 1 è sul vostro computer; i passi 2 e 3 sono in gruppo, quattro o cinque persone per ogni computer virtuale: un computer dentro il computer, con il suo Windows e i suoi programmi.

---

# Slide 04 — Due lavori insieme: piano o risposta?
<!-- layout: CONTENUTO -->

> Chiedete due cose insieme all’agente. Volete vedere subito la risposta, o prima il piano?

Alzata di mano.

Nell’agente della lezione 4 Copilot segue l’elenco e risponde subito. Se sbaglia, lo scoprite dopo.

---

# Slide 05 — Il piano prima della risposta
<!-- layout: CONTENUTO -->

Una regola nelle istruzioni della pizzeria (estratto):

> «Se la richiesta ha due o più lavori, scrivi prima "Piano:" con i lavori nell’ordine in cui li usi e i dati che mancano. Poi fermati e aspetta la parola "Procedi".»

Il docente prova: «La pizza è arrivata fredda e voglio i soldi indietro.»

Prima di vedere la risposta, per alzata di mano: l’agente si ferma dopo il piano?

---

# Slide 06 — Il piano si può correggere
<!-- layout: CONTENUTO -->

Il docente risponde al piano: «Procedi, ma solo il reclamo.»

Che cosa deve fare adesso l’agente? Che cosa deve non fare?

---

# Slide 07 — Scrivete la regola del piano
<!-- layout: CONTENUTO -->

| Domanda | Pizzeria | Noleggio: voi |
| --- | --- | --- |
| Quando scatta? | «due o più lavori» | per quali richieste? |
| Che cosa contiene? | lavori in ordine, dati che mancano | e i testi che userà? |
| Dove si ferma? | dopo il piano | qual è il segno? |
| Che parola lo fa ripartire? | «Procedi» | la scegliete voi |
| E «Lavoro usato:»? | dopo il piano | prima o dopo il piano? |

Aggiungete la regola alle **regole per tutti i casi**, nel file `istruzioni_agente_noleggio.txt`. Poi aggiornate l’agente in Copilot.

---

# Slide 08 — Provate: due lavori insieme
<!-- layout: CONTENUTO -->

Una nuova conversazione. Registro, regole del noleggio e in fondo la richiesta. Con GUASTI aggiungete anche la guida ai guasti. Con il punto di partenza di una persona che non aveva il file, scegliete una delle due righe.

| Il vostro secondo lavoro | Richiesta |
| --- | --- |
| GUASTI | «Bici 12, sabato: quanto è stata fuori servizio, e che cosa significa freni che non tengono?» |
| PASSAGGIO | «Bici 12, sabato: quanto è stata fuori servizio? Scrivi la nota per il turno dopo.» |

Prima di inviare: che piano vi aspettate?

---

# Slide 09 — Il piano era giusto?
<!-- layout: CONTENUTO -->

| Controllate | Sì / No |
| --- | --- |
| il piano viene prima di qualsiasi risposta ai lavori | |
| i due lavori sono nell’ordine che avevate deciso | |
| dice quali testi userà | |
| si ferma e aspetta | |
| dopo «Procedi» risponde | |

Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.

---

# Slide 10 — Il rimborso è un lavoro a sé
<!-- layout: CONTENUTO -->

Nella lezione 4 il titolare ha chiesto, dopo il fuori servizio: «E quanto dobbiamo rimborsare al cliente?»

Il rimborso conta altri minuti: quelli del cliente senza bici, dalla segnalazione al cambio. E ha bisogno di un dato che il registro non ha: il tipo di noleggio.

Quando una richiesta cresce, le si dà un lavoro a sé.

---

# Slide 11 — Il lavoro RIMBORSO
<!-- layout: CONTENUTO -->

| Riga | Pizzeria, lavoro RIMBORSO (in breve) | Voi, lavoro RIMBORSO |
| --- | --- | --- |
| Quando si usa | «il cliente chiede soldi indietro» | per quali richieste? |
| Dati che servono | «numero dell’ordine, importo pagato, motivo» | quali minuti? quale tariffa? |
| Regole del lavoro | «pizza non arrivata: proposta di rimborso intero» | da quando a quando contano i minuti? |
| Come risponde | «PROPOSTA DA CONTROLLARE, l’importo e il calcolo» | che cosa mostra? E se manca un dato? |

Il banco decide: l’agente propone.

---

# Slide 12 — Il rimborso, un lavoro a parte
<!-- layout: CONTENUTO -->

1. Se nel vostro FUORI SERVIZIO c’è il rimborso, toglietelo. Se non c’è, scrivete RIMBORSO da zero.
2. Scrivete il lavoro RIMBORSO con le quattro righe.
3. Aggiornate l’elenco delle richieste.

Nell’elenco: FUORI SERVIZIO e RIMBORSO insieme, quale va prima? Quali orari usa ciascuno dei due?

---

# Slide 13 — Ogni numero, la sua riga
<!-- layout: CONTENUTO -->

Una regola nelle istruzioni della pizzeria (estratto):

> «In fondo alla risposta scrivi "Controllo:" e, per ogni numero della risposta, la riga delle istruzioni da cui viene. Se non la trovi, scrivi "Non trovato".»

Il docente prova: «Quanto costa una Diavola con la consegna?»

Dove cercate la riga, per controllare il controllo?

---

# Slide 14 — Scrivete la regola del controllo
<!-- layout: CONTENUTO -->

| Domanda | Pizzeria | Noleggio: voi |
| --- | --- | --- |
| Che cosa controlla? | «ogni numero della risposta» | solo i numeri, o anche gli orari? |
| Che cosa scrive? | «la riga delle istruzioni» | quale testo? con quale data e ora? |
| E se non trova la riga? | «Non trovato» | che cosa fa? |

Aggiungete la regola alle regole per tutti i casi.

---

# Slide 15 — Tre lavori in una richiesta
<!-- layout: CONTENUTO -->

| Il vostro secondo lavoro | Richiesta |
| --- | --- |
| GUASTI | «Bici 12, sabato: quanto è stata fuori servizio, che cosa significa freni che non tengono, quanto rimborsiamo al cliente?» |
| PASSAGGIO | «Bici 12, sabato: quanto è stata fuori servizio, quanto rimborsiamo al cliente? Prepara la nota per il turno dopo.» |

Una sola prova per le due regole nuove. Aggiornate l’agente. Poi una nuova conversazione, i testi che servono, la richiesta in fondo. Prima di inviare: che dato vi aspettate che chieda?

Quando lo chiede, rispondete: «A ore. Procedi.» Se chiede anche il turno: «La nota è per chi inizia il pomeriggio di sabato.»

---

# Slide 16 — Gli orari devono tornare
<!-- layout: CONTENUTO -->

## {{MINUTI_SENZA_BICI}} minuti senza bici

{{ORA_SEGNALAZIONE}} → {{ORA_CAMBIO}}

| Tipo di noleggio | Rimborso proposto |
| --- | --- |
| a ore | {{RIMBORSO_A_ORE}} euro |
| giornata intera | {{RIMBORSO_GIORNATA}} euro |

Il rimborso non usa i {{MINUTI_FUORI_SERVIZIO}} minuti di fuori servizio della bici. Se avete detto «a ore», il numero giusto è il primo.

---

# Slide 17 — Controllate il controllo
<!-- layout: CONTENUTO -->

Nella risposta alla richiesta a tre lavori scegliete un numero e cercate nel testo la riga che l’agente cita.

> La riga esiste davvero? Dice quello che l’agente dice?

Un controllo che cita una riga inventata è peggio di nessun controllo.

---

# Slide 18 — Una richiesta vostra
<!-- layout: CONTENUTO -->

Inventate una richiesta per il noleggio.

| Tipo di richiesta | Nella pizzeria |
| --- | --- |
| un dato che manca | «Vorrei due pizze per stasera.» (quali? a che ora?) |
| un testo che non basta | «Quanto costa una birra?» (il listino non la dice) |
| un lavoro che l’agente non ha | «Mi prenoti un tavolo per sabato?» |

Scegliete un tipo. Decidete prima la risposta corretta. Poi provate, in una nuova conversazione. Se funziona subito, cercate la regola che lo ha reso possibile. Se funziona subito, cercate la regola che lo ha reso possibile.

---

# Slide 19 — Salvate il file
<!-- layout: CONTENUTO -->

Il file `istruzioni_agente_noleggio.txt` deve contenere tutto: regole per tutti i casi con piano e controllo, i tre o quattro lavori, l’elenco delle richieste, lo stile.

Aggiornate l’agente in Copilot e controllate che il testo sia arrivato intero.

Serve tra poco: lo incollerete in un altro programma.

---

# Slide 20 — Chi ha fatto che cosa?
<!-- layout: CONTENUTO -->

> Scegliere i lavori, decidere l’ordine, fermarsi a chiedere, controllare. Questo lavoro ha un nome: coordinare.

Il vostro agente ha un coordinatore. Dove sta?

---

# Slide 21 — Lo stesso testo, un altro modello
<!-- layout: SEZIONE -->

Computer virtuale, Unsloth Studio

---

# Slide 22 — Quello che avete davanti
<!-- layout: CONTENUTO -->

| | Copilot | il modello del computer virtuale |
| --- | --- | --- |
| Dove gira | in rete, sui computer di Microsoft | sul computer del gruppo |
| Internet | serve | non serve |
| Dimensione | non la conosciamo | un file di circa 1,3 GB |
| Chi lo cambia | Microsoft | nessuno |

Unsloth Studio è il programma che lo carica e vi lascia parlarci. Il computer virtuale è un computer dentro il computer, con il suo Windows e i suoi programmi: uno ogni quattro o cinque persone.

---

# Slide 23 — Quale file porta il gruppo?
<!-- layout: CONTENUTO -->

Una sola richiesta, un solo file di istruzioni. Il modello è lento: non c’è posto per una prova a testa.

Ognuno dice com’è andata la richiesta a tre lavori nella parte 1: il piano, l’ordine, la domanda sul tipo di noleggio, i numeri, il controllo.

> Quale file ha tenuto meglio? Decidete voi, e dite perché.

---

# Slide 24 — Aprite Studio e guardate il pannello
<!-- layout: CONTENUTO -->

> Il docente vi mostra come aprire Studio e caricare il modello.

Nel pannello cercate due voci: **Context Length**, la quantità di testo che il modello riesce a tenere insieme, e **Temperature**.

Temperature è la manopola che avete mosso in Transformer Explainer. Non toccatela adesso.

---

# Slide 25 — Il file del gruppo nel System Prompt
<!-- layout: CONTENUTO -->

| Chi | Che cosa fa |
| --- | --- |
| l’autore del file | lo porta sul computer del gruppo, come il docente indica |
| lo stesso | incolla tutto il testo nel campo System Prompt |
| un altro del gruppo | in una nuova conversazione scrive un solo messaggio: registro, regole del noleggio e in fondo la richiesta a tre lavori; con GUASTI anche la guida ai guasti |

I tre testi sono già nella cartella `noleggio` del computer virtuale. Le istruzioni nel campo System Prompt sono vere istruzioni di sistema: il modello le legge come istruzioni, non come messaggio.

---

# Slide 26 — Prima di inviare
<!-- layout: CONTENUTO -->

> Questo modello è molto più piccolo di Copilot. Farà il piano e si fermerà?

Ognuno scrive una riga su un foglio: sì, no o in parte. Poi alzata di mano per gruppo.

Il modello è lento. Mentre aspettate, rileggete la regola del piano: è scritta in modo che un modello piccolo la capisca?

---

# Slide 27 — Che cosa è successo?
<!-- layout: CONTENUTO -->

| Guardate | Che cosa avete visto |
| --- | --- |
| il piano prima di tutto | |
| i lavori nell’ordine scelto | |
| la domanda sul tipo di noleggio, a cui il gruppo risponde «A ore. Procedi.» | |
| il numero dei minuti | |
| il controllo con la riga | |

Raccontate alla classe una cosa che ha fatto come Copilot e una che ha fatto in modo diverso.

---

# Slide 28 — Se non ci arriva
<!-- layout: CONTENUTO -->

Non è un errore dell’autore. Un modello piccolo può non seguire un testo lungo.

Il gruppo sceglie **una** modifica: accorciare una regola, riscrivere una frase più semplice o togliere un esempio. L’autore la fa. Si riprova una volta.

Se il testo non entra, guardate **Context Length**: è la quantità di testo che il modello riesce a tenere insieme.

---

# Slide 29 — Un solo lavoro, un solo testo
<!-- layout: CONTENUTO -->

> Per rispondere a una richiesta sul fuori servizio servono tutti e tre i documenti?

Pensateci nel gruppo. Poi il docente risponde.

---

# Slide 30 — Il programma che coordina
<!-- layout: SEZIONE -->

opencode: un programma può dare a ogni lavoro soltanto il suo testo

---

# Slide 31 — Il programma legge il file
<!-- layout: CONTENUTO -->

Da qui un passo alla volta, con una persona diversa ai comandi. Chi non è ai comandi scrive la previsione su un foglio, prima del risultato.

Ai comandi: una persona che non ha scritto il file del gruppo. Aprite la cartella `noleggio` del computer virtuale e avviate opencode, come il docente mostra.

> «Quale codice hanno le pastiglie montate sulla bici 12?»

Prima di inviare, tutti scrivono: chi leggerà il registro, il modello o il programma?

---

# Slide 32 — Il modello chiede, il programma fa
<!-- layout: CONTENUTO -->

Guardate l’elenco dei passaggi.

Il modello scrive una richiesta di lettura. Il programma apre il file. Il testo torna al modello. Solo dopo c’è la risposta.

Il modello non ha aperto niente.

---

# Slide 33 — Piano o esecuzione
<!-- layout: CONTENUTO -->

opencode ha due modalità: **Plan** guarda e propone, **Build** esegue. Il docente mostra come passare dall’una all’altra. Ai comandi, un’altra persona.

> «Scrivi la nota per il turno dopo nel file nota_passaggio.txt.»

Prima in Plan, poi in Build. Prima di provare, tutti scrivono su un foglio: in quale dei due il file comparirà?

---

# Slide 34 — Il programma chiede il permesso
<!-- layout: CONTENUTO -->

| Permesso | Che cosa fa il programma |
| --- | --- |
| allow | esegue |
| ask | si ferma e chiede a voi |
| deny | non esegue |

Il docente dice a ogni gruppo se approvare o rifiutare la scrittura. Poi si confrontano dal proiettore le cartelle dei gruppi: in quali c’è il file? Che differenza c’è dal «PROPOSTA DA CONTROLLARE» del vostro file?

---

# Slide 35 — Dov’è il coordinatore, adesso?
<!-- layout: CONTENUTO -->

| Nel vostro file | In Copilot e in Studio | In opencode |
| --- | --- | --- |
| I testi del noleggio | incollati nel messaggio | il programma li apre quando il modello lo chiede |
| Il piano prima di rispondere | una regola scritta nel testo | modalità Plan: il programma non scrive niente |
| «PROPOSTA DA CONTROLLARE» | parole nel testo | il programma si ferma e chiede il permesso |

Non lo abbiamo provato oggi: in opencode ogni lavoro può diventare un agente a parte, con i suoi permessi.

---

# Slide 36 — Che cosa avete costruito
<!-- layout: CHIUSURA -->

Il coordinatore era un testo. Con opencode è un programma che chiede, esegue e riporta.

Quale permesso dareste al vostro agente, e perché?
