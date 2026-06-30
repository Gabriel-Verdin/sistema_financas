import sqlite3

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# ========== Listar Forma de Pagamento ==========
def listar_forma_pagamento():
    cursor.execute("SELECT id_forma_pagamento, nome FROM forma_pagamento")
    formas_pagamento = cursor.fetchall()

    print("Formas de Pagamento desponíveis:")
    for forma in formas_pagamento:
        print(f'{forma[0]} - {forma[1]}')

    return formas_pagamento

# ========== Cadastrar Forma de Pagamento ==========
def cadastrar_forma_pagamento(nova_forma_pagamento):

    if nova_forma_pagamento == '':
        print('Nome da forma de pagamento não pode ser vazio!')
        print('Nova forma de pagamento não adicionada!')
        return

    cursor.execute(f"INSERT INTO forma_pagamento (nome) VALUES ('{nova_forma_pagamento}')")

    conn.commit()
    print('Forma de Pagamento adicionada com sucesso!')

# ========== Editar Forma de Pagamento ==========
def editar_forma_pagamento(id_forma_pagamento, novo_nome):
    if novo_nome:
        cursor.execute("UPDATE forma_pagamento SET nome = ? WHERE id_forma_pagamento = ?", (novo_nome, id_forma_pagamento))
        
    else:
        print('Nenhuma alteração foi informada!')
        return
    
    conn.commit()
    print('Forma de Pagamento alterada com sucesso!')

# ========== Apagar Forma de Pagamento ==========
def apagar_forma_pagamento(id_forma_pagamento):
    cursor.execute("DELETE FROM forma_pagamento WHERE id_forma_pagamento = ?", (id_forma_pagamento,))

    conn.commit()
    print('Forma de pagamento apagada com sucesso!')