# Note su Unsloth Studio per la lezione 5

Documento riservato al docente. Raccoglie solo ciò che resta valido della vecchia lezione 4 con Studio, da usare quando si progetta la lezione 5 (18 novembre 2026). La versione completa precedente, con consegna, slide e guida, è nella cronologia di git (commit precedenti al 10 novembre 2026).

## Decisione

Il docente copia una VM dai PC della scuola su un HDD, a casa installa Studio e il modello, e la consegna agli studenti il 18 novembre. Nessuna installazione in aula e nessuno zip del modello su chiavetta.

## Che cosa è stato provato

Il 5 novembre 2026 sul portatile del docente, **Linux**, versione di Unsloth Studio 2026.11.2, anche in sola CPU. Non è Windows, non è la VM, non è la rete della scuola.

- **Installazione.** `install.sh` con `UNSLOTH_NO_TORCH=1` (modalità senza PyTorch, solo GGUF): nessun errore. Circa 2,3 GB su disco, circa 15 minuti con una connessione domestica. Su Windows il comando è `$env:UNSLOTH_NO_TORCH=1; irm https://unsloth.ai/install.ps1 | iex`: **non provato**.
- **Primo avvio.** `unsloth studio -p <porta>`; la pagina chiede di creare una password di almeno 8 caratteri.
- **Interfaccia.** Casella **Select model**, scheda **On Device**, pannello **Run settings** con **Estimated Memory Usage**, **Context Length**, **System Prompt**, **Temperature** (0,6 di partenza), **Top P** (0,95), **Top K** (20). Nella casella dei messaggi **Search** e **Tools** sono attivi di partenza (verdi) e si disattivano con un clic; la scelta resta dopo il riavvio.
- **Modello.** `unsloth/Qwen3.5-2B-GGUF`, versione `UD-Q4_K_XL`, 2,0 GB indicati da Studio. Con il download predefinito la barra è rimasta ferma a lungo; con `HF_HUB_DISABLE_XET=1` è partito, a circa 1,1–1,8 MB/s.
- **Risposte, solo CPU** (scheda grafica nascosta; 15,6 GB di RAM nel portatile). Registro intero (circa 3,2k token) più una domanda: circa 25 secondi in totale, 15–16 tok/s. Tempo alla prima parola non misurato. Con **Context Length** su Auto il processo del modello occupava circa 5,4 GB, con 8192 circa 2,5 GB (Estimated Memory Usage 6,49 GiB contro 3,34 GiB).
- **Istruzioni di sistema.** Il modello risponde in italiano. Con istruzioni in prosa lunga non ha mai fatto una domanda di chiarimento; con quattro regole numerate (esempio in fondo), alla domanda «Qual era la temperatura dell'olio?» ha risposto «A quale giorno e ora ti riferisci?». Un solo caso, un solo tentativo.
- **Persistenza.** Il System Prompt è rimasto dopo una nuova chat e dopo Reload model. Temperature, Top P e Top K non sono stati verificati.

**Non provato:** installer su Windows; Windows nella VM con 8 GB; permessi degli studenti; rete della scuola; memoria con poca RAM libera (Studio dovrebbe ridurre il contesto da solo con Auto, ma non è stato visto); tempi con i processori della VM; knowledge base BM25; esecuzione di codice; modelli più grandi.

## Da controllare a casa, sulla VM

| Controllo | Che cosa verificare |
| --- | --- |
| Avvio | Dopo l'installazione `unsloth studio -p 8888` riparte e chiede la password; decidere se la imposti tu uguale per tutti o la creano gli studenti |
| Modello | Compare in On Device, si carica con 8 GB di RAM, risponde in italiano |
| Context Length | Si può impostare prima del caricamento? Il valore (8192) resta dopo la riapertura? Con Auto la VM si blocca? |
| Search e Tools | Grigi e persistenti nella versione per Windows |
| System Prompt e parametri | Restano dopo una nuova conversazione, con il modello caricato e dopo una risposta |
| Separatore decimale | Le caselle Temperature e Top P accettano il punto, la virgola o entrambi |
| Immagine VMware | Alla prima accensione sul PC dello studente VMware chiede se la VM è stata spostata o copiata (cambiano identificativo e indirizzo di rete); 22 copie hanno lo stesso nome macchina; niente tuoi accessi a Teams o Copilot nell'immagine; dimensione dell'immagine e tempo di copia su 22 postazioni |
| Memoria dell'host | Con la VM da 8 GB accesa e il browser aperto sul computer reale la memoria del PC reale regge |

Lo script `misura_vm.py` in questa cartella misura memoria e tempi senza interfaccia, ma richiede Python e il corpus del laboratorio e non è stato provato su Windows.

## Vincoli di rete

L'indirizzo pubblico della scuola è condiviso: il 4 novembre Copilot non ha risposto per circa 10 minuti (ipotesi: limite di richieste per indirizzo, non verificata). Per le lezioni con Studio: solo siti che elaborano nel browser, niente servizi che interrogano un modello sul server (HackMerlin, Prompt Airlines, Gandalf).

## Esempio di istruzioni per il System Prompt (provato su un solo caso)

Per provarlo, incollare nella casella System Prompt solo il testo sotto la riga `----`. Non è una soluzione: non garantisce che il modello le segua sempre.

----

Sei l'assistente di reparto della pressa P03. Rispondi in italiano, con frasi brevi. Usa solo il registro che ti viene incollato nella chat.

Regola 1: se la domanda non dice di quale giorno o di quale ora parla e nel registro ci sono più valori, rispondi SOLO con questa domanda: «A quale giorno e ora ti riferisci?». Non scrivere altro.

Regola 2: se il dato non c'è nel registro, rispondi solo: «Dato non presente nel registro.»

Regola 3: negli altri casi rispondi con il valore e con la data e l'ora della nota da cui l'hai preso.

Regola 4: non consigliare interventi sulla macchina, riparazioni o sicurezze. Rispondi solo: «Serve il parere del responsabile di reparto.»
