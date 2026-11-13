# Lezione 5 · Un agente che fa il piano

**ITS MAKER Bologna · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

## Da dove partiamo

Il titolare di Ruota Libera ha provato il vostro agente e chiede tre cose:

> «Quando ti chiedo due cose insieme, voglio vedere il piano prima della risposta. Il rimborso deve essere un lavoro a parte. E accanto a ogni numero voglio sapere da quale riga viene.»

Nella parte 1 ognuno lavora sul proprio computer, partendo dal file della lezione 4: `istruzioni_agente_noleggio.txt`. Non avete il file? Ve ne diamo uno di partenza. Non ci sono file da consegnare: il risultato si guarda sullo schermo. Salvate solo il file delle istruzioni, aggiornato.

Il percorso è questo:

| Passo | Dove | Che cosa succede |
| --- | --- | --- |
| 1 | Microsoft Copilot | al vostro testo aggiungete il piano, il rimborso e il controllo |
| 2 | il computer virtuale del gruppo, Unsloth Studio | lo stesso testo, letto da un altro modello |
| 3 | opencode, sullo stesso computer | lo stesso testo, con un programma accanto al modello |

## Riaprite il vostro agente

1. Aprite Blocco note e il file `istruzioni_agente_noleggio.txt`.
2. Aprite Microsoft Copilot, con l'account scolastico, e il vostro agente. Se non c'è, usate una conversazione normale: nel primo messaggio incollate le istruzioni.
3. Scaricate da Teams i tre testi del noleggio: registro, regole del noleggio e guida ai guasti.
4. In una nuova conversazione scrivete un solo messaggio: registro, regole del noleggio e in fondo la richiesta: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»
5. Controllate gli orari con il registro.

## Parte 1 · Tre cose nuove per il vostro agente

### 1A · Il piano prima della risposta

Il titolare vuole vedere che cosa farà l'agente prima che lo faccia. Un **piano** è l'elenco dei lavori, nell'ordine in cui l'agente li userà, con i dati che mancano. Dopo il piano l'agente si ferma e aspetta.

La regola di una pizzeria d'asporto, proiettata:

> «Se la richiesta ha due o più lavori, scrivi prima "Piano:" con i lavori nell'ordine in cui li usi e i dati che mancano. Poi fermati e aspetta la parola "Procedi".»

La richiesta alla pizzeria: «La pizza è arrivata fredda e voglio i soldi indietro.» Per alzata di mano: dopo il piano, l'agente si ferma? Poi si risponde al piano: «Procedi, ma solo il reclamo.» Che cosa deve fare adesso? Che cosa non deve fare?

Ora scrivete la regola del piano per il noleggio, nelle **regole per tutti i casi**. A destra le domande a cui rispondete voi:

| Domanda | Pizzeria | Noleggio |
| --- | --- | --- |
| Quando scatta? | «due o più lavori» | Per quali richieste? |
| Che cosa contiene? | lavori in ordine, dati che mancano | E i testi che userà? |
| Dove si ferma? | dopo il piano | Qual è il segno? |
| Che parola lo fa ripartire? | «Procedi» | La scegliete voi |
| E «Lavoro usato:»? | Dopo il piano | Il piano viene prima: correggete la regola della prima riga. |

Salvate il file e aggiornate l'agente. Poi, in una nuova conversazione, registro, regole del noleggio e in fondo la richiesta che corrisponde al vostro secondo lavoro. Siete partiti dalle istruzioni di partenza? Scegliete voi GUASTI o PASSAGGIO.

| Il vostro secondo lavoro | Richiesta |
| --- | --- |
| GUASTI (aggiungete anche la guida ai guasti) | «Bici 12, sabato: quanto è stata fuori servizio, e che cosa significa freni che non tengono?» |
| PASSAGGIO | «Bici 12, sabato: quanto è stata fuori servizio? Scrivi la nota per il turno dopo.» |

Prima di inviare, decidete che piano vi aspettate. Poi controllate: il piano viene prima di qualsiasi risposta ai lavori? I lavori sono nell'ordine che avevate deciso? Dice quali testi usa? Si ferma? Dopo «Procedi» risponde?

Una prova riuscita al primo invio vale quanto una riuscita dopo una correzione.

### 1B · Il rimborso diventa un lavoro

Dopo il fuori servizio il titolare chiede anche il rimborso. Il rimborso conta altri minuti: quelli del cliente senza bici, dalla segnalazione al cambio. E ha bisogno di un dato che nel registro non c'è, il tipo di noleggio. Quando una richiesta cresce, le si dà un lavoro a sé.

Qui sotto, a sinistra, il lavoro RIMBORSO della pizzeria; a destra le domande a cui rispondete voi:

| Riga | Pizzeria, lavoro RIMBORSO (in breve) | Noleggio |
| --- | --- | --- |
| Quando si usa | «il cliente chiede soldi indietro» | Per quali richieste? |
| Dati che servono | «numero dell'ordine, importo pagato, motivo» | Quali minuti? Quale tariffa? |
| Regole del lavoro | «pizza non arrivata: proposta di rimborso intero» | Da quando a quando contano i minuti? |
| Come risponde | «PROPOSTA DA CONTROLLARE, l'importo e il calcolo» | Che cosa mostra? E se manca un dato? |

