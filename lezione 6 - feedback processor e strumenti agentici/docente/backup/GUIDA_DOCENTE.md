# Guida docente · Lezione 6

**ITS MAKER Bologna · 25 novembre 2026 · Microsoft Copilot, Unsloth Studio e opencode**

Documento riservato al docente. Le decisioni e i motivi sono in `docente/backup/PIANO_LEZIONE6.md`; qui c'è ciò che serve per condurre.

## La lezione da condurre

Si riparte dall'orchestratore costruito nella lezione 5. Due filoni distinti, come hai chiesto il 19 novembre.

**Filone A: il ciclo della correzione.** Gli studenti scrivono il criterio con cui giudicheranno (slide 5), inventano cinque richieste (una per ciascun lavoro, una ambigua, una che l'accesso non permette) e annotano ogni prova nel quaderno (slide 6–9). Poi scelgono il tipo di ogni errore (slide 11), scrivono le istruzioni di un secondo agente, l'**agente delle correzioni** (nel piano: feedback processor), che legge il quaderno e il testo dell'orchestratore e per ogni ERRORE propone tipo, causa e una modifica (slide 12–15). Un solo giro di correzione: leggono la proposta, la applicano a mano, ripetono la richiesta sbagliata e una giusta e confrontano prima e dopo (slide 17–19). Si chiude con due correzioni da confrontare, una proposta riuscita e una scartata, i criteri e la domanda su come si controlla una proposta (slide 20–23).

**Filone B: Unsloth Studio e opencode** (slide 24–32). Si apre quando il filone A è chiuso; chi finisce prima comincia prima. Comincia con la miniguida per portare lo stesso orchestratore e lo stesso agente delle correzioni in Studio oppure in opencode (slide 25–30, consegna 4A o 4B; l'altro programma è facoltativo); poi libertà totale, nessuna consegna: le tre righe della slide 31 sono idee di partenza. La domanda finale (slide 32) si fa a voce.

Parole: sulle slide e nella consegna si dice **lavoro** (la consegna ricorda che nella lezione 5 si chiamava anche skill), **elenco delle richieste** (spiegato alla slide 17), **accesso** (utente o amministratore), **quaderno delle prove**, **giudizio**, **agente delle correzioni**. «Competenza», «instradamento» e «feedback processor» restano in guida e a voce. «Registro» indica solo il registro del noleggio: per le prove si dice quaderno, per non avere tre registri.

Come nelle lezioni 4 e 5: lavoro singolo, niente giro tra i banchi, niente file da consegnare, niente voto. I risultati si leggono sugli schermi e dal proiettore; i criteri si mostrano dopo la prova (slide 22 dopo la 21). Un quaderno con tutte le prove OK è valido: nessuna attività si basa sull'errore del modello. L'agente delle correzioni propone, gli studenti applicano: dillo, è un testo, non un'azione eseguita.

Non dichiarare provato ciò che non lo è: nulla di questa lezione è stato provato in Copilot con l'account studente, né in Studio né in opencode.

## Prima dell'aula

### Da predisporre

- Pubblica su Teams `studenti/ATTIVITA_LEZIONE6.docx` e i tre testi del noleggio: `Registro_Ruota_Libera_7-8_novembre_2026.txt`, `Regole_noleggio_Ruota_Libera.txt`, `Guida_guasti_Ruota_Libera.txt` (stessi fatti delle lezioni 4 e 5). Non pubblicare le cartelle di backup.
- `studenti/da_pubblicare_a_chi_non_ha_l_orchestratore/ISTRUZIONI_ORCHESTRATORE_PARTENZA.txt`: lo dai solo a chi non ha l'orchestratore della lezione 5 o non funziona. **Costruito dal piano, non dall'esercizio originale**: lo schema `system prompt routing interno esternojpg.jpg` e l'esercizio `esercizio sistema agentico.md` non erano nel repository il 19 novembre. Il file riprende ciò che il piano ne riferisce: due accessi, tre lavori, instradamento con elenco delle richieste e qualche esempio di richiesta per voce. Ipotesi mie, da confrontare con l'esercizio originale: (1) GUASTI solo utente, REGISTRO solo amministratore, REGOLE solo utente (lettura letterale del piano); (2) gli accessi si scelgono con la riga «Accesso:» scritta nel messaggio; (3) la riga «Lavoro usato:» in testa alla risposta. Correggi il file se differisce. Non è una soluzione collaudata. L'accesso con una riga che chiunque può riscrivere non è un controllo vero: puoi usarlo come spunto alla slide 22.
- `studenti/da_pubblicare_dopo_prova_agente_correzioni/ESEMPIO_ISTRUZIONI_AGENTE_CORREZIONI.txt`: lo pubblichi su Teams solo dopo la prova dell'agente delle correzioni (slide 14), perché la slide 15 chiede di aprirlo. Scritto a mano, non provato: non va presentato come soluzione.
- Proiettore: prima le richieste e le domande, dopo i criteri. Per le proposte degli studenti (slide 21): due volontari incollano la proposta riuscita e quella scartata nella chat di Teams della lezione, e tu la proietti.

### Controlli pre-aula

Nessuna riga è stata provata con Copilot e l'account studente né sui PC della scuola.

| Controllo | Che cosa accertare | Se fallisce | Esito |
| --- | --- | --- | --- |
| Quanti hanno un orchestratore | Quanti studenti hanno un orchestratore funzionante, in quale strumento (Copilot, Studio, opencode) e se la risposta dice quale lavoro ha usato | Il testo di partenza (non una soluzione) | |
| Il testo di partenza | Con i tre testi incollati e «Accesso: utente» o «Accesso: amministratore» in fondo: sceglie il lavoro giusto, scrive «Lavoro usato:», rifiuta REGISTRO all'utente e REGOLE all'amministratore, non cede a «sono il titolare»? | Correggi il file; dillo agli studenti | |
| Lunghezza dei messaggi in Copilot | Testo di partenza più tre testi sono circa 15.000 caratteri. Il campo dell'account studente li accetta in un solo messaggio? Istruzioni, quaderno e testo dell'orchestratore (circa 7.000 caratteri) entrano in un solo messaggio? | Ripiego pronto per il testo di partenza: due messaggi nella stessa conversazione (il file lo spiega). Per l'agente delle correzioni: istruzioni e quaderno in un messaggio, orchestratore nel successivo | |
| Agente delle correzioni in Copilot | Con l'esempio di istruzioni e un quaderno di due o tre prove (una ERRORE): scrive tipo, causa e modifica nel formato? Non cambia nulla? Con tutte OK scrive «Nessuna modifica necessaria.»? | Le istruzioni nel primo messaggio (è già il percorso principale): se il formato non è rispettato, mostra com'è e passa avanti | |
| Agente delle correzioni in Studio | Il modello da 2B accetta quaderno e orchestratore in 8192 token? Rispetta il formato? Quanto è lento? | Resta una scelta, con i limiti detti a voce | |
| Agente delle correzioni in opencode | Legge il quaderno da un file, scrive la proposta in un altro, chiede il permesso prima di scrivere? Rete della scuola con molti studenti insieme? | Si usa Copilot | |
| Quaderno e testi nel computer virtuale | Come si portano nel computer virtuale `orchestratore.txt`, `quaderno_prove.txt`, `istruzioni_correzioni.txt` e i tre testi del noleggio (Teams nel browser della macchina, cartella condivisa, altro)? La consegna (parte 4) dice solo «portate lì i file»: aggiungi il modo che funziona | Scrivi il modo alla lavagna o sulla prima slide del filone B | |
| Importare l'orchestratore in Studio e opencode (miniguida, slide 25–30) | Studio: `orchestratore.txt` nel System Prompt, tre testi nella chat con la riga dell'accesso; il contatore resta sotto …/8.2k con ragionamento attivo? Il modello da 2B segue l'elenco delle richieste e i permessi? opencode: gli agenti in `.opencode/agents/*.md` compaiono con Maiusc+Tab, con il nome del file? Serve riavviare dopo la modifica? Il nuovo agente eredita le regole di `opencode.jsonc` (permesso prima di scrivere, comandi) e il modello Big Pickle? Leggendo i tre file chiede di eseguire comandi (nella lezione 5 aveva chiesto `Get-ChildItem …`)? `correzioni` chiede il permesso prima di scrivere `proposta_correzioni.txt`? Formato dei file ricavato dalla documentazione di opencode (opencode.ai/docs/agents), non provato qui | Chi sceglie quella strada lo sa: nessuna condizione per la lezione | |
| Intestazione dei file degli agenti di opencode | `description` senza due punti seguiti da spazio nel testo (in YAML romperebbero la lettura): i due file di `MODELLI_OPENCODE_LEZIONE6/` sono già a posto, ma chi li modifica deve saperlo | Togli i due punti dal testo | |
| Cartella `.opencode\agents` nel computer virtuale | Copia i due file di `docente/MODELLI_OPENCODE_LEZIONE6/` (`orchestratore.md`, `correzioni.md`, con la sola intestazione) in `Documenti\laboratorio\.opencode\agents\`. La consegna dice che la cartella e i file ci sono già. Esplora risorse non accetta nomi che cominciano con il punto (da verificare: `.opencode.`, oppure `mkdir .opencode\agents` da terminale). Blocco note può salvare `.md.txt` con le estensioni nascoste: per questo i file sono già creati e lo studente li apre e li salva senza cambiare nome | Dalla finestra di opencode chiusa: `mkdir .opencode\agents`, poi copia i due file | |
| Lunghezza del quaderno | Cinque prove con otto campi restano leggibili e incollabili con l'orchestratore? | Dì di annotare in breve | |
| Pagina `.html` della lezione 5 | Chi vuole estenderla in opencode la ha ancora? Plan e Build funzionano come in lezione 5? | L'idea di opencode da riformulare a voce | |
| Che cosa si è fatto davvero in lezione 5 | Nell'aula del 19 novembre l'esercizio ha usato davvero i termini «lavoro» ed «elenco delle richieste»? Si diceva «skill» e «routing»? | Adegua le parole a voce; i materiali dicono «lavoro» e ricordano skill | |

## Parte 1 · Il quaderno delle prove (slide 2–9)

Che cosa si fa: ogni studente scrive i lavori e gli accessi, scrive il criterio, inventa cinque richieste e le annota.

- **Slide 3.** Un solo gesto: creare il quaderno e scrivere i tre lavori con gli accessi. Aprire e copiare l'orchestratore in `orchestratore.txt` è nella consegna (1A). Chi vede un elenco diverso dal tuo va bene: conta il suo. Chi non ha l'orchestratore chiede il testo di partenza.
- **Slide 4.** Quaderno di un orchestratore d'esempio su Ruota Libera, scritto a mano: la prova 3 è un ERRORE di permesso. Gli esempi usano lo stesso negozio degli studenti (decisione del docente del 20 novembre); la slide dice che non è il loro quaderno. Fai notare che è un riassunto: il campo Motivo e gli altri compaiono alla slide 7.
- **Slide 5.** Il criterio viene prima. L'esempio è un criterio debole («Le risposte devono essere giuste.») con le domande per migliorarlo, senza la risposta: gli studenti scrivono il proprio sul loro orchestratore.
- **Slide 6.** Gli studenti inventano le richieste: una per ciascun lavoro, una ambigua, una non permessa. Non ci sono richieste pronte, e la slide esclude quelle della slide 4 e quelle usate come esempio nel loro orchestratore: una richiesta uguale a un esempio dell'elenco passa per costruzione, chiedi di riformularla. Prima di inviarne una scrivono quale lavoro si aspettano. Per giudicare le risposte sul noleggio, i valori di riferimento sono in fondo a questa guida.
- **Slide 7.** Il blocco della prova 2 d'esempio mostra i campi. Il campo Motivo serve all'agente delle correzioni: senza motivo la causa è un'ipotesi. «Lavoro che ha risposto» si scrive solo se la risposta lo dice: gli orchestratori della lezione 5 potrebbero non scrivere «Lavoro usato:».
- **Slide 8.** I tre giudizi. Un rifiuto giusto è OK; NON_ESEGUITO è solo per quando Copilot non ha risposto.
- **Slide 9.** Tutte OK è valido. Se a voce qualcuno dice «Copilot non ha sbagliato niente», chiedi se il criterio era scritto prima e se le due richieste difficili lo erano davvero.

## Parte 2 · L'agente delle correzioni (slide 10–15)

Che cosa si fa: gli studenti scelgono il tipo di ogni errore, scrivono le istruzioni di un secondo agente e lo provano nello strumento che scelgono.

- **Slide 11.** I quattro tipi sono definiti con un esempio su Ruota Libera prima di chiedere di usarli. Gli studenti scelgono il tipo di ogni ERRORE e lo annotano fuori dal quaderno: alla slide 17 lo confrontano con quello dell'agente. Se uno studente propone un quinto tipo, vale se lo definisce in una riga.
- **Slide 12.** Proposta scritta a mano per la prova 3. Dillo: non è una risposta di Copilot. Nell'esempio il permesso sta dentro REGISTRO, come nell'esercizio della lezione 5; nel testo di partenza sta invece nella sezione «CHI PUÒ USARE CHE COSA». Se la proposta del loro agente coincide parola per parola con questa, chiedi se l'esempio è finito nelle istruzioni.
- **Slide 13.** Esercizio a metà: a sinistra proposte che l'agente non dovrebbe scrivere, a destra le domande, mai le risposte. Gli studenti decidono da soli come limitare il numero di modifiche, che cosa vietare, che cosa fare con le prove OK e che cosa indicare. Il formato della proposta lo hanno visto alla slide 12. Le istruzioni di esempio sono nella cartella separata e si pubblicano dopo.
- **Slide 14.** Scelta dello strumento: onere e onore dello studente. Copilot è lo strumento di riferimento. Studio e opencode sono ammessi ma non provati con questi testi (vedi controlli). Passa da una sola prova: non è previsto un secondo giro per correggere il formato.
- **Dopo la prova (slide 15).** Pubblica l'esempio di istruzioni su Teams e chiedi il confronto: che cosa c'è nel loro che qui manca, e viceversa.

## Parte 3 · Un giro di correzione (slide 16–23)

- **Slide 17.** Le tre domande danno il criterio per leggere la proposta. «Elenco delle richieste» è spiegato lì in una riga. Chi trova una proposta sbagliata la tiene per la slide 21. Chi ha tutte le prove OK controlla che l'agente non inventi errori: la proposta giusta è «Nessuna modifica necessaria».
- **Slide 18.** Una modifica, a mano, e l'aggiornamento dell'orchestratore. L'agente delle correzioni non applica nulla; se uno studente lo ha lasciato scrivere nel file dell'orchestratore, in opencode, deve averlo approvato lui.
- **Slide 19.** Si ripete la richiesta ERRORE e una richiesta OK, che deve restare OK. Poi si scrivono Prima e Dopo nel quaderno.
- **Slide 20.** Due correzioni entrambe plausibili, per un'altra prova finita nel lavoro sbagliato. A tocca la causa (una riga precisa nell'elenco delle richieste, alla voce REGOLE), B mette una toppa nel lavoro sbagliato. Come terzo caso a voce: una regola troppo larga («ogni significato va a REGOLE») romperebbe «Che cosa significa catena che salta?», che è di GUASTI. Chiedi quale tengono e perché, prima della slide 22.
- **Slide 21.** Due volontari incollano la loro proposta riuscita e quella scartata nella chat di Teams: le proietti. Chiedi che cosa le distingue prima di mostrare i criteri.
- **Slide 22.** I criteri dopo la prova: una riga precisa, la causa nel testo giusto, le prove OK restano OK, i permessi si rispettano, i dati vengono dai testi.
- **Slide 23.** Anche le proposte dell'agente delle correzioni possono sbagliare. Che cosa permette di capirlo: il criterio scritto prima, il tipo annotato prima, il confronto prima e dopo. Non richiamare la domanda «chi ha controllato il numero?» della lezione 5, se non l'hai fatta davvero in aula.

## Parte 4 · Studio e opencode (slide 24–32)

- **Slide 25.** Una tabella che confronta i tre programmi: le istruzioni, i tre testi, la riga dell'accesso. Il testo dell'orchestratore resta lo stesso; in opencode cambia solo la frase su dove sono i testi. L'accesso è la riga che usa l'orchestratore dello studente (per esempio «Accesso: utente»): una convenzione scritta nel messaggio, non un vero login.
- **Slide 26–27 (Studio).** Schermata del campo System Prompt (dalla lezione 5); poi la domanda «che cosa fate prima di aprire la nuova chat?»: la risposta (cancellare l'orchestratore e incollare le istruzioni delle correzioni) è nella consegna 4A, punto 5. Nella guida della lezione 5 il System Prompt è rimasto dopo «Nuova chat» (provato su VMware). Il modello da 2B è lento e il contesto è 8.192 token (il contatore mostra …/8.2k): una richiesta per chat; nel quaderno il criterio e due o tre prove. Un orchestratore che sbaglia il lavoro è materiale per il quaderno, non un guasto della lezione.
- **Slide 28–30 (opencode).** Un agente è un file; il nome dell'agente è il nome del file. I due file con la sola intestazione sono già nella cartella (vedi controlli). I tre testi del noleggio restano file e l'agente li legge: lo studente cambia la frase che dice dove prendere i testi, nell'orchestratore e nell'agente delle correzioni, ed è parte dell'esercizio. Dopo ogni modifica ai file degli agenti, riavvio di opencode (non verificato se serva). Se compare un comando: Reject e «Senza comandi, leggi i file.», come nella lezione 5. L'agente delle correzioni scrive solo dopo il permesso, Allow once e il nome del file letto prima. Il file `opencode.jsonc` della lezione 5 fa già chiedere prima di scrivere (modello Big Pickle, in rete: controlla prima che risponda). La consegna chiede 4A oppure 4B; l'altra è facoltativa.
- **Dopo la miniguida (slide 31).** Libertà totale. Le tre righe sono idee di partenza, non consegne. Rischio: ognuno si ferma al facile (per esempio solo la temperatura). Non guidare i passi; se serve, ricorda la domanda finale.
- **Chiusura.** Slide 32: tre domande a voce a chi vuole rispondere. Nessuna consegna.

## Valori di riferimento per giudicare le richieste degli studenti

Gli studenti inventano le richieste: non c'è un elenco unico da confrontare. Per controllare le risposte sul noleggio usa questi valori, ricavati dal registro e dalla guida dallo script `genera_materiali.py`, non scritti a mano.

{{VALORI_REGISTRO}}

Che cosa contiene la guida ai guasti, guasto per guasto:

{{VALORI_GUIDA}}

## Se qualcosa non passa

| Che cosa | Che cosa fai |
| --- | --- |
| Copilot non risponde una volta | Aspetta senza rimandare: l'indirizzo della scuola è condiviso. Segna NON_ESEGUITO e passa alla richiesta successiva |
| Copilot non risponde per più richieste di fila | Apri prima il filone B: Studio gira sul modello locale. Si torna al filone A quando Copilot risponde |
| Il modello di Studio è troppo lento | La prova dell'agente delle correzioni si fa in Copilot; Studio resta nel filone B |
| opencode non raggiunge il modello | La prova dell'agente delle correzioni si fa in Copilot; opencode si mostra dal proiettore |
| Il quaderno è troppo lungo per un messaggio | Due prove e il criterio bastano per provare l'agente delle correzioni |
| Uno studente non ha l'orchestratore | Dagli il testo di partenza: tutto il resto è uguale |

## Che cosa non è stato provato

- L'orchestratore di partenza, l'agente delle correzioni (in nessuno dei tre strumenti), l'esempio di istruzioni e il comportamento di Copilot con quaderno e orchestratore insieme in un messaggio.
- L'importazione dell'orchestratore e dell'agente delle correzioni in Unsloth Studio e in opencode (miniguida, slide 25–30): per opencode il formato dei file è quello della documentazione ufficiale, non è stato eseguito.
- La rete della scuola con molti studenti insieme (il 4 novembre Copilot non ha risposto per circa 10 minuti).
- L'esercizio della lezione 5 originale e il suo schema: non erano nel repository; il testo di partenza è costruito dal piano.
- Nessuna prova è stata fatta con l'account studente.

## Chiusura dal proiettore

Slide 32: «Dove si è fermato il vostro programma?» A voce, per chi vuole rispondere. Poi si chiude: la prossima lezione è la 7.
