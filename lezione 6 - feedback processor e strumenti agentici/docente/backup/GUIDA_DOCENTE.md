# Guida docente · Lezione 6

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot e opencode**

Documento riservato al docente. Le decisioni e i motivi sono in `docente/backup/PIANO_LEZIONE6.md`; qui c'è ciò che serve per condurre.

## La lezione da condurre

Si riparte dall'orchestratore costruito nella lezione 5. Il filo è uno solo: lo studente corregge, poi lo fanno due programmi, poi si confronta. Decisione del 24 novembre 2026, dopo la prima versione (un agente delle correzioni scritto dagli studenti): quella versione faceva rifare all'agente ciò che lo studente aveva già scritto nel quaderno, e il lavoro era soprattutto burocrazia.

1. **Prove** (slide 2–11). Gli studenti vedono un errore vero (slide 3), il giro in quattro passi (slide 4), scrivono il criterio (slide 7), inventano cinque richieste (slide 8) e annotano ogni prova nel quaderno (slide 9–11).
2. **La correzione dello studente** (slide 12–15). Vedono una correzione d'esempio (Causa e Modifica) e scrivono la propria per il primo ERRORE, in `mia_correzione.txt`. Non la applicano ancora.
3. **La correzione di Copilot** (slide 16–17). Lo studente scrive la richiesta a Copilot, senza la propria correzione. Copilot fa da feedback processor: legge il quaderno e propone.
4. **La correzione di opencode in Build** (slide 18–21). Build legge il quaderno e modifica `orchestratore.md`, dopo il permesso dello studente.
5. **Tre correzioni, una sola** (slide 22–27). Confronto a quattro domande, applicazione, prova prima e dopo con la richiesta riscritta, criteri dopo la prova, chiusura.

Parole: sulle slide e nella consegna si dice **lavoro** (la consegna ricorda che nella lezione 5 si chiamava anche skill), **elenco delle richieste**, **accesso** (utente o amministratore), **quaderno delle prove**, **giudizio**, **criterio**, **correzione** (con Causa e Modifica). «Feedback processor» compare nel titolo e alla slide 4, dopo l'esempio, ed è il nome del ruolo di Copilot e di Build. «Competenza» e «instradamento» restano in guida e a voce. «Registro» indica solo il registro del noleggio: per le prove si dice quaderno.

Ogni parola nuova compare prima in un esempio e poi con il suo nome. Dove si incontra la prima volta:

| Parola | Esempio (slide) | Nome e definizione (slide) |
| --- | --- | --- |
| lavoro, accesso, elenco delle richieste | tre righe d'esempio (2) | stessa slide, dopo la tabella |
| feedback processor | errore dell'utente che vede il registro (3) | giro in quattro passi (4) |
| quaderno, giudizio | due file in Blocco note (5); quaderno d'esempio (6) | stessa slide 6, riga sopra la tabella |
| criterio | «Le risposte devono essere giuste» (7) | stessa slide |
| Causa e Modifica | correzione d'esempio (13–14) | stessa slide 14; Motivo contro Causa alla slide 15 |
| Plan e Build | sezione (18) | stessa slide |
| intestazione di un agente in opencode | due righe d'esempio (19) | stessa slide |

Come nelle lezioni 4 e 5: lavoro singolo, niente giro tra i banchi, niente file da consegnare, niente voto. I risultati si leggono sugli schermi e dal proiettore; i criteri si mostrano dopo la prova (slide 26 dopo la 25). Un quaderno con tutte le prove OK è valido: nessuna attività si basa sull'errore del modello. Copilot propone solo testo, gli studenti decidono. Build invece scrive davvero nel file, ma solo dopo il permesso dello studente: dillo, è la differenza tra una proposta e un'azione eseguita.

