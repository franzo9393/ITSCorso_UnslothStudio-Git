# Lezione 6 · Feedback processor: chi corregge l'agente?

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot e opencode**

## Da dove partiamo

Nella lezione 5 avete costruito un orchestratore per Ruota Libera: un testo che sceglie il lavoro giusto per ogni richiesta e che decide che cosa può avere chi entra come utente e chi entra come amministratore. Oggi lo mettete alla prova con richieste vostre. Poi scrivete voi una correzione per un errore. Poi due programmi propongono la loro: prima Copilot, sul vostro computer; poi opencode, sul proiettore. Voi confrontate le correzioni, tenete una e riprovate.

Ognuno lavora da solo, sul proprio computer. Non ci sono file da consegnare. Per le prove usate Microsoft Copilot con l'account scolastico. Se avete costruito l'orchestratore in Unsloth Studio o in opencode, copiate il testo in Blocco note: le prove si fanno comunque in Copilot. opencode lo guardate soltanto: non dovete aprirlo.

Non avete l'orchestratore, o non funziona? Alzate la mano: vi arriva il testo di partenza, da copiare in `orchestratore.txt`. Ha già i tre lavori e i due accessi. Non è una soluzione: è un punto da cui cominciare, da provare e da correggere. Nella lezione 5 il «lavoro» si chiamava anche skill: è la stessa cosa.

Tre parole nuove:

| Parola | Che cosa vuol dire |
| --- | --- |
| Quaderno delle prove | Un file di Blocco note, `quaderno_prove.txt`, dove scrivete il criterio, ogni richiesta provata e come è andata, e la correzione. |
| Giudizio | La valutazione che date a una risposta: OK, ERRORE oppure NON_ESEGUITO. |
| Feedback processor | Un programma che legge il quaderno e propone una correzione. Copilot la scrive come testo; opencode in Build la scrive nel file, solo dopo un permesso. Voi decidete se tenerla o scartarla. |

## Parte 1 · Mettete alla prova l'orchestratore

### 1A · Preparate i file

1. Aprite il vostro orchestratore e copiatene le istruzioni in un file nuovo di Blocco note: `orchestratore.txt`. Dove sono le istruzioni: in Copilot, nelle istruzioni dell'agente oppure nel primo messaggio che avete scritto; in Unsloth Studio, nel testo delle istruzioni di sistema; in opencode, nel file dell'agente. Se i lavori sono in file separati (per esempio `skill_guasti.md`, dove `.md` indica un file di testo scritto in Markdown), copiate anche il loro testo, sotto le istruzioni. Servirà più avanti.
2. Create un altro file di Blocco note: `quaderno_prove.txt`. Ha tre parti: CRITERIO, PROVE, CORREZIONE. Scrivete i tre titoli, uno sotto l'altro.
3. Sotto CRITERIO scrivete i tre lavori e, accanto a ciascuno, chi può usarlo: utente o amministratore.

I tre testi del noleggio sono quelli delle lezioni scorse: `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt` e `Guida_guasti_Ruota_Libera.txt`. Teneteli aperti accanto al Blocco note. Non li avete più? Scaricateli da Teams.

### 1B · Un esempio di prove

Un orchestratore di Ruota Libera ha tre lavori: GUASTI per utente e amministratore, REGOLE solo per l'utente, REGISTRO solo per l'amministratore. Questa è la parte PROVE del quaderno di un orchestratore d'esempio. È inventata per l'esercizio, non è una prova eseguita e non è il vostro quaderno: le vostre richieste saranno diverse:

| N. | Richiesta, con l'accesso | Esito atteso | Giudizio | Motivo |
| --- | --- | --- | --- | --- |
| 1 | utente: Che cosa significa catena che salta? | GUASTI | OK | |
| 2 | utente: A che ora chiude il negozio? | REGOLE | OK | |
| 3 | utente: Quali bici sono state tolte dal noleggio? | rifiuto | ERRORE | l'utente ha visto il registro |
| 4 | amministratore: Quali bici sono state tolte dal noleggio? | REGISTRO | OK | |

Nella prova 3 l'utente ha avuto i dati del registro: l'orchestratore ha dato a un utente ciò che solo l'amministratore può avere.

### 1C · Prima il criterio

Prima di provare qualsiasi richiesta, scrivete sotto CRITERIO, sotto l'elenco dei tre lavori, il vostro criterio in tre righe: quando direte che una risposta è giusta? Un criterio debole, da migliorare: «Le risposte devono essere giuste.» Giuste rispetto a quale testo? Per quale accesso? Che cosa non deve mai comparire?

### 1D · Tre richieste, inventate da voi

Inventate tre richieste per il noleggio Ruota Libera. Prima di inviarne una, scrivete nel quaderno l'esito atteso: il lavoro che vi aspettate, una domanda di chiarimento oppure un rifiuto. Non valgono le richieste del quaderno d'esempio, né quelle scritte come esempio nel vostro orchestratore. Le domande a cui rispondete voi:

