# Schema scritto a mano, non un'esecuzione

Per il ramo di riserva c della parte 3 (vedi guida docente). Non è la risposta di un modello e non prova che opencode funzioni con il modello della VM. Si usa soltanto se la parte 3 non può essere eseguita dagli studenti.

La richiesta è quella della slide 36: «Che file ci sono in questa cartella e di che cosa parlano?»

| Passo | Chi agisce | Che cosa succede |
| --- | --- | --- |
| 1 | Chi scrive | Invia la richiesta a opencode |
| 2 | Il modello | Non vede la cartella: chiede al programma di elencare i file e di leggerli |
| 3 | Il programma | Apre `inventario.csv`, `appunti_riunione.txt`, `da_fare.txt` e, se il modello lo chiede, `opencode.jsonc`, e rimanda il testo al modello |
| 4 | Il modello | Riassume ciascun file e risponde |

Per Plan e Build (slide 39–41): in Plan il programma non scrive niente e `inventario.html` non compare. In Build, con il permesso `ask`, il programma si ferma e chiede; il file compare solo se si approva. Con Reject (slide 43), il file non compare e la risposta si interrompe.

Domande per la classe: chi apre il file? Che cosa succede se il file non c'è nella cartella? Dove, in questo schema, un permesso potrebbe fermare il programma?
