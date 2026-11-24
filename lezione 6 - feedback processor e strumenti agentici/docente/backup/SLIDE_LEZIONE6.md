# Slide 01 — Feedback processor: chi corregge l’agente?
<!-- layout: COPERTINA -->

Correggete voi il vostro orchestratore. Poi lo fanno Copilot e opencode, e confrontate le correzioni.

ITS MAKER · 25 novembre 2026 · Microsoft Copilot e opencode

---

# Slide 02 — Il vostro orchestratore, in tre righe
<!-- layout: CONTENUTO -->

Lo avete costruito nella lezione 5: riceve una richiesta e la manda al lavoro giusto (lì li chiamavate skill). Ecco tre righe di un orchestratore d’esempio:

| Se la richiesta parla di | va a questo lavoro | e lo può usare |
| --- | --- | --- |
| come si ripara una bici | GUASTI | utente e amministratore |
| orari, prezzi, regole | REGOLE | utente |
| quali bici sono uscite dal noleggio | REGISTRO | solo amministratore |

Le prime due colonne sono l’elenco delle richieste. L’ultima dice chi può usare il lavoro: utente e amministratore sono i due accessi. Il vostro può avere righe diverse.

---

# Slide 03 — Che cosa è andato storto?
<!-- layout: CONTENUTO -->

Un utente scrive:

> «Quali bici sono state tolte dal noleggio?»

L’orchestratore sceglie il lavoro REGISTRO e all’utente elenca le bici del registro.

Ma il registro lo può vedere solo l’amministratore. Chi se ne accorge? Chi lo sistema?

---

# Slide 04 — Un giro in quattro passi
<!-- layout: CONTENUTO -->

1. Provate il vostro orchestratore e annotate ogni prova.
2. Scrivete voi una correzione, senza applicarla.
3. Chiedete una correzione a Copilot e poi a opencode, senza mostrare la vostra.
4. Confrontate, tenete una correzione, applicatela e riprovate.

Copilot e opencode fanno da feedback processor: leggono le prove e propongono una correzione. Copilot scrive solo testo. opencode la scrive nel file, ma solo se gli date il permesso.

---

# Slide 05 — Due file in Blocco note, prima di provare
<!-- layout: CONTENUTO -->

Seguite la consegna, parte 1A: copiate il vostro orchestratore in `orchestratore.txt` e create `quaderno_prove.txt`.

Il quaderno serve a segnare ogni prova. Nel quaderno scrivete i tre lavori e, accanto a ciascuno, chi può usarlo.

Non avete l’orchestratore? Chiedete il testo di partenza: è un orchestratore da provare e correggere, non una soluzione.

---

# Slide 06 — Stessa richiesta: perché la 3 è ERRORE e la 4 è OK?
<!-- layout: CONTENUTO -->

Riassunto di un quaderno d’esempio, non il vostro. Il giudizio è OK se la risposta va bene, ERRORE se no.

| N. | Accesso | Richiesta | Giudizio |
| --- | --- | --- | --- |
| 1 | utente | Che cosa significa catena che salta? | OK |
| 2 | utente | A che ora chiude il negozio? | OK |
| 3 | utente | Quali bici sono state tolte dal noleggio? | ERRORE |
| 4 | amministratore | Quali bici sono state tolte dal noleggio? | OK |

---

# Slide 07 — «Giuste» rispetto a che cosa?
<!-- layout: CONTENUTO -->

> Un criterio da migliorare: «Le risposte devono essere giuste.»

Il criterio è la regola con cui decidete se una risposta è OK. Giuste rispetto a quale testo? Per quale accesso? Che cosa non deve mai comparire?

Scrivete il vostro criterio in tre righe, in cima al quaderno, prima di provare qualsiasi richiesta.

---

# Slide 08 — Cinque richieste, inventate da voi
<!-- layout: CONTENUTO -->

Prima di inviarne una, scrivete nel quaderno quale lavoro vi aspettate. Non valgono le richieste del quaderno d’esempio né quelle scritte come esempio nel vostro orchestratore. Come scrivere l’accesso nel messaggio: consegna 1D.

| Che cosa provare | Voi |
| --- | --- |
| Una richiesta per ciascuno dei tre lavori | Che cosa chiederebbe chi usa quel lavoro? |
| Una richiesta ambigua | Quale frase si può leggere in due modi? |
| Una richiesta che il vostro accesso non permette | Che cosa non può avere l’accesso che userete? |

