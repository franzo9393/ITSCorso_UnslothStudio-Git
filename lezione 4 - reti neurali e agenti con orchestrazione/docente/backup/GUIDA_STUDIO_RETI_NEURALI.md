# Guida di studio · Reti neurali e apprendimento automatico

**Per il docente della lezione 4 · documento riservato.** Serve a capire gli argomenti prima di condurli. Non è un testo da leggere agli studenti. Per i passaggi di conduzione (impostazioni, pulsanti, misure) fa fede `backup/GUIDA_DOCENTE.md`.

## Come usarla

- Leggila dall'inizio alla fine una volta. Poi apri i siti e rifai a mano quello che ti descrivo: capire guardando vale più che rileggere.
- Gli esempi segnati **(inventato)** servono solo a spiegare. Non sono risposte né dati di un programma vero. Non presentarli agli studenti come tali.
- Ogni sezione ha un riquadro **Verificato** e uno **Spiegazione**. Verificato: l'ho visto sul sito con le impostazioni della lezione. Spiegazione: serve a capire, ma il sito non la dimostra.
- In fondo trovi ciò che non so e che non serve sapere.

---

## 0. Che cos'è l'apprendimento automatico

**L'idea.** Normalmente un programma si scrive con regole: «se è sabato e c'è il sole, tieni pronte 15 biciclette». Nell'apprendimento automatico (in inglese *machine learning*) non scrivi la regola. Dai al programma molti esempi e lui trova da solo i numeri che servono per decidere bene.

**Esempio (inventato).** Vuoi che un programma riconosca i giorni in cui un negozio di biciclette fa il pienone. Invece di scrivere le regole, gli mostri mille giorni passati, ognuno con il tempo che faceva e la scritta «pienone» o «tranquillo». Il programma prova, sbaglia, corregge i suoi numeri, e dopo molti giri indovina bene anche i giorni che non ha mai visto.

Quattro parole da avere chiare:

| Parola | Che cosa vuol dire | Esempio |
| --- | --- | --- |
| Esempi (dati) | I casi da cui il programma impara | Mille giorni con l'esito scritto |
| Modello | Il programma che alla fine decide | Quello che dice «pienone» o «tranquillo» |
| Addestramento | Il periodo in cui il modello corregge i suoi numeri | I giri di prova sugli esempi |
| Uso | Quando il modello decide su un caso nuovo | Un giorno che non ha mai visto |

**Perché si tengono da parte degli esempi per la prova.** È come un compito in classe. Se lo studente ripassa soltanto gli esercizi già risolti, li ricorda a memoria e ottiene dieci. Ma il vero compito ha domande nuove. Per questo una parte degli esempi non si usa per imparare: si usa per provare. Ritroverai questa idea in Playground (Training loss e Test loss).

**Domande che possono farti.**

- *«Quindi il computer pensa?»* Il modello calcola. Non serve dire di più: nessuno strumento della lezione permette di dimostrare se «capisca».
- *«Dove sono le regole?»* Dentro i numeri. Non sono scritte in un punto leggibile: sono ripartite su moltissimi numeri.

---

## 1. Come un modello di linguaggio sceglie la parola successiva (Transformer Explainer)

### Che cosa devi capire

Un modello di linguaggio, quando completa una frase, non sceglie «la parola giusta». Per ogni parola possibile calcola una **probabilità** e poi ne estrae una. Le parole più probabili escono più spesso, ma non sempre.

**Esempio (inventato).** La tastiera del telefono, dopo «Stasera ceno con…», propone «te», «mia», «gli». Il modello grande funziona allo stesso modo, solo con molte più parole e molto più testo letto.

### La temperatura

La temperatura è una manopola che decide quanto concentrare o allargare le probabilità.

**Esempio con il dado.** Hai un dado con sei facce. Con temperatura bassa è un dado molto truccato: la faccia più probabile esce quasi sempre. Con temperatura alta è un dado quasi onesto: tutte le facce hanno una possibilità. La parola più probabile resta la prima, ma la sua barra si abbassa e le altre si alzano.

