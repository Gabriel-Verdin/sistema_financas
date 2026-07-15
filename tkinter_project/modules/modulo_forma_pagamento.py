import tkinter as tk

def tela_modulo_forma_pagamento(tela, mostrar_tela, tela_menu_principal):
    label_modulo_forma_pagamento = tk.Label(tela, text='===== Módulo Forma de Pagamento =====')
    label_modulo_forma_pagamento.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)