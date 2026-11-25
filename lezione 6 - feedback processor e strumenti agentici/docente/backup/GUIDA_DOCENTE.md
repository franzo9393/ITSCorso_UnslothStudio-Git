# Guida docente · Lezione 6

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot e opencode**

Documento riservato al docente. Le decisioni e i motivi sono in `docente/backup/PIANO_LEZIONE6.md`; qui c'è ciò che serve per condurre.

## La lezione da condurre

Si riparte dall'orchestratore costruito nella lezione 5. Il filo è uno solo: lo studente corregge, poi lo fanno due programmi, poi si confronta. Gli studenti lavorano in Copilot sul proprio computer; opencode lo usi tu dal proiettore, una volta sola (decisione del 25 novembre 2026, per alleggerire la lezione).

1. **Prove** (slide 2–11). Gli studenti vedono un esempio di errore (slide 3), il giro in quattro passi (slide 4), scrivono il criterio (slide 7), inventano tre richieste (slide 8) e annotano ogni prova in una riga del quaderno (slide 9–11).
2. **La correzione dello studente** (slide 12–15). Vedono una correzione d'esempio (Causa e Modifica) e scrivono la propria per il primo ERRORE, nella parte CORREZIONE del quaderno. Non la applicano ancora.
3. **La correzione di Copilot** (slide 16–17). Lo studente scrive la richiesta a Copilot, senza la propria correzione. Copilot fa da feedback processor: legge criterio e prove e propone.
4. **La correzione di Build, dal proiettore** (slide 18–20). Tu fai correggere a Build un orchestratore d'esempio (quello della prova 3, l'utente che vede il registro). La classe decide la richiesta (slide 19) e vota il permesso (slide 20).
5. **Tre correzioni da confrontare** (slide 21–26). Confronto a tre domande, applicazione, prova prima e dopo con la richiesta riscritta, criteri dopo la prova, chiusura.

Parole: sulle slide e nella consegna si dice **lavoro** (la consegna ricorda che nella lezione 5 si chiamava anche skill), **accesso** (utente o amministratore), **quaderno delle prove**, **giudizio**, **criterio**, **correzione** (con Causa e Modifica). «Feedback processor» compare nel titolo e alla slide 4, dopo l'esempio, ed è il nome del ruolo di Copilot e di Build. «Competenza» e «instradamento» restano in guida e a voce. «Registro» indica solo il registro del noleggio: per le prove si dice quaderno.

Ogni parola nuova compare prima in un esempio e poi con il suo nome. Dove si incontra la prima volta:

| Parola | Esempio (slide) | Nome e definizione (slide) |
| --- | --- | --- |
| lavoro, accesso | tre righe d'esempio (2) | stessa slide, dopo la tabella |
| feedback processor | errore dell'utente che vede il registro (3) | giro in quattro passi (4) |
| quaderno, giudizio | due file in Blocco note (5); prove d'esempio (6) | stessa slide 6, riga sopra la tabella |
| criterio | «Le risposte devono essere giuste» (7) | stessa slide |
| Causa e Modifica | correzione d'esempio (13–14) | stessa slide 14; Motivo contro Causa alla slide 15 |
| Plan e Build | sezione (18) | stessa slide |

Come nelle lezioni 4 e 5: lavoro singolo, niente giro tra i banchi, niente file da consegnare, niente voto. I risultati si leggono sugli schermi e dal proiettore; i criteri si mostrano dopo la prova (slide 25 dopo la 24). Un quaderno con tutte le prove OK è valido: nessuna attività si basa sull'errore del modello. Copilot propone solo testo, gli studenti decidono. Build invece scrive davvero nel file, ma solo dopo il permesso: dillo, è la differenza tra una proposta e un'azione eseguita.

