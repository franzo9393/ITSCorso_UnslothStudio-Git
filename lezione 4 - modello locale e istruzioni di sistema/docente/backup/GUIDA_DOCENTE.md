# Guida docente · Lezione 4

**ITS MAKER Bologna · Lezione 4 · 12 novembre 2026 · Unsloth Studio nella macchina virtuale**

Documento riservato al docente.

## Che cosa si fa

Il caso è la P03 della lezione 3, con un cambio: il modello non è più un servizio esterno ma gira nella macchina virtuale (VM) di ogni studente. Il filo della lezione è l'assistente di reparto che «non fa uscire i registri».

| Parte | Dove | Che cosa fanno gli studenti | Consegna |
| --- | --- | --- | --- |
| 1. Installare | VM, PowerShell | Eseguono l'installer di Unsloth Studio | |
| 2A. Parola successiva | Computer reale, browser | Prevedono e poi osservano l'effetto della temperatura in Transformer Explainer | `misure_VM.txt`: previsioni |
| 2B. Token | Computer reale, browser | Contano i token del registro e di una versione più breve scritta da loro, e si scambiano le versioni brevi | `misure_VM.txt`: token |
| 3A. Primo avvio | VM, Studio | Password, memoria prima del caricamento, estrazione dello zip o scarico, Search e Tools disattivati | `misure_VM.txt`: misure |
| 3B. Memoria e tempi | VM, Studio, Gestione attività | Confrontano la stima di Studio con la memoria misurata, con Context Length su Auto e su 8192; secondi, tok/s e token con testo breve e con il registro intero | `misure_VM.txt`: misure, spiegazione |
| 3C. Parametri | VM, Studio | In coppia: criteri insieme, impostazioni divise (uno Temperature, l'altro Top P oppure Top K, a scelta), scelta insieme | `misure_VM.txt`: criteri, scelta |
| 4A. Istruzioni | VM, Studio | Scrivono le istruzioni e le incollano in System Prompt | `istruzioni_assistente_P03.txt` |
| 4B. Prova del compagno | VM, Studio | Inventano casi e tranelli per l'assistente del compagno | `casi_di_prova.txt` |
| 4C. Correzione | VM, Studio | Correggono le istruzioni dove emergono falle | `istruzioni_assistente_P03.txt` |

L'installazione e il caricamento del modello dipendono dalla rete e non si possono accorciare in aula. Per questo la parte 2 si fa mentre l'installazione procede: le due cose avvengono in luoghi diversi (VM e computer reale).

**Se l'installazione è lenta** (decisione del 5 novembre 2026). Una sola regola, in due passi:

1. Alla fine della parte 2 l'installazione non è finita su una VM: ognuno scrive il proprio `istruzioni_assistente_P03.txt` (4A, punto 1) in Blocco note, senza Studio. Fai vedere le slide 15–16, che spiegano il System Prompt: se l'anticipo riguarda solo alcune coppie, mostrale a quelle coppie dal tuo portatile o rimandale alla parte 4A della consegna; proiettale per tutti solo se riguarda la maggior parte della classe. La regola dell'esempio dopo il tentativo non cambia; le prove restano in Studio.
2. Finita la scrittura anticipata: le coppie con almeno una VM con Studio aperto proseguono (a turno, se ne funziona una sola); le coppie senza Studio passano al ramo di riserva («Se Studio non parte»). Se più di metà della classe è senza Studio, il ramo vale per tutti. Questa è l'unica soglia: le altre sezioni la richiamano.

Tutti e tre i file `.txt` si scrivono con Blocco note dentro la VM, che si può usare anche durante la parte 2. Ogni studente consegna i propri tre file.

## Prima di giovedì 12 novembre

### Da preparare a casa

1. **Modello già pronto.** Il modello pesa circa 2 GB e la rete della scuola è la stessa per tutti: se lo scaricano tutti insieme, il rischio è quello visto con Copilot nella lezione 3. Scaricalo tu una volta sola, con Studio, sul tuo portatile (Select model → `unsloth/Qwen3.5-2B-GGUF` → `UD-Q4_K_XL`) e prepara lo zip come nella sezione «Copia del modello». Porta **più chiavette, una ogni 4–5 studenti**: lo zip è di circa 1,9 GB. **Come entra nella VM** (da scegliere e provare, nulla è stato provato su VMware): con VMware Workstation la chiavetta si può collegare direttamente alla VM (menu VM, Removable Devices, la chiavetta, Connect), oppure lo zip si copia sul computer reale e si trascina nella finestra della VM. Mostra la via scelta alla classe nella parte 1. Le chiavette girano durante la parte 1 e la parte 2: ognuno copia lo zip sul Desktop della VM subito dopo aver avviato l'installazione e restituisce la chiavetta senza aspettare l'estrazione; l'estrazione in `hub` avviene in 3A. Se nessuna via funziona, lo scarico dalla rete va fatto solo su alcune VM e le coppie lavorano a turno su quelle: non su tutte insieme. Con l'estrazione di Windows («Estrai tutto») compare una sottocartella con il nome dello zip: va tolta, perché Studio potrebbe non trovare il modello (non provato).
2. **Pubblica su Teams prima della lezione** `studenti/ATTIVITA_LEZIONE4.docx` e `Registro_P03_13-15_ottobre_2026.txt` (cartella `studenti/`), e crea il compito per i tre file `.txt`. Gli studenti scaricano il registro sul computer reale e, aprendo Teams nel browser della VM, anche nella VM; consegnano da Teams.
3. **Esempio di istruzioni.** `studenti/da_pubblicare_dopo_parte_4C/ESEMPIO_ISTRUZIONI_ASSISTENTE_P03.txt` non si pubblica prima: solo dopo la parte 4C.
4. **Windows nella VM.** Verifica che dalla VM si raggiunga internet e Teams, con l'account studente e l'eventuale verifica in due passaggi. Il copia e incolla tra computer reale e VM (VMware: appunti condivisi, trascinamento, cartella condivisa o USB) è una comodità, tranne per lo zip del modello (punto 1). Se non funziona, gli studenti scrivono a mano il comando di installazione dalla slide 5, controllandolo lettera per lettera; scaricano il registro da Teams nella VM e consegnano da lì; il testo delle istruzioni da mandare al compagno lo scrivono in un messaggio su Teams.

### Controlli prima dell'aula

Non è stato possibile provare nulla sulle VM della scuola né dalla rete della scuola. La colonna «Esito» resta da compilare in aula o prima, sulla prima VM disponibile.

| Controllo | Che cosa verificare | Esito |
| --- | --- | --- |
| Installer su Windows | Il comando della slide 5 (con `$env:UNSLOTH_NO_TORCH=1`) termina senza errori su una VM Windows con 8 GB di RAM; se fallisce, provare la forma normale, senza quella parte. Leggere in Gestione attività, scheda Rete, quanti dati scarica l'installer e moltiplicare per il numero di VM | |
| Permessi | L'installazione funziona con l'utente degli studenti, senza amministratore | |
| Spazio su disco | Almeno 8 GB liberi nella VM: l'installazione occupa circa 2,3 GB, il modello circa 2 GB (Studio segnala poco spazio libero) | |
| Primo avvio | Dopo l'installazione compare la domanda se avviare Studio; `http://127.0.0.1:8888` apre la pagina di creazione della password. Chiusa la finestra, in una nuova PowerShell `unsloth studio -p 8888` riavvia Studio e chiede la password | |
| Modello | `unsloth/Qwen3.5-2B-GGUF`, versione `UD-Q4_K_XL`: il modello si carica con 8 GB di RAM e risponde in italiano | |
| Memoria e contesto | Con Context Length su Auto e poi su 8192 (Reload model): memoria in uso nella VM e tempo con il registro intero; la VM resta utilizzabile. Lo script `docente/prova_vm/misura_vm.py` misura memoria e tempi senza interfaccia, ma richiede Python e il corpus del laboratorio e non è stato provato su Windows | |
| Search e Tools | Attivi di partenza; dopo il clic diventano grigi anche nella versione scaricata dall'installer di Windows | |
| Copia del modello | Lo zip estratto in `%USERPROFILE%\.cache\huggingface\hub` (cartella creata da Esplora file se manca) viene riconosciuto da Studio: compare in On Device, `UD-Q4_K_XL`, e si carica | |
| Memoria dell'host | Con la VM da 8 GB accesa e due schede del browser aperte sul computer reale (Transformer Explainer) la memoria del PC reale regge | |
| Rete | Transformer Explainer e Tokenizer Playground si aprono dalla rete della scuola, con tutte le postazioni accese insieme; leggere quanti dati scarica Transformer Explainer per caricare il modello nel browser. Per decidere vale la regola di «Se l'installazione è lenta» | |
| Passaggio dei file | Teams si apre nel browser della VM; il testo di `istruzioni_assistente_P03.txt` si manda al compagno con un messaggio su Teams; i tre file si caricano dal browser della VM, o si copiano sul computer reale | |
| Zip del modello | Lo zip passa dalla chiavetta alla VM (collegamento USB di VMware o trascinamento) e si estrae in `%USERPROFILE%\.cache\huggingface\hub`; misurare tempo di copia ed estrazione | |
| Context Length | Ordine del controllo: prima «si può impostare prima del caricamento?» (prova senza rischio), poi «la stima di Studio cambia senza Reload?», poi «Studio ricorda l'ultimo valore dopo la riapertura?», per ultimo il caricamento con Auto, che può bloccare la VM: «Studio riduce da solo il contesto alla memoria libera?» (lo fa pensare `--fit on` tra i parametri del motore su Linux, ma non è stato visto con poca RAM). Tre esiti per la classe: (a) si può impostare prima: dì di caricare subito con 8192 e di scrivere nella prima riga della tabella di 3B (Context Length su Auto) solo la stima di Studio; (b) non si può impostare prima ma Auto regge: si segue la consegna; (c) Auto blocca e il valore non si può impostare prima né resta: quella VM non carica il modello, la coppia lavora a turno sull'altra VM e, se il blocco c'è su entrambe, passa al ramo di riserva. Chi ha il blocco scrive «bloccato» nella prima riga della tabella di 3B, al posto della stima e della memoria | |
| Copilot | Con l'account studente accetta in un solo messaggio le istruzioni e il registro intero (circa 10.600 caratteri): serve al ramo di riserva della parte 4. Nella lezione 2 il registro si incollava in quattro parti | |
| System Prompt e regolazioni | Aprendo una nuova conversazione, System Prompt, Temperature, Top P e Top K restano quelli impostati, con il modello caricato e dopo almeno una risposta. Su Linux il System Prompt è rimasto dopo «New chat» (senza modello caricato) e dopo Reload model (con modello caricato); Temperature, Top P e Top K non sono stati verificati. In 4B e 4C gli studenti alternano comunque le istruzioni del compagno e le proprie: le consegne chiedono di controllare Run settings prima di provare | |
| Teams nella VM | Accesso con l'account studente, anche con la verifica in due passaggi; caricamento dei tre file | |

## Che cosa è stato provato

Provato il 5 novembre 2026 sul portatile del docente, **Linux**, versione di Unsloth Studio 2026.11.2. Non è Windows, non è la VM, non è la rete della scuola.

- **Installazione.** `install.sh` con `UNSLOTH_NO_TORCH=1` (modalità senza PyTorch, solo GGUF) termina senza errori. Circa 2,3 GB su disco, circa 15 minuti con una connessione domestica; il tempo è dominato dalla rete, non dal processore.
- **Primo avvio.** `unsloth studio -p <porta>` parte; la pagina chiede di creare una password di almeno 8 caratteri.
- **Interfaccia.** Casella **Select model**; ricerca per indirizzo; elenco delle versioni (`UD-Q4_K_XL` indicata come consigliata); scheda **On Device**; pannello **Run settings** con **Estimated Memory Usage**, **Context Length**, **System Prompt**, **Temperature** (0,6 di partenza), **Top P** (0,95), **Top K** (20). Nella casella dei messaggi **Search** e **Tools** sono **attivi di partenza** (verdi) e si disattivano con un clic (grigi); la scelta resta anche dopo il riavvio.
- **Download.** `unsloth/Qwen3.5-2B-GGUF`, `UD-Q4_K_XL`: Studio indica **2,0 GB** (il modello da 1,3 GB e il file per le immagini). Con il download predefinito la barra è rimasta ferma a lungo e il registro del programma segnalava «connection struggling»; con `HF_HUB_DISABLE_XET=1` è partito, a circa 1,1–1,8 MB/s su quella rete.
- **Cartella del modello copiata.** Una copia della cartella del modello, senza i collegamenti simbolici e senza `blobs`, messa nella cartella `hub`, viene riconosciuta da Studio (scheda On Device, `UD-Q4_K_XL`, 1,3 GB) e il modello si carica.
- **Risposte, solo CPU** (scheda grafica nascosta con `CUDA_VISIBLE_DEVICES=-1`; `UNSLOTH_CPU_THREADS=4` impostato, ma non verificato che limiti anche il motore del modello; 15,6 GB di RAM nel portatile): registro intero (circa 3,2k token mostrati da Studio) più una domanda, circa 25 secondi **in totale**, dall'invio alla fine della risposta (di una riga), 15–16 tok/s. **Il tempo alla prima parola non è stato misurato.** Con **Context Length** su Auto il processo del modello occupava circa 5,4 GB, con 8192 circa 2,5 GB; **Estimated Memory Usage** indicava 6,49 GiB contro 3,34 GiB. Con la scheda grafica: circa 10 secondi in totale, 61 tok/s.
- **Istruzioni di sistema.** Il modello risponde in italiano. Con la prima versione dell'esempio (prosa lunga) non ha mai fatto una domanda di chiarimento e ha ripetuto «Dato non presente nel registro» anche a domande con risposta nel registro. Con la versione a regole numerate ora in `ESEMPIO_ISTRUZIONI_ASSISTENTE_P03.txt`, alla domanda «Qual era la temperatura dell'olio?» ha risposto «A quale giorno e ora ti riferisci?». Provato un solo caso, un solo tentativo: le regole 1–3 non sono verificate oltre questo; la regola 4 non è provata.
- **Persistenza.** Il campo System Prompt non si è svuotato aprendo una nuova chat né dopo Reload model (5 novembre 2026, versione 2026.11.2, Linux). La nuova chat è stata provata senza modello caricato.

**Non provato:** l'installer `install.ps1` su Windows; Windows nella VM con 8 GB di RAM; i permessi degli studenti; la rete della scuola; il tempo di installazione con più postazioni insieme; il comportamento della memoria quando la VM ha meno RAM libera di quella richiesta (Studio dovrebbe ridurre il contesto da solo con Auto, ma non è stato visto); i tempi con i processori della VM.

## Copia del modello

Preparazione sul tuo portatile (Linux), dopo aver scaricato il modello con Studio:

```
mkdir -p ~/modello_per_VM
cp -rL ~/.cache/huggingface/hub/models--unsloth--Qwen3.5-2B-GGUF ~/modello_per_VM/
rm -rf ~/modello_per_VM/models--unsloth--Qwen3.5-2B-GGUF/blobs ~/modello_per_VM/models--unsloth--Qwen3.5-2B-GGUF/.transport*
cd ~/modello_per_VM && zip -0 -r modello_Qwen3.5-2B.zip models--unsloth--Qwen3.5-2B-GGUF
```

`cp -rL` copia i file veri al posto dei collegamenti simbolici, che Windows non gestisce. Nella VM lo zip va estratto in `%USERPROFILE%\.cache\huggingface\hub` (barra dell'indirizzo di Esplora file), in modo che dentro `hub` ci sia la cartella `models--unsloth--Qwen3.5-2B-GGUF`; se `.cache`, `huggingface` o `hub` non esistono, si creano uno alla volta. Il file è di circa 1,9 GB. L'estrazione su Windows non è stata provata.

## Svolgimento

### Parte 1 · Installazione

All'ingresso fai accendere la VM e accedere a Windows, prima delle slide 1–3. Poi fai partire tutti insieme: PowerShell, incolla, Invio. Passa tra i banchi per le prime schermate: è qui che compaiono i problemi. Chi vede un errore in rosso ti chiama senza chiudere la finestra.

**Controllo di Context Length, durante la parte 2.** Avvia l'installazione anche sulla tua postazione di prova, oppure segui la prima VM che la finisce. Fai il controllo della riga «Context Length» dei controlli prima dell'aula, nell'ordine indicato lì, e comunica la decisione alla classe prima che arrivi a 3A, punto 5: le consegne fanno aspettare la tua indicazione prima di cliccare Select model. **Finché il controllo non è finito** dì: «caricate con Auto tenendo aperta Gestione attività; se la memoria arriva quasi al massimo chiudete PowerShell come in 3A e scrivete "bloccato" nella prima riga della tabella di 3B».

Dopo un blocco, chi lo ha avuto non clicca di nuovo Select model finché non lo decidi tu (la consegna lo dice). Con l'esito (a): Context Length a 8192 prima di Select model, anche nella riapertura di Studio. Con l'esito (c): nessun nuovo caricamento su quella VM; la coppia lavora sulla VM del compagno.

Se il comando con `$env:UNSLOTH_NO_TORCH=1;` non funziona, prova la forma normale, `irm https://unsloth.ai/install.ps1 | iex`: scarica anche PyTorch ed è molto più pesante.

Il modello arriva dallo zip; il download dalla rete si fa solo su alcune VM e non su tutte insieme (vedi «Da preparare a casa»). La consegna e la slide 11 dicono agli studenti senza zip di aspettarti. Il file è lo stesso per tutti.

### Parte 2 · Browser del computer reale

Qui la classe lavora mentre l'installazione procede. Non spiegare prima: lascia che prevedano e poi guardino.

- **Transformer Explainer.** Domande utili: che cosa succede alla barra più lunga quando la temperatura sale? Perché a temperatura bassa il modello sceglie quasi sempre la stessa parola? È un modello molto piccolo, in inglese: non giudicare la qualità delle frasi.
- **Tokenizer Playground.** Il registro intero (24 note, circa 1.700 parole) è lungo: serve a far vedere che cosa pesa. Raccogli i numeri di token alla lavagna con il nome del tokenizzatore scelto: cambia il valore. Lo scambio delle versioni brevi fa vedere che cosa si perde quando si riscrive un testo.

### Parte 3 · Studio

- **Primo avvio.** La password serve ogni volta; i fogli con le password evitano blocchi più avanti. La memoria prima del caricamento si legge prima di scegliere il modello. Search e Tools sono attivi di partenza: chi non li disattiva può far partire una ricerca su internet o l'esecuzione di codice nella VM.
- **Misure.** Gli studenti confrontano tre cose: la stima di Studio (Estimated Memory Usage) con la memoria misurata in Gestione attività; la memoria con Context Length su Auto e con 8192; il numero di token del Tokenizer Playground con quello mostrato in alto da Studio. La memoria del modello è la memoria in uso dopo il caricamento meno quella misurata prima. La domanda breve e il registro intero mostrano l'effetto del testo lungo sul tempo. Se la VM ha poca RAM libera, con Auto Studio può scegliere un contesto grande (nel portatile 262.144 token, circa 5,4 GB): se la VM rallenta o si blocca, fai portare subito Context Length a 8192 e fai riaprire Studio come nella consegna. Il registro intero ne usa circa 3.200. Il cambio vale dopo **Reload model**: se non si ricarica al primo clic, si clicca ancora. Raccogli da tutte le coppie memoria a modello caricato, secondi e tok/s con il registro intero: servono per scegliere il modello delle lezioni 5–7.
- **Parametri.** In coppia: criteri e richiesta insieme, poi le prove divise per regolazione (uno Temperature, l'altro Top P oppure Top K, a scelta, ognuno nella propria VM), una nuova conversazione per ogni prova. I valori di partenza li prova chi segue la Temperature, controllando la risposta già ottenuta in 3B con i criteri della coppia e rifacendo la prova solo se la richiesta scritta in 3C è diversa; ognuno prova poi un valore basso e uno alto. Non cercare un valore «giusto»: un'impostazione con valori bassi e una con valori alti possono dare entrambe una risposta valida; conta come la giustificano. Se due impostazioni danno la stessa risposta, è un risultato. A parità di richiesta il modello può dare risposte diverse: chiedi di ripetere la prova solo alle coppie le cui due impostazioni hanno dato risposte diverse. Valori di partenza visti su Linux: Temperature 0,6, Top P 0,95, Top K 20; su Windows da verificare.
- **Se le risposte sono lente** (decisione del 5 novembre 2026). Una regola legata a un evento, non a una durata. Il riferimento su Linux è di circa 25 secondi in totale; gli studenti misurano invece i secondi fino alla prima parola, che su Linux non è stato misurato e non è confrontabile con il totale. Poiché la prima parola arriva prima della fine della risposta, vale solo un confronto in un senso: se i secondi alla prima parola scritti dagli studenti in 3B superano già i 25 secondi, la VM è più lenta del portatile. In quel caso, in 3C ognuno prova **un solo** valore della propria regolazione (il basso o l'alto, a scelta) invece di due; i valori di partenza restano quelli di 3B. Con valori vicini o minori di 25 secondi la regola non scatta, anche se il totale potrebbe essere più lungo: usa il giudizio sui tok/s e sull'attesa in aula. Dillo a voce alla classe prima di 3C e controlla che in «Scelta» compaia una riga per prova. Le prove di 4B e 4C non cambiano. I dati sulla velocità raccolti in 3B servono comunque per le lezioni 5–7.

### Parte 4 · Istruzioni

- Gli studenti scrivono le istruzioni senza esempio. Se chiedono «come si scrive?», rimanda alle quattro voci della consegna.
- La prova del compagno richiede il passaggio del testo delle istruzioni, con un messaggio su Teams: verifica che funzioni per tutte le coppie. Ogni prova è una nuova conversazione con registro e domanda in un solo messaggio; in 4C gli studenti rimettono nel System Prompt le proprie istruzioni prima di riprovare.
- Casi che sanno inventare: dato assente nel registro, domanda senza giorno, due note che danno valori diversi, richiesta di un'azione sulla macchina, domanda fuori dal registro. Non suggerirli: li devono trovare loro.
- **Esempio di istruzioni.** Dopo la parte 4C pubblica `ESEMPIO_ISTRUZIONI_ASSISTENTE_P03.txt` e chiedi di confrontarlo con le proprie: che cosa manca? Che cosa è inutile? Quale regola ha cambiato il comportamento? Non presentarlo come soluzione: è provato su un solo caso. Se la classe vede un comportamento diverso dal tuo, è un dato valido e va discusso.

### Chiusura

Ordine: fai consegnare i tre file; poi pubblica l'esempio di istruzioni e fai il confronto con le istruzioni degli studenti; poi le tre domande della slide 22. In questo modo l'esempio non può cambiare i file consegnati. Risposte attese, dai valori misurati in aula: (1) la memoria dipende dal modello e da Context Length, che si fissa al caricamento; il testo lungo aumenta i token e i secondi di attesa. Con l'esito (b) si confrontano le misure con Auto e con 8192, con l'esito (a) le stime di Studio, con l'esito (c) il blocco è il dato; (2) con la temperatura alta il modello sceglie più spesso parole meno probabili e le risposte variano di più; se i dati restano giusti lo dice il controllo con i criteri, non il valore della temperatura; (3) un caso di prova che ha fatto cambiare o confermare una regola delle proprie istruzioni, con il motivo. Se un valore misurato non coincide, è un dato da discutere.

## Valori di riferimento del registro

Ricavati dallo script del generatore dal testo di `Registro_P03_13-15_ottobre_2026.txt`.

{{VALORI_REGISTRO}}

Dati che il registro **non** contiene, utili per i tranelli: nome del tecnico, contatore del 15 ottobre, il motivo per cui il filtro si è intasato (il registro dice solo che era intasato), nome del responsabile del turno.

## Se Studio non parte

La regola per decidere è quella di «Se l'installazione è lenta» (sopra): evento e non tempo, in due passi. Se una sola VM della coppia funziona, la coppia lavora a turno su quella. Le alternative sono nella consegna degli studenti («Se Unsloth Studio non parte»).

| Attività | Con Studio | Senza Studio |
| --- | --- | --- |
| 2A Parola successiva | Transformer Explainer | Uguale |
| 3B Memoria | Misure nella VM | Calcolatore OCTOO nel browser del computer reale, con modello da 2 miliardi di parametri a 4 bit, contesto 8192 e massimo: stima per schede grafiche, non misura della VM |
| 3C Parametri | Prove divise in Studio | Si usano le distribuzioni di Transformer Explainer: la coppia scrive i criteri, sceglie una temperatura e la motiva; in «Scelta» segna che ha lavorato senza Studio |
| 4 Istruzioni | System Prompt di Studio | Le istruzioni si provano come primo messaggio in Copilot, con il registro sotto, scrivendo che non è il campo di sistema e che il registro esce dal reparto. Se Copilot non risponde o non accetta il messaggio, chi ha inventato i casi li pone e l'autore delle istruzioni risponde applicando alla lettera solo le regole che ha scritto, e lo scrive nei casi |

I file consegnati sono gli stessi: cambia la nota su come sono stati ottenuti.

## Problemi probabili

| Sintomo | Possibile causa | Che cosa fare |
| --- | --- | --- |
| Il comando di installazione dà errore subito | Criteri di esecuzione di PowerShell o rete | Copiare il messaggio e verificare con un'altra postazione; provare senza `$env:UNSLOTH_NO_TORCH=1;` |
| L'installazione non finisce | Rete saturata da tutte le postazioni | Proseguire con la parte 2; alla fine della parte 2 applicare la regola di «Se l'installazione è lenta» (scrittura anticipata, poi ramo di riserva) |
| Il download del modello resta a 0 % | Il metodo di download predefinito può bloccarsi su alcune reti | Chiudere Studio, in PowerShell scrivere `$env:HF_HUB_DISABLE_XET=1` e poi `unsloth studio -p 8888`; oppure usare la cartella del modello su chiavetta |
| «Disk space is running low» | VM con poco spazio | Verificare lo spazio libero prima di scaricare il modello |
| Il PC reale rallenta | 8 GB assegnati alla VM e il browser con Transformer Explainer | Chiudere altri programmi sul computer reale; una scheda per sito |
| La risposta non arriva | Modello troppo grande per la memoria, o testo lungo su CPU | Aspettare; con il registro intero la prima risposta può richiedere tempo, è un dato da misurare |
| La VM non risponde affatto | Memoria esaurita, per esempio con Context Length su Auto | Nella finestra di VMware Ctrl+Alt+Ins e Gestione attività, chiudere il processo di Studio; in ultima istanza menu VM, Power, Restart Guest; poi riaprire Studio come nella consegna |

## Dati da raccogliere per le lezioni 5–7

Prima di riprendere con la lezione 5 (18 novembre): quante VM hanno finito l'installazione, con quale metodo è arrivato il modello e quanto ha impiegato; memoria e secondi di risposta; quali istruzioni di sistema sono state seguite e quali ignorate dal modello da 2 miliardi di parametri; che cosa è passato dal campo System Prompt e che cosa no.
