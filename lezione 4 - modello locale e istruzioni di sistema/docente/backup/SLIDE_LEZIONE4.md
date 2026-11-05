# Slide 01 — Un assistente sul computer del reparto
<!-- layout: COPERTINA -->

Lezione 4 · Unsloth Studio e istruzioni di sistema

12 novembre 2026 · Unsloth Studio nella macchina virtuale

---

# Slide 02 — La richiesta del responsabile
<!-- layout: CONTENUTO -->

«I registri della pressa P03 non devono uscire dal reparto. Vorrei un assistente che lavori sul nostro computer.»

Il modello che usate oggi gira dentro la vostra macchina virtuale: i testi che gli date non vanno a un servizio esterno.

Il caso è quello che conoscete: la pressa P03 e il registro del 13–15 ottobre.

---

# Slide 03 — Il percorso di oggi
<!-- layout: CONTENUTO -->

| Parte | Dove lavorate | Che cosa ottenete |
| --- | --- | --- |
| 1. Installare Unsloth Studio | Macchina virtuale | Programma e modello pronti |
| 2. Capire come risponde un modello | Computer reale, browser | Previsioni e numero di token |
| 3. Misurare e regolare | Unsloth Studio | misure_VM.txt |
| 4. Scrivere le istruzioni dell'assistente | Unsloth Studio | istruzioni_assistente_P03.txt e casi_di_prova.txt |

In coppia, ognuno con la propria macchina virtuale. I tre file si scrivono con Blocco note dentro la macchina virtuale.

---

# Slide 04 — Installiamo Unsloth Studio
<!-- layout: SEZIONE -->

Il programma che fa girare il modello.

---

# Slide 05 — L'installazione, nella macchina virtuale
<!-- layout: CONTENUTO -->

Nella macchina virtuale aprite PowerShell: menu Start, scrivete PowerShell, premete Invio.

Incollate questa riga e premete Invio. Dice a Windows di scaricare e avviare il programma di installazione:

$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex

- Non chiudete la finestra: scarica molti file e può metterci a lungo.
- Se compare un errore in rosso, chiamate il docente.
- Intanto aprite Teams nella macchina virtuale e scaricate il registro; copiate lo zip del modello sul Desktop e restituite la chiavetta; create in Documenti i tre file .txt vuoti. Poi la parte 2 sul computer reale.

---

# Slide 06 — Come sceglie la parola successiva
<!-- layout: SEZIONE -->

Un modello piccolo che si vede all'opera.

---

# Slide 07 — Transformer Explainer
<!-- layout: CONTENUTO -->

Sul computer reale, nel browser: poloclub.github.io/transformer-explainer

È un modello piccolo che completa frasi in inglese: non è un assistente.

1. Scrivete una frase breve in inglese e guardate quali parole propone dopo.
2. Prima di muovere la temperatura, scrivete in misure_VM.txt, nella macchina virtuale, che cosa pensate che succeda alle probabilità se la alzate e se la abbassate.
3. Provate. Poi scrivete che cosa avete visto e spiegatelo al compagno.

Si osservano le probabilità: non c'è un errore da trovare.

---

# Slide 08 — Quanto pesa il testo
<!-- layout: CONTENUTO -->

Il modello legge pezzi di testo, i token. Sul computer reale: huggingface.co/spaces/Xenova/the-tokenizer-playground

1. Incollate il testo del registro. Scegliete il tokenizzatore dal menu in alto e scrivete in misure_VM.txt il suo nome e i token.
2. Riscrivete voi il testo più breve nella casella, con gli stessi fatti importanti, e scrivete il nuovo numero.
3. Leggete la versione breve del compagno: quale fatto importante ha tolto?

Installazione non finita alla fine di questa parte? Avvisate il docente.

---

# Slide 09 — Il modello sul vostro computer
<!-- layout: SEZIONE -->

Avviamo Studio e carichiamo il modello.

---

# Slide 10 — Il primo avvio
<!-- layout: CONTENUTO -->

Quando l'installazione finisce, PowerShell chiede se avviare Unsloth Studio: scrivete Y e premete Invio.

1. Nel browser della macchina virtuale aprite http://127.0.0.1:8888 e create una password di almeno 8 caratteri. Scrivetela su un foglio.
2. Chiudete la scheda di Teams e aprite Gestione attività: Ctrl+Maiusc+Esc, Prestazioni, Memoria.
3. Scrivete in misure_VM.txt la memoria in uso prima di caricare il modello.

---

# Slide 11 — Il modello
<!-- layout: CONTENUTO -->

1. Zip sul Desktop? Estraetelo in %USERPROFILE%\\.cache\huggingface\hub e controllate la cartella models--unsloth--Qwen3.5-2B-GGUF.
2. Aspettate l'indicazione del docente su Context Length.
3. Cliccate Select model: con lo zip aprite On Device. Senza zip aspettate il docente: la rete è la stessa per tutti.
4. Search e Tools all'inizio sono attivi (verdi): cliccateli, devono diventare grigi.

Memoria quasi al massimo? Slide 13.

---

# Slide 12 — Che cosa occupa il modello
<!-- layout: CONTENUTO -->

Studio stima la memoria in Run settings. La misura vera è in Gestione attività.

| Quando | Che cosa scrivete in misure_VM.txt |
| --- | --- |
| Modello caricato, Context Length su Auto | Stima di Studio e memoria in uso |
| Context Length 8192, poi Reload model | Stima di Studio e memoria in uso |
| Domanda breve | Secondi dal tasto Invio alla prima parola, e tok/s |
| Registro intero con una domanda | Secondi, tok/s e token usati |