1. Se nel vostro FUORI SERVIZIO c'è il rimborso, toglietelo. Se non c'è, scrivete RIMBORSO da zero.
2. Scrivete il lavoro RIMBORSO con le quattro righe. Il banco decide: l'agente propone.
3. Aggiornate l'**elenco delle richieste**. Quando una richiesta ha FUORI SERVIZIO e RIMBORSO insieme: quale va prima? Quali orari usa ciascuno dei due?

### 1C · Ogni numero, la sua riga, e una prova sola

Il titolare vuole sapere da dove viene ogni numero. La regola della pizzeria, proiettata:

> «In fondo alla risposta scrivi "Controllo:" e, per ogni numero della risposta, la riga delle istruzioni da cui viene. Se non la trovi, scrivi "Non trovato".»

La richiesta alla pizzeria: «Quanto costa una Diavola con la consegna?» Dove cercate la riga che il controllo cita? Poi, dal proiettore, le istruzioni della pizzeria.

Scrivete la regola per il noleggio:

| Domanda | Pizzeria | Noleggio |
| --- | --- | --- |
| Che cosa controlla? | «ogni numero della risposta» | Solo i numeri, o anche gli orari? |
| Che cosa scrive? | «la riga delle istruzioni» | Quale testo? Con quale data e ora? |
| E se non trova la riga? | «Non trovato» | Che cosa fa? |

Poi una sola prova per le due regole nuove: aggiornate l'agente, aprite una nuova conversazione, con i testi che servono. In fondo la richiesta con tre lavori:

| Il vostro secondo lavoro | Richiesta |
| --- | --- |
| GUASTI | «Bici 12, sabato: quanto è stata fuori servizio, che cosa significa freni che non tengono, quanto rimborsiamo al cliente?» |
| PASSAGGIO | «Bici 12, sabato: quanto è stata fuori servizio, quanto rimborsiamo al cliente? Prepara la nota per il turno dopo.» |

Prima di inviare: che dato vi aspettate che chieda?

Dopo l'invio, se l'agente chiede il tipo di noleggio, rispondete: «A ore. Procedi.» Se chiede anche il turno: «La nota è per chi inizia il pomeriggio di sabato.» Poi controllate i numeri proiettati: minuti senza bici, rimborso a ore e a giornata. Il rimborso deve usare i minuti del cliente senza bici, non quelli di fuori servizio della bici.

Poi scegliete un numero della risposta e cercate nel registro o nelle regole del noleggio la riga che l'agente cita: esiste davvero? Dice quello che l'agente dice? Un controllo con una riga inventata è peggio di nessun controllo.

### 1D · Una richiesta vostra

Inventate una richiesta per il noleggio, di uno di questi tipi:

| Tipo di richiesta | Nella pizzeria |
| --- | --- |
| un dato che manca | «Vorrei due pizze per stasera.» (quali? a che ora?) |
| un testo che non basta | «Quanto costa una birra?» (il listino non la dice) |
| un lavoro che l'agente non ha | «Mi prenoti un tavolo per sabato?» |

Scrivete su un foglio la risposta corretta. Provate la richiesta in una nuova conversazione. Se funziona subito, cercate la regola che lo ha reso possibile. Se qualcosa non va, correggete il punto necessario nel file e riprovate. Non peggiorate le istruzioni per provocare un errore.

Prima di passare alla parte 2 il file `istruzioni_agente_noleggio.txt` deve essere completo: regole per tutti i casi con piano e controllo, i lavori, l'elenco delle richieste, lo stile. Controllate che il testo in Copilot sia arrivato intero.

### Chi ha fatto che cosa

Scegliere i lavori, decidere l'ordine, fermarsi a chiedere, controllare: questo lavoro si chiama **coordinare**. Il vostro agente ha un coordinatore. Dove sta?

## Parte 2 · Lo stesso testo, un altro modello

Da qui lavorate in gruppo, quattro o cinque persone per ogni computer virtuale: un computer dentro il computer, con il suo Windows e i suoi programmi. Il modello è lento e risponde a una richiesta alla volta: il gruppo fa **una** prova. Unsloth Studio è il programma che carica il modello e vi lascia parlarci.

| | Copilot | il modello del computer virtuale |
| --- | --- | --- |
| Dove gira | in rete, sui computer di Microsoft | sul computer del gruppo |
| Internet | serve | non serve |
| Dimensione | non la conosciamo | un file di circa 1,3 GB |
| Chi lo cambia | Microsoft | nessuno |

