# Lezione 6 · Feedback processor: chi corregge l'agente?

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot e opencode**

## Da dove partiamo

Nella lezione 5 avete costruito un orchestratore per Ruota Libera: un testo che sceglie il lavoro giusto per ogni richiesta e che decide che cosa può avere chi entra come utente e chi entra come amministratore. Oggi lo mettete alla prova con richieste vostre. Poi scrivete voi una correzione per un errore. Poi due programmi propongono la loro: prima Copilot, poi opencode, che la scrive nel file dopo il vostro permesso. Voi confrontate le tre correzioni, tenete una e riprovate.

Ognuno lavora da solo, sul proprio computer. Non ci sono file da consegnare. Per le prove usate Microsoft Copilot con l'account scolastico. Se avete costruito l'orchestratore in Unsloth Studio o in opencode, copiate il testo in Blocco note: le prove si fanno comunque in Copilot.

Non avete l'orchestratore, o non funziona? Chiedete il testo di partenza. Ha già i tre lavori e i due accessi. Non è una soluzione: è un punto da cui cominciare, da provare e da correggere. Nella lezione 5 il «lavoro» si chiamava anche skill: è la stessa cosa.

Tre parole nuove:

| Parola | Che cosa vuol dire |
| --- | --- |
| Quaderno delle prove | Un file di Blocco note, `quaderno_prove.txt`, dove scrivete ogni richiesta provata e come è andata. |
| Giudizio | La valutazione che date a una risposta: OK, ERRORE oppure NON_ESEGUITO. |
| Feedback processor | Un programma che legge il quaderno e propone una correzione. Copilot la scrive come testo; opencode in Build la scrive nel file, solo dopo il vostro permesso. Voi decidete se tenerla o scartarla. |

## Parte 1 · Mettete alla prova l'orchestratore

### 1A · Preparate i file

1. Aprite il vostro orchestratore e copiatene le istruzioni in un file nuovo di Blocco note: `orchestratore.txt`. Se i lavori sono in file separati (per esempio `skill_guasti.md`), copiate anche il loro testo, sotto le istruzioni. Servirà più avanti.
2. Create un altro file di Blocco note: `quaderno_prove.txt`.
3. Scrivete nel quaderno i tre lavori e, accanto a ciascuno, chi può usarlo: utente o amministratore.

I tre testi del noleggio (registro, regole del noleggio, guida ai guasti) sono quelli delle lezioni scorse. Non li avete più? Scaricateli da Teams.

### 1B · Un esempio di quaderno

Un orchestratore di Ruota Libera ha tre lavori: GUASTI per utente e amministratore, REGOLE solo per l'utente, REGISTRO solo per l'amministratore. Questo è il riassunto del quaderno di un orchestratore d'esempio, non il vostro: le vostre richieste saranno diverse:

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
| Motivo | l'utente ha visto il registro |

I giudizi possibili sono tre:

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

Prendete il primo ERRORE del vostro quaderno. In un file nuovo di Blocco note, `mia_correzione.txt`, scrivete:

- la **Causa**: che cosa manca nelle istruzioni dell'orchestratore;
- la **Modifica**: il testo preciso da scrivere e il punto dove va.

Il Motivo del quaderno dice che cosa è andato storto nella risposta. La Causa dice che cosa manca nelle istruzioni. Una sola modifica. Non applicatela ancora: prima la confrontate con quelle dei programmi. Tenete `mia_correzione.txt` solo sul vostro computer: non va incollato in nessuna richiesta.

Nessun ERRORE? Scrivete in `mia_correzione.txt` «nessuna correzione necessaria»: è un risultato valido. Fate lo stesso le parti 3 e 4, chiedendo a Copilot e a Build di controllare il quaderno. Se propongono una modifica quando tutto era OK, è materiale per il confronto.

## Parte 3 · La correzione di Copilot

### 3A · Che cosa chiedete a Copilot

Aprite una conversazione nuova in Copilot e scrivete voi la richiesta. Copilot non deve vedere la vostra correzione: deve arrivarci da solo. Un esempio, per la prova 5 di 2A, e le domande a cui rispondete voi:

| Parte della richiesta | Esempio | Voi |
| --- | --- | --- |
| Che cosa incollo | l'orchestratore, il quaderno e le regole del noleggio | Quali testi incollate? |
| Che cosa chiedo | «Per la prova 5 scrivi la causa e una sola modifica.» | Per quale prova? |
| Che cosa vieto | «Non riscrivere tutte le istruzioni.» | Che cosa non deve fare? |
| Che cosa controllo | «Dimmi quale prova OK potrebbe rompersi.» | Che cosa gli fate controllare? |

Dopo la risposta controllate: ha scritto una sola modifica o ha riscritto tutte le istruzioni? Non chiudete la conversazione: vi serve per il confronto.

## Parte 4 · opencode: Build modifica il file

In opencode ci sono due modalità: Plan legge e propone, senza scrivere file; Build modifica i file, ma chiede il permesso. Qui Build corregge il file dell'orchestratore. Lavorate nel computer virtuale: portate lì i file che vi servono (`orchestratore.txt`, `quaderno_prove.txt` e i tre testi del noleggio). Non portate `mia_correzione.txt`.