Non dichiarare provato ciò che non lo è: nulla di questa lezione è stato provato in Copilot con l'account studente né in opencode.

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE6.docx` e i tre testi del noleggio: `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt` (stessi fatti delle lezioni 4 e 5). Non pubblicare le cartelle di backup.
- `studenti/da_pubblicare_a_chi_non_ha_l_orchestratore/ISTRUZIONI_ORCHESTRATORE_PARTENZA.txt`: lo dai solo a chi non ha l'orchestratore della lezione 5 o non funziona. Costruito dal piano e allineato all'esercizio originale per i permessi: GUASTI per utente e amministratore, REGISTRO solo amministratore, REGOLE solo utente. Ipotesi mie: gli accessi si scelgono con la riga «Accesso:» scritta nel messaggio; la riga «Lavoro usato:» in testa alla risposta. Non è una soluzione collaudata. L'accesso con una riga che chiunque può riscrivere non è un controllo vero: puoi usarlo come spunto alla slide 26.
- Proiettore: prima le richieste e le domande, dopo i criteri. Nessuno studente condivide le proprie correzioni: i confronti sono sullo schermo di ognuno; se vuoi proiettarne uno, scegli tu uno studente che si offre.
- Copia in `Documenti\laboratorio\.opencode\agents\` il solo file `docente/MODELLI_OPENCODE_LEZIONE6/orchestratore.md` (intestazione, senza testo).
- Controlla che in `Documenti\laboratorio` ci sia ancora `opencode.jsonc` della lezione 5: fa chiedere il permesso prima di scrivere e prima dei comandi. Senza quel file Build scrive senza chiedere e la slide 21 non ha senso.

### Controlli pre-aula

Nessuna riga è stata provata con Copilot e l'account studente né sui PC della scuola.

| Controllo | Che cosa accertare | Se fallisce | Esito |
| --- | --- | --- | --- |
| Quanti hanno un orchestratore | Quanti studenti hanno un orchestratore funzionante, in quale strumento (Copilot, Studio, opencode) e se la risposta dice quale lavoro ha usato | Il testo di partenza (non una soluzione) | |
| Il testo di partenza | Con i tre testi incollati e «Accesso: utente» o «Accesso: amministratore» in fondo: sceglie il lavoro giusto, scrive «Lavoro usato:», rifiuta REGISTRO all'utente e REGOLE all'amministratore, non cede a «sono il titolare»? | Correggi il file; dillo agli studenti | |
| Lunghezza dei messaggi in Copilot | Testo di partenza più tre testi sono circa 15.000 caratteri. Il campo dell'account studente li accetta in un solo messaggio? Orchestratore e quaderno (circa 7.000 caratteri) entrano in un solo messaggio? | Per il testo di partenza: due messaggi nella stessa conversazione. Per la richiesta a Copilot (slide 17): orchestratore in un messaggio, quaderno nel successivo | |
| Copilot come feedback processor | Con un quaderno di due o tre prove (una ERRORE) e l'orchestratore: scrive una causa e una modifica? Riscrive tutte le istruzioni? Con tutte le prove OK inventa una correzione? | Mostra com'è e passa avanti: è materiale per il confronto | |
| Build modifica `orchestratore.md` | Build è disponibile con Maiusc+Tab? Legge `quaderno_prove.txt` e `orchestratore.md`? Chiede il permesso prima di scrivere in `.opencode\agents`? La finestra del permesso mostra la modifica (prima e dopo) o solo il nome del file? Chiede di eseguire comandi (nella lezione 5 aveva chiesto `Get-ChildItem …`)? Funziona con il modello Big Pickle e con la rete della scuola? | Se Build non può scrivere in `.opencode\agents`: dì di chiedere la modifica a `orchestratore.txt` (nella cartella `laboratorio`) e di incollare poi il testo in `orchestratore.md`. Se la finestra non mostra la modifica: dì di chiedere prima la modifica in Plan, che non scrive file, di leggerla, e solo dopo di passare a Build e farla applicare | |
| Intestazione del file dell'agente | `description` senza due punti seguiti da spazio nel testo (in YAML romperebbero la lettura): il file di `MODELLI_OPENCODE_LEZIONE6/` è già a posto | Togli i due punti dal testo | |
| Cartella `.opencode\agents` nel computer virtuale | Copia il file `orchestratore.md` in `Documenti\laboratorio\.opencode\agents\`. Esplora risorse non accetta nomi che cominciano con il punto (da verificare: `.opencode.`, oppure `mkdir .opencode\agents` da terminale). Blocco note può salvare `.md.txt` con le estensioni nascoste: per questo il file è già creato e lo studente lo apre e lo salva senza cambiare nome | Dalla finestra di opencode chiusa: `mkdir .opencode\agents`, poi copia il file | |
| File nel computer virtuale, andata e ritorno | Come si portano nel computer virtuale `orchestratore.txt`, `quaderno_prove.txt` e i tre testi del noleggio (Teams nel browser della macchina, cartella condivisa, altro)? Come si riporta indietro una correzione di Build per applicarla in `orchestratore.txt`? La consegna (parte 4) dice solo «portate lì i file»: aggiungi il modo che funziona | Scrivi il modo alla lavagna o sulla prima slide della parte 4 (slide 18). Per il ritorno basta ricopiare le righe cambiate a mano | |
| Lunghezza del quaderno | Cinque prove con otto righe restano leggibili e incollabili con l'orchestratore? | Dì di annotare in breve | |
| Che cosa si è fatto davvero in lezione 5 | Nell'aula del 19 novembre l'esercizio ha usato davvero i termini «lavoro» ed «elenco delle richieste»? Si diceva «skill» e «routing»? | Adegua le parole a voce; i materiali dicono «lavoro» e ricordano skill | |

## Parte 1 · Le prove (slide 2–11)

Che cosa si fa: ogni studente scrive i lavori e gli accessi, scrive il criterio, inventa cinque richieste e le annota.

- **Slide 2.** Riparte dall'orchestratore con tre righe d'esempio: da qui gli studenti vedono che cosa sono un lavoro, un accesso e l'elenco delle richieste. Il loro orchestratore può avere righe diverse: va bene.
- **Slide 3.** Un errore vero, senza ancora il nome del rimedio: l'utente vede il registro. Chiedi chi se ne accorge e chi lo sistema, e lascia rispondere.
- **Slide 4.** Il quadro in quattro passi. Qui compare il nome «feedback processor», con la differenza tra Copilot (testo) e opencode (scrive nel file con il permesso).
- **Slide 5.** Due file in Blocco note: orchestratore e quaderno. I passi sono nella consegna (1A). Chi vede un elenco diverso dal tuo va bene: conta il suo. Chi non ha l'orchestratore chiede il testo di partenza.
- **Slide 6.** Riassunto del quaderno di un orchestratore d'esempio su Ruota Libera, scritto a mano: la prova 3 è un ERRORE di permesso. La domanda del titolo si fa a mano alzata. Il giudizio OK/ERRORE è definito nella riga sopra la tabella.
- **Slide 7.** Il criterio viene prima. L'esempio è un criterio debole con le domande per migliorarlo, senza la risposta: gli studenti scrivono il proprio sul loro orchestratore.
- **Slide 8.** Gli studenti inventano le richieste: una per ciascun lavoro, una ambigua, una non permessa. Non ci sono richieste pronte: una richiesta uguale a un esempio dell'elenco passa per costruzione, chiedi di riformularla. Prima di inviarne una scrivono quale lavoro si aspettano. Come scrivere l'accesso nel messaggio è nella consegna 1D. I valori di riferimento per giudicare le risposte sono in fondo a questa guida.
- **Slide 9.** Il blocco della prova 3 d'esempio mostra i campi; il Motivo serve dopo, per scrivere la correzione. «Lavoro che ha risposto» si scrive solo se la risposta lo dice. Con il testo di partenza un rifiuto giusto compare come «Lavoro usato: nessuno.»: è OK.
- **Slide 10.** Controllo a mano alzata prima di dare la regola: un rifiuto giusto è OK.
- **Slide 11.** I tre giudizi. NON_ESEGUITO è solo per quando il programma non ha risposto. Tutte OK è valido: se a voce qualcuno dice «Copilot non ha sbagliato niente», chiedi se il criterio era scritto prima e se le due richieste difficili lo erano davvero.

## Parte 2 · Correggete voi (slide 12–15)

- **Slide 13.** Prima di ogni nome, la domanda: che cosa scrivereste per correggerlo? L'esempio è un errore di dato inventato (orario sbagliato), diverso dal permesso della slide 3 che quasi tutti avranno nel proprio quaderno. Lascia rispondere due o tre studenti.
- **Slide 14.** Correzione d'esempio scritta a mano, su un altro quaderno: una causa, una modifica con il punto preciso.
- **Slide 15.** Lo studente scrive Causa e Modifica per il primo ERRORE in `mia_correzione.txt` e non la applica. Deve restare sul suo computer: serve a un confronto onesto con i programmi. La slide separa il Motivo (che cosa è andato storto nella risposta) dalla Causa (che cosa manca nelle istruzioni): se uno studente ricopia il Motivo, chiedigli che cosa manca nelle istruzioni. Chi non ha ERRORE scrive «nessuna correzione necessaria» e fa lo stesso le parti 3 e 4: si vede se Copilot e Build inventano errori.

## Parte 3 · La correzione di Copilot (slide 16–17)

- **Slide 17.** Esercizio a metà: l'esempio è la prova 5 della slide 14, a destra le domande, mai le risposte. Lo studente decide da solo che cosa incollare (servono anche le regole del noleggio per un dato inventato?), per quale prova chiedere, che cosa vietare e che cosa far controllare. La richiesta non deve contenere la sua correzione. Se Copilot riscrive tutte le istruzioni, è materiale per il confronto: lascialo vedere.

## Parte 4 · opencode in Build (slide 18–21)

- **Slide 18.** Plan e Build sono definiti qui in una frase: erano già stati mostrati nella lezione 5. Chi non riesce ad aprire opencode passa alla parte 5 con due correzioni.
- **Slide 19.** Un agente è un file; il nome dell'agente è il nome del file; l'intestazione è mostrata prima di essere nominata. Il file con la sola intestazione è già nella cartella (vedi controlli). I tre testi del noleggio restano file e l'agente li legge: lo studente cambia la frase che dice dove prenderli (consegna 4A, passo 3).
- **Slide 20.** Quattro cose da decidere e scrivere a Build; niente esempio, per non dare la richiesta pronta. Nella consegna 4B, passo 2, ci sono gli stessi quattro punti, in forma di domanda. La richiesta non contiene né la correzione dello studente né quella di Copilot.
- **Slide 21.** Il permesso: lo studente legge file e modifica prima di approvare. Allow once (consenti una volta) o Reject (rifiuta). Se compare un comando: Reject e «Senza comandi, leggi i file.», come nella lezione 5. Non verificato: che il permesso mostri la modifica (vedi controlli).

## Parte 5 · Tre correzioni, una sola (slide 22–27)

- **Slide 23.** Le quattro domande danno il criterio per confrontare. La quarta chiede una prova OK che la correzione potrebbe rompere: la scrive e la riprova alla slide 25. Lo studente può tenere la propria, una delle altre o un misto, e lo scrive in `mia_correzione.txt`. Chi ha solo due correzioni confronta quelle.
- **Slide 24.** Si applica una modifica, a mano, in `orchestratore.txt`; come aggiornare l'orchestratore (agente di Copilot, primo messaggio, opencode) lo dice la consegna 5B. Nessuno strumento applica in automatico, tranne Build in `orchestratore.md`, che è comunque un'altra copia: `orchestratore.txt` resta quello da correggere. Chi non ha correzione salta passo e prova.
- **Slide 25.** Si ripete la richiesta ERRORE, scritta con altre parole (decisione del docente del 23 novembre), e la prova OK indicata al punto 4 della slide 23. Poi si scrivono Prima e Dopo nel quaderno. Una richiesta riscritta può finire in un altro lavoro per un motivo diverso: se succede, è materiale per un secondo errore, non per il giro di oggi.
- **Slide 26.** I criteri dopo la prova: una riga precisa, la causa nel testo giusto, le prove OK restano OK, i permessi si rispettano, i dati vengono dai testi. La domanda in fondo: chi ha corretto meglio, lo studente, Copilot o Build? Senza un dato la risposta è di gusto: sostienila con la prova della slide 25. Non richiamare la domanda «chi ha controllato il numero?» della lezione 5, se non l'hai fatta davvero in aula.
- **Chiusura.** Slide 27: due domande a voce a chi vuole rispondere. Nessuna consegna.

## Valori di riferimento per giudicare le richieste degli studenti

Gli studenti inventano le richieste: non c'è un elenco unico da confrontare. Per controllare le risposte sul noleggio usa questi valori, ricavati dal registro e dalla guida dallo script `genera_materiali.py`, non scritti a mano.

{{VALORI_REGISTRO}}

Che cosa contiene la guida ai guasti, guasto per guasto:

{{VALORI_GUIDA}}

## Se qualcosa non passa

| Che cosa | Che cosa fai |
| --- | --- |
| Copilot non risponde una volta | Aspetta senza rimandare: l'indirizzo della scuola è condiviso. Segna NON_ESEGUITO e passa alla richiesta successiva |
| Copilot non risponde per più richieste di fila | Anticipa la parte 4A: gli studenti fanno le prove della parte 1 con l'agente `orchestratore` in opencode, se il modello risponde. Le parti 2, 3 e 5 si fanno quando Copilot torna |
| opencode non raggiunge il modello | Il confronto si fa con due correzioni; opencode si mostra dal proiettore |
| Build non può scrivere in `.opencode\agents` | Chiedi la modifica a `orchestratore.txt` nella cartella `laboratorio` |
| La finestra del permesso non mostra la modifica | Chiedi prima la modifica in Plan, leggila, poi passa a Build e falla applicare |
| La richiesta a Copilot è troppo lunga per un messaggio | Orchestratore in un messaggio, quaderno nel successivo |
| Il quaderno è troppo lungo | Due prove e il criterio bastano per chiedere la correzione |
| Uno studente non ha l'orchestratore | Dagli il testo di partenza: tutto il resto è uguale |

## Che cosa non è stato provato

- L'orchestratore di partenza, Copilot come feedback processor e il comportamento di Copilot con quaderno e orchestratore insieme in un messaggio.
- Build che modifica `orchestratore.md`: permesso, finestra con la modifica, rete della scuola con molti studenti insieme (il 4 novembre Copilot non ha risposto per circa 10 minuti).
- Il testo di partenza è una ricostruzione, allineata all'esercizio originale della lezione 5 solo per i permessi.
- Nessuna prova è stata fatta con l'account studente.

## Chiusura dal proiettore

Slide 27: «Chi ha deciso che cosa?» A voce, per chi vuole rispondere. Poi si chiude: la prossima lezione è la 7.
