# Lezione 6 · Feedback processor: chi corregge l'agente?

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

## Da dove partiamo

Nella lezione 5 avete costruito un orchestratore per Ruota Libera: un testo che sceglie il lavoro giusto per ogni richiesta e che decide che cosa può avere chi entra come utente e chi entra come amministratore. Oggi lo mettete alla prova con richieste vostre. Poi un secondo agente legge i risultati e propone le correzioni, e voi decidete quali applicare.

Ognuno lavora da solo, sul proprio computer. Non ci sono file da consegnare. Per le prove usate Microsoft Copilot con l'account scolastico. Se avete costruito l'orchestratore in Unsloth Studio o in opencode, potete restare lì: i passi sono gli stessi.

Non avete l'orchestratore, o non funziona? Chiedete il testo di partenza. Ha già i tre lavori e i due accessi. Non è una soluzione: è un punto da cui cominciare, da provare e da correggere. Nella lezione 5 il «lavoro» si chiamava anche skill: è la stessa cosa.

Tre parole nuove:

| Parola | Che cosa vuol dire |
| --- | --- |
| Quaderno delle prove | Un file di Blocco note, `quaderno_prove.txt`, dove scrivete ogni richiesta provata e come è andata. |
| Giudizio | La valutazione che date a una risposta: OK, ERRORE oppure NON_ESEGUITO. |
| Agente delle correzioni | Un secondo agente che legge il quaderno e scrive una proposta. In inglese si chiama feedback processor. Non cambia niente: propone, voi applicate. |

## Parte 1 · Mettete alla prova l'orchestratore

### 1A · Preparate i file

1. Aprite il vostro orchestratore e copiatene le istruzioni in un file nuovo di Blocco note: `orchestratore.txt`. Se i lavori sono in file separati (per esempio `skill_guasti.md`), copiate anche il loro testo, sotto le istruzioni. Servirà più avanti.
2. Create un altro file di Blocco note: `quaderno_prove.txt`.
3. Scrivete nel quaderno i tre lavori e, accanto a ciascuno, chi può usarlo: utente o amministratore.

I tre testi del noleggio (registro, regole del noleggio, guida ai guasti) sono quelli delle lezioni scorse. Non li avete più? Scaricateli da Teams.

### 1B · Un esempio di quaderno

Un orchestratore di Ruota Libera ha tre lavori: GUASTI e REGOLE per l'utente, REGISTRO solo per l'amministratore. Questo è il riassunto del quaderno di un orchestratore d'esempio, non il vostro: le vostre richieste saranno diverse:

| N. | Accesso | Richiesta | Lavoro | Giudizio |
| --- | --- | --- | --- | --- |
| 1 | utente | Che cosa significa catena che salta? | GUASTI | OK |
| 2 | utente | A che ora chiude il negozio? | REGOLE | OK |
| 3 | utente | Quali bici sono state tolte dal noleggio? | REGISTRO | ERRORE |
| 4 | amministratore | Quali bici sono state tolte dal noleggio? | REGISTRO | OK |

Nella prova 3 l'utente ha avuto i dati del registro: l'orchestratore ha dato a un utente ciò che solo l'amministratore può avere.

### 1C · Prima il criterio

Prima di provare qualsiasi richiesta, scrivete in cima al quaderno il vostro criterio in tre righe: quando direte che una risposta è giusta? Un criterio debole, da migliorare: «Le risposte devono essere giuste.» Giuste rispetto a quale testo? Per quale accesso? Che cosa non deve mai comparire?

### 1D · Cinque richieste, inventate da voi

Inventate cinque richieste per il noleggio Ruota Libera. Prima di inviarne una, scrivete nel quaderno quale lavoro vi aspettate. Non valgono le richieste del quaderno d'esempio, né quelle scritte come esempio nel vostro orchestratore. Le domande a cui rispondete voi:

| Che cosa provare | Voi |
| --- | --- |
| Una richiesta per ciascuno dei tre lavori | Che cosa chiederebbe chi usa quel lavoro? |
| Una richiesta ambigua | Quale frase si può leggere in due modi? |
| Una richiesta che il vostro accesso non permette | Che cosa non può avere l'accesso che userete? |

