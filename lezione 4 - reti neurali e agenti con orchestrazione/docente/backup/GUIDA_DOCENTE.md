# Guida docente · Lezione 4

**ITS MAKER Bologna · Lezione 4 · 12 novembre 2026 · Microsoft Copilot e giochi nel browser**

Documento riservato al docente.

## Che cosa cambia rispetto alla versione precedente

Decisione del 10 novembre 2026: la lezione 4 **non usa Unsloth Studio**. La macchina virtuale con Studio e il modello già installati la prepari tu a casa e la consegni agli studenti alla lezione 5 (18 novembre). Quello che serve di Studio per la lezione 5 è in `docente/backup/da_riprendere_lezione_5/NOTE_STUDIO_PER_LEZIONE_5.md`.

Altra decisione del 10 novembre 2026: in questa lezione **si lavora da soli**, ognuno sul proprio computer. Non ci sono scambi di postazione né controlli incrociati tra studenti: le prove le fa ognuno sul proprio agente, e la verifica la fai tu a voce.

La lezione 4 diventa: tre giochi nel browser per capire come impara un programma (parti 1–3), poi un agente di Microsoft Copilot con più competenze (parte 4). Il testo dell'agente, `istruzioni_assistente_P03.txt`, si potrà riprendere nella lezione 5 (System Prompt di Studio), se vorrai: non è stato provato che un modello piccolo segua istruzioni con indice e competenze.

## Che cosa si fa

Il caso è la P03, con tre testi: il registro del 13–15 ottobre, la guida agli allarmi e le regole degli indicatori. Sono quelli già usati nella lezione 3, ma la consegna non presume che ogni studente li ricordi. Il responsabile vuole un solo assistente che sappia fare tre lavori.

| Parte | Dove | Che cosa fanno gli studenti | Appunti personali |
| --- | --- | --- | --- |
| 1. Parola successiva | Browser, Transformer Explainer | Con gli esempi del menu Examples prevedono e poi osservano l'effetto della temperatura | `appunti_reti.txt` |
| 2. Una rete che impara | Browser, TensorFlow Playground | Criterio, prova, rete più piccola e rumore sul cerchio; poi la spirale | `appunti_reti.txt` |
| 3. Imparare dai risultati | Browser, Flappy Learning | Prevedono e osservano in quale generazione l'uccellino non muore più; ricaricano e confrontano | `appunti_reti.txt` |
| 4A. Esempio | Proiettore, Copilot | Guardano l'agente del noleggio di biciclette e annotano quali richieste toccano più competenze | `casi_di_prova.txt` |
| 4B. I tre lavori | Consegna | Leggono obiettivo e limiti dei tre lavori | |
| 4C. Progettare | Blocco note | Scrivono il proprio agente: due lavori su tre | `istruzioni_assistente_P03.txt` |
| 4D. Creare e provare | Copilot | Creano l'agente e provano una richiesta per competenza e una che ne tocca due | |
| 4E. Mettere alla prova | Copilot | Inventano casi critici per il proprio agente; scrivono prima che cosa si aspettano, poi che cosa succede | `casi_di_prova.txt` |
| 4F. Correzione | Copilot | Correggono dove emergono falle e riprovano | `istruzioni_assistente_P03.txt` |
| 4G. Istruzioni o addestramento | Copilot | Stessa richiesta con agente e senza; due risposte dell'agente a confronto; che cosa è cambiato e che cosa no | `appunti_reti.txt` |

I tre file `.txt` si scrivono con Blocco note e sono appunti personali: **non si consegna nulla** e non c'è un voto (decisione del 6 novembre 2026). Il voto ci sarà solo nel lavoro di gruppo della lezione 7. `istruzioni_assistente_P03.txt` contiene solo il testo dell'agente e, in fondo, «Correzioni dopo le prove».

### Come verifichi, a voce

Passi tra i banchi e chiedi di mostrare lo schermo e raccontare. Non segni punteggi. Con 22 studenti non puoi sentirli tutti a ogni momento: a ogni momento senti **8 studenti** diversi, a rotazione, così ognuno è sentito almeno una volta. Una domanda sola per momento, legata a ciò che lo studente ha sullo schermo.

