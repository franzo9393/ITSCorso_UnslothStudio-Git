# Bozza del percorso · lezioni 4–7 con Unsloth Studio in locale

Documento riservato al docente. **Bozza da approvare**: non sono ancora materiali per gli studenti e nessuna attività è stata provata sulle VM della scuola. Le risorse vengono da `RICERCA_ATTIVITA_ONLINE.md`, dove sono indicati esiti della validazione, termini d'uso e fonti.

## Struttura

| Incontro | Data | Durata | Contenuto |
| --- | --- | --- | --- |
| Lezione 4 | 12 novembre 2026 | 2 ore | Modello locale e istruzioni di sistema |
| Lezione 5 | 18 novembre 2026 | 2 ore | Documenti e recupero (RAG) |
| Lezione 6 | 25 novembre 2026 | 2 ore | Agenti, permessi e difese |
| Lezione 7 | 2 dicembre 2026 | 4 ore | Lavoro di gruppo e test finale individuale |

## Vincoli

- **VM della scuola: al massimo 8 GB di RAM, nessuna GPU.** Unsloth Studio dichiara il funzionamento su sola CPU ([Chat](https://unsloth.ai/docs/new/studio/chat)); memoria e tempi sulla VM sono da misurare.
  - Un solo modello GGUF piccolo e quantizzato, caricato prima della lezione.
  - Niente Model Arena (carica due modelli), addestramento, esportazioni o conversioni.
  - RAG in modalità BM25, già indicata in `materiali_aula/RISORSE_E_ACCESSO.md` §3.1.
- **Siti esterni dal browser del PC fisico, solo quelli che elaborano nel browser** (decisione del 5 novembre 2026). Nella lezione 3 Copilot non ha risposto a nessuno per circa 10 minuti: ipotesi, limite di richieste dallo stesso indirizzo pubblico in uscita, non verificata. Restano nel percorso solo siti statici o che calcolano nel browser; sono esclusi HackMerlin, Prompt Airlines e Gandalf, che interrogano un modello sul server. Il controllo dei siti è nella tabella «Siti esterni» più sotto. Unsloth Studio gira nella VM e non usa la rete. Restano esclusi anche gli strumenti che richiedono WebGPU (WebLLM, Qwen3 Embedding Scatterplot) finché non si conoscono le schede grafiche dei PC fisici.
- **La VM non si può provare prima della lezione 4** (decisione del 5 novembre 2026). Il percorso ha un ramo di riserva: se Studio o il modello non partono, la lezione prosegue senza modello locale (vedi «Ramo di riserva» nella lezione 4). Le misure sulla VM sono un'attività in più, non il filo della lezione.
- **Lezione 3 svolta il 4 novembre 2026** (resoconto del docente del 5 novembre). Svolti: agenti con Python creati dagli studenti; Prova A e Prova B «più o meno»; confronto dell'output dell'agente con e senza la scheda di passaggio (`.handoff`), sul file `.xlsx`; limiti e potenzialità del RAG. Il blocco di Copilot ha rallentato i lavori, ma il materiale non copriva comunque le 2 ore: finito a 1 h 40 min. La stima del revisore (circa 141 minuti) era quindi troppo alta; per la lezione 4 si può progettare una lezione più piena. I materiali per gli studenti non citano tempi.
- Regole del progetto: gli studenti scrivono e correggono le proprie istruzioni; i casi di prova li inventano loro; nessuna attività si basa sull'errore atteso del modello; le istruzioni di esempio si pubblicano dopo il tentativo, in una cartella separata; nessun tempo di completamento nei materiali.

## Filo conduttore

Ogni studente costruisce sulla propria VM un **assistente di reparto per la P03**. Ogni lezione riusa i file prodotti nella precedente; nella lezione 7 il gruppo lo estende a un documento nuovo e lo fa collaudare da un altro gruppo.

```mermaid
flowchart LR
  L4["Lezione 4<br/>istruzioni di sistema"] -->|istruzioni_assistente_P03.txt| L5["Lezione 5<br/>knowledge base"]
  L5 -->|registro prove + istruzioni riviste| L6["Lezione 6<br/>permessi e difese"]
  L6 -->|tabella_permessi_P03.txt| L7["Lezione 7<br/>gruppi + test individuale"]
```

## Lezione 4 · Un modello che gira sul tuo computer

**Materiali pronti:** `Lezione4_Modello_locale_e_istruzioni_di_sistema_ITS_MAKER.pptx`, `studenti/ATTIVITA_LEZIONE4.docx`, `docente/GUIDA_DOCENTE.docx`. Fa fede la guida docente: questa sezione riassume le scelte.

Obiettivo: capire che cosa vuol dire usare un modello in locale e progettare istruzioni di sistema vere.

**Decisione del 5 novembre 2026: installazione in diretta.** Le VM degli studenti (8 GB di RAM, Windows 10 o 11, internet e permessi) non si possono preparare prima. Gli studenti installano Unsloth Studio con l'installer in modalità senza PyTorch (`UNSLOTH_NO_TORCH=1`, solo GGUF) e, mentre l'installazione procede nella VM, lavorano sul PC reale con i due siti statici. Il modello `unsloth/Qwen3.5-2B-GGUF` `UD-Q4_K_XL` pesa 2,0 GB per postazione: il docente lo scarica una volta e lo porta in uno zip, su più chiavette. **Se l'installazione è lenta** il docente anticipa la scrittura delle istruzioni (decisione del 5 novembre).

Parti, come nella consegna degli studenti:

1. **Installare Unsloth Studio** · PowerShell nella VM.
2. **Come risponde un modello** · [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (previsione sulla temperatura, poi osservazione) e [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) (token del registro e di una versione breve scritta dagli studenti, scambiata fra compagni), sul PC reale durante l'installazione.
3. **Il modello sul computer** · Unsloth Studio. Primo avvio; memoria prima del caricamento, con Context Length su Auto e su 8192 (stima di Studio contro misura in Gestione attività); secondi e tok/s con testo breve e con il registro; criteri e prove sui parametri (Temperature, Top P, Top K) divise fra i compagni.
4. **Le istruzioni dell'assistente** · casella System Prompt. Ogni studente scrive le istruzioni di un assistente che fa domande prima di rispondere quando mancano dati; il compagno inventa casi di prova e tranelli; ciascuno corregge o conferma le proprie istruzioni.

Consegne di ogni studente: `misure_VM.txt`, `istruzioni_assistente_P03.txt`, `casi_di_prova.txt`. Esempio di istruzioni in `studenti/da_pubblicare_dopo_parte_4C/`, da pubblicare dopo la parte 4C.

### Ramo di riserva della lezione 4

Segnale per decidere, un evento e non un tempo: l'installazione non è finita quando le coppie hanno terminato la parte 2. La regola in due passi (scrittura anticipata delle istruzioni, poi ramo di riserva per le coppie senza Studio) è nella guida docente («Se l'installazione è lenta»); il ramo, attività per attività, è nella guida («Se Studio non parte») e nella consegna degli studenti. Se una sola VM della coppia funziona, la coppia lavora a turno su quella.

## Lezione 5 · Il modello legge i documenti

Obiettivo: rendere visibile il recupero dei passaggi e distinguere un errore di recupero da un errore di risposta.

1. **Tagliare il testo in blocchi** · [ChunkViz](https://chunkviz.up.railway.app/). Le coppie fissano un criterio («macchina, orario, allarme e causa nello stesso blocco»), confrontano dimensioni, sovrapposizione e tipo di divisione, e motivano la scelta. Poi si confronta la scelta con la divisione fissa di Studio, che non si imposta da ChunkViz.
2. **Parole esatte o significato** · [Vector Search Methods Comparison](https://huggingface.co/spaces/arad1367/Vector_Search_Methods_Comparison), riquadro BM25. Breve illustrazione con esempi fissi, prima dei documenti veri.
3. **Knowledge base BM25** · Unsloth Studio, con il corpus del laboratorio (`laboratorio/corpus/`: P03, P30, catalogo ricambi, bolla). Gli studenti scrivono domande di tipi diversi (codice esatto, più fonti, dato assente, P03 o P30), guardano i passaggi recuperati, cambiano il numero di passaggi e correggono la domanda, il documento o le istruzioni della lezione 4.
4. **Documento aggiornato** · Unsloth Studio. Si sostituisce il catalogo con la revisione 2 e si ripete la prova in una nuova conversazione.

Consegna: registro delle prove (domanda, passaggi recuperati, risposta, giudizio, correzione) in tabella con celle vuote, con i giudizi `OK`, `ERRORE`, `NON_ESEGUITO` già usati in `laboratorio/docente/SOLUZIONI.md`.

## Lezione 6 · Agenti: strumenti, permessi e difese

Obiettivo: vedere che cosa fa un agente oltre a scrivere testo e dove si mettono le protezioni.

1. **Istruzioni nascoste** · attività da riprogettare senza server esterni. HackMerlin e Gandalf sono esclusi perché interrogano un modello sul server. Candidata: le coppie scrivono su carta le istruzioni di difesa per un assistente di reparto, le scambiano e provano ad aggirarle in Unsloth Studio (o con il ramo di riserva della lezione 4). Da approvare.
2. **Dentro un agente** · attività da riprogettare senza Prompt Airlines (server esterno). Candidata: la scheda ricavata da [Hugging Face Agents Course · Unità 1](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure) (Apache-2.0): una persona della coppia fa da programma di controllo, decide quando fermare il modello, quale funzione eseguire e quale risultato reinserire; l'altra fa da modello e risponde solo con il formato Pensiero–Azione–Osservazione. Si svolge sulla carta o in un file di testo, senza rete. Da approvare.
3. **Istruzioni dentro un documento** · Unsloth Studio. Ogni studente inserisce in un documento sintetico della knowledge base del compagno una nota che contiene un'istruzione. Il compagno controlla se il proprio assistente la tratta come dato o come ordine; entrambi gli esiti si analizzano e si decide che cosa protegge davvero: istruzioni, permessi o controllo umano.
4. **Tabella dei permessi** · Unsloth Studio, esecuzione di codice. Solo se il collaudo sulla VM riesce: la coppia decide che cosa l'assistente può fare da solo, che cosa deve chiedere e che cosa gli è vietato, poi prova un calcolo eseguito e lo confronta con un riepilogo calcolato con regole note. Senza collaudo positivo la tabella si progetta senza esecuzione.

Consegne: `tabella_permessi_P03.txt`, istruzioni riviste.

## Lezione 7 · Lavoro di gruppo e test individuale

Riprende il blocco «Sfida e restituzione» già progettato in `laboratorio/docente/SOLUZIONI.md` §8 (documento nuovo DOC-T10, domande T07–T09, verifica individuale), adattato al percorso delle lezioni 4–6.

### Prima parte · Lavoro di gruppo

- **Gruppi di quattro**, ognuno sulla propria VM. Il gruppo divide il lavoro per argomento: istruzioni di sistema, documenti, permessi, casi di prova.
- **Consegna del gruppo**: estendere l'assistente P03 a un **documento nuovo scritto dal gruppo** (DOC-T10: titolo, data, revisione, due dati sintetici con macchina e unità, un dato lasciato volutamente fuori dal documento). Il gruppo aggiorna istruzioni, knowledge base e tabella dei permessi.
- **Collaudo incrociato**: ogni gruppo prepara per un altro gruppo un pacchetto di tranelli inventati (dato assente, P03 o P30, revisione vecchia, istruzione nascosta in un documento, richiesta di azione non permessa). Il gruppo ospite, non l'autore, formula le domande sul DOC-T10, come previsto per T08/T09.
- **Correzione e restituzione**: ogni gruppo corregge dove il collaudo ha trovato falle e presenta alla classe una falla e la correzione, con i passaggi recuperati come prova. Non si valuta la percentuale di risposte corrette del modello.

Consegna del gruppo: istruzioni finali, DOC-T10, registro del collaudo incrociato, tabella dei permessi.

### Seconda parte · Test individuale

- **Parte scritta**, mista: domande aperte brevi e domande a scelta multipla con motivazione. Riguardano casi descritti dal docente, dichiarati come esempi scritti a mano e non come risposte reali del modello. Argomenti: locale o cloud e memoria, temperatura e token, messaggio di sistema e messaggio utente, blocchi e numero di passaggi, errore di recupero o di risposta, catalogo corrente o storico, dato o istruzione dentro un documento, che cosa deve essere un permesso e non un'istruzione. Le quattro domande della verifica individuale in `SOLUZIONI.md` §8 si riusano.
- **Parte pratica sulla propria VM**: un documento breve nuovo preparato dal docente e una richiesta. Lo studente decide le domande di controllo, registra passaggi recuperati, risposta e giudizio (`OK`, `ERRORE`, `NON_ESEGUITO`) e propone una correzione motivata.
- **Valutazione**: griglia e peso del lavoro di gruppo rispetto al test individuale da definire. La griglia di `SOLUZIONI.md` §8 è un punto di partenza, ma comprende anche il mini-dataset, che non è nel percorso.

## Da verificare prima delle lezioni

**Stato delle prove (5 novembre 2026):** Unsloth Studio e il modello `unsloth/Qwen3.5-2B-GGUF` sono stati provati sul portatile del docente, Linux, anche in sola CPU (dettagli nella guida della lezione 4). Restano da provare Windows, la VM da 8 GB e la rete della scuola; la knowledge base BM25, l'esecuzione di codice e i modelli più grandi non sono stati provati.

| Punto | Controllo |
| --- | --- |
| Modello | `unsloth/Qwen3.5-2B-GGUF` `UD-Q4_K_XL` scelto per la lezione 4: memoria e tempi nella VM con tutte le VM accese, capacità di seguire istruzioni in italiano. Per le lezioni 5–7 decidere in base alle misure raccolte il 12 novembre |
| Unsloth Studio | Versione installata, campo System Prompt, parametri, knowledge base, impostazioni di recupero, esecuzione di codice |
| Memoria | Studio e modello entro 8 GB durante indicizzazione e risposta |
| Corpus | Coerenza di `laboratorio/corpus/` con i dati P03 della lezione 3: stessa macchina, date compatibili, quantità che tornano |
| Siti esterni | Il controllo su pagina e codice, fatto il 5 novembre 2026, conferma che **elaborano nel browser, senza modello sul server**: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (GPT-2 nel browser, README), [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) (Space statico), [Vector Search Methods Comparison](https://huggingface.co/spaces/arad1367/Vector_Search_Methods_Comparison) (Space statico), [ChunkViz](https://chunkviz.up.railway.app/) (applicazione statica, divisione del testo in `chunkers.js`; ospitata su piano gratuito), [OCTOO VRAM Calculator](https://octooai.com/llm-vram-calculator/) (la pagina dichiara che gira nel browser). Tiktokenizer: tokenizzazione nel browser secondo la validazione. Restano da provare dalla rete della scuola: caricamento del modello e dei tokenizzatori scaricati da ogni postazione, cache e proxy. Un sito statico può comunque scaricare file dalla rete: non è dimostrato che non raggiunga mai un limite per indirizzo. |
| Collaudo incrociato | Modo di scambiare documenti e istruzioni fra VM (cartella condivisa, chiavetta, posta scolastica) |

## Decisioni

| Tema | Stato |
| --- | --- |
| Formato del test scritto | **Deciso:** misto, domande aperte brevi e a scelta multipla con motivazione. |
| Dataset e addestramento | **Deciso:** fuori dal percorso; con 8 GB e senza GPU non si eseguono. |
| Griglia di valutazione | Da definire. |
| Peso del lavoro di gruppo e del test individuale | Da definire. |
