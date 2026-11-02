# Lezione 3 — L'assistente di reparto della P03

**ITS MAKER Bologna · 4 novembre 2026 · Microsoft Copilot Basic**

## Che cosa costruite

In questa attività, **assistente di reparto** significa Microsoft Copilot con le istruzioni che progettate voi. Aiuta un collega a leggere i documenti della P03 e a verificare una richiesta di ricambi. Non è un nuovo programma da installare.

L'assistente prepara risposte e tabelle da controllare: non ordina materiale, non modifica il magazzino e non autorizza interventi sulle macchine. I dati di magazzino descrivono il **19 ottobre 2026**, non il giorno della lezione.

## Che cosa aprire

1. In **Teams**, scaricate `ATTIVITA_LEZIONE3.docx` e `01_DOCUMENTI_P03.txt`.
2. Aprite questa scheda in **Word o LibreOffice Writer**: scriverete qui le decisioni e i controlli. Il PDF serve per leggere o stampare la stessa scheda.
3. Aprite `01_DOCUMENTI_P03.txt` con un programma di testo, per esempio **Blocco note**. Contiene diario, catalogo e magazzino. Il `.txt` è un file di testo semplice. Se il docente indica la versione Word o PDF, usate quella: non servono più copie dello stesso documento in Copilot.
4. Aprite **Microsoft Copilot** con l'account scolastico. Recuperate il testo delle istruzioni P03 salvato nella lezione precedente.

Una persona usa il computer; l'altra legge i documenti e annota i controlli. Scambiate i compiti nella progettazione e nelle prove.

## 1. Decidete a chi serve l'assistente

Scegliete un collega del reparto che potrebbe usarlo. Decidete quali domande deve poter fare e quali decisioni resteranno alla persona.

| Progetto della coppia | Da compilare |
| --- | --- |
| Nomi dei componenti | |
| Chi userà l'assistente? | |
| Che cosa deve poter ottenere? | |
| Che cosa l'assistente non deve fare? | |
| Come rendere la risposta facile da controllare? | |

<!-- pagebreak -->

## 2. Leggete e controllate i documenti

Leggete diario, catalogo e magazzino. Scegliete un fatto e trovate il passaggio che lo documenta, prima di chiedere aiuto a Copilot.

Se il docente indica **Copilot Blocchi appunti**, apritelo ora e aggiungete `01_DOCUMENTI_P03.txt`. Scrivete domande vostre e confrontate le risposte con i documenti. Altrimenti fate il controllo leggendo direttamente i testi. Non ricompilate il registro dei 24 appunti: usatelo per controllare le nuove risposte.

Completate la prima colonna con data e revisione, quando presente.

| Documento, data e revisione | Fatto controllato e passaggio che lo documenta | Che cosa non permette di affermare |
| --- | --- | --- |
| Diario P03 | | |
| Catalogo ricambi | | |
| Magazzino | | |

### Annotate subito il controllo svolto

Se avete usato i Blocchi appunti, riportate una richiesta realmente inviata e un breve pezzo della risposta ricevuta. Se avete svolto soltanto lettura diretta, descrivete quel controllo: non inventate una risposta di Copilot.

| Controllo sui documenti | Da compilare |
| --- | --- |
| Come abbiamo lavorato: Blocchi appunti o lettura diretta | |
| Richiesta inviata o controllo svolto | |
| Parte della risposta ricevuta, se presente | |
| Passaggio originale usato per controllare | |
| La risposta è corretta? Perché? Che cosa non dimostra? | |

## 3. Scrivete le vostre istruzioni

In questo lavoro ci sono tre testi diversi:

- **Istruzioni:** le regole di comportamento che scrivete per l'assistente.
- **Documenti:** i fatti del caso da consultare, non da cambiare.
- **Richiesta di prova:** la domanda di un collega che inventate per vedere come risponde l'assistente.

Rileggete le istruzioni della lezione precedente e decidete che cosa serve ancora. Se non avete il vecchio file, partite dal progetto della vostra coppia.

| Decisione sulle istruzioni | Regola scelta e motivo |
| --- | --- |
| Una regola che conserviamo | |
| Una regola che cambiamo o eliminiamo | |
| Una regola nuova, se necessaria | |

Decidete quando la richiesta contiene già tutto ciò che serve e quando manca un'informazione che cambia la risposta. Una domanda di chiarimento deve essere utile, non obbligatoria in ogni conversazione.

Scrivete le istruzioni con parole vostre, senza farle preparare a Copilot. Salvatele in `istruzioni_assistente_P03.txt`. I dati del caso rimangono nei documenti: non vanno ricopiati tutti nelle istruzioni.

Se usate un agente, aggiornate il suo campo **Istruzioni**. Se il docente indica una normale chat, inviate il vostro testo nel primo messaggio: sono istruzioni dell'utente, non un vero messaggio di sistema. In una nuova chat normale dovrete inviarle di nuovo.

<!-- pagebreak -->

## 4. Provate una richiesta e controllate il calcolo

1. Aprite una conversazione nuova con l'agente preparato. Se usate una normale chat, inviate prima le vostre istruzioni.
2. Allegate `01_DOCUMENTI_P03.txt`, o il formato indicato dal docente, con il pulsante per aggiungere file al messaggio. Se il docente vi fa usare il testo incollato, inviate la raccolta integrale, non un riassunto. I documenti non passano da soli dai Blocchi appunti all'agente.
3. Inventate una richiesta del collega che richieda almeno due documenti e un calcolo. La quantità richiesta la scegliete voi: è un'ipotesi, non un prelievo reale. La disponibilità, invece, deve essere ricavata dal documento, non inventata né suggerita nella domanda.
4. Prima di inviare la richiesta, annotate nella tabella quali dati usereste e quale risultato vi aspettate. Poi inviatela a Copilot.

