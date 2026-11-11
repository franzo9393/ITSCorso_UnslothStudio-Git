# Lezione 4 · Un agente che sa fare più cose

**ITS MAKER Bologna · 12 novembre 2026 · Microsoft Copilot e tre siti nel browser**

## Da dove partiamo

Il responsabile del reparto presse chiede:

> «Per la P03 vorrei un solo assistente: deve controllare un fermo e saper fare anche un altro lavoro. Quando gli chiedo due cose insieme, deve capire quali informazioni servono.»

Prima provate come imparano piccole reti nel browser. Poi scrivete e provate le vostre istruzioni in Microsoft Copilot. È un'esercitazione: Copilot produce testo, non comanda la pressa.

Ognuno lavora sul proprio computer. Non ci sono file da consegnare né un diario da compilare. Il risultato si guarda sullo schermo e si discute insieme dal proiettore. Salvate un solo file vostro: `istruzioni_assistente_P03.txt`, con **solo le istruzioni dell'agente**.

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

## Parte 4 · Costruite e collaudate l'agente P03

Aprite Microsoft Copilot con l'account scolastico. Scaricate da Teams questi tre testi e apriteli con Blocco note:

- `Registro_P03_13-15_ottobre_2026.txt`: i fatti della pressa;
- `Regole_indicatori_P03.txt`: le definizioni per i calcoli;
- `Guida_allarmi_P03.txt`: le spiegazioni e i limiti degli interventi.

L'estensione `.txt` indica un file di testo semplice. Per copiarlo: Ctrl+A, Ctrl+C; per incollarlo: Ctrl+V. I documenti restano fonti separate: non vanno copiati nel file delle istruzioni.

Un **agente** è un assistente di Copilot con istruzioni salvate. Una **competenza** è una parte delle istruzioni dedicata a un lavoro. L'**indice delle richieste** collega le domande alle competenze. **Orchestrazione** significa scegliere quali usare e in quale ordine: qui lo chiedete con del testo, non programmate funzioni separate.

### 4A · Scegliete prima di vedere la risposta

Il docente mostra un agente per un noleggio di biciclette. Non è la P03: serve a vedere la struttura di un agente con più competenze prima di scrivere il vostro. Per la richiesta proiettata, scegliete per alzata di mano quale competenza serve, oppure se ne servono due. Poi guardate la risposta e le istruzioni che l'hanno guidata. La riga «Competenza usata» è una dichiarazione del modello: controllate anche quello che fa davvero. Poi tornate alla pressa.

### 4B · Provate subito una competenza

Aprite Blocco note e salvate `istruzioni_assistente_P03.txt`. Scrivete voi, senza far preparare il testo a Copilot:

- le regole comuni: ruolo, lingua, fonti ammesse e limiti;
- una competenza **FERMO**, che ricavi la durata secondo le regole, mostri gli orari usati e chieda i dati necessari quando mancano.

Decidete come deve essere fatta la risposta. Deve cominciare con «Competenza usata:» e il nome. Le istruzioni devono permettere di distinguere un dato documentato da un dato assente: non basta dire «rispondi bene».

Il docente mostra come inserire e salvare le istruzioni, se la funzione agente è disponibile. Non usate la creazione automatica del testo. Copiate le vostre istruzioni, poi aprite una nuova conversazione con l'agente.

Incollate **registro e regole degli indicatori**, poi la prima richiesta dal proiettore, senza aggiungere suggerimenti. Inviatela prima che il docente mostri i criteri. Confrontate risposta e fonti con i criteri rivelati, poi rispondete per alzata di mano. Se serve, correggete le istruzioni e riprovate in una conversazione nuova.

Nella chat che contiene la prima prova proseguite con la seconda richiesta del proiettore. Aspettate la risposta prima di leggere il nuovo criterio. Controllate se il modello usa dati presenti oppure sceglie da solo quelli che gli servono. Correggete soltanto dove occorre.

### 4C · Aggiungete un secondo lavoro

Scegliete una delle due competenze:

| Competenza | Fonte | Obiettivo e limiti |
| --- | --- | --- |
| ALLARMI | Guida allarmi | Spiegare significato, primo controllo e chi interviene, dove la guida lo indica. Niente consigli aggiunti né aggiramenti delle protezioni. |
| PASSAGGIO | Registro | Preparare una nota per il turno successivo con fatti, interventi e controlli ancora richiesti. Chiarire giorno o turno quando non sono identificabili. |

Aggiungete al vostro file la competenza scelta e un indice per riconoscere le richieste. Stabilite che cosa fare se una richiesta richiede **entrambe** le competenze, in quale ordine usarle e che cosa rispondere a una richiesta **fuori indice**. Ogni competenza deve dire quali documenti servono e che cosa fare se le fonti non bastano.

