import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# ========== Listar Transações ==========
def listar_transacoes():
    cursor.execute("""
        SELECT t.id_transacao, t.data, t.descricao, c.nome, c.tipo_padrao, t.valor, t.entrada_saida 
        FROM transacao t
        JOIN categoria c ON t.id_categoria = c.id_categoria
    """)
    # t = tabela transacao
    # c = tabela categoria
    return cursor.fetchall()

# ========== Mostrar Transações ==========
def mostrar_transacoes(frame):

    transacoes = listar_transacoes()

    lista = tk.Listbox(frame, width=70)
    lista.pack(pady=10)

    for trans in transacoes:
        lista.insert(tk.END, f'{trans[0]} - {trans[1]} - {trans[2]} - {trans[3]} - {trans[4]} - {trans[5]} - {trans[6]}')