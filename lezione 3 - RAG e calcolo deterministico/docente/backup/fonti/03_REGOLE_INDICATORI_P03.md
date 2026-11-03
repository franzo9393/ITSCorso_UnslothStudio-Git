# Regole di calcolo degli indicatori della pressa P03

**Procedura PR-IND-03 · Revisione 2 del 5 gennaio 2026 · Ufficio produzione**

Documento inventato per l'esercitazione ITS MAKER. Stabilisce come si calcolano i numeri del riepilogo mensile che compare in testa a ogni diario di produzione della P03.

## 1. Da dove vengono i dati

Il pannello della P03 registra ogni evento con data, ora, tipo di evento, cadenza e una breve descrizione. A fine mese l'ufficio produzione esporta il diario in un file Word e in un file Excel con gli stessi dati.

La cadenza è il numero di pezzi all'ora impostato nella ricetta. La ricetta è l'insieme delle impostazioni della pressa per un certo pezzo, per esempio PR-12.

## 2. I tipi di evento

| Evento | Che cosa indica |
| --- | --- |
| PROGRAMMAZIONE | Caricamento di una nuova ricetta e della sua cadenza. |
| VERIFICA SETUP | Controllo della ricetta già attiva prima dell'avvio, senza cambiare la cadenza. |
| AVVIO | La pressa comincia o riprende a produrre. |
| ARRESTO | Arresto comandato da una persona: pausa mensa, fine turno, controllo di un pezzo campione. |
| FAULT | Arresto automatico causato da un allarme. |
| RIPRISTINO | Allarme azzerato dopo il controllo. La pressa resta ferma. |

## 3. Gli indicatori del riepilogo mensile

**Giornate lavorative.** Giorni del mese in cui il diario registra almeno un AVVIO.

**Ore di produzione.** Somma dei periodi di marcia. Un periodo di marcia comincia con un AVVIO e finisce con il primo ARRESTO o FAULT che lo segue.

**Pezzi teorici.** Per ogni periodo di marcia: durata in ore × cadenza indicata nella riga di AVVIO. Il riepilogo riporta la somma del mese, arrotondata all'unità. Sono pezzi stimati, non pezzi contati.

**Fault.** Numero di eventi FAULT del mese.

**Fermo per fault.** Per ogni FAULT si misurano i minuti dall'ora del FAULT all'ora del primo AVVIO successivo. Il riepilogo riporta la somma del mese in minuti. Gli ARRESTO comandati, anche quelli per il controllo del pezzo campione, non contano come fermo per fault.

## 4. Indicatore usato nelle proposte di miglioramento

**Pezzi teorici persi per fault.** Per ogni FAULT: minuti di fermo per fault × cadenza della ricetta attiva ÷ 60. La cadenza della ricetta attiva è quella dell'ultimo AVVIO prima del FAULT.

Questo indicatore non compare nel riepilogo mensile. Si calcola quando serve confrontare problemi diversi.

## 5. Controllo dei calcoli

Chi ricalcola gli indicatori confronta i risultati con il riepilogo mensile del diario. Se un valore non coincide, prima di usarlo si cerca il motivo della differenza.
