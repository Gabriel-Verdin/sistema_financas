from functions import categorias

print('==============================')
print('===== Sistema Financeiro =====')
print('==============================')

print('[1] - Cadastrar Categoria')
print('[2] - Listar Categoria')
print('[3] - ')
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

except ValueError:
    print('Por favor, digite uma escolha válida!')
