# Guida docente · Lezione 4

**ITS MAKER Bologna · 12 novembre 2026 · Microsoft Copilot e siti nel browser**

Documento riservato al docente.

## La lezione da condurre

Ognuno lavora da solo. Non passi tra i banchi, non raccogli file e non fai compilare appunti o registri di controllo. Gli esiti si leggono sugli schermi; il confronto collettivo avviene dal proiettore. Nessun nuovo strumento, cruscotto o punteggio legato alla fortuna del modello.

L'ordine è **Transformer Explainer → TensorFlow Playground → Flappy Learning (solo dal proiettore) → agente per il noleggio Ruota Libera**. Si passa dalle probabilità di una parola a come una rete piccola impara cambiando numeri, poi a un altro modo di imparare (tenere le reti migliori), infine alla distinzione fra istruzioni e addestramento. I siti sono dimostrazioni di meccanismi diversi, non riproduzioni di Copilot. L'attività su cui si lavora a lungo è Playground: Flappy dura un paio di minuti.

Nella parte sul noleggio si prova subito un lavoro, prima di completare l'agente. Poi ciascuno aggiunge un secondo lavoro e inventa due casi critici. Il criterio è superare collaudi controllabili sui testi: un risultato corretto al primo invio e uno ottenuto dopo una correzione hanno lo stesso valore. Non occorre provocare un errore.

Si salva un solo file personale, `istruzioni_agente_noleggio.txt`, con **solo le istruzioni**: niente diario delle correzioni, richieste o esiti in fondo. Si usa Blocco note per scrivere un oggetto da provare, non per compilare una scheda. Nessuna consegna e nessun voto in questa lezione.

