# Piano della lezione 6 · 25 novembre 2026

Documento riservato al docente. Bozza da approvare. Sostituisce la lezione 6 «Agenti, permessi e difese» e il blocco RAG di `lezione 4 - reti neurali e agenti con orchestrazione/docente/backup/BOZZA_PERCORSO_LEZIONI_4-7.md`, che slittano o restano materiale in attesa.

## Che cosa è successo in lezione 5 (riferito dal docente il 19 novembre 2026)

- Durata: 1 h 50 min piena.
- Orchestratore: esercizio `lezione 5 - orchestratore, Unsloth Studio e opencode/esercizio sistema agentico.md` più lo schema `system prompt routing interno esternojpg.jpg`. Ha occupato circa 70 minuti, quindi circa 40 minuti per il resto. Struttura dell'esercizio: login admin o utente; tre skill (guasti → utente, registro → solo admin, regole di noleggio → solo utente) sul caso Ruota Libera; istruzioni di routing nell'agente, con esempi di rinforzo positivo.
- Unsloth Studio: interfaccia mostrata, qualche prova con la temperatura.
- opencode: interfaccia mostrata, dashboard in `.html` creata con opencode.
- Stato a fine lezione (riferito dal docente il 19 novembre): la maggior parte degli studenti ha un orchestratore funzionante. Non so quanti restano senza, né dove si sono bloccati: serve ancora un punto di partenza per chi non ce l'ha.

## Decisioni del docente (19 novembre 2026)

1. Due direttrici distinte: A, un «feedback processor» associato all'orchestratore; B, l'esplorazione di Unsloth Studio e opencode.
2. Il feedback processor chiude il ciclo completo: esiti → classificazione → proposta di correzione → nuova prova.
3. Si parte dall'orchestratore costruito nella lezione 5.
4. Strumento scelto liberamente dagli studenti (Copilot, Unsloth Studio, opencode) per il processore, senza obbligo di provarne uno diverso. Onere e onore della scelta sono dello studente. Il filone B (esplorazione di Studio e opencode) resta un'attività distinta, come chiesto dal collega.
5. Durata: 1 h 50 min come la lezione 5.
6. Blocco 3 ridotto a un solo giro di correzione, senza iterazioni.
7. Il feedback processor può girare anche in Unsloth Studio e in opencode: secondo il docente (19 novembre 2026) l'importazione dell'agente è facile in entrambi. Non l'ho verificato: l'orchestratore della lezione 5 è fatto di istruzioni di sistema e file di competenze (`skill_guasti.md` e simili), e il passaggio in Studio (campo System Prompt) e in opencode (file degli agenti con permessi) va provato prima dell'aula.
8. Filone B a libertà totale: nessuna domanda concreta per strumento, ognuno decide che cosa esplorare in Studio e opencode. Le due righe della tabella del filone B sono idee di partenza, non consegne.

## Filo della lezione

Filone A: richiesta → orchestratore → esito → feedback processor → correzione → nuova prova. Filone B: esplorazione autonoma di Unsloth Studio e opencode.

## Struttura

