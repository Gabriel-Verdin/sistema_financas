import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()


# ========== Listar Categoria ==========
def listar_categorias(): # Guarda os dados 
    cursor.execute("SELECT id_categoria, nome, tipo_padrao FROM categoria")
    return cursor.fetchall()

# ========== Mostrar Categoria ==========
def mostrar_categorias(frame): # Mosta as Categorias
    categorias = listar_categorias()

    lista = tk.Listbox(frame, width=50)
    lista.pack(pady=10)

    # print('Categorias Disponíveis:')
    for cat in categorias:
        lista.insert(tk.END, f'{cat[0]} - {cat[1]} | ({cat[2]})')
        # print(f'{cat[0]} - {cat[1]} | ({cat[2]})')

# ========== Cadastrar Categoria ==========
def cadastrar_categoria(nova_categoria, tipo_nova_categoria = None):

    if nova_categoria == '':
        messagebox.showwarning('Erro', 'Nome da categoria não pode ser vazio')
        # print('Nome da categoria não pode ser Vazio!')
        # print('Categoria não adicionada!')
        return
    
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", (nova_categoria, tipo_nova_categoria))

    conn.commit()
    # print('Categoria adicionada com sucesso!')
    messagebox.showwarning('Sucesso','Categoria adicionada com sucesso!')
