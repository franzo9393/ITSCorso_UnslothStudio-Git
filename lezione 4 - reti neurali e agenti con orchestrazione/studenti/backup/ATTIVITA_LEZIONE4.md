# Lezione 4 · Un agente che sa fare più cose

**ITS MAKER Bologna · 12 novembre 2026 · Microsoft Copilot e tre siti nel browser**

## Da dove partiamo

Il titolare del noleggio di biciclette Ruota Libera chiede:

> «Vorrei un solo assistente: deve dirmi da quanto tempo una bici è fuori servizio e saper fare anche un altro lavoro. Quando gli chiedo due cose insieme, deve capire quali informazioni servono.»

Prima provate come imparano piccole reti nel browser. Poi scrivete e provate le vostre istruzioni in Microsoft Copilot. È un'esercitazione: Copilot produce testo, non gestisce il negozio.

Ognuno lavora sul proprio computer. Non ci sono file da consegnare né un diario da compilare. Il risultato si guarda sullo schermo e si discute insieme dal proiettore. Salvate un solo file vostro: `istruzioni_agente_noleggio.txt`, con **solo le istruzioni dell'agente**.

## Parte 1 · Cambiate le probabilità

**Sfida: portate la barra più lunga sopra il 90%, poi sotto il 30%, cambiando solo Temperature.**

1. Aprite Transformer Explainer: `https://poloclub.github.io/transformer-explainer/`, quando lo dice il docente, oppure seguite il proiettore. La pagina avvia uno scarico di circa 650 MB anche se usate gli esempi. Se compare «What is Transformer?», chiudetelo con la X.
2. Usate il primo esempio del menu **Examples**: «Data visualization empowers users to». Il docente traduce la frase e le parole candidate: non è una prova d'inglese. È un modello che completa un testo, non un assistente a cui fare domande.
3. Guardate a destra **Probabilities**, le probabilità delle parole successive. Prima di toccare il cursore, scegliete per alzata di mano: alzando **Temperature**, la barra più lunga salirà o scenderà?
4. Cercate i due bersagli della sfida. Lasciate **Top-k** a 5; non toccate **Sampling** né **Generate**. Leggete le percentuali, non contate quante volte esce una parola.
5. Confrontate i due risultati e chiudete la scheda.

La parola più probabile non è l'unica possibile. Una probabilità alta non significa che un'affermazione sia vera.

## Parte 2 · Quanti neuroni servono?

**Sfida: separare i punti blu da quelli arancioni, con Test loss sotto 0,05 entro 1.500 giri, usando meno neuroni nascosti possibile.**

Aprite TensorFlow Playground: `https://playground.tensorflow.org/`. La rete deve separare punti di due colori. Una parte dei punti serve ad addestrarla; gli altri servono a provarla, come in un compito in classe con domande nuove.

La pagina si apre già pronta. Controllate tre cose: i dati sono il cerchio, gli ingressi sono solo **X1** e **X2**, **Noise** è 0. Il docente legge dal proiettore le altre impostazioni. Con il pulsante **−**, accanto a «Hidden layers», togliete i due strati nascosti che ci sono all'inizio: devono essere 0.

Prima di toccare qualcosa, per alzata di mano: quanti neuroni servono per circondare i punti blu? Nessuno, 1, 2, 3 o 10? Contano solo i neuroni nascosti, quelli tra gli ingressi e l'uscita.

