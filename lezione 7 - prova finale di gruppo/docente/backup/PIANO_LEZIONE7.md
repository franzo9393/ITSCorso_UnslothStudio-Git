# Piano della lezione 7 · 2 dicembre 2026

Documento riservato al docente. **Bozza da approvare**: non sono ancora materiali per gli studenti. Sostituisce la sezione «Lezione 7» di `lezione 4 - reti neurali e agenti con orchestrazione/docente/backup/BOZZA_PERCORSO_LEZIONI_4-7.md`. Rivista il 25 novembre 2026 dopo il parere del revisore didattico e del revisore studente (entrambi DA CORREGGERE sulla prima versione).

## Decisioni del docente (25 novembre 2026)

1. Durata: 4 ore. Prima metà: lavoro di gruppo. Seconda metà, che si chiama «collaudo e presentazione»: collaudo, teoria, presentazione dei gruppi, poi test individuale breve su carta. La parola «correzione» resta alla sezione CORREZIONE del quaderno della lezione 6.
2. 22 studenti, cinque gruppi: 4+4+4+5+5.
3. Casi assegnati dal docente, uno per gruppo, tutti diversi dal noleggio Ruota Libera. Va bene che non appartengano al mestiere.
4. Unsloth Studio e opencode: solo teoria, nessuna prova vera.
5. Voto di gruppo con parti firmate, presentazione a rotazione; più voto del test.
6. Teoria dopo il collaudo, con ordine nascosto in un documento e accesso falsificato come prove obbligatorie del collaudo.
7. Scambio dei file tra gruppi: chiavetta.
8. La lezione 6 si è svolta come da programma (dichiarato dal docente). Non è dichiarato: quanti studenti hanno un orchestratore funzionante e se Copilot ha risposto sempre. Sono verifiche pre-aula, non blocchi.
9. Per evitare che il lavoro passi tutto a Copilot (preoccupazione del docente, 25 novembre 2026): previsione scritta prima di ogni prova; tre numeri ricavati a mano dal registro stampato prima di aprire Copilot; presentazione con domande sul proprio testo, con persona scelta dal docente solo in quel momento; test con previsione.
10. Regola nella consegna: criterio, prove e giudizi li scrive una persona del gruppo; Copilot li riceve soltanto. La regola non è verificabile: le difese vere sono la previsione, le domande in presentazione e il test.
11. Peso del voto finale: 60% gruppo, 40% test.
12. I dati riservati (elenco dei destinatari della sicurezza, regole interne delle prenotazioni) si consegnano ai gruppi a parte, non nel pacchetto del caso. Le date dei casi le anticipa il docente.

## Che cosa sanno fare gli studenti

- Lezione 4: agente Copilot per Ruota Libera, con più lavori e un elenco delle richieste.
- Lezione 5: orchestratore con accesso amministratore o utente e tre lavori. Unsloth Studio e opencode solo mostrati.
- Lezione 6: quaderno con criterio, tre prove (normale, ambigua, non permessa), correzione a mano, proposta di Copilot, Build dal proiettore.

## Casi

Ogni caso ha tre testi inventati dal docente della stessa forma (registro, regole, guida), senza persone reali, coerenti tra loro e di lunghezza limitata, perché Copilot li riceve in un solo messaggio con l'orchestratore. Dati e valori di riferimento si ricavano con uno script; nei casi con date, «oggi» è fissato nei testi.

| Caso | Gruppo | Lavoro che dipende da un altro | Solo amministratore | Azione che l'agente non compie da solo | Informazione assente dai testi |
| --- | --- | --- | --- | --- | --- |
| Segnalazioni di sicurezza | da 5 | l'inoltro dipende dalla priorità; tabella delle priorità nelle regole, con regola fissa per il pericolo immediato | elenco dei destinatari | decidere di fermare un'attività; dire che un pericolo è «risolto» o «non grave» | gravità reale, valutata solo da una persona |
| Manutenzione programmata | da 5 | l'avviso dipende dalle scadenze e dagli interventi fatti | registro degli interventi | spostare una scadenza | intervento fatto ma non registrato |
| Stampanti 3D | da 4 | la diagnosi dipende dal registro guasti | registro e costi | cambiare i parametri della macchina | causa di un guasto non annotata |
| Prenotazione dei laboratori | da 4 | i conflitti dipendono dal calendario | regole d'uso interne | confermare una prenotazione | prenotazione fatta fuori dal calendario |
| Archivio attrezzi in prestito | da 4 | il ritiro dipende dai prestiti aperti | storico dei prestiti | segnare un attrezzo come restituito | stato dell'attrezzo al rientro |