| Che cosa provare | Voi |
| --- | --- |
| Una richiesta normale, per un lavoro a vostra scelta | Che cosa chiederebbe chi usa quel lavoro? |
| Una richiesta ambigua | Quale frase si può leggere in due modi? |
| Una richiesta che il vostro accesso non permette | Che cosa non può avere l'accesso che userete? |

Provate ogni richiesta in una conversazione nuova. Ogni conversazione nuova parte da zero: il contesto va ricostruito ogni volta.

- Avete un agente di Copilot già configurato? Aprite una conversazione nuova con quell'agente. Incollate nel primo messaggio i tre testi del noleggio, a meno che li abbiate già caricati nell'agente; poi scrivete la richiesta e, in fondo, l'accesso.
- Usate le istruzioni nel primo messaggio? Aprite una conversazione ordinaria e incollate nell'ordine: le istruzioni di `orchestratore.txt`, i tre testi del noleggio, la richiesta e, in fondo, l'accesso.

L'accesso è sempre l'ultima riga, come lo chiede il vostro orchestratore, per esempio «Accesso: utente». Se l'agente vi fa una domanda, rispondete nella stessa conversazione.

### 1E · Annotate ogni prova

Dopo ogni prova aggiungete sotto PROVE una riga con questi campi, come nell'esempio 1B: numero, richiesta con l'accesso, esito atteso, giudizio. Il motivo si scrive solo se il giudizio è ERRORE. Un esempio di riga nel Blocco note: `3 · utente: Quali bici sono state tolte dal noleggio? · rifiuto · ERRORE · l'utente ha visto il registro`. Sotto la riga copiate la risposta ricevuta, senza riscriverla: vi servirà per la parte 3. Se l'agente ha fatto una domanda, copiate l'intero scambio (domanda, vostra risposta e risposta finale) e giudicate la risposta finale. I giudizi possibili sono tre:

| Giudizio | Quando |
| --- | --- |
| OK | La risposta rispetta il vostro criterio. Anche un rifiuto giusto è OK. |
| ERRORE | Non lo rispetta. |
| NON_ESEGUITO | Il programma non ha risposto: non c'è niente da valutare. |

Giudicate con il criterio che avete scritto, non a sensazione. Tutte le prove OK? È un risultato valido. Controllate solo che il criterio fosse scritto prima e che la richiesta ambigua e quella non permessa fossero le più difficili che vi venivano in mente.

## Parte 2 · Correggete voi

### 2A · Una correzione scritta bene: l'esempio

Prova 5 di un altro quaderno d'esempio. L'utente chiede «A che ora chiude il negozio?». L'orchestratore risponde «Alle 20:00», ma le regole del noleggio dicono 19:00. La correzione potrebbe essere questa. Una causa, una modifica:

| Campo | Esempio |
| --- | --- |
| Causa | in REGOLE non c'è scritto di prendere gli orari solo dalle regole del noleggio |
| Modifica | in REGOLE, come prima riga: «Gli orari si prendono solo dalle regole del noleggio. Se non ci sono, scrivi: Dato non presente nel testo.» |

### 2B · La vostra correzione

Prendete il primo ERRORE del vostro quaderno. Sotto CORREZIONE scrivete:

- la **Causa**: che cosa manca nelle istruzioni dell'orchestratore;
- la **Modifica**: il testo preciso da scrivere e il punto dove va.

Il Motivo della prova dice che cosa è andato storto nella risposta. La Causa dice che cosa manca nelle istruzioni. Una sola modifica. Non applicatela ancora: prima la confrontate con quelle dei programmi. Non incollate la parte CORREZIONE in nessuna richiesta: quando incollate il quaderno in Copilot, lasciatela fuori.

Poi guardate la riga che somiglia al vostro quaderno:

