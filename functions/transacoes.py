import sqlite3

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# ========== Listar Transações ==========
def listar_transacoes():
    cursor.execute("SELECT id_transacao, data, descricao, id_categoria, tipo, id_forma_pagamento, valor, entrada_saida FROM transacao")
    transacoes = cursor.fetchall()

    print('Transações:')
    for trans in transacoes:
        print(f'{trans[0]} - {trans[1]} - {trans[2]} - {trans[3]} - {trans[4]} - {trans[5]} - {trans[6]} - {trans[7]}')

    return transacoes

# ========== Cadastrar Transações ==========
def cadastrar_transacao():
    ...