1. **Fine della parte 3.** «Mostrate le previsioni in `appunti_reti.txt`: che cosa pensavate e che cosa avete visto?» Chi sbaglia la previsione non sbaglia: è quello che ci si aspetta di vedere.
2. **Durante la parte 4E.** «Mostrate un caso in `casi_di_prova.txt`: che cosa vi aspettavate, che cosa è successo, il dato c'è nel documento?»
3. **Fine della parte 4F.** «Quale regola avete cambiato e com'è andata la nuova prova?» Durante la 4C, a chi sta scrivendo: «Perché avete scritto questa regola dell'indice?»

Una tabella tua per sapere chi hai già sentito (non è una consegna degli studenti):

| Studente | Momento sentito | Annotazione |
| --- | --- | --- |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |
| 11 | | |
| 12 | | |
| 13 | | |
| 14 | | |
| 15 | | |
| 16 | | |
| 17 | | |
| 18 | | |
| 19 | | |
| 20 | | |
| 21 | | |
| 22 | | |

Nella chiusura due o tre studenti leggono ad alta voce, dal proprio schermo, la richiesta di un caso fallito, la risposta e la regola cambiata. Scrivi la regola alla lavagna.

## Prima di giovedì 12 novembre

### Da preparare a casa

1. **Agente di prova.** Con un account studente (o equivalente), se lo hai, crea un agente con il testo di `docente/ESEMPIO_DIMOSTRAZIONE_NOLEGGIO_BICICLETTE.txt` (la parte sotto la riga `----`) e prova le quattro richieste suggerite in fondo al file, ognuna in una nuova conversazione. Tieni la schermata pronta per il proiettore. Se non riesci a eseguirlo, mostra solo il testo (slide 11–13) e dichiara che non è stato eseguito. Controlla anche se la funzione per creare agenti offre di scrivere le istruzioni al posto dello studente: se sì, la consegna dice di non usarla.
2. **Esempio P03.** Prova `studenti/da_pubblicare_dopo_parte_4F/ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` allo stesso modo: una richiesta per competenza (con i documenti giusti incollati) e una che ne tocca due. Non è stato provato in Copilot: annota che cosa fa davvero. Non pubblicarlo prima della parte 4F.
3. **Pubblica su Teams** `studenti/ATTIVITA_LEZIONE4.docx`, `studenti/Registro_P03_13-15_ottobre_2026.txt`, `studenti/Guida_allarmi_P03.txt` e `studenti/Regole_indicatori_P03.txt`. Non serve un compito: non si consegna nulla. Gli ultimi tre sono testi da incollare in Copilot: controlla che si aprano con Blocco note.
4. **Siti.** Apri dal browser delle postazioni (con la rete della scuola) i tre siti e controlla la tabella qui sotto. Transformer Explainer scarica da solo circa 650 MB all'apertura (63 file, 656.662.664 byte misurati il 10 novembre): su una postazione con buona connessione non si nota, con 22 postazioni insieme sono circa 14 GB sulla rete della scuola. Se la prova con più postazioni dà problemi, falla tu al proiettore e gli studenti scrivono comunque previsione e osservazione.
5. **Macchina virtuale per la lezione 5.** Non fa parte di questa lezione; le note sono nel file indicato sopra.

### Controlli prima dell'aula

La colonna «Esito» resta da compilare in aula o prima. Nulla di quanto segue su Copilot è stato provato.

