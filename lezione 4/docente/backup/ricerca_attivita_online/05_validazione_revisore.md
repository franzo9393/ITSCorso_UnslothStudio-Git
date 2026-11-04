# Validazione indipendente delle risorse per la lezione 4

**Conclusione:** i rapporti contengono risorse utili, ma **non sono utilizzabili come elenco di attività già collaudate**. Ho confermato le principali funzioni documentate di Unsloth Studio e diversi strumenti browser; ho trovato errori sulla licenza di Studio, sul funzionamento di alcune demo RAG, sulle condizioni di partecipazione a HackAPrompt e alcune generalizzazioni improprie su privacy e disponibilità degli account.

**Metodo e limiti:** ho letto i quattro rapporti e aperto direttamente documentazione ufficiale, informative, termini e codice sorgente. **Non ho eseguito conversazioni, scaricato modelli, effettuato registrazioni né utilizzato gli account studenti.** Una pagina raggiungibile, un controllo presente nel codice o lo stato `RUNNING` di uno Space non equivalgono a una prova completa del servizio. Nessun file è stato modificato.

## 1. Tabelle di validazione

Gli esiti riguardano **l’impiego proposto in questa lezione**, non il valore generale della risorsa. **CONFERMATA** significa conferma documentale delle caratteristiche indicate, non collaudo interattivo.

### A. Unsloth Studio: verifica delle affermazioni prioritarie

