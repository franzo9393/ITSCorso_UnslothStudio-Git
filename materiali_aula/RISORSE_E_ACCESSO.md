# Risorse e accesso · Unsloth Studio al centro

## 1. Regola di scelta

Il modulo esplora Unsloth Studio come prodotto: inferenza/chat, documenti/RAG, dataset, personalizzazione, valutazione, export e integrazioni. Una risorsa esterna chiarisce o confronta un concetto, non sostituisce Studio. Nessun deployment obbligatorio sulle macchine degli studenti; nessun acquisto o account esterno necessario per completare il percorso guidato.

**Gratuito non significa compute garantito, accesso anonimo, disponibilità continua o autorizzazione a caricare documenti aziendali.** Solo dati sintetici. Le fonti sotto sono documentazione di riferimento; il loro accesso con rete/account dell'istituto e il carico d'aula vanno verificati prima dell'erogazione.

## 2. Selezione di risorse

| Risorsa | Impiego | Accesso e limiti | Ruolo nel modulo |
| --- | --- | --- | --- |
| [Panoramica Studio](https://unsloth.ai/docs/new/studio) | Mappa del prodotto in B1: eseguire, preparare dati, addestrare, esportare. | Documentazione pubblica; esecuzione richiede infrastruttura. Non trasferire in aula le promesse prestazionali upstream. | Riferimento principale. |
| [Studio: percorso guidato](https://unsloth.ai/docs/new/studio/start) | B2/B5: modello, dataset, anteprima, training, valutazione ed export. | Menu e capacità dipendono dalla release; usare schermate della versione qualificata. | Riferimento operativo docente. |
| [Chat e documenti](https://unsloth.ai/docs/new/studio/chat) | B2–B4: contesto, inferenza, corpus e fonti. | Documentazione non prova di recupero osservabile sul sistema d'aula. | Laboratorio principale. |
| [Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe) | B5: dai documenti agli esempi, controlli sulla qualità dei dati sintetici. | Generazione può richiedere modelli, risorse e servizi; leggere configurazione e costi prima. | Esplorazione, non generazione obbligatoria. |
| [Export](https://unsloth.ai/docs/new/studio/export) | B5: differenza fra dati, adapter e modello esportato. | Hardware, formato e runtime di destinazione vanno verificati; esportare non garantisce eseguibilità ovunque. | Walkthrough o demo qualificata. |
| [API](https://unsloth.ai/docs/basics/api) e [OpenCode](https://unsloth.ai/docs/integrations/opencode) | Collegare Studio a un'applicazione o agente. | Credenziali, permessi, tool e backend aggiungono rischi; nessun tool su sistemi reali. | Potenzialità in B1/B5; laboratorio solo nell'estensione scelta. |
| [Notebook Studio ufficiale su Colab](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb) | Esplorazione personale facoltativa dopo il corso. | Account, runtime, download, quote e compatibilità; risorse non garantite. Le [FAQ Colab](https://research.google.com/colaboratory/faq.html) limitano l'uso gratuito principalmente tramite UI web esterna al notebook. La presenza del notebook ufficiale non deroga alle policy Colab. | Non infrastruttura base né fallback automatico. |
| [Hugging Face: schede modello](https://huggingface.co/docs/hub/model-cards) | Leggere compito, licenza, limiti e condizioni d'uso prima di scegliere un modello per Studio. | Pesi gated possono richiedere account e accettazione licenza; niente download casuali in aula. | Breve lettura guidata. |
| [Google ML Crash Course: embedding](https://developers.google.com/machine-learning/crash-course/embeddings) | Esempio qualitativo di somiglianza e rappresentazione. | Il modulo completo presuppone nozioni ML: selezionare figure e spiegazioni, non assegnarlo integralmente. | Supporto concettuale facoltativo. |
| [NotebookLM / Gemini Notebook](https://support.google.com/notebooklm/answer/16164461?hl=en) | Un esempio di prodotto documentale, confronto sulle citazioni. | Account, abilitazione amministratore per account gestiti e [quote variabili](https://support.google.com/gemininotebook/answer/17670842?hl=en). Citazioni non equivalgono a osservazione completa del recupero. | Confronto facoltativo breve; non fulcro o sostituto della sandbox Unsloth. |
| [Learn Git Branching](https://learngitbranching.js.org/) | Visualizzare checkpoint e cronologia, se utile. | Simulatore: non salva i veri file del laboratorio; evitare il percorso completo sul branching. | Accessorio, non requisito della consegna. |

Non assegnare il catalogo aperto di Hugging Face Spaces come attività libera: una demo terza può cambiare, essere indisponibile o avere policy inadeguate. Eventuali demo vanno selezionate dal docente, aperte tramite link diretto e provate con dati sintetici; nessun servizio esterno è necessario per superare il modulo.

## 3. Modalità di erogazione

| Modalità | Organizzazione | Evidenza da registrare |
| --- | --- | --- |
| ESEGUITO_STUDENTE | Sandbox Unsloth separate o turni su postazioni qualificate. | Coppia, ambiente, domanda, risposta, fonti, versione e giudizio. |
| OSSERVATO_DOCENTE | Un ambiente Unsloth proiettato; coppie propongono prompt, prevedono e verificano. | Esperimento osservato e motivazione personale; non dichiarare uso autonomo. |
| ANALISI_CASO | Corpus e tracce di vere esecuzioni Studio preparate prima; anche su carta. | Identificativo/data della traccia, parti visibili, diagnosi e limiti. |

Modalità e giudizio sono indipendenti: una risposta errata osservata può essere diagnosticata bene. Una prova mai eseguita né documentata non ha un output da giudicare. Lasciare NON_ESEGUITO ed esprimere separatamente cosa ci si aspetta dalle fonti.

**Browser non significa compute assente:** l'inferenza deve girare su una macchina qualificata. Non presumere isolamento multiutente di un'istanza condivisa; HTTPS e login da soli non dimostrano separazione di file e chat. Se l'isolamento non è verificato, adottare turni su ambiente docente o istanze distinte predisposte dal tecnico.

### 3.1 Indirizzo operativo: VM locali con risorse limitate

La configurazione preferita per il laboratorio pratico è **Unsloth Studio installato nella VM di ogni studente**, con lavoro anche a coppie e ruoli alternati. Non è sufficiente la sola dimostrazione del docente per attestare uso autonomo. Questa è una scelta di predisposizione da collaudare, non una configurazione già qualificata: le modalità guidata e di analisi restano distinte e non sostituiscono implicitamente l'attività pratica.

**Vincolo prioritario: specifiche di sistema molto limitate.** Dimensionare sulla VM effettiva, non sul PC host. La GPU dell'host non è automaticamente disponibile nella VM: senza passthrough o vGPU verificati, progettare la prova per CPU. Rilevare sistema operativo/architettura, vCPU, CPU host, RAM assegnata, spazio libero, eventuale GPU accessibile e memoria video, numero di VM concorrenti e risorse complessive dell'host. Non fissare requisiti minimi o tempi garantiti prima della misura.

#### Configurazione minima da provare

| Componente | Scelta di collaudo |
| --- | --- |
| Inferenza | Un solo piccolo modello instruct GGUF quantizzato, già scaricato; primo candidato Qwen2.5-1.5B-Instruct Q4_K_M, non scelta definitiva né garanzia di qualità sul corpus. |
| Recupero | RAG lessicale nativo di Studio, modalità **BM25 only**; non presumere necessario un database vettoriale esterno. |
| Corpus | I cinque piccoli documenti Markdown del corso; niente scansioni, OCR, immagini o grandi manuali nella prova iniziale. |
| Passaggi | Partire da due passaggi; verificare le domande a più fonti e aumentare solo entro il contesto disponibile. |
| Contesto e risposte | Contesto corto e controllato, risposte brevi con dato/fonte/limite, nuove chat per confronti indipendenti. |
| Funzioni escluse dal laboratorio minimo | Ricerca web, esecuzione di codice, vision, generazione massiva di dataset e training. |
| Distribuzione | Stessa versione Studio e stessi modelli/materiali; installazioni e download completati prima della lezione. |

BM25 più generazione è RAG anche senza ricerca vettoriale: seleziona passaggi in base ai termini e li fornisce al modello. È adatto a sperimentare codici esatti e termini presenti; sinonimi e parafrasi sono un limite da misurare, non una capacità semantica garantita. L'embedding è distinto dall'LLM generativo e serve se si adotta il recupero vettoriale. Il predefinito inglese non è automaticamente adeguato al corpus italiano; cambiando spazio di embedding occorre ricostruire i vettori.

**Punto aperto decisivo:** il selettore `BM25 only` riguarda la ricerca e non dimostra che il caricamento/indicizzazione eviti il modello di embedding. Verificare dipendenze caricate, memoria e tempi lungo tutto il percorso. Non dichiarare già disponibile un RAG leggero senza embedding. Le impostazioni vanno controllate nella release installata: il codice upstream esaminato non è una prova di esecuzione sulla VM.

Per osservare davvero il recupero, verificare anche che Studio non inserisca integralmente i piccoli documenti nel contesto. La configurazione upstream esaminata espone `RAG_THREAD_WHOLE_DOC=0` per disabilitare tale comportamento; verificarne l'effetto sul percorso adottato. Citazioni o badge delle fonti, da soli, non dimostrano tutti i passaggi forniti al modello.

#### Attività studente e accettazione

Gli studenti creano una knowledge base locale, caricano il corpus, attendono l'indicizzazione e la selezionano nella chat. Confrontano una domanda senza fonti e con recupero, controllano codici P03/P30, numeri e dato assente; conservano risposta e fonti, distinguendo recupero e generazione solo quando osservabili. Confrontano poi rev1/rev2 in nuove chat, selezionando soltanto la raccolta pertinente; due raccolte separate sono una prima modalità di confronto controllabile.

Restano pratiche anche la progettazione di istruzioni, la classificazione con pochi esempi nel prompt e un caso di verifica escluso dagli esempi, la correzione documentale e lo scambio di un nuovo documento sintetico tra coppie. Non confondere esempi nel prompt con fine-tuning, né testo incollato nel contesto con recupero RAG. Un GGUF funzionante in inferenza non prova capacità di addestramento della VM.

Prima di replicare l'immagine, provare su **una VM pilota con le risorse effettive degli studenti**:

- [ ] Avvio Studio e caricamento del piccolo modello; risposta breve in italiano.
- [ ] Creazione della knowledge base e indicizzazione dei cinque documenti; osservazione di memoria, tempi e componenti caricati, anche in modalità BM25.
- [ ] Recupero su codice esatto, domanda a più fonti e dato assente; verifica di passaggi effettivamente consultabili e risposta fedele.
- [ ] Aggiornamento catalogo e ripetizione della domanda senza contaminazione da chat o raccolte precedenti.
- [ ] Prova con tutte le VM concorrenti: misurare attese e pressione sulle risorse dell'host, non soltanto la singola VM isolata.

Se Studio resta troppo pesante, cambiare soltanto LLM potrebbe non bastare. Un recuperatore BM25 esterno collegato all'inferenza è un'architettura alternativa da concordare esplicitamente, non un'aggiunta implicita. Se il RAG non supera il collaudo, non dichiararlo attività autonoma garantita e non sostituirlo silenziosamente con allegati integrali o dimostrazione docente.

Riferimenti della valutazione tecnica, non attestazioni di collaudo:

- [Controlli nativi di recupero: BM25, hybrid, top K e recupero automatico](https://github.com/unslothai/unsloth/blob/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/frontend/src/features/rag/components/retrieval-settings-section.tsx).
- [Knowledge base e caricamento documenti](https://github.com/unslothai/unsloth/blob/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/frontend/src/features/rag/components/knowledge-base-dialog.tsx).
- [Configurazione embedding e contesto a documento intero](https://github.com/unslothai/unsloth/blob/46c3bbbdf6ebf6098b22d5fb9953ea55c5ed1dfc/studio/backend/core/rag/config.py).
- [Modello candidato e quantizzazioni ufficiali](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF).

### 3.2 Copilot Basic disponibile agli studenti: confronto cloud da qualificare

Gli studenti dispongono anche di **Microsoft Copilot con licenza indicata come Basic**, secondo quanto comunicato dalla scuola. Questo conferma la disponibilità dichiarata del prodotto, non le singole funzioni del tenant. Distinguere le etichette `Copilot Chat (Basic)` e `Microsoft 365 Copilot (Basic)`: integrazione nelle applicazioni Office, accessi e limiti dipendono da licenze e configurazione. Usare account scolastici, non personali.

Copilot può affiancare il percorso Unsloth locale per attività che non consumano risorse di inferenza nella VM, ma richiedono rete e servizio cloud. Non sostituisce implicitamente il laboratorio locale né garantisce disponibilità continua: upload e altre funzioni con accesso standard sono soggetti alla capacità del servizio. Usare soltanto i dati sintetici del corso; non introdurre account esterni o acquisti obbligatori.

#### Blocchi appunti: prima opzione documentale da provare

Si intendono i **Copilot Notebooks**, non i normali blocchi di OneNote. Valutarli per una raccolta persistente delle fonti del caso d'officina, interrogazione dei documenti e confronto tra revisioni. **Disponibilità agli studenti Basic non ancora verificata.** La pagina Microsoft sui requisiti consultata presenta indicazioni non perfettamente allineate: la tabella cita una licenza Microsoft Copilot, mentre il testo cita Microsoft Copilot o Copilot Chat. Le policy del tenant possono inoltre disabilitare i Notebooks. Non promettere accesso sulla sola base del nome della licenza o della presenza della voce nel menu.

Se il collaudo riesce, ogni coppia crea un blocco dedicato, aggiunge le fonti nei formati effettivamente supportati, interroga un dato presente e uno assente, controlla i riferimenti e confronta rev1/rev2 chiaramente identificate. Registra domanda, risposta fedele, fonte e giudizio. Presentare l'attività come **interrogazione documentale e verifica delle fonti**: non presumere accesso a embedding, chunking, ranking o all'intera traccia di recupero.

#### Agenti: distinguere istruzioni da conoscenza documentale

| Capacità | Copilot Chat senza fatturazione a consumo |
| --- | --- |
| Istruzioni personalizzate e ricerca web pubblica | Previste nella matrice Microsoft, con limiti d'uso; verificare creazione, utilizzo e policy per gli account studenti. |
| Conoscenza su SharePoint o file incorporati nell'agente | Non inclusa nella configurazione senza fatturazione a consumo descritta dalla matrice; richiede licenza appropriata o abilitazione a consumo, oltre alle policy. |

La presenza di **Agenti** non prova che si possa creare gratuitamente un assistente sul corpus dell'officina. Non confondere allegare un file alla chat con configurarlo come conoscenza permanente dell'agente. Non attivare Copilot Credits, fatturazione a consumo o nuove sottoscrizioni per aggirare il limite senza autorizzazione.

Se la creazione è abilitata, un esercizio compatibile da valutare è un agente classificatore GUASTO/MANUTENZIONE/INFORMAZIONE basato su istruzioni: definizione delle categorie, casi nuovi, analisi degli errori e revisione delle istruzioni. Non chiamarlo RAG documentale o fine-tuning.

#### Attività comuni e GO Copilot

Riutilizzare corpus, domande e scheda delle evidenze del laboratorio locale: miglioramento delle istruzioni, estrazione di macchina/evento/durata con campi assenti espliciti, controllo P03/P30, confronto revisioni e classificazione con casi esclusi dagli esempi. Per il confronto Copilot–Unsloth mantenere domanda e dati uguali, dichiarando che si confrontano sistemi diversi e non si isola la qualità del solo modello.

Prima di inserire le attività nel programma, collaudare con **un account studente Basic reale**, non soltanto docente o amministratore:

- [ ] Registrare etichetta/licenze effettive, accesso con account scolastico e policy applicate.
- [ ] Provare upload e analisi di due documenti sintetici, formati ammessi, riferimenti, dato assente e limiti del servizio.
- [ ] Verificare creazione di un Notebook, aggiunta delle fonti e interrogazione riferita ai documenti; distinguere semplice visibilità della funzione da uso riuscito.
- [ ] Verificare separatamente creazione/utilizzo degli agenti e sorgenti consentite, specificando eventuali costi aggiuntivi senza abilitarli.
- [ ] Per esperimenti solo documentali, verificare il controllo della ricerca web con i tecnici: una richiesta nel prompt non garantisce che il web sia escluso.
- [ ] Registrare cosa è davvero osservabile; non giudicare il recupero dalla sola presenza di citazioni.

Se i Notebooks non sono disponibili, la chat con allegati resta un'attività distinta, da verificare e dichiarare; non presentarla come knowledge base persistente. Il NO-GO Copilot non autorizza a dichiarare eseguite le attività né elimina la necessità di qualificare Unsloth.

Fonti ufficiali consultate per queste considerazioni; accesso del tenant scolastico non ancora provato:

- [Copilot Chat: Basic, funzionalità e accesso standard](https://learn.microsoft.com/en-us/copilot/overview).
- [Requisiti dei Copilot Notebooks](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-requirements) e [policy amministrative](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration).
- [Capacità degli agenti e modelli di licenza](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models).
- [Agent Builder e controlli di accesso](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder).
- [Account scolastici e controllo amministrativo della ricerca web](https://learn.microsoft.com/en-us/copilot/manage).


## 4. Checklist prima dell'aula

### Percorso guidato: requisito minimo

- [ ] Studio docente provato; modello, embedding e dati già disponibili; versioni congelate.
- [ ] B2–B4 e B6 provati: chat/contesto, recupero visibile, revisione, nuovo documento e dato assente.
- [ ] B5 preparato: schermate reali del percorso dati/training/valutazione/export; distinguere cosa è stato eseguito da cosa è illustrato.
- [ ] Pacchetto offline di continuità distribuito: fonti rev1/rev2, tracce input/passaggi/output, schermate e schede; privo di credenziali.
- [ ] Prova senza rete: corpus e casi leggibili, nessun login necessario per lavorare sulle evidenze.
- [ ] Tempi della sequenza misurati su un gruppo pilota; nessuna attesa tecnica senza attività alternativa.

### Sandbox: GO aggiuntivo

- [ ] URL e browser dalla rete studente provati; account e policy dell'istituto approvati.
- [ ] Separazione chat/file, autorizzazioni e ripristino provati; nessuna credenziale amministrativa condivisa.
- [ ] Carico atteso e tempi misurati; turni definiti se le risorse non bastano.
- [ ] Nessuna esposizione pubblica improvvisata o inoltro di porte senza controllo tecnico.
- [ ] Pulizia dati e revoca accessi a fine laboratorio; nessun dato personale/aziendale nei servizi esterni.

### Training: GO aggiuntivo indipendente

- [ ] Modello e licenza adatti, formato addestrabile, dataset verificato, casi di valutazione separati.
- [ ] Hardware, durata, spazio disco, adapter/export e caricamento di verifica provati.
- [ ] Risultati e limiti conservati; nessuna deduzione di qualità dalla sola loss o da tre esempi.

Il NO-GO sandbox/training lascia praticabile il percorso guidato, con i limiti dichiarati sulle abilità esercitate. Se manca anche l'ambiente docente qualificato in preparazione con il pacchetto di evidenze, non dichiarare il corso pronto: non basta avere link a servizi gratuiti.

## 5. Pacchetto di continuità da preparare, non già incluso

Il repository include corpus, consegne e strumenti di supporto, ma non pesi, immagine macchina qualificata o tracce AI registrate. Per ogni caso il docente deve conservare:

1. ID, data, versione Studio, modello/embedding, impostazioni essenziali e corpus/revisione.
2. Domanda e istruzioni; stato iniziale della chat.
3. Passaggi effettivamente visibili e risposta fedele, anche se errata.
4. Fonte completa consultabile e giudizio motivato; limiti di osservabilità.
5. Per B4, prima/dopo e domanda di controllo; per B5, dataset e caso escluso dal training.

Non sostituire le risposte osservate con le soluzioni della guida. Screenshot ufficiali illustrano funzioni, non certificano che il laboratorio sia stato eseguito sul proprio ambiente.