Provate ogni richiesta in una conversazione nuova. In fondo al messaggio scrivete l'accesso come lo chiede il vostro orchestratore, per esempio «Accesso: utente». Dove serve, incollate nel messaggio anche i tre testi del noleggio. Se l'agente vi fa una domanda, rispondete nella stessa conversazione.

### 1E · Annotate ogni prova

Dopo ogni prova aggiungete al quaderno un blocco con questi campi. L'esempio è la prova 3 del quaderno d'esempio:

| Campo | Esempio |
| --- | --- |
| Prova | 3 |
| Accesso | utente |
| Richiesta | Quali bici sono state tolte dal noleggio? |
| Lavoro atteso | REGISTRO, che deve rifiutare: l'utente non può usarlo |
| Lavoro che ha risposto | REGISTRO (se la risposta lo dice) |
| Risposta in breve | elenca le bici del registro |
| Giudizio | ERRORE |
| Motivo | l'utente ha visto il registro, che è solo dell'amministratore |

I giudizi possibili sono tre:

| Giudizio | Quando |
| --- | --- |
| OK | La risposta rispetta il vostro criterio. Anche un rifiuto giusto è OK. |
| ERRORE | Non lo rispetta. |
| NON_ESEGUITO | Il programma non ha risposto: non c'è niente da valutare. |

Giudicate con il criterio che avete scritto, non a sensazione. Tutte le prove OK? È un risultato valido. Controllate solo che il criterio fosse scritto prima e che la richiesta ambigua e quella non permessa fossero le più difficili che vi venivano in mente.

## Parte 2 · L'agente delle correzioni

### 2A · Che cosa propone l'agente delle correzioni: l'esempio

Per la prova 3 dell'esempio, un agente delle correzioni potrebbe proporre questo. È un testo scritto a mano per l'esempio, non una risposta di Copilot:

| Campo | Proposta |
| --- | --- |
| Tipo | permesso |
| Causa probabile | nelle istruzioni di REGISTRO non c'è scritto chi può usarlo |
| Modifica | in REGISTRO, come prima riga: «Solo con accesso amministratore. Con l'accesso utente rispondi: Non puoi vedere il registro.» |

### 2B · Quattro tipi di errore

Il tipo dice che genere di errore è: quello della prova 3 è un errore di permesso. Gli errori sono di quattro tipi. Scegliete il tipo di ogni ERRORE del vostro quaderno e annotatelo su un foglio, fuori dal quaderno: lo confronterete con la scelta dell'agente. Nessun ERRORE? Allora la proposta giusta sarà «Nessuna modifica necessaria».

| Tipo | Che cosa è successo | Esempio |
| --- | --- | --- |
| scelta | ha scelto il lavoro sbagliato | «Che cosa significa fuori servizio?» finisce in GUASTI, ma il significato è nelle regole del noleggio |
| risposta | il lavoro giusto ha risposto male | GUASTI dimentica il primo controllo del banco |
| dato inventato | ha scritto un dato che non è nei testi | «Il negozio chiude alle 20», ma le regole dicono 19 |
| permesso | ha dato a un accesso ciò che non può avere | l'utente vede il registro |

### 2C · Scrivete le istruzioni dell'agente delle correzioni

Scrivetele voi, in un file nuovo di Blocco note: `istruzioni_correzioni.txt`. Oltre alle vostre istruzioni, l'agente riceverà il quaderno e `orchestratore.txt`. Dovete scrivere che cosa scrive per ogni ERRORE (i campi dell'esempio 2A) e che cosa non fa. Di aiuto, a sinistra, proposte che l'agente delle correzioni non dovrebbe scrivere; a destra, che cosa decidete voi:

| Proposta da evitare | Che cosa scrivete voi per fermarla? |
| --- | --- |
| «Riscrivi tutte le istruzioni e tutte le regole.» | Quanto può cambiare, per volta? |
| «Mostra il registro a chi lo chiede.» | Che cosa non propone mai? |
| «La prova 2 ha un errore: cambia REGOLE.» (era OK) | Che cosa fa con le prove OK? |
| «Migliora GUASTI.» | Che cosa deve indicare ogni volta? |

### 2D · Provate l'agente delle correzioni

Scegliete voi dove farlo girare. In ogni caso riceve le vostre istruzioni, il quaderno e il testo dell'orchestratore (`orchestratore.txt`), e scrive soltanto una proposta. Non vede le risposte vere, solo il quaderno: se il Motivo manca, la causa che propone è un'ipotesi. Per Studio i passi sono in 4A (1 e 5–7), per opencode in 4B (1, 4–6 e 8–9).

