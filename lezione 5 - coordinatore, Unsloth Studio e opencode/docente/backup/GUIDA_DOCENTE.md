# Guida docente · Lezione 5

**ITS MAKER Bologna · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

Documento riservato al docente. Struttura e motivi sono in `docente/backup/PIANO_LEZIONE5.md`; qui c'è ciò che serve per condurre.

## La lezione da condurre

Si riparte dall'agente Ruota Libera della lezione 4. Nella **parte 1**, in Copilot e ognuno sul proprio computer, il file `istruzioni_agente_noleggio.txt` riceve tre novità: il piano mostrato prima della risposta, il rimborso come lavoro a sé e il controllo che cita la riga di ogni numero. Nelle **parti 2 e 3** si lavora in gruppo, quattro o cinque persone per ogni computer virtuale con Unsloth Studio e opencode: lo stesso testo letto da un modello piccolo e locale, poi un programma (opencode) che apre i file e chiede il permesso, con un modello in rete (Big Pickle).

Parole: in aula si dice **coordinatore** per chi sceglie i lavori, decide l'ordine, si ferma a chiedere e controlla. «Orchestratore» lo dici tu alla fine, a voce. Nomi dei prodotti (Plan, Build, allow, ask, deny) si lasciano come compaiono nel programma e si spiegano la prima volta.

Come nella lezione 4: niente giro tra i banchi, niente file da consegnare, niente voto. I risultati si leggono sugli schermi e dal proiettore; i criteri si mostrano dopo la prova. Una prova riuscita subito vale quanto una riuscita dopo una correzione. Nessuna attività si basa sull'errore del modello.

