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