---

# Slide 09 — Dopo ogni prova, scrivete com’è andata
<!-- layout: CONTENUTO -->

Un blocco nel quaderno per ogni prova. Questo è il blocco della prova 3 d’esempio, ridotto:

Accesso: utente

Richiesta: Quali bici sono state tolte dal noleggio?

Atteso: REGISTRO, che deve rifiutare. Ha risposto: REGISTRO

Giudizio: ERRORE

Motivo: l’utente ha visto il registro

---

# Slide 10 — L’orchestratore dice di no: OK o ERRORE?
<!-- layout: CONTENUTO -->

L’utente chiede il registro. L’orchestratore risponde:

> «Non puoi vedere il registro.»

Alzate la mano: OK o ERRORE? Perché?

---

# Slide 11 — Quando scrivete OK, quando ERRORE
<!-- layout: CONTENUTO -->

| Giudizio | Quando |
| --- | --- |
| OK | la risposta rispetta il vostro criterio; anche un rifiuto giusto è OK |
| ERRORE | non lo rispetta |
| NON_ESEGUITO | il programma non ha risposto: non c’è niente da valutare |

Tutte OK? Va bene, se il criterio era scritto prima di provare e se la richiesta ambigua e quella non permessa erano le più difficili che vi venivano in mente.

---

# Slide 12 — Prima correggete voi
<!-- layout: SEZIONE -->

Gli agenti arrivano dopo. Prima la correzione scritta da voi.

---

# Slide 13 — Che cosa correggereste?
<!-- layout: CONTENUTO -->

Prova 5 di un altro quaderno d’esempio. L’utente chiede: «A che ora chiude il negozio?»

L’orchestratore risponde: «Alle 20:00». Le regole del noleggio dicono 19:00.

> Che cosa scrivereste per correggerlo?

---

# Slide 14 — Una correzione scritta bene
<!-- layout: CONTENUTO -->

Per la prova 5 la correzione potrebbe essere questa. Una causa, una modifica.

| Campo | Esempio |
| --- | --- |
| Causa | in REGOLE non c’è scritto di prendere gli orari solo dalle regole del noleggio |
| Modifica | in REGOLE, come prima riga: «Gli orari si prendono solo dalle regole del noleggio. Se non ci sono, scrivi: Dato non presente nel testo.» |

---

# Slide 15 — Correggete il vostro primo ERRORE
<!-- layout: CONTENUTO -->

In `mia_correzione.txt` scrivete la Causa: che cosa manca nelle istruzioni. Poi la Modifica: il testo preciso e il punto dove va. Una sola modifica. Non applicatela ancora.

Il Motivo dice che cosa è andato storto nella risposta. La Causa dice che cosa manca nelle istruzioni.

Nessun ERRORE? Scrivete «nessuna correzione necessaria» e fate lo stesso le parti con Copilot e opencode: è un risultato valido.

---

# Slide 16 — La correzione di Copilot
<!-- layout: SEZIONE -->

Copilot, in una conversazione nuova, legge il vostro quaderno e propone la sua.

---

# Slide 17 — Che cosa chiedete a Copilot?
<!-- layout: CONTENUTO -->

Scrivete la richiesta. Non incollate la vostra correzione: Copilot deve arrivarci da solo. Un esempio, per la prova 5:

| Parte della richiesta | Esempio | Voi |
| --- | --- | --- |
| Che cosa incollo | l’orchestratore, il quaderno e le regole del noleggio | Quali testi incollate? |
| Che cosa chiedo | «Per la prova 5 scrivi la causa e una sola modifica.» | Per quale prova? |
| Che cosa vieto | «Non riscrivere tutte le istruzioni.» | Che cosa non deve fare? |
| Che cosa controllo | «Dimmi quale prova OK potrebbe rompersi.» | Che cosa gli fate controllare? |

---

# Slide 18 — opencode: Build modifica il file
<!-- layout: SEZIONE -->

Plan propone e basta. Build modifica i file, dopo il vostro permesso. Qui Build corregge il file dell’orchestratore.

---

# Slide 19 — In opencode un agente è un file
<!-- layout: CONTENUTO -->

