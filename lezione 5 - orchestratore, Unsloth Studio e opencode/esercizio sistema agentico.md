1) creare un system prompt per un agente che rappresenti un negozio di noleggio di biciclette, che noleggia biciclette ad utenti.


Login differenziato, admin o utente.

Le skill possono essere abilitate per admin, utente o entrambi (sulla base di un campo dichiarato all’interno della singola skill).


2) prima skill dei guasti (skill\_guasti.md)


risponde ad admin o user (preferably user)


contesto: guasti ruota libera, registro ruota libera, regole noleggio ruota libera,

la skill di guasti deve rispondere all’utente sulla base delle informazioni che reperisce guardando i guasti.

La skill deve fare “digest” del file guasti.




3) seconda skill è per il gestore. 


Risponde solo ad admin


contesto: guasti ruota libera, registro ruota libera, regole noleggio ruota libera,

la skill deve dare informazioni sul registro del noleggio, all’admin, sulla base delle informazioni che reperisce guardando il registro utente.

La skill deve fare “digest” del file registro ruota libera.


4) terza skill di regole di noleggio


risponde solo ad user


contesto: guasti ruota libera, registro ruota libera, regole noleggio ruota libera,


la skill da le regole di noleggio all’utente. Può rispondere all’utente a richieste sul noleggio.


5) progettazione di istruzioni di routing (da incorporare dentro l’agente),


Linee guida:

- interpretare se la richiesta riguarda guasti, dati di noleggio o regole di noleggio.

Se la richiesta riguarda guasti chiamare la prima skill

se la richiesta riguarda dati di noleggio chiamare la seconda skill

se la richiesta riguarda regole di noleggio chiamare la terza skill


esempi di rinforzo positivo (non limitative):

domande sui guasti

“mi si è rotto il componente X, cosa devo fare?”


