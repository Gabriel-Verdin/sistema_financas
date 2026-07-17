import tkinter as tk

# Função para limpar os widgets da tela
def limpar_tela(tela):
    for widget in tela.winfo_children():
        widget.destroy()

# =============== Tela Cadastrar Transações ===============
def tela_cadastrar_transacao(tela_cadastrar_transacao, mostrar_tela, tela_modulo_transacao):
    # Levanta a tela
    mostrar_tela(tela_cadastrar_transacao)

    # Limpa widgets
    limpar_tela(tela_cadastrar_transacao)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_cadastrar_transacao, text='Cadastro de Transações')
    label_cadastro.pack(pady=20)

    botao_voltar = tk.Button(tela_cadastrar_transacao, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_transacao))
    botao_voltar.pack(pady=20)

# =============== Tela Mostrar Transações ===============
def tela_mostrar_transacao(tela_mostrar_transacao, mostrar_tela, tela_modulo_transacao):
    # Levanta a tela
    mostrar_tela(tela_mostrar_transacao)

    # Limpa widgets
    limpar_tela(tela_mostrar_transacao)

    # Cria os widgets novamente
    label_mostrar = tk.Label(tela_mostrar_transacao, text='Transações')
    label_mostrar.pack(pady=20)

    botao_voltar = tk.Button(tela_mostrar_transacao, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_transacao))
    botao_voltar.pack(pady=20)

# =============== Tela Editar Transações ===============
def tela_editar_transacao(tela_editar_transacao, mostrar_tela, tela_modulo_transacao):
    # Levanta a tela
    mostrar_tela(tela_editar_transacao)

    # Limpa widgets
    limpar_tela(tela_editar_transacao)

    # Cria os widgets novamente
    label_editar = tk.Label(tela_editar_transacao, text='Transações para Editar')
    label_editar.pack(pady=20)

    botao_voltar = tk.Button(tela_editar_transacao, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_transacao))
    botao_voltar.pack(pady=20)

# =============== Tela Apagar Transações ===============
def tela_apagar_transacao(tela_apagar_transacao, mostrar_tela, tela_modulo_transacao):
    # Levanta a tela
    mostrar_tela(tela_apagar_transacao)

    # Limpa widgets
    limpar_tela(tela_apagar_transacao)

    # Cria os widgets novamente
    label_editar = tk.Label(tela_apagar_transacao, text='Transações para Apagar')
    label_editar.pack(pady=20)

    botao_voltar = tk.Button(tela_apagar_transacao, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_transacao))
    botao_voltar.pack(pady=20)

# =============== Tela Principal Transações ===============
def tela_modulo_transacao(tela, mostrar_tela, tela_menu_principal, frame_cadastrar_transacao, frame_mostrar_transacoes, frame_editar_transacao, frame_apagar_transacao):
    label_modulo_transacao = tk.Label(tela, text='===== Módulo Transação =====')
    label_modulo_transacao.pack(pady=20)

    botao_cadastrar_transacao = tk.Button(tela, text='Cadastrar Transação', command=lambda: tela_cadastrar_transacao(frame_cadastrar_transacao, mostrar_tela, tela))
    botao_cadastrar_transacao.pack(pady=20)

    botao_mostrar_transacao = tk.Button(tela, text='Mostrar Transações', command=lambda: tela_mostrar_transacao(frame_mostrar_transacoes, mostrar_tela, tela))
    botao_mostrar_transacao.pack(pady=20)

    botao_editar_transacao = tk.Button(tela, text='Editar Transação', command=lambda: tela_editar_transacao(frame_editar_transacao, mostrar_tela, tela))
    botao_editar_transacao.pack(pady=20)

    botao_apagar_transacao = tk.Button(tela, text='Apagar Transação', command=lambda: tela_apagar_transacao(frame_apagar_transacao, mostrar_tela, tela))
    botao_apagar_transacao.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)