# Laboratorio Rapido: Le 4 Regole del Prompting in Azienda
**ITS MAKER Bologna** · Tecnico Superiore per la Digitalizzazione dei Processi Industriali  
*Scheda pratica a coppie · Durata totale: 45–50 minuti · Nessuna installazione richiesta*

---

## Come si lavora
- Lavorate a coppie: **Studente A** scrive il prompt al computer, **Studente B** controlla il risultato sulla fonte.
- Aprite una finestra di chat (ChatGPT, Claude o la sandbox messa a disposizione dal docente).
- **Regola base:** L'AI non è una persona e non è una calcolatrice: è un assistente a cui dare istruzioni precise e verificabili.

---

## Il testo di manutenzione di partenza
Copiate e incollate questo rapporto di fermo (DOC-FERMO) per tutte le attività:

```text
Rapporto del 14 Ottobre (DOC-FERMO):
Ore 14:20: la pressa P03 si è fermata per sovratemperatura dell'olio idraulico. Temperatura registrata: 78 °C. Soglia: 65 °C. Sostituito il filtro intasato con il ricambio FLT-992.
Fermo macchina totale: 45 minuti.
```
---

## Attività 1 · «Basta chiacchiere» (Formato e Vincoli)
> **Obiettivo:** Far capire che nei processi aziendali l'AI deve produrre tabelle e dati puliti, non discorsi lunghi.

1. **Tentativo 1 (Senza vincoli):**  
   Incollate il testo e chiedete:  
   > *«Riassumimi cosa è successo alla macchina.»*  
   *Cosa notate?* Quante parole inutili e convenevoli ha aggiunto il modello?
2. **Tentativo 2 (Con formato e vincolo negativo):**  
   Nello stesso messaggio o in una chat pulita, chiedete:  
   > *«Dal testo allegato estrai: Macchina, Causa fermo, Durata minuti, Codice ricambio.*  
   > *Rispondi SOLO con una tabella a 4 colonne.*  
   > *Vincolo rigido: nessun saluto, nessuna premessa, nessuna spiegazione prima o dopo la tabella.»*
3. **Controllo del compagno (Studente B):**  
   La tabella contiene esattamente 4 colonne? Il modello è riuscito a stare zitto prima e dopo la tabella?

💡 **Regola d'oro 1:** *Se non specifichi il formato e non metti vincoli negativi, l'AI riempie lo spazio con convenevoli inutilizzabili per un software.*

---

## Attività 2 · «Un esempio vale più di mille parole» (Few-Shot)
> **Obiettivo:** Ottenere esattamente lo stile voluto dando un esempio pratico, invece di scrivere lunghe spiegazioni teoriche.

1. **Il problema:** Dobbiamo scrivere una riga sintetica per il registro manutenzione aziendale (es. `[P03] 45 min | ALLARME TEMPERATURA | RICAMBIO: FLT-992`).
2. **Tentativo 1 (Istruzione astratta):**  
   Provate a chiedere: *«Scrivi una riga breve e tecnica per il registro manutenzione da inserire nel gestionale.»*  
   *Cosa notate?* Ognuno ottiene uno stile, parole e simboli diversi.
3. **Tentativo 2 (Con un esempio concreto):**  
   Inviate questo prompt:  
   > *«Crea una riga di registro manutenzione seguendo ESATTAMENTE lo stile di questo esempio:*  
   > *Esempio: [Linea 1] 20 min | BLOCCO NASTRO | RICAMBIO: CINGHIA-B12*  
   >  
   > *Ora genera la riga per il rapporto della pressa P03.»*
4. **Controllo del compagno (Studente B):**  
   Il modello ha rispettato parentesi, barre `|` e ordine dei campi dell'esempio?

💡 **Regola d'oro 2:** *Non perdere tempo a descrivere lo stile a parole: mostra all'AI 1 o 2 esempi di input/output già risolti.*

---

## Attività 3 · «La calcolatrice che sbaglia» (Ragionamento passo-passo)
> **Obiettivo:** Capire che l'AI genera parole probabili e può sbagliare i calcoli logici se forzata a dare subito il risultato finale.

