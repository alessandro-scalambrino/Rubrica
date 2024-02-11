import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import *

class RubricaTelefonicaApp:
    def __init__(self, master, logged_user):
        self.master = master
        self.master.title("Rubrica Telefonica")
        self.logged_user = logged_user

        style = ttk.Style()
        style.theme_use("clam")

        self.toolbar = tk.Frame(master)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self.table_frame = tk.Frame(master)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(self.table_frame, columns=("Nome", "Cognome", "Età", "Telefono"))
        self.table.heading("Nome", text="Nome")
        self.table.heading("Cognome", text="Cognome")
        self.table.heading("Età", text="Età")
        self.table.heading("Telefono", text="Telefono")
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.table.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.config(yscrollcommand=self.scrollbar.set)

        self.mostra_contatti()

        self.new_button = ttk.Button(self.toolbar, text="Nuovo", command=self.nuovo_contatto)
        self.new_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = ttk.Button(self.toolbar, text="Modifica", command=self.modifica_contatto)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.toolbar, text="Elimina", command=self.elimina_contatto)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        self.search_label = ttk.Label(self.toolbar, text="Cerca:")
        self.search_label.pack(side=tk.LEFT, padx=5)

        style.configure("Smussato.TEntry", borderwidth=0, fieldbackground="#f0f0f0")
        
        self.search_entry = ttk.Entry(self.toolbar, style="Smussato.TEntry")
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.toolbar, text="Cerca", command=self.cerca_contatti)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def mostra_contatti(self, contatti=None):
        self.table.delete(*self.table.get_children())  

        if contatti is None:
            contatti = getUser(self.logged_user)

        if contatti:
            for contatto in contatti:
                self.table.insert("", "end", values=contatto)
        else:
            messagebox.showinfo("Nessun contatto", "Nessun contatto trovato per l'utente corrente.")

    def nuovo_contatto(self):
        editor = ContattoEditor(self.master, self.mostra_contatti, self.logged_user, nuovo=True)
        editor.editor_window.grab_set()


    def modifica_contatto(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showerror("Errore", "Per modificare è necessario selezionare un contatto.")
            return

        contatto = self.table.item(selection)['values']
        editor = ContattoEditor(self.master, self.mostra_contatti, self.logged_user, contatto=contatto, nuovo=False)
        editor.editor_window.grab_set()


    def elimina_contatto(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showerror("Errore", "Per eliminare è necessario selezionare un contatto.")
            return

        contatto = self.table.item(selection)['values']
        result = messagebox.askokcancel("Conferma", f"Eliminare il contatto {contatto[0]} {contatto[1]}?")

        if result:
            elimina_contatto(contatto[0], contatto[1], contatto[2], contatto[3], self.logged_user)
            self.mostra_contatti()
    
    def cerca_contatti(self):
        termine_ricerca = self.search_entry.get()

        if not termine_ricerca:
            self.mostra_contatti()
            return

        contatti = searchUser(self.logged_user,  termine_ricerca)
        self.mostra_contatti(contatti)
        
class ContattoEditor:
    def __init__(self, master, callback, logged_user, nuovo=True, contatto=None):
        self.master = master
        self.callback = callback
        self.logged_user = logged_user
        self.nuovo = nuovo
        self.contatto = contatto

        self.editor_window = tk.Toplevel(master)
        self.editor_window.title("Editor Contatto")

        style = ttk.Style()
        style.theme_use("clam")

        self.nome_label = ttk.Label(self.editor_window, text="Nome:")
        self.nome_label.grid(row=0, column=0, pady=5, padx=5)
        self.nome_entry = ttk.Entry(self.editor_window, style="Smussato.TEntry")
        self.nome_entry.grid(row=0, column=1, pady=5, padx=5)

        self.cognome_label = ttk.Label(self.editor_window, text="Cognome:")
        self.cognome_label.grid(row=1, column=0, pady=5, padx=5)
        self.cognome_entry = ttk.Entry(self.editor_window, style="Smussato.TEntry")
        self.cognome_entry.grid(row=1, column=1, pady=5, padx=5)

        self.telefono_label = ttk.Label(self.editor_window, text="Telefono:")
        self.telefono_label.grid(row=2, column=0, pady=5, padx=5)
        self.telefono_entry = ttk.Entry(self.editor_window, style="Smussato.TEntry")
        self.telefono_entry.grid(row=2, column=1, pady=5, padx=5)

        self.eta_label = ttk.Label(self.editor_window, text="Età:")
        self.eta_label.grid(row=3, column=0, pady=5, padx=5)
        self.eta_entry = ttk.Entry(self.editor_window, style="Smussato.TEntry")
        self.eta_entry.grid(row=3, column=1, pady=5, padx=5)

        self.save_button = ttk.Button(self.editor_window, text="Salva", command=self.salva_contatto)
        self.save_button.grid(row=4, column=0, pady=5, padx=5)
        self.cancel_button = ttk.Button(self.editor_window, text="Annulla", command=self.editor_window.destroy)
        self.cancel_button.grid(row=4, column=1, pady=5, padx=5)

        if self.contatto:
            self.nome_entry.insert(tk.END, self.contatto[0])
            self.cognome_entry.insert(tk.END, self.contatto[1])
            self.eta_entry.insert(tk.END, self.contatto[2])
            self.telefono_entry.insert(tk.END, self.contatto[3])
            

    def salva_contatto(self):
        nome = self.nome_entry.get()
        cognome = self.cognome_entry.get()
        eta = self.eta_entry.get()
        telefono = self.telefono_entry.get()
        

        if not nome or not cognome or not telefono or not eta:
            messagebox.showerror("Errore", "Inserire tutti i campi.")
            return

        contatto = (nome, cognome, eta, telefono)
       

      

        if self.contatto is None:
            # Se self.contatto è None, crea un nuovo contatto
            if inserisci_contatto(nome, cognome, eta, telefono, self.logged_user):
                messagebox.showinfo("Successo", "Contatto salvato con successo!")
                self.callback()
                self.editor_window.destroy()
            else:
                messagebox.showerror("Errore", "Errore durante il salvataggio del contatto.")
        else:
            # modifica un contatto esistente
            # pastrocchio sull'ordine da sistemare
            if modifica_contatto(self.contatto[0], self.contatto[1], self.contatto[3], self.contatto[2], self.contatto[4], nome, cognome, eta, telefono  ):
                messagebox.showinfo("Successo", "Contatto aggiornato con successo!")
                self.callback()
                self.editor_window.destroy()
            else:
                messagebox.showerror("Errore", "Errore durante l'aggiornamento del contatto.")

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        style = ttk.Style()
        style.theme_use("clam")

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.pack(pady=5, padx=5)
        self.email_entry = ttk.Entry(master, style="Smussato.TEntry")
        self.email_entry.pack(pady=5, padx=5)

        self.password_label = ttk.Label(master, text="Password:")
        self.password_label.pack(pady=5, padx=5)
        self.password_entry = ttk.Entry(master, show="*", style="Smussato.TEntry")
        self.password_entry.pack(pady=5, padx=5)

        self.login_button = ttk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=5, padx=5)

        self.register_button = ttk.Button(master, text="Registrati", command=self.open_registration_window)
        self.register_button.pack(pady=5, padx=5)

        self.logged_user = None

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if check_credentials(email, password):
            messagebox.showinfo("Successo", "Accesso effettuato con successo!")
            self.logged_user = email
            self.master.destroy()
            root = tk.Tk()
            app = RubricaTelefonicaApp(root, self.logged_user)
            root.mainloop()
        else:
            messagebox.showerror("Errore", "Credenziali non valide. Riprova.")

    def open_registration_window(self):
        registration_window = tk.Toplevel()
        registration_app = RegistrationApp(registration_window)

class RegistrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrazione")

        style = ttk.Style()
        style.theme_use("clam")

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.pack(pady=5, padx=5)
        self.email_entry = ttk.Entry(master, style="Smussato.TEntry")
        self.email_entry.pack(pady=5, padx=5)

        self.password_label = ttk.Label(master, text="Password:")
        self.password_label.pack(pady=5, padx=5)
        self.password_entry = ttk.Entry(master, show="*", style="Smussato.TEntry")
        self.password_entry.pack(pady=5, padx=5)

        self.register_button = ttk.Button(master, text="Registrazione", command=self.register)
        self.register_button.pack(pady=5, padx=5)

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if inserisci_utente(email, password):
            messagebox.showinfo("Successo", "Registrazione completata con successo!")
            self.master.destroy()
        else:
            messagebox.showerror("Errore", "Errore durante la registrazione. Riprova.")

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
