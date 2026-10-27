# Slide 01 – Copertina

**Digitalizzare i processi con l'Intelligenza Artificiale**  
*Lezione 2 · Tecniche di prompting d'officina e guida operativa degli LLM*

ITS MAKER Bologna · Tecnico Superiore per la Digitalizzazione dei Processi Industriali

- Dalla teoria alla pratica a coppie (Driver & Tester).
- Il prompt come dima di processo: specificare, guidare, controllare.
- 4 micro-sfide hands-on su dati reali d'officina.
- Nessuna programmazione richiesta: linguaggio naturale e collaudo visivo.

> **Regia docente:** Aula pronta a coppie con una finestra di chat aperta (ChatGPT, Claude o sandbox locale). Proiettare le slide delle sfide durante i 10 minuti di lavoro autonomo.

---

# Slide 02 – Il piano di oggi: la regola del «10 – 10 – 5»

| Fase | Minuti | Cosa facciamo |
| :--- | :---: | :--- |
| **Micro-lezione** | 5–7 min | Presentiamo un solo problema reale d'officina e vediamo l'errore tipico dell'AI a video. |
| **Sfida a coppie** | 10–12 min | Lavorate al computer a ruoli alternati: 1 persona scrive il prompt, 1 persona collauda l'esito. |
| **Debrief collettivo** | 5 min | Proiettiamo i risultati, discutiamo cosa ha funzionato e fissiamo la regola d'oro. |

Le 4 sfide di oggi:
1. **Formato e vincoli:** fermare la logorrea dell'AI per inserire dati nel gestionale.
2. **Few-shot pratico:** dare 1 esempio per fissare lo standard senza scrivere pagine di regole.
3. **Passaggi intermedi (CoT):** evitare errori nei calcoli di tempi e costi di fermo.
4. **Bloccare l'allucinazione:** insegnare all'AI a dire "non lo so" quando il dato manca.

---

# Slide 03 – Il nostro pezzo grezzo: il rapporto di fermo

Per tutte le prove di oggi lavoriamo su questo rapporto d'officina (DOC-FERMO):

```text
Rapporto del 14 Ottobre (DOC-FERMO):
Ore 14:20: la pressa P03 si è fermata per sovratemperatura dell'olio idraulico. Temperatura registrata: 78 °C. Soglia: 65 °C. Sostituito il filtro intasato con il ricambio FLT-992.
Fermo macchina totale: 45 minuti.
```

- Copiatelo nella vostra finestra di chat.
- Sarà il testo di base su cui testeremo i nostri prompt.

---

# Slide 04 – Sfida 1: «Basta chiacchiere» (Il problema)

### Il problema reale nei processi aziendali
Se chiedete all'AI: *«Riassumimi cosa è successo alla macchina»*, cosa succede?
- L'AI risponde con 3 paragrafi di testo discorsivo.
- Inizia con: *«Certamente! Ecco un riassunto dettagliato del fermo macchina avvenuto...»*.
- Conclude con: *«Spero che questo ti sia utile! Fammi sapere se desideri altre informazioni.»*.

**Perché è un problema?**  
Nessun gestionale aziendale (MES o ERP) può digerire un testo del genere. Serve un dato strutturato in tabella o campi predefiniti, senza "chiacchiere".

---

# Slide 05 – Sfida 1: Al lavoro (10 minuti)

### Consegna per la coppia:
1. **Tentativo A (senza vincoli):** Chiedete all'AI di riassumere il fermo con parole vostre. Osservate la prolissità.
2. **Tentativo B (con vincoli rigidi):** Riscrivete il prompt imponendo:
   - **Campi richiesti:** Macchina, Causa fermo, Durata minuti, Codice ricambio.
   - **Formato:** Solo una tabella a 4 colonne.
   - **Vincolo negativo:** *Nessun saluto, nessuna premessa, nessuna spiegazione prima o dopo la tabella.*

> **Compito del Collaudatore:** Controlla che il modello abbia obbedito al vincolo negativo. Ha scritto testo prima della tabella? Segnalalo!

---

# Slide 06 – Sfida 1: Debrief & Regola 1

```
              ┌────────────────────────────────────────────────┐
SENZA VINCOLI │ «Certamente! Ecco il riassunto... (3 paragrafi)»│
              └────────────────────────────────────────────────┘
                                     ▼
              ┌────────────────────────────────────────────────┐
CON VINCOLI   │ | Macchina | Causa        | Durata | Ricambio  |│
              │ | P03      | Sovratemp.   | 45 min | FLT-992   |│
              └────────────────────────────────────────────────┘
```