Non dichiarare provato ciò che non lo è: nulla di questa lezione è stato provato in Copilot con l'account studente né su VMware. La parte 3 è stata provata il 15 novembre con Big Pickle su una copia della VM aperta con QEMU (vedi «Prova nella VM»).

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE5.docx` e i tre testi `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt` (copie della lezione 4: stessi fatti). Non pubblicare le cartelle di backup.
- `studenti/da_pubblicare_a_chi_non_ha_il_file/ISTRUZIONI_DI_PARTENZA_NOLEGGIO.txt`: lo dai solo a chi non ha il proprio `istruzioni_agente_noleggio.txt`. È il testo mostrato nella lezione 4 con un solo esempio cambiato (la bici 5), non una soluzione collaudata. Chi lo riceve aggiunge comunque piano, rimborso e controllo. Il suo «Esempio 1» usa la bici 5, non la bici 12, per non dare la risposta alla richiesta della slide 2.
- Dimostrazione: `docente/ESEMPIO_DIMOSTRAZIONE_PIZZERIA_L5.txt`. Nelle istruzioni dell'agente va solo il testo **tra i due separatori**. Provalo prima con le richieste in fondo al file, ciascuna in una chat nuova. Se non puoi, mostra il testo dichiarando che non è una risposta del modello. Le risposte non sono scritte nel file: sono quelle del modello.
- Sulla VM, nella cartella `Documenti\noleggio`: i tre testi (da questa cartella `studenti/`) e `docente/MODELLI_OPENCODE/opencode.jsonc` nella stessa cartella. Le slide e la consegna dicono «la cartella `noleggio`» o «Documenti › noleggio»: controlla il percorso e che le slide 26 e 32 trovino la cartella presente.
- Una chiavetta per gruppo (5 o 6), per portare il file dell'autore sul computer del gruppo (slide 26). Prova prima come si collega la chiavetta alla VM invece che al PC che la ospita, e prepara il gesto esatto da dire a voce.
- Proiettore: **prima le richieste, dopo i criteri**. I valori vengono dalle tavole in fondo, non da numeri ricopiati.

### Organizzazione delle VM (da decidere prima)

Una VM ogni quattro o cinque postazioni. La VM preparata e lo script sono stati provati solo su una copia aperta con QEMU: il resto della sequenza è quella che propongo, da correggere dopo le verifiche in VMware.

| Quando | Che cosa |
| --- | --- |
| Prima dell'aula | Gruppi decisi per postazione. VM copiate e accese, Unsloth Studio aperto con il modello **già caricato** (Context Length 8192, Search spento). Nella cartella `noleggio`: i tre testi e `opencode.jsonc`; sul desktop il collegamento «opencode»: li crea lo script `docente/PREPARA_VM_LEZIONE5.ps1` (vedi «TODO prima dell'aula») |
| Parte 1 | Sul PC che ospita la VM solo la finestra di Copilot e Blocco note: la memoria è il controllo più incerto. Se una VM manca, il gruppo si unisce a un altro |
| Inizio parte 2 | Gli studenti si spostano alla postazione con la VM. Mostri Studio con il modello già caricato; non si carica in aula |
| Inizio parte 3 | Si avvia opencode dal collegamento sul desktop |

### Controlli pre-aula

Le righe con «Provato su QEMU» hanno un esito del 15 novembre; nessuno è stato eseguito su VMware né con Copilot e l'account studente.

| Controllo | Che cosa accertare | Se fallisce | Esito |
| --- | --- | --- | --- |
| Copilot, agente | Come in lezione 4: salvare, riaprire, modificare le istruzioni | Chat normale con le istruzioni nel primo messaggio, non vere istruzioni di sistema | |
| Piano e controllo in Copilot | La pizzeria della lezione 5, con la richiesta suggerita: si ferma dopo il piano? Cita le righe? | Raccontalo come è: un modello non segue sempre una regola, e la prova passa dalla correzione del testo | |
| Tempo alla prima parola, VM | Registro, regole e istruzioni nel messaggio a Qwen (circa 3,5–4k token): la parte 2. Su QEMU la prima risposta di un testo lungo ha richiesto minuti: misurare su VMware | Una sola prova per gruppo, il resto dal proiettore | |
| opencode con Big Pickle | La rete dalla VM raggiunge il servizio di OpenCode (indirizzo condiviso della scuola: il 4 novembre Copilot non ha risposto per circa 10 minuti). Una richiesta di lettura risponde in pochi secondi | Ramo di riserva a o b della parte 3 | Provato su QEMU dalla rete di questo PC: sì (lettura in 12 s, file in 41 s) · rete della scuola: da fare |
| Permesso `ask` in Windows | Provato il 15 novembre con `docente/MODELLI_OPENCODE/opencode.jsonc` nella cartella `noleggio` e Big Pickle: Plan nega la scrittura, Build chiede il permesso e scrive dopo Allow once. Da ripetere su VMware | Senza quel file Build scrive senza chiedere: si toglie la parte Build della slide 34 e la slide 35 | Provato su QEMU: sì · VMware: da fare |
| Come arriva il file dell'autore alla VM | Deciso: chiavetta (slide 26). Si vede dentro la VM, si apre il file e si copia il testo nel campo System Prompt? Provalo su una VM copiata | Copia e incolla tra PC e VM con VMware Tools, da dire a voce | |
| Copia della VM su 5 o 6 PC | Dimensione, tempo, domanda «spostata o copiata» alla prima accensione, memoria del PC reale | Un gruppo si unisce a un altro | |
| Ripristino prima della copia | Copia la VM prima delle prove, oppure dopo le prove cancella `nota_passaggio.txt`, le conversazioni di prova in Studio e in opencode, il testo nel System Prompt e le approvazioni salvate («Allow always» salva una regola `allow` e fa sparire la richiesta). Nella cartella `noleggio` devono restare solo i tre testi e `opencode.jsonc` | VM nuova da copia pulita | |
| Context Length | Impostare 8192 nella VM consegnata (si scrive nel riquadro e si preme «Reload model»; Studio salva l'impostazione per quel modello). La slide 25 chiede agli studenti che numero c'è accanto: deve leggere 8192. Con Auto la memoria stimata è 6,48 GiB, con 8192 è 3,33 GiB | Valore fisso | |
| Search e Tools in Studio | Disattivare Search (usa la rete). Verificare che restino grigi su Windows | Disattivarli a mano a ogni avvio | |
| Prompt di opencode e Context Length | Con Big Pickle non conta: la finestra è molto più grande (nelle prove fino a 10,9K, il 5%). Conta solo per la parte 2 con Qwen: il messaggio ha circa 3,5–4k token e 8192 bastano sulla carta | Alzare il valore |  |
| «Ragionamento» di Qwen3.5-2B | Secondo la scheda del modello (Hugging Face), il 2B parte senza ragionamento; con il ragionamento attivo il rischio è che si ripeta a lungo. In Studio non l'ho verificato | Spegnerlo se Studio lo permette |  |
| System Prompt dopo una nuova conversazione | Restava nelle prove su Linux; non provato su Windows | Incollarlo di nuovo a ogni conversazione |  |
| Cambio da Plan a Build | Provato il 15 novembre: Maiusc+Tab nella stessa conversazione. Da provare: dopo Plan, nella stessa conversazione, Build scrive davvero o risponde a parole? | Nuova sessione per la 3B: scrivere `/new` e premere Invio (provato il 15 novembre: apre una sessione nuova) | Provato su QEMU (cambio e `/new`) |
| Avvio di opencode da una finestra nuova | `opencode` da PowerShell e dal collegamento creato dallo script (con `-NoExit -Command "opencode"`) | Collegamento provato solo nella forma `unsloth start opencode`; `opencode` provato da PowerShell | |
| Passaggi «Explored» | In opencode v2.2.7 si espandono e mostrano i nomi dei file? Se sì, la slide 33 torna alla domanda «quali file ha aperto?» | Si lasciano le sole letture contate | |
| Reject nella 3A | Dopo un Reject e la richiesta ripetuta, il modello risponde leggendo il file? Quante volte ricompare un comando? | Il docente approva a voce, comando per comando | |
| Ramo b pronto sul tuo PC | opencode installato, una cartella con i tre testi e `opencode.jsonc`, lettura e scrittura provate con Big Pickle | Ramo a o c | |

Riferimenti: opencode, agenti e permessi: https://opencode.ai/docs/agents/ e https://opencode.ai/docs/permissions/ (regole generali, regole di Plan, «Allow always» salvato per il progetto). Unsloth e opencode: https://unsloth.ai/docs/integrations/opencode (scritta per un modello da 27B: per il 2B la prova è tua).

## Parte 1 · Il coordinatore in Copilot

| Slide | Passo | Che cosa fanno gli studenti |
| --- | --- | --- |
| 1–3 | Si riparte | Riaprono l'agente, rifanno la richiesta della lezione 4; quadro d'insieme |
| 4–9 | Il piano | Pizzeria; regola e prova; correzione del piano; la scrivono; due lavori insieme; criteri |
| 10–12 | Il rimborso | Scrivono RIMBORSO (o lo separano da FUORI SERVIZIO) e aggiornano l'elenco |
| 13–14 | Il controllo | Pizzeria; scrivono la regola |
| 15–18 | Una sola prova | Richiesta a tre lavori; risposta al tipo di noleggio; numeri; controllano la riga citata |
| 19–20 | Un caso proprio e file | Una richiesta inventata; file completo e agente aggiornato |
| 21 | Nome | «Coordinare»: lo dici a voce dopo che l'hanno fatto |

Non distribuire un agente del noleggio già scritto. Le tabelle a metà (slide 7, 11, 14) hanno le domande, mai le risposte.

### Slide 2 · Riaprite

La richiesta è quella della lezione 4: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.» Controllo: stessi orari della tavola «Valori di riferimento»; dopo il controllo li dici a voce. Serve a vedere che il file e l'agente funzionino ancora: chi ha perso l'agente passa a una chat normale. Non presumere che tutti abbiano finito la lezione 4: chi non ha il file riceve il punto di partenza.

### Slide 4–9 · Il piano prima

Slide 5: le frasi sono estratti del file della pizzeria. Chiedi l'alzata di mano prima di provare: si ferma dopo il piano? Prova la richiesta «La pizza è arrivata fredda e voglio i soldi indietro.» Slide 6: rispondi al piano «Procedi, ma solo il reclamo.»; l'agente deve fare solo RECLAMO e lasciare il rimborso fuori. La regola 2 della pizzeria (prima «Mi dispiace») resta valida: «Mi dispiace» viene prima del piano.

Slide 8: la richiesta dipende dal secondo lavoro scelto in lezione 4 (GUASTI o PASSAGGIO). Per GUASTI serve anche la guida ai guasti, per PASSAGGIO bastano registro e regole.

**Criterio, dopo la prova (slide 9):** il piano viene prima di qualsiasi risposta ai lavori, anche prima di «Lavoro usato:» (la tabella della slide 7 lo chiede esplicitamente: tre regole non devono chiedere tre prime righe diverse); i due lavori sono nell'ordine deciso dallo studente; dice quali testi usa; si ferma; dopo «Procedi» risponde. Se risponde subito senza piano, la regola non l'ha fermato: lo studente guarda la regola e la riscrive, non è un errore dello studente. Se si ferma e chiede il tipo di noleggio, è corretto. Non chiedere a nessuno di far sbagliare il modello.

### Slide 10–12 · Il rimborso diventa un lavoro

Nella lezione 4 gli studenti hanno scritto da soli l'agente, ognuno il suo, a partire dai tre testi: un chatbot per il noleggio che risponde alle richieste dei clienti (rimborso, aiuto con i guasti e simili). Non è accertato che tutti abbiano trattato il rimborso come richiesta a sé: nel file di ogni studente può essere dentro FUORI SERVIZIO o non esserci. Qui si separa, o si scrive da zero: conta altri minuti, dalla segnalazione al cambio, e ha bisogno del tipo di noleggio che il registro non riporta. Dillo una volta, poi lascia lavorare.

Alla slide 11 scrivono RIMBORSO con le quattro righe (e tolgono le righe del rimborso da FUORI SERVIZIO, se ci sono); alla slide 12 aggiornano l'elenco: quando FUORI SERVIZIO e RIMBORSO vanno insieme, quale viene prima e quali orari usa ciascuno dei due? Non c'è una sola risposta giusta sull'ordine, purché sia scritta e il piano la rispetti. Gli orari sono diversi: il rimborso non usa il risultato di FUORI SERVIZIO.

### Slide 13–14 · Ogni numero, la sua riga

La pizzeria: «Quanto costa una Diavola con la consegna?» (8 più 2, 10 euro). La colonna «Pizzeria» della slide 14 cita «la riga delle istruzioni», come il file. Il controllo deve citare la riga dei prezzi e quella della consegna: proietta le istruzioni della pizzeria accanto alla risposta, perché gli studenti non le hanno. Alla slide 14 scrivono la regola per il noleggio. Si scrive ora, prima della prova unica: non si aggiorna ancora l'agente.

Perché serve: quando un'informazione passa da uno strumento all'altro (qui dal testo alla risposta) si può perdere; il controllo è un modo esterno per accorgersene.

### Slide 15–18 · Una sola prova per le due regole nuove

Aggiornano l'agente con RIMBORSO e controllo, poi una sola conversazione con la richiesta a tre lavori. Per GUASTI: «Bici 12, sabato: quanto è stata fuori servizio, che cosa significa freni che non tengono, quanto rimborsiamo al cliente?» Per PASSAGGIO: «Bici 12, sabato: quanto è stata fuori servizio, quanto rimborsiamo al cliente? Prepara la nota per il turno dopo.» La previsione prima dell'invio (slide 15) è: che dato chiederà? Il tipo di noleggio manca nel registro; chi ha PASSAGGIO può ricevere anche la domanda sul turno. Le risposte da dare sono sulla slide 16, che mostri solo dopo la previsione: «A ore. Procedi.» e, se serve, «La nota è per chi inizia il pomeriggio di sabato.»

**Criterio (slide 17).** Il rimborso conta i **minuti senza bici** del cliente (dalla segnalazione al cambio), non i minuti di fuori servizio della bici. Le cifre sono nelle tavole in fondo (righe «Minuti senza bici del cliente» e «Rimborso proposto»). Se manca il tipo di noleggio l'agente lo chiede: è corretto. Se lo sceglie al posto dello studente, no. È una proposta: l'agente scrive «PROPOSTA DA CONTROLLARE», il banco decide.

**Slide 18.** Controllano il controllo: scelgono un numero della risposta e cercano nel registro o nelle regole la riga che l'agente cita. Una riga inventata o troppo vaga è un problema da correggere nel testo.

Per GUASTI vale la regola obbligatoria della guida: nessun consiglio per far uscire dal negozio una bici con freni che non tengono. Per PASSAGGIO: se il giorno o il turno non sono identificabili l'agente chiede; non si inventa una divisione dei turni.

### Slide 19–21 · Un caso proprio, file, nome

Slide 19: una richiesta inventata da ciascuno: dato mancante, testo insufficiente o lavoro che l'agente non ha (esempi della pizzeria, come nella lezione 4). Scrivono su un foglio la risposta corretta prima di provare. Se funziona al primo invio, cercano la regola che lo ha reso possibile, senza peggiorare le istruzioni; se qualcosa non va, correggono il punto necessario e riprovano. La correzione del piano da parte di chi scrive la mostri tu alla slide 6, e non la fanno inventare agli studenti.

Slide 20: il file `istruzioni_agente_noleggio.txt` deve essere completo e arrivato intero in Copilot, perché in parte 2 lo si porta altrove.

Slide 21: dai il nome **coordinare** e fai la domanda «Dove sta il coordinatore?». Risposta, a voce: era già lì, nel loro testo, letto da Copilot. Nessun programma lo ha eseguito.

## Parte 2 · Lo stesso testo, un altro modello

Lavoro di gruppo: quattro o cinque persone per ogni computer virtuale. Il modello è lento e risponde a una richiesta alla volta: una sola prova per gruppo.

- **Slide 23:** non conosciamo la dimensione di Copilot. Il modello della VM è Qwen3.5-2B, un file di circa 1,3 GB, e non usa Internet. Non dichiarare differenze di qualità che non hai misurato.
- **Slide 24:** il gruppo sceglie il file che ha tenuto meglio la richiesta a tre lavori. Si decide a parole, con i criteri delle slide 9 e 17.
- **Slide 25:** nel pannello **Context Length** (la quantità di testo che il modello riesce a tenere insieme) e **Temperature**. Il numero accanto a Context Length deve essere 8192. Estimated Memory Usage lo guardi tu, non lo chiedi a loro. Temperature è la manopola di Transformer Explainer: non si tocca ora.
- **Slide 26:** l'autore porta il file sulla chiavetta; lo incolla nel campo **System Prompt**; un altro scrive il messaggio con registro, regole (con GUASTI anche la guida ai guasti) e richiesta in una nuova conversazione. Quando il modello chiede il tipo di noleggio, il gruppo risponde «A ore. Procedi.» Le istruzioni nel campo sono vere istruzioni di sistema (il System Prompt di Studio è rimasto dopo una nuova chat nelle prove su Linux; non provato su Windows).
- **Slide 27–28:** ognuno scrive la previsione su un foglio prima dell'invio. Non anticipare l'esito. Alla slide 28 ogni gruppo dice una sola cosa diversa da Copilot: i resoconti restano brevi.
- **Slide 29:** se non ci arriva, una sola modifica e una riprova. Un modello piccolo può non seguire un testo lungo: non è colpa di chi ha scritto. Se il testo non entra, si alleggerisce il messaggio.
- **Slide 30–31:** un lavoro, un testo: la slide 30 fa la domanda, rispondi tu a voce e poi la slide 31 introduce opencode come un programma attorno al modello. Per il solo FUORI SERVIZIO il registro e le regole bastano; per quel lavoro la guida ai guasti non serve. Dici a voce il ponte: un programma può dare a ogni lavoro solo il suo testo. La slide 31 non dice chi apre i file: è la previsione della slide 32.

Il passaggio del file dalla postazione dell'autore alla VM è il punto più fragile dal punto di vista organizzativo: è deciso (chiavetta, slide 26), ma non provato. Controlla prima che la chiavetta si veda dentro la VM (tabella dei controlli).

## Parte 3 · opencode

**Il modello di opencode è Big Pickle**, uno dei modelli gratuiti di OpenCode (compare nell'elenco di `/models` senza registrazione). Il modello della VM (Qwen3.5-2B, in locale) resta solo nella parte 2. La dimensione di Big Pickle non è dichiarata dalla documentazione; la parte 3 è veloce anche perché il modello gira sui computer del fornitore e non sulla CPU della VM, non solo per la dimensione. Serve la rete dalla VM. Dalla documentazione di OpenCode: «free for a limited time» e durante il periodo gratuito i dati raccolti possono essere usati per migliorare il modello; i testi del noleggio sono inventati, ma non far scrivere dati personali (c'è una riga nella consegna). I modelli gratuiti cambiano in pochi giorni (il revisore ha trovato nella documentazione modelli gratuiti ritirati a inizio novembre): **la mattina del 18 controlla con `/models` che Big Pickle ci sia ancora**. Se manca, o se vuoi un modello che non usi i dati per l'addestramento, scegline un altro gratuito dall'elenco leggendo prima nella documentazione di OpenCode (pagina dei modelli) quali dichiarano di non conservare i dati, e cambia `"model"` in `opencode.jsonc` prima dell'aula. Prova una richiesta neutra dalla rete della scuola durante la parte 1, con le VM già accese, poi una nuova sessione.

Un passo alla volta, con una persona diversa ai comandi; gli altri scrivono la previsione su un foglio prima del risultato.

| Slide | Passo | Che cosa si vede |
| --- | --- | --- |
| 32–33 | 3A · Il programma legge | La richiesta è «Quale codice hanno le pastiglie montate sulla bici 12?». Nella prova Big Pickle ha letto il registro (tre passaggi «Explored: 1 read, 2 reads, 3 reads», senza i nomi dei file) e ha risposto in 12 secondi: «PF-44», citando il registro, righe 36 e 40, e avvertendo di non confonderlo con CA-26 (bici 5). Alla slide 33 si contano le righe «Explored» e si legge il numero dell'ultima. Non so se quel numero sia il totale delle letture o il conteggio fino a quel passo: nella prova è cresciuto da una riga all'altra (1, 2, 3), quindi lo leggo come totale; non verificato, può cambiare da una prova all'altra. Da dire: «ogni riga con la freccia è una lettura che il programma ha eseguito perché il modello l'ha chiesta; quali file, lo dice solo la risposta, e va controllata». Se la risposta cita file e riga, un altro del gruppo apre il registro con Blocco note e cerca con Ctrl+F il codice citato (con l'andata a capo automatica le righe sullo schermo non sono quelle del file: il numero di riga è in basso, non provato nella VM). Se la risposta non cita la riga, il gruppo la chiede. Poi dici tu a voce che chi legge il file è il programma, non il modello. Se compare una richiesta di permesso, vedi «Quando in 3A compare un permesso per la shell» |
| 34–35 | 3B · Piano, Build, permessi | La richiesta è «Crea il file nota_passaggio.txt con una sola riga: Controllare i freni della bici 12.». In Plan il modello spiega che non può scrivere e descrive che cosa farebbe (nella prova: 5,5 secondi). Dici dopo Plan: «In Plan il modello non ci ha nemmeno provato: segue le istruzioni di Plan. Se ci provasse, il programma glielo negherebbe: è la regola deny nel file.» Poi Maiusc+Tab, di nuovo la stessa richiesta: in Build compare «Permission required» con Allow once, Always allow e Reject: «approvare» è Allow once, «rifiutare» è Reject. Alla slide 35 si guarda in Documenti › noleggio se il file c'è. Ogni gruppo decide se approvare o rifiutare e scrive il perché; se tutti approvano, chiedi a un gruppo di rifiutare. Dopo le risposte scrivi alla lavagna le quattro regole (leggere: nessuna regola; scrivere: ask; comando: ask; scrivere in Plan: deny), senza proiettare il file, e chiedi perché la lettura non ha chiesto. opencode parte in Build |
| 36 | Quadro | Tabella testo → Copilot e Studio → opencode: modello, testi, piano, «PROPOSTA DA CONTROLLARE». È dopo l'esperienza, non prima. Una frase: in opencode ogni lavoro può diventare un agente a parte, con i suoi permessi; oggi non l'abbiamo provato |
| 37 | Distillazione | Un esempio documentato, non Big Pickle: DistilBERT, versione piccola di BERT (un modello di Google), «40% più piccola, 60% più veloce, 97% della comprensione del linguaggio» (Sanh e altri, arXiv 1910.01108, 2019); la scheda su Hugging Face dice che è stato addestrato con BERT come maestro, per restituire le stesse probabilità (licenza Apache 2.0). Dici a voce: «le stesse probabilità» sono le barre di Transformer Explainer; la distillazione è una tecnica, non una regola, e come è nato un modello si legge nella sua scheda. **Risposta alla domanda finale.** Scheda `huggingface.co/Qwen/Qwen3.5-2B` (letta il 15 novembre, non per intero): «Training Stage: Pre-training & Post-training», modello di partenza `Qwen3.5-2B-Base`, licenza Apache 2.0; nelle parti lette non compare la parola «distillazione». Il file di Studio (`unsloth/Qwen3.5-2B-GGUF`, UD-Q4_K_XL, circa 1,3 GB) è una versione compressa dello stesso modello: compressione e distillazione sono cose diverse. Di Big Pickle la documentazione di OpenCode dice solo «stealth model»: non si sa come sia nato, quindi non attribuirgli una distillazione. La velocità dipende anche dal computer che esegue il modello (la CPU della VM contro i server del fornitore), non solo dalla dimensione. |
| 38 | Chiusura | In opencode il modello decide ancora che cosa chiedere; il programma apre i file, scrive e chiede il permesso. Se il vostro agente potesse registrare un rimborso: allow, ask o deny? Perché? |

**File per opencode.** `docente/MODELLI_OPENCODE/opencode.jsonc` va nella cartella `noleggio` della VM e fa tre cose: sceglie il modello Big Pickle per Plan e Build; in Build fa chiedere conferma prima di scrivere o di eseguire un comando; in Plan nega la scrittura e `execute` (senza il secondo, il modello locale provava a scrivere con un programmino e ripeteva lo stesso errore) e chiede conferma per un comando della shell. **Provato il 15 novembre** su una copia della VM con opencode v2.2.7: in Plan Big Pickle risponde «Sono in modalità Plan, quindi non posso creare file» senza chiedere il permesso; in Build compare «Permission required» e dopo «Allow once» il file viene creato. Gli agenti di lavoro (`subagent`) e il coordinatore con più agenti sono stati tolti dalla lezione.

**Da dire a voce a tutta la classe, prima dell'invio della slide 32** (niente giro tra i banchi): se compare una richiesta di permesso, si legge il comando ad alta voce (vedi sotto); per approvare si sceglie una volta sola («Allow once»), mai «Always allow», che salva la regola e fa sparire la richiesta. La regola del comando identico non è sulla slide 32 (non c'è spazio): è nella consegna, che i gruppi devono avere aperta accanto alla VM; ripetila a voce. L'unica eccezione al divieto di giro tra i banchi è la mano alzata per un comando dubbio: chi è ai comandi legge il comando intero ad alta voce e decidi tu, oppure vai solo a quella VM. Alla 3B, appena i gruppi vedono la richiesta di permesso, proietta la slide 35. Il modello può scrivere il nome del file in modo diverso da quello chiesto: nella prova locale con Qwen è successo (`notapassaggio.txt`), con Big Pickle no.

**Quando in 3A compare un permesso per la shell.** Il comportamento del modello non è sempre uguale: nella prima prova Big Pickle ha letto il registro con lo strumento di lettura, senza chiedere; in altre ha provato `Get-ChildItem -Force | Select-Object Mode,Length,Name` e il programma ha chiesto il permesso (anche con la shell su `deny` nel file, provata il 15 novembre: il permesso è comparso lo stesso, quindi `deny` non è una soluzione verificata). **Rifiutare interrompe tutta la risposta** («The user declined this tool call», nessuna risposta alla domanda). Regola data agli studenti: Allow once **solo** se il comando è identico, lettera per lettera, a quello visto nella prova (sopra); in ogni altro caso Reject e ripetere la richiesta; se dopo il Reject compare di nuovo un comando, alzano la mano. Non esiste una regola «a parole» sicura: un comando che comincia con `Get-Content` può continuare con `; Clear-Content` e modificare il file, quindi nessun controllo sulla prima parola basta. Se un gruppo ti chiede se un comando diverso va bene, leggilo tu per intero prima di dire Allow once. Per chi ha visto il permesso, la domanda della slide 35 («nella prova con le pastiglie il programma vi ha chiesto il permesso? perché sì o perché no?») ha risposta sì: scrittura e comandi chiedono, la lettura con lo strumento no. Per gli altri la risposta è no: la lettura non ha regole. La domanda sulla «PROPOSTA DA CONTROLLARE» della consegna si chiude alla slide 36. Le regole `allow` per i comandi di lettura sono state provate in una versione di prova: con quel comando il permesso è comparso lo stesso. Per questo nel file non ci sono; non ho verificato come il programma tratta i comandi composti.

**Differenza da cogliere.** Nel loro file i testi sono incollati nel messaggio; in opencode il programma li apre quando il modello lo chiede. «PROPOSTA DA CONTROLLARE» nel loro file sono parole; in Build il programma si ferma davvero. Se il modello non fa la chiamata, si legge perché: non è un fallimento da nascondere.

Fuori dalla lezione: nessuna modifica di codice, nessuna configurazione di fornitori di modelli. Il programma lavora nella cartella `noleggio` per convenzione, non per un limite tecnico.

### Rami di riserva della parte 3

Se Big Pickle non risponde (rete, limite di richieste, modello tolto), scegli **una** alternativa e dichiarala:

| Alternativa | Che cosa è | Come si dichiara |
| --- | --- | --- |
| a · Qwen locale, dal collegamento Studio | `unsloth start opencode` in PowerShell nella cartella `noleggio`: il modello è `unsloth/Qwen3.5-2B-GGUF`, in locale. Nella prova una risposta è arrivata dopo più di quattro minuti e in Plan il modello ha ripetuto errori; la parte 3 diventa una dimostrazione | «Qui il modello è piccolo e locale: è lento.» |
| b · Esecuzione dal vivo dal tuo PC | opencode sul tuo PC con Big Pickle, proiettato. Usa lo stesso servizio ma un altro indirizzo: prova con l'hotspot del telefono se il guasto è la rete della scuola; non aiuta se Big Pickle è stato ritirato | «Esecuzione reale sul computer del docente, non sulle VM.» |
| c · Prova a secco su carta | Si segue `docente/SCHEMA_A_SECCO_PARTE3.md`: il modello chiede, il programma legge, il modello risponde | «Non è un'esecuzione: è uno schema scritto a mano. Non prova che opencode funzioni.» |

Non presentare testi scritti a mano come registrazioni del modello. Le parti 1 e 2 restano eseguibili anche con la sola alternativa c.

## Se manca il servizio o qualcosa non passa

Il 4 novembre Copilot non ha risposto per circa 10 minuti (ipotesi, non accertata: limite di richieste per indirizzo condiviso). Niente servizi online alternativi: niente HackMerlin, Prompt Airlines o Gandalf.

| Situazione | Condotta |
| --- | --- |
| Agente non disponibile | Chat normale con le istruzioni nel primo messaggio, ripetuto in ogni chat nuova. Non vera istruzione di sistema |
| Copilot non risponde | Prova a secco collettiva dal proiettore: si cerca nelle istruzioni di uno studente quale regola copre la richiesta. Non è una risposta del modello |
| Messaggio troppo lungo | Solo i giorni completi del registro necessari, senza spezzare la sequenza del fuori servizio |
| Studio o VM non partono | Il gruppo si unisce a un altro, oppure guardano la prova dal tuo computer |
| Modello molto lento | Una sola prova per gruppo; nel frattempo si rilegge la regola del piano. Il ramo di riserva della parte 3 si decide prima dell'aula, dopo la misura del tempo alla prima parola, non in aula |
| Istruzioni tagliate nel passaggio | Controllare il testo nel campo System Prompt; accorciare le ripetizioni, non le regole |

## Fonti del noleggio e valori automatici

I tre testi sono inventati per l'esercitazione ITS MAKER e identici a quelli della lezione 4. `docente/genera_materiali.py` ricava le tavole seguenti dagli originali in `docente/backup/fonti/`: sono il riferimento per controllare risposte e criteri. Non ricopiare numeri a mano.

### Valori di riferimento del registro

{{VALORI_REGISTRO}}

La prova del meccanico precede il rientro in fila: una prova riuscita non significa bici disponibile. Il cambio della bici al cliente non chiude il fuori servizio della bici 12. Per il rimborso valgono i minuti senza bici, dalla segnalazione al cambio: non vanno scambiati con i minuti fuori servizio della bici. Il tipo di noleggio, gli importi pagati e il nome del meccanico non sono nel registro: l'agente deve chiederli o dire che non ci sono. La catena della bici 9 è un aggiustamento al banco, non un fuori servizio.

### Note che nominano il turno

{{NOTE_TURNO}}

Il registro non suddivide tutte le note per turno. Per PASSAGGIO, se il giorno o il turno non sono identificabili, l'agente chiede.

### Che cosa contiene la guida ai guasti

{{VALORI_GUIDA}}

Dove un'informazione manca, dirlo è corretto. Per freni e sterzo vale la regola obbligatoria della guida: nessun consiglio aggiunto, nessuna autorizzazione a far uscire una bici dal negozio.

## TODO prima dell'aula

- **Schermate dalla VM**: fatte il 15 novembre (Studio 2026.11.4, opencode v2.2.7) e inserite nelle slide 25, 26, 32, 33 e 34, con il punto cerchiato e il testo alternativo. Immagini in `docente/backup/immagini_slide/`; gli originali non ritoccati in `immagini_slide/originali_vm/`. Le schermate di opencode (32, 33, 34) sono fatte con Big Pickle. Per la slide 33 è una richiesta diversa («Quali file ci sono in questa cartella?»); non c'è né la risposta alla domanda della slide 32 né la richiesta di permesso. La schermata della slide 25 non mostra il valore di Context Length (è la domanda della slide): nella VM deve leggersi 8192.
- **VM preparata senza avviarla.** Nella cartella della chiavetta `VM_Studenti/ITSMAKER-Win11-Studio-lezione5/` c'è una copia della VM con tutto già al suo posto, preparata con la VM spenta: i quattro file nella cartella di partenza, un richiamo nella cartella di avvio automatico che al primo accesso crea `Documenti\noleggio` e il collegamento «opencode» e poi si cancella da solo. La VM originale non è stata toccata. **Non è stata aperta in VMware** (non è installato su questo computer): è stata provata soltanto con QEMU, su una copia usa e getta. Al primo avvio in VMware controlla che il collegamento e la cartella compaiano; VMware chiederà se la VM è stata spostata o copiata. Se qualcosa non va, lo script `docente/PREPARA_VM_LEZIONE5.ps1` fa le stesse cose a mano: metti nella stessa cartella lo script, i tre testi di `studenti/` e `opencode.jsonc`, apri PowerShell lì e scrivi `powershell -ExecutionPolicy Bypass -File .\PREPARA_VM_LEZIONE5.ps1`.
- **Studio, da fare a mano**: all'avvio il modello non è caricato (Select model, On Device) e Context Length non è fissato. Si imposta 8192 e si preme Reload model; spunta «Always load» se vuoi che si ricarichi da solo. Il collegamento a opencode lancia `opencode` con Big Pickle: non usa Studio.
- Revisione del `revisore-didattico`: fatta più volte il 15 novembre (vedi il piano); l'ultima va ripetuta solo se cambia la struttura.

## Prova nella VM del 15 novembre

Fatta su copie temporanee della VM `ITSMAKER-Win11-Studio`, aperte con QEMU/KVM (non VMware) su un overlay: il file `.vmdk` sulla chiavetta non è stato toccato. Tastiera della VM: italiana. I tempi non valgono per le VM in aula.

- **Studio.** Si apre dal collegamento in Edge (localhost:8888). Il modello **non è caricato** all'avvio: Select model, scheda On Device, Qwen3.5-2B-GGUF; il caricamento ha richiesto circa tre minuti. Appaiono la proposta di traduzione di Edge e «2 aggiornamenti del runtime» (llama.cpp e whisper.cpp, 21 MB): chiudere la prima, scegliere «Più tardi» sul secondo. Il pannello Run settings è chiuso: si apre con l'icona in alto a destra. Context Length è su **Auto** (nell'intestazione 65.5k); la memoria stimata è 6,48 GiB con l'avviso «Exceeds system RAM». Si scrive 8192 nel riquadro e si preme Reload model: Studio salva l'impostazione per quel modello, la memoria stimata passa a 3,33 GiB e nell'intestazione si legge 8.2k.
- **opencode con il modello locale (Qwen3.5-2B, avviato con `unsloth start opencode`).** Troppo lento per la parte 3: una richiesta di lettura ha richiesto 4 minuti e 11 secondi a 0,7 token al secondo, con 8192 di contesto nessuna risposta in circa nove minuti, e in Plan il modello ha ripetuto lo stesso errore («Cannot import "fs"» di `execute`). Con le regole di permesso senza quelle di Plan, la richiesta di scrivere un file chiedeva il permesso anche in Plan. Il modello ha scritto anche un nome diverso (`notapassaggio.txt`).
- **opencode con Big Pickle** (`opencode` da PowerShell nella cartella `noleggio`; compare nell'elenco di `/models` come «Big Pickle · Free», senza registrazione). Parte in Build; Maiusc+Tab passa a Plan. **Plan:** «Sono in modalità Plan, quindi non posso creare file…», 5,5 secondi, nessuna richiesta di permesso. **Build:** «Write nota_passaggio.txt», poi «Permission required» (Allow once, Always allow, Reject); dopo Allow once il file è stato creato e riletto, 41,7 secondi in tutto. **Lettura:** il codice delle pastiglie della bici 12 è stato trovato in 12,3 secondi (PF-44, registro righe 36 e 40, con l'avvertenza su CA-26 della bici 5); i passaggi mostrati sono «Explored: 1 read», «2 reads», «3 reads» e «Thought», senza i nomi dei file. Contesto usato: 10,9K, il 5%.
- **Privacy e disponibilità.** Dalla documentazione di OpenCode, Big Pickle è «free for a limited time» e nel periodo gratuito i dati raccolti possono migliorare il modello. Non ho verificato come sia stato addestrato né se sia «distillato»: la documentazione lo definisce solo «stealth model».

## Che cosa non è stato provato

- Copilot con l'account studente: creazione e modifica dell'agente, comportamento del piano, del controllo e dell'esempio della pizzeria.
- La VM preparata in VMware (collegamento, cartella, avvio) e Studio con Search spento.
- Big Pickle dalla rete della scuola, con 5 o 6 VM insieme sullo stesso indirizzo.
- Il collegamento «opencode» con il comando `opencode`: è stato provato `unsloth start opencode` dal collegamento e `opencode` da PowerShell, ma non il collegamento nella forma finale (la VM preparata contiene già la forma finale).
- Tempi di risposta della parte 2 (Qwen con i testi della lezione) su VMware.
- Copia della VM e memoria dei PC reali.

La revisione didattica è stata fatta più volte: cinque il 12 e il 13 novembre (esito dell'ultima: DA CORREGGERE su un solo punto importante, il comportamento di Plan con la shell, corretto poi nel testo) e sei il 15 novembre, dopo il cambio a Big Pickle e l'aggiunta della slide 37; l'ultima, di conferma, ha dato APPROVATA con sei minori (applicati cinque; la sesta, la regola del permesso anche sulla slide 32, non è entrata per mancanza di spazio). I problemi corretti e l'esito sono nel piano («Revisioni del 15 novembre»). Corretti nelle revisioni del 13 novembre: previsioni con la risposta già scritta, slide 16 separata, slide 33 trasformata in controllo, decisione del permesso al gruppo, chiavetta per il file, richiesta 3B con una sola scrittura, regole `ask` nell'elenco generale dei permessi, ripristino della VM prima della copia. La stima dei tempi resta nel rapporto del revisore e non entra nei materiali. Il recupero di documenti (RAG) è rimandato alla lezione 6: le verifiche già raccolte sono nel piano.

## Chiusura dal proiettore

Chiedi quale regola utile hanno scoperto e se il loro agente, potendo registrare un rimborso, dovrebbe avere allow, ask o deny, e perché. Non raccogliere un'autovalutazione scritta. Dal confronto conserva tu ciò che serve alla lezione 6: che cosa ha tenuto il modello piccolo, quale ramo della parte 3 si è usato, che cosa ha funzionato nella VM.
