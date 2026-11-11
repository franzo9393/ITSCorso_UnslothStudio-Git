# Guida docente · Lezione 4

**ITS MAKER Bologna · 12 novembre 2026 · Microsoft Copilot e siti nel browser**

Documento riservato al docente.

## La lezione da condurre

Ognuno lavora da solo. Non passi tra i banchi, non raccogli file e non fai compilare appunti o registri di controllo. Gli esiti si leggono sugli schermi; il confronto collettivo avviene dal proiettore. Nessun nuovo strumento, cruscotto o punteggio legato alla fortuna del modello.

L'ordine è **Transformer Explainer → TensorFlow Playground → Flappy Learning (solo dal proiettore) → agente P03**. Si passa dalle probabilità di una parola a come una rete piccola impara cambiando numeri, poi a un altro modo di imparare (tenere le reti migliori), infine alla distinzione fra istruzioni e addestramento. I siti sono dimostrazioni di meccanismi diversi, non riproduzioni di Copilot. L'attività su cui si lavora a lungo è Playground: Flappy dura un paio di minuti.

Nella parte P03 si prova subito una competenza, prima di completare l'agente. Poi ciascuno aggiunge un secondo lavoro e inventa due casi critici. Il criterio è superare collaudi controllabili sulle fonti: un risultato corretto al primo invio e uno ottenuto dopo una correzione hanno lo stesso valore. Non occorre provocare un errore.

Si salva un solo file personale, `istruzioni_assistente_P03.txt`, con **solo le istruzioni**: niente diario delle correzioni, richieste o esiti in fondo. Si usa Blocco note per scrivere un oggetto da provare, non per compilare una scheda. Nessuna consegna e nessun voto in questa lezione.

