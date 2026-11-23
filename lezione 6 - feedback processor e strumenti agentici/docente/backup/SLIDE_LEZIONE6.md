# Slide 01 — Feedback processor: chi corregge l’agente?
<!-- layout: COPERTINA -->

Un secondo agente legge le vostre prove e propone le correzioni. Voi decidete quali applicare.

ITS MAKER · 25 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode

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

1. Provate il vostro orchestratore con richieste vostre e scrivete come va ogni risposta.
2. Un secondo agente legge le prove e propone le correzioni.
3. Voi scegliete quale proposta applicare.
4. Riprovate.

Il secondo agente si chiama feedback processor. Noi lo chiamiamo agente delle correzioni. Propone soltanto: non cambia niente da solo.

---

# Slide 05 — Due file in Blocco note, prima di provare
<!-- layout: CONTENUTO -->

Seguite la consegna, parte 1A: copiate il vostro orchestratore in `orchestratore.txt` e create `quaderno_prove.txt`.

Il quaderno serve a segnare ogni prova. L’agente delle correzioni lo leggerà per capire come è andata. Nel quaderno scrivete i tre lavori e, accanto a ciascuno, chi può usarlo.

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

Prima di inviarne una, scrivete nel quaderno quale lavoro vi aspettate. Non valgono le richieste del quaderno d’esempio né quelle scritte come esempio nel vostro orchestratore.

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

Risposta in breve: elenca le bici del registro

Giudizio: ERRORE

Motivo: l’utente ha visto il registro, che è solo dell’amministratore

Il Motivo serve all’agente delle correzioni. Tutti i campi: consegna 1E.

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

# Slide 12 — L’agente delle correzioni
<!-- layout: SEZIONE -->

Lo scrivete voi, e lo provate sul vostro quaderno.

---

# Slide 13 — Che cosa correggereste?
<!-- layout: CONTENUTO -->

Prova 3: l’utente ha visto il registro.

Nelle istruzioni di REGISTRO non c’è scritto chi può usarlo.

> Che cosa scrivereste per correggerlo?

---

# Slide 14 — Una proposta dell’agente delle correzioni
<!-- layout: CONTENUTO -->

Per la prova 3 potrebbe proporre questo. Testo scritto a mano per l’esempio: non è una risposta di Copilot.

| Campo | Proposta |
| --- | --- |
| Tipo | permesso |
| Causa probabile | nelle istruzioni di REGISTRO non c’è scritto chi può usarlo |
| Modifica | in REGISTRO, come prima riga: «Solo con accesso amministratore. Con l’accesso utente rispondi: Non puoi vedere il registro.» |

---

# Slide 15 — Quattro tipi di errore
<!-- layout: CONTENUTO -->

Il tipo dice che genere di errore è. Quello della prova 3 è un errore di permesso.

| Tipo | Che cosa è successo | Esempio |
| --- | --- | --- |
| lavoro sbagliato | la richiesta è andata a un lavoro che non doveva rispondere | «Che cosa significa fuori servizio?» finisce in GUASTI, ma il significato è nelle regole del noleggio |
| risposta sbagliata | il lavoro giusto ha risposto male | GUASTI dimentica il primo controllo del banco |
| dato inventato | ha scritto un dato che non è nei testi | «Il negozio chiude alle 20», ma le regole dicono 19 |
| permesso | ha dato a un accesso ciò che non può avere | l’utente vede il registro |

---

# Slide 16 — Di che tipo sono i vostri errori?
<!-- layout: CONTENUTO -->

Per ogni ERRORE del vostro quaderno scegliete il tipo. Annotatelo su un foglio, fuori dal quaderno: lo confronterete con la scelta dell’agente.

Nessun ERRORE? Allora la proposta giusta sarà «Nessuna modifica necessaria».

---

# Slide 17 — Che cosa non deve proporre l’agente?
<!-- layout: CONTENUTO -->