### 💡 Regola d'oro 1:
> **Il prompt è una dima: se non fissi i confini e i vincoli negativi, l'AI riempie lo spazio con convenevoli inutilizzabili per un processo industriale.**

---

# Slide 07 – Sfida 2: «Un esempio vale 1000 parole» (Il problema)

### Il problema: spiegare lo stile è difficile
Vogliamo registrare il fermo in una riga compatta per il bollettino di manutenzione.  
Se chiedete: *«Scrivi una riga breve, sintetica e tecnica per il registro manutenzione»*, ogni coppia otterrà qualcosa di diverso:
- Coppia 1: *«14/10/2026 - P03 ferma 45 min guasto olio.»*
- Coppia 2: *«Fermo P03: temperatura 78C, ricambio FLT-992.»*
- Coppia 3: *«P03 (45 minuti) - Allarme temperatura - Filtro sostituito.»*

Come facciamo a imporre uno standard rigoroso e uniforme per tutti i turni di lavoro?

---

# Slide 08 – Sfida 2: Al lavoro (10 minuti)

### Usare il Few-Shot (fornire 1 esempio già risolto)
Riscrivete il prompt fornendo **un modello di riferimento**:

> *«Crea una riga di registro manutenzione seguendo ESATTAMENTE lo stile di questo esempio:*  
>  
> *Esempio: [Linea 1] 20 min | BLOCCO NASTRO | RICAMBIO: CINGHIA-B12*  
>  
> *Ora genera la riga per il rapporto allegato della pressa P03.»*

> **Compito del Collaudatore:**  
> Controlla se il modello ha rispettato parentesi quadre `[]`, barre verticali `|`, maiuscole e ordine delle informazioni dell'esempio.

---

# Slide 09 – Sfida 2: Debrief & Regola 2

### Perché il Few-Shot vince sulle spiegazioni lunghe?

| Approccio | Prompt | Risultato |
| :--- | :--- | :--- |
| **Zero-Shot (solo teoria)** | *«Sii conciso, usa parentesi e barre, non mettere date, usa lo stile d'officina...»* | Spesso ignora 1 o 2 regole. |
| **Few-Shot (1 esempio)** | *«Segui questo schema: [L1] 20m \| GUASTO \| RICAMBIO: X»* | **Imita la struttura al 100% al primo colpo.** |

### 💡 Regola d'oro 2:
> **Non perdere tempo a spiegare lo stile a parole: mostra all'AI 1 o 2 esempi pratici di input/output. Gli LLM imparano per imitazione di pattern.**

---

# Slide 10 – Sfida 3: «La calcolatrice che sbaglia» (Il problema)

### L'illusione della calcolatrice
Molti credono che gli LLM siano calcolatori elettronici. **Falso.**  
Un LLM prevede parole e numeri probabili, non esegue calcoli su un circuito aritmetico.

### Il caso pratico d'officina:
- Tariffa di fermo impianto aziendale: **160 €/ora**.
- La pressa P03 è rimasta ferma per **45 minuti**.
- Quanto è costato il fermo all'azienda?

*Attenzione:* 45 minuti NON sono 0,45 ore!  
45 minuti = 0,75 ore ($45 / 60$). Il costo esatto è $0{,}75 \times 160\text{ \euro} = \mathbf{120\text{ \euro}}$.

---

# Slide 11 – Sfida 3: Al lavoro (10 minuti)

### Test 1 — La risposta secca:
> *«Il costo di fermo è 160 €/ora. Dal rapporto allegato calcola il costo totale del fermo della P03. Rispondi subito con la sola cifra finale in euro.»*  
*(Cosa ha risposto il modello? Ha sbagliato o ha indovinato?)*

### Test 2 — Forzare i passaggi (Chain of Thought):
> *«Calcola il costo del fermo spiegando prima i passaggi intermedi:*  
> *1. Minuti totali di fermo estratti dal testo.*  
> *2. Conversione dei minuti in ore decimali (minuti / 60).*  
> *3. Moltiplicazione ore decimali per tariffa oraria (160 €/ora).*  
> *4. Cifra finale in euro.»*