| Il vostro quaderno | Che cosa fate |
| --- | --- |
| Almeno un ERRORE, nessun NON_ESEGUITO | Scegliete il primo ERRORE e scrivete Causa e Modifica. Come seconda prova da riprovare dopo scegliete di solito una prova OK; se non ce n'è, un'altra richiesta già eseguita (se non c'è nessuna prova OK, nel quaderno resta il suo giudizio vero, non diventa OK). |
| Tutte OK | Per ogni prova scrivete la frase che conferma la risposta: dal testo del noleggio per i dati, dalle istruzioni o dal criterio per un rifiuto o una domanda di chiarimento (per esempio: «la risposta dice 19:00 come le regole, non c'è niente da aggiungere»). Per le due richieste più difficili scrivete anche perché nessuna modifica le migliorerebbe. Poi scrivete sotto CORREZIONE «nessuna correzione necessaria» e, nella parte 3, seguite il caso «Tutte OK». |
| OK e NON_ESEGUITO, nessun ERRORE | Confermate le prove eseguite come nel caso «tutte OK». Scrivete sotto CORREZIONE «nessun errore nelle prove eseguite; verifica incompleta» e non applicate modifiche. |
| Almeno un ERRORE e almeno un NON_ESEGUITO | Scegliete il primo ERRORE. Se manca una seconda prova da riprovare, scrivete «seconda prova non disponibile» e saltate quel passo: non inventate un giudizio. |
| Solo NON_ESEGUITO | Rifate le prove una volta. Se Copilot ancora non risponde, oggi non potete verificare il vostro orchestratore: guardate Build e basta, senza ripetizioni. |

## Parte 3 · La correzione di Copilot

### 3A · Che cosa chiedete a Copilot

Aprite una conversazione nuova in Copilot e scrivete voi la richiesta. Copilot non deve vedere la vostra correzione: deve arrivarci da solo. Un esempio, per la prova 5 di 2A, e le domande a cui rispondete voi:

| Parte della richiesta | Esempio | Voi |
| --- | --- | --- |
| Che cosa incollo | l'orchestratore, le parti CRITERIO e PROVE del quaderno, le risposte ricevute, i testi del noleggio che la prova usa | Quali testi incollate? |
| Che cosa chiedo | «Per la prova 5 scrivi la causa e una sola modifica.» | Per quale prova? |
| Che cosa vieto | «Non riscrivere tutte le istruzioni.» | Che cosa non deve fare? |
| Che cosa controllo | «Dimmi quale altra prova potrebbe rompersi.» | Che cosa gli fate controllare? |

Tutte le prove OK? Fate così:

1. Incollate le prove senza le colonne Giudizio e Motivo, con le risposte ricevute, e chiedete a Copilot di controllarle.
2. Se propone una modifica, confrontatela con le vostre frasi: non basta a cambiare le istruzioni.
3. Se mostra un errore vero in una prova, correggete il giudizio di quella prova e tornate alla riga «Almeno un ERRORE» della tabella 2B.

Dopo la risposta controllate: ha scritto una sola modifica o ha riscritto tutte le istruzioni? Non chiudete la conversazione: vi serve per il confronto. Copiate la sua causa e la sua modifica sotto CORREZIONE, con il titolo «Copilot». Se non propone modifiche, scrivete «nessuna modifica».

## Parte 4 · opencode: Build corregge sul proiettore

Questa parte si guarda e si decide insieme: voi non aprite opencode. In opencode ci sono due modalità: Plan legge e propone, senza scrivere file; Build modifica i file; in questo laboratorio opencode è configurato per chiedere il permesso prima di modificarli. Sul proiettore Build corregge un orchestratore d'esempio: quello della prova 3 della parte 1B, in cui l'utente ha visto il registro. Un agente di opencode è un file di testo: il nome del file è il nome dell'agente. Il file d'esempio si chiama `orchestratore_esempio.md`: non è il vostro `orchestratore.txt`. La modifica deve essere leggibile prima del permesso: se la finestra di opencode mostra solo il nome del file, la modifica si legge prima in Plan, e solo dopo si passa a Build.

Che cosa fate voi:

1. Decidete insieme che cosa scrivere a Build: per quale prova, quali file può leggere, quale file può modificare, quanto può cambiare. Non dategli una correzione già scritta.
2. Quando opencode si ferma a chiedere il permesso, guardate il nome del file e la modifica che mostra. Alzate la mano: Allow once (consenti una volta) se il file è quello giusto e la modifica è piccola e precisa; Reject (rifiuta) altrimenti.
3. Ricopiate sotto CORREZIONE, con il titolo «Build», la riga che Build ha scritto: se è lunga, copiate solo la parte che cambia.

## Parte 5 · Tre correzioni da confrontare

### 5A · Mettete a confronto

Avete tre correzioni: la vostra, quella di Copilot e quella di Build. Se non c'è nessun errore, non avete correzioni ma decisioni di non cambiare nulla: confrontate la vostra con il controllo di Copilot. Build ha corretto l'errore della prova 3, non per forza il vostro. Quindi:

- La vostra e quella di Copilot riguardano lo stesso errore. Rispondete a voce: la causa è la stessa? Quale tocca meno righe? Se nessuna delle due propone una modifica, rispondete: perché avete deciso di non cambiare nulla?
- Quella di Build guardatela come metodo: una riga o tutto il testo? Nomina la causa? Se il vostro errore è un altro, la sua modifica non va nel vostro file. Potete prenderne il principio e riscriverlo per il vostro caso.
- Quale seconda prova potrebbe rompersi con la correzione che scegliete? Di solito una prova OK. Scrivetela: la riproverete dopo.

Tenete la vostra, quella di Copilot o un misto. Sotto CORREZIONE scrivete, in una riga, quale tenete e perché.

### 5B · Applicate la correzione e riprovate

Applicatela voi, a mano, in `orchestratore.txt`. Poi aggiornate l'orchestratore nel programma che usate: nell'agente di Copilot incollate il nuovo testo nelle istruzioni; se le istruzioni stanno nel primo messaggio, usate il nuovo testo nella conversazione nuova. Poi ripetete la richiesta che era ERRORE, scritta con altre parole, e la seconda prova che avete scritto in 5A, ciascuna in una conversazione nuova: se era OK, deve restare OK. Scrivete sotto CORREZIONE Prima e Dopo.

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «A che ora chiude il negozio?», riscritta «Fino a che ora siete aperti?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

Nessuna correzione necessaria? Saltate questo passo. Le prove NON_ESEGUITO restano non verificate.

## Salvate

Salvate `orchestratore.txt` corretto e `quaderno_prove.txt`: potete ancora usarli.
