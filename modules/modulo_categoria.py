import tkinter as tk

from functions import function_categorias
from functions import function_validacoes

# Função para limpar os widgets da tela
def limpar_tela(tela):
    for widget in tela.winfo_children():
        widget.destroy()


# =================
# ===== Telas =====
# =================

# =============== Tela Cadastrar Categorias ===============
def tela_cadastrar_categoria(tela_cadastrar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_cadastrar_categoria)

    # Limpa widgets
    limpar_tela(tela_cadastrar_categoria)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_cadastrar_categoria, text='Cadastro de Categorias')
    label_cadastro.pack(pady=20)

    # Nome da Categoria
    label_nome = tk.Label(tela_cadastrar_categoria, text='Nome da Categoria:')
    label_nome.pack(pady=10)
    nome_categoria = tk.Entry(tela_cadastrar_categoria)
    nome_categoria.pack(pady=5)

    # Tipo da Categoria
    label_tipo = tk.Label(tela_cadastrar_categoria, text='Tipo da Categoria (Receita / Despesa):')
    label_tipo.pack(pady=10)
    tipo_categoria = tk.Entry(tela_cadastrar_categoria)
    tipo_categoria.pack(pady=5)

    # Cadastrar Categoria
    botao_cadastrar = tk.Button(tela_cadastrar_categoria, text='Cadastrar', command=lambda: function_categorias.cadastrar_categoria(nome_categoria.get(), tipo_categoria.get())) # cadastrar_categoria(entrada.get(), 'Receita'
    botao_cadastrar.pack(pady=10)

    # Voltar ao Módulo
    botao_voltar = tk.Button(tela_cadastrar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Mostrar Categorias ===============
def tela_mostrar_categoria(tela_mostrar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_mostrar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_mostrar_categoria)
    
    # Cria os widgets novamente
    label_mostrar = tk.Label(tela_mostrar_categoria, text="Categorias")
    label_mostrar.pack(pady=20)

    # Função de mostrar categorias na tela
    function_categorias.mostrar_categorias(tela_mostrar_categoria) 

    botao_voltar = tk.Button(tela_mostrar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Editar Categorias ===============
def navegar_para_edicao_categoria(escolha_editar, mostrar_tela, frame_edicao_categorias, frame_editar_categoria):
    validacao = function_validacoes.escolha_valida_categoria(escolha_editar)

    if validacao:
        tela_edicao_categorias(frame_edicao_categorias, mostrar_tela, frame_editar_categoria)


def tela_editar_categoria(tela_editar_categoria, mostrar_tela, tela_modulo_categoria, tela_edicao_categorias):
    # Levanta a tela
    mostrar_tela(tela_editar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_editar_categoria)
    
    # Cria os widgets novamente
    label_editar = tk.Label(tela_editar_categoria, text="Categorias para Editar")
    label_editar.pack(pady=20)

    # Função de mostrar categorias na tela
    function_categorias.mostrar_categorias(tela_editar_categoria) 

    # Escolha da Categoria
    label_escolha = tk.Label(tela_editar_categoria, text='Escolha uma categoria para editar:')
    label_escolha.pack(pady=10)
    escolha_editar = tk.Entry(tela_editar_categoria)
    escolha_editar.pack(padx=5)

    botao_escolha = tk.Button(tela_editar_categoria, text='Escolher Categoria', command=lambda: navegar_para_edicao_categoria(escolha_editar.get(), mostrar_tela, tela_edicao_categorias, tela_editar_categoria))
    botao_escolha.pack(pady=10)

    # Voltar ao Módulo
    botao_voltar = tk.Button(tela_editar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)
    
# =============== Tela de Edição de Categorias ===============
def tela_edicao_categorias(tela_edicao_categorias, mostrar_tela, tela_editar_categoria):
    # Levanta a tela
    mostrar_tela(tela_edicao_categorias)

    # Limpa todos os widgets existentes
    limpar_tela(tela_edicao_categorias)

    # Criar os widgets novamente
    label_edicao = tk.Label(tela_edicao_categorias, text='Tela de Edição de Categorias')
    label_edicao.pack(pady=20)

    # Voltar ao Módulo
    botao_voltar = tk.Button(tela_edicao_categorias, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_editar_categoria))
    botao_voltar.pack(pady=20)


# =============== Tela Apagar Categorias ===============
def tela_apagar_categoria(tela_apagar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_apagar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_apagar_categoria)
    
    # Cria os widgets novamente
    label_apagar = tk.Label(tela_apagar_categoria, text="Categorias para Editar")
    label_apagar.pack(pady=20)

    botao_voltar = tk.Button(tela_apagar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Principal Categorias ===============
def tela_modulo_categoria(tela, mostrar_tela, tela_menu_principal, frame_mostrar_categorias, frame_cadastrar_categoria, frame_editar_categoria, frame_edicao_categorias, frame_apagar_categoria):
    label_modulo_categoria = tk.Label(tela, text='===== Módulo Categoria =====')
    label_modulo_categoria.pack(pady=20)

    botao_cadastrar_categoria = tk.Button(tela, text='Cadastrar Categoria', command=lambda: tela_cadastrar_categoria(frame_cadastrar_categoria, mostrar_tela, tela))
    botao_cadastrar_categoria.pack(pady=20)

    botao_mostrar_categoria = tk.Button(tela, text='Mostrar Categorias', command=lambda: tela_mostrar_categoria(frame_mostrar_categorias, mostrar_tela, tela))
    botao_mostrar_categoria.pack(pady=20)

    botao_editar_categoria = tk.Button(tela, text='Editar Categoria', command=lambda: tela_editar_categoria(frame_editar_categoria, mostrar_tela, tela, frame_edicao_categorias))
    botao_editar_categoria.pack(pady=20)

    botao_apagar_categoria = tk.Button(tela, text='Apagar Categoria', command=lambda: tela_apagar_categoria(frame_apagar_categoria, mostrar_tela, tela))
    botao_apagar_categoria.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)