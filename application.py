from functions import validacoes, categorias, forma_pagamento

def modulo_categoria():
    while True:
        print()
        print('======== CATEGORIAS ========')
        print('[1] - Cadastrar Categoria')
        print('[2] - Listar Categoria')
        print('[3] - Editar Categoria')
        print('[4] - Apagar Categoria')
        print('[0] - Voltar')

        print()
        escolha_str = input('Escolha uma das opções: ')

        escolha_int = validacoes.str_para_int(escolha_str)

        if escolha_int is not None:
            if escolha_int == 1:
                nova_categoria = input('Digite a categoria que deseja adicionar: ')
                tipo_nova_categoria = input('Digite o tipo padrão da categoria (Despesa/Receita/Nada): ')

                categorias.cadastrar_categoria(nova_categoria, tipo_nova_categoria)

            elif escolha_int == 2:
                print()
                categorias.listar_categorias()

            elif escolha_int == 3:
                print()
                categorias.listar_categorias()

                print()
                id_categoria_str = input('Escolha a categoria que deseja editar: ')

                id_categoria_int = validacoes.str_para_int(id_categoria_str)

                if id_categoria_int is not None:
                    novo_nome = input('Digite o novo nome da categoria (nada para manter o atual): ')
                    novo_tipo = input('Digite o novo tipo da categoria (nada para manter o atual): ')

                    categorias.editar_categoria(id_categoria_int, novo_nome, novo_tipo)

            elif escolha_int == 4:
                print()
                categorias.listar_categorias()

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

def modulo_forma_pagamento():
    while True:
        print()
        print('======== FORMAS DE PAGAMENTO ========')
        print('[1] - Cadastrar Forma de Pagamento')
        print('[2] - Listar Forma de Pagamento')
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
                forma_pagamento.listar_forma_pagamento()

            elif escolha_int == 3:
                print()
                forma_pagamento.listar_forma_pagamento()

                print()
                id_forma_pagamento_str = input('Escolha a forma de pagamento que deseja editar: ')

                id_forma_pagamento_int = validacoes.str_para_int(id_forma_pagamento_str)

                if id_forma_pagamento_int is not None:
                    novo_nome = input('Digite o novo nome da forma de pagamento (nada para manter o atual): ')

                    forma_pagamento.editar_forma_pagamento(id_forma_pagamento_int, novo_nome)

            elif escolha_int == 4:
                print()
                forma_pagamento.listar_forma_pagamento()

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

# ============================================== MAIN ==============================================  
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
            print('Em andamento!')
            print()

        elif escolha_int == 2:
            modulo_categoria()
        
        elif escolha_int == 3:
            modulo_forma_pagamento()

        elif escolha_int == 0:
            print('Saindo....')
            break

        else:
            print('Digite uma opção existente')