**Top-k.** Vuol dire «considera solo le k parole più probabili». Con k = 5 si guardano le cinque barre più lunghe e si ignora il resto. Nella lezione si lascia a 5 e non si tocca.

### Che cosa fanno gli studenti

Aprono `https://poloclub.github.io/transformer-explainer/`, usano il primo esempio («Data visualization empowers users to») e muovono solo **Temperature**. Devono portare la barra più lunga sopra il 90%, poi sotto il 30%. Leggono le percentuali: non estraggono parole e non premono Generate.

### Che cosa dire a voce

- «Ogni barra è una parola possibile. L'altezza dice quanto il modello la considera probabile.»
- «La temperatura non cambia il testo letto. Cambia quanto sono distanti le barre.»
- «Una barra alta non dice che la frase sia vera. Dice solo che quella parola è molto probabile dopo quelle prima.»
- La stessa richiesta può dare risposte diverse perché la parola viene estratta tra più possibilità. È la risposta alla slide 2.

### Che cosa aspettarti

**Verificato** (10 novembre 2026, primo esempio): la prima barra vale 97,66% con Temperature 0,2; 90,86% con 0,3; 54,67% con 0,8; 22,26% con 10. I due bersagli della consegna si raggiungono, ma sono osservati su quella versione del sito.

**Attenzione pratica.** La pagina scarica circa 650 MB all'apertura, anche se si usano solo gli esempi. Con la rete della scuola condivisa, aprila tu dal proiettore se la rete non regge.

### Domande probabili

- *«Perché ChatGPT o Copilot a volte mi dà risposte diverse?»* Perché esce una parola scelta tra più possibili, non sempre la più probabile. Le impostazioni interne di Copilot non le conosciamo, quindi non dire quale temperatura usa.
- *«Se una barra è al 98%, è vera?»* No. Vuol dire che quella parola è molto probabile, non che l'affermazione sia vera.
- *«Perché in inglese?»* Il sito usa un modello piccolo in inglese. Traduci la frase e le parole candidate; non è una prova d'inglese.

---

## 2. Che cos'è una rete neurale (TensorFlow Playground)

### Che cosa devi capire

Una rete neurale è fatta di tanti piccoli calcoli collegati. Ogni piccolo calcolo si chiama **neurone**. Il nome viene dall'idea del cervello, ma qui un neurone è soltanto un calcolo semplice.

**Che cosa fa un neurone.** Riceve dei numeri, li moltiplica ognuno per un suo numero (il **peso**), li somma, aggiunge un altro suo numero e restituisce un risultato.

**Esempio (inventato): decidere se portare l'ombrello.** Un neurone riceve due informazioni: quanto è nuvolo (da 0 a 10) e quanto è probabile la pioggia secondo le previsioni (da 0 a 10). Ha due pesi che dicono quanto conta ciascuna: per esempio le previsioni contano il doppio delle nuvole. Somma, e se il totale supera una soglia dice «porta l'ombrello». Cambiare i pesi cambia la decisione. **Imparare, per una rete, è trovare i pesi giusti.**

Tre parole che incontrerai sullo schermo:

| Parola | In breve |
| --- | --- |
| Peso | Il numero su un collegamento tra due neuroni. È ciò che la rete cambia mentre impara |
| Strato nascosto | Una colonna di neuroni tra gli ingressi e l'uscita. «Nascosto» perché non si vede né l'ingresso né il risultato finale |
| Errore (loss) | Un numero che dice quanto la rete sbaglia. Più è basso, meglio è |

### Come impara

**Esempio con la ricetta.** Assaggi una zuppa, è troppo salata, ne metti meno; la riassaggi, ora è insipida, ne rimetti un po'. Ogni assaggio è un errore e ogni correzione è piccola. La rete fa lo stesso: guarda l'errore e cambia ogni peso un pochino nella direzione che lo riduce, poi ripete. Un giro completo su tutti i punti di addestramento si chiama **Epoch**. Nella lezione dico «giri».

Altra immagine utile: scendere da una collina con la nebbia. Non vedi la valle, ma senti da che parte scende il terreno e fai un passo da quella parte.

### Che cosa fa Playground

