import mysql.connector
from configparser import ConfigParser

def leggi_credenziali(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config['mysql']

def connetti_database(credenziali):
    try:
        db_connection = mysql.connector.connect(
            host=credenziali['ip-server-mysql'],
            port=credenziali.getint('porta'),
            user=credenziali['username'],
            password=credenziali['password'],
            database='rubrica'
        )
        print("Connessione al database MySQL riuscita!")
        return db_connection
    except mysql.connector.Error as error:
        print("Errore durante la connessione al database MySQL:", error)
        return None

def check_credentials(email, password):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        query = "SELECT * FROM utente WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        if cursor.fetchone():
            return True
        cursor.close()
        db_connection.close()
    except Exception as e:
        print("Errore durante il controllo delle credenziali:", e)
    return False

def inserisci_utente(email, password):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        query = "INSERT INTO utente (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, password))
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return True
    except Exception as e:
        print("Errore durante l'inserimento dell'utente:", e)
        return False

def inserisci_contatto(nome, cognome, eta, telefono, creatore):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        query = "INSERT INTO contatti (nome, cognome, eta, telefono, creatore) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nome, cognome, eta, telefono, creatore))
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return True
    except Exception as e:
        print("Errore durante l'inserimento del contatto:", e)
        return False

def elimina_contatto(nome, cognome, eta, telefono, creatore):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        query = "DELETE FROM contatti WHERE nome = %s AND cognome = %s AND eta = %s AND telefono = %s AND creatore = %s"
        cursor.execute(query, (nome, cognome, eta, telefono, creatore))
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return True
    except Exception as e:
        print("Errore durante l'eliminazione del contatto:", e)
        return False

def getUser(logged_user):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        query = "SELECT * FROM contatti WHERE creatore = %s ORDER BY nome"
        cursor.execute(query, (logged_user,))
        contatti = cursor.fetchall()
        cursor.close()
        db_connection.close()
        return contatti
    except Exception as e:
        print("Errore durante il recupero dei contatti dell'utente:", e)
        return None

def modifica_contatto(oldname, oldsurname, oldtel, oldage, logged_user, nome, cognome, eta, telefono ):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        update_query = "UPDATE contatti SET nome = %s, cognome = %s, telefono = %s, eta = %s WHERE creatore = %s AND nome = %s AND cognome = %s AND telefono = %s AND eta = %s"
        cursor.execute(update_query, (nome, cognome, telefono, eta, logged_user, oldname, oldsurname, oldtel, oldage))
        db_connection.commit()
        print("Contatto aggiornato con successo.")
        return True
    except Exception as e:
        print("Errore durante la modifica del contatto nel database:", e)
        return False

def searchUser(logged_user, search_term=None):
    try:
        db_connection = connetti_database(leggi_credenziali('./credenziali_database.properties'))
        cursor = db_connection.cursor()
        if search_term:
            query = "SELECT * FROM contatti WHERE creatore = %s AND (nome LIKE %s OR cognome LIKE %s)"
            cursor.execute(query, (logged_user, f"{search_term}%", f"{search_term}%"))
        else:
            query = "SELECT * FROM contatti WHERE creatore = %s"
            cursor.execute(query, (logged_user,))
        contatti = cursor.fetchall()
        cursor.close()
        db_connection.close()
        return contatti
    except Exception as e:
        print("Errore durante il recupero dei contatti dell'utente:", e)
        return None
