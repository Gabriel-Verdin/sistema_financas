import tkinter as tk

def tela_modulo_transacao(tela, mostrar_tela, tela_menu_principal):
    label_modulo_transacao = tk.Label(tela, text='===== Módulo Transação =====')
    label_modulo_transacao.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)