Il sito mostra punti di due colori (blu e arancione) su un foglio. Ogni punto ha due coordinate, **X1** (orizzontale) e **X2** (verticale). La rete riceve le coordinate e deve indovinare il colore. Lo sfondo colorato a destra mostra, per ogni posizione, che colore la rete prevede.

Nel cerchio i punti blu stanno al centro e gli arancioni attorno. Una linea retta non basta a separarli: serve chiudere i blu.

### Perché servono tre neuroni

**Spiegazione** (serve per leggere ciò che si vede, non è una dimostrazione):

- Un neurone di questo tipo separa i colori con **una linea**, sfumata dal blu all'arancione. Se passi il mouse su un neurone, vedi la sua linea nel riquadro grande a destra.
- Con zero neuroni nascosti la rete ha una linea sola. Con uno, anche. Con due, due linee: possono fare una striscia o un angolo, ma non chiudono il cerchio.
- Con tre linee si può chiudere un triangolo con gli angoli arrotondati attorno ai blu.

**Verificato** (11 novembre 2026, cerchio, sei serie diverse di punti, uno strato nascosto):

| Neuroni nascosti | Test loss dopo circa 1.500 giri |
| --- | --- |
| 0 | circa 0,50, in tutte le prove |
| 1 | tra 0,40 e 0,44 |
| 2 | tra 0,22 e 0,29 |
| 3 | sotto 0,05 in 5 prove su 6; la sesta è rimasta a 0,19 |
| 4 | sotto 0,05 in tutte le 6 prove |

