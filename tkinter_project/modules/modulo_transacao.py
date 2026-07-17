import tkinter as tk

# Função para limpar os widgets da tela
def limpar_tela(tela):
    for widget in tela.winfo_children():
        widget.destroy()

# =============== Tela Cadastrar Transação ===============
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

# =============== Tela Principal Transações ===============
def tela_modulo_transacao(tela, mostrar_tela, tela_menu_principal, frame_cadastrar_transacao):
    label_modulo_transacao = tk.Label(tela, text='===== Módulo Transação =====')
    label_modulo_transacao.pack(pady=20)

    botao_cadastrar_transacao = tk.Button(tela, text='Cadastrar Transação', command=lambda: tela_cadastrar_transacao(frame_cadastrar_transacao, mostrar_tela, tela))
    botao_cadastrar_transacao.pack(pady=20)

    botao_mostrar_transacao = tk.Button(tela, text='Mostrar Transações', command=lambda: None)
    botao_mostrar_transacao.pack(pady=20)

    botao_editar_transacao = tk.Button(tela, text='Editar Transação', command=lambda: None)
    botao_editar_transacao.pack(pady=20)

    botao_apagar_transacao = tk.Button(tela, text='Apagar Transação', command=lambda: None)
    botao_apagar_transacao.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)