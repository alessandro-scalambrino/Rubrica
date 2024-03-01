# Rubrica Telefonica

Questo progetto è una rubrica telefonica che consente agli utenti di aggiungere, modificare ed eliminare contatti tramite un'interfaccia grafica.

## Contenuti

- `database.py`: Contiene le funzioni di backend per l' interazione col database.
- `rubrica.py`: Contiene le classi principali `RubricaTelefonicaApp` e `ContattoEditor`, insieme alle rispettive interfacce grafiche.
- `rubrica.sql`: Contiene le query per la creazione del database per la rubrica telefonica.
- `credenziali_database.properties`: File di configurazione per specificare i parametri di connessione al database.

## Istruzioni per l'uso
1. Importare il database MySQL utilizzando `rubrica.sql`
2. Specifica i parametri di connessione al database utilizzando 'credenziali_database.properties'
3. Esegui il file `rubrica.py` per avviare l'applicazione della rubrica telefonica.
4. Accedi utilizzando le credenziali fornite (email: ale.scala@gmail.com, pw: 6caratteri) o registrane di nuove.
5. Utilizza l'applicazione per aggiungere, modificare o eliminare contatti.

## Requisiti di sistema

- Python 3.x
- MySQL Server

## Credits
This project was developed by [Alessandro Scalambrino](https://github.com/alessandro-scalambrino)
