from functions import validacoes
from functions import categorias

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
            print('Em andamento!')
            print()

        elif escolha_int == 0:
            print('Saindo....')
            break

        else:
            print('Digite uma opção existente')