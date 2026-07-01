import sqlite3
from datetime import datetime

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
def cadastrar_transacao(data, descricao, id_categoria, tipo, id_forma_pagamento, valor, entrada_saida):
    if not data:
        data = datetime.now().strftime("%d-%m-%Y")

    cursor.execute("INSERT INTO transacao (data, descricao, id_categoria, tipo, id_forma_pagamento, valor, entrada_saida) VALUES (?, ?, ?, ?, ?, ?, ?)", (data, descricao, id_categoria, tipo, id_forma_pagamento, valor, entrada_saida))

    conn.commit()
    print('Transação cadastrada com sucesso!')