In `istruzioni_correzioni.txt` scrivete che cosa scrive l’agente per ogni ERRORE (Tipo, Causa probabile, Modifica) e che cosa non fa. Riceverà il quaderno e `orchestratore.txt`. Quattro proposte che non dovrebbe scrivere:

| Proposta da evitare | Che cosa scrivete voi per fermarla? |
| --- | --- |
| «Riscrivi tutte le istruzioni e tutte le regole.» | Quanto può cambiare, per volta? |
| «Mostra il registro a chi lo chiede.» | Che cosa non propone mai? |
| «La prova 2 ha un errore: cambia REGOLE.» (era OK) | Che cosa fa con le prove OK? |
| «Migliora GUASTI.» | Che cosa deve indicare ogni volta? |

---

# Slide 18 — Provate l’agente delle correzioni
<!-- layout: CONTENUTO -->

Scegliete voi dove. In ogni caso riceve le vostre istruzioni, il quaderno e `orchestratore.txt`, e scrive soltanto una proposta.

| Programma | Come |
| --- | --- |
| Microsoft Copilot | conversazione nuova: istruzioni, quaderno e orchestratore, tutto nello stesso messaggio |
| Unsloth Studio | consegna 4A, passi 1 e 5–7 |
| opencode | consegna 4B, passi 1, 4–6 e 8–9 |

---

# Slide 19 — Che cosa manca nelle vostre istruzioni?
<!-- layout: CONTENUTO -->

Aprite su Teams `ESEMPIO_ISTRUZIONI_AGENTE_CORREZIONI.txt`. È scritto a mano e non è provato.

Che cosa ha l’esempio che nel vostro manca?

---

# Slide 20 — Un giro di correzione
<!-- layout: SEZIONE -->

Applicate una sola proposta, poi riprovate.

---

# Slide 21 — La proposta è giusta?
<!-- layout: CONTENUTO -->

Leggete la proposta e rispondete a tre domande:

1. Il tipo di errore è quello che avevate annotato voi?
2. La causa indica il punto giusto: l’elenco delle richieste, le righe su chi può usare che cosa, oppure le istruzioni di un lavoro?
3. La modifica sistema questa prova senza rompere le altre?

Una proposta sbagliata non applicatela: tenetela per la discussione.

---

# Slide 22 — Applicate la modifica
<!-- layout: CONTENUTO -->

Scegliete una proposta e applicatela voi, a mano, in `orchestratore.txt`. Poi aggiornate l’orchestratore: come, lo dice la consegna, parte 3B.

Nessuna proposta perché tutte le prove erano OK? Passate alla parte 4.

---

# Slide 23 — Che cosa è cambiato?
<!-- layout: CONTENUTO -->

Ripetete la richiesta che era ERRORE, scritta con altre parole, e una che era OK, ciascuna in una conversazione nuova. Scrivete nel quaderno Prima e Dopo. L’esempio:

| Richiesta | Prima | Dopo |
| --- | --- | --- |
| utente: «Quali bici sono state tolte dal noleggio?», riscritta «Che bici avete messo da parte?» | ERRORE | OK |
| utente: «Che cosa significa catena che salta?» | OK | OK |

---

# Slide 24 — Quale correzione tenete?
<!-- layout: CONTENUTO -->

Un’altra prova finita male: «Che cosa significa fuori servizio?» è andata a GUASTI, ma il significato è nelle regole del noleggio. Due correzioni. Quale tenete? Perché?

| Correzione A | Correzione B |
| --- | --- |
| Nell’elenco delle richieste, alla voce REGOLE: aggiungere l’esempio «Che cosa significa fuori servizio?». | In GUASTI: se la domanda chiede il significato di un termine, rispondi tu. |

Se qualcuno scrive «Che vuol dire che una bici è fuori servizio?», dove va con la A?

---

# Slide 25 — Avete scartato una proposta?
<!-- layout: CONTENUTO -->

Chi ne ha una applicata che funziona, o una scartata, la incolla nella chat della lezione su Teams.

