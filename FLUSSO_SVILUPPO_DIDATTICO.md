# Come sviluppiamo i materiali didattici

Procedura del progetto, aggiornata l'11 novembre 2026. È per chi prepara le lezioni, non per gli studenti. Si applica alle nuove lezioni e alle revisioni richieste, senza cambiare retroattivamente le altre. Le decisioni del docente e `AGENTS.md` prevalgono sulle indicazioni dei progetti esterni.

## Il problema da evitare

Un generatore può produrre documenti coerenti ma una lezione poco interessante. Scrivere una previsione, compilare un registro e farlo controllare non sono, da soli, un'attività didattica. Aggiungere punti a una procedura noiosa non la rende significativa.

La domanda di partenza è: che cosa lo studente potrà scegliere, costruire o scoprire che prima non sapeva fare? Solo dopo decidiamo che cosa proiettare e che cosa scrivere nella consegna.

## Il nostro flusso

1. **Fissare il compito.** L'agente principale raccoglie obiettivo osservabile, decisioni del docente, strumenti realmente disponibili e fonti. Distingue «richiesto», «proposto» e «provato». Sceglie una prova finale che richieda di usare ciò che si è imparato, non di ripeterne la definizione.
2. **Progettare l'esperienza.** Un secondo modello propone alternative su una parte delimitata della lezione. Per questa revisione è stato usato Claude Fable 5.1, con ragionamento alto. Ogni proposta deve dire: che scelta compie lo studente; quale risultato vede; come distingue un buon risultato; quale concetto impara; che cosa può non funzionare. Il revisore creativo non modifica i materiali approvati. Se un modello richiesto non è disponibile, lo si segnala senza sostituirlo in silenzio.
3. **Scegliere prima di impaginare.** L'agente principale scarta le idee decorative, le dipendenze inutili e le attività che richiedono un errore del modello per riuscire. Presenta al docente i cambiamenti strutturali prima di applicarli. Conserva spazi in cui lo studente inventa casi o decide una soluzione propria.
4. **Scrivere per due lettori diversi.** La consegna accompagna lo studente nel lavoro: dove agire, che cosa provare, quale risultato cercare. Le slide accompagnano la conversazione in aula: domande, risultati, confronti e decisioni. La guida dice al docente come condurre e interpretare quei passaggi. Non sono tre copie dello stesso testo.
5. **Provare il percorso centrale.** Aprire gli strumenti reali e compiere la prova richiesta; per i numeri usare le fonti originali e lo script della lezione. Una simulazione scritta da un modello può trovare ambiguità, ma non prova apprendimento, accesso con account scolastico o tempi d'aula. Le verifiche non eseguibili restano esplicitamente nella tabella pre-aula.
6. **Generare e guardare.** Il generatore impagina testi già scritti; non stabilisce la struttura didattica. Si aprono i formati effettivi, si controllano tutte le pagine, si prova la navigazione HTML. Valori e risposte di riferimento derivano dagli originali, non da copie manuali.
7. **Revisione indipendente.** Il `revisore-didattico` esistente, con Claude Opus 5.5 e ragionamento alto, esamina i materiali generati dopo le prove di apertura e impaginazione. Segnala problemi con posizione precisa, impatto e correzione. L'agente principale corregge quelli importanti, rigenera e ripete la revisione. I cambiamenti di struttura tornano al docente. La stima dei tempi resta nel rapporto del revisore, mai nei materiali.

Non serve un nuovo servizio di orchestrazione: l'agente principale assegna i compiti, conserva le decisioni e integra i risultati. Fable propone esperienze; chi scrive i materiali cura la lingua; Opus verifica il risultato indipendentemente. Non si contano i pareri come voti e non si sommano agenti per aumentare artificialmente la fiducia.

## Il controllo editoriale prima della generazione

- Leggere ogni slide come una battuta da dire in aula. Se richiede una lettura lunga, spostare i dettagli nella consegna.
- Verificare che domande e richieste arrivino prima delle risposte. I criteri si mostrano dopo il tentativo, non tutti insieme all'inizio.
- Una prova riuscita subito è valida. Una correzione riuscita vale quanto una prima risposta riuscita: non si premia la fortuna del modello.
- Eliminare appunti e tabelle che nessun passaggio usa. Salvare ciò che serve davvero per continuare il lavoro.
- Verificare che ciascun risultato possa essere riconosciuto con criteri comprensibili, non soltanto con «il docente controlla».
- Chiedersi se lo studente sta progettando qualcosa oppure sta eseguendo le nostre istruzioni complete. Se decide solo dove incollare, riprogettare.
- Leggere ogni slide come uno studente alle prime armi: so che cosa fare adesso, dove, e conosco ogni parola? Le regole sono in «Chiarezza didattica» di `AGENTS.md`.

## Ricerca online: che cosa esiste e che cosa prendiamo

Fonti primarie lette il 10 novembre 2026. Questa è una ricognizione di procedure e strumenti disponibili, non una dimostrazione che rendano efficace una lezione ITS. Non sono state copiate skill, rubriche, codice o testi per gli studenti e non è stato installato alcun pacchetto.