Unsloth Studio non si usa. Le note per preparare la macchina virtuale della lezione successiva restano in `docente/backup/da_riprendere_lezione_5/NOTE_STUDIO_PER_LEZIONE_5.md`. Non promettere che le istruzioni P03 funzioneranno allo stesso modo con un modello piccolo. Non presumere che gli studenti abbiano svolto attività specifiche nella lezione precedente.

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE4.docx` e i tre testi `Registro_P03_13-15_ottobre_2026.txt`, `Guida_allarmi_P03.txt`, `Regole_indicatori_P03.txt`. Non pubblicare le cartelle di backup né l'esempio P03 all'inizio.
- Prepara la dimostrazione con `docente/ESEMPIO_DIMOSTRAZIONE_NOLEGGIO_BICICLETTE.txt`: nelle istruzioni dell'agente va soltanto il testo **tra i due separatori**, non l'introduzione né le richieste suggerite. Prova in anticipo le richieste del file, ciascuna in una chat nuova. Se non puoi eseguirlo, mostra il testo dichiarando che non è una risposta del modello.
- Tieni riservato `studenti/da_pubblicare_dopo_collaudo/ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` fino alla fine della parte **4E**. È un esempio da discutere, non una soluzione già collaudata in Copilot. Provalo prima dell'aula se l'account lo consente.
- Prepara il proiettore per mostrare **prima le richieste e soltanto dopo i criteri**. I valori P03 vengono dalle tavole automatiche in fondo a questa guida, non da numeri ricopiati a mano. La generazione è affidata a `docente/genera_materiali.py`, che legge gli originali in `docente/backup/fonti/`: conserva quei file intatti.
- Apri i siti dalla rete scolastica e controlla le impostazioni. Non aprire Transformer Explainer da tutte le postazioni in anticipo: usare Examples non ferma lo scarico del modello. Se la rete non regge, usa solo il proiettore.

### Controlli pre-aula

**Copilot non è stato provato con l'account studente.** La documentazione non sostituisce la prova sulla piattaforma della scuola. Mostra l'interfaccia agli studenti solo dopo il controllo; non dare per certi nomi di comandi o autorizzazioni.

| Controllo | Che cosa accertare | Esito |
| --- | --- | --- |
| Agente in Copilot | Creazione disponibile, campo delle istruzioni, salvataggio, modifica e riapertura in una chat nuova con le istruzioni aggiornate. Riferimento Microsoft: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder; indirizzo già registrato nella ricerca del corso, non riletto in questa riscrittura. | |
| Scrittura autonoma | Se la piattaforma propone di generare le istruzioni, mostra come evitarlo: gli studenti le scrivono loro. | |
| Limiti del testo | Prova istruzioni e messaggi con registro, regole e guida. Controlla che non si perdano righe nel copia-incolla e che le modifiche siano salvate. Non assumere un limite di caratteri non misurato. | |
| Nuove conversazioni | Verifica come aprire chat separate con l'agente e senza agente. Controlla eventuale memoria o personalizzazione dell'account: possono influire sul confronto finale. | |
| Transformer Explainer | Primo esempio, Top-k a 5, Probabilities leggibile, bersagli sopra 90% e sotto 30% con il solo Temperature. Controlla anche dopo lo scarico completo: quella condizione non è stata provata. | |
| Playground | Impostazioni della consegna con **zero strati nascosti**; il **+** degli strati crea 2 neuroni, il **−** e il **+** sopra la colonna ne tolgono e aggiungono uno; azzeramento; visibilità di Test loss, Training loss ed Epoch; passando il mouse su un neurone il suo disegno compare nel riquadro grande dell'uscita; passando su una linea compare «Weight is…». Prova tu 0, 1, 2, 3 e 4 neuroni e guarda i disegni. Prepara anche il confronto sul disturbo al proiettore. | |
| Flappy Learning | Si apre e parte da solo; trova il comando della velocità. Lo usi tu dal proiettore: gli studenti non lo aprono. La velocità delle postazioni scolastiche non è misurata. | |
| Rete e classe | Apertura simultanea dei siti e richieste Copilot con gli account scolastici. L'indirizzo pubblico è condiviso; prepara il ramo senza servizio. | |
| Documenti | I tre testi si aprono in Blocco note e si incollano senza perdere accenti, righe e numeri. | |

## Parti 1–3 · Risultati visibili, senza scrittura

### Transformer Explainer · Due bersagli sulle probabilità

Traduci «Data visualization empowers users to»: «La visualizzazione dei dati permette agli utenti di…». Dai anche il significato delle candidate quando le mostri. Non farne una prova di inglese.

Prima di muovere Temperature, chiedi per alzata di mano se alzandola la barra più lunga salirà o scenderà. La sfida usa **il primo esempio, Top-k a 5**: prima barra sopra 90%, poi sotto 30%, cambiando soltanto Temperature. Niente conteggio di estrazioni, Sampling o Generate. Il criterio è leggibile nelle percentuali; non serve che la parola estratta cambi ogni volta.

Se il riquadro «What is Transformer?» copre la pagina, chiudilo con la X. Probabilities è all'estrema destra: prova zoom e leggibilità sulla postazione reale. Alla fine chiudi la scheda, anche al proiettore. Se fai la prova soltanto tu, gli studenti prevedono e leggono i risultati, ma non hanno manipolato il sito personalmente: non presentare le due modalità come identiche.

Punto da dire: il testo precedente influenza le probabilità della prossima parola; la temperatura ne cambia la concentrazione. La parola più probabile non è una verifica di verità. Non conosciamo le impostazioni interne di Copilot.

### TensorFlow Playground · Quanti neuroni servono per circondare il cerchio

**Per te, in poche righe.** Non è teoria da leggere agli studenti: serve a capire che cosa si vede.

- Un neurone prende i due numeri che dicono dove sta un punto (X1 e X2), li moltiplica per due **pesi**, li somma e aggiunge un terzo numero suo, che sposta la linea. Ne esce un colore. I pesi sono i numeri dei collegamenti, e sono ciò che la rete cambia mentre impara: il sito li mostra passando il mouse su una linea.
- Un neurone di questo tipo separa i colori con **una linea**, sfumata dal blu all'arancione: si vede nel suo disegno. Con zero o un neurone nascosto c'è una linea sola. Con due ci sono due linee: possono fare una striscia o un angolo, ma la zona resta aperta e non chiude il cerchio. Con tre si può chiudere un triangolo con gli angoli arrotondati attorno ai punti blu. È la ragione per cui il risultato più probabile è 3.
- Questa è una spiegazione per leggere ciò che si vede, non una dimostrazione. Le misure la confermano: con 0, 1 e 2 neuroni Test loss resta alta, con 3 e 4 scende. La rete reale può disegnare una forma un po' diversa.
- Imparare vuol dire cambiare i pesi per ridurre l'errore sui punti di addestramento. L'errore sui punti di prova dice se la rete funziona anche su punti che non ha visto.

Se uno studente chiede altro (che cos'è Tanh, che cos'è la discesa del gradiente), puoi dire che non serve per questa attività e che vi tornate se resta interesse. Non devi saperlo spiegare per condurla.

**Impostazioni comuni:** Classification; cerchio; solo X1 e X2; Learning rate 0,03; Activation Tanh; Noise 0; 50% addestramento; Batch size 10; nessuna regolarizzazione; **zero strati nascosti**. La pagina aperta senza indirizzo parte già con queste impostazioni e con due strati da 4 e 2 neuroni; il browser può però conservare impostazioni precedenti. Gli studenti controllano solo cerchio, X1 e X2, Noise 0: leggi tu dal proiettore le altre. Tolgono i due strati con il **−** accanto a «Hidden layers».

**Come funzionano i pulsanti (provati l'11 novembre):** il **+** accanto a «Hidden layers» aggiunge uno strato che nasce con **2 neuroni**. Il **−** sopra la colonna toglie un neurone (si ferma a 1), il **+** ne aggiunge uno. Ogni cambio del numero di neuroni azzera l'addestramento. Quindi la sequenza è: 0 (nessuno strato), 2 (appena aggiunto lo strato), poi **−** per avere 1, poi **+** per 2, 3, 4.

**Sequenza.**

1. Alzata di mano: quanti neuroni servono per circondare i punti blu? Nessuno, 1, 2, 3 o 10. Nessuna risposta è sbagliata: serve a guardare con un'idea in testa.
2. Con zero neuroni avviano e fermano a 1.500 giri. Test loss resta intorno a 0,5 e il confine tra i colori è quasi una linea diritta.
3. Aggiungono uno strato, poi provano con 1, 2, 3 e 4 neuroni, avviando e fermando a 1.500 giri. Non toccano altre impostazioni, non usano Regenerate, non cambiano gli ingressi. Contano i quadratini nascosti, non gli ingressi e l'uscita.
4. Lasciano sullo schermo la prova con meno neuroni che raggiunge Test loss < 0,05. Se un numero non riesce, azzerano (pulsante a sinistra del triangolo) e riprovano una volta: l'azzeramento rinnova i pesi, non i punti. Se non riesce, mostrano dove sono arrivati: nessun obbligo e nessun diario. Il numero è un record osservato, non un minimo dimostrato.
5. Con la rete funzionante passano il mouse su un neurone: il suo disegno compare in grande nel riquadro dell'uscita. Chiedi: che cosa disegna ogni neurone? Come si mettono insieme? **Risposta da dare:** ogni neurone divide il foglio con una linea; l'uscita mette insieme le linee, e con tre si chiude una zona attorno ai blu.
6. Peso: azzerano, passano il mouse su una linea (compare «Weight is…» e il numero), avviano, fermano a 1.500 giri e rileggono la stessa linea. Il numero è cambiato: imparare, per questa rete, vuol dire cambiare questi numeri. Quella finestra dice anche «Click anywhere to edit»: si può cambiare il peso a mano, ma non serve e non lo proponi.
7. Spirale con la stessa sfida; possono aggiungere strati e neuroni, non cambiare gli ingressi. **Risposta da dare:** la spirale gira su se stessa, servono molte più linee, combinate in più strati. Nelle prove dell'11 novembre (un seme, Test loss alla fine dei 1.500 Epoch) 4 e 2 neuroni davano 0,50; uno strato da 8 dava 0,30; 8 e 4 davano 0,20; 8 e 8 sono arrivati sotto 0,05 a 1.293 e 1.222 Epoch (0,040 e 0,052 a fine prova): vicino alla soglia, non garantito. Anche un insuccesso è completo. Non aggiungere un livello sulle Features.

**Che cosa aspettarti sul cerchio** (prove dell'11 novembre, sei semi dei punti, impostazioni sopra, uno strato):

| Neuroni nascosti | Test loss dopo circa 1.500 giri o primo passaggio sotto 0,05 |
| --- | --- |
| 0 | circa 0,50, in tutte le prove |
| 1 | 0,40–0,44, in tutte le prove |
| 2 | 0,22–0,29, in tutte le prove |
| 3 | sotto 0,05 tra 76 e 110 giri in cinque prove su sei; la sesta è rimasta a 0,19 |
| 4 | sotto 0,05 tra 79 e 95 giri, in tutte le prove |

Con 3 neuroni la soglia non è garantita. Nella prova rimasta a 0,19, quattro azzeramenti con riavvio ne hanno portate tre sotto 0,05. Dì agli studenti di riprovare una volta prima di concludere. Non presentare «3» come regola: con 4 le prove sono riuscite tutte.

Spiega i termini mentre servono: pesi = numeri dei collegamenti; Epoch = giri sui punti per imparare; Training loss = errore su quei punti; Test loss = errore sui punti riservati alla prova. Indica una linea che cambia: si stanno modificando numeri, non istruzioni testuali. Usa «giri» solo per Epoch e «generazione» per Flappy.

**Disturbo (Noise) soltanto al proiettore:** cerchio, X1 e X2, Noise 50, quota di addestramento 10%, rete da 8 e 8; lascia le altre impostazioni comuni. Leggi Training loss e Test loss attorno a 200 Epoch, poi di nuovo attorno a 1.000. Chiedi se migliorare sui punti già visti assicura un miglioramento sugli altri. Nessun esito è promesso e non è una gara: non ripetere finché compare il peggioramento desiderato. **Se Training loss scende e Test loss sale:** la rete ha imparato anche il disturbo dei punti che ha visto e va peggio sui punti nuovi. **Se scendono tutte e due:** questa volta non è successo, ma per saperlo servono punti tenuti da parte. Vale anche per l'agente: lo proverete con richieste diverse dagli esempi.

### Flappy Learning · Un paio di minuti dal proiettore

Lo apri tu e gli studenti guardano. La pagina parte da sola: lascia una generazione a x1, poi accelera e guarda Generation e Score. Non fare previsioni e non chiedere agli studenti di aprirla.

Cosa dire: ci sono cinquanta uccellini, ognuno con una piccola rete che decide quando saltare. A ogni generazione si tengono le reti dei migliori, con piccole variazioni a caso e qualche rete nuova. Dopo qualche generazione gli uccellini volano a lungo. **Score conta passi della simulazione, non tubi.** La rete legge l'altezza dell'uccellino e quella del varco; gli ingressi sono ricavati dal codice, non mostrati sullo schermo. Il singolo uccellino non corregge i propri pesi durante il volo.

Nessuna promessa di un uccellino che «non muore più». Un volo lungo non è un volo infinito. Una frase basta per il confronto: in Playground i pesi si correggono guardando l'errore; in Flappy si copiano le reti migliori con modifiche a caso, e anche lì cambiano i pesi; in Copilot i pesi restano fermi e gli studenti cambiano il testo che il modello legge.

## Parte 4 · Copilot, richiesta, criterio, correzione

### 4A · Prima le biciclette, non le istruzioni P03

Mostra il caso del file del noleggio. Prima della risposta, fai scegliere per alzata di mano quale competenza serve alla richiesta mostrata, o se ne servono due. Usa le richieste già presenti nel file: non serve un personaggio aggiunto o un altro caso.

Poi mostra l'esecuzione reale, se disponibile, e i pezzi del testo che la guidano: regole, indice, competenze, gestione di due competenze o nessuna, stile. Una domanda per ottenere dati effettivamente necessari è un esito corretto. «Competenza usata» è una dichiarazione del modello, non una prova di instradamento software. Indice e competenze restano testo letto da Copilot.

Nella richiesta sui freni e sul rimborso, la regola 2 dell'esempio dà precedenza a «Non usare la bici» e alla proposta di cambio, anche se manca il numero della bici. Solo dopo viene la domanda sui dati mancanti. Una domanda sul rimborso senza la gestione iniziale del guasto non rispetta le istruzioni.

Non distribuire un agente P03 già scritto. L'obiettivo non è copiare le cinque sezioni e aspettare fino alla fine per vedere se funzionano.

### 4B · FERMO entra subito in prova

Fai aprire Blocco note e salvare `istruzioni_assistente_P03.txt`. Scrivono regole comuni e **solo FERMO**: durata con gli orari secondo le definizioni della fonte, dati mancanti, forma della risposta. Tu dai obiettivi e limiti, non una frase pronta da incollare. Non chiedono a Copilot di scrivere le istruzioni.

Mostra dove inserire, salvare e modificare le istruzioni **solo se controllato pre-aula**. Se la funzione non c'è, passa al primo messaggio in chat normale. Gli studenti incollano registro e regole degli indicatori in una nuova conversazione, poi inviano:

> **M1 · «Quanto è durato il fermo del 14 ottobre? Mostrami gli orari.»**

**Rivela il criterio dopo la risposta:** i due estremi devono essere fermo e ripresa effettiva della produzione, non la fine della sostituzione né la scomparsa dell'allarme. Durata e orari devono coincidere con la riga del fermo nella tavola automatica **Valori di riferimento del registro**. Proietta quei valori generati, senza ricopiarli in questa guida.

Prima alzata di mano collettiva P03: «La vostra risposta rispetta tutti questi criteri?» Il confronto non assegna punti: serve a vedere subito se modificare le istruzioni. Chi deve correggere aggiorna il testo e riprova M1 in una chat nuova con le stesse fonti.

Nella chat di M1 inviano poi:

> **M2 · «E quanti pezzi abbiamo perso?»**

**Soltanto dopo rivela:** manca la cadenza della ricetta, necessaria secondo le regole. È corretto chiederla o dichiarare che non si può calcolare il numero senza quel dato; non sceglierla né dedurla dai contatori del registro. Non fornire una cadenza inventata per chiudere il calcolo. Non occorre un'altra alzata di mano: leggono il criterio e correggono dove serve. Il seguito nella stessa chat serve a vedere se il limite viene rispettato anche quando la richiesta riprende un lavoro già avviato.

### 4C · Una seconda competenza e un indice proprio

Scelgono **ALLARMI oppure PASSAGGIO**, oltre a FERMO. Gli obiettivi e i documenti sono nella consegna; la formulazione delle istruzioni resta loro.

Aggiungono un indice che riconosca le richieste, la gestione di due competenze e delle richieste fuori indice, e **due esempi di stile scritti da loro**. Ogni competenza deve indicare fonti, informazioni necessarie e modo di rispondere quando le fonti non bastano. Non richiedere tutte e tre le competenze.

Dopo il salvataggio aggiornano Copilot e controllano che il testo sia stato trasferito intero. Se il campo è corto, eliminano ridondanze e accorciano gli esempi, senza perdere fonti, limiti e regole dell'indice. Il file non contiene una sezione «correzioni».

### 4D · Due casi originali, non un registro da compilare

Ciascuno inventa:

- un caso che incroci **entrambe le competenze**;
- un caso con dato mancante, fonte insufficiente o richiesta fuori indice.

Prima dell'invio decide che cosa conterà come corretto e trova sullo schermo i passi dei documenti utili al confronto. Può dirlo a voce; nessuna riga da compilare. Scrive poi il caso direttamente in Copilot, una chat nuova per caso.

Per **FERMO + ALLARMI** servono registro, regole degli indicatori e guida allarmi. Per **FERMO + PASSAGGIO** servono registro e regole. Nel secondo caso sceglie le fonti pertinenti senza aggiungere apposta il dato assente. Fai notare la differenza fra un dato non fornito al modello e un dato assente dalla fonte.

Dopo la risposta controlla contenuto e fonti, non soltanto il nome della competenza. Una risposta corretta al primo invio resta valida. Se tutti i casi funzionano, lo studente spiega quale regola ha reso possibile il comportamento e inventa un altro caso: non deve peggiorare le istruzioni né creare un errore artificiale.

### 4E · Ultimo collaudo e correzioni mirate

In una nuova chat fanno la richiesta seguente con il **registro**:

> **«Come si chiama il tecnico che ha cambiato il filtro?»**

**Rivela dopo:** il nome non è nel registro. È valido dichiararlo, chiedere la fonte che lo contenga oppure segnalare che la domanda è fuori ambito. Può essere valida anche una competenza diversa da quella prevista dal docente, purché l'agente non inventi un nome e rispetti i propri limiti.

Correggono solo dove occorre: regola, indice, competenza oppure documenti trasferiti. Aggiornano Copilot e riprovano in una nuova chat il caso interessato, compreso un caso originale se aveva mostrato un problema. Non chiedere di scrivere gli esiti.

Seconda e ultima alzata di mano collettiva P03: «Dopo i controlli e le eventuali correzioni, le risposte rispettano i criteri e le fonti?» Non distinguere chi è riuscito subito da chi ha corretto. Chiedi poi ad alcuni studenti, dal posto e guardando il loro schermo, di raccontare un caso e quale regola hanno mantenuto o cambiato. Non devono necessariamente raccontare un fallimento.

**Solo ora** pubblica l'esempio nella cartella `studenti/da_pubblicare_dopo_collaudo/`. È un testo da confrontare con il loro: non una soluzione garantita e non un motivo per sostituire istruzioni proprie già funzionanti.

### 4F · Lo stile non dimostra un addestramento

Riutilizzano una risposta **reale** dell'agente già ottenuta nel collaudo. Scelgono quella richiesta con i documenti esatti e mantengono le istruzioni che hanno prodotto la risposta scelta: se intanto le hanno cambiate, scelgono una prova ottenuta con la versione che confronteranno.

Fanno due nuovi invii in chat separate: stessa richiesta e stessi documenti con **Copilot normale, senza istruzioni proprie**, e poi ancora con **l'agente**. Hanno così due risposte reali dell'agente e una senza. Non sostituire una risposta con un esempio scritto a mano.

Confrontano ordine, lunghezza e parole. Tra le due dell'agente scelgono la preferita motivando a voce con due ragioni; una parità motivata è valida. Confrontano anche con Copilot normale. Non promettere differenze: due risposte possono coincidere, e una chat senza agente può avere già uno stile simile o risentire di personalizzazioni dell'account.

La conclusione dipende dall'operazione svolta, non dall'aspetto della risposta: qui hanno modificato **testo letto dal modello**, non i **pesi**. Preferenze umane come queste possono diventare dati per un vero addestramento; questa attività non lo esegue. Nessuna stima esatta degli esempi necessari e nessuna affermazione che una singola preferenza addestri Copilot.

## Fonti P03 e valori automatici

I tre testi sono inventati per l'esercitazione ITS MAKER: non sono fonti pubbliche né documenti industriali reali. Non modificare i fatti per rendere l'attività più facile o per ottenere un errore.

`docente/genera_materiali.py` ricava le tavole seguenti dagli originali. Sono il riferimento per controllare risposte e proiettare criteri numerici: qui non si trascrivono manualmente valori, calcoli o riepiloghi concorrenti.

### Valori di riferimento del registro

{{VALORI_REGISTRO}}

Per M1 usa la riga del fermo. La lettura di temperatura durante le prove dopo il cambio filtro **precede la ripartenza**, non la segue: l'assenza dell'allarme non significa ancora produzione ripresa. Non scambiare il controllo successivo alla ripartenza con le prove precedenti. Le righe originali distinguono esplicitamente queste fasi.

La cadenza, il nome del tecnico e il controllo dello scambiatore non sono documentati nel registro. La guida allarmi richiede il controllo dello scambiatore per la ripartenza: è una prescrizione della guida, non la prova che quell'intervento sia avvenuto nel caso. Il filtro intasato è il problema trovato; il registro non spiega perché si sia intasato. Non colmare i vuoti con una ricostruzione plausibile.

### Note che nominano il turno

{{NOTE_TURNO}}

Il registro non suddivide tutte le note per turno. Per PASSAGGIO, se il giorno o il turno non sono identificabili, l'agente chiede; se la selezione è già chiara, rende riconoscibili le note usate. Non trasformare le note sparse in una suddivisione dei turni inventata.

### Che cosa contiene la guida allarmi

{{VALORI_GUIDA}}

La guida non contiene significato, primo controllo e incaricato in modo identico per tutti gli allarmi. Dove manca un'informazione, dirlo è corretto. È ammesso citare un'informazione presente in un'altra parte della stessa voce, distinguendo il ruolo citato da un intervento effettivamente eseguito. Nessun consiglio aggiunto sulle protezioni, nessuna autorizzazione operativa: resta un'esercitazione testuale.

## Se manca il servizio o qualcosa non passa

Nella lezione del 4 novembre Copilot non ha risposto alle postazioni per circa 10 minuti. Un limite di richieste sull'indirizzo pubblico condiviso è un'ipotesi, non una causa accertata. Non aggiungere servizi online alternativi: niente HackMerlin, Prompt Airlines o Gandalf. Questa lezione non ha un modello locale di riserva.

| Situazione | Condotta |
| --- | --- |
| Agente non disponibile | Chat normale: prima il messaggio con le istruzioni dello studente, poi documenti e richiesta. Ripetere quel primo messaggio in ogni chat nuova. Non chiamarlo vera istruzione di sistema. In 4F confrontare con e senza quel messaggio. |
| Copilot non risponde | Prova a secco collettiva dal proiettore: stessa richiesta, fonti e istruzioni di uno studente; cercare quale regola copre il caso o quale manca. Correggere il testo, ma non presentare la discussione come risposta del modello né come prova della sua affidabilità. Il confronto di risposte reali non si può eseguire finché il servizio manca. |
| Messaggio troppo lungo | Usare soltanto i giorni completi necessari del registro, senza spezzare la sequenza del fermo. Conservare le regole e le altre fonti richieste dal caso. |
| Istruzioni tagliate o non aggiornate | Controllare il passaggio dal file, accorciare ridondanze e salvare di nuovo; non eliminare le regole sostanziali per fare entrare il testo. |
| Sito bloccato | Provare un altro browser; se non si apre, usare il proiettore dove disponibile. Non presentare schermate o testi preparati come esecuzioni avvenute in classe. |

## Che cosa sappiamo dei siti e della rete

Le osservazioni seguenti sono del **10 novembre 2026, postazione Linux del docente, rete non scolastica, Chromium senza interfaccia**. Non sono prove su Windows, sulla rete della scuola o su Copilot. Le nuove letture del codice e le esecuzioni dei siti non risolvono i controlli pre-aula.

### Misure e osservazioni già registrate

- **Transformer Explainer:** il messaggio della pagina parla di un modello da 600 MB; Generate è disattivato durante lo scarico. Le richieste HEAD ai 63 file `gpt2.onnx.part0`–`part62` hanno dato complessivamente **656.662.664 byte**, circa 626 MiB, comunemente arrotondati qui a 650 MB. Le aperture simultanee moltiplicano il traffico anche usando Examples. Sul primo esempio, la prima candidata aveva probabilità **97,66% a Temperature 0,2; 90,86% a 0,3; 54,67% a 0,8; 22,26% a 10**. I bersagli della consegna sono stati osservati, non garantiti per versioni future. Tutti e cinque gli esempi sono stati aperti anche con il download del modello bloccato; il comportamento a download finito resta da provare.
- **Playground, prove precedenti:** cerchio, X1/X2, rate 0,03, Tanh, Noise 0, 50% addestramento: senza strati nascosti Test loss **0,505 a 963 Epoch**; con 4 e 2 neuroni **0,001 a 902**; con uno strato da 2 **0,28 a 965**. Spirale con 4 e 2: **0,435 a 963**, senza scendere sotto 0,43. Cerchio con Noise 50 e 4 e 2: Training loss da **0,315** (circa 660) a **0,297** (circa 3.500); Test loss da **0,306** (circa 660) a **0,325** (circa 2.100), poi intorno a quel valore. Le reti 8,8,8 erano lente, circa 3 epoche al secondo: non è una misura delle postazioni scolastiche.
- **Playground, prove precedenti (10 novembre, letture a quel punto, non primo passaggio sotto 0,05):** con uno strato da 4, Test loss **0,014 a 1.085** e **0,009 a 1.072**, cambiando seme dei dati. Con 3 neuroni: **0,028 e 0,015 a 1.265**, ma circa **0,26** con un altro seme. Per la dimostrazione con Noise 50, 10% addestramento, 8 e 8: una prova passava da Training/Test **0,236/0,375** attorno a 172 Epoch a **0,066/0,556** attorno a 1.000; altre prove a 1.000 davano **0,174/0,374** e **0,116/0,545**. Sono esecuzioni, non un esito obbligatorio. Non trasferire alla spirale o a punti diversi una garanzia di successo sul cerchio.
- **Playground, prove dell'11 novembre (Chromium senza interfaccia, Linux, rete non scolastica):** cerchio, X1/X2, rate 0,03, Tanh, Noise 0, 50% addestramento, Batch size 10, uno strato nascosto, sei semi dei punti (0,1; 0,2; 0,3; 0,5; 0,7; 0,9), fermata a 1.500 Epoch o alla prima lettura sotto 0,05. 0 neuroni: 0,50–0,54. 1: 0,40–0,44. 2: 0,22–0,29. 3: sotto 0,05 a 76–110 Epoch in cinque semi su sei, 0,19 a 1.505 nel sesto; su quel seme quattro azzeramenti con riavvio hanno dato una prova ferma a 0,19 e tre sotto 0,05 (a 79, 107 e 107 Epoch). 4: sotto 0,05 a 79–95 Epoch in sei semi su sei. Il tempo reale è circa 25 secondi per 1.500 Epoch a questa velocità: non è una misura delle postazioni scolastiche. Pulsanti verificati sul sito: il **+** degli strati crea 2 neuroni; **−** e **+** sopra la colonna cambiano di uno; ogni cambio riporta Epoch a 0; il mouse su un neurone mostra il suo disegno nell'uscita; il mouse su una linea mostra «Weight is 0.35.» con «Click anywhere to edit». **Spirale** (seme 0,5; due prove 8,8 con semi 0,5 e 0,3): 4 e 2 → 0,50; 8 → 0,30; 8 e 4 → 0,20; 8 e 8 → sotto 0,05 a 1.293 e 1.222 Epoch. **Provato e scartato:** zero strati nascosti con X1² e X2² al posto di X1 e X2: sotto 0,001 a circa 20 Epoch in 4 semi su 6, ma 2 su 6 sono rimasti intorno a 1,0. Per questo e perché serve spiegare un ingrediente in più, non è nell'attività. La pagina aperta senza indirizzo parte con due strati da 4 e 2 neuroni.
- **Flappy Learning:** nessun errore rilevato. Le vecchie prove a MAX descrivevano voli lunghi nelle generazioni **40, 10 e circa 90**, senza una soglia finita: non dimostrano immortalità. Nelle nuove prove, al controllo Score era già oltre 10.000 nelle generazioni **26, 22, 45 e 44**, con rispettivamente **1, 2, 1 e 1** uccellini vivi. Sono letture osservate, non la prima generazione esatta del superamento e non una frequenza attesa per la classe.

### Chiamate di rete e privacy

| Sito | Osservato dalla postazione del docente | Limite da conservare |
| --- | --- | --- |
| Transformer Explainer | Oltre al sito: `fonts.googleapis.com`, `www.googletagmanager.com`, `cdn.jsdelivr.net`, `www.youtube.com`, `googleads.g.doubleclick.net`, `www.google.com`, `region1.google-analytics.com`, `huggingface.co`; una richiesta Analytics è fallita. | Non è stato provato il blocco selettivo di queste destinazioni. Gli esempi non evitano il download del modello. |
| Playground | Nessun errore in console; richieste a `playground.tensorflow.org`, `fonts.googleapis.com`, `fonts.gstatic.com`, `www.google-analytics.com`. | Il repository contiene un identificativo Analytics segnaposto; non sappiamo che cosa faccia il sito ospitato. Provare anche con blocchi della rete scolastica. |
| Flappy Learning | Nessun errore; chiamate a `fonts.googleapis.com` e `fonts.gstatic.com`. | Funzionamento con caratteri bloccati e velocità MAX scolastica non provati. |

Non sono state lette le informative sulla privacy. «Elabora nel browser» non significa «nessun dato viene raccolto». Riferimenti e licenze già letti sono in `docente/backup/fonti_online/LICENZE_E_FONTI.md`: Transformer Explainer e Flappy Learning **MIT**, TensorFlow Playground **Apache-2.0**. Si collegano i siti, non si redistribuisce codice.

Fonti tecniche del controllo del 10 novembre:

- Transformer Explainer: repository https://github.com/poloclub/transformer-explainer, commit `bfe50afba10b9b560b84143ee1107d977defa74f`; componenti `InputForm.svelte`, `Temperature.svelte`, `src/utils/data.ts` e `src/store/index.ts`. Licenza letta il 4 novembre.
- Playground: https://github.com/tensorflow/playground, `src/state.ts` e `src/playground.ts`, ramo master letto il 10 novembre senza fissare il commit; il sito ospitato può differire. Licenza letta il 10 novembre.
- Flappy: pagina pubblicata https://xviniette.github.io/FlappyLearning/, file `game.js` e `Neuroevolution.js` della versione pubblicata. Non confondere master con gh-pages: i controlli non coincidono. Licenza letta il 10 novembre.

## Chiusura dal proiettore

Chiedi una regola utile mostrata da un caso reale e la differenza fra cambiare istruzioni e addestrare pesi. Non raccogliere un'autovalutazione scritta. Gli studenti salvano il solo file delle istruzioni.

Dalla discussione puoi conservare tu le informazioni utili per le lezioni successive: funzioni Copilot effettivamente disponibili, limiti osservati, competenze scelte, regole motivate e problemi di rete. Non serve una tabella nominativa né un giro di controllo delle postazioni.
