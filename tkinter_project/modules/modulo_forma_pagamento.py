import tkinter as tk

def tela_modulo_forma_pagamento(tela, mostrar_tela, tela_menu_principal):
    label_modulo_forma_pagamento = tk.Label(tela, text='===== Módulo Forma de Pagamento =====')
    label_modulo_forma_pagamento.pack(pady=20)

    botao_cadastrar_forma_pagamento = tk.Button(tela, text='Cadastrar Forma de Pagamento', command=lambda: None)
    botao_cadastrar_forma_pagamento.pack(pady=20)

    botao_mostrar_forma_pagamento = tk.Button(tela, text='Mostrar Formas de Pagamento', command=lambda: None)
    botao_mostrar_forma_pagamento.pack(pady=20)

    botao_editar_forma_pagamento = tk.Button(tela, text='Editar Forma de Pagamento', command=lambda: None)
    botao_editar_forma_pagamento.pack(pady=20)

    botao_apagar_forma_pagamento = tk.Button(tela, text='Apagar Forma de Pagamento', command=lambda: None)
    botao_apagar_forma_pagamento.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)