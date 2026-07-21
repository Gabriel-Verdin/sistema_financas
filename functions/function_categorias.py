import sqlite3
import tkinter as tk
from tkinter import messagebox

from functions import function_validacoes

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
def cadastrar_categoria(nova_categoria, tipo_nova_categoria):

    if nova_categoria == '':
        messagebox.showwarning('Erro', 'Nome da categoria não pode ser vazio')
        # print('Nome da categoria não pode ser Vazio!')
        # print('Categoria não adicionada!')
        return
    
    tipo_nova_categoria_valido = function_validacoes.despesa_ou_receita(tipo_nova_categoria)
    if tipo_nova_categoria_valido == None:
        return
    
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", (nova_categoria, tipo_nova_categoria_valido))

    conn.commit()
    # print('Categoria adicionada com sucesso!')
    messagebox.showinfo('Sucesso','Categoria adicionada com sucesso!')

# ========== Editar Categoria ==========
def editar_categoria(id_categoria, novo_nome = None, novo_tipo = None):

    id_categoria_valido = function_validacoes.str_para_int(id_categoria)
    if id_categoria_valido == None:
        return

    if novo_nome and novo_tipo:
        cursor.execute("UPDATE categoria SET nome = ?, tipo_padrao = ? WHERE id_categoria = ?", (novo_nome, novo_tipo, id_categoria_valido))
    elif novo_nome:
        cursor.execute("UPDATE categoria SET nome = ? WHERE id_categoria = ?", (novo_nome, id_categoria_valido))
    elif novo_tipo:
        cursor.execute("UPDATE categoria SET tipo_padrao = ? WHERE id_categoria = ?", (novo_tipo, id_categoria_valido))
    else:
        messagebox.showwarning('Aviso','Nenhuma alteração foi informada!')
        return

    conn.commit()
    messagebox.showinfo('Sucesso','Categoria atualizada com sucesso!')

# ========== Apagar Categoria ==========
def apagar_categoria(id_categoria):

    id_categoria_valido = function_validacoes.escolha_valida_categoria(id_categoria)
    if id_categoria_valido:

        cursor.execute("DELETE FROM categoria WHERE id_categoria = ?", (id_categoria,))

        conn.commit()
        messagebox.showinfo('Sucesso!', 'Categoria apagada com sucesso!')