| Tema | Risorsa | URL | Esito | Che cosa ho verificato direttamente | Correzioni ai rapporti |
|---|---|---|---|---|---|
| LLM locali | Unsloth Studio: chat, parametri, Model Arena, export | [Chat](https://unsloth.ai/docs/new/studio/chat.md), [Export](https://unsloth.ai/docs/new/studio/export.md) | **CONFERMATA CON RISERVE** | La documentazione dichiara supporto CPU senza GPU, modifica manuale di temperatura/top-p/top-k e system prompt. **Model Arena esiste**: confronta due modelli con lo stesso prompt, caricandoli **prima uno e poi l’altro**, non in inferenza parallela. Export GGUF/LoRA/modello merged documentato. | Non è dimostrata la presenza di tutte queste funzioni nella versione installata sulle VM. Arena non va descritta automaticamente come confronto fra due system prompt dello stesso modello. Evitare conversioni/export durante il laboratorio CPU. |
| System prompt | Unsloth Studio: campo dedicato | [Documentazione](https://unsloth.ai/docs/new/studio/chat.md), [campo nel sorgente][U-settings] | **CONFERMATA CON RISERVE** | Nel codice letto esiste una sezione `System Prompt` con textarea modificabile e salvataggio nei preset. | Distinguere il campo system dalle istruzioni incollate nella chat. L’effettiva applicazione al GGUF e al template della VM resta da provare. |
| Agenti | Unsloth Studio: Web search, esecuzione codice, MCP | [Chat](https://unsloth.ai/docs/new/studio/chat.md), [MCP](https://unsloth.ai/docs/basics/mcp.md), [controlli UI][U-composer] | **CONFERMATA CON RISERVE** | Documentati ricerca DuckDuckGo, Bash/Python e collegamento MCP. Nel sorgente sono presenti controlli Search, Tools e MCP; le etichette non coincidono sempre con quelle dei rapporti. La guida MCP distingue server, autenticazione e interruttore generale. | **Web search spento non basta a garantire assenza di traffico esterno**: anche provider remoti e MCP possono inviare dati. Non è verificata l’affidabilità del tool calling di Qwen2.5-1.5B sulle VM. |
| RAG | Unsloth Studio: BM25, semantico, ibrido, top-K | [Controlli retrieval][U-retrieval-ui], [dispatch backend][U-retrieval] | **CONFERMATA CON RISERVE** | Nel commit citato dal rapporto sono presenti `BM25 only`, `Semantic only`, `Hybrid`, top-K **1–20**, Auto/On/Off e soglia **0–1**. Il backend instrada effettivamente le tre modalità; Hybrid usa fusione RRF. | Conferma del **codice upstream**, non della versione d’aula. Il contesto disponibile indica BM25: non costruire la lezione sul confronto semantico/ibrido prima di averlo abilitato e provato. |
| RAG | Unsloth Studio: whole-document e indicizzazione | [Configurazione][U-config], [consumatore whole-document][U-tool], [ingestion][U-ingestion] | **CONFERMATA CON RISERVE** | Confermati default `RAG_THREAD_WHOLE_DOC=1`, budget 6000 token, chunk 500/overlap 64. Tuttavia `whole_document_context` legge gli **allegati del thread**; il codice precisa che knowledge base e progetti restano search-only. Nell’ingestion letta viene comunque eseguito embedding. | Correggere la generalizzazione “file corti della KB inseriti interamente”. **BM25 only non significa pipeline priva di embedding**: esistono indicizzazione vettoriale e, in alcune condizioni, una sonda dense per l’auto-retrieval. |
| Tutti | Licenza Unsloth | [LICENSE ufficiale](https://raw.githubusercontent.com/unslothai/unsloth/main/LICENSE) | **CONFERMATA** | Il file distingue esplicitamente core `unsloth/*`, test e script **Apache-2.0**, da `studio/*` e `unsloth_cli/*` **AGPLv3**. I file Studio letti riportano `AGPL-3.0-only`. | **È corretta la distinzione del rapporto RAG. Sono errate le attribuzioni indiscriminate Apache-2.0 a Studio negli altri tre rapporti.** |

### B. Strumenti browser e LLM locali complementari

| Tema | Risorsa | URL | Esito | Che cosa ho verificato direttamente | Correzioni ai rapporti |
|---|---|---|---|---|---|
| LLM locali | Transformer Explainer | [App](https://poloclub.github.io/transformer-explainer/), [repository](https://github.com/poloclub/transformer-explainer) | **CONFERMATA** | Pagina pubblica e repository descrivono GPT-2 small 124M nel browser, ONNX, testo proprio, temperatura/top-k/top-p; licenza MIT letta. | Non serve presentarlo come chatbot italiano. L’esito “temperatura alta → parole sbagliate” non è garantito: osservare le **distribuzioni**, non pretendere un errore. Prestazioni del browser da provare. |
| LLM locali | The Tokenizer Playground | [Space](https://huggingface.co/spaces/Xenova/the-tokenizer-playground), [app](https://xenova-the-tokenizer-playground.static.hf.space/index.html) | **CONFERMATA CON RISERVE** | Space statico pubblico; bundle letto con selezione tokenizer e invio del testo a un **Web Worker locale**. La UI dichiara elaborazione nel browser. [Termini HF](https://huggingface.co/terms-of-service) letti. | I tokenizer disponibili sono versioni specifiche: non equivalgono necessariamente ai tokenizer correnti di tutti i servizi omonimi. Non garantire una riduzione del 30% senza perdita informativa. La licenza della libreria non va automaticamente attribuita a ogni asset della demo. |
| LLM locali / system | WebLLM Chat | [App](https://chat.webllm.ai/), [repository ufficiale](https://github.com/mlc-ai/web-llm-chat) | **CONFERMATA CON RISERVE** | Repository: inferenza WebGPU nel browser, accesso offline dopo setup/download, Apache-2.0. Supporto modelli descritto anche nel [motore WebLLM](https://github.com/mlc-ai/web-llm). | Non adatto come attività obbligatoria sulle VM CPU. Browser aggiornato non prova che WebGPU sia disponibile nella sessione remota. La modalità endpoint REST avanzata non è la stessa cosa dell’inferenza nel browser. |
| LLM locali | OCTOO VRAM Calculator | [Calcolatore](https://octooai.com/llm-vram-calculator/), [privacy](https://octooai.com/privacy/), [metadati Space](https://huggingface.co/api/spaces/octooai/llm-vram-calculator) | **CONFERMATA CON RISERVE** | Dichiarazione di calcolo browser, pesi/KV cache/runtime, formule e limiti espliciti; MIT nei metadati dello Space. Privacy: niente analytics/cookie del sito, ma **access log del server**, hosting USA e video esterni su click. | Ottimo per **stime**, non certificazione di compatibilità. La pagina esclude CPU/offload, multi-GPU e Mac unified memory: non basta trasporre automaticamente il totale VRAM sulla RAM della VM. |
| LLM locali | TokenCalc | [VRAM](https://tokencalc.dev/tools/vram-calculator/), [token counter](https://tokencalc.dev/tools/token-counter/) | **SCARTARE** come risorsa selezionata | Le pagine dichiarano client-side/no signup. Confermati conteggi approssimati caratteri/4 per modelli non OpenAI. Ho ottenuto **404** da `/privacy` e `/terms`. | I rapporti segnalano correttamente i 404, ma questo impedisce di considerare verificato l’insieme delle condizioni richieste. I byte/parametro e i risultati vanno presentati come stime. |
| System / token | Tiktokenizer | [App](https://tiktokenizer.vercel.app/), [repository](https://github.com/dqbd/tiktokenizer) | **CONFERMATA CON RISERVE** | App pubblica con messaggi e token ID; MIT. Nel [caller frontend](https://raw.githubusercontent.com/dqbd/tiktokenizer/master/src/pages/index.tsx) il testo viene tokenizzato localmente; il [modulo tokenizer](https://raw.githubusercontent.com/dqbd/tiktokenizer/master/src/models/tokenizer.ts) scarica eventualmente risorse/tokenizer tramite proxy. | **Non è corretta l’affermazione che l’aggiornamento della vista richieda tokenizzazione su route edge/web.** Non dimostra nemmeno che un backend LLM ricalcoli sempre tutto a ogni turno. |
| LLM locali | LLM Visualization — Bycroft | [App](https://bbycroft.net/llm), [repository](https://github.com/bbycroft/llm-viz) | **CONFERMATA CON RISERVE** | Repository MIT: modello minuscolo con pesi funzionanti per ordinare A/B/C; architetture maggiori visualizzabili, ma i pesi GPT-2 non sono scaricati. | Non confondere la visualizzazione in scala con esecuzione reale di GPT-2/GPT-3. Supporto breve, non laboratorio centrale sul caso P03. |
| LLM locali | llamafile | [Repository ufficiale](https://github.com/Mozilla-Ocho/llamafile) | **CONFERMATA CON RISERVE** | Confermati eseguibile singolo, quickstart Qwen3.5-0.8B, funzionamento locale, Apache-2.0/MIT e limite Windows per eseguibili oltre 4 GB. | È comunque download ed esecuzione di software. Ridondante con Studio e non necessario nelle due ore; eventuale dimostrazione preparata dal docente, non setup simultaneo. |

### C. Agenti, system prompt e giochi di sicurezza

| Tema | Risorsa | URL | Esito | Che cosa ho verificato direttamente | Correzioni ai rapporti |
|---|---|---|---|---|---|
| Agenti | Wiz Prompt Airlines | [Gioco](https://promptairlines.com/), [spiegazione ufficiale](https://www.wiz.io/blog/prompt-airlines-ai-security-challenge) | **CONFERMATA CON RISERVE** | Pagina pubblica con avvio sfida, registrazione proposta per leaderboard, pannello **Chat Under The Hood**, upload tessera dal livello 4. Letti i [termini collegati](https://legal.wiz.io/legal#terms-of-use): 18+. | Il biglietto è **fittizio**, dichiarato esplicitamente. Non ho collaudato chiamate/backend o verificato conservazione dei prompt. L’informativa Google Acquisitions tratta Service Data e non risolve da sola il trattamento del contenuto delle chat. |
| Agenti / system | Lakera Gandalf / Agent Breaker | [Agent Breaker](https://play.lakera.ai/agent-breaker), [Gandalf](https://play.lakera.ai/gandalf), [privacy](https://www.checkpoint.com/privacy/) | **CONFERMATA CON RISERVE** | Entrambi gli indirizzi servono l’app. HTML con HubSpot/analytics; policy Check Point con soglia privacy under-16. Nel [bundle pubblico](https://play.lakera.ai/assets/index-ef5a798b.js) esistono scenari con autenticazione differenziata. | **“Nessun account per Agent Breaker” non è universalmente vero**: `northwind_pricing_exfil` risulta `requiresAuth: true`. La clausola privacy sui minori non equivale, da sola, a termini completi del gioco. Numero fisso di app/livelli non riconfermato. |
| System | Tensor Trust | [Sito e consenso](https://tensortrust.ai/), [repository](https://github.com/HumanCompatibleAI/tensor-trust) | **CONFERMATA CON RISERVE** | Letto consenso esplicito: prevista pubblicazione di testi, timestamp e identificatori raggruppabili per utente; IP/browser raccolti ma esclusi dal dataset pubblico. Il consenso fa riferimento alla creazione account. | **Non ho confermato una partita funzionante**, la creazione account o il matchmaking. Non è un piano B certo. Solo segreti completamente inventati; mai codici reali. |
| System | HackAPrompt / HackAPromptle | [Homepage](https://www.hackaprompt.com/), [accordo partecipanti](https://www.hackaprompt.com/participant_agreement), [TOS](https://www.hackaprompt.com/tos), [privacy](https://www.hackaprompt.com/privacy) | **SCARTARE** dal laboratorio principale | Tutorial Track esiste e rimanda a signup; HackAPromptle restituisce un guscio pagina. Accordo competizione: **18+**, trasferimento dei diritti sulle submission, vincoli di riservatezza; privacy con tracking/marketing. | La generica indicazione **16 anni** è insufficiente/errata per la competizione. Non è dimostrata la pubblicazione open-source di **tutti** i prompt: è pubblicato uno specifico dataset Pliny, mentre gli accordi disciplinano più ampiamente i diritti sulle submission. |
| System | HackMerlin | [App](https://hackmerlin.io/), [repository](https://github.com/bgalek/hackmerlin.io) | **CONFERMATA CON RISERVE** | Pagina raggiungibile; repository GPL-3.0; backend Azure OpenAI documentato. | Nessuna prova di partita eseguita; condizioni del servizio ospitato e raccolta dei prompt non sufficientemente verificate. Più utile leggere codice selezionato che dipendere dal gioco. |
| Agenti / system | Prefactor Prompt Injection Test | [Tester](https://prefactor.tech/tools/prompt-injection-test), [privacy](https://prefactor.tech/privacy-policy) | **CONFERMATA CON RISERVE** | Pagina: 13 pattern, scoring client-side per presenza di canary, nessun collegamento automatico all’agente. Specifica che non è un audit di sicurezza. La pagina privacy letta contiene sostanzialmente solo titolo e rimandi commerciali. | **Non verifica l’esecuzione di un comando** come `FERMA_PRESSA`: cerca una stringa nella risposta incollata. Comandi solo descritti nel prompt restano simulati. Informativa privacy sostanziale non confermata. |
| Agenti / system | Courtney Root Prompt Injection Game | [Gioco](https://courtneyroot.dev/projects/prompt-injection-game/), [repository](https://github.com/rootcour/prompt-injection-game) | **SCARTARE** per uso contemporaneo delle coppie | Confermati cinque livelli, Cloudflare Workers AI, dichiarazione di non salvare i testi e **40 turni/giorno condivisi per IP**, 800 globali. Il repository riconosce esplicitamente il problema delle reti scolastiche. | Il limite è un ostacolo concreto. Non proporre hotspot come soluzione organizzativa ordinaria. Codice pubblico non significa automaticamente licenza open-source verificata. |
| Agenti / system | PromptInjects | [Sfide](https://promptinjects.com/play), [privacy](https://promptinjects.com/privacy) | **CONFERMATA CON RISERVE** | Pagina dichiara sfide gratuite senza login per chat/capture. Privacy: prompt elaborati da **OpenRouter e provider sottostanti**, log tecnici; servizio non diretto a under-16. | “Tracciato solo nel browser” riguarda una parte del progresso anonimo, **non l’intera interazione**. Non ho riconfermato capacità/costi dell’evento privato o provato una chat. |
| Agenti | Unsloth + OpenCode | [Integrazione](https://unsloth.ai/docs/integrations/opencode.md), [permessi V2](https://opencode.ai/v2/docs/permissions/) | **SCARTARE** per questa lezione | Integrazione reale, installazione client e chiave API locale documentate; regole V2 `allow/ask/deny` confermate. | Default non significa “chiede sempre prima di scrivere”: la policy di base permette molte azioni. Richiede configurazione preventiva, aumenta complessità e introduce un coding agent non necessario. |
| Agenti | Hugging Face Agents Course | [Ciclo agente](https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure), [Dummy Agent](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library), [repository](https://github.com/huggingface/agents-course) | **CONFERMATA CON RISERVE** | Lettura pubblica, repository Apache-2.0. Dummy Agent contiene codice Python con token HF e esempio documentato di falsa Observation. | **Non è un simulatore browser autonomo zero-codice**. Non trasferire l’output dell’esempio in una previsione certa del comportamento di Qwen sulla VM. |
| Agenti | Microsoft AI Agents for Beginners | [Lezione italiana letta](https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main/translations/it/06-building-trustworthy-agents/README.md), [licenza](https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main/LICENSE) | **CONFERMATA** come materiale di supporto | Lezione italiana con framework per istruzioni, minacce e iterazione; MIT verificata. | Non è di per sé attività interattiva. Usare una scheda di progettazione e prova, non far copiare passivamente il meta-prompt o leggere intere lezioni. |
| System | DAIR.AI in italiano | [Suggerimenti](https://www.promptingguide.ai/it/introduction/tips), [repository](https://github.com/dair-ai/Prompt-Engineering-Guide) | **CONFERMATA** come supporto | Pagina italiana pubblica; progettazione iterativa, specificità, esempi e “fare/non fare”; MIT del repository. | Gli esempi sono illustrativi, non dimostrazione che una formulazione fallisca sempre e un’altra riesca sempre. |
| System | Learn Prompting: XML/Sandwich | [XML](https://learnprompting.org/docs/prompt_hacking/defensive_measures/xml_tagging), [termini](https://learnprompting.org/terms-of-service) | **CONFERMATA CON RISERVE** | XML tagging pubblico; la guida stessa ammette aggirabilità e dice che XML+escape richiede programmazione. Termini: 16+, consenso genitore sotto 18; ampia licenza sui contenuti inviati. | I delimitatori **non creano un vero ruolo system** e non sono un controllo autorizzativo. Consultazione della guida distinta da riuso integrale dei contenuti o invio a esercizi. |

### D. Servizi cloud con account

| Tema | Risorsa | URL | Esito | Che cosa ho verificato direttamente | Correzioni ai rapporti |
|---|---|---|---|---|---|
| Agenti | Copilot Agent Builder | [Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder), [licenze/capacità](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites), [gestione Basic](https://learn.microsoft.com/en-us/copilot/manage/manage-agents-copilot-chat) | **CONFERMATA CON RISERVE** | Le fonti documentano agenti basati su istruzioni/siti pubblici inclusi in Basic e capacità come Code Interpreter nella matrice senza billing. Agenti su dati tenant condivisi richiedono condizioni ulteriori/billing. Admin e rete possono limitare accesso. | **Non “già disponibile” per ogni studente.** La documentazione contiene anche formulazioni non perfettamente allineate sull’authoring: serve prova account. Email e Teams nella matrice richiedono licenza completa, non basta il pay-as-you-go. |
| RAG | Copilot Notebooks → Workspaces | [Requisiti](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-requirements), [rinomina](https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-notebooks-to-copilot-workspaces) | **CONFERMATA CON RISERVE** | **Rinomina reale**, rollout a fasi da fine ottobre 2026. Requisiti distinguono licenza, storage SharePoint Embedded, rete e policy. Confermato disallineamento fra tabella e paragrafo licenze. | L’esperienza della lezione 3 non prova l’abilitazione di tutti gli studenti. Non è documentato in queste pagine un algoritmo interno “top-K che perde necessariamente righe”. |
| System | Google AI Studio | [Termini](https://aistudio.google.com/docs/terms), [accesso Workspace](https://aistudio.google.com/docs/workspace), [requisiti età](https://aistudio.google.com/docs/troubleshoot-ai-studio) | **CONFERMATA CON RISERVE** | Accesso AI Studio gratuito documentato; **18+**; Workspace supportato, con controllo amministratore e classificazione età per Education. Confermata clausola EEA che applica il trattamento dati dei Paid Services anche all’uso gratuito. | **Account personale non obbligatorio**: è possibile Workspace. Non è però disponibile tramite il solo account Microsoft. I termini lo destinano a sviluppo professionale/business e non autorizzano generici tentativi di aggirare le protezioni. |
| RAG | NotebookLM / Gemini Notebook | [Sito](https://notebook.google/), [requisiti/privacy](https://support.google.com/gemininotebook/answer/16164461?hl=en), [scuola e limiti](https://support.google.com/gemininotebook/answer/16337734?hl=en) | **CONFERMATA CON RISERVE** | Le pagine ufficiali usano **Gemini Notebook**; account Google necessario, personale o scuola/lavoro, admin per account gestiti. Education disponibile a tutte le età; Standard 100 notebook, 50 fonti/notebook, 50 chat/giorno. Protezioni Education confermate. | Non generalizzare “18+ necessario per accedere”: per personali vale l’età di consenso applicabile, con alcune funzioni 18+. Non richiedere la creazione di account personali come ripiego automatico. |
| System | HuggingChat / Assistants | [Chat corrente](https://huggingface.co/chat/), [Assistants](https://huggingface.co/chat/assistants), [codice corrente](https://github.com/huggingface/chat-ui) | **NON CONFERMATA** per il laboratorio Assistants | La chat è raggiungibile e presenta **Omni/ML Intern**: non risulta semplicemente un servizio chiuso. `/assistants` reindirizza al login. Il repository distingue versione corrente e legacy; nelle route correnti lette non compare la vecchia sezione Assistants. | Il redirect OAuth **non prova** che, dopo login, esistano ancora creazione/condivisione Assistant come descritte. Non selezionare questo esercizio senza prova autenticata. |
| System | GroqCloud Playground | [Playground](https://console.groq.com/playground), [accordo servizi](https://console.groq.com/docs/legal/services-agreement) | **CONFERMATA CON RISERVE** | Pagina con System/User/View code; accordo applicabile a Playground: account, **18+**, trattamento input/output, limiti e condizioni dei modelli. | Il rapporto cita soprattutto i [Terms of Use del sito](https://groq.com/terms-of-use/), che **escludono espressamente Playground/GroqCloud**. Non ho provato signup, quota gratuita o inferenza. |

### E. Demo RAG ed embedding

| Tema | Risorsa | URL | Esito | Che cosa ho verificato direttamente | Correzioni ai rapporti |
|---|---|---|---|---|---|
| RAG | ChunkViz | [App](https://chunkviz.up.railway.app/), [codice](https://raw.githubusercontent.com/gkamradt/ChunkViz/main/src/App.js), [licenza](https://raw.githubusercontent.com/gkamradt/ChunkViz/main/LICENSE.txt) | **CONFERMATA CON RISERVE** | App raggiungibile; codice con textarea, FileReader, chunk size/overlap e splitter JS; MIT con attribuzione. | Non collaudato il runtime. ChunkViz **non modifica** i chunk di Studio: il trasferimento didattico va esplicitato. Avviare una copia locale non è garantito “in pochi secondi” senza preparazione. |
| RAG | quickgrid RAG-Chat-Visualizer | [Space/API](https://huggingface.co/api/spaces/quickgrid/RAG-Chat-Visualizer), [codice](https://huggingface.co/spaces/quickgrid/RAG-Chat-Visualizer/raw/main/index.html) | **SCARTARE** dal laboratorio principale | Statico pubblico `RUNNING`. Codice letto per caricamento modelli, generazione e Rigid Mode; nessuna licenza specifica dichiarata nei metadati letti. | **Rigid non aggiunge il system prompt descritto:** con contesto tale istruzione è già sempre presente. Il fallback CPU automatico non è affidabilmente implementato; errori LLM possono produrre **estratti/template**, pur mostrando “Models Ready”. |
| RAG | Qwen3 Embedding Scatterplot | [Metadati](https://huggingface.co/api/spaces/webml-community/qwen3-embedding-webgpu), [codice](https://huggingface.co/spaces/webml-community/qwen3-embedding-webgpu/raw/main/index.html) | **CONFERMATA CON RISERVE** | Apache-2.0, statico pubblico; `device:"webgpu"` e `q4f16`, senza fallback esplicito. Frasi ed etichette editabili, embedding e UMAP nel browser. | `Labels` sono **categorie candidate**: il codice assegna ciascuna frase per similarità, non una categoria manuale per ogni riga. La posizione 2D non è una misura fedele di tutte le distanze originali. Non per VM CPU. |
| RAG | TensorFlow Embedding Projector | [App e sorgente incorporato](https://projector.tensorflow.org/) | **CONFERMATA CON RISERVE** | Nel sorgente letto: licenze Apache/BSD/MIT delle componenti, lettura locale TSV tramite FileReader, calcolo vicini e controlli Load/neighbors. | **Carica vettori già calcolati**, non trasforma da solo i documenti P03 in embedding. Proiezione PCA/t-SNE/UMAP e distanza originale vanno distinte. Browser/WebGL da collaudare. |
| RAG | Vector Search Methods Comparison | [Metadati](https://huggingface.co/api/spaces/arad1367/Vector_Search_Methods_Comparison), [codice](https://huggingface.co/spaces/arad1367/Vector_Search_Methods_Comparison/raw/main/index.html) | **CONFERMATA** come illustrazione | Statico pubblico, MIT; pannelli e selettori BM25/TF-IDF/Hybrid presenti nel codice. | È una **simulazione illustrativa con esempi predefiniti**, non un benchmark delle prestazioni dei metodi sui dati P03. |
| RAG / embedding | Cemantle / Cémantix / Semantle | [Regole Cemantle](https://static.certitudes.org/html/cemantle-rules.html), [privacy Cémantix](https://static.certitudes.org/html/cemantix-privacy.html) | **CONFERMATA CON RISERVE** per Cemantle/Cémantix; **NON CONFERMATA** per Semantle | Regole: prossimità contestuale, top-1000, contrari talvolta vicini; privacy menziona strumenti Google per analytics/pubblicità. Non ho riconfermato separatamente Semantle originale. | Non garantire che la parola del giorno offra il contrasto didattico voluto. Lingua e tempo di ricerca riducono l’utilità nelle due ore. Non ho verificato diritti di riuso del corpus vettoriale. |

**Controllo aggiuntivo di una risorsa scartata:** ho letto l’[annuncio ufficiale Flowise](https://flowiseai.com/sunset): conferma code freeze, archivio ed EOL nelle date riportate. **Non ho invece riconvalidato tutte le altre motivazioni di esclusione**, compresi stato dei singoli Space guasti e analisi di `semantle.it`.

## 2. Errori fattuali e affermazioni da correggere

### Errori verificati

1. **Licenza di Unsloth Studio attribuita interamente ad Apache-2.0.**  
   Errato nei rapporti Locali, Agenti e System Prompt. Il [LICENSE ufficiale](https://raw.githubusercontent.com/unslothai/unsloth/main/LICENSE) separa core Apache-2.0 da Studio/CLI AGPLv3.

2. **Generalizzazione del whole-document alle knowledge base.**  
   Il default è reale, ma il [consumatore letto][U-tool] lavora sugli allegati del thread e dice esplicitamente che KB/progetti restano search-only. Anche il limite va inteso nel percorso/budget implementato, non come regola universale “ogni file sotto 6000 token entra tutto”.

3. **Cambio Rigid Mode presentato come introduzione di un system prompt rigoroso.**  
   Nel [codice quickgrid](https://huggingface.co/spaces/quickgrid/RAG-Chat-Visualizer/raw/main/index.html), `genAnswer` inserisce già l’istruzione “ONLY the provided context” quando usa contesto, indipendentemente da Rigid. Rigid interviene invece soprattutto quando manca contesto.

4. **Fallback CPU automatico di quickgrid presentato come garanzia.**  
   Il caricamento ripristina la scelta WebGPU dalla checkbox; nei catch non ritenta automaticamente la pipeline in WASM. Inoltre, se il generatore manca o fallisce, può mostrare **testo estratto dai documenti**, non una risposta generata. L’etichetta “Models Ready” non basta. Stessa [fonte](https://huggingface.co/spaces/quickgrid/RAG-Chat-Visualizer/raw/main/index.html).

5. **Prefactor usato come prova dell’esecuzione di strumenti.**  
   La [metodologia ufficiale](https://prefactor.tech/tools/prompt-injection-test) controlla la presenza del canary nella risposta: non osserva chiamate, autorizzazioni o azioni. Il laboratorio descritto non dimostra che una pressa, un ticket o un comando siano stati realmente azionati.

6. **Tiktokenizer descritto come dipendente da route edge per aggiornare i token.**  
   Il [frontend](https://raw.githubusercontent.com/dqbd/tiktokenizer/master/src/pages/index.tsx) chiama direttamente `tokenize(inputText)` nel browser. Il download di un tokenizer o il routing Next.js non sono tokenizzazione remota del testo.

7. **Account Google personale indicato come obbligatorio per AI Studio.**  
   La [guida Workspace](https://aistudio.google.com/docs/workspace) documenta l’accesso anche per account gestiti, con controlli admin ed esclusione Education under-18.

8. **HackAPrompt ridotto a una soglia uniforme di 16 anni e dataset sempre pubblico.**  
   L’[accordo partecipanti](https://www.hackaprompt.com/participant_agreement) stabilisce **18+ per la competizione**, trasferimento dei diritti e obblighi di riservatezza. La pubblicazione del dataset Pliny non prova che ogni prompt di ogni attività venga pubblicato con licenza open-source.

9. **Agent Breaker presentato senza eccezioni come no-login.**  
   Nel [bundle servito](https://play.lakera.ai/assets/index-ef5a798b.js) lo scenario `northwind_pricing_exfil` è giocabile ma richiede autenticazione. Va selezionato e provato **lo scenario specifico**, non solo il portale.

10. **Email e Teams accomunati alle capacità ottenibili con pay-as-you-go in Copilot Chat.**  
    La [matrice Microsoft](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites) mette Email/People/Teams a ❌ anche nella colonna Chat con billing: queste capacità non seguono la stessa regola di SharePoint/connettori.

11. **Prompt Airlines descritto come emissione di un biglietto “vero”.**  
    La [pagina del gioco](https://promptairlines.com/) precisa che compagnia e biglietto sono **fittizi**. È possibile osservare azioni nel sistema dimostrativo, non una prenotazione aerea reale.

12. **Termini Groq sbagliati come riferimento principale del Playground.**  
    I [termini del sito](https://groq.com/terms-of-use/) escludono Playground/GroqCloud e rinviano all’[accordo servizi](https://console.groq.com/docs/legal/services-agreement). Il risultato 18+ è confermato, ma va fondato sul documento applicabile.

### Affermazioni non dimostrate, da non trasformare in fatti

- “Nessun dato lascia la VM se Web search è spento”: insufficiente con MCP/provider remoti o altre connessioni attive.
- Tempi CPU **20–40 o 30–60 secondi**, tok/s, download e consumi RAM indicati come realistici: **non misurati sulle VM d’aula**.
- “HuggingChat Assistants disponibile dopo login”: non dimostrato. La chat corrente è online, ma non ho verificato la vecchia funzione Assistant.
- “Copilot Basic sicuramente disponibile con queste capacità”: matrice documentale ≠ entitlement, rollout e policy dello studente.
- “Copilot Notebooks perde righe perché usa un preciso top-K”: comportamento interno non provato dalle pagine lette.
- “Inferenza locale” o “client-side” come sinonimo di **zero dati raccolti dal sito**: hosting, log, CDN, cookie e analytics sono un piano diverso dal contenuto elaborato dal modello.
- “Fonte pubblica” come sinonimo di materiale liberamente caricabile in un RAG: servono diritti sul **documento**, non solo licenza del software che lo legge.

## 3. Selezione raccomandata

Queste sono **alternative e supporti**, non dodici attività da accumulare. Per due ore sceglierei un percorso unico P03 con pochi strumenti riutilizzati.

### LLM locali — massimo 3

1. **Unsloth Studio — risorsa principale.**  
   Compito: scegliere una configurazione per estrarre campi da un breve diario sintetico, definire prima i criteri di successo, provare e correggere. Misurare latenza e completezza senza aspettarsi allucinazioni.  
   **Prima dell’aula:** confermare versione, GGUF/template, parametri visibili e tempi con il numero effettivo di sessioni.

2. **Transformer Explainer — microscopio di 8–10 minuti.**  
   Le coppie prevedono come cambierà l’istogramma variando un solo parametro, poi osservano e spiegano la differenza. Non occorre ottenere testo assurdo.  
   **Prima:** caricamento e fluidità sulle postazioni, breve input inglese, controllo dei comandi.

3. **OCTOO VRAM Calculator — dimensionamento, non benchmark.**  
   Le coppie progettano una configurazione entro un budget di memoria e la rivedono cambiando contesto/concorrenza.  
   **Prima:** fissare due modelli e scenari, distinguere GB/GiB e stima GPU dalla VM CPU.

### Agenti — massimo 3

1. **Copilot Agent Builder — solo se passa il collaudo account studente.**  
   Ripartire dall’agente della lezione 3: studenti definiscono quali operazioni sono testo, quali codice e quali non autorizzate; verificano le tracce di esecuzione su dati sintetici.  
   **Prima:** accesso, creazione/modifica, Code Interpreter, salvataggio, quote e assenza di billing necessario.

2. **Prompt Airlines — alternativa breve, con uso circoscritto.**  
   Prima una richiesta legittima: le coppie mappano strumenti, argomenti e risultati. Solo successivamente propongono un test avversario e analizzano **sia successo sia rifiuto**, senza obbligo di “bucare” un livello.  
   **Prima:** provare la chat e il pannello, scenario/livello scelto, anonimato operativo, condizioni di uso e dati inviati. Nessuna tessera o informazione reale.

3. **HF Agents Course — scheda di progettazione, non installazione.**  
   Fornire una traccia documentata Thought/Action/Observation e far progettare alle coppie il controllore: quando fermare il modello, quale funzione eseguire e quale risultato reinserire.  
   **Prima:** preparare una pagina/scheda breve con attribuzione. Non chiedere agli studenti di configurare token HF o programmare.

**Non renderei obbligatorio il tool calling locale con Qwen2.5-1.5B:** la funzione esiste, ma il suo comportamento e i tempi sulla VM non sono dimostrati.

### System prompt — massimo 3

1. **Unsloth Studio — progettazione e collaudo del ruolo reale.**  
   Ogni coppia scrive istruzioni brevi per classificare eventi P03, chiedere dati mancanti e separare fonte/istruzione. Si scambiano **casi di test**, non soluzioni da copiare.  
   **Prima:** verificare persistenza del system prompt e avvio di conversazioni pulite.

2. **Tiktokenizer — visualizzare ruoli e costo del testo.**  
   Confrontare due formulazioni equivalenti e motivare quale conserva i requisiti con meno token.  
   **Prima:** tokenizer scelto e formato chat disponibili; spiegare che non è il template Qwen della VM né una misura delle prestazioni del backend.

3. **DAIR.AI in italiano — guida di consultazione.**  
   Le coppie selezionano un principio, progettano una modifica e ne confrontano gli effetti su una griglia comune.  
   **Prima:** link diretti e attribuzione MIT; niente lunga lettura o copia del meta-prompt.

### RAG — massimo 3

1. **Unsloth Studio in BM25 — risorsa principale.**  
   Corpus sintetico piccolo, risposte attese controllabili e identificatori P03/P30 espliciti. Le coppie progettano domande, ispezionano i passaggi recuperati e correggono query o documenti.  
   **Prima:** distinguere KB da allegati thread; provare top-K, auto-retrieval, citazioni e ingestione. Non richiedere il fallimento sui sinonimi.

2. **ChunkViz — rendere verificabile il chunking.**  
   Progettare un criterio concreto: ogni evento deve conservare macchina, orario, allarme e causa nello stesso blocco o in blocchi collegabili. Confrontare configurazioni e giustificare il compromesso.  
   **Prima:** runtime e testo breve preparato; chiarire che la configurazione scelta **non si trasferisce automaticamente** a Studio.

3. **Embedding Projector — estensione facoltativa breve.**  
   Confrontare vicini nello spazio originale e proiezione visiva, senza presentarlo come motore RAG.  
   **Prima:** dataset/vettori con diritti verificati, browser/WebGL, istruzioni limitate a pochi controlli. Se serve troppo setup, ometterlo.

### Attività dei rapporti da riscrivere o eliminare

- **Da eliminare nella forma proposta:** “prima il modello sbaglia i calcoli”, “produce certamente una falsa Observation”, “Rigid blocca le allucinazioni”, “BM25 fallisce sui sinonimi”, “RAG perde necessariamente righe”.
- **Da riscrivere:** gare che richiedono il superamento di livelli, attese che il modello ceda al bypass, classificazioni basate su un cluster “giusto” predeterminato.
- **Da evitare:** chiedere procedure di esclusione dei ripari della pressa. Per illustrare le priorità delle istruzioni bastano vincoli innocui su formato, fonte o richiesta di chiarimenti.
- **Troppo oneroso per due ore:** Arena con modelli aggiuntivi, conversioni GGUF, OpenCode, nuovi account multipli, tre modelli browser caricati per coppia, semantico/ibrido non già predisposto.

Una scansione realistica è: **10 minuti introduzione, 20 locale/token, 25 system prompt, 20 agenti, 30 RAG, 15 confronto e sintesi**, riutilizzando Studio e lo stesso corpus P03.

## 4. Punti aperti da verificare prima dell’aula o con account studente

1. **Versione effettiva di Studio:** confronto con i sorgenti citati; presenza e funzionamento dei controlli richiesti.
2. **VM e carico simultaneo:** RAM, CPU assegnate, condivisione del backend, tempi di ingestione e risposta con 10–12 coppie.
3. **RAG:** KB contro allegati thread, modalità whole-document, passaggi realmente recuperati, citazioni, embedding avviati anche in BM25 e comportamento dell’auto-retrieval.
4. **Esecuzione strumenti:** sandbox pronta, autorizzazioni, chiamata realmente eseguita e output osservabile; non semplice codice stampato.
5. **Account Microsoft studente:** SKU/servizi assegnati, Agent Builder, Code Interpreter, Notebooks/Workspaces, policy di condivisione e quote. **Non attivare pay-as-you-go come ripiego.**
6. **Dati Copilot:** accesso organizzativo corretto, protezioni EDP e uso della ricerca web. La [documentazione EDP](https://learn.microsoft.com/en-us/copilot/plan/enterprise-data-protection) distingue le query Bing dal perimetro Microsoft 365.
7. **Browser fisico e remoto:** WebGPU/WebGL, memoria disponibile, proxy/CDN, download e persistenza della cache. Nessuna demo WebGPU come requisito minimo finché questo non passa.
8. **Giochi selezionati:** completare una prova reale anonima della specifica sfida; verificare login, limiti per IP, raccolta prompt e termini applicabili. Per Lakera non basta aprire la homepage.
9. **Account Google eventuali:** presenza di Workspace scolastico, abilitazione admin ed età. Non imporre account personali nuovi.
10. **HuggingChat:** verificare autenticati se esista ancora il flusso Assistant proposto; fino ad allora non inserirlo nella consegna.
11. **Diritti e privacy:** corpus P03 sintetico/autoriale; niente log aziendali, credenziali, nomi operatori o manuali pubblici senza diritti verificati. Anche i servizi “no account” possono raccogliere metadati di accesso.
12. **Riuscita didattica:** ogni attività deve produrre una decisione motivata, una prova osservabile e una revisione. Il risultato corretto del modello deve essere **altrettanto utile** di quello errato.

**Scelta finale consigliata:** costruire il nucleo su **Unsloth Studio + ChunkViz**, con **Transformer Explainer o Tiktokenizer** come breve supporto e **un solo percorso agenti già verificato**. Tenere giochi, nuovi cloud e demo WebGPU fuori dal percorso obbligatorio finché non risultano provati con infrastruttura e account reali della classe.

[U-settings]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/frontend/src/features/chat/chat-settings-sheet.tsx
[U-composer]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/frontend/src/features/chat/shared-composer.tsx
[U-retrieval-ui]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/frontend/src/features/rag/components/retrieval-settings-section.tsx
[U-retrieval]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/backend/core/rag/retrieval.py
[U-config]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/backend/core/rag/config.py
[U-tool]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/backend/core/rag/tool.py
[U-ingestion]: https://raw.githubusercontent.com/unslothai/unsloth/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/backend/core/rag/ingestion.py