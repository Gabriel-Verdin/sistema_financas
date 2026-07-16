import tkinter as tk

def tela_modulo_transacao(tela, mostrar_tela, tela_menu_principal):
    label_modulo_transacao = tk.Label(tela, text='===== Módulo Transação =====')
    label_modulo_transacao.pack(pady=20)

    botao_cadastrar_transacao = tk.Button(tela, text='Cadastrar Transação', command=lambda: None)
    botao_cadastrar_transacao.pack(pady=20)

    botao_mostrar_transacao = tk.Button(tela, text='Mostrar Transações', command=lambda: None)
    botao_mostrar_transacao.pack(pady=20)

    botao_editar_transacao = tk.Button(tela, text='Editar Transação', command=lambda: None)
    botao_editar_transacao.pack(pady=20)

    botao_apagar_transacao = tk.Button(tela, text='Apagar Transação', command=lambda: None)
    botao_apagar_transacao.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)