1. **Il problema:** Il costo orario di fermo linea per l'azienda è di **160 €/ora**. Vogliamo calcolare il costo totale del fermo della P03 (durato 45 minuti).
2. **Tentativo 1 (Risposta diretta):**  
   Chiedete:  
   > *«Il costo orario di fermo è 160 € all'ora. Dal testo del fermo P03 calcola il costo totale. Dammi subito e soltanto la cifra finale in euro.»*  
   *(Attenzione: 45 minuti NON sono 0,45 ore, ma 0,75 ore! Quindi 0,75 × 160 € = 120 €).*  
   *Cosa notate?* Il modello ha indovinato il numero esatto o ha fatto confusione tra minuti e decimali?
3. **Tentativo 2 (Mostra i passaggi intermedi - Chain of Thought):**  
   Chiedete:  
   > *«Calcola il costo totale del fermo procedendo per passaggi ordinati:*  
   > *Passo 1: Estrai i minuti totali di fermo dal testo.*  
   > *Passo 2: Converti i minuti in ore decimali (minuti / 60).*  
   > *Passo 3: Moltiplica le ore decimali per la tariffa oraria di 160 €/ora.*  
   > *Passo 4: Scrivi il costo totale finale in euro.»*
4. **Controllo del compagno (Studente B):**  
   Verificate con la calcolatrice dello smartphone il Passo 2 e il Passo 3. I passaggi sono chiari e verificabili?

💡 **Regola d'oro 3:** *Per calcoli, logiche o conversioni, chiedi sempre all'AI di scrivere i passaggi intermedi: scrivere le tappe le impedisce di tirare a indovinare.*

---

## Attività 4 · «Il test del trabocchetto» (Bloccare le allucinazioni)
> **Obiettivo:** Insegnare all'AI a fermarsi e dire "non lo so" quando un dato manca nei documenti aziendali.

1. **Il tranello:** Nel testo del rapporto sopra **non è specificato il nome dell'operatore o del manutentore** che ha fatto il lavoro.
2. **Tentativo 1 (Domanda a tranello senza paracadute):**  
   Chiedete:  
   > *«Chi è l'operatore che ha effettuato la sostituzione del filtro della P03?»*  
   *Cosa notate?* L'AI ha provato a inventare un nome, a fare ipotesi vaghe («un tecnico incaricato») o si è scusata a lungo?
3. **Tentativo 2 (Con la clausola di sicurezza):**  
   Chiedete:  
   > *«Chi è l'operatore che ha effettuato l'intervento?*  
   > *Regola tassativa: Rispondi basandoti ESCLUSIVAMENTE sulle informazioni scritte nel testo.*  
   > *Se l'informazione non è presente o non è certa, rispondi testualmente con: 'DATO NON PRESENTE NEL DOCUMENTO'. Non aggiungere altro.»*
4. **Controllo del compagno (Studente B):**  
   Il modello ha obbedito e si è astenuto, oppure ha comunque cercato di spiegare perché non lo sapeva?

💡 **Regola d'oro 4:** *In azienda un'informazione inventata fa danni gravi. Bisogna sempre dare all'AI il permesso esplicito di dire che il dato non c'è.*

---

## Sintesi per la classe: Il ponte verso Unsloth Studio e il RAG

Avete appena applicato le stesse 4 regole che useremo quando collegheremo l'AI ai manuali e cataloghi tecnici:

| Problema visto oggi | Come lo abbiamo risolto | Cosa diventerà con Unsloth Studio e RAG |
| :--- | :--- | :--- |
| Risposte lunghe e vaghe | **Vincoli di formato e tabelle** | Estrazione automatica nei campi del gestionale |
| Stile incoerente | **Esempi pratici (Few-shot)** | Istruzioni stabili per catalogare le anomalie |
| Errori su calcoli e logica | **Passaggi intermedi (CoT)** | Controllo indipendente tra dati e formule |
| Dati inventati (Allucinazioni) | **Clausola di astensione** | Risposte sicure basate solo sui documenti caricati |