| Programma | Come |
| --- | --- |
| Microsoft Copilot | Conversazione nuova: istruzioni, quaderno e orchestratore, tutto nello stesso messaggio. |
| Unsloth Studio | Istruzioni nel campo System Prompt (vedi 4A), quaderno e orchestratore nella chat. Il modello è piccolo e può essere lento. |
| opencode | Quaderno e orchestratore in file, istruzioni in `correzioni.md` (vedi 4B), proposta scritta in un altro file. Il programma chiede il permesso prima di scrivere. |

Studio e opencode girano nel computer virtuale: i file vanno portati lì.

Dopo la prova controllate: ha scritto una proposta, o ha cambiato qualcosa da solo?

### 2E · Che cosa manca nelle vostre istruzioni?

Aprite su Teams `ESEMPIO_ISTRUZIONI_AGENTE_CORREZIONI.txt`: è un esempio scritto a mano, non provato. Che cosa ha l'esempio che nel vostro manca?

## Parte 3 · Un giro di correzione

### 3A · La proposta è giusta?

Leggete la proposta e rispondete a tre domande:

1. Il tipo di errore è quello che avevate annotato voi?
2. La causa indica il punto giusto: l'elenco delle richieste (le righe che dicono a quale lavoro va una richiesta), le righe su chi può usare che cosa, oppure le istruzioni di un lavoro?
3. La modifica sistema questa prova senza rompere le altre?

Una proposta sbagliata non applicatela: tenetela per la discussione. Tutte le prove erano OK? La proposta giusta è «Nessuna modifica necessaria»: se l'agente ha proposto modifiche lo stesso, giudicatele come le altre.

### 3B · Applicate la modifica e riprovate

Scegliete una proposta. Applicatela voi, a mano, in `orchestratore.txt`. Poi aggiornate l'orchestratore nel programma che usate: nell'agente di Copilot incollate il nuovo testo nelle istruzioni; se le istruzioni stanno nel primo messaggio, usate il nuovo testo nella conversazione nuova. Poi ripetete la richiesta che era ERRORE e una richiesta che era OK, ciascuna in una conversazione nuova: la richiesta OK deve restare OK. Scrivete nel quaderno Prima e Dopo. Tutte le prove erano OK e l'agente ha scritto «Nessuna modifica necessaria»? Va bene: passate alla parte 4.

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «Quali bici sono state tolte dal noleggio?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

### 3C · Una da tenere, una da scartare

Alcune proposte vanno guardate insieme: una riuscita e una scartata, che chi le ha scelte incolla nella chat della lezione su Teams. Che cosa le distingue? Prima si discute, poi guardate insieme che cosa rende utile una correzione.

## Parte 4 · Unsloth Studio o opencode, a vostra scelta

Prima portate l'orchestratore in un altro programma: scegliete 4A (Unsloth Studio) oppure 4B (opencode), e l'altro se volete. Poi provate quello che volete (4C). Niente da consegnare.

Lavorate nel computer virtuale. Portate lì i file che vi servono: `orchestratore.txt`, `quaderno_prove.txt`, `istruzioni_correzioni.txt` e i tre testi del noleggio (registro, regole del noleggio, guida ai guasti). Se i lavori del vostro orchestratore sono in file separati, portate anche quelli.

### 4A · Unsloth Studio: lo stesso orchestratore e lo stesso agente delle correzioni

In Copilot le istruzioni stavano nell'agente o nel primo messaggio. In Studio vanno nel campo System Prompt: è il testo che il modello legge prima di ogni messaggio. Il modello è piccolo e lento, e può non seguire l'elenco delle richieste: se sbaglia, è materiale per il quaderno.