> **Compito del Collaudatore:** Calcolatrice alla mano, verifica se il passaggio 2 e 3 tornano matematicamente.

---

# Slide 12 – Sfida 3: Debrief & Regola 3

```
DOMANDA DIRETTA   ──►  L'AI "spara" un numero a intuito linguistico  ──► RISCHIO ERRORE
                                                                        (es. 0.45 × 160)
PASSAGGI FORZATI  ──►  45 min  ──►  45/60 = 0.75 h  ──►  0.75 × 160  ──► 120 € ESATTI!
```

### 💡 Regola d'oro 3:
> **L'AI "pensa con i token che scrive". Se le chiedi solo il numero finale, non ha spazio computazionale per elaborare la logica. Chiedi sempre i passaggi intermedi (Chain-of-Thought).**

---

# Slide 13 – Sfida 4: «Il test del trabocchetto» (Il problema)

### La trappola peggiore dell'AI: l'Allucinazione
Gli LLM sono addestrati per essere gentili e dare sempre una risposta.  
Se fate una domanda su un dato che non conoscono o che non c'è nel testo, **tendono a inventare una risposta plausibile pur di non deludervi**.

In un processo industriale o su una macchina:
- Un ricambio inventato ordina il pezzo sbagliato.
- Una procedura inventata può causare incidenti di sicurezza.

---

# Slide 14 – Sfida 4: Al lavoro (10 minuti)

### Nel rapporto DOC-FERMO NON c'è il nome dell'operatore!

1. **Il tranello (domanda aperta):**  
   > *«Chi è l'operatore che ha effettuato la sostituzione del filtro della P03?»*  
   *Cosa risponde l'AI?* Prova a dedurre un nome o usa frasi vaghe?

2. **La clausola di sicurezza (paracadute):**  
   > *«Chi è l'operatore che ha effettuato l'intervento?*  
   > *Regola tassativa: Rispondi basandoti ESCLUSIVAMENTE sulle informazioni scritte nel testo.*  
   > *Se l'informazione non è presente o non è certa, rispondi testualmente con: 'DATO NON PRESENTE'. Non inventare nulla.»*

> **Compito del Collaudatore:** Il modello ha ammesso il limite o ha continuato a inventare scuse?

---

# Slide 15 – Sfida 4: Debrief & Regola 4

```
TRABOCCHETTO      ──►  «Chi è l'operatore?»  ──► «Il tecnico specializzato...» (Invenzione)

CON PARACADUTE    ──►  «Se manca: DATO NON PRESENTE»  ──► «DATO NON PRESENTE» (Sicuro)
```

### 💡 Regola d'oro 4:
> **In azienda un'invenzione plausibile è peggiore di un errore evidente. Bisogna sempre autorizzare formalmente l'AI ad astenersi («Se non è nel testo, scrivi DATO NON PRESENTE»).**

---

# Slide 16 – Il ponte verso Unsloth Studio e i Documenti (RAG)

Oggi avete imparato a governare l'AI su un singolo paragrafo:

| Oggi nel prompt | Nel lavoro industriale | Con Unsloth Studio & RAG |
| :--- | :--- | :--- |
| **Tabelle e vincoli** | Dati puliti per il MES/ERP | Estrazione automatica nei campi del database |
| **Few-shot con 1 esempio** | Standardizzazione del linguaggio | Classificazione automatica dei cartellini guasto |
| **Passaggi intermedi (CoT)** | Controllo qualità e tempi | Verifica incrociata tra formule e registri |
| **Clausola di astensione** | Sicurezza e conformità | Risposte affidabili basate solo sui manuali d'officina |

Nella prossima lezione collegheremo l'AI **all'intero archivio tecnico** (schede macchina, cataloghi ricambi rev1 e rev2) usando Unsloth Studio!

---

# Slide 17 – Riepilogo finale: Cosa sappiamo fare oggi

1. **Basta convenevoli:** usiamo vincoli negativi per ottenere tabelle e dati pronti all'uso.
2. **Guidare con esempi:** usiamo il Few-shot per fissare formati e stili senza ambiguità.
3. **Calcoli verificabili:** forziamo i passaggi intermedi (Chain-of-Thought) per non far tirare a indovinare l'AI.
4. **Zero allucinazioni:** diamo sempre il permesso esplicito di dire *"Dato non presente"*.

> **Alla macchina il volume e l'esecuzione, alla persona il controllo e la responsabilità.**
