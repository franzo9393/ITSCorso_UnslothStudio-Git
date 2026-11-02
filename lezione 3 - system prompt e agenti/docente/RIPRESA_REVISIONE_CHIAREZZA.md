# Ripresa — Revisione della chiarezza, lezione 3

## Richiesta e punto di arresto

L'utente ha chiesto di usare «assistente di reparto» e di rivedere la chiarezza dei materiali con Gemini 4 Argon. Ha poi chiesto di interrompere al primo punto utile e riprendere nella prossima sessione.

Il lavoro è sospeso dopo l'aggiornamento dei sorgenti e la rigenerazione completa dei formati. Non sono ancora state eseguite le verifiche finali visive di questa revisione. Non presentare i materiali come già collaudati nell'account studente.

## Completato

- Titolo corrente: «L'assistente di reparto della P03». Il testo spiega che è Microsoft Copilot con le istruzioni progettate dagli studenti, non un altro programma.
- Chiariti programmi da aprire, compilazione della scheda in Word o LibreOffice Writer, differenza tra istruzioni, documenti e richiesta di prova.
- La registrazione del controllo sui documenti è ora nella sezione 2, prima della scrittura delle istruzioni. Le sezioni numerate della scheda vanno da 1 a 7.
- Chiariti ruoli delle coppie A/B, computer e scheda da usare, divieto di suggerire risposte e righe da compilare prima di inviare la richiesta.
- Precisato in AGENTS.md il vincolo su nomi concreti, termini spiegati, attori e ordine delle azioni. La chiarezza era già richiesta dalle regole generali.
- Aggiornati guida docente, canovaccio, README e generatore, compresi nomi di file e metadati.
- Rinominati i file prodotti, senza mantenere copie concorrenti con la precedente denominazione.
- Eseguito con successo: python3 'lezione 3 - system prompt e agenti/docente/genera_materiali.py'. LibreOffice ha esportato presentazione e tre documenti Word in PDF; il generatore ha prodotto 22 slide.

## Nomi correnti

Nella cartella lezione 3 - system prompt e agenti:
- Lezione3_Assistente_Reparto_P03_ITS_MAKER.pptx
- Lezione3_Assistente_Reparto_P03_ITS_MAKER.html
- Lezione3_Assistente_Reparto_P03_ITS_MAKER.pdf
- SLIDE_LEZIONE3.md
- studenti/ATTIVITA_LEZIONE3.md, .docx e .pdf
- studenti/01_DOCUMENTI_P03.txt, .docx e .pdf
- docente/GUIDA_DOCENTE.md, .docx e .pdf
- docente/CANOVACCIO_LEZIONE3_RAG_COPILOT.md
- docente/genera_materiali.py

Il nome del file che gli studenti devono creare con le proprie istruzioni è istruzioni_assistente_P03.txt: non è una soluzione da distribuire già compilata.

## Contributo di Argon

Consulto effettuato tramite ArgonLessonConsult, riprendendo la sessione identificata dal prefisso 01a18195-7db3, il cui modello salvato è google-antigravity/gemini-4-argon. Il consulto è stato sospeso e non ha modificato file.

Ultimo controllo di Argon sui sorgenti: nessuna ambiguità sostanziale residua. Un solo ritocco opzionale per la sezione 5 della scheda: precisare che le righe prima dell'invio si compilano nella scheda dei compagni, non nella propria.

Formulazione attuale da individuare per testo, senza affidarsi a un vecchio numero di riga:
«Prima di inviarla, compilate nella tabella qui sotto la richiesta, il risultato atteso e i documenti da controllare».

Possibile precisazione:
«Prima di inviarla sul computer dei compagni, compilate nella tabella della loro scheda la richiesta, il risultato atteso e i documenti da controllare».

La precisazione non è stata applicata prima della pausa. Se viene applicata, rigenerare i formati prima delle verifiche finali.

## Da fare alla ripresa

1. Valutare il solo ritocco opzionale sopra, senza riaprire il progetto della lezione.
2. Controllare impaginazione dei PDF e dei Word aggiornati: nessuna pagina quasi vuota, tabella spezzata male o cella da compilare persa. Il numero di pagine della nuova scheda non è ancora stato verificato.
3. Aprire l'HTML corrente nel browser, provare navigazione, tastiera e ridimensionamento, controllare tutte le 22 slide per testo fuori dai riquadri. Conservare grafica ufficiale 16:10 e HTML autosufficiente.
4. Verificare titoli e nomi aggiornati in PowerPoint, HTML, PDF e metadati; controllare i collegamenti del README e l'assenza di copie obsolete.
5. Verificare che tutti i 24 appunti siano integri in TXT, Word e PDF e che le celle della scheda restino modificabili e vuote dove previsto.
6. Concludere la revisione e rimuovere questa nota quando non serve più.

## Invarianti da non cambiare

- Nessuna modifica a date, fatti e testo dei 24 appunti del diario.
- Catalogo rev2 del 18/10/2026: P03 associata a FLT-993, P30 a FLT-229; il montaggio storico del 14/10 resta FLT-992.
- Magazzino al 19/10/2026 ore 08:00: FLT-992 = 5, FLT-993 = 8, FLT-229 = 4; i movimenti sono già compresi.
- Teams distribuisce i file; documenti completi forniti in ogni conversazione nuova. Nessuna dipendenza dalla ricerca pubblica e nessun collegamento automatico dai Blocchi appunti.
- Python e CSV sono stati osservati dall'utente; lettura dei nuovi allegati e Blocchi appunti richiedono ancora prova con account studente.
- Istruzioni e richieste di prova inventate dagli studenti: niente testi completi da copiare, nessun obbligo di far sbagliare il modello, nessuna durata didattica.

## Git e modifiche estranee

L'utente ha poi richiesto commit e push della revisione sospesa, comprensiva di questa nota di ripresa. Le verifiche finali restano rinviate alla prossima sessione. Il commit base precedente alla revisione è c51e55f.

Lasciare intatte e fuori da eventuali commit le due modifiche estranee già presenti:
- eliminazione di lezione 2 - 28 ottobre 2026/lezione 2 - 28 ottobre 2026 - prompting.zip;
- file non tracciato lezione 2 - 28 ottobre 2026/ipotesi 2 - system prompt e agenti.zip.

Non modificare altre lezioni e non applicare procedure GSD o creare artefatti di pianificazione: questa è una nota di ripresa dei materiali del corso.