tok/s: token al secondo. 1.5k: circa 1.500 token. Context Length: token tenuti presenti. Token di Studio e del Tokenizer: uguali?

---

# Slide 13 — Se Studio si blocca
<!-- layout: CONTENUTO -->

Se la macchina virtuale rallenta molto o la finestra non risponde: chiudete la finestra di PowerShell in cui gira Studio, scrivete «bloccato» nella prima riga della tabella di 3B e avvisate il docente. Non cliccate Select model: aspettate le sue indicazioni.

Per riaprire Studio, col via del docente: nuova finestra di PowerShell, unsloth studio -p 8888, Invio. Nel browser aprite http://127.0.0.1:8888 e aspettate il docente prima di Select model. Poi in Run settings Context Length a 8192 e Reload model.

---

# Slide 14 — Regolare le risposte
<!-- layout: CONTENUTO -->

Insieme: decidete come giudicherete una risposta. Scrivete i dati del fermo del 14 ottobre da trovare nel registro, come li controllerete e la richiesta che farete.

Poi in Run settings dividetevi le regolazioni: uno prova Temperature, l'altro Top P oppure Top K, a scelta.

- Temperature: bassa, risposte più prevedibili; alta, più varietà.
- Top P e Top K: limitano le parole tra cui il modello può scegliere.

I valori di partenza li prova chi segue Temperature; poi ognuno prova un valore basso e uno alto. Scegliete insieme e scrivete in misure_VM.txt quale impostazione e perché.

---

# Slide 15 — Le istruzioni dell'assistente
<!-- layout: SEZIONE -->

Che cosa deve fare, e come.

---

# Slide 16 — Le istruzioni di sistema
<!-- layout: CONTENUTO -->

In Run settings c'è la casella System Prompt: le istruzioni scritte lì valgono per tutta la conversazione. Il messaggio che scrivete nella chat è un'altra cosa.

Scrivete in istruzioni_assistente_P03.txt le istruzioni per un assistente di reparto:

- che cosa deve fare e da quali fonti può rispondere;
- quando deve farvi una domanda prima di rispondere;
- che cosa non deve fare;
- come deve rispondere.

---

# Slide 17 — Provate le vostre istruzioni
<!-- layout: CONTENUTO -->

1. Incollate le istruzioni nella casella System Prompt e usate l'impostazione che avete scelto.
2. Aprite una nuova conversazione e incollate in un solo messaggio il registro e, sotto, la vostra domanda.
3. Guardate se l'assistente rispetta le istruzioni.

Le istruzioni non servono a farlo rispondere bene a qualunque domanda: servono a dire come deve comportarsi quando la domanda è incompleta o fuori dal registro.

---

# Slide 18 — Mettetevi alla prova
<!-- layout: CONTENUTO -->

Mandatevi il testo delle istruzioni con un messaggio su Teams. Poi ognuno prova l'assistente del compagno nel proprio Studio.

Inventate voi almeno quattro casi di prova e tranelli: che cosa può sfuggire a un assistente che legge solo questo registro?

In casi_di_prova.txt, per ogni caso: la domanda, la risposta ricevuta, OK oppure ERRORE e perché.

Ogni prova in una nuova conversazione.

---

# Slide 19 — Correggete le istruzioni
<!-- layout: CONTENUTO -->

Rileggete i casi del compagno sul vostro assistente.

Per ogni ERRORE decidete che cosa correggere: le istruzioni, la domanda o il testo dato all'assistente.

Correggete le regole nel testo delle istruzioni e scrivete sotto «Correzioni dopo le prove» che cosa avete cambiato, il motivo e l'esito. Tutti OK? Scrivete quale regola ha funzionato e aggiungete la regola per un caso nuovo. In System Prompt incollate solo le regole, senza «Correzioni dopo le prove».

---

# Slide 20 — Le consegne
<!-- layout: CONTENUTO -->

Ognuno consegna i propri tre file .txt nel compito su Teams, dal browser della macchina virtuale oppure dal computer reale:

| File | Contenuto |
| --- | --- |
| misure_VM.txt | Previsioni, token, misure, spiegazione, criteri, scelta |
| istruzioni_assistente_P03.txt | Istruzioni e correzioni dopo le prove |
| casi_di_prova.txt | I casi inventati per il compagno e gli esiti |

---

# Slide 21 — Se Studio non parte
<!-- layout: CONTENUTO -->

Se l'installazione non è finita quando avete terminato la parte 2, avvisate il docente. Se una sola macchina virtuale della coppia funziona, lavorate a turno su quella.

- Memoria: octooai.com/llm-vram-calculator, modello da 2 miliardi di parametri a 4 bit, contesto 8192 e massimo. È una stima.
- Regolazioni: scegliete una temperatura con Transformer Explainer e scrivete perché.
- Istruzioni: provatele in Copilot. Non è System Prompt, e il registro esce dal reparto: scrivetelo. Copilot non risponde? Chi ha inventato i casi li pone, l'autore risponde con le sole regole scritte.

---

# Slide 22 — Che cosa avete verificato?
<!-- layout: CHIUSURA -->

Che cosa occupa un modello sul vostro computer, e che cosa cambia con testi lunghi?

Che cosa cambia la temperatura nelle risposte?

Quale caso di prova vi ha fatto cambiare o confermare le istruzioni?