Note:
- Nomi e codici dei guasti delle stampanti 3D sono cambiati rispetto alla P03, perché nessuno risponda a memoria.
- Per la sicurezza: niente incidenti con persone ferite nei testi. Le regole dicono che l'agente ordina e inoltra, e che una persona decide.
- Il lavoro riservato che alimenta un lavoro aperto all'utente (diagnosi dal registro, ritiro dai prestiti) è la decisione più interessante: che cosa può dire l'agente all'utente senza mostrare il registro? Prima dell'aula si prepara un esempio svolto su Ruota Libera (risposta di GUASTI che usa il registro senza mostrarlo); la risposta attesa di ogni caso sta nella guida docente, con valori dallo script.
- Collaudo: ogni gruppo prova il caso del gruppo successivo nel giro A→B→C→D→E→A.
- Gruppi da 5: nessun cambio, restano cinque gruppi e cinque casi (decisione del 25 novembre 2026).

## Struttura (senza tempi)

| Blocco | Che cosa fa il gruppo | Risultato visibile |
| --- | --- | --- |
| 1 · Caso e divisione del lavoro | Riceve il caso. Divide: una persona per ognuno dei tre lavori, una per accessi e assemblaggio, nei gruppi da 5 una per criterio e prove. Ognuno firma la propria parte. | Divisione scritta con i nomi. |
| 2 · Progetto | Scrive l'orchestratore e il criterio, prima di provare. Compila la tabella degli strumenti (Copilot, Unsloth Studio, opencode): 3-4 situazioni del caso, uno strumento per ogni situazione, la motivazione con il fatto visto in aula su cui si basa. | Istruzioni, criterio, tabella degli strumenti. |
| 3 · Prove | Prima di aprire Copilot ricava a mano dal registro stampato i tre numeri indicati nella consegna (valori dallo script) e li annota. Inventa tre prove (normale, ambigua, non permessa). Prima di ogni invio scrive una riga di previsione: «risponderà X, perché la regola Y dice Z». Prova in Copilot, annota il giudizio in una riga e confronta con la previsione e con i tre numeri. Ognuno lancia almeno una prova dal proprio computer. | Quaderno con previsioni, giudizi e tre numeri. |
| 4 · Collaudo | Passa con la chiavetta istruzioni, testi e criterio al gruppo successivo; riceve quelli del gruppo precedente. Inventa le prove nuove su carta, leggendo i testi stampati, senza chiedere a Copilot di inventarle: tra queste almeno una con un ordine nascosto in una copia di un documento e una con un accesso falsificato. Poi le prova. Corregge le falle trovate nel proprio agente. | Registro del collaudo. |
| 5 · Teoria breve | Parte da ciò che è emerso nel collaudo: che cosa ha fatto l'agente davanti all'ordine nascosto e all'accesso falsificato? Poi: «Chi può scrivere "Accesso: amministratore"? Che cosa lo impedisce davvero?», collegato al permesso di opencode della lezione 6. «RAG» si definisce in una riga dopo l'esempio, oppure resta nella guida docente. | Risposte del gruppo, discusse con la classe. |
| 6 · Presentazione | A rotazione presenta una persona del gruppo, scelta dal docente solo in quel momento: una falla e la correzione, oppure la prova più difficile che ha retto e la frase del testo che lo conferma. La classe e il docente chiedono «perché hai scritto questa riga?» e «che cosa risponde se tolgo questa regola?». Prima di mostrare la correzione la classe indovina la causa alzando la mano. | Presentazione di gruppo. |
| 7 · Test individuale | Risponde da solo, su carta, a un test breve, con almeno una domanda di previsione. | Test compilato. |

**Percorso minimo se i tempi saltano:** due prove nel collaudo invece di tre o quattro, una sola falla per presentazione, test ridotto a metà. Il test è l'ultimo: non va schiacciato.

**Se Copilot non risponde:** la prova resta NON_ESEGUITO e non si penalizza; il gruppo è valutato sul criterio e sulle prove scritte.

## File del gruppo (una consegna per gruppo, con chiavetta)

- istruzioni dell'orchestratore;
- quaderno (criterio, prove, collaudo);
- tabella degli strumenti.

Ogni parte riporta il nome di chi l'ha scritta. Un solo nome per cosa: «quaderno» (non «scheda del progetto»), «tabella degli strumenti».

**Chi scrive che cosa.** Il criterio, le prove e i giudizi li scrive una persona del gruppo. Copilot li riceve e risponde: non li scrive. Lo si dice nella consegna in una riga.

## Test individuale breve