1. Con zero neuroni nascosti, avviate con il triangolo. **Epoch** conta i giri di addestramento. **Test loss** è l'errore sui punti di prova: più è basso, meglio è. Fermatevi a 1.500 giri. Guardate l'area colorata a destra: che forma ha il confine tra i due colori?
2. Con il **+** accanto a «Hidden layers» aggiungete uno strato: nasce già con 2 neuroni. Sopra la colonna dei neuroni, il **−** ne toglie uno e il **+** ne aggiunge uno. Ogni volta che cambiate il numero di neuroni la rete riparte da zero: premete il triangolo e fermatevi a 1.500 giri. Provate con 1, 2, 3 e 4 neuroni. Non cambiate altre impostazioni e non usate **Regenerate**: cambia i punti.
3. Cercate il numero più piccolo di neuroni con cui Test loss scende sotto 0,05, e lasciate quella prova sullo schermo. Se con un certo numero non ci riuscite, azzerate con il pulsante a sinistra del triangolo e riprovate una volta: i numeri di partenza dei collegamenti cambiano e il risultato può cambiare.
4. Con la rete che funziona, passate il mouse su un neurone: il suo disegno compare in grande nel riquadro a destra, al posto dell'uscita. Che cosa disegna ogni neurone? Come si mettono insieme nell'uscita?
5. Azzerate. Passate il mouse su una linea tra due neuroni: compare «Weight is…», un numero. È il **peso** di quel collegamento. Avviate, fermatevi a 1.500 giri e rileggete lo stesso peso: è cambiato. Imparare, per questa rete, vuol dire cambiare questi numeri.
6. Selezionate la spirale e provate la stessa sfida. Potete aggiungere strati e neuroni; non cambiate gli ingressi. Anche non riuscire entro il limite è un risultato da spiegare.

La struttura della rete e i numeri di partenza possono cambiare il risultato.

Poi guardate il proiettore: il docente aggiunge disturbo (**Noise**) ai punti e confronta **Training loss**, l'errore sui punti usati per imparare, con **Test loss**. Migliorare sui punti già visti basta per migliorare anche sugli altri?

## Parte 3 · Un esempio dal proiettore

Il docente apre Flappy Learning: `https://xviniette.github.io/FlappyLearning/`. Ogni uccellino ha una piccola rete che decide quando saltare. A ogni generazione restano le reti dei migliori, con piccole variazioni a caso. Guardate che cosa succede dopo qualche generazione. **Score** conta i passi della simulazione, non i tubi superati.

Anche qui cambiano i pesi, ma nessuno li corregge guardando un errore: si copiano le reti migliori con piccole modifiche a caso. È un altro modo di imparare.

## Parte 4 · Un agente per il noleggio Ruota Libera

Ora cambia il lavoro: non guardate più reti, scrivete istruzioni per Copilot. Copilot legge il testo che scrivete voi: i suoi pesi non cambiano. Il percorso è questo:

1. guardate un agente già fatto, per un altro caso: una pizzeria d'asporto;
2. scrivete il primo lavoro dell'agente per il noleggio: il fuori servizio;
3. aggiungete un secondo lavoro;
4. inventate due richieste per metterlo alla prova;
5. confrontate le risposte con e senza le vostre istruzioni.

Prima di cominciare, aprite questi programmi:

| Programma | Che cosa ci fate |
| --- | --- |
| Teams | scaricate i tre testi del noleggio |
| Blocco note | aprite i tre testi e scrivete le vostre istruzioni |
| Microsoft Copilot | con l'account scolastico, salvate l'agente e lo provate |

| Testo da scaricare | Che cosa contiene |
| --- | --- |
| `Registro_Ruota_Libera_7-8_novembre_2026.txt` | gli appunti del banco di un fine settimana |
| `Regole_noleggio_Ruota_Libera.txt` | orari, listino, termini e calcoli |
| `Guida_guasti_Ruota_Libera.txt` | i guasti più comuni e che cosa fa il banco |

L'estensione `.txt` indica un file di testo semplice. Per copiarlo: Ctrl+A, Ctrl+C; per incollarlo: Ctrl+V. I tre testi sono le fonti: non vanno copiati nel file delle istruzioni.

### 4A · Guardate un agente già fatto

Il docente mostra un agente per una pizzeria d'asporto. Un **agente** è un assistente di Copilot con istruzioni salvate: le scrive chi lo crea e Copilot le legge a ogni conversazione. Quello della pizzeria non è il vostro noleggio: serve a vedere com'è fatto un agente che sa fare più lavori. Le sue istruzioni hanno quattro parti:

| Parte | A che cosa serve |
| --- | --- |
| Regole per tutte le richieste | valgono sempre |
| Indice delle richieste | dice quale lavoro usare |
| Competenze | un lavoro ciascuna, con i suoi dati e le sue regole |
| Stile delle risposte | come deve parlare |

Il docente proietta una richiesta di un cliente. Per alzata di mano: quale lavoro serve per primo, oppure ne servono due? Poi guardate la risposta e il testo che l'ha guidata. La prima riga dice «Competenza usata»: l'ha scritta il modello. Controllate voi se la risposta fa davvero quel lavoro.