Unsloth Studio non si usa. Le note per preparare la macchina virtuale della lezione successiva restano in `docente/backup/da_riprendere_lezione_5/NOTE_STUDIO_PER_LEZIONE_5.md`. Non promettere che le istruzioni del noleggio funzioneranno allo stesso modo con un modello piccolo. Non presumere che gli studenti abbiano svolto attività specifiche nella lezione precedente.

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE4.docx` e i tre testi `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt`. Non pubblicare le cartelle di backup né l'esempio del noleggio all'inizio.
- Prepara la dimostrazione con `docente/ESEMPIO_DIMOSTRAZIONE_PIZZERIA.txt`: nelle istruzioni dell'agente va soltanto il testo **tra i due separatori**, non l'introduzione né le richieste suggerite. Prova in anticipo le richieste del file, ciascuna in una chat nuova. Se non puoi eseguirlo, mostra il testo dichiarando che non è una risposta del modello.
- Tieni riservato `studenti/da_pubblicare_dopo_collaudo/ESEMPIO_ISTRUZIONI_AGENTE_NOLEGGIO.txt` fino alla fine della parte **4E**. È un esempio da discutere, non una soluzione già collaudata in Copilot. Provalo prima dell'aula se l'account lo consente.
- Prepara il proiettore per mostrare **prima le richieste e soltanto dopo i criteri**. I valori del noleggio vengono dalle tavole automatiche in fondo a questa guida, non da numeri ricopiati a mano. La generazione è affidata a `docente/genera_materiali.py`, che legge gli originali in `docente/backup/fonti/`: conserva quei file intatti.
- Apri i siti dalla rete scolastica e controlla le impostazioni. Non aprire Transformer Explainer da tutte le postazioni in anticipo: usare Examples non ferma lo scarico del modello. Se la rete non regge, usa solo il proiettore.

### Controlli pre-aula

**Copilot non è stato provato con l'account studente.** La documentazione non sostituisce la prova sulla piattaforma della scuola. Mostra l'interfaccia agli studenti solo dopo il controllo; non dare per certi nomi di comandi o autorizzazioni.

| Controllo | Che cosa accertare | Esito |
| --- | --- | --- |
| Agente in Copilot | Creazione disponibile, campo delle istruzioni, salvataggio, modifica e riapertura in una chat nuova con le istruzioni aggiornate. Riferimento Microsoft: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder; indirizzo già registrato nella ricerca del corso, non riletto in questa riscrittura. | |
| Scrittura autonoma | Se la piattaforma propone di generare le istruzioni, mostra come evitarlo: gli studenti le scrivono loro. | |
| Limiti del testo | Prova istruzioni e messaggi con registro, regole e guida. Controlla che non si perdano righe nel copia-incolla e che le modifiche siano salvate. Non assumere un limite di caratteri non misurato. | |
| Nuove conversazioni | Verifica come aprire chat separate con l'agente e senza agente. Controlla eventuale memoria o personalizzazione dell'account: possono influire sul confronto finale. | |
| Transformer Explainer | Primo esempio, Top-k a 5, Probabilities leggibile, bersagli sopra 90% e sotto 30% con il solo Temperature. Prova dell'11 novembre, primo esempio, durante lo scarico del modello, cursore da 0,2 a 10 (parte da 0,8): 0,3 → 90,86%; 0,8 → 54,67%; 2 → 32,64%; 5 → 24,67%. Quindi **sotto il 30% si arriva solo oltre 2**: dillo se qualcuno si ferma. Controlla anche dopo lo scarico completo: non è stato provato. | |
| Playground | Impostazioni della consegna con **zero strati nascosti**; il **+** degli strati crea 2 neuroni, il **−** e il **+** sopra la colonna ne tolgono e aggiungono uno; azzeramento; visibilità di Test loss, Training loss ed Epoch; passando il mouse su un neurone il suo disegno compare nel riquadro grande dell'uscita; passando su una linea compare «Weight is…». Prova tu 0, 1, 2, 3 e 4 neuroni e guarda i disegni. Prepara anche il confronto sul disturbo al proiettore. | |
| Flappy Learning | Si apre e parte da solo; trova il comando della velocità. Lo usi tu dal proiettore: gli studenti non lo aprono. La velocità delle postazioni scolastiche non è misurata. | |
| Rete e classe | Apertura simultanea dei siti e richieste Copilot con gli account scolastici. L'indirizzo pubblico è condiviso; prepara il ramo senza servizio. | |
| Documenti | I tre testi si aprono in Blocco note e si incollano senza perdere accenti, righe e numeri. | |

## Parti 1–3 · Risultati visibili, senza scrittura

### Come sono costruite le slide 1–17 (e perché)

Riscritte l'11 novembre 2026 con gli stessi criteri della parte 4, e con schermate dei siti (catturate lo stesso giorno da un browser di prova su Linux, in una rete non scolastica): dove lo studente deve trovare un numero o un tasto, lo vede cerchiato.

| Slide | Passo | Che cosa si guarda o si fa |
| --- | --- | --- |
| 1–3 | Domanda iniziale e quadro | La stessa richiesta, la stessa risposta? Poi lo schema: oggi si vede come cambiano i pesi, poi si cambia il testo |
| 4–7 | Transformer Explainer | Frase da completare su un foglio; Temperature fra due bersagli; tre temperature a confronto; ritorno alla domanda iniziale |
| 8–13 | TensorFlow Playground | Previsione sui neuroni; dove si legge Test loss e Epoch; partenza da zero neuroni; un neurone in più alla volta; disegno del neurone; peso della linea |
| 14–15 | Disturbo (Noise) | Scommessa prima, nomi dei due errori dopo |
| 16 | Flappy Learning | Solo dal proiettore |
| 17 | Ponte | Da qui si cambia il testo, non i pesi |

- *Quadro prima dei dettagli* (slide 3): senza lo schema gli studenti non capiscono perché giocano con le reti. Ripetilo a voce in una frase.
- *Esempio del docente, poi prova loro* (slide 5, 10, 11): sul proiettore muovi tu Temperature una volta; per Playground fai girare tu la rete a zero neuroni (slide 10), poi tocca a loro.
- *Una domanda si chiude* (slide 2 e 7): la slide 7 richiama la domanda iniziale e dice che il modello «pesca» una parola con le probabilità (90 biglietti su 100 nel sacchetto); chiude dicendo che per un calcolo oggi non basta e che si controlleranno gli orari sul registro.
- *Prima il concreto, poi il nome* (slide 14–15): la scommessa viene prima di «Training loss» e «Test loss».
- *Una cosa per slide, con l'azione in chiaro* (slide 9–13): dove si legge il risultato (9); partenza da zero strati (10); neuroni da 1 a 4 con strato e neurone nominati nell'immagine (11); un'idea per slide.
- *Le immagini non danno il risultato.* La slide 9 mostra una rete a zero neuroni e Test loss intorno a 0,5; la slide 6 i valori del primo esempio a tre temperature (dati veri, riportati nella tabella dei controlli); la slide 15 evidenzia solo le due scritte a epoca 0. L'esito del disturbo si legge dal vivo.
- *Notazione del sito.* Epoch compare come «000,282» e «001,500»; Test loss come «0.501». È la notazione inglese: la slide 9 lo dice. Ripetilo a voce.
- Ricatturare le schermate se un sito cambia aspetto: sono in `docente/backup/immagini_slide/`.


### Transformer Explainer · Due bersagli sulle probabilità

Slide 4: dai il significato in italiano («La visualizzazione dei dati permette agli utenti di…») e fai scrivere su un foglio la parola che metterebbero. Non farne una prova di inglese; dai anche il significato delle candidate quando le mostri.

Slide 5: prima muovi tu Temperature una volta sul proiettore, poi tocca a loro. Prima di farlo, chiedi per alzata di mano se alzandola la barra più lunga salirà o scenderà. La sfida usa **il primo esempio, Top-k a 5**: prima barra sopra 90%, poi sotto 30%, cambiando soltanto Temperature (da 0,2 a 10). Niente conteggio di estrazioni, Sampling o Generate. Il criterio è leggibile nelle percentuali; non serve che la parola estratta cambi ogni volta. Slide 6: il confronto fra tre temperature (valori veri del primo esempio).

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

**Disturbo (Noise) soltanto al proiettore** (slide 14–15): cerchio, X1 e X2, Noise 50, quota di addestramento 10%, rete da 8 e 8; lascia le altre impostazioni comuni. Prima la scommessa (slide 14), poi leggi Training loss e Test loss attorno a 200 Epoch e di nuovo attorno a 1.000 (slide 15). Chiedi se migliorare sui punti già visti assicura un miglioramento sugli altri. Nessun esito è promesso e non è una gara: non ripetere finché compare il peggioramento desiderato. **Se Training loss scende e Test loss sale:** la rete ha imparato anche il disturbo dei punti che ha visto e va peggio sui punti nuovi. **Se scendono tutte e due:** questa volta non è successo, ma per saperlo servono punti tenuti da parte. Vale anche per l'agente: lo proverete con richieste diverse dagli esempi. Nella prova dell'11 novembre (8 e 8 neuroni, Noise 50, 10% di punti) a circa 900 Epoch Training loss era 0,076 e Test loss 0,539: è un'esecuzione, non un esito garantito.

### Flappy Learning · Un paio di minuti dal proiettore

Lo apri tu e gli studenti guardano. La pagina parte da sola: lascia una generazione a x1, poi accelera e guarda Generation e Score. Non fare previsioni e non chiedere agli studenti di aprirla.

Cosa dire: ci sono cinquanta uccellini, ognuno con una piccola rete che decide quando saltare. A ogni generazione si tengono le reti dei migliori, con piccole variazioni a caso e qualche rete nuova. Dopo qualche generazione gli uccellini volano a lungo. **Score conta passi della simulazione, non tubi.** La rete legge l'altezza dell'uccellino e quella del varco; gli ingressi sono ricavati dal codice, non mostrati sullo schermo. Il singolo uccellino non corregge i propri pesi durante il volo.

Nessuna promessa di un uccellino che «non muore più». Un volo lungo non è un volo infinito. Una frase basta per il confronto: in Playground i pesi si correggono guardando l'errore; in Flappy si copiano le reti migliori con modifiche a caso, e anche lì cambiano i pesi; in Copilot i pesi restano fermi e gli studenti cambiano il testo che il modello legge.

## Parte 4 · Copilot, richiesta, criterio, correzione

**Il filo da tenere:** nelle reti cambiavano i pesi; adesso gli studenti cambiano il testo che Copilot legge. Lo hai annunciato alla slide 3; dillo di nuovo alla slide 17 e riprendilo alla slide 46. In mezzo ciascuna slide è un passo della stessa costruzione: un agente per il noleggio Ruota Libera che calcola da quanto tempo una bici è fuori servizio e fa un secondo lavoro.

**Come è costruita (e perché).** La parte 4 segue alcune indicazioni dalla ricerca sull'insegnamento, scelte perché gli studenti sono alle prime armi:

- *Prima il quadro d'insieme* (slide 18–19): che cosa legge Copilot, che cosa si costruisce. Una slide sola, prima dei dettagli.
- *Prima l'esempio, poi il nome* (slide 20–23): le frasi vere delle istruzioni della pizzeria si vedono prima che si diano i nomi delle parti. Poi si passa al noleggio con la stessa tabella.
- *Esempio svolto, poi esercizio simile* (slide 25–26, poi 31): la bici 5 è calcolata davanti agli studenti, la bici 12 la calcola il loro agente. Lo stesso vale per la scrittura: il lavoro RECLAMO della pizzeria sta accanto alle domande del lavoro FUORI SERVIZIO (slide 28).
- *Esercizio a metà* (slide 28): le quattro righe del lavoro sono date come domande, non come risposte. Per i casi da inventare (slide 40) ci sono esempi della pizzeria.
- *Un'idea alla volta, con l'azione in chiaro* (tutte le slide): programma da aprire, che cosa scrivere, in quale ordine.
- *Controlli frequenti* (alzate di mano, previsioni prima di inviare): servono a far vedere subito se ci si è persi.

Parole in aula e nomi tecnici: in aula si dice **lavoro** (nome tecnico: competenza), **elenco delle richieste** (indice) e **lavoro usato**. «Orchestrare» non compare nelle slide né nella consegna: scegliere quale lavoro usare e in che ordine è già nell'elenco. Se vuoi dargli il nome, dillo a voce solo alla fine.

| Slide | Passo | Che cosa fanno gli studenti |
| --- | --- | --- |
| 17–19 | Dalla rete al testo; che cosa legge Copilot; che cosa si costruisce | Ascoltano il percorso: esempio, primo lavoro, secondo lavoro, prove, confronto |
| 20–23 | 4A · La pizzeria | Guardano il messaggio e le frasi delle istruzioni, poi la stessa tabella per il noleggio |
| 24 | Programmi | Aprono Teams, Blocco note e Copilot |
| 25–35 | 4B · Primo lavoro: fuori servizio | Leggono due appunti ed esempio svolto, scrivono le regole e le quattro righe, provano le due richieste |
| 36–38 | 4C · Secondo lavoro, elenco, stile | Aggiungono GUASTI o PASSAGGIO, l'elenco delle richieste e due esempi di stile |
| 39–40 | 4D · Due richieste vostre | Inventano e provano una richiesta con tutti e due i lavori e una scomoda |
| 41–44 | 4E · Ultima richiesta | Provano l'ultima richiesta, correggono, confrontano con l'esempio del docente |
| 45–47 | 4F · Testo o pesi | Confrontano tre risposte e concludono |

### 4A · Prima la pizzeria, non le istruzioni del noleggio

**Perché la pizzeria.** Gli studenti devono vedere com'è fatto un agente con più lavori **prima** di scrivere il proprio, ma non si può mostrare un esempio sul noleggio: sarebbe la soluzione dell'esercizio. La pizzeria ha la stessa struttura su un caso diverso. Dillo in una riga: «Non è il vostro noleggio: serve a vedere com'è fatto. Il vostro avrà le stesse parti.» Poi riporta subito al noleggio con la slide 23.

**Come condurlo.** Slide 20: mostra il messaggio «La pizza è arrivata fredda e dopo un'ora. Mi ridate anche i soldi?» e fai scegliere per alzata di mano: prima la pizza fredda o i soldi? Slide 21: le frasi delle istruzioni sono estratti del file `ESEMPIO_DIMOSTRAZIONE_PIZZERIA.txt`: restano uguali al file. Slide 22: invia il messaggio all'agente, se disponibile, e chiedi quale riga ha guidato la risposta. Usa le altre richieste del file se ti servono: non serve un personaggio aggiunto o un altro caso.

**Termini.** Agente (slide 18), parti delle istruzioni e lavoro (slide 21) compaiono con una definizione in una riga ciascuno, dopo averli visti nell'esempio. Non aggiungerne altri a voce. «Lavoro» è soltanto «una parte delle istruzioni con i suoi dati e le sue regole».

Nella richiesta sulla pizza fredda e sul rimborso, la regola 2 dell'esempio dà precedenza a «Mi dispiace» e alla proposta di rifare la pizza, anche se manca il numero dell'ordine. Solo dopo viene la domanda sui dati mancanti. Una domanda sul rimborso senza la gestione iniziale del reclamo non rispetta le istruzioni. Una domanda per ottenere dati effettivamente necessari è un esito corretto. «Lavoro usato» è una dichiarazione del modello, non una prova di instradamento software. L'elenco e i lavori restano testo letto da Copilot.

Non distribuire un agente del noleggio già scritto. L'obiettivo non è copiare le sezioni e aspettare fino alla fine per vedere se funzionano.

### 4B · FUORI SERVIZIO entra subito in prova

Slide 25–26: nel registro mostra due appunti della bici 5 (sono estratti del registro) e il conto svolto: 12:35 → 13:00, 25 minuti. È l'esempio svolto; la bici 5 non è la domanda della classe. Dì la regola in una riga: dal momento in cui la bici è tolta dal noleggio a quando torna in fila.

Slide 27–28: fai aprire Blocco note e salvare `istruzioni_agente_noleggio.txt` (la slide 27 lo dice, con l'inizio delle regole della pizzeria). Scrivono prima le regole per tutti i casi, poi le quattro righe di **FUORI SERVIZIO**: quando si usa, dati che servono, regole del lavoro, come risponde. La tabella della slide 28 mette accanto il lavoro RECLAMO della pizzeria (in breve) e le domande per il loro lavoro: le domande, non le risposte. Tu dai obiettivi e limiti, non una frase pronta da incollare. Non chiedono a Copilot di scrivere le istruzioni. La prima riga della risposta è «Lavoro usato:» seguita dal nome.

Slide 29: mostra dove inserire, salvare e modificare le istruzioni **solo se controllato pre-aula**. Non nominare pulsanti o menu non verificati. Se la funzione non c'è, gli studenti usano la riga della slide: in ogni nuova conversazione incollano prima le proprie istruzioni, poi testi e richiesta (vedi la tabella «Se manca il servizio»). Alla slide 30 mostra la struttura del messaggio: registro, poi regole del noleggio, in fondo la domanda, **in un solo messaggio**. Se inviano prima i testi da soli, Copilot risponde ai testi e la prova si confonde. Alla slide 31 inviano:

> **M1 · «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.»**

**Rivela il criterio dopo la risposta (slide 32):** i due estremi devono essere il momento in cui la bici viene tolta dal noleggio e il momento in cui è di nuovo disponibile. Non valgono la segnalazione, il cambio della bici al cliente, la fine della riparazione né la prova del meccanico. Durata e orari devono coincidere con la riga «Minuti fuori servizio, bici 12» nella tavola automatica **Valori di riferimento del registro**. Proietta quei valori generati, senza ricopiarli in questa guida.

Prima alzata di mano collettiva: «La vostra risposta rispetta tutti questi criteri?» Il confronto non assegna punti: serve a vedere subito se modificare le istruzioni. Chi deve correggere aggiorna il testo e riprova M1 in una chat nuova con gli stessi testi.

Nella chat di M1 inviano poi (slide 33):

> **M2 · «E quanto dobbiamo rimborsare al cliente?»**

**Soltanto dopo rivela (slide 34–35):** il rimborso si calcola sui **minuti senza bici** del cliente, dalla segnalazione al cambio (slide 34), non sui minuti fuori servizio della bici. Serve inoltre il tipo di noleggio, a ore o per la giornata, che non è nel registro (slide 35): è corretto chiederlo o dichiarare che non si può calcolare il rimborso senza quel dato; non sceglierlo né dedurlo. Se lo studente risponde «a ore» o «per la giornata», il risultato deve coincidere con la riga corrispondente della tavola. Non occorre un'altra alzata di mano: leggono il criterio e correggono dove serve. Il seguito nella stessa chat serve a vedere se il limite viene rispettato anche quando la richiesta riprende un lavoro già avviato.

### 4C · Un secondo lavoro e un elenco delle richieste proprio

Scelgono **GUASTI oppure PASSAGGIO**, oltre a FUORI SERVIZIO (slide 36). Gli obiettivi e i documenti sono nella consegna; la formulazione delle istruzioni resta loro. Lo scrivono con le stesse quattro righe del primo lavoro (quando si usa, dati che servono, regole del lavoro, come risponde).

Slide 37: la tabella mostra l'elenco della pizzeria; loro scrivono quello del noleggio, la gestione di due lavori insieme e delle richieste che non sono un lavoro dell'agente. Slide 38: **due esempi di stile scritti da loro**, con un esempio della pizzeria. Ogni lavoro deve indicare i testi da usare, le informazioni necessarie e come rispondere quando i testi non bastano. Non richiedere tutti e tre i lavori.

Dopo il salvataggio aggiornano Copilot e controllano che il testo sia stato trasferito intero. Se il campo è corto, eliminano ridondanze e accorciano gli esempi, senza perdere testi, limiti e regole dell'elenco. Il file non contiene una sezione «correzioni».

### 4D · Due casi originali, non un registro da compilare

Slide 39–40 (la 40 mostra tre esempi della pizzeria, uno per tipo). Ciascuno inventa:

- un caso che usi **tutti e due i lavori**;
- un caso con dato mancante, testo insufficiente o lavoro che l'agente non ha.

Prima dell'invio decide che cosa conterà come corretto e trova sullo schermo i passi dei documenti utili al confronto. Può dirlo a voce; nessuna riga da compilare. Scrive poi il caso direttamente in Copilot, una chat nuova per caso, in un solo messaggio con i documenti e in fondo la richiesta.

Per **FUORI SERVIZIO + GUASTI** servono registro, regole del noleggio e guida ai guasti. Per **FUORI SERVIZIO + PASSAGGIO** servono registro e regole. Nel secondo caso sceglie i testi pertinenti senza aggiungere apposta il dato assente. Fai notare la differenza fra un dato non fornito al modello e un dato assente dal testo.

Dopo la risposta controlla contenuto e testi, non soltanto il nome del lavoro. Una risposta corretta al primo invio resta valida. Se tutti i casi funzionano, lo studente spiega quale regola ha reso possibile il comportamento e inventa un altro caso: non deve peggiorare le istruzioni né creare un errore artificiale.

### 4E · Ultimo collaudo e correzioni mirate

Slide 41. In una nuova chat, in un solo messaggio, fanno la richiesta seguente con il **registro**:

> **«Come si chiama il meccanico che ha cambiato le pastiglie?»**

**Rivela dopo (slide 42):** il nome non è nel registro, che dice solo «il meccanico del negozio». È valido dichiararlo, chiedere il testo che lo contenga oppure segnalare che la domanda non è un lavoro dell'agente. Può essere valido anche un lavoro diverso da quello previsto dal docente, purché l'agente non inventi un nome e rispetti i propri limiti.

Correggono solo dove occorre: regola, elenco, lavoro oppure documenti trasferiti. Aggiornano Copilot e riprovano in una nuova chat il caso interessato, compreso un caso originale se aveva mostrato un problema. Non chiedere di scrivere gli esiti.

Seconda e ultima alzata di mano collettiva: «Dopo i controlli e le eventuali correzioni, le risposte rispettano i criteri e i testi?» Non distinguere chi è riuscito subito da chi ha corretto. Chiedi poi ad alcuni studenti, dal posto e guardando il loro schermo, di raccontare un caso e quale regola hanno mantenuto o cambiato. Non devono necessariamente raccontare un fallimento.

**Solo ora** (slide 44; la 43 è «Correggete e riprovate») pubblica su Teams l'esempio `studenti/da_pubblicare_dopo_collaudo/ESEMPIO_ISTRUZIONI_AGENTE_NOLEGGIO.txt` e proiettalo. È un testo da confrontare con il loro: non una soluzione garantita e non un motivo per sostituire istruzioni proprie già funzionanti. Indica tre punti: la regola 2 (dati mancanti: una sola domanda), la riga dell'elenco per due lavori insieme (quale prima), la riga di tutte le altre richieste. Per ciascuno chiedi per alzata di mano chi ha una regola che fa la stessa cosa. Chi non ce l'ha la scrive con parole proprie: non si copia l'esempio. Le tre domande scritte in cima al file («Che cosa avete scritto voi e non c'è qui? …») sono quelle da fare.

### 4F · Lo stile non dimostra un addestramento

Slide 45–47. Riutilizzano una risposta **reale** dell'agente già ottenuta nel collaudo. Scelgono quella richiesta con i documenti esatti e mantengono le istruzioni che hanno prodotto la risposta scelta. Chi ha cambiato le istruzioni dopo l'esempio (4E) usa la prova rifatta alla fine della 4E: non deve tornare a una versione precedente.

Fanno due nuovi invii in chat separate: stessa richiesta e stessi documenti con **Copilot normale, senza istruzioni proprie**, e poi ancora con **l'agente**. Hanno così due risposte reali dell'agente e una senza. Non sostituire una risposta con un esempio scritto a mano.

Confrontano ordine, lunghezza e parole. Tra le due dell'agente scelgono la preferita motivando a voce con due ragioni; una parità motivata è valida. Confrontano anche con Copilot normale. Non promettere differenze: due risposte possono coincidere, e una chat senza agente può avere già uno stile simile o risentire di personalizzazioni dell'account.

La conclusione dipende dall'operazione svolta, non dall'aspetto della risposta: qui hanno modificato **testo letto dal modello**, non i **pesi**. Preferenze umane come queste possono diventare dati per un vero addestramento; questa attività non lo esegue. Nessuna stima esatta degli esempi necessari e nessuna affermazione che una singola preferenza addestri Copilot.

## Fonti del noleggio e valori automatici

I tre testi sono inventati per l'esercitazione ITS MAKER: non sono fonti pubbliche né documenti di un negozio reale. Non modificare i fatti per rendere l'attività più facile o per ottenere un errore.

`docente/genera_materiali.py` ricava le tavole seguenti dagli originali. Sono il riferimento per controllare risposte e proiettare criteri numerici: qui non si trascrivono manualmente valori, calcoli o riepiloghi concorrenti.

### Valori di riferimento del registro

{{VALORI_REGISTRO}}

Per M1 usa la riga dei minuti fuori servizio della bici 12. La prova del meccanico (11:40) **precede** il rientro in fila (11:50): una prova riuscita non significa bici disponibile. Il cambio della bici al cliente (11:10) non chiude il fuori servizio della bici 12. Non scambiare il fuori servizio della bici 12 con quello della bici 5, né con i minuti senza bici del cliente.

Il tipo di noleggio, gli importi pagati e il nome del meccanico non sono documentati nel registro. Le pastiglie consumate sono il problema trovato; il registro non spiega perché si siano consumate. La catena della bici 9 è un aggiustamento al banco, non un fuori servizio: le regole lo dicono. Non colmare i vuoti con una ricostruzione plausibile.

### Note che nominano il turno

{{NOTE_TURNO}}

Il registro non suddivide tutte le note per turno. Per PASSAGGIO, se il giorno o il turno non sono identificabili, l'agente chiede; se la selezione è già chiara, rende riconoscibili le note usate. Non trasformare le note sparse in una suddivisione dei turni inventata.

### Che cosa contiene la guida ai guasti

{{VALORI_GUIDA}}

La guida non contiene significato, primo controllo e incaricato in modo identico per tutti i guasti. Dove manca un'informazione, dirlo è corretto. È ammesso citare un'informazione presente in un'altra parte della stessa voce, distinguendo il ruolo citato da un intervento effettivamente eseguito. Per freni e sterzo vale la regola obbligatoria della guida: nessun consiglio aggiunto, nessuna autorizzazione a far uscire una bici dal negozio. Resta un'esercitazione testuale.

## Se manca il servizio o qualcosa non passa

Nella lezione del 4 novembre Copilot non ha risposto alle postazioni per circa 10 minuti. Un limite di richieste sull'indirizzo pubblico condiviso è un'ipotesi, non una causa accertata. Non aggiungere servizi online alternativi: niente HackMerlin, Prompt Airlines o Gandalf. Questa lezione non ha un modello locale di riserva. Non c'è più una slide per questi casi: la conduci a voce con la tabella e con la sezione «Se Copilot non è disponibile» della consegna.

| Situazione | Condotta |
| --- | --- |
| Agente non disponibile | Chat normale: prima il messaggio con le istruzioni dello studente, poi documenti e richiesta. Ripetere quel primo messaggio in ogni chat nuova. Non chiamarlo vera istruzione di sistema. In 4F confrontare con e senza quel messaggio. |
| Copilot non risponde | Prova a secco collettiva dal proiettore: stessa richiesta, testi e istruzioni di uno studente; cercare quale regola copre il caso o quale manca. Correggere il testo, ma non presentare la discussione come risposta del modello né come prova della sua affidabilità. Il confronto di risposte reali non si può eseguire finché il servizio manca. |
| Messaggio troppo lungo | Usare soltanto i giorni completi necessari del registro, senza spezzare la sequenza del fuori servizio. Conservare le regole e gli altri testi richiesti dal caso. |
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

Dalla discussione puoi conservare tu le informazioni utili per le lezioni successive: funzioni Copilot effettivamente disponibili, limiti osservati, lavori scelti, regole motivate e problemi di rete. Non serve una tabella nominativa né un giro di controllo delle postazioni.
