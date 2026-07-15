import tkinter as tk

def frame_modulo_transacao(frame, mostrar_tela, tela_menu_principal):
    label_modulo_transacao = tk.Label(frame, text='===== Módulo Transação =====')
    label_modulo_transacao.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(frame, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)