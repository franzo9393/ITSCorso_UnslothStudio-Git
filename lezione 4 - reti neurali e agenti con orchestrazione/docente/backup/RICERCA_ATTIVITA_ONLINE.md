# Lezione 4 · Ricerca di attività interattive online

Temi: LLM locali, agenti, istruzioni di sistema (system prompt), RAG.
Data della ricerca: 4 novembre 2026. Documento riservato al docente.

## Stato del documento

- È una **ricerca preliminare**, non una progettazione della lezione e non un collaudo.
- Le risorse sono state verificate leggendo pagine ufficiali, termini e, dove utile, codice sorgente. **Nessuna conversazione, partita, download di modelli, registrazione o prova con account studente è stata eseguita.**
- «Confermata» significa conferma documentale. Tutto ciò che riguarda VM d'aula, rete della scuola e account studenti resta da provare.

### Metodo

| Fase | Agente | Modello | Prodotto |
| --- | --- | --- | --- |
| Ricerca per tema (4 in parallelo) | `scout` | ruolo `@task` (Gemini) con ricerca web Perplexity | `ricerca_attivita_online/01`–`04` |
| Validazione indipendente | `reviewer` | ruolo `@plan` (GPT) | `ricerca_attivita_online/05_validazione_revisore.md` |
| Approfondimento Colab con Gemini | `scout` + `reviewer` | come sopra | `ricerca_attivita_online/06`–`07` |
| Sintesi | agente principale | — | questo file |

I rapporti grezzi `01`–`04` contengono errori corretti dalla validazione (elencati sotto) e stime di durata non misurate: fa fede questo file.

## Selezione validata

Esiti: **C** confermata, **CR** confermata con riserve.

### LLM locali

