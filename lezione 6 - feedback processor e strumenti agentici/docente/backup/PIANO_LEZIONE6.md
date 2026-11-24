# Piano della lezione 6 · 25 novembre 2026

Documento riservato al docente. Sostituisce la lezione 6 «Agenti, permessi e difese» e il blocco RAG di `lezione 4 - reti neurali e agenti con orchestrazione/docente/backup/BOZZA_PERCORSO_LEZIONI_4-7.md`, che slittano o restano materiale in attesa.

## Che cosa è successo in lezione 5 (riferito dal docente il 19 novembre 2026)

- Durata: 1 h 50 min piena.
- Orchestratore: esercizio `lezione 5 - orchestratore, Unsloth Studio e opencode/esercizio sistema agentico.md` più lo schema `system prompt routing interno esternojpg.jpg`. Ha occupato circa 70 minuti. Struttura: login admin o utente; tre skill (guasti → admin o utente, preferibilmente utente; registro → solo admin; regole di noleggio → solo utente) sul caso Ruota Libera; istruzioni di routing nell'agente, con esempi di rinforzo positivo.
- Unsloth Studio: interfaccia mostrata, qualche prova con la temperatura.
- opencode: interfaccia mostrata, dashboard in `.html` creata con opencode.
- Stato a fine lezione: la maggior parte degli studenti ha un orchestratore funzionante. Non so quanti restano senza: serve un punto di partenza.

## Decisioni del docente

Del 19 novembre 2026 (ancora valide):
1. Si parte dall'orchestratore costruito nella lezione 5.
2. Durata: 1 h 50 min come la lezione 5.
3. Un solo giro di correzione, senza iterazioni.
4. Il lavoro è singolo: niente controlli incrociati tra studenti.

Del 23 novembre 2026: la ripetizione dopo la correzione usa la richiesta sbagliata scritta con altre parole. Il permesso di GUASTI è come nell'originale (utente e amministratore). La parola «feedback processor» sta nel titolo.

Del 24 novembre 2026, dopo la prima versione (lo studente scriveva le istruzioni di un «agente delle correzioni»): quella versione faceva rifare all'agente quello che lo studente aveva già scritto nel quaderno ed era soprattutto burocrazia con file. Nuovo disegno:
1. Lo studente corregge a mano un errore e solo dopo confronta con Copilot.
2. opencode in modalità Build modifica il file dell'orchestratore, dopo il permesso dello studente.
3. Si confrontano tre correzioni: dello studente, di Copilot, di Build.
4. Tolti: istruzioni dell'agente scritte dagli studenti, quattro tipi di errore, Unsloth Studio, esempio di istruzioni dell'agente, estensione della pagina `.html`.

Del 24 novembre 2026, sera, per alleggerire la lezione: tolti il caso d'esempio «fuori servizio» con le correzioni A e B (consegna 5C, slide 27) e la prova dell'orchestratore dentro opencode dopo la modifica di Build (consegna 4B passo 5, slide 22). Il Prima e Dopo resta quello della parte 5 (slide 25).

## Struttura

| Blocco | Azione dello studente | Risultato visibile |
| --- | --- | --- |
| 1 · Le prove | Scrive il criterio. Inventa cinque richieste (una per ciascun lavoro, una ambigua, una non permessa). Le prova in Copilot e le annota nel quaderno con accesso, richiesta, risposta, giudizio, motivo. | Il quaderno compilato. |
| 2 · La correzione dello studente | Prende il primo ERRORE e scrive Causa e Modifica in `mia_correzione.txt`, senza applicarla. | Una correzione scritta da lui. |
| 3 · Copilot come feedback processor | Scrive lui la richiesta a Copilot (quaderno e orchestratore, senza la propria correzione) e legge la proposta. | La correzione di Copilot. |
| 4 · opencode in Build | Porta nel computer virtuale i file, prepara `orchestratore.md`, scrive la richiesta a Build, legge la modifica e approva o rifiuta. | `orchestratore.md` modificato, o rifiuto motivato. |
| 5 · Tre correzioni, una sola | Confronta con quattro domande, tiene una (o un mix), la applica in `orchestratore.txt`, riprova con la richiesta riscritta e una richiesta OK. | Prima e Dopo nel quaderno; criteri discussi dopo la prova. |

## Cose da non fare

- Nessun agente applica da solo le modifiche, salvo Build in `orchestratore.md` dopo il permesso: va dichiarato.
- Nessuna aspettativa che l'orchestratore sbagli: un quaderno con tutti `OK` è valido, ma il criterio va scritto prima e le richieste difficili devono esserlo davvero.
- La correzione dello studente non va incollata né in Copilot né in opencode: altrimenti il confronto non è onesto.
- Non presentare testi preparati a mano come risposte vere del modello.

## Da verificare prima dell'aula

Vedi la tabella dei controlli nella guida docente. I rischi maggiori: Copilot con messaggi lunghi e account studente; Build con il permesso di scrittura in `.opencode\agents` e la finestra con la modifica; come portare i file nel computer virtuale.

## Stato

Prodotti: 27 slide (PowerPoint, HTML, PDF), consegna (Word, PDF), guida docente (Word, PDF), generatore `docente/genera_materiali.py`, testo di partenza dell'orchestratore, file di partenza dell'agente di opencode (`docente/MODELLI_OPENCODE_LEZIONE6/orchestratore.md`). Gli esempi sono tutti sul noleggio Ruota Libera (decisione del 20 novembre: niente pizzeria): l'errore d'esempio della correzione è un dato inventato (orario), diverso dal permesso che quasi tutti avranno nel quaderno. Restano: prove con l'account studente e le verifiche della guida.

## Rinviato

Materiale RAG (ChunkViz, BM25, documento aggiornato), istruzioni nascoste, tabella dei permessi: slittano alla lezione 7 o restano fuori. Da decidere insieme al piano della lezione 7.
