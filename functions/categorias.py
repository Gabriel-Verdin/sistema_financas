import sqlite3

conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# ========== Listar Categoria ==========
def listar_categorias(): # Guarda os dados 
    cursor.execute("SELECT id_categoria, nome, tipo_padrao FROM categoria")
    return cursor.fetchall()

# ========== Mostrar Categoria ==========
def mostrar_categorias(): # Mosta as Categorias
    categorias = listar_categorias()

    print('Categorias Disponíveis:')
    for cat in categorias:
        print(f'{cat[0]} - {cat[1]} | ({cat[2]})')


# ========== Cadastrar Categoria ==========
def cadastrar_categoria(nova_categoria, tipo_nova_categoria = None):

    if nova_categoria == '':
        print('Nome da categoria não pode ser Vazio!')
        print('Categoria não adicionada!')
        return
    
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", (nova_categoria, tipo_nova_categoria))

    conn.commit()
    print('Categoria adicionada com sucesso!')

# ========== Editar Categoria ==========
def editar_categoria(id_categoria, novo_nome = None, novo_tipo = None):
    if novo_nome and novo_tipo:
        cursor.execute("UPDATE categoria SET nome = ?, tipo_padrao = ? WHERE id_categoria = ?", (novo_nome, novo_tipo, id_categoria))
    elif novo_nome:
        cursor.execute("UPDATE categoria SET nome = ? WHERE id_categoria = ?", (novo_nome, id_categoria))
    elif novo_tipo:
        cursor.execute("UPDATE categoria SET tipo_padrao = ? WHERE id_categoria = ?", (novo_tipo, id_categoria))
    else:
        print('Nenhuma alteração foi informada!')
        return

    conn.commit()
    print('Categoria atualizada com sucesso!')

# ========== Apagar Categoria ==========
def apagar_categoria(id_categoria):
    cursor.execute("DELETE FROM categoria WHERE id_categoria = ?", (id_categoria,))

    conn.commit()
    print('Categoria apagada com sucesso!')
# # Escolher categoria
# def escolher_categoria():
#     categorias = listar_categorias()

#     escolha = int(input('Digite o ID da categoria desejada: '))

#     return escolha

# Exemplo 
# id_categoria_escolhida = escolher_categoria()
# print(f'Você escolheu a categoria com id {id_categoria_escolhida}')

