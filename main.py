import tkinter as tk

from tkinter import messagebox
root = tk.Tk()
root.title("Formularz rejestracyjny dla wolontariusza na festiwal")

# Etykiety i pola tekstowe..

label_name = tk.Label(root, text="Imię:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_SurName = tk.Label(root, text="Nazwisko:")
label_SurName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_SurName = tk.Entry(root, width=40)
entry_SurName.grid(row=1, column=1, padx=10, pady=5)

label_mail = tk.Label(root, text="Adres e-mail:")
label_mail.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_mail = tk.Entry(root, width=40)
entry_mail.grid(row=2, column=1, padx=10, pady=5)

label_PhoneNr = tk.Label(root, text="Numer telefonu:")
label_PhoneNr.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_PhoneNr = tk.Entry(root, width=40)
entry_PhoneNr.grid(row=3, column=1, padx=10, pady=5)

# Dodanie kolejny Etykiet oraz pola tekstowego przez pozostałych członków grupy



# Przycisk zapisu
button_save = tk.Button(root, text="Zapisz", command=lambda x:x)
button_save.grid(row=4, column=0, columnspan=2, pady=10)

# Uruchomienie pętli głównej
root.mainloop()