Non dichiarare provato ciò che non lo è: nulla di questa lezione è stato provato in Copilot con l'account studente né in opencode.

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE6.docx` e i tre testi del noleggio: `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt` (stessi fatti delle lezioni 4 e 5). Non pubblicare le cartelle di backup.
- `studenti/da_pubblicare_a_chi_non_ha_l_orchestratore/ISTRUZIONI_ORCHESTRATORE_PARTENZA.txt`: lo dai solo a chi non ha l'orchestratore della lezione 5 o non funziona. Costruito dal piano e allineato all'esercizio originale per i permessi: GUASTI per utente e amministratore, REGISTRO solo amministratore, REGOLE solo utente. Ipotesi mie: gli accessi si scelgono con la riga «Accesso:» scritta nel messaggio; la riga «Lavoro usato:» in testa alla risposta. Non è una soluzione collaudata. L'accesso con una riga che chiunque può riscrivere non è un controllo vero: puoi usarlo come spunto alla slide 25.
- Proiettore: prima le richieste e le domande, dopo i criteri. Nessuno studente condivide le proprie correzioni: i confronti sono sullo schermo di ognuno; se vuoi proiettarne uno, scegli tu uno studente che si offre.
- Dimostrazione di Build, sul tuo computer (o nel computer virtuale):
  - copia in `Documenti\laboratorio\.opencode\agents\` il file `docente/MODELLI_OPENCODE_LEZIONE6/dimostrazione/orchestratore_esempio.md`. È il testo di partenza **senza** la sezione «CHI PUÒ USARE CHE COSA», con i testi letti dai file: così l'errore della prova 3 è davvero possibile;
  - nella cartella operativa deve esserci una sola copia dell'agente dimostrativo, chiamata `orchestratore_esempio.md` (il nome del file è il nome dell'agente; la slide 19 elenca i file della cartella);
  - copia in `Documenti\laboratorio\` il file `dimostrazione/quaderno_prove.txt` (criterio e quattro prove d'esempio, scritte a mano: dì agli studenti, prima di usarlo, che gli esiti sono inventati per l'esercizio e non sono esecuzioni registrate) e i tre testi del noleggio;
  - controlla che in `Documenti\laboratorio` ci sia ancora `opencode.jsonc` della lezione 5 (se manca, ce n'è una copia in `dimostrazione/opencode.jsonc`: copiala lì; averlo non prova che il permesso funzioni, per questo la prova pre-aula è obbligatoria): fa chiedere il permesso prima di scrivere e prima dei comandi. Senza quel file Build scrive senza chiedere e la slide 20 non ha senso. La richiesta di permesso dipende da quella configurazione, non da Build in sé: se la finestra non mostra la modifica, segui l'alternativa Plan → Build della tabella dei controlli.
- Percorsi (cartella `Documenti\laboratorio`, da cui avvii opencode): il quaderno e i tre testi stanno in `laboratorio`; l'agente in `laboratorio\.opencode\agents\orchestratore_esempio.md`. Dopo la prova preliminare ripristina il file dalla copia in `dimostrazione/`, così il difetto della prova 3 c'è di nuovo, e in aula avvia Build in una conversazione nuova.
- Prova la dimostrazione una volta prima delle 14:00: è un prerequisito, perché il voto sul permesso (slide 20) dipende da ciò che la finestra mostra davvero. Se la richiesta che la classe decide alla slide 19 è vaga, aiutala a precisare: prova 3, file che può leggere (`quaderno_prove.txt`, `orchestratore_esempio.md`), solo `orchestratore_esempio.md` da modificare, una sola modifica.

### Controlli pre-aula

Nessuna riga è stata provata con Copilot e l'account studente né sui PC della scuola.

| Controllo | Che cosa accertare | Se fallisce | Esito |
| --- | --- | --- | --- |
| Quanti hanno un orchestratore | Quanti studenti hanno un orchestratore funzionante, in quale strumento (Copilot, Studio, opencode) e se la risposta dice quale lavoro ha usato | Il testo di partenza (non una soluzione) | |
| Il testo di partenza | Con i tre testi incollati e «Accesso: utente» o «Accesso: amministratore» in fondo: sceglie il lavoro giusto, scrive «Lavoro usato:», rifiuta REGISTRO all'utente e REGOLE all'amministratore, non cede a «sono il titolare»? | Correggi il file; dillo agli studenti | |
| Lunghezza dei messaggi in Copilot | Testo di partenza più tre testi sono circa 15.000 caratteri. Il campo dell'account studente li accetta in un solo messaggio? Orchestratore, criterio, prove con le risposte e fonti del noleggio entrano in un solo messaggio (con le risposte per esteso, più di 5.000 caratteri)? | Per il testo di partenza: due messaggi nella stessa conversazione. Per la richiesta a Copilot (slide 17): orchestratore e fonti del noleggio in un messaggio, criterio e prove con le risposte nel successivo (CORREZIONE resta fuori) | |
| Copilot come feedback processor | Con criterio e due o tre prove (una ERRORE) e l'orchestratore: scrive una causa e una modifica? Riscrive tutte le istruzioni? Con tutte le prove OK inventa una correzione? | Mostra com'è e passa avanti: è materiale per il confronto | |
| Build corregge la dimostrazione | Build è disponibile con Maiusc+Tab? Legge `quaderno_prove.txt` e `orchestratore_esempio.md`? Chiede il permesso prima di scrivere in `.opencode\agents`? La finestra del permesso mostra la modifica (prima e dopo) o solo il nome del file? Chiede di eseguire comandi (nella lezione 5 aveva chiesto `Get-ChildItem …`)? Funziona con il modello Big Pickle e con la rete della scuola? | Se Build non può scrivere in `.opencode\agents`: chiedi la modifica a un file nella cartella `laboratorio`. Se la finestra non mostra la modifica: chiedi prima la modifica in Plan, leggila ad alta voce, poi passa a Build e falla applicare | |
| Intestazione del file dell'agente | `description` senza due punti seguiti da spazio nel testo (in YAML romperebbero la lettura): il file di `MODELLI_OPENCODE_LEZIONE6/dimostrazione/` è già a posto | Togli i due punti dal testo | |
| Cartella `.opencode\agents` | Esplora risorse non accetta nomi che cominciano con il punto (da verificare: `.opencode.`, oppure `mkdir .opencode\agents` da terminale). Blocco note può salvare `.md.txt` con le estensioni nascoste: per questo il file è già pronto | Dalla finestra di opencode chiusa: `mkdir .opencode\agents`, poi copia il file | |
| Lunghezza del quaderno | Tre prove e il criterio restano leggibili e incollabili con l'orchestratore? | Dì di annotare in breve | |
| Che cosa si è fatto davvero in lezione 5 | Nell'aula del 19 novembre l'esercizio ha usato davvero i termini «lavoro» ed «elenco delle richieste»? Si diceva «skill» e «routing»? | Adegua le parole a voce; i materiali dicono «lavoro» e ricordano skill | |

## Parte 1 · Le prove (slide 2–11)

Che cosa si fa: ogni studente scrive i lavori e gli accessi, scrive il criterio, inventa tre richieste e le annota.

- **Slide 2.** Riparte dall'orchestratore con tre righe d'esempio: da qui gli studenti vedono che cosa sono un lavoro e un accesso. Il loro orchestratore può avere righe diverse: va bene.
- **Slide 3.** Un esempio di errore, senza ancora il nome del rimedio: l'utente vede il registro. Chiedi chi se ne accorge e chi lo sistema, e lascia rispondere. È anche l'errore che Build corregge alla slide 19.
- **Slide 4.** Il quadro in quattro passi. Qui compare il nome «feedback processor», con la differenza tra Copilot (testo) e opencode (scrive nel file con il permesso).
- **Slide 5.** Due file in Blocco note: orchestratore e quaderno, con tre parti (CRITERIO, PROVE, CORREZIONE). I passi sono nella consegna (1A). Chi vede un elenco diverso dal tuo va bene: conta il suo. Chi non ha l'orchestratore alza la mano (slide 5) e riceve il testo di partenza: portalo su Teams o dallo a voce con il nome del file.
- **Slide 6.** Le prove di un quaderno d'esempio su Ruota Libera, scritto a mano: la prova 3 è un ERRORE di permesso. La domanda del titolo si fa a mano alzata. Il giudizio OK/ERRORE è definito nella riga sopra la tabella.
- **Slide 7.** Il criterio viene prima. L'esempio è un criterio debole con le domande per migliorarlo, senza la risposta: gli studenti scrivono il proprio sul loro orchestratore.
- **Slide 8.** Gli studenti inventano tre richieste: una normale, una ambigua, una non permessa. Non ci sono richieste pronte: una richiesta uguale a un esempio dell'elenco passa per costruzione, chiedi di riformularla. Prima di inviarne una scrivono l'esito atteso: un lavoro, una domanda di chiarimento o un rifiuto. Come scrivere l'accesso nel messaggio è nella consegna 1D. I valori di riferimento per giudicare le risposte sono in fondo a questa guida.
- **Slide 9.** Una riga per prova: numero, richiesta con l'accesso, esito atteso, giudizio; il motivo solo se è ERRORE. Il motivo serve dopo, per scrivere la correzione. Con il testo di partenza un rifiuto giusto compare come «Lavoro usato: nessuno.»: è OK.
- **Slide 10.** Controllo a mano alzata prima di dare la regola: un rifiuto giusto è OK.
- **Slide 11.** I tre giudizi. NON_ESEGUITO è solo per quando il programma non ha risposto. Tutte OK è valido: se a voce qualcuno dice «Copilot non ha sbagliato niente», chiedi se il criterio era scritto prima e se le due richieste difficili lo erano davvero.

## Parte 2 · Correggete voi (slide 12–15)

- **Slide 13.** Prima di ogni nome, la domanda: che cosa scrivereste per correggerlo? L'esempio è un errore di dato inventato (orario sbagliato), diverso dal permesso della slide 3, che è quello su cui lavora Build. Lascia rispondere due o tre studenti.
- **Slide 14.** Correzione d'esempio scritta a mano, su un altro quaderno: una causa, una modifica con il punto preciso.
- **Slide 15.** Lo studente scrive Causa e Modifica per il primo ERRORE sotto CORREZIONE e non la applica. Quando incolla il quaderno in Copilot, lascia fuori CORREZIONE: serve a un confronto onesto. La slide separa il Motivo (che cosa è andato storto nella risposta) dalla Causa (che cosa manca nelle istruzioni): se uno studente ricopia il Motivo, chiedigli che cosa manca nelle istruzioni. Chi ha tutte le prove OK scrive per ciascuna la frase che la conferma (dal testo del noleggio per i dati, dalle istruzioni o dal criterio per un rifiuto o una domanda di chiarimento) e, per le due più difficili, perché nessuna modifica le migliorerebbe; poi «nessuna correzione necessaria». È il suo lavoro di oggi, insieme alla parte 3 (Copilot controlla le prove senza le colonne Giudizio e Motivo), dove si vede se Copilot inventa errori. Chi ha prove parziali valuta quelle eseguite, lascia NON_ESEGUITO le altre e, se manca la seconda prova, scrive «seconda prova non disponibile» senza inventare un giudizio. Se tra le prove eseguite non c'è nessun ERRORE ma qualcuna è NON_ESEGUITO, conferma quelle eseguite come nel caso «tutte OK», scrivi «nessun errore nelle prove eseguite; verifica incompleta» e nessuna modifica. Chi ha solo NON_ESEGUITO rifà le prove una volta; se Copilot ancora non risponde, la verifica del suo orchestratore oggi non è possibile e segue la dimostrazione senza ripetizioni. Chi ha ERRORE senza nessuna prova OK sceglie il primo ERRORE e, come seconda prova, un'altra richiesta già eseguita: nel quaderno resta il suo giudizio vero.

## Parte 3 · La correzione di Copilot (slide 16–17)

- **Slide 17.** Esercizio a metà: l'esempio è la prova 5 della slide 14, a destra le domande, mai le risposte. Lo studente decide da solo che cosa incollare (servono anche le regole del noleggio per un dato inventato?), per quale prova chiedere, che cosa vietare e che cosa far controllare. La richiesta non deve contenere la sua correzione. Se Copilot riscrive tutte le istruzioni, è materiale per il confronto: lascialo vedere. Lo studente copia causa e modifica di Copilot sotto CORREZIONE.

## Parte 4 · Build corregge, dal proiettore (slide 18–20)

Gli studenti non aprono opencode. Lo schermo è il tuo: Build corregge la copia operativa dell'orchestratore d'esempio in `laboratorio\.opencode\agents` (l'originale resta in `dimostrazione/`; vedi «Da predisporre»).

- **Slide 18.** Plan e Build sono definiti in una frase: erano già stati mostrati nella lezione 5. Un agente di opencode è un file: dillo a voce mentre apri `orchestratore_esempio.md` (intestazione di due righe, poi le istruzioni).
- **Slide 19.** La classe decide con te la richiesta a Build: per quale prova, quali file può leggere, quale file può modificare, quanto può cambiare. Scrivila sul proiettore quando l'hanno detta. Non contiene nessuna correzione. Se è troppo vaga, chiedi che cosa può succedere se Build può modificare tutti i file.
- **Slide 20.** Il permesso: leggete insieme file e modifica prima di approvare (se la finestra mostra solo il nome del file, la modifica si legge prima in Plan, come dice la consegna). Voto per alzata di mano: Allow once (consenti una volta) o Reject (rifiuta). Se la maggioranza rifiuta, rifiuta davvero e fai riscrivere la richiesta. Se compare un comando: Reject e «Senza comandi, leggi i file.», come nella lezione 5. Non verificato: che il permesso mostri la modifica (vedi controlli). Gli studenti copiano la modifica di Build sotto CORREZIONE.

## Parte 5 · Tre correzioni da confrontare (slide 21–26)

- **Slide 22.** Le domande della consegna 5A danno il criterio per confrontare. La terza chiede una seconda prova (di solito una OK, il giudizio vero resta nel quaderno) che la correzione potrebbe rompere: la scrive e la riprova alla slide 24. Lo studente può tenere la propria, quella di Copilot o un misto (Build è il metodo da confrontare), e lo scrive sotto CORREZIONE. La correzione di Build vale per l'errore della prova 3 e non si applica al file di chi ha un errore diverso: la consegna chiede di confrontare la propria con quella di Copilot (stesso errore) e di guardare Build come metodo (una riga o tutto il testo, nomina la causa), prendendone al più il principio. Chi non ha Build (o Build non ha funzionato) confronta le due che ha.
- **Slide 23.** Si applica una modifica, a mano, in `orchestratore.txt`; come aggiornare l'orchestratore (agente di Copilot, primo messaggio) lo dice la consegna 5B. Nessuno strumento applica in automatico, tranne Build nel file dimostrativo: è un'altra copia, `orchestratore.txt` resta quello da correggere. Chi non ha correzione salta passo e prova.
- **Slide 24.** Si ripete la richiesta ERRORE, scritta con altre parole (decisione del docente del 23 novembre), e la seconda prova scelta alla slide 22 (di solito una OK). Poi si scrivono Prima e Dopo sotto CORREZIONE. Una richiesta riscritta può finire in un altro lavoro per un motivo diverso: se succede, è materiale per un secondo errore, non per il giro di oggi.
- **Slide 25.** I criteri dopo la prova: una riga precisa, la causa nel testo giusto, le prove OK restano OK, i permessi si rispettano, i dati vengono dai testi. Chiedi quale delle tre correzioni li rispetta di più, sostenendo la risposta con la prova della slide 24. Non richiamare la domanda «chi ha controllato il numero?» della lezione 5, se non l'hai fatta davvero in aula.
- **Chiusura.** Slide 26: due domande a voce a chi vuole rispondere. Nessuna consegna.

## Valori di riferimento per giudicare le richieste degli studenti

Gli studenti inventano le richieste: non c'è un elenco unico da confrontare. Per controllare le risposte sul noleggio usa questi valori, ricavati dal registro e dalla guida dallo script `genera_materiali.py`, non scritti a mano.

{{VALORI_REGISTRO}}

Che cosa contiene la guida ai guasti, guasto per guasto:

{{VALORI_GUIDA}}

## Se qualcosa non passa

| Che cosa | Che cosa fai |
| --- | --- |
| Copilot non risponde una volta | Aspetta senza rimandare: l'indirizzo della scuola è condiviso. Segna NON_ESEGUITO e passa alla richiesta successiva |
| Copilot non risponde per più richieste di fila | Fai la dimostrazione di Build (parte 4) mentre gli studenti aspettano; chi ha già prove prosegue con le parti 2, 3 e 5 quando Copilot torna; chi non ne ha rifà le prove una sola volta, poi la verifica del suo orchestratore oggi non è possibile e segue la dimostrazione senza ripetizioni |
| opencode non raggiunge il modello | Il confronto si fa con due correzioni; racconta a voce che cosa avrebbe fatto Build |
| Build non può scrivere in `.opencode\agents` | Chiedi la modifica a un file nella cartella `laboratorio` |
| La finestra del permesso non mostra la modifica | Chiedi prima la modifica in Plan, leggila ad alta voce, poi passa a Build e falla applicare |
| La richiesta a Copilot è troppo lunga per un messaggio | Orchestratore e fonti in un messaggio, criterio e prove con le risposte nel successivo; CORREZIONE resta fuori |
| Il quaderno è troppo lungo | Il criterio e due prove bastano per chiedere la correzione |
| Uno studente non ha l'orchestratore | Dagli il testo di partenza: tutto il resto è uguale |

## Che cosa non è stato provato

- L'orchestratore di partenza, Copilot come feedback processor e il comportamento di Copilot con orchestratore, criterio e prove insieme in un messaggio.
- Build che modifica `orchestratore_esempio.md` nella copia operativa in `laboratorio`: permesso, finestra con la modifica, rete della scuola (il 4 novembre Copilot non ha risposto per circa 10 minuti).
- Il testo di partenza è una ricostruzione, allineata all'esercizio originale della lezione 5 solo per i permessi.
- Nessuna prova è stata fatta con l'account studente.

## Chiusura dal proiettore

Slide 26: «Chi ha deciso che cosa?» A voce, per chi vuole rispondere. Poi si chiude: la prossima lezione è la 7.
