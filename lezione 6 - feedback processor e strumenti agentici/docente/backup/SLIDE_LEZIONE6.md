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
3. Chiedete una correzione a Copilot, senza mostrare la vostra. Poi guardate opencode farla sul proiettore.
4. Confrontate, tenete una correzione, applicatela e riprovate.

Copilot e opencode fanno da feedback processor: leggono le prove e propongono una correzione. Copilot scrive solo testo. opencode la scrive nel file, ma qui è configurato per chiedere prima un permesso.

---

# Slide 05 — Due file in Blocco note, prima di provare
<!-- layout: CONTENUTO -->

Consegna, parte 1A: `orchestratore.txt` e `quaderno_prove.txt`. Il quaderno ha tre parti: CRITERIO, PROVE, CORREZIONE.

Non avete l’orchestratore? Chiedete il testo di partenza: è un orchestratore da provare e correggere, non una soluzione.

---

# Slide 06 — Stessa richiesta: perché la 3 è ERRORE e la 4 è OK?
<!-- layout: CONTENUTO -->

Le PROVE di un quaderno d’esempio, non il vostro. Il giudizio è OK se la risposta va bene, ERRORE se no.

| N. | Accesso e richiesta | Esito atteso | Giudizio |
| --- | --- | --- | --- |
| 1 | utente: Che cosa significa catena che salta? | GUASTI | OK |
| 2 | utente: A che ora chiude il negozio? | REGOLE | OK |
| 3 | utente: Quali bici sono state tolte dal noleggio? | rifiuto | ERRORE |
| 4 | amministratore: Quali bici sono state tolte dal noleggio? | REGISTRO | OK |

---

# Slide 07 — «Giuste» rispetto a che cosa?
<!-- layout: CONTENUTO -->

> Un criterio da migliorare: «Le risposte devono essere giuste.»

Il criterio è la regola con cui decidete se una risposta è OK. Giuste rispetto a quale testo? Per quale accesso? Che cosa non deve mai comparire?

Sotto CRITERIO, prima di provare qualsiasi richiesta: tre righe.

---

# Slide 08 — Tre richieste, inventate da voi
<!-- layout: CONTENUTO -->

Non valgono le richieste del quaderno d’esempio né quelle scritte come esempio nel vostro orchestratore. Come inviarle: consegna 1D.

| Che cosa provare | Voi |
| --- | --- |
| Una richiesta normale, per un lavoro a vostra scelta | Che cosa chiederebbe chi usa quel lavoro? |
| Una richiesta ambigua | Quale frase si può leggere in due modi? |
| Una richiesta che il vostro accesso non permette | Che cosa non può avere l’accesso che userete? |

---

# Slide 09 — Dopo ogni prova, una riga nel quaderno
<!-- layout: CONTENUTO -->

Sotto PROVE, una riga per ogni prova. Questa è la prova 3 d’esempio:

3 · utente: Quali bici sono state tolte dal noleggio? · esito atteso: rifiuto · ERRORE

Il motivo si scrive solo se è ERRORE: l’utente ha visto il registro.

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

# Slide 14 — Che cosa manca, e dove?
<!-- layout: CONTENUTO -->

Per la prova 5 la correzione potrebbe essere questa. Una causa, una modifica.

| Campo | Esempio |
| --- | --- |
| Causa | in REGOLE non c’è scritto di prendere gli orari solo dalle regole del noleggio |
| Modifica | in REGOLE, come prima riga: «Gli orari si prendono solo dalle regole del noleggio. Se non ci sono, scrivi: Dato non presente nel testo.» |

---

# Slide 15 — Correggete il vostro primo ERRORE
<!-- layout: CONTENUTO -->

Sotto CORREZIONE: Causa e Modifica, una sola, senza applicarla.

Il Motivo dice che cosa è andato storto nella risposta. La Causa dice che cosa manca nelle istruzioni.

Nessun ERRORE? Consegna 2B.

---

# Slide 16 — Copilot trova la stessa causa?
<!-- layout: SEZIONE -->

Copilot, in una conversazione nuova, legge le vostre prove e propone la sua.

---

# Slide 17 — Che cosa chiedete a Copilot?
<!-- layout: CONTENUTO -->

Consegna 3A. Lasciate fuori CORREZIONE: Copilot deve arrivarci da solo. Un esempio, per la prova 5:

| Parte della richiesta | Esempio | Voi |
| --- | --- | --- |
| Che cosa incollo | l’orchestratore, CRITERIO e PROVE, le risposte, le regole del noleggio | Quali testi incollate? |
| Che cosa chiedo | «Per la prova 5 scrivi la causa e una sola modifica.» | Per quale prova? |
| Che cosa vieto | «Non riscrivere tutte le istruzioni.» | Che cosa non deve fare? |
| Che cosa controllo | «Dimmi quale altra prova potrebbe rompersi.» | Che cosa gli fate controllare? |

---

# Slide 18 — opencode: Build corregge
<!-- layout: SEZIONE -->

Guardate il proiettore: Build corregge l’orchestratore d’esempio della prova 3. Plan propone e basta. Build modifica i file, e qui chiede prima un permesso. Voi non aprite opencode.

---

# Slide 19 — Che cosa scrivereste a Build?
<!-- layout: CONTENUTO -->

Quattro cose da decidere insieme per la richiesta:

1. Per quale prova del quaderno.
2. Quali file può leggere.
3. Quale file può modificare.
4. Quanto può cambiare.

Nessuno detta la correzione: Build deve arrivarci da solo.

---

# Slide 20 — Allow once o Reject?
<!-- layout: CONTENUTO -->

Quando opencode chiede il permesso, guardate il file e la modifica.

> Il file è `orchestratore.md`, quello d’esempio (un file di testo, non il vostro `orchestratore.txt`)? Cambia una riga o tutto il testo? Rompe una regola che andava bene?

Alzate la mano: Allow once (consenti una volta) oppure Reject (rifiuta)? Perché?

---

# Slide 21 — Tre correzioni, una sola da tenere
<!-- layout: SEZIONE -->

La vostra, quella di Copilot, quella di Build.

---

# Slide 22 — Mettete a confronto le tre correzioni
<!-- layout: CONTENUTO -->

La vostra, quella di Copilot, quella di Build: quale tenete? Consegna 5A.

---

# Slide 23 — Applicate la correzione che tenete
<!-- layout: CONTENUTO -->

Applicatela voi, a mano, in `orchestratore.txt`. Come aggiornare l’orchestratore: consegna 5B.

Nessuna correzione necessaria? Saltate questo passo e la prova: avete già controllato le prove eseguite; quelle NON_ESEGUITO restano da verificare.

---

# Slide 24 — Che cosa è cambiato?
<!-- layout: CONTENUTO -->

Prima e Dopo: che cosa è cambiato? Consegna 5B. L’esempio:

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «A che ora chiude il negozio?», riscritta «Fino a che ora siete aperti?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

---

# Slide 25 — Che cosa rende utile una correzione
<!-- layout: CONTENUTO -->

| Utile | Pericolosa |
| --- | --- |
| cambia una riga precisa | riscrive tutto il testo |
| sistema la causa, nel testo giusto | aggiunge una toppa in un altro lavoro |
| le prove che andavano bene restano OK | ne sistema una e ne rompe un’altra |
| rispetta i permessi | apre un’eccezione per chi scrive «sono il titolare» |
| usa solo dati dei testi | aggiunge un dato inventato |

---

# Slide 26 — Chi ha deciso che cosa?
<!-- layout: CHIUSURA -->

Che cosa avete deciso voi? Che cosa hanno deciso gli agenti?
