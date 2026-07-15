import tkinter as tk

def tela_modulo_categoria(tela, mostrar_tela, tela_menu_principal):
    label_modulo_categoria = tk.Label(tela, text='===== Módulo Categoria =====')
    label_modulo_categoria.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)