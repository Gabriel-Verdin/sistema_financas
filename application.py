from functions import transacoes, validacoes, categorias, forma_pagamento

# ============================================== TRANSACÃO ==============================================  
def modulo_transacao():
    while True:
        print()
        print('======== TRANSAÇÕES ========')
        print('[1] - Cadastrar Transação')
        print('[2] - Mostrar Transações')
        print('[3] - Editar Transação')
        print('[4] - Apagar Transação')
        print('[0] - Voltar')

        print()
        escolha_str = input('Escolha uma das opções: ')

        escolha_int = validacoes.str_para_int(escolha_str)

        if escolha_int is not None:
            if escolha_int == 1:
                data = input('Digite a data da transação (d/m/a) (vazio para data atual): ')
                descricao = input('Digite a descrição da transação: ')

                print()
                categorias.mostrar_categorias()
                id_categoria_str = input('Escolha uma categoria: ')

                id_categoria_int = validacoes.str_para_int(id_categoria_str)

                categoria_valida = validacoes.escolha_valida_categoria(id_categoria_int)

                if id_categoria_int is not None and categoria_valida is not None:

                    print()
                    forma_pagamento.mostrar_forma_pagamento()
                    id_forma_pagamento_str = input('Escolha uma forma de pagamento: ')

                    id_forma_pagamento_int = validacoes.str_para_int(id_forma_pagamento_str)

                    forma_pagamento_valida = validacoes.escolha_valida_forma_pagamento(id_forma_pagamento_int)

                    if id_forma_pagamento_int is not None and forma_pagamento_valida is not None:
                        valor_str = input('Digite o valor da transação: ')

                        valor_float = validacoes.str_para_float(valor_str)

                        if valor_float is not None:
                            entrada_saida = input('Digite se a transação é entrada ou saída: ')

                        transacoes.cadastrar_transacao(data, descricao, id_categoria_int, id_forma_pagamento_int, valor_float, entrada_saida)
            
            elif escolha_int == 2:
                print()
                transacoes.mostrar_transacoes()

            elif escolha_int == 3:
                print()
                transacoes.mostrar_transacoes()

                id_transacao_str = input('Escolha a transação que deseja editar: ')

                id_transacao_int = validacoes.str_para_int(id_transacao_str)

                if id_transacao_int is not None:
                    transacoes.editar_transacao(id_transacao_int)

            elif escolha_int == 4:
                print()
                transacoes.mostrar_transacoes()

                print()
                id_transacao_str = input('Escolha a transação que deseja apagar: ')

                id_transacao_int = validacoes.str_para_int(id_transacao_str)

                if id_transacao_int is not None:
                    transacoes.apagar_transacao(id_transacao_int)

            elif escolha_int == 0:
                print('Voltando ao menu principal....')
                break
                
            else:
                print('Digite uma opção existente!')


# ============================================== CATEGORIA ==============================================  
def modulo_categoria():
    while True:
        print()
        print('======== CATEGORIAS ========')
        print('[1] - Cadastrar Categoria')
        print('[2] - Mostrar Categorias')
        print('[3] - Editar Categoria')
        print('[4] - Apagar Categoria')
        print('[0] - Voltar')

        print()
        escolha_str = input('Escolha uma das opções: ')

        escolha_int = validacoes.str_para_int(escolha_str)

        if escolha_int is not None:
            if escolha_int == 1:
                nova_categoria = input('Digite a categoria que deseja adicionar: ')
                tipo_nova_categoria = input('Digite o tipo padrão da categoria (Despesa/Receita): ')

                categorias.cadastrar_categoria(nova_categoria, tipo_nova_categoria)

            elif escolha_int == 2:
                print()
                categorias.mostrar_categorias()

            elif escolha_int == 3:
                print()
                categorias.mostrar_categorias()

                print()
                id_categoria_str = input('Escolha a categoria que deseja editar: ')

                id_categoria_int = validacoes.str_para_int(id_categoria_str)

                if id_categoria_int is not None:
                    novo_nome = input('Digite o novo nome da categoria (nada para manter o atual): ')
                    novo_tipo = input('Digite o novo tipo da categoria (nada para manter o atual): ')

                    categorias.editar_categoria(id_categoria_int, novo_nome, novo_tipo)

            elif escolha_int == 4:
                print()
                categorias.mostrar_categorias()

                print()
                id_categoria_str = input('Escolha a categoria que deseja apagar: ')

                id_categoria_int = validacoes.str_para_int(id_categoria_str)

                if id_categoria_int is not None:
                    categorias.apagar_categoria(id_categoria_int)

            elif escolha_int == 0:
                print('Voltando ao menu principal....')
                break
            
            else:
                print('Digite uma opção existente!')

# ============================================== FORMA PAGAMENTO ==============================================  
def modulo_forma_pagamento():
    while True:
        print()
        print('======== FORMAS DE PAGAMENTO ========')
        print('[1] - Cadastrar Forma de Pagamento')
        print('[2] - Mostrar Formas de Pagamento')
        print('[3] - Editar Forma de Pagamento')
        print('[4] - Apagar Forma de Pagamento')
        print('[0] - Voltar')

        print()
        escolha_str = input('Escolha uma das opções: ')

        escolha_int = validacoes.str_para_int(escolha_str)

        if escolha_int is not None:
            if escolha_int == 1:
                nova_forma_pagamento = input('Digite a forma de pagamento que deseja adicionar: ')

                forma_pagamento.cadastrar_forma_pagamento(nova_forma_pagamento)

            elif escolha_int == 2:
                print()
                forma_pagamento.mostrar_forma_pagamento()

            elif escolha_int == 3:
                print()
                forma_pagamento.mostrar_forma_pagamento()

                print()
                id_forma_pagamento_str = input('Escolha a forma de pagamento que deseja editar: ')

                id_forma_pagamento_int = validacoes.str_para_int(id_forma_pagamento_str)

                if id_forma_pagamento_int is not None:
                    novo_nome = input('Digite o novo nome da forma de pagamento (nada para manter o atual): ')

                    forma_pagamento.editar_forma_pagamento(id_forma_pagamento_int, novo_nome)

            elif escolha_int == 4:
                print()
                forma_pagamento.mostrar_forma_pagamento()

                print()
                id_forma_pagamento_str = input('Escolha a forma de pagamento que deseja apagar: ')

                id_forma_pagamento_int = validacoes.str_para_int(id_forma_pagamento_str)

                if id_forma_pagamento_int is not None:
                    forma_pagamento.apagar_forma_pagamento(id_forma_pagamento_int)

            elif escolha_int == 0:
                print('Voltando ao menu principal....')
                break
            
            else:
                print('Digite uma opção existente!')

# ==================================================================================================  
# ============================================== MAIN ==============================================  
# ==================================================================================================  
while True:
    print('==============================')
    print('===== SISTEMA FINANCEIRO =====')
    print('==============================')

    print('[1] - Transações')
    print('[2] - Categorias')
    print('[3] - Formas de Pagamento')
    print('[0] - Sair')

    print()
    escolha_str = input('Escolha um dos Módulos: ')

    escolha_int = validacoes.str_para_int(escolha_str)

    if escolha_int is not None:
        if escolha_int == 1:
            modulo_transacao()

        elif escolha_int == 2:
            modulo_categoria()
        
        elif escolha_int == 3:
            modulo_forma_pagamento()

        elif escolha_int == 0:
            print('Saindo....')
            break

        else:
            print('Digite uma opção existente')