Scrivete anche **due esempi vostri** del modo in cui volete ricevere le risposte. Devono mostrare uno stile, non diventare risposte da ripetere a tutte le domande.

Salvate e aggiornate le istruzioni in Copilot. Controllate che il testo sia arrivato intero: nel passaggio possono perdersi righe. Il file conserva soltanto le istruzioni, senza appunti sulle modifiche.

### 4D · Inventate due casi che contano

Inventate voi due richieste, diverse dagli esempi di stile:

- una che richieda **entrambe le competenze**;
- una con **un dato mancante, una fonte insufficiente o una richiesta fuori indice**.

Prima di inviare ogni caso, decidete che cosa conterà come risposta corretta e individuate sullo schermo i passi delle fonti che permettono di controllarla. Potete dirlo a voce: non compilate un registro.

Scrivete la richiesta direttamente in Copilot, in una **nuova conversazione per ogni caso**, insieme ai documenti necessari. Con FERMO + ALLARMI servono registro, regole degli indicatori e guida allarmi; con FERMO + PASSAGGIO servono registro e regole. Nel secondo caso scegliete le fonti in base alla richiesta, senza aggiungere il dato che volete mettere alla prova.

Confrontate la risposta con ciò che avevate deciso e con i documenti. Una domanda per ottenere un dato davvero necessario può essere la risposta corretta. Se tutto funziona, spiegate quale vostra regola lo rende possibile e inventate un altro caso: non peggiorate le istruzioni per provocare un errore.

### 4E · L'ultima richiesta e le correzioni

Aprite una nuova conversazione, incollate il **registro** e inviate l'ultima richiesta dal proiettore. Solo dopo la risposta il docente mostra il criterio.

Riguardate anche i vostri casi originali. Se qualcosa non rispetta fonti o istruzioni, correggete il punto necessario nel file, aggiornate Copilot e riprovate quel caso in una conversazione nuova. Un collaudo superato dopo una correzione vale quanto uno superato al primo invio. Non c'è un errore da ottenere per forza.

Nel confronto finale raccontate dal vostro schermo un caso e la regola che avete mantenuto o cambiato. Niente elenco scritto degli esiti.

### 4F · Avete cambiato i pesi o il testo?

1. Scegliete una richiesta del collaudo per cui avete già una risposta reale del vostro agente. Riutilizzate quella risposta e conservate esattamente richiesta e documenti.
2. In una nuova conversazione con **Copilot normale, senza agente**, inviate gli stessi documenti e la stessa richiesta, senza le vostre istruzioni.
3. In un'altra nuova conversazione con l'agente, inviate ancora gli stessi documenti e la stessa richiesta. Per il confronto mantenete le stesse istruzioni della prima risposta scelta.
4. Confrontate ordine, lunghezza e parole delle tre risposte. Tra le due risposte reali dell'agente, scegliete quella che preferite e dite **due motivi** a voce; se sono equivalenti, motivate la parità. Confrontatele anche con quella senza agente.

Possono uscire risposte uguali o differenze poco visibili: sono risultati validi. Le istruzioni cambiano il **testo letto** da Copilot, non i suoi **pesi**. Le preferenze tra risposte possono diventare dati per un vero addestramento; questa attività non addestra il modello. Flappy e Playground aiutano a distinguere i procedimenti, non riproducono l'addestramento di Copilot.

## Se Copilot non è disponibile

Avvisate il docente. Se non potete creare un agente, usate una conversazione normale: in ogni chat nuova inviate prima le vostre istruzioni, poi documenti e richiesta. È un primo messaggio, **non una vera istruzione di sistema**. Nel confronto finale usate una chat con quel messaggio e una senza.

Se la piattaforma non risponde, seguite la prova a secco collettiva: si legge una richiesta e si cerca nelle istruzioni di uno studente come gestirla. È un controllo del testo, non una risposta eseguita dal modello e non dimostra l'affidabilità dell'agente.

Se il messaggio è troppo lungo, usate soltanto i giorni completi del registro necessari alla richiesta, conservando la sequenza degli eventi. Se il campo delle istruzioni è troppo corto, togliete ripetizioni e accorciate gli esempi, senza perdere fonti, limiti e regole dell'indice.

Prima di chiudere salvate `istruzioni_assistente_P03.txt`. Non dovete caricarlo o consegnarlo.

## I siti usati

Transformer Explainer: Georgia Tech, Polo Club of Data Science, licenza MIT. TensorFlow Playground: Daniel Smilkov e Shan Carter, Apache-2.0. Flappy Learning: xviniette, MIT. I documenti P03 sono inventati per questa esercitazione.
