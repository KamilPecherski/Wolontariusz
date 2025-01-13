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

label_City = tk.Label(root, text="Miasto:")
label_City.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_City = tk.Entry(root, width=40)
entry_City.grid(row=4, column=1, padx=10, pady=5)

label_Country = tk.Label(root, text="Kraj:")
label_Country.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_Country = tk.Entry(root, width=40)
entry_Country.grid(row=5, column=1, padx=10, pady=5)

label_Data_Birth = tk.Label(root, text="Data Urodzenia:")
label_Data_Birth.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_Data_Birth = tk.Entry(root, width=40)
entry_Data_Birth.grid(row=6, column=1, padx=10, pady=5)

# Przycisk zapisu
button_save = tk.Button(root, text="Zapisz", command=lambda x:x)
button_save.grid(row=7, column=0, columnspan=2, pady=10)

# Uruchomienie pętli głównej
root.mainloop()