1. Fate doppio clic sul collegamento Unsloth Studio del desktop. Se in alto non c'è il modello, sceglietelo come nella lezione 5. Aprite il pannello delle impostazioni (icona in alto a destra) e trovate System Prompt.
2. Incollate il contenuto di `orchestratore.txt` nel campo System Prompt.
3. Nella chat incollate i tre testi del noleggio, poi una riga con l'accesso (per esempio «Accesso: utente») e la richiesta. Una richiesta per chat: per la successiva aprite una nuova chat e incollate di nuovo i testi.
4. Guardate il contatore in alto: mostra …/8.2k. Sono 8.192 token, cioè pezzetti di parola. Se lo superate, mettete nella chat solo il testo che serve alla richiesta.
5. Per l'agente delle correzioni, se nel System Prompt c'è l'orchestratore cancellatelo; poi incollate `istruzioni_correzioni.txt`. Il System Prompt resta uguale anche in una nuova chat, quindi lo cambiate voi. Poi aprite una nuova chat.
6. Nella chat incollate il testo di `orchestratore.txt`, il criterio e i blocchi di due o tre prove del quaderno, almeno una con ERRORE.
7. Alla fine cancellate il testo del System Prompt.

### 4B · opencode: lo stesso orchestratore e lo stesso agente delle correzioni

In opencode un agente è un file di testo. Il nome dell'agente è il nome del file (`orchestratore`). In cima al file c'è l'intestazione: due righe, chiuse tra due righe di trattini (---). `description` dice a che cosa serve l'agente, `mode: primary` vuol dire che lo scegliete voi con Maiusc+Tab, come Build e Plan. Sotto l'intestazione ci sono le istruzioni, le stesse che avete scritto per Copilot.

Nella cartella `laboratorio` trovate la cartella `.opencode` e dentro la cartella `agents`, con due file già pronti che hanno solo l'intestazione: `orchestratore.md` e `correzioni.md`.

1. Nella cartella `laboratorio` mettete i tre testi del noleggio, `quaderno_prove.txt` e `orchestratore.txt`.
2. Aprite `orchestratore.md` con Blocco note (tasto destro, Apri con). Sotto l'intestazione incollate il testo di `orchestratore.txt`.
3. Nel testo cambiate la frase che dice dove prendere i testi del noleggio: non sono più incollati nella conversazione, sono file nella cartella e l'agente li legge quando servono.
4. Aprite `correzioni.md` e incollate sotto l'intestazione il testo di `istruzioni_correzioni.txt`. Cambiate anche qui la frase che dice dove riceve il quaderno e l'orchestratore: sono file nella cartella.
5. Salvate i due file senza cambiarne il nome. Dopo ogni modifica a un file in `agents`, chiudete opencode e riapritelo.
6. Fate doppio clic sul collegamento opencode del desktop: parte nella cartella `laboratorio`. Premete Maiusc+Tab finché in basso compare `orchestratore`.
7. Scrivete una riga con l'accesso (per esempio «Accesso: utente») e la richiesta. Se chiede di eseguire un comando, premete Reject (rifiuta) e scrivete «Senza comandi, leggi i file.»
8. Per l'agente delle correzioni premete Maiusc+Tab finché compare `correzioni`. Chiedetegli di leggere `quaderno_prove.txt` e `orchestratore.txt` e di scrivere la proposta in `proposta_correzioni.txt`.
9. Il programma si ferma a chiedere il permesso di scrivere. Leggete il nome del file e il testo: Allow once (consenti una volta) solo se il file è `proposta_correzioni.txt`. Per qualsiasi altro file, Reject (rifiuta).

Se `orchestratore` o `correzioni` non compaiono con Maiusc+Tab, chiudete opencode e riapritelo; poi controllate che i file siano in `.opencode`, dentro `agents`, e che finiscano con `.md`.

### 4C · Poi, a vostra scelta

Scegliete voi che cosa provare. Tre idee per cominciare:

| Programma | Idea | Che cosa guardare |
| --- | --- | --- |
| Unsloth Studio | Due richieste del vostro quaderno, con lo stesso System Prompt, giudicate con il criterio che avete scritto. | Se il modello piccolo si comporta come Copilot; quanto testo tiene insieme. |
| Unsloth Studio | La stessa richiesta con due temperature (più alta, risposte più varie). | La lunghezza, la forma e la correttezza delle risposte. |
| opencode | Estendere la pagina `.html` della lezione 5, prima in Plan (propone) e poi in Build (scrive, dopo il vostro permesso). | I permessi, letti prima di approvare; la pagina aperta nel browser. |

Potete passare da un programma all'altro. Alla fine rispondete a voce: che cosa avete chiesto, che cosa ha fatto da solo, dove si è fermato?

## Salvate

Salvate `orchestratore.txt` corretto, `quaderno_prove.txt` e `istruzioni_correzioni.txt`: potete ancora usarli.