| Controllo | Che cosa verificare | Esito |
| --- | --- | --- |
| Transformer Explainer | La pagina scarica da sola circa 650 MB all'apertura. Controllare con la rete della scuola e più postazioni insieme quanto ci mette e se rallenta gli altri. Il 10 novembre è stato provato, durante lo scarico, solo l'esempio già presente nella pagina: controllare che anche gli altri esempi del menu Examples funzionino mentre il modello si scarica | |
| TensorFlow Playground | Si apre dalla rete della scuola. Il 10 novembre, dalla postazione del docente (rete non scolastica), la pagina ha chiamato anche `fonts.googleapis.com`, `fonts.gstatic.com` e `www.google-analytics.com`: controllare che il gioco funzioni anche se la rete blocca queste chiamate | |
| Flappy Learning | Si apre dalla rete della scuola. Chiama `fonts.googleapis.com` e `fonts.gstatic.com` per il carattere: controllare che funzioni anche se bloccate | |
| Agente in Copilot | Con l'account studente: la funzione per creare un agente esiste, c'è un campo per le istruzioni, si salva, e una nuova conversazione con l'agente riparte da quelle istruzioni. Documentazione Microsoft: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder (indirizzo preso da `RICERCA_ATTIVITA_ONLINE.md`, 4 novembre 2026; non riletto il 10 novembre). Non nominare comandi non verificati | |
| Creazione guidata | La funzione offre di scrivere le istruzioni da una descrizione a parole? Se sì, dire agli studenti di non usarla | |
| Lunghezza delle istruzioni | Quanto testo accetta il campo. L'esempio P03 ha circa 3.050 caratteri, quello del noleggio circa 2.500. Se il limite è più basso, la consegna dice di accorciare prima gli esempi di stile e le frasi ripetute, senza togliere l'indice né la regola per due competenze | |
| Documenti incollati | Con l'agente, un messaggio con il registro da solo (10.600 caratteri), con registro e regole degli indicatori (13.075) e con tutti e tre i testi (18.739) viene accettato; altrimenti gli studenti incollano i soli giorni del registro che servono (la consegna lo dice) | |
| Copilot senza agente | Parte 4G: in una conversazione nuova senza agente, lo stile degli esempi non compare. Se compare (memoria o personalizzazione dell'account), annotarlo e dirlo alla classe | |
| Classe intera | Comportamento con 22 account collegati insieme, ognuno con almeno 12 richieste lunghe: la lezione 3 ha avuto un blocco di circa 10 minuti, ipotesi limite di richieste per indirizzo pubblico condiviso | |
| Registro e documenti | I tre testi si incollano senza perdere caratteri accentati, righe o numeri | |

## Che cosa è stato verificato

Il 10 novembre 2026 da una postazione Linux del docente, **rete non scolastica**, con Chromium senza interfaccia. Non è Windows, non è la rete della scuola, non è Copilot.

- **Licenze, lette sul repository GitHub.** TensorFlow Playground: Apache-2.0 (la pagina dice: «You're free to use it in any way that follows our Apache License»). Flappy Learning (xviniette): MIT. Transformer Explainer: MIT, letto il 4 novembre. Non sono state lette informative sulla privacy di questi siti.
- **Transformer Explainer si apre.** La pagina dice «Try the examples while GPT-2 model is being downloaded (600MB)» e il pulsante Generate resta disattivato durante lo scarico. La dimensione reale, sommando i 63 file del modello (`gpt2.onnx.part0`–`part62`, misurati con richieste HEAD), è di 656.662.664 byte (circa 626 MiB). Con l'esempio già presente nella pagina, il cursore Temperature cambia le probabilità senza che il modello sia scaricato: sull'esempio «powers users to» la parola più probabile ha 97,66% a temperatura 0,2, 54,67% a 0,8 e 22,26% a 10. La pagina ha chiamato anche `fonts.googleapis.com`, `www.googletagmanager.com`, `cdn.jsdelivr.net`, `www.youtube.com`, `googleads.g.doubleclick.net`, `www.google.com`, `region1.google-analytics.com` e `huggingface.co`; una richiesta a Google Analytics è fallita. Non sono state lette informative sulla privacy: non dire agli studenti «nessun dato viene raccolto».
- **Playground si apre e funziona.** Nessun errore in console. Richieste verso `playground.tensorflow.org`, `fonts.googleapis.com`, `fonts.gstatic.com` e `www.google-analytics.com`. Nel repository `analytics.js` ha l'identificativo segnaposto «Add your own analytics ID here»: non è noto cosa faccia il sito ospitato. Non dire agli studenti «nessun dato viene raccolto».
- **Prove di Playground** (stessa impostazione di partenza della consegna: X1 e X2, tasso di apprendimento 0,03, Tanh, rumore 0, 50% dei punti per l'addestramento). Cerchio senza strati nascosti: Test loss resta 0,505 dopo 963 epoche. Cerchio con strati da 4 e 2 neuroni: Test loss 0,001 dopo 902 epoche. Cerchio con un solo strato da 2 neuroni: 0,28 dopo 965 epoche, non scende più. Spirale con 4 e 2 neuroni: Test loss 0,435 dopo 963 epoche, non scende sotto 0,43. Cerchio con rumore 50 e 4 e 2 neuroni: il Training loss scende da 0,315 (circa 660 epoche) a 0,297 (circa 3.500) mentre il Test loss sale da 0,306 (circa 660 epoche) a 0,325 (circa 2.100) e poi resta intorno a 0,325. Reti grandi (8,8,8) in Chromium senza interfaccia vanno lente (circa 3 epoche al secondo): sulle postazioni potrebbe essere diverso.
- **Flappy Learning si apre e funziona.** Nessun errore. Tre prove con velocità MAX: il punteggio ha cominciato a salire senza fermarsi alla generazione 40, 10 e circa 90. Il numero cambia da una prova all'altra.
- **Coerenza dei documenti.** Il limite di 65 °C del registro è quello della guida allarmi; l'allarme «temperatura dell'olio troppo alta» del 14 ottobre corrisponde a «Sovratemperatura olio idraulico»; il filtro dell'olio intasato è tra le cause elencate nella guida; il fermo dalle 14:20 alle 15:05 è di 45 minuti, come il registro scrive e come dà la definizione (dal FAULT al primo AVVIO). Nel registro non compaiono le parole FAULT e AVVIO. **La cadenza non è nel registro:** per i pezzi teorici persi l'agente deve chiederla. La guida dice che la pressa riparte dopo il raffreddamento dell'olio e il controllo dello scambiatore di calore; il registro non nomina lo scambiatore. Non è un errore del caso: se emerge nelle prove, la risposta giusta è «il registro non lo dice».

## Svolgimento

### Parte 1 · Browser, Transformer Explainer

Non spiegare prima: lascia che prevedano e poi guardino. Domande utili: che cosa succede alla barra più lunga quando la temperatura sale? Perché a temperatura bassa il modello sceglie quasi sempre la stessa parola? È un modello molto piccolo, in inglese: non giudicare la qualità delle frasi.

La consegna chiede di usare solo il menu Examples e di chiudere la scheda alla fine, per via dello scarico (vedi «Da preparare a casa», punto 4). Il legame con la parte 4: il modello sceglie la parola successiva leggendo il testo che sta prima, e le istruzioni dell'agente sono testo messo prima della richiesta. Dillo in una frase, senza spiegare come funziona un trasformatore. Se salti la parte 1, dì alla classe questa frase e che la scelta non è sempre la stessa, perché la consegna richiama la parte 1 nella parte 4 e nella 4G.

### Parte 2 · Browser, TensorFlow Playground

- Lo scopo è vedere che una rete impara cambiando i propri pesi con esempi, e che serve una struttura abbastanza grande. Non spiegare i termini tecnici di Playground: la consegna dà solo i pochi che servono (rete, addestramento, pesi, Test loss, Training loss, Epoch, Hidden layers).
- Tutti cominciano dal cerchio e alla fine ripetono con la spirale: con poche unità può non arrivare al criterio, ed è un risultato; si scrive fin dove si arriva.
- Le previsioni non vanno giudicate. Con zero strati e il cerchio la rete resta ferma intorno a 0,50 (vedi «Che cosa è stato verificato»): è utile se la previsione era diversa.
- **Il passo del rumore.** Che cosa dovrebbero vedere: con Noise a 50 e la rete da 4 e 2 neuroni il Training loss continua a scendere piano mentre il Test loss smette di scendere e sale un po': la rete impara anche il disturbo dei punti di addestramento. L'effetto è piccolo (nella prova del 10 novembre da 0,306 a 0,325) e potrebbe non vedersi chiaramente: anche questo è un risultato. Se la postazione è lenta, lascia andare la rete mentre lo studente scrive le altre note.
- Domanda utile: i punti usati per provare la rete sono gli stessi usati per addestrarla? Perché conta? È la stessa idea dei casi di prova nella parte 4: non devono essere gli esempi già usati nelle istruzioni.

### Parte 3 · Browser, Flappy Learning

- Il gioco non ha comandi se non la velocità. Il fare è prevedere, osservare, ricaricare e confrontare: la differenza tra le ricariche è il dato.
- Con x5 una prova richiede un po' di attesa; con MAX l'animazione scorre troppo veloce per leggere la generazione. Se una prova sembra non finire, ricaricare.
- Il punto da far dire a voce: in questo gioco nessuno mostra la risposta giusta, ma i risultati migliori restano. È un'analogia con l'addestramento da preferenze (si confrontano risposte e il modello viene spinto verso quelle preferite), che è un modo tra altri di addestrare uno stile; senza entrare nei dettagli dei modelli reali.
- **Verifica a voce.** Momento 1.

### Parte 4 · L'agente con più competenze

**4A. Esempio.** Mostra l'agente del noleggio di biciclette: prima le slide 11–13, poi, se funziona, una o due richieste eseguite. Fai notare solo le cinque parti e la riga «Competenza usata»: non spiegare le soluzioni dei casi complessi. Nell'esempio, la richiesta «La bici 12 ha i freni che non tengono. Mi ridate anche i soldi?» può portare l'agente a chiedere prima giorno e importo: anche questo è un comportamento corretto, perché la competenza RIMBORSO li richiede. Chiedi di annotare quali richieste toccano più competenze.

**4B. I tre lavori.** I limiti dei lavori sono quelli della consegna: sono obiettivi, non istruzioni da copiare. Non dare tu le istruzioni; se chiedono «come si scrive?», rimanda alle cinque parti della consegna.

**4C. Progettare.** È il cuore della lezione: ognuno scrive il proprio agente da solo, senza chiedere a Copilot di scriverlo. Lascia che sbaglino la struttura. Se un testo è troppo lungo per Copilot, la regola è la stessa che trovano nella consegna: accorciare prima gli esempi di stile e le frasi ripetute; non togliere né l'indice né la regola per le richieste che toccano due competenze. Passando, chiedi: «Perché avete scritto questa regola dell'indice?».

**4D. Creare e provare.** Mostra al proiettore dove si crea un agente e dove si incolla il testo (solo dopo aver verificato nel controllo «Agente in Copilot»). La riga «Competenza usata» è una dichiarazione dell'agente, non la prova che il programma abbia instradato la richiesta: dillo se qualcuno la tratta come prova. Se l'agente fa una domanda e gli studenti la scambiano per un errore, ricorda che mancava un dato.

**4E. Mettere alla prova.** Ognuno prova il proprio agente: nessun controllo incrociato. Il controllo viene dal fatto che gli studenti scrivono prima competenza e dato che si aspettano e solo dopo guardano la risposta, e che il campo «dato nel documento» li costringe a confrontarla con il testo. I **tipi** dei cinque casi sono nella consegna (richiesta fuori indice, su due competenze, a cui manca un dato, che chiede un dato che il documento non contiene, per la competenza provata meno); le richieste concrete le inventano loro. Per tuo orientamento, richieste che possono uscire, senza suggerirle: richiesta senza giorno, allarme non nominato, calcolo senza cadenza, richiesta che sposta la decisione al responsabile, due note che danno valori diversi. Una competenza giusta con un dato assente (per esempio un «primo controllo» per la sovratemperatura, che la guida non contiene) è `ERRORE`. **Verifica a voce.** Momento 2.

**4F. Correzione.** Alla fine pubblica `ESEMPIO_ISTRUZIONI_AGENTE_P03.txt` e chiedi di confrontarlo con le proprie: che cosa manca? Che cosa è inutile? Quale regola ha cambiato il comportamento? Non presentarlo come soluzione: non è stato provato in Copilot. Se la classe vede un comportamento diverso dal tuo, è un dato valido. **Verifica a voce.** Momento 3.

**4G. Istruzioni o addestramento.** Lo scopo non è che Copilot «impari» lo stile, ma che gli studenti vedano tre cose: gli esempi scritti nelle istruzioni cambiano la risposta dell'agente e solo quella (una conversazione normale non ne porta traccia, a meno che l'account abbia memoria o personalizzazione: vedi controllo «Copilot senza agente»); la stessa richiesta può dare risposte diverse anche con lo stesso agente (si ricollega alla parte 1: la scelta della parola successiva non è sempre la stessa); scegliere tra due risposte è il tipo di dato con cui si può addestrare uno stile. Risposta attesa alla domanda su quante scelte servirebbero: moltissime, migliaia di confronti; dentro il modello cambierebbero i pesi, come per gli uccellini scelti a ogni generazione. Un vero addestramento richiede molta potenza di calcolo e non si fa in aula. Non dichiarare cosa Copilot fa internamente.

### Chiusura

Ordine: confronto con l'esempio P03; due o tre studenti leggono un caso fallito, la risposta e la regola cambiata; poi le domande della slide 22, a voce. Risposte attese: (1) quando si addestra un programma i numeri dentro cambiano e il cambiamento resta; quando si scrivono istruzioni la conversazione cambia ma il modello è lo stesso, e se si apre una conversazione senza le istruzioni non c'è traccia; (2) la regola che ha dato risultati dipende dall'agente: accetta ogni risposta motivata che si appoggi a un caso; (3) un caso dove l'indice non prevedeva la richiesta o due competenze si pestavano i piedi.

## Valori di riferimento del registro

Ricavati dallo script del generatore dal testo di `Registro_P03_13-15_ottobre_2026.txt`.

{{VALORI_REGISTRO}}

Dati che il registro **non** contiene, utili per i tranelli: nome del tecnico, contatore del 15 ottobre, il motivo per cui il filtro si è intasato (il registro dice solo che era intasato), nome del responsabile del turno, cadenza della ricetta, controllo dello scambiatore.

### Note che nominano il turno

Per il lavoro «Passaggio di turno»: il registro non divide le note per turno. Queste sono le note che nominano il turno (ricavate dallo script).

{{NOTE_TURNO}}

Comportamento atteso dell'agente: chiede di quale giorno o turno si parla, oppure dichiara quali note ha usato.

## Guida allarmi: che cosa contiene

Per il lavoro «Spiegare un allarme» l'agente deve scrivere tre punti, ma la guida non li ha tutti per ogni allarme. La tabella è ricavata dallo script dal testo di `Guida_allarmi_P03.txt`.

{{VALORI_GUIDA}}

Dove la guida non indica un punto, la risposta attesa è che l'agente lo dica («La guida non lo indica») e non lo scriva da sé. Un'informazione presa da un'altra parte dello stesso allarme (per esempio il capoturno che autorizza la ripartenza dopo l'arresto di emergenza, o che verifica come si lavora vicino alla pressa dopo l'intervento della barriera) è corretta se è citata dalla guida. Per la barriera di sicurezza e l'arresto di emergenza vale la regola scritta nella guida: nessun consiglio che non sia già lì.

## Se Copilot non funziona

Il 4 novembre Copilot non ha risposto a nessuna postazione per circa 10 minuti. Senza Studio questa lezione non ha un modello locale di riserva: le parti 1–3 si fanno nel browser, la parte 4 ha questi rami.

| Situazione | Che cosa fare |
| --- | --- |
| L'agente non si crea o non accetta il testo | Conversazione normale: in ogni nuova conversazione incollare per prime le istruzioni, poi documenti e richiesta. Nella 4G si confrontano una conversazione che comincia con le istruzioni e una senza. Non è l'agente: lo scrivono nei casi |
| Copilot non risponde | Prova sulla carta: per ogni caso della 4E lo studente cerca nel proprio testo la riga dell'indice o della competenza che lo gestisce e la copia accanto al caso; se non c'è, è `ERRORE`. Poi scrive quale competenza e quale risposta |
| Il registro intero non viene accettato | Incollare solo i giorni che servono alla richiesta |
| Solo alcune postazioni hanno problemi | Chi ha problemi lavora sulla carta come sopra, fino a quando Copilot risponde |

Gli appunti sono gli stessi: cambia la nota su come sono stati ottenuti.

## Problemi probabili

| Sintomo | Possibile causa | Che cosa fare |
| --- | --- | --- |
| Il gioco non si apre | Rete della scuola o chiamate ai caratteri di Google bloccate | Usare un altro browser; se non serve, aspettare e passare al gioco successivo |
| Transformer Explainer lento o fermo | Scarico di circa 650 MB su una rete condivisa | Usare solo gli esempi, farla al proiettore o saltarla (vedi «Parte 1») |
| Playground molto lento con la rete grande | Postazione lenta | Chiedere di usare una rete piccola e di far andare meno epoche |
| Nessuna differenza tra le ricariche di Flappy | Nessuna | È un dato: chiedere di riprovare |
| L'agente scrive la riga «Competenza usata» ma risponde con un'altra competenza | L'indice è ambiguo | È un caso da registrare: va in `casi_di_prova.txt` come `ERRORE` |
| Il testo dell'agente viene tagliato | Limite del campo | Accorciare prima gli esempi di stile e le frasi ripetute; annotare cosa è stato tolto |

## Dati da raccogliere per le lezioni 5–7

Prendi nota tu, durante il giro tra i banchi e nella discussione finale. Annota: quanti agenti hanno funzionato in Copilot e con quale limite di lunghezza; quali lavori hanno scelto gli studenti; quali regole dell'indice sono state le più corrette; se Copilot ha avuto rallentamenti o blocchi; quanto ha scaricato Transformer Explainer e come ha retto la rete.
