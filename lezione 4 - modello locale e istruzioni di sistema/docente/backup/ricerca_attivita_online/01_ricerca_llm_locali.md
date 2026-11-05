# Attività interattive per la Lezione 4 — Tema: LLM locali

**Data di verifica:** 2026-11-04  
**Contesto d'aula considerato:** 20–24 studenti ITS MAKER Bologna (adulti, profili tecnici, neofiti AI/LLM), lavoro a coppie, 2 ore, approccio pratico (*imparare facendo*), caso studio della pressa industriale **"P03"** (diari di produzione e fermi macchina), disponibilità di **Unsloth Studio** su VM (spesso solo CPU con modello `Qwen2.5-1.5B` GGUF) e **Microsoft Copilot** (account scolastico Basic).

Di seguito sono presentati **9 candidati validi**, ordinati per idoneità didattica e praticità rispetto ai vincoli dell'aula.

---

## 1. Unsloth Studio (Chat locale, Parametri di generazione, Model Arena & Export GGUF)
- **Nome e URL ufficiale:** Unsloth Studio — https://unsloth.ai/docs/new/studio (Documentazione Chat: https://unsloth.ai/docs/new/studio/chat.md | Export GGUF: https://unsloth.ai/docs/new/studio/export.md | Repo: https://github.com/unslothai/unsloth)
- **Che cosa fa lo studente (interazione concreta):** Accede via browser all'interfaccia web di Unsloth Studio già attiva sulla VM d'aula; avvia una chat con il modello locale (`Qwen2.5-1.5B` GGUF), modifica manualmente i parametri di inferenza (**temperatura**, **top-p**, **top-k**), osserva in tempo reale la generazione su CPU (velocità di emissione dei token e latenza iniziale), allega file/testi come contesto locale, usa la vista **Model Arena** per confrontare due modelli/quantizzazioni fianco a fianco sullo stesso prompt ed esplora la sezione **Export** per vedere la differenza tra pesi `16-bit safetensors`, `LoRA` e `GGUF`.
- **Concetto reso visibile:** Differenza concreta tra inferenza locale (100% offline sulla VM tramite backend `llama.cpp`) e cloud (Microsoft Copilot); impatto dell'esecuzione su sola CPU in termini di **token al secondo (tok/s)**; effetto pratico di **temperatura/top-p/top-k** sulla stabilità delle risposte tecniche; significato del formato compresso **GGUF**.
- **Accesso:** **Gratis / Open-source**. Già installato sulla VM del corso (nessuna nuova installazione richiesta agli studenti, accesso via browser; nessuna API key né carta di credito). Funziona anche su sola CPU senza GPU dedicata.
- **Lingua:** Interfaccia e documentazione in **inglese** semplice; il modello `Qwen2.5-1.5B` comprende e risponde in **italiano**.
- **Termini/licenza/privacy rilevanti:** Codice rilasciato sotto licenza open-source **Apache 2.0** (verificato su https://github.com/unslothai/unsloth). L'esecuzione del modello GGUF avviene **100% in locale/offline** sulla VM senza invio di prompt a server esterni (a meno che lo studente non attivi esplicitamente il toggle *Web search* che interroga DuckDuckGo o non colleghi provider cloud esterni). Ideale per lavorare su dati industriali simulati o reali in totale privacy.
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://unsloth.ai/docs/new/studio, https://unsloth.ai/docs/new/studio/chat.md, https://unsloth.ai/docs/new/studio/export.md e https://github.com/unslothai/unsloth in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"Stress-test locale vs Cloud sul diario della Pressa P03"*. Ogni coppia riceve un estratto sintetico di 15 righe del diario di bordo della pressa P03 (con 3 fermi macchina, codici allarme e note operatore ambigue) e deve estrarre una tabella strutturata (Ora, Causa, Azione correttiva).
  1. Gli studenti eseguono il prompt su Unsloth Studio (modello locale 1.5B su CPU) con **Temperatura = 1.2** e poi con **Temperatura = 0.1**, cronometrando i secondi impiegati e annotando eventuali allucinazioni sui codici guasto.
  2. Ripetono lo stesso prompt (solo con dati sintetici!) su Microsoft Copilot (cloud).
  3. Compilano una matrice decisionale da tecnici di stabilimento: quando basta il modello 1.5B locale (privacy assoluta, zero costi ricorrenti, rete isolata) e dove soffre rispetto al modello cloud (lentezza su CPU, ragionamento complesso).
- **Rischi:** Su VM con sola CPU, se gli studenti incollano un testo troppo lungo (migliaia di token) o avviano la *Model Arena* con due modelli in sequenza, il tempo di *prefill* (lettura del prompt) può bloccare la risposta per 30–60 secondi; tenere disattivato il toggle *Web Search* per non confondere conoscenza del modello e ricerca web.

---

## 2. Transformer Explainer (Polo Club – Georgia Tech)
- **Nome e URL ufficiale:** Transformer Explainer — https://poloclub.github.io/transformer-explainer/ (Repo: https://github.com/poloclub/transformer-explainer)
- **Che cosa fa lo studente (interazione concreta):** Scrive una breve frase nella barra di input (o sceglie un esempio), regola con appositi slider la **Temperatura** ($T < 1$, $T = 1$, $T > 1$) e i filtri di campionamento **top-k** e **top-p**, e osserva dal vivo un vero modello `GPT-2 (small)` (124 milioni di parametri) in esecuzione nel proprio browser (via ONNX Runtime) che mostra passo-passo: scomposizione in token, vettori di embedding (768 dimensioni), matrici di attenzione nei 12 blocchi e grafico a barre delle probabilità (*logit* $\rightarrow$ *softmax*) per la scelta del token successivo.
- **Concetto reso visibile:** Come un LLM genera testo **un token alla volta** tramite previsione probabilistica (*next-token prediction*); perché la **temperatura** divide matematicamente i logit rendendo il modello deterministico/rigido ($T$ bassa) oppure "creativo"/instabile ($T$ alta); ruolo di `top-k` e `top-p` nel tagliare la coda dei token improbabili; esecuzione di una rete neurale direttamente nel browser.
- **Accesso:** **Gratis**, direttamente nel browser, **nessun account**, nessuna installazione, nessuna chiave API. Esegue in locale nel browser tramite JavaScript + ONNX Runtime (scarica i pesi di GPT-2 124M alla prima apertura).
- **Lingua:** Interfaccia e testo esplicativo in **inglese** (molto visivo con diagrammi interattivi). Il modello sottostante (GPT-2 124M) è addestrato prevalentemente in inglese, ma accetta qualsiasi testo in input.
- **Termini/licenza/privacy rilevanti:** Progetto accademico open-source del Georgia Institute of Technology rilasciato sotto **MIT License** (verificata su https://github.com/poloclub/transformer-explainer). L'inferenza gira interamente lato client nel browser dell'utente; nessun dato di testo viene inviato a server di inferenza esterni (presente solo telemetria statica della pagina GitHub Pages).
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://poloclub.github.io/transformer-explainer/ e https://github.com/poloclub/transformer-explainer in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"Domare la probabilità: dal delirio alla diagnosi tecnica"*. Le coppie inseriscono l'inizio di una segnalazione tecnica in inglese semplice (es. `"Industrial press P03 stopped due to hydraulic pressure"`).
  1. Portano la **Temperatura a 2.0** con `top-k` alto: osservano come l'istogramma delle probabilità si appiattisca e fanno generare 5 token, annotando come il modello scelga parole fuori contesto.
  2. Abbassano la **Temperatura a 0.2** e restringono `top-k = 5` / `top-p`: osservano il picco netto sul token più probabile (`drop`, `loss`, `failure`) e verificano la stabilità ripetendo la generazione.
  3. Aprono il pannello *Embedding* per notare come parole tecniche meno comuni vengano spezzate in più sub-token.
- **Rischi:** GPT-2 (124M) è un modello base di completamento (non un chatbot istruito) e lavora bene in inglese: se gli studenti scrivono una domanda in italiano aspettandosi una risposta da assistente, otterranno completamenti incoerenti. Va presentato come "microscopio sul motore probabilistico".

---

## 3. OCTOO AI – LLM VRAM Calculator (anche su Hugging Face Spaces)
- **Nome e URL ufficiale:** LLM VRAM Calculator — https://octooai.com/llm-vram-calculator/ (Mirror su Hugging Face Spaces: https://huggingface.co/spaces/octooai/llm-vram-calculator)
- **Che cosa fa lo studente (interazione concreta):** Seleziona un modello open-weight (tra 25 modelli reali come `Qwen3-8B`, `Qwen3-14B`, `Llama 3.1 8B`, `Llama 3.3 70B`, `Phi-4 14B`, `Gemma 3/4` oppure imposta un **Custom model** inserendo miliardi di parametri e layer), sceglie il livello di **quantizzazione** (`BF16`, `Q8_0`, `Q6_K`, `Q5_K_M`, `Q4_K_M`, `AWQ`, `Q3_K_M`, `Q2_K`), imposta la **lunghezza del contesto** (da 4k a 256k token), il **numero di richieste simultanee** (utenti in parallelo), il motore (`llama.cpp / Ollama` vs `vLLM`) e la precisione della KV cache (`16-bit` vs `8-bit`). Il calcolatore mostra istantaneamente i GiB richiesti suddivisi tra **Weights** (pesi), **KV cache** e **Runtime overhead**, e una tabella semaforica di compatibilità su schede GPU da **8 GB a 96 GB**.
- **Concetto reso visibile:** Perché i modelli grandi non entrano nei PC normali; la formula reale della memoria ($\text{Totale} = \text{Pesi} + \text{KV Cache} + \text{Runtime}$); come la **quantizzazione** (es. da 16-bit a 4-bit `Q4_K_M`) riduca di ~3–4 volte il peso del file; perché aumentare la **finestra di contesto** o gli **utenti contemporanei** fa esplodere la memoria (KV Cache) anche a parità di modello.
- **Accesso:** **Gratis**, 100% nel browser, **nessun account**, nessuna installazione, nessun requisito hardware speciale (basta JavaScript).
- **Lingua:** **Inglese**, **Tedesco** e **Spagnolo** (interfaccia numerica e tabellare intuitiva anche per chi ha un inglese base).
- **Termini/licenza/privacy rilevanti:** Codice dello Space rilasciato sotto licenza **MIT** (verificato su https://huggingface.co/spaces/octooai/llm-vram-calculator); sito gestito da OCTOO AI (Spagna, UE, conforme GDPR). La Privacy Policy ufficiale (letta su https://octooai.com/privacy/ e https://octooai.com/imprint/) dichiara esplicitamente: **zero cookie, zero analytics/tracciamento, esecuzione 100% nel browser** (*"It runs in your browser. Nothing you enter is sent anywhere"*).
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://octooai.com/llm-vram-calculator/, https://huggingface.co/spaces/octooai/llm-vram-calculator, https://octooai.com/privacy/ e https://octooai.com/imprint/ in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"Preventivo hardware per il server AI del reparto Presse"*. Il docente assegna alle coppie una sfida di progettazione industriale: l'azienda vuole installare in fabbrica un server locale per analizzare i diari della pressa P03 con un budget massimo per una singola scheda GPU da **16 GB** (o **8 GB**).
  1. La coppia deve verificare se un modello da 14B (`Qwen3-14B` o `Phi-4 14B`) in formato non compresso (`BF16`) entra nella scheda (vedranno che richiede ~30 GB $\rightarrow$ bocciato).
  2. Devono scegliere la quantizzazione giusta (`Q4_K_M` su motore `llama.cpp`) per farlo entrare in 16 GB.
  3. A questo punto il "capo reparto" chiede: *"E se 6 capi-turno interrogano il sistema contemporaneamente incollando 32.768 token di storico fermi macchina?"*. Gli studenti aumentano *Context* a `32k` e *Requests* a `6`, vedono esplodere la **KV cache** oltre i 16 GB e devono negoziare una soluzione tecnica (ridurre il contesto con RAG, attivare la KV cache a 8-bit o scendere a un modello 8B).
- **Rischi:** Il calcolatore è focalizzato sulla VRAM di una singola GPU (non simula l'offload parziale su RAM di sistema/CPU); il docente può precisare in 30 secondi che sulla VM d'aula senza GPU quegli stessi GiB vengono allocati nella RAM di sistema.

---

## 4. The Tokenizer Playground (Xenova / Transformers.js su Hugging Face Spaces)
- **Nome e URL ufficiale:** The Tokenizer Playground — https://huggingface.co/spaces/Xenova/the-tokenizer-playground (App diretta statica: https://xenova-the-tokenizer-playground.static.hf.space/index.html | Codice: https://github.com/huggingface/transformers.js)
- **Che cosa fa lo studente (interazione concreta):** Incolla un testo nella casella centrale e seleziona dal menu a tendina diversi tokenizzatori reali (tra cui `Llama`, `Gemma`, `Mistral`, `GPT-4`, `Claude`, `Command-R`, `Grok-1`, `T5`, `BERT`). L'interfaccia colora ogni singolo token con un colore alternato e mostra istantaneamente il numero totale di token e di caratteri, permettendo di confrontare come famiglie di modelli diverse spezzano lo stesso testo.
- **Concetto reso visibile:** Gli LLM non leggono né parole né lettere, ma **token** (parole intere, radici, sillabe o singoli caratteri/cifre); perché l'**italiano**, i **codici tecnici industriali** (es. `ALM_P03_HYD_404`) e i numeri consumano molti più token dell'inglese comune (impattando su velocità di generazione locale e consumo di memoria/contesto).
- **Accesso:** **Gratis**, nel browser, **nessun account** richiesto per l'uso, nessuna installazione, nessuna API key. Esegue in locale nel browser tramite `@huggingface/transformers`.
- **Lingua:** Interfaccia minimale in **inglese** (un campo di testo e un menu a tendina); supporta pienamente input in **italiano**.
- **Termini/licenza/privacy rilevanti:** Libreria Transformers.js sotto licenza **Apache 2.0** (https://github.com/huggingface/transformers.js); ospitato su Hugging Face Spaces soggetto ai Terms of Service (https://huggingface.co/terms-of-service, età minima 13 anni per eventuale creazione account) e Privacy Policy (https://huggingface.co/privacy). L'app è uno Space `static` che esegue la tokenizzazione in JavaScript nel browser dell'utente; comunque non inserire dati personali o riservati.
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://huggingface.co/spaces/Xenova/the-tokenizer-playground, https://xenova-the-tokenizer-playground.static.hf.space/index.html, https://github.com/huggingface/transformers.js, https://huggingface.co/terms-of-service e https://huggingface.co/privacy in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"La tassa linguistica e dei codici macchina"*. Ogni coppia prepara tre brevi testi relativi alla pressa P03:
  1. Una frase di guasto in inglese standard (es. `"Press P03 stopped for oil overheat at 14:30"`).
  2. La stessa frase tradotta in italiano tecnico con abbreviazioni da officina.
  3. Una riga di log grezzo piena di sigle, timestamp e numeri decimali (es. `2026-11-04T14:32:09Z | P03_PRESS_HYD | ERR_0x804F | P_bar=184.75`).
  Le coppie confrontano il conteggio token su `Llama`, `Mistral` e `GPT-4`, calcolano il rapporto *token/parola* e progettano un formato di diario di produzione "compatto per LLM" che riduca del 30% i token consumati senza perdere informazioni.
- **Rischi:** Nessun rischio tecnico; al cambio di modello nel menu a tendina il browser scarica il file `tokenizer.json` da Hugging Face (pochi MB, richiede qualche secondo la prima volta).

---

## 5. WebLLM Chat (MLC AI – LLM nel browser via WebGPU)
- **Nome e URL ufficiale:** WebLLM Chat — https://chat.webllm.ai/ (Sito progetto: https://webllm.mlc.ai/ | Repo: https://github.com/mlc-ai/web-llm e https://github.com/mlc-ai/web-llm-chat)
- **Che cosa fa lo studente (interazione concreta):** Apre la web app nel browser, sceglie un modello dalla lista integrata (es. `Qwen2-0.5B`, `Qwen2-1.5B`, `Llama-3.2-1B/3B`, `Phi-3.5`, `Gemma-2B`, tutti con indicazione della quantizzazione MLC es. `q4f16_1` o `q4f32_1`), avvia il download dei pesi nella cache del browser, **disattiva il Wi-Fi / la rete** (o apre il tab Network degli strumenti di sviluppo) e dialoga con il modello leggendo a fine risposta le statistiche di velocità (**token/s** di prefill e decoding) e modificando System Prompt e Temperatura nelle impostazioni.
- **Concetto reso visibile:** Dimostrazione "shock" di cosa significa **esecuzione locale e privacy totale**: una volta scaricati i pesi nella cache del browser, il modello risponde anche a cavo di rete scollegato; relazione diretta tra taglia del modello (0.5B vs 1.5B vs 7B), tempo di download/caricamento in memoria e velocità di generazione in token/s.
- **Accesso:** **Gratis**, 100% nel browser, **nessun account**, nessuna installazione di software, nessuna API key. **Requisito tecnico importante:** richiede un browser con supporto **WebGPU** attivo (Chrome / Edge aggiornati) e una GPU (integrata o dedicata) accessibile dal browser; scarica da ~350 MB (modelli 0.5B) a diversi GB nella cache del browser.
- **Lingua:** Interfaccia in **inglese** (con icone intuitive in stile ChatGPT); i modelli multilingua come `Qwen2` o `Llama` rispondono in **italiano**.
- **Termini/licenza/privacy rilevanti:** Codice open-source sotto licenza **Apache 2.0** (verificata su https://github.com/mlc-ai/web-llm e https://github.com/mlc-ai/web-llm-chat). Sul sito ufficiale https://webllm.mlc.ai/ è indicato che la demo `chat.webllm.ai` è per scopi di ricerca/studio nel rispetto delle licenze dei singoli modelli (Llama, Qwen, ecc.). Privacy massima: l'elaborazione avviene interamente in locale nel browser dell'utente e nessun prompt viene trasmesso a server esterni.
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://chat.webllm.ai/, https://webllm.mlc.ai/, https://github.com/mlc-ai/web-llm e https://github.com/mlc-ai/web-llm-chat in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"La prova del cavo staccato: 0.5B vs 1.5B"*.
  1. Le coppie aprono `chat.webllm.ai` sul proprio PC d'aula (usando Chrome o Edge) e selezionano il modello più piccolo (`Qwen2-0.5B` o `Llama-3.2-1B` quantizzato a 4-bit).
  2. Aprono il pannello *DevTools -> Network* del browser per verificare che, finito il caricamento, non parta alcuna chiamata di rete quando inviano un messaggio su un fermo della pressa P03.
  3. Annotano i **token/s** ottenuti sul PC locale con WebGPU e li confrontano con i **token/s** ottenuti sulla VM d'aula (solo CPU) in Unsloth Studio, toccando con mano la differenza tra accelerazione GPU e calcolo CPU.
- **Rischi:** **Rischio alto di banda e compatibilità hardware:** se 12 postazioni scaricano contemporaneamente un modello da 2–4 GB sulla stessa rete Wi-Fi dell'aula, la rete si satura; inoltre se i PC d'aula usano browser senza WebGPU o accedono solo via Desktop Remoto a una VM priva di GPU, WebLLM restituirà errore WebGPU. *Mitigazione:* far scaricare solo modelli ultra-leggeri (0.5B = ~350 MB) oppure usarlo su 2–3 PC fisici con GPU integrata/dedicata come esperimento guidato.

---

## 6. TokenCalc – VRAM Calculator & Context Window Visualizer
- **Nome e URL ufficiale:** TokenCalc — https://tokencalc.dev/ (VRAM Calculator: https://tokencalc.dev/tools/vram-calculator/ | Context Window Visualizer: https://tokencalc.dev/tools/context-window/ | Token Counter: https://tokencalc.dev/tools/token-counter/)
- **Che cosa fa lo studente (interazione concreta):** Usa due strumenti interattivi nella stessa web app:
  1. Nel **VRAM Calculator** seleziona una GPU reale consumer o Apple Silicon (es. `RTX 4060 8GB`, `RTX 3060 12GB`, `RTX 4090 24GB`, `M1 Pro 16GB`), un modello (`Llama 3.1 7B/70B/405B`, `Qwen 2.5 7B/72B`, `Phi-3 3.8B/14B`, `Mistral 7B`, `Gemma 2 9B/27B`) e la quantizzazione da `FP32` (4 B/param) fino a `Q2_K` (0.3125 B/param), vedendo quali quantizzazioni entrano nella scheda e una tabella di impatto del contesto da `0.5K` a `64K`.
  2. Nel **Context Window Visualizer** incolla un testo lungo (es. più pagine di diario della pressa P03) e vede una barra di avanzamento con soglie di allerta al 75% e 90% confrontata su decine di modelli.
- **Concetto reso visibile:** Corrispondenza diretta in **byte per parametro** di ogni sigla di quantizzazione GGUF (`FP32 = 4 B`, `FP16 = 2 B`, `Q8 = 1 B`, `Q4_K_M = 0.5625 B`, `Q2_K = 0.3125 B`); saturazione della finestra di contesto al crescere dei documenti incollati.
- **Accesso:** **Gratis**, 100% nel browser, **nessun account**, nessuna installazione, nessuna chiave API.
- **Lingua:** **Inglese** chiaro e schematico; accetta testi in **italiano** nel contatore e nel visualizzatore di contesto.
- **Termini/licenza/privacy rilevanti:** La pagina dichiara che tutti i calcoli avvengono **100% client-side nel browser** (*"Your prompts never leave your browser / No Signup / No Uploads"*); nel codice HTML è presente solo il beacon statistico anonimo di Cloudflare Web Analytics. **Nota di verifica:** i link `/privacy` e `/terms` presenti nel footer del sito restituiscono errore `HTTP 404` alla data di verifica (2026-11-04). Non inserire comunque dati personali o aziendali reali.
- **Stato verifica + pagina letta:** **PARZIALE** (Strumenti interattivi **VERIFICATI** e funzionanti; pagine legali `/privacy` e `/terms` non disponibili per HTTP 404) — Lette https://tokencalc.dev/, https://tokencalc.dev/tools/vram-calculator/, https://tokencalc.dev/tools/context-window/, https://tokencalc.dev/tools/token-counter/, https://tokencalc.dev/privacy (404) e https://tokencalc.dev/terms (404) in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"Quanti turni della pressa P03 entrano nella memoria del modello?"*.
  1. Le coppie usano il *VRAM Calculator* impostando una scheda economica da `8 GB` (`RTX 4060`) e verificano fino a quale lunghezza di contesto (`0.5K` $\rightarrow$ `64K`) un modello da 7B (`Qwen 2.5 7B`) in `Q4_K_M` riesce a restare sotto gli 8 GB prima di andare in *Out of Memory*.
  2. Poi passano al *Context Window Visualizer*, incollano il diario di un turno della pressa P03 e lo moltiplicano (1 turno, 1 settimana, 1 mese, 1 anno di log) per scoprire dopo quanti turni superano il limite fisico della finestra di contesto locale, introducendo così la necessità del **RAG** (tema successivo della lezione).
- **Rischi:** Per i modelli non-OpenAI il conteggio dei token nel *Token Counter* usa una stima basata sui caratteri ($\text{caratteri}/4$), come dichiarato nelle FAQ della pagina stessa; per vedere le differenze esatte di vocabolario tra modelli è quindi preferibile abbinarlo a *The Tokenizer Playground* (Candidato 4).

---

## 7. Tiktokenizer (Playground visuale BPE e formato Chat)
- **Nome e URL ufficiale:** Tiktokenizer — https://tiktokenizer.vercel.app/ (Repo: https://github.com/dqbd/tiktokenizer)
- **Che cosa fa lo studente (interazione concreta):** Compila o modifica i blocchi di una conversazione strutturata (`System`, `User`, `Assistant` tramite il pulsante *Add message*), attiva la spunta **Show whitespace** per rendere visibili spazi e a capo, e osserva in tempo reale sulla destra sia i **blocchi colorati dei token** sia la **sequenza di ID numerici interi** che vengono effettivamente passati al modello.
- **Concetto reso visibile:** Come una chat (incluso il *System Prompt* e i delimitatori di ruolo) venga trasformata in un unico array di numeri interi (token IDs); perché gli spazi bianchi, l'indentazione o i formati tabellari incidono sul numero di token.
- **Accesso:** **Gratis**, nel browser, **nessun account**, nessuna installazione, nessuna chiave API.
- **Lingua:** Interfaccia minimale in **inglese**; accetta qualsiasi testo in **italiano**.
- **Termini/licenza/privacy rilevanti:** Progetto open-source rilasciato sotto **MIT License** (verificata su https://github.com/dqbd/tiktokenizer). Nessuna registrazione richiesta; non incollare dati riservati.
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://tiktokenizer.vercel.app/ e https://github.com/dqbd/tiktokenizer in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"Anatomia numerica di una chat industriale"*. Le coppie usano l'editor a blocchi (`System` + `User`) per scrivere un System Prompt di istruzioni per l'assistente di manutenzione della pressa P03 e un messaggio utente con il report di guasto. Attivano *Show whitespace* e passano il mouse sui numeri interi a destra: scoprono che anche il System Prompt viene riletto e ri-tokenizzato a ogni turno di conversazione, capendo perché su un LLM locale lento su CPU un System Prompt prolisso rallenta ogni singola risposta.
- **Rischi:** L'app effettua chiamate alle proprie route edge/web per aggiornare la vista; richiede connessione internet attiva durante la prova.

---

## 8. LLM Visualization (Brendan Bycroft – Modello 3D interattivo dei pesi)
- **Nome e URL ufficiale:** LLM Visualization — https://bbycroft.net/llm (Repo: https://github.com/bbycroft/llm-viz)
- **Che cosa fa lo studente (interazione concreta):** Naviga in 3D (zoom, rotazione, spostamento col mouse) dentro l'architettura volumetrica di un LLM stile GPT; segue il walkthrough guidato passo-passo o commuta tra modelli di dimensioni diverse (`nano-gpt` da 85.000 parametri con pesi reali caricati nel browser che ordina le lettere A, B, C, fino alla struttura in scala di `GPT-2 small`, `GPT-2 XL` e `GPT-3 175B`), vedendo illuminarsi le celle dei pesi e delle attivazioni durante la generazione di un singolo token.
- **Concetto reso visibile:** Che cosa sono fisicamente i "miliardi di parametri" di un modello (enormi blocchi tridimensionali di numeri in memoria che devono essere moltiplicati a ogni singolo token generato) e perché la **velocità in token/s** dipende dalla larghezza di banda della memoria e dal numero di parametri attivi.
- **Accesso:** **Gratis**, 100% nel browser (WebGL/Canvas), **nessun account**, nessuna installazione, nessuna chiave API.
- **Lingua:** **Inglese** (ma l'interazione è principalmente spaziale/grafica in 3D).
- **Termini/licenza/privacy rilevanti:** Codice open-source rilasciato sotto **MIT License** (verificata su https://github.com/bbycroft/llm-viz). Gira interamente nel browser tramite WebAssembly/JavaScript statico senza raccolta di input utente.
- **Stato verifica + pagina letta:** **VERIFICATO** — Lette https://bbycroft.net/llm e https://github.com/bbycroft/llm-viz in data 2026-11-04.
- **Idea d'uso in aula:** *"Esplorazione in 3D: perché 1.5 miliardi di parametri pesano e rallentano la CPU"*. Attività lampo (10 minuti) a coppie prima di usare i calcolatori di VRAM: gli studenti confrontano visivamente nel modello 3D la dimensione delle matrici di `nano-gpt` (85k parametri) con quelle di `GPT-2` e `GPT-3`, individuano dove si concentrano i parametri (Embedding, Attention QKV, MLP) e deducono perché ridurre ogni cella da 16 bit a 4 bit (quantizzazione) dimezza o riduce a un quarto l'intero blocco blu dei pesi.
- **Rischi:** Non permette di inserire testo libero sulla pressa P03 (usa l'esempio precaricato `nano-gpt` per l'esecuzione live dei pesi); va usato come supporto visivo breve (5–10 min) e non per tutta l'ora.

---

## 9. llamafile (Mozilla.ai – Un intero LLM locale in un singolo file eseguibile)
- **Nome e URL ufficiale:** llamafile — https://github.com/Mozilla-Ocho/llamafile (Documentazione: https://docs.mozilla.ai/llamafile)
- **Che cosa fa lo studente (interazione concreta):** Vede (o esegue sulla VM Linux del corso / sul proprio PC) come un singolo file autosufficiente (es. `Qwen3.5-0.8B-Q8_0.llamafile`), reso eseguibile senza alcuna installazione di librerie Python o driver, avvii in pochi secondi un motore `llama.cpp` con interfaccia web locale nel browser (`localhost:8080`), pronto a rispondere offline su CPU.
- **Concetto reso visibile:** Demistificazione definitiva del concetto di "LLM locale": un modello locale non è una "magia nel cloud", ma letteralmente **un file di pesi quantizzati + un motore di calcolo C++ (`llama.cpp`)** che può stare su una chiavetta USB ed essere avviato su una macchina isolata di fabbrica.
- **Accesso:** **Gratis / Open-source**, nessun account, nessuna chiave API. **Nota installazione/esecuzione locale:** non richiede un processo di installazione (grazie a Cosmopolitan Libc è un eseguibile singolo portabile), ma richiede il download del file `.llamafile` (da ~800 MB per `Qwen3.5-0.8B-Q8_0.llamafile`) e il permesso di esecuzione locale. Su Windows i singoli file eseguibili non possono superare i 4 GB (per modelli più grandi si usa il binario `llamafile` + file `.gguf` esterno).
- **Lingua:** Interfaccia web integrata (`llama.cpp` server) in **inglese** semplice; i modelli come `Qwen` rispondono anche in **italiano**.
- **Termini/licenza/privacy rilevanti:** Progetto ufficiale Mozilla Builders / Mozilla.ai rilasciato sotto licenza **Apache 2.0** (modifiche a `llama.cpp` sotto **MIT License**, verificato su https://github.com/Mozilla-Ocho/llamafile). Esecuzione **100% locale e offline**, zero telemetria verso terzi.
- **Stato verifica + pagina letta:** **VERIFICATO** — Letta https://github.com/Mozilla-Ocho/llamafile in data 2026-11-04.
- **Idea d'uso in aula (adattabile al caso Pressa P03):** *"L'AI in chiavetta USB per la rete OT isolata"*. Il docente (o ogni coppia direttamente sulla VM Linux se il file `Qwen3.5-0.8B-Q8_0.llamafile` viene pre-copiato in una cartella condivisa prima della lezione) mostra che con due soli comandi (`chmod +x ...` e `./Qwen3.5-0.8B-Q8_0.llamafile`) nasce un chatbot locale interrogabile sul diario della pressa P03. Gli studenti confrontano la qualità di risposta di un modello da `0.8B` in `Q8_0` con il `1.5B` presente in Unsloth Studio.
- **Rischi:** Se gli studenti dovessero scaricare il file da Hugging Face durante la lezione (~800 MB a coppia), rallenterebbero la rete d'aula; funziona in modo ottimale solo se il file `.llamafile` è già pre-scaricato sulla VM o distribuito via LAN/USB.

---

## Classifica Top 3 motivata per la Lezione 4

1. **1° Posto — Unsloth Studio (già sulla VM) + Microsoft Copilot (già disponibile):**  
   *Motivazione:* Azzerano ogni attrito tecnico e di rete in aula. Usando Unsloth Studio sulla VM (CPU + `Qwen2.5-1.5B` GGUF) in parallelo a Copilot sul diario sintetico della **pressa P03**, le coppie sperimentano direttamente sulla propria pelle i 4 concetti cardine: **velocità (tok/s su CPU)**, **temperatura/parametri di generazione**, **privacy locale vs cloud** e **limiti di capacità di un modello piccolo quantizzato (1.5B)**.
2. **2° Posto — OCTOO AI LLM VRAM Calculator (`octooai.com/llm-vram-calculator`):**  
   *Motivazione:* È lo strumento browser-based più chiaro, rigoroso e rispettoso della privacy (zero cookie, zero invio dati, licenza MIT) per trasformare i concetti astratti di **dimensione del modello (B)**, **quantizzazione (`BF16` vs `Q8` vs `Q4_K_M`)** e **impatto del contesto/utenti sulla memoria (KV Cache)** in un vero esercizio di dimensionamento hardware da tecnici industriali, senza dover scaricare decine di gigabyte di modelli.
3. **3° Posto — Transformer Explainer (`poloclub.github.io/transformer-explainer`) + The Tokenizer Playground (`Xenova/the-tokenizer-playground`):**  
   *Motivazione:* In coppia coprono perfettamente il "dietro le quinte" nel browser senza login né installazioni: *The Tokenizer Playground* fa toccare con mano come il testo italiano e le sigle dei fermi macchina della pressa P03 vengano spezzati in **token** da Llama/Mistral/GPT-4, mentre *Transformer Explainer* fa vedere dal vivo su un modello reale nel browser come **temperatura, top-k e top-p** modifichino le probabilità del prossimo token.

---

## Lista risorse scartate (con motivazione in una riga)

- **LMArena / Arena AI (`https://lmarena.ai/` / `https://arena.ai/`)**: Scartata perché esegue modelli in cloud e i prompt inseriti dagli utenti vengono registrati e resi pubblici per il benchmark/addestramento, violando il criterio sulla riservatezza e non mostrando il funzionamento locale.
- **OpenAI Tokenizer (`https://platform.openai.com/tokenizer`)**: Scartata perché legata alla console sviluppatori cloud di OpenAI e limitata ai soli modelli proprietari GPT, risultando meno didattica e flessibile rispetto a *The Tokenizer Playground* (che include Llama, Gemma e Mistral) e *Tiktokenizer*.
- **LM Studio (`https://lmstudio.ai/`)**: Scartata perché richiede un'installazione desktop pesante, è software proprietario closed-source (Termini v. 23/08/2026 con spinta alla creazione di account e funzioni cloud "Bionic") ed è ridondante rispetto a Unsloth Studio già installato sulla VM.
- **Ollama (`https://ollama.com/`)**: Scartata per l'attività pratica di 2 ore perché richiede installazione di sistema/CLI con privilegi amministrativi ed è ridondante avendo già Unsloth Studio (basato anch'esso su `llama.cpp`) pronto sulla VM d'aula.
- **Jan (`https://jan.ai/`)**: Scartata perché richiede l'installazione di un client desktop nativo e il download locale di diversi GB di modelli su ogni postazione, poco sostenibile in 2 ore su VM con risorse limitate.
- **GPT4All (`https://www.nomic.ai/gpt4all`)**: Scartata perché richiede installazione desktop nativa su ogni macchina e le sue funzioni locali (esecuzione GGUF e RAG locale) sono già coperte senza installazioni aggiuntive da Unsloth Studio sulla VM.
- **SmolLM WebGPU Space (`https://huggingface.co/spaces/HuggingFaceTB/SmolLM2-1.7B-Instruct-WebGPU`)**: Scartata in favore di *WebLLM Chat* perché carica un unico modello fisso (`SmolLM-360M-Instruct`) senza controlli sui parametri di generazione né scelta della quantizzazione.