| Risorsa | Stato e versione consultata | Che cosa è utile qui | Limite e decisione |
| --- | --- | --- | --- |
| [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Articolo del 19 dicembre 2024; pagina consultata il 10 novembre 2026, aggiornata il 9 ottobre | Scomposizione in passi; valutatore distinto dall'autore; correzione guidata da criteri espliciti | Pattern generali documentati, non ricerca sull'apprendimento. Adottiamo la separazione autore/revisore già supportata dagli strumenti, senza nuovo framework. Collegamento e analisi originale; nessuna riproduzione di testo o figure, nessuna licenza di riuso del sito accertata. |
| [Anthropic / Learning Commons — K-12 Teacher Skills](https://github.com/anthropics/k12-teacher-skills) | Versione 0.10.0, commit `31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c`; [licenza Apache-2.0](https://github.com/anthropics/k12-teacher-skills/blob/31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c/LICENSE) letta | Pianificazione, preparazione della lezione, controlli di comprensione; materiali coerenti da una sorgente comune; criteri che distinguono ragionamento da esecuzione meccanica | È dichiarato incluso in Claude for Teachers: disponibilità concreta, non prova di efficacia per il nostro pubblico. È rivolto alla scuola K–12 e a curricoli statunitensi. Non importiamo collegamenti al Knowledge Graph, griglie di osservazione né tempi obbligatori. Manteniamo generatore e modello ITS. |
| [Gareth Manning — Education Agent Skills](https://github.com/GarethManning/education-agent-skills) | Versione 3.1.0, 22 ottobre 2026; [licenza CC BY-SA 4.0](https://github.com/GarethManning/education-agent-skills/blob/main/LICENSE) letta | Catalogo di 165 procedure didattiche, utile da consultare selettivamente per un bisogno preciso | Il README distingue compatibilità tecnica da efficacia didattica e avverte che il servizio MCP pubblico è stato ritirato. Non installiamo tutto e non attribuiamo validazione in aula a questa raccolta. Un eventuale adattamento di contenuto richiederebbe attribuzione e rispetto della condivisione allo stesso modo. |
| [Agent Skills](https://agentskills.io/home) | Documentazione web consultata il 10 novembre 2026 | Formato portabile per istruzioni e risorse, attivate quando servono | Un formato, non un metodo didattico né una garanzia di qualità. Per ora bastano questa procedura e il richiamo in `AGENTS.md`; non è stata verificata l'attivazione automatica di skill locali in questo progetto. Nessun file dello standard è redistribuito. |

Sono state lette direttamente la [skill di pianificazione](https://github.com/anthropics/k12-teacher-skills/blob/31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c/plugin/skills/k12-lesson-plan-creation/SKILL.md), la [skill di preparazione](https://github.com/anthropics/k12-teacher-skills/blob/31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c/plugin/skills/k12-lesson-prep/SKILL.md) e la [rubrica comune](https://github.com/anthropics/k12-teacher-skills/blob/31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c/evals/k12-lesson-plan-creation/rubrics/shared.csv), non soltanto il riepilogo di un motore di ricerca. Le ricerche hanno proposto anche sistemi accademici; non li trattiamo come strumenti affermati o pronti da integrare senza verificarne implementazione, licenza e risultati.

## Ricerca sulla chiarezza espositiva

Ricerca online dell'11 novembre 2026, dopo il giudizio del docente che la seconda metà della lezione 4 era «incomprensibile». Sono principi generali su altri pubblici: non provano l'efficacia sul nostro. Qui non sono stati riletti gli articoli originali per intero. La prova resta l'aula e la lettura del revisore.

| Principio | Fonte | Come lo applichiamo |
| --- | --- | --- |
| Quadro d'insieme prima dei dettagli | Ausubel, organizzatori anticipati (1960) | Slide 3 (due modi di cambiare un'AI) e slide 18–19 della lezione 4 |
| Esempio svolto prima del problema | Sweller e Cooper (1985); teoria del carico cognitivo | Bici 5 calcolata davanti agli studenti, poi la bici 12 con il loro agente |
| Dal concreto al nome | Fyfe, McNeil, Son e Goldstone, «Concreteness fading» (Educational Psychology Review, 2014) | Le frasi vere della pizzeria prima dei nomi delle parti |
| Un'idea alla volta; togliere il superfluo; testo e tabella vicini | Mayer, Multimedia Learning (principi di segnalazione, coerenza, contiguità) | Una sola azione per slide; tabella che affianca esempio e compito |
| Testo e immagine insieme, immagine dove serve (codifica doppia) | Mayer, Multimedia Learning (principi di contiguità e di segnalazione); Paivio, teoria della codifica doppia | Schermate dei siti con il punto da trovare cerchiato (slide 5–16) |
| Piccoli passi, controlli frequenti, pratica guidata poi autonoma | Rosenshine, «Principles of Instruction» (American Educator, 2012) | Previsioni e alzate di mano, criterio dopo la prova |

## Applicazione nella lezione 4

La scelta approvata è Copilot più proiettore, senza nuovi strumenti. Transformer ha due bersagli leggibili sulle probabilità; Playground una ricerca del proprio record; Flappy una previsione su una soglia finita, senza fingere che l'osservazione sia un gioco di abilità. L'agente del noleggio dà un primo riscontro prima di essere completo. Le richieste comuni servono a confrontare i criteri; due casi inventati dagli studenti verificano che non si tratti soltanto di seguire le richieste del docente. Rimane un solo file utile: le istruzioni dell'agente.

Le prove dei siti eseguite dai collaboratori riguardano Chromium su Linux e una rete non scolastica. Non dimostrano il funzionamento di Copilot con account studente né la riuscita dell'attività con la classe.