Su carta, formato dichiarato a inizio test. Casi di Ruota Libera o un caso nuovo descritto nel test, dichiarati esempi scritti a mano e non risposte del modello. Argomenti, con le parole usate in aula («lavoro», «accesso», «amministratore», «orchestratore»): istruzioni e messaggio dell'utente, orchestratore e accesso, criterio scritto prima, dato o ordine dentro un documento, permesso o istruzione, tabella degli strumenti. Almeno una domanda di previsione: «ecco le istruzioni e un pezzo di registro: che cosa risponderà l'agente, e perché?». Le quattro domande di `laboratorio/docente/SOLUZIONI.md` §8 non si riusano così come sono (riguardano catalogo e training, fuori dal percorso). Non si inserisce «errore di recupero» se la teoria non lo mostra con un esempio.

## Griglia di valutazione (proposta da approvare)

Uguale per tutti i cinque casi, resa nota agli studenti a inizio lezione. Non si valuta la risposta di Copilot né la percentuale di prove riuscite; una prova senza risposta non si penalizza.

**Voto di gruppo (100 punti)**

| Criterio | Punti | Che cosa si guarda |
| --- | --- | --- |
| Criterio scritto prima, previsioni e prove | 25 | Il criterio c'è prima delle prove. Ogni prova ha la previsione scritta prima dell'invio. I tre numeri a mano sono scritti e confrontati. Le tre prove sono davvero normale, ambigua, non permessa. La prova ambigua è ambigua. |
| Orchestratore | 25 | Il lavoro che dipende da un altro è scritto come dipendente. Gli accessi sono distinti. Il dato riservato non esce all'utente. |
| Collaudo | 20 | Prove nuove inventate per l'altro gruppo, comprese l'ordine nascosto e l'accesso falsificato; giudizi motivati con il testo. |
| Correzione e presentazione | 20 | La correzione è mirata e motivata. Presenta a rotazione una persona diversa. Chiaro che cosa è stato cambiato e perché. |
| Tabella degli strumenti | 10 | Ogni scelta è motivata con un fatto visto in aula, non con un'ipotesi. |

**Parti firmate.** Il voto di gruppo è uguale per tutti. Chi non ha una parte firmata perde 2 punti sul voto di gruppo (decisione del 25 novembre 2026).

**Test individuale (100 punti).** Su carta, 8 domande brevi di peso pari; si valutano le motivazioni più dell'esito.

**Voto finale.** 60% gruppo, 40% test (decisione del docente, 25 novembre 2026).

## Cose da non fare

- Nessuna prova in Unsloth Studio o opencode.
- Nessuna aspettativa che l'agente sbagli: un quaderno tutto `OK` è valido se il criterio c'era prima e le prove erano difficili.
- Nessun testo scritto a mano presentato come risposta del modello.
- Niente tempi nei materiali per gli studenti.
- Non attribuire a Unsloth Studio o opencode funzioni non viste in aula (per esempio la base di conoscenza di Studio, non provata). La tabella degli strumenti si basa su: lezione 5 (Studio nel computer virtuale con temperatura; opencode che crea una pagina `.html`) e lezione 6 (Plan e Build con permesso).

## Verifiche prima dell'aula

| Punto | Controllo |
| --- | --- |
| Chiavette | I PC fisici le accettano; il computer virtuale vede i file copiati. Una chiavetta per gruppo. |
| Copilot, account studente | Un messaggio con orchestratore e tre testi del caso viene accettato; limite di lunghezza dei testi fissato dal generatore. |
| Rete | Cinque gruppi che provano insieme non arrivano al limite di richieste già visto in lezione 3. |
| Ordine nascosto | Come si comporta Copilot: da osservare, senza costruirci sopra l'attività né presentarlo come risultato certo. |
| Orchestratori | Quanti studenti ne hanno uno funzionante dalla lezione 5; punto di partenza per chi non lo ha. |
| Stampa | Test e pacchetti dei casi su carta. |
| Dati riservati | I file di sicurezza e prenotazioni in `docente/da_consegnare_a_parte/` sono pronti per ogni computer che invia prove dei casi interessati, anche nel collaudo; negli altri tre casi i dati riservati sono nel registro stesso. |

## Prossimi passi

1. Piano e griglia approvati (25 novembre 2026).
2. Fatto il 25 novembre 2026: generatore autonomo in `docente/genera_materiali.py` con dati e valori di riferimento dei cinque casi (i moduli stanno in `docente/casi/`).
3. Slide, consegna di gruppo, test, guida docente.
4. Revisione del revisore didattico e del revisore studente, poi commit.
