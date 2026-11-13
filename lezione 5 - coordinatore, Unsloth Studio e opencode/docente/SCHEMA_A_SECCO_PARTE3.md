# Schema scritto a mano, non un'esecuzione

Per il ramo di riserva c della parte 3 (vedi guida docente). Non è la risposta di un modello e non prova che opencode funzioni con il modello della VM. Si usa soltanto se la parte 3 non può essere eseguita dagli studenti.

La richiesta è quella della slide 32: «Quale codice hanno le pastiglie montate sulla bici 12?»

| Passo | Chi agisce | Che cosa succede |
| --- | --- | --- |
| 1 | Chi scrive | Invia la richiesta a opencode |
| 2 | Il modello | Non conosce la risposta: chiede al programma di leggere il registro |
| 3 | Il programma | Apre il file `Registro_Ruota_Libera_7-8_novembre_2026.txt` e rimanda il testo al modello |
| 4 | Il modello | Cerca nel testo il codice delle pastiglie e risponde |

Per Plan e Build (slide 34–35): in Plan il programma non scrive niente e il file non compare. In Build, con il permesso `ask`, il programma si ferma e chiede; il file compare solo se si approva.

Domande per la classe: chi apre il file? Che cosa succede se il file non c'è nella cartella? Dove, in questo schema, un permesso potrebbe fermare il programma?
