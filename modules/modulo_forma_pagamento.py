import tkinter as tk

from functions import function_forma_pagamento
from functions import function_validacoes

# Função para limpar os widgets da tela
def limpar_tela(tela):
    for widget in tela.winfo_children():
        widget.destroy()

# =================
# ===== Telas =====
# =================

# =============== Tela Cadastrar Formas de Pagamento ===============
def tela_cadastrar_forma_pagamento(tela_cadastrar_forma_pagamento, mostrar_tela, tela_modulo_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_cadastrar_forma_pagamento)

    # Limpa widgets
    limpar_tela(tela_cadastrar_forma_pagamento)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_cadastrar_forma_pagamento, text='Cadastro de Forma de Pagamento')
    label_cadastro.pack(pady=20)

    label_nome = tk.Label(tela_cadastrar_forma_pagamento, text='Nome da Forma de Pagamento:')
    label_nome.pack(pady=10)
    nome_forma_pagamento = tk.Entry(tela_cadastrar_forma_pagamento)
    nome_forma_pagamento.pack(pady=10)

    botao_cadastrar = tk.Button(tela_cadastrar_forma_pagamento, text='Cadastrar Forma de Pagamento', command=lambda: function_forma_pagamento.cadastrar_forma_pagamento(nome_forma_pagamento.get()))
    botao_cadastrar.pack(pady=5)

    botao_voltar = tk.Button(tela_cadastrar_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_forma_pagamento))
    botao_voltar.pack(pady=20)

# =============== Tela Mostrar Formas de Pagamento ===============
def tela_mostrar_forma_pagamento(tela_mostrar_forma_pagamento, mostrar_tela, tela_modulo_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_mostrar_forma_pagamento)

    # Limpa widgets
    limpar_tela(tela_mostrar_forma_pagamento)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_mostrar_forma_pagamento, text='Formas de Pagamento')
    label_cadastro.pack(pady=20)

    function_forma_pagamento.mostrar_forma_pagamento(tela_mostrar_forma_pagamento)

    botao_voltar = tk.Button(tela_mostrar_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_forma_pagamento))
    botao_voltar.pack(pady=20)

# =============== Função Intermediária para Edição de Categorias ===============
def navegar_para_edicao_forma_pagamento(escolha_editar, mostrar_tela, frame_edicao_forma_pagamento, frame_editar_forma_pagamento):
    id_validado = function_validacoes.escolha_valida_forma_pagamento(escolha_editar)

    if id_validado:
        tela_edicao_forma_pagamento(id_validado, frame_edicao_forma_pagamento, mostrar_tela, frame_editar_forma_pagamento)

# =============== Tela Editar Formas de Pagamento ===============
def tela_editar_forma_pagamento(tela_editar_forma_pagamento, mostrar_tela, tela_modulo_forma_pagamento, tela_edicao_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_editar_forma_pagamento)

    # Limpa widgets
    limpar_tela(tela_editar_forma_pagamento)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_editar_forma_pagamento, text='Formas de Pagamento para Editar')
    label_cadastro.pack(pady=20)

    function_forma_pagamento.mostrar_forma_pagamento(tela_editar_forma_pagamento)

    # Escolha da Forma de Pagamento
    label_escolha = tk.Label(tela_editar_forma_pagamento, text='Escolha uma Forma de Pagamento para editar:')
    label_escolha.pack(pady=10)
    escolha_editar = tk.Entry(tela_editar_forma_pagamento)
    escolha_editar.pack(padx=5)
    
    botao_escolha = tk.Button(tela_editar_forma_pagamento, text='Escolher Forma de Pagamento', command=lambda: navegar_para_edicao_forma_pagamento(escolha_editar.get(), mostrar_tela, tela_edicao_forma_pagamento, tela_editar_forma_pagamento))
    botao_escolha.pack(pady=10)
    

    botao_voltar = tk.Button(tela_editar_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_forma_pagamento))
    botao_voltar.pack(pady=20)

# =============== Tela de Edição de Formas de Pagamento ===============
def tela_edicao_forma_pagamento(id_validado, tela_edicao_forma_pagamento, mostrar_tela, tela_editar_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_edicao_forma_pagamento)

    # Limpa todos os widgets existentes
    limpar_tela(tela_edicao_forma_pagamento)

    # Criar os widgets novamente
    label_edicao = tk.Label(tela_edicao_forma_pagamento, text='Tela de Edição de Formas de Pagamento')
    label_edicao.pack(pady=20)

    label_novo_nome = tk.Label(tela_edicao_forma_pagamento, text='Novo nome da Forma de Pagamento')
    label_novo_nome.pack(pady=10)
    novo_nome = tk.Entry(tela_edicao_forma_pagamento)
    novo_nome.pack(pady=5)

    botao_atualizar = tk.Button(tela_edicao_forma_pagamento, text='Atualizar Forma de Pagamento', command=lambda: function_forma_pagamento.editar_forma_pagamento(id_validado, novo_nome.get()))
    botao_atualizar.pack(pady=20)

    # Voltar ao Módulo
    botao_voltar = tk.Button(tela_edicao_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_editar_forma_pagamento))
    botao_voltar.pack(pady=20)


# =============== Tela Apagar Formas de Pagamento ===============
def tela_apagar_forma_pagamento(tela_apagar_forma_pagamento, mostrar_tela, tela_modulo_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_apagar_forma_pagamento)

    # Limpa widgets
    limpar_tela(tela_apagar_forma_pagamento)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_apagar_forma_pagamento, text='Formas de Pagamento para Apagar')
    label_cadastro.pack(pady=20)

    botao_voltar = tk.Button(tela_apagar_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_forma_pagamento))
    botao_voltar.pack(pady=20)

# =============== Tela Principal Forma de Pagamento ===============
def tela_modulo_forma_pagamento(tela, mostrar_tela, tela_menu_principal, frame_cadastrar_forma_pagamento, frame_mostrar_forma_pagamento, frame_editar_forma_pagamento, frame_edicao_forma_pagamento, frame_apagar_forma_pagamento):
    label_modulo_forma_pagamento = tk.Label(tela, text='===== Módulo Forma de Pagamento =====')
    label_modulo_forma_pagamento.pack(pady=20)

    botao_cadastrar_forma_pagamento = tk.Button(tela, text='Cadastrar Forma de Pagamento', command=lambda: tela_cadastrar_forma_pagamento(frame_cadastrar_forma_pagamento, mostrar_tela, tela))
    botao_cadastrar_forma_pagamento.pack(pady=20)

    botao_mostrar_forma_pagamento = tk.Button(tela, text='Mostrar Formas de Pagamento', command=lambda: tela_mostrar_forma_pagamento(frame_mostrar_forma_pagamento, mostrar_tela, tela))
    botao_mostrar_forma_pagamento.pack(pady=20)

    botao_editar_forma_pagamento = tk.Button(tela, text='Editar Forma de Pagamento', command=lambda: tela_editar_forma_pagamento(frame_editar_forma_pagamento, mostrar_tela, tela, frame_edicao_forma_pagamento))
    botao_editar_forma_pagamento.pack(pady=20)

    botao_apagar_forma_pagamento = tk.Button(tela, text='Apagar Forma de Pagamento', command=lambda: tela_apagar_forma_pagamento(frame_apagar_forma_pagamento, mostrar_tela, tela))
    botao_apagar_forma_pagamento.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)