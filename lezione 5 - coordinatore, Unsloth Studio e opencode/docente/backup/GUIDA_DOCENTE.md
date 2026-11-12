# Guida docente · Lezione 5

**ITS MAKER Bologna · 18 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

Documento riservato al docente. Struttura e motivi sono in `docente/backup/PIANO_LEZIONE5.md`; qui c'è ciò che serve per condurre.

## La lezione da condurre

Si riparte dall'agente Ruota Libera della lezione 4. Nella **parte 1**, in Copilot e ognuno sul proprio computer, il file `istruzioni_agente_noleggio.txt` riceve tre novità: il piano mostrato prima della risposta, il rimborso come lavoro a sé e il controllo che cita la riga di ogni numero. Nelle **parti 2 e 3** si lavora in gruppo, quattro o cinque persone per ogni computer virtuale con Unsloth Studio e opencode: lo stesso testo letto da un modello piccolo, poi un programma che esegue il coordinamento.

Parole: in aula si dice **coordinatore** per chi sceglie i lavori, decide l'ordine, si ferma a chiedere e controlla. «Orchestratore» lo dici tu alla fine, a voce. Nomi dei prodotti (Plan, Build, allow, ask, deny) si lasciano come compaiono nel programma e si spiegano la prima volta.

Come nella lezione 4: niente giro tra i banchi, niente file da consegnare, niente voto. I risultati si leggono sugli schermi e dal proiettore; i criteri si mostrano dopo la prova. Una prova riuscita subito vale quanto una riuscita dopo una correzione. Nessuna attività si basa sull'errore del modello.