Progettate le istruzioni perché Copilot esegua il calcolo con **Python**, un linguaggio di programmazione. Copilot lo usa in un ambiente separato, chiamato *sandbox*. Voi non dovete programmare: dovete controllare i numeri usati, l'operazione e il risultato.

Il docente vi mostra dove leggere i dettagli del calcolo nell'interfaccia. Controllate che Python sia stato eseguito: vedere soltanto codice scritto nel messaggio non basta. Se non riuscite a verificarlo, chiedete aiuto e annotatelo.

Fate produrre un file con la tabella dei risultati, scaricatelo e apritelo. Confrontate numeri e risultati con i documenti. Un file `.csv` contiene una tabella che si può aprire con **Excel o LibreOffice Calc**.

| Controllo della prova numerica | Da compilare |
| --- | --- |
| Richiesta scritta da noi | |
| Numeri scelti e documento da cui provengono | |
| Operazione e risultato attesi da noi | |
| Come abbiamo verificato l'esecuzione di Python e quale risultato abbiamo ricevuto | |
| Nome del file scaricato e controllo del suo contenuto | |
| Che cosa resta da decidere a una persona | |

<!-- pagebreak -->

## 5. Mettete alla prova l'assistente di un'altra coppia

Inventate una richiesta adatta all'assistente dei compagni. Prima di inviarla, compilate nella tabella qui sotto la richiesta, il risultato atteso e i documenti da controllare. Non inserite il risultato atteso nella domanda inviata a Copilot.

Potete verificare una risposta che usa più documenti, il confronto tra un evento e un documento successivo, una richiesta incompleta oppure un'informazione non presente nei testi. Non serve una frase ingannevole: serve un controllo utile. Scegliete una richiesta diversa da quella già usata dai compagni.

Per controllare le domande di chiarimento, potete togliere un'informazione davvero necessaria e poi fornirla: osservate se l'assistente sa chiedere ciò che manca e riprendere il lavoro.

1. La **coppia A** apre il proprio assistente in una conversazione nuova e fornisce di nuovo tutti i documenti. Se usa una chat normale, invia anche le proprie istruzioni iniziali.
2. La **coppia B** usa il computer della coppia A, senza cambiare account: invia la richiesta e completa la tabella nella scheda della coppia A. Una persona scrive, l'altra verifica i documenti. La coppia A osserva senza suggerire risposte.
3. Invertite A e B: ogni coppia deve provare l'assistente altrui e ricevere una prova sul proprio. Non scambiate credenziali e non modificate le istruzioni dei compagni.

| Prova dei compagni, da registrare nella scheda di chi ha creato l'assistente | Da compilare |
| --- | --- |
| Coppia che ha svolto la prova e compiti dei due studenti | |
| Richiesta realmente inviata | |
| Risultato atteso, scritto prima dell'invio | |
| Documenti da controllare e motivo della scelta | |
| Parte della risposta ricevuta | |
| Documento, passaggio e data controllati | |
| Numeri e calcolo controllati, se presenti | |
| La risposta è corretta? Perché? | |

<!-- pagebreak -->

## 6. Decidete se cambiare le istruzioni

Tornate al vostro assistente e scambiate i compiti nella coppia.

Se è emerso un problema, cercate che cosa è successo: un documento non usato, un numero scelto male, un'operazione diversa da quella richiesta o un risultato non controllato. Non date per scontato che ogni problema dipenda da una regola mancante.

Cambiate soltanto ciò che sapete spiegare. Se la risposta era già corretta, indicate quale regola ha funzionato e scegliete un altro tipo di richiesta da provare. Non è necessario trovare un errore.

Se cambiate una regola, deve servire anche ad altre richieste: non inserite nelle istruzioni la risposta alla singola prova. Per riprovare, ripetete i primi due passaggi della sezione 4: conversazione nuova, istruzioni se necessarie e documenti forniti di nuovo.

| Decisione della coppia che ha creato l'assistente | Da compilare |
| --- | --- |
| Che cosa conserviamo o cambiamo e perché | |
| Nuova richiesta di prova | |
| Documenti forniti nella nuova conversazione | |
| Risultato ricevuto e confronto con la prova precedente | |

## 7. Risposta individuale, senza Copilot

Ognuno risponde con parole proprie, usando una prova realmente svolta.

| Primo componente | Risposta |
| --- | --- |
| Nome | |
| Quale frase avete controllato? In quale documento e data trovate il riscontro? | |
| Quali numeri sono entrati nel calcolo? Che cosa resta da decidere a una persona? | |
| Quale regola avete conservato o cambiato, e perché? | |

| Secondo componente | Risposta |
| --- | --- |
| Nome | |
| Quale frase avete controllato? In quale documento e data trovate il riscontro? | |
| Quali numeri sono entrati nel calcolo? Che cosa resta da decidere a una persona? | |
| Quale regola avete conservato o cambiato, e perché? | |

## Che cosa consegnare su Teams

Nel punto indicato dal docente, caricate:

- questa scheda compilata, con le prove e le due risposte individuali;
- `istruzioni_assistente_P03.txt`, nella versione finale;
- il file con la tabella dei risultati prodotta da Python e controllata da voi.

Indicate se ogni passaggio è stato eseguito da voi, osservato nella dimostrazione del docente o soltanto controllato sui documenti. Un risultato atteso non è una vera esecuzione di Copilot.