| Blocco | Azione dello studente | Risultato visibile |
| --- | --- | --- |
| 1 · Riapertura e registro delle prove | Riapre il proprio orchestratore. Prima scrive il criterio con cui giudicherà una risposta. Poi fa 4–5 richieste: una per ciascuna delle tre skill, una ambigua, una che con il suo ruolo non gli è permessa (utente che chiede il registro). Compila il registro: richiesta, skill chiamata, risposta, giudizio (`OK`, `ERRORE`, `NON_ESEGUITO`). | Tabella con celle vuote, compilata dallo studente. |
| 2 · Il feedback processor | Scrive le istruzioni di un secondo agente che legge il registro e per ogni `ERRORE` indica il tipo (instradamento sbagliato, skill sbagliata, dato inventato, permesso violato), la causa probabile e una modifica precisa alle istruzioni di routing o a una skill. Sceglie lo strumento. | Proposta scritta dal processore, da leggere e controllare. |
| 3 · Un giro di correzione | Valuta la proposta (è giusta? è sul testo giusto?). Applica la modifica a mano. Ripete le richieste fallite e confronta prima e dopo. Una proposta sbagliata o da ignorare si porta alla discussione con la classe. | Esito prima/dopo per ogni richiesta ripetuta. |
| 4 · Discussione | Si guarda alla lavagna una proposta riuscita e una da scartare. Criterio: che cosa rende una correzione utile e che cosa la rende pericolosa (peggiora un'altra skill, aggira un permesso). | Criteri scritti insieme. |

## Filone B · Esplorazione di Unsloth Studio e opencode (direttrice distinta)

Il collega ha chiesto due direttrici distinte: il filone A (blocchi 1–4) è il ciclo del feedback processor, il filone B è un'attività autonoma di esplorazione dei due strumenti, che non dipende dal ciclo. La scelta libera dello strumento vale dentro il filone A (dove far girare il processore) e dentro il filone B (da quale dei due partire).

Proposta, da approvare (il docente non ha ancora fissato il contenuto del filone B; ripartire da quanto fatto in lezione 5, dove avete visto le interfacce, provato la temperatura in Studio e creato la dashboard `.html` con opencode):

| Strumento | Esplorazione proposta | Risultato visibile |
| --- | --- | --- |
| Unsloth Studio | Lo studente sceglie una richiesta e la prova con istruzioni di sistema e temperatura diverse. Guarda come cambiano lunghezza, forma e correttezza, e quando si riempie il contesto. | Due risposte affiancate e la differenza scritta in una riga dallo studente. |
| opencode | Lo studente estende la dashboard `.html` (nuovi dati o una nuova sezione), prima in modalità Plan e poi in Build, leggendo i permessi prima di approvare. | La pagina modificata, aperta nel browser. |

Ogni studente parte da uno dei due e può passare all'altro. Obiettivo dichiarato: capire che cosa si può chiedere a ciascuno strumento e dove si ferma, non produrre una consegna.

Il blocco 3 a un solo giro di correzione serve a lasciare spazio a B. Il filone B va aperto alla fine, quando il ciclo A è chiuso; chi finisce prima in A comincia B prima. Stima dei tempi: nel rapporto del revisore, non nei materiali.

Il processore può girare in tutti e tre gli strumenti, orchestratore compreso. Quindi chi sceglie Studio o opencode per il filone A ci lavora già: in B approfondisce lo stesso strumento (altre richieste, altre impostazioni) oppure passa all'altro, a sua scelta. Nessun obbligo di cambiare.

- **Copilot (A):** il processore è un secondo agente o una conversazione con le istruzioni nel primo messaggio.
- **Unsloth Studio (A):** il processore usa il modello della macchina virtuale. Il registro va incollato; il modello da 2B è lento e può non rispettare il formato.
- **opencode (A):** il registro sta in un file, il processore legge il file e scrive la proposta in un altro file. Il programma chiede permesso prima di scrivere in modalità Build. Il modello scelto e la rete vanno controllati (Big Pickle in rete; indirizzo condiviso della scuola).

Rischio: nel filone B ognuno si ferma al facile (per esempio solo la temperatura). Il docente decide se dare una domanda concreta a ciascuno strumento.

## Cose da non fare

- Il processore non applica da solo le modifiche: propone, lo studente applica. Va dichiarato come proposta di testo, non azione eseguita.
- Nessuna aspettativa che l'orchestratore sbagli: un registro con tutti `OK` è valido, ma deve avere un criterio scritto prima e gli studenti devono inventare casi critici (regola del progetto sugli esercizi).
- Nessun controllo incrociato tra studenti: lavoro singolo (decisione del 10 novembre 2026, vale finché il docente non dice altro).
- Non presentare testi preparati a mano come risposte vere del modello.

## Da verificare prima dell'aula

| Controllo | Perché conta |
| --- | --- |
| Quanti studenti hanno un orchestratore funzionante e dove (Copilot, Studio, opencode) | Il ciclo parte da lì. Per chi non ce l'ha serve un punto di partenza, come `studenti/da_pubblicare_a_chi_non_ha_il_file/` in lezione 5. |
| Il feedback processor in Copilot con l'account studente | Non provato. Non dichiarare provati creazione e comportamento dell'agente. |
| Il processore in Studio (modello da 2B) | Lentezza e rispetto del formato non provati. Il contesto (8192 token) potrebbe non contenere registro e istruzioni insieme. |
| Il processore in opencode | Lettura e scrittura di file, permessi, rete della scuola con indirizzo condiviso. |
| Lunghezza del registro delle prove | Con 4–5 richieste deve restare breve da incollare e da leggere. |
| Importare l'orchestratore e il processore in Studio e in opencode | Affermato dal docente come facile, non provato da me. In Studio le istruzioni vanno nel campo System Prompt e il modello da 2B potrebbe non seguire il routing a tre competenze. In opencode i file degli agenti hanno un formato proprio (intestazione con modalità e permessi). Provare entrambi con i testi della lezione 5. |

### TODO: informazioni da chiedere al docente prima dei materiali

- [ ] Quanti studenti non hanno un orchestratore funzionante, e serve per loro un punto di partenza (orchestratore base, non presentato come soluzione).
- [ ] Dove si sono bloccati gli studenti nei 70 minuti dell'orchestratore (competenze, routing, ruoli admin e utente), per costruire esempi e registro delle prove.
- [ ] In quale strumento hanno costruito l'orchestratore (Copilot, Studio, opencode).
- [ ] Prova dell'importazione di orchestratore e processore in Studio e in opencode, prima dell'aula.

## Decisioni dell'utente del 19 novembre 2026 (seconda parte)

- Procedere con i materiali.
- L'orchestratore è stato costruito in tutti e tre gli strumenti, Copilot soprattutto; gli studenti possono adattarlo agli altri programmi.
- Serve un punto di partenza per chi non ha l'orchestratore: lo schema dell'esercizio della lezione 5. Il file e lo schema non erano nel repository: il punto di partenza è costruito dalla descrizione di questo piano, in `studenti/da_pubblicare_a_chi_non_ha_l_orchestratore/`. Da confrontare con l'esercizio originale.
- Dove si sono bloccati: in tutte e tre le parti (competenze, routing, ruoli).
- Filone B: libertà totale.

## Stato

Prodotti: 32 slide (PowerPoint, HTML, PDF; 25–30 sono la miniguida per portare orchestratore e agente delle correzioni in Studio e in opencode), consegna (Word, PDF), guida docente (Word, PDF), generatore `docente/genera_materiali.py`, testo di partenza dell'orchestratore, esempio di istruzioni dell'agente delle correzioni (da pubblicare dopo la prova), due file di partenza per gli agenti di opencode (`docente/MODELLI_OPENCODE_LEZIONE6/`). Parole per gli studenti: quaderno delle prove, giudizio, agente delle correzioni (il registro resta solo quello del noleggio). Decisione del docente del 20 novembre 2026: niente pizzeria, gli esempi sono sul noleggio Ruota Libera (il caso degli studenti); per non anticipare le soluzioni le richieste degli studenti sono escluse dagli esempi e il criterio d'esempio è volutamente debole. Restano: prove con l'account studente e le verifiche della tabella pre-aula della guida.

## Rinviato

Materiale RAG (ChunkViz, BM25, documento aggiornato), istruzioni nascoste, tabella dei permessi: slittano alla lezione 7 o restano fuori. Da decidere insieme al piano della lezione 7.
