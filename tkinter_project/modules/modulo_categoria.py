import tkinter as tk

def tela_modulo_categoria(tela, mostrar_tela, tela_menu_principal):
    label_modulo_categoria = tk.Label(tela, text='===== Módulo Categoria =====')
    label_modulo_categoria.pack(pady=20)

    botao_cadastrar_categoria = tk.Button(tela, text='Cadastrar Categoria', command=lambda: None)
    botao_cadastrar_categoria.pack(pady=20)

    botao_mostrar_categoria = tk.Button(tela, text='Mostrar Categorias', command=lambda: None)
    botao_mostrar_categoria.pack(pady=20)

    botao_editar_categoria = tk.Button(tela, text='Editar Categoria', command=lambda: None)
    botao_editar_categoria.pack(pady=20)

    botao_apagar_categoria = tk.Button(tela, text='Apagar Categoria', command=lambda: None)
    botao_apagar_categoria.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)