Non dichiarare provato ciò che non lo è: nulla di questa lezione è stato provato in Copilot con l'account studente, e la parte 3 non è stata provata con il modello della VM (vedi sotto).

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE5.docx` e i tre testi `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt` (copie della lezione 4: stessi fatti). Non pubblicare le cartelle di backup.
- `studenti/da_pubblicare_a_chi_non_ha_il_file/ISTRUZIONI_DI_PARTENZA_NOLEGGIO.txt`: lo dai solo a chi non ha il proprio `istruzioni_agente_noleggio.txt`. È il testo mostrato nella lezione 4 con un solo esempio cambiato (la bici 5), non una soluzione collaudata. Chi lo riceve aggiunge comunque piano, rimborso e controllo. Il suo «Esempio 1» usa la bici 5, non la bici 12, per non dare la risposta alla richiesta della slide 2.
- Dimostrazione: `docente/ESEMPIO_DIMOSTRAZIONE_PIZZERIA_L5.txt`. Nelle istruzioni dell'agente va solo il testo **tra i due separatori**. Provalo prima con le richieste in fondo al file, ciascuna in una chat nuova. Se non puoi, mostra il testo dichiarando che non è una risposta del modello. Le risposte non sono scritte nel file: sono quelle del modello.
- Sulla VM, nella cartella `noleggio`: i tre testi (da questa cartella `studenti/`) e `docente/MODELLI_OPENCODE/opencode.jsonc` nella stessa cartella. Controlla il percorso: le slide 25 e 31 li danno per presenti.
- Proiettore: **prima le richieste, dopo i criteri**. I valori vengono dalle tavole in fondo, non da numeri ricopiati.

### Organizzazione delle VM (da decidere prima)

Una VM ogni quattro o cinque postazioni. Nessuno di questi passaggi è stato provato: è la sequenza che propongo, da correggere dopo le verifiche.

| Quando | Che cosa |
| --- | --- |
| Prima dell'aula | Gruppi decisi per postazione. VM copiate e accese, Unsloth Studio aperto con il modello **già caricato** (Context Length 8192, Search spento). Nella cartella `noleggio`: i tre testi e `opencode.jsonc`. Sul desktop della VM un collegamento che avvia opencode nella cartella `noleggio` (da creare e provare) |
| Parte 1 | Sul PC che ospita la VM solo la finestra di Copilot e Blocco note: la memoria è il controllo più incerto. Se una VM manca, il gruppo si unisce a un altro |
| Inizio parte 2 | Gli studenti si spostano alla postazione con la VM. Mostri Studio con il modello già caricato; non si carica in aula |
| Inizio parte 3 | Si avvia opencode dal collegamento sul desktop |

### Controlli pre-aula

Nessuno di questi controlli è stato eseguito: la colonna Esito è vuota.

| Controllo | Che cosa accertare | Se fallisce | Esito |
| --- | --- | --- | --- |
| Copilot, agente | Come in lezione 4: salvare, riaprire, modificare le istruzioni | Chat normale con le istruzioni nel primo messaggio, non vere istruzioni di sistema | |
| Piano e controllo in Copilot | La pizzeria della lezione 5, con la richiesta suggerita: si ferma dopo il piano? Cita le righe? | Raccontalo come è: un modello non segue sempre una regola, e la prova passa dalla correzione del testo | |
| Tempo alla prima parola, VM | Registro, regole e istruzioni nel messaggio (circa 3,5–4k token); poi la prima risposta di opencode | Parte 3 come dimostrazione del docente (vedi rami) | |
| opencode e modello da 2B | Una richiesta di lettura file produce la chiamata allo strumento nel formato giusto. Provare più volte | Parte 3 secondo il ramo di riserva | |
| Permesso `ask` in Windows | Con `docente/MODELLI_OPENCODE/opencode.jsonc` nella cartella `noleggio`, la richiesta di conferma compare davvero quando il modello vuole scrivere. Controlla che la creazione di un file nuovo passi da `edit` e che anche la shell chieda conferma. Senza quel file Build scrive senza chiedere | Si toglie la parte Build della slide 33 e la slide 34 | |
| Come arriva il file dell'autore alla VM | Chiavetta o copia e incolla tra PC e VM con VMware Tools | Decidere prima: le slide dicono «come il docente indica» | |
| Copia della VM su 5 o 6 PC | Dimensione, tempo, domanda «spostata o copiata» alla prima accensione, memoria del PC reale | Un gruppo si unisce a un altro | |
| Context Length | Impostare 8192 nella VM consegnata; con Auto su Linux la memoria era maggiore | Valore fisso | |
| Search e Tools in Studio | Disattivare Search (usa la rete). Verificare che restino grigi su Windows | Disattivarli a mano a ogni avvio | |
| Prompt di opencode e Context Length 8192 | Le definizioni degli strumenti di opencode entrano nel contesto fissato per la parte 2? | Alzare Context Length per la parte 3 |  |
| «Ragionamento» di Qwen3.5-2B | Se è attivo, la risposta si allunga e il tempo cresce. Non verificato | Spegnerlo se Studio lo permette |  |
| System Prompt dopo una nuova conversazione | Restava nelle prove su Linux; non provato su Windows | Incollarlo di nuovo a ogni conversazione |  |
| Cambio da Plan a Build | Come si fa nella versione installata di opencode | Mostrarlo prima e metterlo in una slide, non a voce |  |
| Avvio di opencode da una finestra nuova | `unsloth start opencode` con il modello già caricato, senza il PATH della sessione di prova | Collegamento sul desktop | |

Riferimenti: opencode, agenti e permessi: https://opencode.ai/docs/agents/. Unsloth e opencode: https://unsloth.ai/docs/integrations/opencode (scritta per un modello da 27B: per il 2B la prova è tua).

## Parte 1 · Il coordinatore in Copilot

| Slide | Passo | Che cosa fanno gli studenti |
| --- | --- | --- |
| 1–3 | Si riparte | Riaprono l'agente, rifanno la richiesta della lezione 4; quadro d'insieme |
| 4–9 | Il piano | Pizzeria; regola e prova; correzione del piano; la scrivono; due lavori insieme; criteri |
| 10–12 | Il rimborso | Scrivono RIMBORSO (o lo separano da FUORI SERVIZIO) e aggiornano l'elenco |
| 13–14 | Il controllo | Pizzeria; scrivono la regola |
| 15–17 | Una sola prova | Richiesta a tre lavori; numeri; controllano la riga citata |
| 18–19 | Un caso proprio e file | Una richiesta inventata; file completo e agente aggiornato |
| 20 | Nome | «Coordinare»: lo dici a voce dopo che l'hanno fatto |

Non distribuire un agente del noleggio già scritto. Le tabelle a metà (slide 7, 11, 16) hanno le domande, mai le risposte.

### Slide 2 · Riaprite

La richiesta è quella della lezione 4: «Per quanti minuti è stata fuori servizio la bici 12 sabato? Mostrami gli orari.» Controllo: stessi orari della tavola «Valori di riferimento». Serve a vedere che il file e l'agente funzionino ancora: chi ha perso l'agente passa a una chat normale. Non presumere che tutti abbiano finito la lezione 4: chi non ha il file riceve il punto di partenza.

### Slide 4–9 · Il piano prima

Slide 5: le frasi sono estratti del file della pizzeria. Chiedi l'alzata di mano prima di provare: si ferma dopo il piano? Prova la richiesta «La pizza è arrivata fredda e voglio i soldi indietro.» Slide 6: rispondi al piano «Procedi, ma solo il reclamo.»; l'agente deve fare solo RECLAMO e lasciare il rimborso fuori. La regola 2 della pizzeria (prima «Mi dispiace») resta valida: «Mi dispiace» viene prima del piano.

Slide 8: la richiesta dipende dal secondo lavoro scelto in lezione 4 (GUASTI o PASSAGGIO). Per GUASTI serve anche la guida ai guasti, per PASSAGGIO bastano registro e regole.

**Criterio, dopo la prova (slide 9):** il piano viene prima di qualsiasi risposta ai lavori, anche prima di «Lavoro usato:» (la tabella della slide 7 lo chiede esplicitamente: tre regole non devono chiedere tre prime righe diverse); i due lavori sono nell'ordine deciso dallo studente; dice quali testi usa; si ferma; dopo «Procedi» risponde. Se risponde subito senza piano, la regola non l'ha fermato: lo studente guarda la regola e la riscrive, non è un errore dello studente. Se si ferma e chiede il tipo di noleggio, è corretto. Non chiedere a nessuno di far sbagliare il modello.

### Slide 10–12 · Il rimborso diventa un lavoro

Nella lezione 4 il rimborso era la seconda richiesta del titolare dopo il fuori servizio (slide 33–35 di allora); nel file di ogni studente può essere dentro FUORI SERVIZIO o non esserci. Qui si separa, o si scrive da zero: conta altri minuti, dalla segnalazione al cambio, e ha bisogno del tipo di noleggio che il registro non riporta. Dillo una volta, poi lascia lavorare.

Alla slide 12 tolgono le righe del rimborso da FUORI SERVIZIO se ci sono, scrivono RIMBORSO con le quattro righe e aggiornano l'elenco: quando FUORI SERVIZIO e RIMBORSO vanno insieme, quale viene prima e quali orari usa ciascuno dei due? Non c'è una sola risposta giusta sull'ordine, purché sia scritta e il piano la rispetti. Gli orari sono diversi: il rimborso non usa il risultato di FUORI SERVIZIO.

### Slide 13–14 · Ogni numero, la sua riga

La pizzeria: «Quanto costa una Diavola con la consegna?» (8 più 2, 10 euro). La colonna «Pizzeria» della slide 14 cita «la riga delle istruzioni», come il file. Il controllo deve citare la riga dei prezzi e quella della consegna: proietta le istruzioni della pizzeria accanto alla risposta, perché gli studenti non le hanno. Alla slide 14 scrivono la regola per il noleggio. Si scrive ora, prima della prova unica: non si aggiorna ancora l'agente.

Perché serve: quando un'informazione passa da uno strumento all'altro (qui dal testo alla risposta) si può perdere; il controllo è un modo esterno per accorgersene.

### Slide 15–17 · Una sola prova per le due regole nuove

Aggiornano l'agente con RIMBORSO e controllo, poi una sola conversazione con la richiesta a tre lavori. Per GUASTI: «Bici 12, sabato: quanto è stata fuori servizio, che cosa significa freni che non tengono, quanto rimborsiamo al cliente?» Per PASSAGGIO: «Bici 12, sabato: quanto è stata fuori servizio, quanto rimborsiamo al cliente? Prepara la nota per il turno dopo.» La previsione prima dell'invio è: che dato chiederà? Il tipo di noleggio manca nel registro; chi ha PASSAGGIO può ricevere anche la domanda sul turno. Risposte: «A ore. Procedi.» e, se serve, «La nota è per chi inizia il pomeriggio di sabato.»

**Criterio (slide 16).** Il rimborso conta i **minuti senza bici** del cliente (dalla segnalazione al cambio), non i minuti di fuori servizio della bici. Le cifre sono nelle tavole in fondo (righe «Minuti senza bici del cliente» e «Rimborso proposto»). Se manca il tipo di noleggio l'agente lo chiede: è corretto. Se lo sceglie al posto dello studente, no. È una proposta: l'agente scrive «PROPOSTA DA CONTROLLARE», il banco decide.

**Slide 17.** Controllano il controllo: scelgono un numero della risposta e cercano la riga che l'agente cita. Una riga inventata o troppo vaga è un problema da correggere nel testo.

Per GUASTI vale la regola obbligatoria della guida: nessun consiglio per far uscire dal negozio una bici con freni che non tengono. Per PASSAGGIO: se il giorno o il turno non sono identificabili l'agente chiede; non si inventa una divisione dei turni.

### Slide 18–20 · Un caso proprio, file, nome

Slide 18: una richiesta inventata da ciascuno: dato mancante, testo insufficiente o lavoro che l'agente non ha (esempi della pizzeria, come nella lezione 4). Decidono prima la risposta corretta. Se funziona al primo invio, cercano la regola che lo ha reso possibile, senza peggiorare le istruzioni. La correzione del piano da parte di chi scrive la mostri tu alla slide 6, e non la fanno inventare agli studenti.

Slide 19: il file `istruzioni_agente_noleggio.txt` deve essere completo e arrivato intero in Copilot, perché in parte 2 lo si porta altrove.

Slide 20: dai il nome **coordinare** e fai la domanda «Dove sta il coordinatore?». Risposta, a voce: era già lì, nel loro testo, letto da Copilot. Nessun programma lo ha eseguito.

## Parte 2 · Lo stesso testo, un altro modello

Lavoro di gruppo: quattro o cinque persone per ogni computer virtuale. Il modello è lento e risponde a una richiesta alla volta: una sola prova per gruppo.

- **Slide 22:** non conosciamo la dimensione di Copilot. Il modello della VM è Qwen3.5-2B, un file di circa 1,3 GB, e non usa Internet. Non dichiarare differenze di qualità che non hai misurato.
- **Slide 23:** il gruppo sceglie il file che ha tenuto meglio la richiesta a tre lavori. Si decide a parole, con i criteri delle slide 9 e 16.
- **Slide 24:** nel pannello **Context Length** (la quantità di testo che il modello riesce a tenere insieme) e **Temperature**. Estimated Memory Usage lo guardi tu, non lo chiedi a loro. Temperature è la manopola di Transformer Explainer: non si tocca ora.
- **Slide 25:** il file nel campo **System Prompt**, il messaggio con registro, regole (con GUASTI anche la guida ai guasti) e richiesta in una nuova conversazione. Quando il modello chiede il tipo di noleggio, il gruppo risponde «A ore. Procedi.» Le istruzioni nel campo sono vere istruzioni di sistema (il System Prompt di Studio è rimasto dopo una nuova chat nelle prove su Linux; non provato su Windows).
- **Slide 26–27:** ognuno scrive la previsione su un foglio prima dell'invio. Non anticipare l'esito.
- **Slide 28:** se non ci arriva, una sola modifica e una riprova. Un modello piccolo può non seguire un testo lungo: non è colpa di chi ha scritto.
- **Slide 29–30:** un lavoro, un testo: la slide 29 fa la domanda, rispondi tu a voce e poi la slide 30 dice che un programma può dare a ogni lavoro soltanto il suo testo. Per il solo FUORI SERVIZIO il registro e le regole bastano; per quel lavoro la guida ai guasti non serve. Un programma può dare a ogni lavoro solo il suo testo: è il ponte verso la parte 3.

Il passaggio del file dalla postazione dell'autore alla VM è il punto più fragile dal punto di vista organizzativo: decidilo prima (tabella dei controlli).

## Parte 3 · opencode

**La parte 3 dipende dal controllo «opencode e modello da 2B» della tabella.** Le slide 30–35 sono scritte per il caso in cui il programma esegua le chiamate agli strumenti con il modello della VM. Se il controllo non riesce, non c'è una versione più semplice eseguibile dagli studenti con quel modello: vale il ramo di riserva.

Un passo alla volta, con una persona diversa ai comandi; gli altri scrivono la previsione su un foglio prima del risultato.

| Slide | Passo | Che cosa si vede |
| --- | --- | --- |
| 31–32 | 3A · Il programma legge | La richiesta è «Quale codice hanno le pastiglie montate sulla bici 12?»: la risposta sta solo nel registro, quindi il modello deve **chiedere** di leggerlo e il programma lo apre. Chi legge è il programma. Con una domanda generale il modello potrebbe rispondere senza leggere |
| 33–34 | 3B · Piano, Build, permessi | In Plan il file non compare; in Build il programma chiede conferma prima di scrivere. Dici tu a ogni gruppo se approvare o rifiutare; si confrontano dal proiettore le cartelle: in quali c'è il file? Una sola esecuzione per gruppo (il modello è lento) |
| 35 | Quadro | Tabella file → Copilot e Studio → opencode: testi, piano, «PROPOSTA DA CONTROLLARE». È dopo l'esperienza, non prima. Una frase: in opencode ogni lavoro può diventare un agente a parte, con i suoi permessi; oggi non l'abbiamo provato |
| 36 | Chiusura | Quale permesso dareste al vostro agente, e perché? |

**File per opencode.** `docente/MODELLI_OPENCODE/opencode.jsonc` va nella cartella `noleggio` della VM: fa chiedere conferma a Build prima di scrivere. È scritto sulla documentazione, **non è stato provato** con la versione installata (v2.2.7). Gli agenti di lavoro (`subagent`) e il coordinatore con più agenti sono stati tolti dalla lezione: sono materia per un'altra occasione.

**Differenza da cogliere.** Nel loro file i testi sono incollati nel messaggio; in opencode il programma li apre quando il modello lo chiede. «PROPOSTA DA CONTROLLARE» nel loro file sono parole; in Build il programma si ferma davvero. Se il modello non fa la chiamata, si legge perché: non è un fallimento da nascondere.

Fuori dalla lezione: nessuna modifica di codice, nessuna configurazione di fornitori di modelli. Il programma lavora nella cartella `noleggio` per convenzione, non per un limite tecnico.

### Rami di riserva della parte 3

Se il modello della VM non produce chiamate agli strumenti, scegli **una** alternativa e dichiarala:

| Alternativa | Che cosa è | Come si dichiara |
| --- | --- | --- |
| a · Registrazione di una prova riuscita | Schermate o registrazione di 3A–3B riuscite nella VM col modello consegnato, più volte | «Esecuzione reale registrata prima della lezione.» |
| b · Esecuzione dal vivo con un modello più grande | opencode sul tuo PC con un modello già collaudato | «Esecuzione reale con un altro modello, non quello della VM.» |
| c · Prova a secco su carta | Si segue `docente/SCHEMA_A_SECCO_PARTE3.md`: il modello chiede, il programma legge, il modello risponde | «Non è un'esecuzione: è uno schema scritto a mano. Non prova che opencode funzioni con questo modello.» |

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

- **Schermate dalla VM** (Studio 2026.11.4, opencode v2.2.7), da mettere in `docente/backup/immagini_slide/` e nelle slide, con il punto cerchiato e un testo alternativo: pannello con Context Length e Temperature (slide 24); campo System Prompt (slide 25); avvio di opencode (slide 31); passaggio da Plan a Build (slide 33). Non catturare l'elenco dei passaggi con la lettura del file né la richiesta di permesso: anticiperebbero il risultato delle slide 32 e 34. Finché mancano, le slide dicono «il docente mostra».
- Collegamento sul desktop della VM che avvia opencode nella cartella `noleggio`: da creare e provare.
- Ripetere la revisione del `revisore-didattico` dopo le schermate.

## Che cosa non è stato provato

- Copilot con l'account studente: creazione e modifica dell'agente, comportamento del piano, del controllo e dell'esempio della pizzeria.
- Unsloth Studio su Windows nella VM: avvio, System Prompt, Context Length, parametri.
- opencode con il modello da 2B: connessione, chiamate agli strumenti, permessi.
- Tempi di risposta del modello con i testi della lezione e con opencode.
- Copia della VM e memoria dei PC reali.

La revisione didattica è stata fatta due volte (12 novembre); la stima dei tempi resta nel rapporto del revisore e non entra nei materiali. Il recupero di documenti (RAG) è rimandato alla lezione 6: le verifiche già raccolte sono nel piano.

## Chiusura dal proiettore

Chiedi quale regola utile hanno scoperto e quale permesso darebbero all'agente. Non raccogliere un'autovalutazione scritta. Dal confronto conserva tu ciò che serve alla lezione 6: che cosa ha tenuto il modello piccolo, quale ramo della parte 3 si è usato, che cosa ha funzionato nella VM.
