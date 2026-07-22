import sqlite3
import tkinter as tk
from tkinter import messagebox

from functions import function_validacoes

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# ========== Listar Forma de Pagamento ==========
def listar_forma_pagamento():
    cursor.execute("SELECT id_forma_pagamento, nome FROM forma_pagamento")
    return cursor.fetchall()

# ========== Mostrar Forma de Pagamento ==========
def mostrar_forma_pagamento(frame):
    formas_pagamento = listar_forma_pagamento()

    lista = tk.Listbox(frame, width=50)
    lista.pack(pady=10)

    for forma in formas_pagamento:
        lista.insert(tk.END, f'{forma[0]} - {forma[1]}')
