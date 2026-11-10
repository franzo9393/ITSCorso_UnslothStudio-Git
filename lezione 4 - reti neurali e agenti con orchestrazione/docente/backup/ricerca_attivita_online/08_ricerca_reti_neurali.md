# Ricerca · giochi nel browser sulle reti neurali

Data: 10 novembre 2026. Documento riservato al docente.

## Che cosa è stato fatto e con quali limiti

- Richiesta del docente: risorse online, didattiche e ludiche, che mostrino come funziona una rete neurale e il machine learning, adatte a introdurre l'idea di addestrare uno stile sulle risposte. Senza webcam (decisione del 10 novembre 2026). Solo siti che elaborano nel browser, come per la lezione 4 (decisione del 5 novembre 2026).
- Le licenze delle tre risorse scelte sono state lette sul repository GitHub. Le pagine sono state aperte con Chromium senza interfaccia da una postazione Linux del docente, rete non scolastica, e si è guardato quali indirizzi contattano e se compaiono errori in console. Playground e Flappy Learning sono stati anche provati con scenari numerici (vedi `GUIDA_DOCENTE.md`, «Che cosa è stato verificato»).
- **Non sono state lette** le informative sulla privacy né i termini dei siti; non è stata provata la rete della scuola né alcuna postazione degli studenti.
- Il primo tentativo di ricerca web ha dato un errore del servizio; il secondo ha restituito sintesi dei motori di ricerca. Le voci che non sono sotto «Selezionate» provengono solo da quelle sintesi e dalla lettura dei repository indicati, non da prove: sono candidate, non verificate.

## Selezionate

| Risorsa | Indirizzo | Licenza | Che cosa mostra | Note |
| --- | --- | --- | --- | --- |
| TensorFlow Playground | https://playground.tensorflow.org/ | Apache-2.0 (repository `tensorflow/playground`) | Una rete piccola che impara a separare punti di due colori; neuroni, strati, pesi, Training loss e Test loss, rumore | Elabora nel browser. Contatta `fonts.googleapis.com`, `fonts.gstatic.com`, `www.google-analytics.com`. Nel repository `analytics.js` ha un identificativo segnaposto: non si sa cosa faccia il sito ospitato |
| Flappy Learning | https://xviniette.github.io/FlappyLearning/ | MIT (repository `xviniette/FlappyLearning`) | Neuroevoluzione: 50 uccellini con una piccola rete ciascuno; i migliori restano di generazione in generazione | Elabora nel browser. Contatta `fonts.googleapis.com` e `fonts.gstatic.com` per il carattere. L'unico comando è la velocità. Prove del 10 novembre con velocità MAX: il punteggio sale senza fermarsi alla generazione 40, 10 e circa 90 |
| Transformer Explainer | https://poloclub.github.io/transformer-explainer/ | MIT | Modello GPT-2 piccolo nel browser: parola successiva, probabilità, temperatura | Già in questa ricerca (`01_ricerca_llm_locali.md`). Il 10 novembre la pagina dichiara lo scarico di circa 600 MB all'apertura («Try the examples while GPT-2 model is being downloaded (600MB)»); durante lo scarico il pulsante Generate è disattivato ma il cursore Temperature funziona sugli esempi. Contatta anche Google Fonts, Google Tag Manager, DoubleClick, YouTube, Google Analytics, `cdn.jsdelivr.net` e `huggingface.co`. Lo scarico completo non è stato atteso |

## Candidate non usate (da verificare prima di un eventuale uso)

| Risorsa | Motivo |
| --- | --- |
| ConvNetJS (demo `classify2d`, `rldemo`) | Licenza MIT letta sul repository `karpathy/convnetjs`. L'autore dichiara di non mantenerla più. Doppione di Playground per la parte 2. Eventuale riserva |
| [Neural Playground](https://github.com/zrnge/neural-playground) (zrnge) | Licenza MIT letta sul repository. Raccoglie simulatori di RNN, LSTM, CNN, GAN, diffusione, Transformer. Progetto recente e con una sola stella; l'elenco è più ampio e più astratto di quanto serve alla lezione |
| Nascent, Neural Network Playground di terzi e altri simulatori | Citati dalle sintesi della ricerca, non aperti né letti: licenza e funzionamento non verificati |
| Generatori di testo a catena di Markov (per esempio Zelaron `Markov-chain-text-generator`, `bespoyasov/text-generator`) | Mostrano come uno stile si impara dagli esempi, ma non sono reti neurali. Non letti né provati. Scartati per ora: la parte sullo stile si fa con le istruzioni dell'agente |
| Teachable Machine | Esclusa: usa la webcam e non si è letta la pagina delle condizioni (la FAQ non si è caricata nella lettura) |

## Che cosa non è stato trovato

Una risorsa pronta, gratuita, senza account e con licenza chiara, che faccia vedere in modo ludico l'addestramento di uno stile di scrittura con una vera rete neurale. L'idea di stile è perciò introdotta dall'analogia di Flappy Learning (si tengono i risultati migliori) e dal confronto, nella parte 4G della consegna, tra esempi scritti nelle istruzioni di un agente e un addestramento che cambia i pesi.