| Risorsa | Esito | Che cosa fanno gli studenti | Condizioni prima dell'aula |
| --- | --- | --- | --- |
| [Unsloth Studio · Chat](https://unsloth.ai/docs/new/studio/chat) | CR | Scelgono temperatura, top-p e top-k per estrarre campi da un breve diario sintetico P03, fissano prima i criteri di riuscita, provano e correggono. Osservano latenza e completezza. | Versione installata, modello GGUF e template, parametri visibili, tempi reali con tutte le coppie collegate. Model Arena carica i due modelli **uno dopo l'altro**: non adatta alle VM a sola CPU. |
| [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) (Georgia Tech, MIT) | C | Prevedono come cambierà la distribuzione delle probabilità cambiando un solo parametro, poi osservano e spiegano. GPT-2 piccolo gira nel browser. | Fluidità sulle postazioni. Testo breve in inglese: è un modello di completamento, non un assistente. Si osservano le distribuzioni, non si cerca un errore. |
| [OCTOO VRAM Calculator](https://octooai.com/llm-vram-calculator/) (MIT, nessun account) | CR | Progettano un server di reparto entro un budget di memoria e lo rivedono cambiando quantizzazione, lunghezza del contesto e utenti contemporanei. | È una stima per GPU: esclude CPU, scarico su RAM e memoria unificata. Non trasferire i numeri alla VM. Il server registra gli accessi. |

Supporti brevi: [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) (CR, conteggio token di testi italiani e codici macchina nel browser) e [LLM Visualization](https://bbycroft.net/llm) (CR, solo visualizzazione in scala: i pesi GPT-2/3 non vengono eseguiti).

### Agenti

| Risorsa | Esito | Che cosa fanno gli studenti | Condizioni prima dell'aula |
| --- | --- | --- | --- |
| [Copilot · Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder) ([requisiti](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites)) | CR | Definiscono quali operazioni dell'agente producono solo testo, quali eseguono codice e quali non sono autorizzate; verificano le tracce di esecuzione su dati sintetici. | Prova con account studente: creazione, modifica, Code Interpreter, salvataggio, quote, nessuna fatturazione a consumo. Email, persone e Teams restano esclusi anche con fatturazione. |
| [Wiz Prompt Airlines](https://promptairlines.com/) | CR | Con una richiesta legittima mappano strumenti, argomenti e risultati nel pannello «Chat Under The Hood»; poi propongono un test e analizzano sia il successo sia il rifiuto, senza obbligo di superare il livello. | Termini [Wiz](https://legal.wiz.io/legal#terms-of-use): 18 anni. Compagnia e biglietti fittizi. Provare la chat e il livello scelto; conservazione dei messaggi non verificata. Nessuna immagine o dato reale. |
| [Hugging Face Agents Course · Unità 1](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure) (Apache-2.0) | CR | Su una scheda ricavata dal ciclo Pensiero–Azione–Osservazione progettano il programma di controllo: quando fermare il modello, quale funzione eseguire, quale risultato reinserire. | Non è un simulatore senza codice. Preparare una scheda breve con attribuzione; nessun token HF o programmazione per gli studenti. |

Supporto in italiano: [Microsoft AI Agents for Beginners, lezione 6](https://github.com/microsoft/ai-agents-for-beginners/blob/main/translations/it/06-building-trustworthy-agents/README.md) (C, MIT), da usare come traccia di progettazione, non come lettura integrale.

Unsloth Studio documenta ricerca web, esecuzione di codice e collegamenti [MCP](https://unsloth.ai/docs/basics/mcp) (CR), ma la chiamata di strumenti con Qwen2.5-1.5B sulla VM non è dimostrata: **non renderla obbligatoria** prima di un collaudo.

### Istruzioni di sistema

| Risorsa | Esito | Che cosa fanno gli studenti | Condizioni prima dell'aula |
| --- | --- | --- | --- |
| Unsloth Studio · campo System Prompt | CR | Scrivono istruzioni brevi per classificare eventi P03, chiedere i dati mancanti e separare fonte e istruzione. Le coppie si scambiano **casi di prova inventati**, non soluzioni. | Persistenza del campo, applicazione al template del GGUF, avvio di conversazioni pulite. Distinguere il campo di sistema dalle istruzioni incollate nel messaggio. |
| [Tiktokenizer](https://tiktokenizer.vercel.app/) (MIT) | CR | Scrivono messaggi di sistema e utente, vedono token e numeri identificativi; confrontano due formulazioni equivalenti e motivano la scelta. | Il formato mostrato non è il template Qwen della VM e non misura le prestazioni del motore. |
| [Prompt Engineering Guide in italiano](https://www.promptingguide.ai/it/introduction/tips) (DAIR.AI, MIT) | C | Scelgono un principio, progettano una modifica alle proprie istruzioni e ne confrontano l'effetto con una griglia comune. | Link diretti alle pagine gratuite; gli esempi sono illustrativi, non garanzie di comportamento. |

Giochi di attacco e difesa, solo dopo una partita di prova sulla rete della scuola: [Lakera Gandalf](https://play.lakera.ai/gandalf) (CR: alcuni scenari di Agent Breaker richiedono login; i messaggi sono raccolti per ricerca), [Tensor Trust](https://tensortrust.ai/) (CR: account; testi pubblicati in un dataset di ricerca), [HackMerlin](https://hackmerlin.io/) (CR: codice dei livelli leggibile su GitHub, GPL-3.0; condizioni del servizio non verificate). Evitare richieste su come escludere ripari o sicurezze della pressa: bastano vincoli innocui su formato, fonte o domande di chiarimento.

### RAG

| Risorsa | Esito | Che cosa fanno gli studenti | Condizioni prima dell'aula |
| --- | --- | --- | --- |
| Unsloth Studio · knowledge base in BM25 | CR | Su un corpus sintetico piccolo con codici P03/P30 espliciti progettano domande, ispezionano i passaggi recuperati e correggono domande o documenti. | Nel codice: `BM25 only`, `Semantic only`, `Hybrid`, top-K 1–20, recupero automatico. Il documento intero (`RAG_THREAD_WHOLE_DOC=1`) riguarda gli **allegati della conversazione**, non la knowledge base. Anche in BM25 l'indicizzazione calcola embedding: misurare RAM e tempi. |
| [ChunkViz](https://chunkviz.up.railway.app/) (MIT con attribuzione) | CR | Fissano un criterio verificabile (macchina, orario, allarme e causa nello stesso blocco), confrontano dimensione, sovrapposizione e tipo di divisione, motivano il compromesso. | Ospitato su piano gratuito: provarlo. La configurazione scelta **non si trasferisce** a Unsloth Studio (500 token, sovrapposizione 64): esplicitarlo. |
| [TensorFlow Embedding Projector](https://projector.tensorflow.org/) | CR, facoltativo | Confrontano i vicini nello spazio originale con la proiezione visiva. | Carica vettori già calcolati: non trasforma da solo i documenti P03. Se richiede troppa preparazione, ometterlo. |

Illustrazione breve: [Vector Search Methods Comparison](https://huggingface.co/spaces/arad1367/Vector_Search_Methods_Comparison) (C, MIT), esempi fissi BM25/TF-IDF/ibrido; non è una misura sui dati P03.

## Google Colab con Gemini

Colab è un servizio cloud: un modello a pesi aperti eseguito sulla GPU di Colab **non è un LLM locale** dal punto di vista della riservatezza.

| Funzione | Esito | Fatti verificati | Uso possibile |
| --- | --- | --- | --- |
| Data Science Agent ([annuncio](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/), [FAQ](https://research.google.com/colaboratory/faq.html)) | C | Riceve un obiettivo e un file (CSV, TSV, JSON, Excel), presenta un piano da approvare, scrive ed esegue celle, osserva i risultati e si corregge. Aperto a tutti gli utenti Colab. | **Esempio concreto di agente con azioni eseguite e osservabili.** Dimostrazione del docente su un file sintetico P03: la classe prevede il piano, lo controlla prima dell'esecuzione e verifica i risultati con un riepilogo calcolato a parte. |
| `google.colab.ai` ([sorgente](https://raw.githubusercontent.com/googlecolab/colabtools/main/google/colab/ai.py)) | CR | Modelli Gemini/Gemma senza chiave personale, tramite credenziali interne di Colab; catalogo da `ai.list_models()`. `generate_text()` invia un solo messaggio con ruolo `user`. | Inadatto per le istruzioni di sistema. Possibile solo come generatore in un RAG BM25 a celle preparate. |
| Notebook [Unsloth Studio su Colab](https://raw.githubusercontent.com/unslothai/unsloth/main/studio/Unsloth_Studio_Colab.ipynb) | Scartato per l'aula | Avvia un'interfaccia web, di solito tramite tunnel Cloudflare. Nel piano gratuito le [FAQ](https://research.google.com/colaboratory/faq.html#disallowed-activities) vietano di usare il runtime soprattutto da un'interfaccia web esterna al notebook. GPU gratuita non garantita. | Resta un'esplorazione personale facoltativa, come già indicato in `materiali_aula/RISORSE_E_ACCESSO.md`. |

Condizioni e limiti:

- **Account:** serve un account Google che risulti maggiorenne e con lingua e area supportate. Con Workspace for Education Colab è un servizio aggiuntivo che deve risultare attivo per gli studenti. Che la scuola abbia account Google **non è stato verificato**.
- **Dati:** prompt, codice e risultati inviati a Gemini in Colab possono essere letti da revisori umani, usati per migliorare i prodotti Google e conservati fino a 18 mesi senza possibilità di cancellazione. L'esclusione dall'addestramento prevista per Education riguarda l'app Gemini, non Colab. Solo dati sintetici.
- **Credenziali:** i termini di Colab vietano di condividerle. La dimostrazione resta sull'account del docente.
- **Decisione (4 novembre 2026): Colab non si usa nella lezione 4.** Il Data Science Agent ripete l'idea dell'agente che esegue Python già prevista nella lezione 3 e richiede account Google non verificati; la lezione deve mostrare strumenti nuovi e interattivi.

## Risorse in riserva

Utilizzabili solo dopo un collaudo specifico; fuori dal percorso obbligatorio.

| Risorsa | Motivo della riserva |
| --- | --- |
| [WebLLM Chat](https://chat.webllm.ai/) | Richiede WebGPU nel browser effettivo; download pesante se ripetuto su tutte le postazioni. |
| [Qwen3 Embedding Scatterplot](https://huggingface.co/spaces/webml-community/qwen3-embedding-webgpu) | Solo WebGPU, senza ripiego su CPU. Le etichette sono categorie candidate assegnate per somiglianza. |
| [PromptInjects](https://promptinjects.com/play) | Messaggi inviati a OpenRouter e ai fornitori dei modelli; servizio non rivolto ai minori di 16 anni. |
| [Prefactor Prompt Injection Test](https://prefactor.tech/tools/prompt-injection-test) | Cerca una stringa di controllo nella risposta incollata: non osserva azioni eseguite. Informativa privacy non sostanziale. |
| [Google AI Studio](https://aistudio.google.com/) | 18 anni; account Google personale o Workspace scolastico abilitato. Non raggiungibile con il solo account Microsoft. |
| [Gemini Notebook / NotebookLM](https://notebook.google/) | Account Google; per account scolastici serve abilitazione dell'amministratore. Non imporre account personali. |
| [GroqCloud Playground](https://console.groq.com/playground) | Account, 18 anni, [accordo servizi](https://console.groq.com/docs/legal/services-agreement) specifico del Playground. |
| [Copilot Notebooks → Workspaces](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-to-copilot-workspaces) | Previsti nella progettazione della lezione 3 (da verificare che cosa è stato svolto in aula); cambio di nome in corso da fine ottobre 2026, l'etichetta nel menu può variare. |
| Cemantle / Cémantix | Solo inglese o francese; la parola del giorno non garantisce il contrasto didattico voluto. |
| llamafile | Dimostrazione eventuale del docente; ridondante con Unsloth Studio. |

## Risorse scartate

Il revisore ha riconfermato i motivi di TokenCalc, HackAPrompt, Courtney Root, RAG-Chat-Visualizer, OpenCode, HuggingChat e Flowise. Gli altri motivi provengono dai rapporti di ricerca e non sono stati riverificati.

| Risorsa | Motivo |
| --- | --- |
| TokenCalc | Pagine `/privacy` e `/terms` in errore 404. |
| HackAPrompt | [Accordo partecipanti](https://www.hackaprompt.com/participant_agreement): 18 anni, cessione dei diritti sui testi, registrazione. |
| Courtney Root Prompt Injection Game | 40 turni al giorno per indirizzo IP: insufficiente con l'IP condiviso della scuola. |
| RAG-Chat-Visualizer (quickgrid) | La modalità «Rigid» non fa ciò che descrive; nessun ripiego CPU affidabile; può mostrare estratti al posto di risposte generate; licenza non dichiarata. |
| Unsloth + OpenCode | Installazione e configurazione preventive, agente di programmazione non necessario. |
| HuggingChat Assistants | Dopo il login non è verificato che la funzione esista ancora nella versione corrente. |
| Flowise | [Chiuso](https://flowiseai.com/sunset) (fine supporto 31 agosto 2026). |
| Langflow, n8n | Installazione o account individuale, troppo complessi per la lezione. |
| Semantle italiano | Punteggi calcolati con una funzione di hash, non con embedding. |
| Spazi HF guasti al 4/11/2026 | `m-ric/chunk_visualizer`, `sentence-transformers/embeddings-semantic-search`, demo BM25 e altri: errori di avvio o chiave OpenAI obbligatoria. |
| Anthropic tutorial, Crucible, Immersive Labs, OpenRouter Chat | Chiave API, iscrizioni chiuse, sito non disponibile o crediti. |

## Errori dei rapporti grezzi corretti dalla validazione

1. **Licenza di Unsloth Studio:** il [LICENSE](https://raw.githubusercontent.com/unslothai/unsloth/main/LICENSE) separa la libreria `unsloth/*` (Apache-2.0) da `studio/*` e `unsloth_cli/*` (**AGPL-3.0**).
2. **Privacy locale:** spegnere la ricerca web non basta a escludere traffico esterno se sono attivi MCP o fornitori remoti.
3. **Documento intero nel contesto:** vale per gli allegati della conversazione, non per la knowledge base.
4. **Prompt Airlines:** biglietti e compagnia fittizi, non azioni reali.
5. **Agent Breaker:** non tutti gli scenari sono giocabili senza login.
6. **Google AI Studio:** l'account personale non è obbligatorio se il Workspace scolastico è abilitato.
7. **Groq:** i termini del sito escludono il Playground; vale l'accordo servizi.
8. **Copilot:** email, persone e Teams sono esclusi anche con fatturazione a consumo.
9. **Tiktokenizer:** la tokenizzazione avviene nel browser.
10. **Prefactor:** non verifica l'esecuzione di comandi.

Affermazioni **non dimostrate** da non riportare nei materiali: tempi di risposta e token al secondo sulle VM, disponibilità delle funzioni Copilot per ogni studente, comportamento interno dei Blocchi appunti, «nessun dato raccolto» per i siti che elaborano nel browser.

## Indicazioni per la progettazione

- Costruire il nucleo su **Unsloth Studio + ChunkViz**, con **Transformer Explainer o Tiktokenizer** come supporto breve e **un solo percorso sugli agenti** già collaudato.
- Riutilizzare lo stesso corpus sintetico P03 nelle quattro parti, con pochi strumenti.
- Riscrivere le idee dei rapporti grezzi fondate sull'errore atteso del modello: «sbaglia i calcoli», «inventa l'osservazione», «BM25 fallisce sui sinonimi», «il RAG perde righe», gare per superare livelli. Un risultato corretto deve essere utile quanto uno sbagliato.
- Ogni attività produce una decisione motivata, una prova osservabile e una revisione delle istruzioni da parte degli studenti.
- Corpus sintetico o con diritti verificati; niente log aziendali, credenziali o nomi di operatori.

## Collaudo prima dell'aula

| Punto | Controllo | Esito |
| --- | --- | --- |
| Versione Unsloth Studio | Presenza di campo di sistema, parametri, impostazioni di recupero, strumenti | |
| VM e carico | RAM, CPU, tempi di indicizzazione e risposta con tutte le coppie collegate | |
| RAG | Knowledge base o allegati, passaggi recuperati, citazioni, embedding avviati in BM25 | |
| Strumenti dell'agente | Esecuzione realmente osservabile, non solo codice stampato | |
| Account studente Microsoft | Agent Builder, Code Interpreter, Workspaces, quote; nessuna fatturazione a consumo | |
| Browser delle postazioni | WebGL, WebGPU, proxy, download, cache | |
| Giochi selezionati | Partita anonima completa sullo scenario scelto, limiti per IP, raccolta messaggi, termini | |
| Account Google | Workspace scolastico ed età, se si usa un servizio Google | |

## Reti neurali e addestramento (aggiunta del 10 novembre 2026)

La lezione 4 è stata riprogettata senza Unsloth Studio (vedi `BOZZA_PERCORSO_LEZIONI_4-7.md`). Le risorse sopra su Studio, System Prompt e RAG restano valide per le lezioni 5–7. Per la nuova lezione 4 serviva una ricerca su giochi nel browser che mostrino come funziona una rete neurale; il rapporto è in `ricerca_attivita_online/08_ricerca_reti_neurali.md` e le licenze in `fonti_online/LICENZE_E_FONTI.md`.

| Risorsa | Esito | Uso nella lezione 4 |
| --- | --- | --- |
| [TensorFlow Playground](https://playground.tensorflow.org/) | C | Parte 2: addestramento con esempi, pesi, Training loss e Test loss, rumore. Apache-2.0 (repository); la pagina dichiara che si può usare «in any way that follows our Apache License». Contatta Google Fonts e Google Analytics. |
| [Flappy Learning](https://xviniette.github.io/FlappyLearning/) | C | Parte 3: neuroevoluzione, un'analogia con addestrare premiando i risultati. MIT (repository). Contatta Google Fonts. |
| [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) | C, con riserva | Parte 1, già in questa ricerca. Il 10 novembre la pagina dichiara lo scarico di circa 600 MB all'apertura: su 22 postazioni è un carico sulla rete della scuola (vedi guida docente, «Parte 1»). |

Esiti **C**: confermata da lettura di licenza, apertura e prove con Chromium dalla postazione del docente, rete non scolastica. Funzionamento dalla rete della scuola e dalle postazioni degli studenti da provare.
