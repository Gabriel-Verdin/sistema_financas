import sqlite3
from datetime import datetime
from functions import categorias, forma_pagamento, validacoes

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
def mostrar_transacoes():

    transacoes = listar_transacoes()
    print('Transações:')
    for trans in transacoes:
        print(f'{trans[0]} - {trans[1]} - {trans[2]} - {trans[3]} - {trans[4]} - {trans[5]} - {trans[6]}')

# ========== Cadastrar Transações ==========
def cadastrar_transacao(data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida):
    if not data:
        data = datetime.now().strftime("%d-%m-%Y")

    cursor.execute("INSERT INTO transacao (data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida) VALUES (?, ?, ?, ?, ?, ?)", (data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida))

    conn.commit()
    print('Transação cadastrada com sucesso!')

# ========== Editar Transação ==========
def editar_transacao(id_transacao):
    while True:

        print('Opções de Edição:')
        print('[1] - Data')
        print('[2] - Descrição')
        print('[3] - Categoria')
        print('[4] - Forma de Pagamento')
        print('[5] - Valor')
        print('[6] - Entrada ou Saída')
        print('[0] - Voltar (Nada)')

        escolha_str = input('Esolha o que deseja editar: ')

        escolha_int = validacoes.str_para_int(escolha_str)

        if escolha_int is not None:
            if escolha_int == 1: # Data
                nova_data = input('Digite uma nova data (Vazio para hoje): ')
                if not nova_data:
                    nova_data = datetime.now().strftime("%d-%m-%Y")

                cursor.execute("UPDATE transacao SET data = ? WHERE id_transacao = ?", (nova_data, id_transacao))

            elif escolha_int == 2: # Descrição
                nova_descricao = input('Digite uma nova descrição: ')

                cursor.execute("UPDATE transacao SET descricao = ? WHERE id_transacao = ?", (nova_descricao, id_transacao))

            elif escolha_int == 3: # Categoria
                print()
                categorias.listar_categorias()

                nova_categoria_str = input('Escolha a nova categoria: ')

                nova_categoria_int = validacoes.str_para_int(nova_categoria_str)

                if nova_categoria_int is not None:
                    cursor.execute("UPDATE transacao SET id_categoria = ? WHERE id_transacao = ?", (nova_categoria_int, id_transacao))

            elif escolha_int == 4: # Forma de Pagamento
                print()
                forma_pagamento.listar_forma_pagamento()

                nova_forma_pagamento_str = input('Escolha a nova categoria: ')

                nova_forma_pagamento_int = validacoes.str_para_int(nova_forma_pagamento_str)

                if nova_forma_pagamento_int is not None:
                    cursor.execute("UPDATE transacao SET id_forma_pagamento = ? WHERE id_transacao = ?", (nova_forma_pagamento_int, id_transacao))

            elif escolha_int == 5: # Valor
                novo_valor_str = input('Digite o novo Valor: ')

                novo_valor_float = validacoes.str_para_float(novo_valor_str)

                if novo_valor_float is not None:
                    cursor.execute("UPDATE transacao SET valor = ? WHERE id_transacao = ?", (novo_valor_float, id_transacao))

            elif escolha_int == 6:
                nova_entrada_Saida = input('Digite se é estrada ou saída: ')

                cursor.execute("UPDATE transacao SET entrada_saida = ? WHERE id_transacao = ?", (nova_entrada_Saida, id_transacao))

            elif escolha_int == 0:
                print('Nenhuma alteração realizada!')
                break

            else: 
                print('Selecione uma opção válida!')

        conn.commit()
        print('Transação atualizada com sucesso!')

# ========== Apagar Transação ==========
def apagar_transacao(id_transacao):
    cursor.execute("DELETE FROM transacao WHERE id_transacao = ?", (id_transacao,))

    conn.commit()
    print('Transação apagada com sucesso!')