> Che cosa distingue la proposta riuscita da quella scartata?

---

# Slide 26 — Che cosa rende utile una correzione
<!-- layout: CONTENUTO -->

| Utile | Pericolosa |
| --- | --- |
| cambia una riga precisa | riscrive tutto il testo |
| sistema la causa, nel testo giusto | aggiunge una toppa in un altro lavoro |
| le prove che andavano bene restano OK | ne sistema una e ne rompe un’altra |
| rispetta i permessi | apre un’eccezione per chi scrive «sono il titolare» |
| usa solo dati dei testi | aggiunge un dato inventato |

Anche l’agente delle correzioni può sbagliare. Quale riga della tabella ve lo ha fatto capire?

---

# Slide 27 — Lo stesso orchestratore, in un altro programma
<!-- layout: SEZIONE -->

Scegliete Unsloth Studio o opencode. I passi sono nella consegna, parte 4. Niente da consegnare.

---

# Slide 28 — Che cosa cambia da un programma all’altro
<!-- layout: CONTENUTO -->

Il testo dell’orchestratore resta quasi lo stesso: in opencode cambia solo la frase che dice dove sono i testi del noleggio.

| | Copilot | Unsloth Studio | opencode |
| --- | --- | --- | --- |
| Dove vanno le istruzioni | nell’agente, o nel primo messaggio | nel campo System Prompt, il testo che il modello legge prima di ogni messaggio | in un file di testo: l’agente |
| Dove stanno i tre testi del noleggio | incollati nel messaggio | incollati nella chat | file nella cartella `laboratorio` |
| L’accesso | una riga, per esempio «Accesso: utente» | la stessa riga | la stessa riga |

---

# Slide 29 — In Studio, il System Prompt
<!-- layout: CONTENUTO -->

Qui incollate il testo di `orchestratore.txt` (consegna 4A).

![Unsloth Studio: il campo System Prompt, evidenziato, dove si incolla il testo.](immagini_slide/studio_system_prompt.png)

---

# Slide 30 — Una nuova chat: che cosa resta?
<!-- layout: CONTENUTO -->

Per l’agente delle correzioni serve un altro testo. Ma il System Prompt resta com’è anche in una nuova chat.

> Che cosa fate prima di aprirla?

---

# Slide 31 — In opencode un agente è un file
<!-- layout: CONTENUTO -->

Il file `orchestratore.md` è già nella cartella `.opencode`, dentro `agents`. In cima ha l’intestazione: due righe, chiuse tra due righe di trattini (---).

| Riga | Esempio |
| --- | --- |
| description | Orchestratore del noleggio Ruota Libera |
| mode | primary |

Sotto incollate il testo di `orchestratore.txt`. Il nome del file è il nome dell’agente.

---

# Slide 32 — Che file vuole scrivere?
<!-- layout: CONTENUTO -->

L’agente delle correzioni chiede il permesso di scrivere un file.

Leggete il nome prima di rispondere. Se è `proposta_correzioni.txt`: Allow once (consenti una volta). Se è un altro file: Reject (rifiuta).

---

# Slide 33 — Da dove cominciate?
<!-- layout: CONTENUTO -->

Scegliete voi che cosa provare, anche altro. Potete passare da un programma all’altro.

| Programma | Idea | Che cosa guardare |
| --- | --- | --- |
| Unsloth Studio | due richieste del vostro quaderno, giudicate con il vostro criterio | se il modello piccolo si comporta come Copilot; quanto testo tiene insieme |
| Unsloth Studio | la stessa richiesta con due temperature (più alta, risposte più varie) | lunghezza, forma e correttezza delle risposte |
| opencode | estendere la pagina `.html` della lezione 5, prima in Plan (propone) e poi in Build (scrive, dopo il vostro permesso) | i permessi; la pagina nel browser |

---

# Slide 34 — Dove si è fermato il vostro programma?
<!-- layout: CHIUSURA -->

Che cosa avete chiesto? Che cosa ha fatto da solo?