**Orchestrare** significa scegliere quali lavori usare e in che ordine. Qui lo fate con del testo: le competenze non sono programmi separati.

Il vostro agente avrà le stesse quattro parti. Il contenuto lo scrivete voi.

### 4B · Primo lavoro: il fuori servizio

1. Aprite Blocco note e salvate un file nuovo: `istruzioni_agente_noleggio.txt`.
2. Scrivete voi, senza far preparare il testo a Copilot, due cose:
   - le regole comuni: ruolo (l'agente risponde al titolare e al banco, non ai clienti), lingua, quali testi può usare, che cosa non deve fare;
   - il lavoro **FUORI SERVIZIO**: quando si usa, quali dati servono, come calcola i minuti secondo le regole del noleggio, quali orari mostra, che cosa risponde se un dato manca.
3. Decidete come comincia ogni risposta: con «Competenza usata:» e il nome del lavoro. «Rispondi bene» non basta: dite che cosa fare con un dato scritto nei testi e con un dato che manca.
4. Il docente vi mostra dove incollare le istruzioni in Copilot, se la funzione agente è disponibile. Non usate la creazione automatica del testo: incollate le vostre istruzioni e salvate l'agente. Se la funzione non c'è, seguite «Se Copilot non è disponibile», in fondo.
5. Aprite una nuova conversazione con l'agente. In un solo messaggio incollate il registro e le regole del noleggio e scrivete in fondo la prima richiesta del proiettore, senza aggiungere suggerimenti. Inviatela prima che il docente mostri i criteri.
6. Confrontate la risposta con i criteri e rispondete per alzata di mano. Se qualcosa non va, correggete le istruzioni e riprovate in una nuova conversazione.
7. Nella conversazione della prima prova, scrivete la seconda richiesta del proiettore. Aspettate la risposta prima di leggere il nuovo criterio. Controllate che ogni numero usato dal modello sia scritto nel registro o nelle regole del noleggio. Correggete soltanto dove serve.

### 4C · Secondo lavoro, indice e stile

Scegliete uno dei due lavori:

| Lavoro | Fonte | Obiettivo e limiti |
| --- | --- | --- |
| GUASTI | Guida ai guasti | Spiegare significato, primo controllo del banco e chi interviene, dove la guida lo indica. Niente consigli per far uscire dal negozio una bici con freni o sterzo che non funzionano. |
| PASSAGGIO | Registro | Preparare una nota per il turno successivo con fatti, interventi e controlli ancora da fare. Chiarire giorno o turno quando non sono identificabili. |

Aggiungete al vostro file:

- il lavoro scelto, scritto come FUORI SERVIZIO: quando si usa, quali testi usa, quali dati servono, come risponde, che cosa fa se i testi non bastano;
- l'**indice delle richieste**: quale richiesta va a quale lavoro;
- che cosa fare se una richiesta serve a **entrambi** i lavori, e quale viene prima;
- che cosa rispondere a una richiesta che non serve a nessuno dei due, cioè **fuori indice**;
- **due esempi vostri** del modo in cui volete ricevere le risposte. Devono mostrare uno stile, non diventare risposte da ripetere a tutte le domande.

Salvate e aggiornate l'agente in Copilot. Controllate che il testo sia arrivato intero: nel passaggio possono perdersi righe. Il file conserva soltanto le istruzioni, senza appunti sulle modifiche.

### 4D · Inventate due richieste per metterlo alla prova

Inventate voi due richieste, diverse dagli esempi di stile:

- una che richieda **entrambi i lavori**;
- una con **un dato che manca** (la richiesta non lo dice), **un testo che non basta** (i documenti non lo contengono) oppure **un lavoro che l'agente non ha** (fuori indice).

Prima di inviare ogni richiesta, decidete che cosa conterà come risposta corretta e individuate nei testi i passi che permettono di controllarla. Potete dirlo a voce: non compilate un registro.

Scrivete la richiesta in Copilot, in una **nuova conversazione per ogni caso**. In un solo messaggio, come nella prima prova, mettete i documenti necessari e in fondo la richiesta. Con FUORI SERVIZIO e GUASTI servono registro, regole del noleggio e guida ai guasti; con FUORI SERVIZIO e PASSAGGIO servono registro e regole. Nel secondo caso scegliete i documenti in base alla richiesta, senza aggiungere il dato che volete mettere alla prova.

Confrontate la risposta con ciò che avevate deciso e con i documenti. Una domanda per ottenere un dato davvero necessario può essere la risposta corretta. Se tutto funziona, spiegate quale vostra regola lo rende possibile e inventate un'altra richiesta: non peggiorate le istruzioni per provocare un errore.

### 4E · L'ultima richiesta e le correzioni

Aprite una nuova conversazione. In un solo messaggio incollate il **registro** e scrivete in fondo l'ultima richiesta dal proiettore. Solo dopo la risposta il docente mostra il criterio.

Riguardate anche le vostre due richieste. Se qualcosa non rispetta i testi o le istruzioni, correggete il punto necessario nel file, aggiornate Copilot e riprovate quel caso in una nuova conversazione. Una prova superata dopo una correzione vale quanto una superata al primo invio. Non c'è un errore da ottenere per forza.

Nel confronto finale raccontate dal vostro schermo un caso e la regola che avete mantenuto o cambiato. Niente elenco scritto degli esiti.

Poi il docente proietta un esempio di istruzioni per il noleggio. Confrontatelo con il vostro file: che cosa avete scritto voi e non c'è nell'esempio? Che cosa c'è nell'esempio e vi manca? Se trovate una regola che vi manca, scrivetela con parole vostre: non si copia l'esempio. Se avete aggiunto una regola, aggiornate l'agente e riprovate una vostra richiesta in una nuova conversazione: questa risposta vi servirà nel confronto finale.

### 4F · Avete cambiato i pesi o il testo?

1. Scegliete una richiesta provata con le istruzioni che avete adesso, per cui avete una risposta reale del vostro agente. Conservate esattamente richiesta e documenti.
2. In una nuova conversazione con **Copilot normale, senza agente**, inviate in un solo messaggio gli stessi documenti e la stessa richiesta, senza le vostre istruzioni.
3. In un'altra nuova conversazione con l'agente, inviate ancora in un solo messaggio gli stessi documenti e la stessa richiesta. Mantenete le stesse istruzioni della prima risposta.
4. Confrontate ordine, lunghezza e parole delle tre risposte. Tra le due risposte dell'agente, scegliete quella che preferite e dite **due motivi** a voce; se sono equivalenti, motivate la parità. Poi confrontatele con quella senza agente.

Possono uscire risposte uguali o differenze poco visibili: sono risultati validi. Le istruzioni cambiano il **testo letto** da Copilot, non i suoi **pesi**. Le preferenze tra risposte possono diventare dati per un vero addestramento; questa attività non addestra il modello. Flappy e Playground aiutano a distinguere i procedimenti, non riproducono l'addestramento di Copilot.

## Se Copilot non è disponibile

Avvisate il docente. Se non potete creare un agente, usate una conversazione normale: in ogni chat nuova inviate prima le vostre istruzioni, poi documenti e richiesta. È un primo messaggio, **non una vera istruzione di sistema**. Nel confronto finale usate una chat con quel messaggio e una senza.

Se la piattaforma non risponde, seguite la prova a secco collettiva: si legge una richiesta e si cerca nelle istruzioni di uno studente come gestirla. È un controllo del testo, non una risposta eseguita dal modello e non dimostra l'affidabilità dell'agente.

Se il messaggio è troppo lungo, usate soltanto i giorni completi del registro necessari alla richiesta, conservando la sequenza degli eventi. Se il campo delle istruzioni è troppo corto, togliete ripetizioni e accorciate gli esempi, senza perdere fonti, limiti e regole dell'indice.

Prima di chiudere salvate `istruzioni_agente_noleggio.txt`. Non dovete caricarlo o consegnarlo.

## I siti usati

Transformer Explainer: Georgia Tech, Polo Club of Data Science, licenza MIT. TensorFlow Playground: Daniel Smilkov e Shan Carter, Apache-2.0. Flappy Learning: xviniette, MIT. I documenti del noleggio sono inventati per questa esercitazione.
