from functions import categorias

print('==============================')
print('===== Sistema Financeiro =====')
print('==============================')

print('[1] - Cadastrar Categoria')
print('[2] - Listar Categoria')
print('[3] - Editar Categoria')
print('[4] - ')
print('[5] - ')

print()
escolha_str = input('Escolha uma das opções: ')

try:
    escolha_int = int(escolha_str)

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

        try:
            id_categoria_int = int(id_categoria_str)

            novo_nome = input('Digite o novo nome da categoria (nada para manter o atual): ')
            novo_tipo = input('Digite o novo tipo da categoria (nada para manter o atual): ')

            categorias.editar_categoria(id_categoria_int, novo_nome, novo_tipo)
        except ValueError:
            print('Por favor, digite uma categoria válida!')

except ValueError:
    print('Por favor, digite uma escolha válida!')
