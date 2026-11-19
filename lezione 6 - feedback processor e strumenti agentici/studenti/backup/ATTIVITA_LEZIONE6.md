# Lezione 6 · Chi corregge l'agente?

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
| Agente delle correzioni | Un secondo agente che legge il quaderno e scrive una proposta. Non cambia niente: propone, voi applicate. |

## Parte 1 · Mettete alla prova l'orchestratore

### 1A · Preparate i file

1. Aprite il vostro orchestratore e copiatene le istruzioni in un file nuovo di Blocco note: `orchestratore.txt`. Servirà più avanti.
2. Create un altro file di Blocco note: `quaderno_prove.txt`.
3. Scrivete nel quaderno i tre lavori e, accanto a ciascuno, chi può usarlo: utente o amministratore.

I tre testi del noleggio (registro, regole del noleggio, guida ai guasti) sono quelli delle lezioni scorse. Non li avete più? Scaricateli da Teams.

### 1B · Un esempio: la pizzeria d'asporto

L'orchestratore di una pizzeria ha tre lavori: ORDINI e ALLERGENI per l'utente, INCASSI solo per l'amministratore. Questo è il riassunto del suo quaderno:

| N. | Accesso | Richiesta | Lavoro | Giudizio |
| --- | --- | --- | --- | --- |
| 1 | utente | Quanto costa la margherita? | ORDINI | OK |
| 2 | utente | Il calzone ha il glutine? | ALLERGENI | OK |
| 3 | utente | Quanto abbiamo incassato ieri? | INCASSI | ERRORE |
| 4 | amministratore | Quanto abbiamo incassato ieri? | INCASSI | OK |

Nella prova 3 l'utente ha avuto la cifra degli incassi: l'orchestratore ha dato a un utente ciò che solo l'amministratore può avere.

### 1C · Prima il criterio

Prima di provare qualsiasi richiesta, scrivete in cima al quaderno il vostro criterio in tre righe: quando direte che una risposta è giusta? Per la pizzeria era: «ALLERGENI nomina ogni allergene del menù. I prezzi sono quelli del listino. L'utente non vede mai gli incassi.»

### 1D · Cinque richieste, inventate da voi

Inventate cinque richieste per il noleggio Ruota Libera. Prima di inviarne una, scrivete nel quaderno quale lavoro vi aspettate. Accanto all'esempio della pizzeria, le domande a cui rispondete voi:

| Che cosa provare | Esempio: pizzeria | Voi |
| --- | --- | --- |
| Una richiesta per ciascuno dei tre lavori | «Il calzone ha il glutine?» | Che cosa chiederebbe chi usa quel lavoro? |
| Una richiesta ambigua | «Quanto ho preso con le pizze?» | Quale frase si può leggere in due modi? |
| Una richiesta che il vostro accesso non permette | utente: «Quanto abbiamo incassato ieri?» | Che cosa non può avere l'accesso che userete? |

Provate ogni richiesta in una conversazione nuova, con l'accesso che serve (utente o amministratore, come lo avete costruito nel vostro orchestratore). Dove serve, incollate nel messaggio anche i testi del noleggio. Se l'agente vi fa una domanda, rispondete nella stessa conversazione.

### 1E · Annotate ogni prova

Dopo ogni prova aggiungete al quaderno un blocco con questi campi. L'esempio è la prova 2 della pizzeria:

| Campo | Esempio |
| --- | --- |
| Prova | 2 |
| Accesso | utente |
| Richiesta | Il calzone ha il glutine? |
| Lavoro atteso | ALLERGENI |
| Lavoro che ha risposto | ALLERGENI (se la risposta lo dice) |
| Risposta in breve | Sì, la farina è di frumento. |
| Giudizio | OK |
| Motivo | il dato è nel menù |

I giudizi possibili sono tre:

| Giudizio | Quando |
| --- | --- |
| OK | La risposta rispetta il vostro criterio. Anche un rifiuto giusto è OK. |
| ERRORE | Non lo rispetta. |
| NON_ESEGUITO | Copilot non ha risposto: non c'è niente da valutare. |

Giudicate con il criterio che avete scritto, non a sensazione. Tutte le prove OK? È un risultato valido. Controllate solo che il criterio fosse scritto prima e che la richiesta ambigua e quella non permessa fossero le più difficili che vi venivano in mente.

## Parte 2 · L'agente delle correzioni

### 2A · Quattro tipi di errore

Gli errori sono di quattro tipi. Scegliete il tipo di ogni ERRORE del vostro quaderno e annotatelo su un foglio, fuori dal quaderno: lo confronterete con la scelta dell'agente.

| Tipo | Che cosa è successo | Esempio: pizzeria |
| --- | --- | --- |
| scelta | ha scelto il lavoro sbagliato | «Il calzone ha il glutine?» finisce in ORDINI |
| risposta | il lavoro giusto ha risposto male | ALLERGENI dimentica l'uovo |
| dato inventato | ha scritto un dato che non è nei testi | «Il calzone costa 9 euro», ma il menù dice 8 |
| permesso | ha dato a un accesso ciò che non può avere | l'utente vede gli incassi |

