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

# =============== Tela Editar Formas de Pagamento ===============
def tela_editar_forma_pagamento(tela_editar_forma_pagamento, mostrar_tela, tela_modulo_forma_pagamento):
    # Levanta a tela
    mostrar_tela(tela_editar_forma_pagamento)

    # Limpa widgets
    limpar_tela(tela_editar_forma_pagamento)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_editar_forma_pagamento, text='Formas de Pagamento para Editar')
    label_cadastro.pack(pady=20)

    botao_voltar = tk.Button(tela_editar_forma_pagamento, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_forma_pagamento))
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
def tela_modulo_forma_pagamento(tela, mostrar_tela, tela_menu_principal, frame_cadastrar_forma_pagamento, frame_mostrar_forma_pagamento, frame_editar_forma_pagamento, frame_apagar_forma_pagamento):
    label_modulo_forma_pagamento = tk.Label(tela, text='===== Módulo Forma de Pagamento =====')
    label_modulo_forma_pagamento.pack(pady=20)

    botao_cadastrar_forma_pagamento = tk.Button(tela, text='Cadastrar Forma de Pagamento', command=lambda: tela_cadastrar_forma_pagamento(frame_cadastrar_forma_pagamento, mostrar_tela, tela))
    botao_cadastrar_forma_pagamento.pack(pady=20)

    botao_mostrar_forma_pagamento = tk.Button(tela, text='Mostrar Formas de Pagamento', command=lambda: tela_mostrar_forma_pagamento(frame_mostrar_forma_pagamento, mostrar_tela, tela))
    botao_mostrar_forma_pagamento.pack(pady=20)

    botao_editar_forma_pagamento = tk.Button(tela, text='Editar Forma de Pagamento', command=lambda: tela_editar_forma_pagamento(frame_editar_forma_pagamento, mostrar_tela, tela))
    botao_editar_forma_pagamento.pack(pady=20)

    botao_apagar_forma_pagamento = tk.Button(tela, text='Apagar Forma de Pagamento', command=lambda: tela_apagar_forma_pagamento(frame_apagar_forma_pagamento, mostrar_tela, tela))
    botao_apagar_forma_pagamento.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)