In opencode un agente è un file di testo. Il nome dell'agente è il nome del file (`orchestratore`). In cima al file c'è l'intestazione: due righe, chiuse tra due righe di trattini (---). `description` dice a che cosa serve l'agente, `mode: primary` vuol dire che lo scegliete voi con Maiusc+Tab, come Build e Plan. Sotto l'intestazione ci sono le istruzioni, le stesse che avete scritto per Copilot.

Nella cartella `laboratorio` trovate la cartella `.opencode` e dentro la cartella `agents`, con un file già pronto che ha solo l'intestazione: `orchestratore.md`.

Chi non riesce ad aprire opencode passa alla parte 5 e confronta due correzioni invece di tre.

### 4A · Preparate l'orchestratore

1. Nella cartella `laboratorio` mettete i tre testi del noleggio, `quaderno_prove.txt` e `orchestratore.txt`.
2. Aprite `orchestratore.md` con Blocco note (tasto destro, Apri con). Sotto l'intestazione incollate il testo di `orchestratore.txt`.
3. Nel testo cambiate la frase che dice dove prendere i testi del noleggio: non sono più incollati nella conversazione, sono file nella cartella e l'agente li legge quando servono.
4. Salvate il file senza cambiarne il nome.
5. Fate doppio clic sul collegamento opencode del desktop: parte nella cartella `laboratorio`.

### 4B · Chiedete a Build

1. Premete Maiusc+Tab finché in basso compare `build`.
2. Scrivete voi la richiesta. Decidete: per quale prova del quaderno; quali file può leggere (servono anche i testi del noleggio?); quale file può modificare; quanto può cambiare. Non scrivete la vostra correzione né quella di Copilot.
3. Il programma si ferma a chiedere il permesso di modificare un file. Leggete il nome del file e la modifica che mostra. Allow once (consenti una volta) solo se il file è `orchestratore.md` e la modifica è piccola e precisa. Altrimenti Reject (rifiuta) e riscrivete la richiesta più precisa.
4. Se chiede di eseguire un comando, premete Reject (rifiuta) e scrivete «Senza comandi, leggi i file.»
5. Chiudete opencode e riapritelo. Premete Maiusc+Tab finché compare `orchestratore`. Scrivete una riga con l'accesso (per esempio «Accesso: utente») e la richiesta che era ERRORE, scritta con altre parole. L'errore c'è ancora? Qui risponde un altro modello: un risultato diverso da quello di Copilot non dice per forza che la correzione è sbagliata.

Se `orchestratore` non compare con Maiusc+Tab, chiudete opencode e riapritelo; poi controllate che il file sia in `.opencode`, dentro `agents`, e che finisca con `.md`.

## Parte 5 · Tre correzioni, una sola da tenere

### 5A · Mettete a confronto

Avete tre correzioni: la vostra (`mia_correzione.txt`), quella di Copilot (nella conversazione) e quella di Build (la modifica in `orchestratore.md`). Rispondete a quattro domande:

1. La causa è la stessa?
2. Il punto dell'orchestratore è lo stesso?
3. Quale tocca meno righe?
4. Quale prova che andava bene potrebbe rompersi? Scrivetela: la riproverete dopo.

Tenete la vostra, una delle altre due o un misto. Scrivete in `mia_correzione.txt`, in una riga, quale tenete e perché.

### 5B · Applicate la correzione e riprovate

Applicatela voi, a mano, in `orchestratore.txt`. Se tenete quella di Build, copiatela da `orchestratore.md`. Poi aggiornate l'orchestratore nel programma che usate: nell'agente di Copilot incollate il nuovo testo nelle istruzioni; se le istruzioni stanno nel primo messaggio, usate il nuovo testo nella conversazione nuova. Poi ripetete la richiesta che era ERRORE, scritta con altre parole, e la prova OK che avete indicato al punto 4 di 5A, ciascuna in una conversazione nuova: la prova OK deve restare OK. Scrivete nel quaderno Prima e Dopo.

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «A che ora chiude il negozio?», riscritta «Fino a che ora siete aperti?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

Nessuna correzione necessaria? Saltate questo passo.

### 5C · Una da tenere, una da scartare

Un'altra prova finita male: «Che cosa significa fuori servizio?» è andata a GUASTI, ma il significato è nelle regole del noleggio. Due correzioni:

| Correzione A | Correzione B |
| --- | --- |
| Nell'elenco delle richieste, alla voce REGOLE: aggiungere l'esempio «Che cosa significa fuori servizio?». | In GUASTI: se la domanda chiede il significato di un termine, rispondi tu. |

Quale tenete? Perché? E se qualcuno scrive «Che vuol dire che una bici è fuori servizio?», dove va con la A? Poi guardate insieme che cosa rende utile una correzione e chi ha corretto meglio nel vostro caso: voi, Copilot o Build.

## Salvate

Salvate `orchestratore.txt` corretto, `quaderno_prove.txt` e `mia_correzione.txt`: potete ancora usarli.