Con 3 neuroni la soglia non è garantita: partenze diverse dei pesi (numeri casuali all'inizio) danno risultati diversi. Se uno studente non ci riesce, azzera e riprova una volta. Non dire «servono 3» come regola: con 4 sono riuscite tutte.

### Che cosa fanno gli studenti

Aprono `https://playground.tensorflow.org/`, tolgono gli strati nascosti (zero), prevedono a mano alzata quanti neuroni servono, poi provano con 0, 1, 2, 3, 4 neuroni, fermandosi a 1.500 giri. Cercano il numero più piccolo con cui **Test loss** scende sotto 0,05. Poi:

- passano il mouse su un neurone e guardano il suo disegno;
- passano il mouse su una linea tra due neuroni: compare «Weight is…», il peso. Lo leggono, azzerano, avviano e lo rileggono: è cambiato;
- provano la spirale, senza obbligo di riuscire.

### Il punto sull'errore di addestramento e di prova

- **Training loss**: l'errore sui punti che la rete usa per imparare.
- **Test loss**: l'errore sui punti tenuti da parte.

È il compito in classe con esercizi già visti contro un compito con domande nuove.

Il docente (tu) aggiunge **Noise**: un disturbo che sposta i punti a caso, così i due colori si mescolano un po' e alcuni punti fanno da «tranello». Con tanti neuroni e pochi punti di addestramento la rete può imparare a memoria anche i tranelli: l'errore sugli esempi scende, ma sui punti nuovi va peggio. Si chiama **sovradattamento** (in inglese *overfitting*) ma nella lezione non serve il nome.

**Verificato** (10 novembre 2026, Noise 50, 10% di punti per addestrare, 8 e 8 neuroni): in una prova Training/Test sono passati da 0,236/0,375 (circa 172 giri) a 0,066/0,556 (circa 1.000 giri): l'errore sugli esempi è sceso, quello sui punti nuovi è salito. In altre due prove a 1.000 giri: 0,174/0,374 e 0,116/0,545. Sono esecuzioni, non un esito garantito: se Test loss non peggiora, leggi quello che vedi.

**Come dirlo.** Se Training loss scende e Test loss sale, la rete ha imparato anche il disturbo dei punti che ha visto e va peggio sui punti nuovi. Vale anche per un agente: va provato con richieste diverse dagli esempi (è il punto della slide 32 e della parte 4D).

### Spirale

**Verificato** (11 novembre 2026, un seme): 4 e 2 neuroni → Test loss 0,50; uno strato da 8 → 0,30; 8 e 4 → 0,20; 8 e 8 → sotto 0,05 a 1.293 e 1.222 giri. Vicino alla soglia, non garantito. Come dirlo: la spirale gira su se stessa, servono molte più linee, combinate in più strati.

### Domande probabili

- *«Il neurone è come quello del cervello?»* Il nome viene da lì. In Playground è solo un piccolo calcolo: moltiplica, somma, decide.
- *«Perché con tre neuroni a me non riesce?»* I pesi partono da numeri casuali: dipende anche dalla partenza. Riprova dopo l'azzeramento.
- *«Che cos'è Tanh?»* Un tipo di funzione che trasforma il risultato in un numero tra −1 e 1. Non serve per l'attività: vi tornate se resta interesse.
- *«Che cos'è il Learning rate?»* Quanto grande è ogni correzione. Troppo grande e la rete salta oltre il punto giusto, troppo piccolo e ci mette molto. Nella lezione è fisso a 0,03.
- *«Quanti neuroni ha un modello vero?»* Molti più: miliardi di pesi nei modelli grandi. Per Copilot non lo so e non serve dirlo.

---

## 3. Un altro modo di imparare: tenere le reti migliori (Flappy Learning)

### Che cosa devi capire

Qui nessuno corregge i pesi guardando un errore. Funziona come un allevamento: si tengono quelli che vanno meglio e si fanno piccoli cambiamenti a caso.

**Esempio.** Cinquanta uccellini. Ognuno ha una piccola rete che, guardando la sua altezza e l'altezza del bordo superiore del varco tra i tubi, decide se saltare. All'inizio quasi tutti sbattono subito. A ogni generazione restano le reti dei migliori, le loro copie con piccole variazioni a caso, e qualche rete nuova. Dopo qualche generazione gli uccellini volano molto più a lungo.

**Un punto che confonde.** Anche qui i pesi cambiano, ma da una generazione all'altra e a caso, non perché qualcuno li corregge dopo un errore. Il singolo uccellino non impara durante il suo volo.

**Verificato** (10 novembre 2026, velocità MAX): in quattro prove Score oltre 10.000 alla generazione 26, 22, 45 e 44, con 1 o 2 uccellini ancora vivi. Sono letture osservate, non una frequenza attesa.

### Che cosa fai tu

Lo apri dal proiettore, gli studenti guardano. Non fare previsioni e non farlo aprire a loro. **Score conta i passi della simulazione, non i tubi.** Nessuna promessa di un uccellino «immortale»: un volo lungo non è un volo infinito.

### Frase di confronto

«In Playground i pesi si correggono guardando l'errore. In Flappy si copiano le reti migliori con modifiche a caso. In Copilot i pesi restano fermi: voi cambiate il testo che il modello legge.»

### Domande probabili

- *«Quindi l'uccellino impara?»* Impara la popolazione, generazione dopo generazione. Il singolo uccellino no.
- *«Anche Copilot è stato addestrato così?»* Non lo sappiamo e non lo diciamo.

---

## 4. Pesi contro testo: che cosa si cambia con un agente di Copilot

### Che cosa devi capire

I modelli come quello dietro Copilot hanno un numero enorme di pesi. Si fissano durante l'addestramento, fatto dall'azienda, con moltissimi testi. Gli studenti non lo toccano.

Quando scrivono le istruzioni di un agente, cambiano una cosa diversa: **un testo che il modello legge insieme alla richiesta**. I pesi restano uguali.

**Esempio.** Un collega esperto. Anni di esperienza lo hanno formato: sono i suoi pesi. Un foglio con le regole di oggi («rispondi in due righe, chiedi sempre il numero della bici») cambia come risponde oggi, ma non gli cambia l'esperienza.

### Dove sta il punto nella lezione

- Slide 11: «In Playground e in Flappy cambiavano i pesi. Qui cambiate il testo.»
- Parte 4F: stessa richiesta, stessi documenti, con e senza istruzioni. Le risposte possono essere uguali o diverse: sono risultati validi. Il confronto non mostra i pesi, mostra solo l'effetto del testo.
- Le preferenze tra risposte («questa mi piace di più») possono diventare dati per un vero addestramento. Qui non succede.

### Parole della parte 4

| Parola | In breve |
| --- | --- |
| Agente | Un assistente di Copilot con istruzioni salvate |
| Lavoro | Una parte delle istruzioni dedicata a un compito (per esempio FUORI SERVIZIO). Nome tecnico: competenza |
| Elenco delle richieste | L'elenco che dice quale lavoro usare per quale domanda. Nome tecnico: indice |
| Orchestrazione | Nome tecnico di «scegliere quali lavori usare e in che ordine». In aula non si usa: basta l'elenco |

### Domande probabili

- *«Copilot impara dalle mie istruzioni?»* Per questa attività si cambia solo il testo letto. Che cosa Microsoft faccia con le conversazioni non lo sappiamo: non lo dire e non promettere.
- *«Allora le istruzioni non servono?»* Servono: cambiano le risposte. Non cambiano i pesi.
- *«Perché la riga «Lavoro usato» non basta?»* È una frase scritta dal modello. Conta ciò che fa la risposta, e si controlla sui documenti.

---

## Glossario

- **Agente**: assistente di Copilot con istruzioni salvate.
- **Apprendimento automatico**: far trovare a un programma i numeri giusti partendo da esempi.
- **Lavoro** (nome tecnico: competenza): parte delle istruzioni dedicata a un compito.
- **Epoch**: un giro completo sui punti di addestramento. Nella lezione «giri».
- **Errore (loss)**: numero che dice quanto la rete sbaglia.
- **Elenco delle richieste** (nome tecnico: indice): elenco che collega ogni domanda a un lavoro.
- **Modello**: il programma che alla fine decide.
- **Neurone**: piccolo calcolo: moltiplica, somma, restituisce un risultato.
- **Noise**: disturbo che sposta i punti a caso, così i due colori si mescolano un po'.
- **Orchestrazione**: scegliere quali lavori usare e in quale ordine. In aula non si usa il nome.
- **Peso**: numero su un collegamento tra neuroni; è ciò che la rete cambia mentre impara.
- **Probabilità**: quanto una parola è attesa dopo il testo che la precede.
- **Sovradattamento**: imparare a memoria gli esempi e andare male sui casi nuovi.
- **Strato nascosto**: colonna di neuroni tra ingressi e uscita.
- **Temperatura**: manopola che concentra o allarga le probabilità.
- **Test loss**: errore sui punti tenuti da parte.
- **Top-k**: considera solo le k parole più probabili.
- **Training loss**: errore sui punti usati per imparare.

## Riepilogo da rileggere prima di entrare in aula

1. Un modello non sceglie «la parola giusta»: assegna probabilità e ne estrae una. La temperatura le concentra o le allarga.
2. Una rete è fatta di neuroni che moltiplicano, sommano e decidono. Imparare vuol dire cambiare i pesi per ridurre l'errore.
3. Un neurone traccia una linea: con 0, 1 o 2 non si chiude il cerchio, con 3 si può, con 4 sempre nelle mie prove.
4. L'errore sui punti di addestramento non basta: conta l'errore sui punti nuovi.
5. In Flappy si tengono le reti migliori; in Copilot si cambia il testo letto, non i pesi.

## Che cosa non so e che non serve sapere

- Come funzionano esattamente le piccole variazioni a caso in Flappy (so che le reti migliori vengono copiate e variate; non ho letto il dettaglio del codice per questa guida).
- Quanti neuroni o quali impostazioni ha Copilot.
- Che cosa Microsoft faccia con le conversazioni degli studenti.
- Perché Playground usa proprio Tanh e quali alternative ci siano.
- Se un modello «capisca»: gli strumenti della lezione non permettono di rispondere.

Se uno studente chiede una di queste cose, puoi dire: «Non lo so e non serve per quello che facciamo. Lo cerchiamo se resta interesse.»

## Prima di entrare in aula

Apri tu i tre siti e rifai quello che hai letto: il disegno dentro ogni neurone, il peso che cambia, le barre che si spostano con la temperatura. Non ho provato nulla con gli studenti né in Copilot con l'account scolastico: le misure sopra sono del mio browser, non delle postazioni della scuola.