### 2B · Che cosa propone l'agente delle correzioni: l'esempio della pizzeria

Per la prova 3 della pizzeria, un agente delle correzioni potrebbe proporre questo. È un testo scritto a mano per l'esempio, non una risposta di Copilot:

| Campo | Proposta |
| --- | --- |
| Tipo | permesso |
| Causa probabile | nelle istruzioni di INCASSI non c'è scritto chi può usarlo |
| Modifica | in INCASSI, come prima riga: «Solo con accesso amministratore. Con l'accesso utente rispondi: Non puoi vedere gli incassi.» |

### 2C · Scrivete le istruzioni dell'agente delle correzioni

Scrivetele voi, in un file nuovo di Blocco note: `istruzioni_correzioni.txt`. Dovete scrivere che cosa riceve l'agente, che cosa scrive per ogni ERRORE (i campi dell'esempio 2B) e che cosa non fa. Di aiuto, a sinistra, proposte che l'agente delle correzioni di una pizzeria non dovrebbe scrivere; a destra, che cosa decidete voi:

| Proposta da evitare | Che cosa scrivete voi per fermarla? |
| --- | --- |
| «Riscrivi tutto il menù e tutte le regole.» | Quanto può cambiare, per volta? |
| «Mostra gli incassi al titolare.» | Che cosa non propone mai? |
| «La prova 2 ha un errore: cambia ALLERGENI.» (era OK) | Che cosa fa con le prove OK? |
| «Migliora ALLERGENI.» | Che cosa deve indicare ogni volta? |

### 2D · Provate l'agente delle correzioni

Scegliete voi dove farlo girare. In ogni caso riceve le vostre istruzioni, il quaderno e il testo dell'orchestratore (`orchestratore.txt`), e scrive soltanto una proposta. Non vede le risposte vere, solo il quaderno: se il Motivo manca, la causa che propone è un'ipotesi.

| Programma | Come |
| --- | --- |
| Microsoft Copilot | Conversazione nuova: istruzioni, quaderno e orchestratore, tutto nello stesso messaggio. |
| Unsloth Studio | Istruzioni nel campo System prompt, quaderno e orchestratore nella chat. Il modello è piccolo e può essere lento. |
| opencode | Quaderno e orchestratore in file, istruzioni nel messaggio, proposta scritta in un altro file. In modalità Build il programma chiede il permesso prima di scrivere. |

Studio e opencode girano nel computer virtuale: i file vanno portati lì.

Dopo la prova controllate: ha scritto una proposta, o ha cambiato qualcosa da solo?

### 2E · Che cosa manca nelle vostre istruzioni?

Aprite su Teams `ESEMPIO_ISTRUZIONI_AGENTE_CORREZIONI.txt`: è un esempio scritto a mano, non provato. Che cosa c'è nel vostro che qui manca? Che cosa manca nel vostro?

## Parte 3 · Un giro di correzione

### 3A · La proposta è giusta?

Leggete la proposta e rispondete a tre domande:

1. Il tipo di errore è quello che avevate annotato voi?
2. La causa guarda il testo giusto: l'elenco delle richieste (le righe che dicono a quale lavoro va una richiesta), un accesso o un lavoro?
3. La modifica sistema questa prova senza rompere le altre?

Una proposta sbagliata o da ignorare tenetela da parte: serve alla discussione. Tutte le prove erano OK? La proposta giusta è «nessuna modifica necessaria»: se l'agente ha proposto modifiche lo stesso, giudicatele come le altre.

### 3B · Applicate la modifica e riprovate

Scegliete una proposta. Applicatela voi, a mano, nel testo dell'orchestratore e aggiornate l'orchestratore. Poi, in una conversazione nuova, ripetete la richiesta che era ERRORE e una richiesta che era OK: la richiesta OK deve restare OK. Scrivete nel quaderno Prima e Dopo.

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «Quanto abbiamo incassato ieri?» | ERRORE | OK |
| utente: «Il calzone ha il glutine?» | OK | OK |

### 3C · Una da tenere, una da scartare

Alcune proposte vanno guardate insieme: una riuscita e una scartata. Che cosa le distingue? Prima si discute, poi si scrive il criterio.

## Parte 4 · Unsloth Studio o opencode, a vostra scelta

Non c'è una consegna. Scegliete voi che cosa provare. Due idee per cominciare:

| Programma | Idea | Che cosa guardare |
| --- | --- | --- |
| Unsloth Studio | Una richiesta con istruzioni di sistema e temperatura diverse. | La lunghezza, la forma e la correttezza delle risposte; quanto testo tiene insieme il modello. |
| opencode | Estendere la pagina `.html` della lezione 5: nuovi dati o una sezione, prima in Plan e poi in Build. | I permessi, letti prima di approvare; la pagina aperta nel browser. |

Potete passare da un programma all'altro. Alla fine rispondete a voce: che cosa avete chiesto, che cosa ha fatto da solo, dove si è fermato?

## Salvate

Salvate `orchestratore.txt` corretto, `quaderno_prove.txt` e `istruzioni_correzioni.txt`: potete ancora usarli.