1. **Scegliete il file.** Ognuno dice com'è andata la richiesta a tre lavori nella parte 1: il piano, l'ordine, la domanda sul tipo di noleggio, i numeri, il controllo. Il gruppo sceglie il file che ha tenuto meglio e dice perché.
2. Unsloth Studio è già aperto, con il modello caricato. Nel pannello trovate **Context Length** (la quantità di testo che il modello riesce a tenere insieme): che numero c'è? E **Temperature**, la manopola di Transformer Explainer. Non toccatela adesso.
3. L'autore del file lo copia su una chiavetta e lo porta al computer del gruppo. Lo apre e incolla tutto il testo nel campo **System Prompt**. Sono vere istruzioni di sistema: il modello le legge come istruzioni, non come messaggio.
4. Un altro del gruppo apre una nuova conversazione e scrive un solo messaggio: registro, regole del noleggio e in fondo la richiesta con tre lavori del file scelto; con GUASTI anche la guida ai guasti. Aprite con Blocco note i tre testi nella cartella `noleggio` del computer virtuale e copiateli nel messaggio.
5. Prima di inviare, ognuno scrive una riga su un foglio: farà il piano e si fermerà? Sì, no o in parte. Il modello è lento. Mentre aspettate, rileggete la regola del piano: è scritta in modo che un modello piccolo la capisca?
6. Guardate la risposta. Ha scritto il piano prima di tutto? Ha rispettato l'ordine? Ha chiesto il tipo di noleggio? Quando lo chiede, rispondete: «A ore. Procedi.» Se chiede anche il turno, date la stessa risposta della parte 1. Quanti minuti ha trovato? Ogni numero ha la sua riga?
7. Se non ci arriva, non è un errore dell'autore: un modello piccolo può non seguire un testo lungo. Il gruppo sceglie **una** modifica, per esempio accorciare una regola. L'autore la fa e si riprova una volta. Se il testo non entra, alleggerite il messaggio: **Context Length** dice quanto testo entra.

Ogni gruppo dice una sola cosa che il modello ha fatto in modo diverso da Copilot.

Per rispondere a una richiesta sul fuori servizio servono tutti e tre i documenti? Pensateci nel gruppo.

## Parte 3 · opencode, il programma che coordina

Un passo alla volta, con una persona diversa ai comandi del computer del gruppo. Chi non è ai comandi scrive la previsione su un foglio prima di vedere il risultato.

### 3A · Il programma legge il file

Ai comandi, una persona che non ha scritto il file del gruppo. Sul desktop del computer virtuale c'è il collegamento opencode: fate doppio clic, parte nella cartella `noleggio`. Scrivete: «Quale codice hanno le pastiglie montate sulla bici 12?»

Prima di inviare, tutti scrivono: chi leggerà il registro, il modello o il programma? Poi guardate l'elenco dei passaggi, le righe che opencode scrive mentre lavora: trovate la richiesta di lettura e il file che il programma ha aperto. Quale file è stato aperto?

### 3B · Piano, esecuzione e permessi

opencode ha due modalità: **Plan** guarda e propone, **Build** esegue. Ai comandi, un'altra persona. Chiedete: «Crea il file nota_passaggio.txt con una sola riga: Controllare i freni della bici 12.» Prima in Plan, poi in Build. Prima di provare, tutti scrivono su un foglio in quale dei due il file comparirà.

I permessi di opencode sono tre:

| Permesso | Che cosa fa il programma |
| --- | --- |
| allow | esegue |
| ask | si ferma e chiede a voi |
| deny | non esegue |

Prima di rispondere al programma, decidete nel gruppo se approvare o rifiutare la scrittura e scrivete il perché. Alzata di mano: nel vostro computer virtuale il file c'è? Nella prova con le pastiglie il programma ha letto il registro senza chiedere: perché? Che differenza c'è con «PROPOSTA DA CONTROLLARE» nel vostro file?

### Che cosa avete visto

In Copilot e in Studio il coordinatore è un testo che il modello legge. In opencode il modello decide ancora che cosa chiedere; il programma apre i file, scrive e chiede il permesso.

| Che cosa | In Copilot e in Studio | In opencode |
| --- | --- | --- |
| I testi del noleggio | incollati nel messaggio | il programma li apre quando il modello lo chiede |
| Il piano prima di rispondere | una regola scritta nel testo | modalità Plan: il programma non modifica i file |
| «PROPOSTA DA CONTROLLARE» | parole nel testo | il programma si ferma e chiede il permesso |

Non lo abbiamo provato oggi: in opencode ogni lavoro può diventare un agente a parte, con i suoi permessi.

## Alla fine

Se il vostro agente potesse registrare un rimborso: allow, ask o deny? Perché? Prima di chiudere salvate `istruzioni_agente_noleggio.txt`. Non dovete consegnarlo.

## Se qualcosa non va

Se Copilot non è disponibile, usate una conversazione normale: nel primo messaggio incollate le vostre istruzioni, poi documenti e richiesta. Non sono vere istruzioni di sistema.

Se il computer virtuale del gruppo non parte o il modello non risponde, il gruppo si unisce a un altro, oppure la prova si fa dal proiettore: voi proponete la richiesta.

## I programmi usati

opencode: licenza MIT. I documenti del noleggio sono inventati per questa esercitazione.