Il file `orchestratore.md` è già nella cartella `.opencode`, dentro `agents`. In cima ha l’intestazione: due righe, chiuse tra due righe di trattini (---).

| Riga | Esempio |
| --- | --- |
| description | Orchestratore del noleggio Ruota Libera |
| mode | primary |

Sotto incollate il testo di `orchestratore.txt`. Il nome del file è il nome dell’agente.

---

# Slide 20 — Che cosa chiedete a Build?
<!-- layout: CONTENUTO -->

Quattro cose da decidere e scrivere nella richiesta:

1. Per quale prova del quaderno.
2. Quali file può leggere.
3. Quale file può modificare.
4. Quanto può cambiare.

Non scrivete la vostra correzione né quella di Copilot.

---

# Slide 21 — Che cosa guardate prima di approvare?
<!-- layout: CONTENUTO -->

opencode si ferma e mostra la modifica che vuole fare.

> Il file è `orchestratore.md`? Cambia una riga o tutto il testo? Rompe una regola che andava bene?

Se va bene: Allow once (consenti una volta). Altrimenti: Reject (rifiuta) e riscrivete la richiesta.

---

# Slide 22 — Build ha corretto: l’errore c’è ancora?
<!-- layout: CONTENUTO -->

Chiudete opencode e riapritelo. Scegliete `orchestratore` con Maiusc+Tab e scrivete la richiesta che era ERRORE con altre parole.

Qui risponde un altro modello: un risultato diverso da quello di Copilot non dice per forza che la correzione è sbagliata.

---

# Slide 23 — Tre correzioni, una sola da tenere
<!-- layout: SEZIONE -->

La vostra, quella di Copilot, quella di Build.

---

# Slide 24 — Mettete a confronto le tre correzioni
<!-- layout: CONTENUTO -->

1. La causa è la stessa?
2. Il punto dell’orchestratore è lo stesso?
3. Quale tocca meno righe?
4. Quale prova che andava bene potrebbe rompersi? Scrivetela: la riproverete dopo.

Tenete la vostra, una delle altre due o un misto. In `mia_correzione.txt` scrivete quale e perché.

---

# Slide 25 — Applicate la correzione che tenete
<!-- layout: CONTENUTO -->

Applicatela voi, a mano, in `orchestratore.txt`. Se tenete quella di Build, copiatela da `orchestratore.md`. Come aggiornare l’orchestratore: consegna 5B.

Nessuna correzione necessaria? Saltate questo passo e la prova.

---

# Slide 26 — Che cosa è cambiato?
<!-- layout: CONTENUTO -->

Ripetete la richiesta che era ERRORE, scritta con altre parole, e la prova OK indicata al punto 4. Ciascuna in una conversazione nuova. Scrivete nel quaderno Prima e Dopo. L’esempio:

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «A che ora chiude il negozio?», riscritta «Fino a che ora siete aperti?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

---

# Slide 27 — Quale di queste due tenete?
<!-- layout: CONTENUTO -->

Un’altra prova finita male: «Che cosa significa fuori servizio?» è andata a GUASTI, ma il significato è nelle regole del noleggio. Due correzioni. Quale tenete? Perché?

| Correzione A | Correzione B |
| --- | --- |
| Nell’elenco delle richieste, alla voce REGOLE: aggiungere l’esempio «Che cosa significa fuori servizio?». | In GUASTI: se la domanda chiede il significato di un termine, rispondi tu. |

Se qualcuno scrive «Che vuol dire che una bici è fuori servizio?», dove va con la A?

---

# Slide 28 — Che cosa rende utile una correzione
<!-- layout: CONTENUTO -->

| Utile | Pericolosa |
| --- | --- |
| cambia una riga precisa | riscrive tutto il testo |
| sistema la causa, nel testo giusto | aggiunge una toppa in un altro lavoro |
| le prove che andavano bene restano OK | ne sistema una e ne rompe un’altra |
| rispetta i permessi | apre un’eccezione per chi scrive «sono il titolare» |
| usa solo dati dei testi | aggiunge un dato inventato |

Chi ha corretto meglio nel vostro caso: voi, Copilot o Build?

---

# Slide 29 — Chi ha deciso che cosa?
<!-- layout: CHIUSURA -->

Che cosa avete deciso voi? Che cosa hanno deciso gli agenti?
