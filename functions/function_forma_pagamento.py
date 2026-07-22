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

# ========== Cadastrar Forma de Pagamento ==========
def cadastrar_forma_pagamento(nova_forma_pagamento):

    if nova_forma_pagamento == '':
        messagebox.showerror('Erro', 'Nome da forma de pagamento não pode ser vazio!')
        return

    cursor.execute(f"INSERT INTO forma_pagamento (nome) VALUES ('{nova_forma_pagamento}')")

    conn.commit()
    messagebox.showinfo('Sucesso!', 'Forma de Pagamento adicionada com sucesso!')

# ========== Editar Forma de Pagamento ==========
def editar_forma_pagamento(id_forma_pagamento, novo_nome = None):

    id_forma_pagamento_valido = function_validacoes.str_para_int(id_forma_pagamento)
    if id_forma_pagamento_valido == None:
        return

    if novo_nome:
        cursor.execute("UPDATE forma_pagamento SET nome = ? WHERE id_forma_pagamento = ?", (novo_nome, id_forma_pagamento_valido))
        
    else:
        messagebox.showerror('Erro', 'Nenhuma alteração foi informada!')
        return
    
    conn.commit()
    messagebox.showinfo('Sucesso!', 'Forma de Pagamento alterada com sucesso!')