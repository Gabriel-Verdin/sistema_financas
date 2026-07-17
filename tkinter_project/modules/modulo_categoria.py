import tkinter as tk

def tela_mostrar_categoria(tela_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_categoria)

    # Limpa todos os widgets existentes
    for widget in tela_categoria.winfo_children():
        widget.destroy()
    
    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_categoria, text="Categorias")
    label_cadastro.pack(pady=20)

    botao_voltar = tk.Button(tela_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

def tela_modulo_categoria(tela, mostrar_tela, tela_menu_principal, frame_mostrar_categorias):
    label_modulo_categoria = tk.Label(tela, text='===== Módulo Categoria =====')
    label_modulo_categoria.pack(pady=20)

    botao_cadastrar_categoria = tk.Button(tela, text='Cadastrar Categoria', command=lambda: None)
    botao_cadastrar_categoria.pack(pady=20)

    botao_mostrar_categoria = tk.Button(tela, text='Mostrar Categorias', command=lambda: tela_mostrar_categoria(frame_mostrar_categorias, mostrar_tela, tela))
    botao_mostrar_categoria.pack(pady=20)

    botao_editar_categoria = tk.Button(tela, text='Editar Categoria', command=lambda: None)
    botao_editar_categoria.pack(pady=20)

    botao_apagar_categoria = tk.Button(tela, text='Apagar Categoria', command=lambda: None)
    botao_apagar_categoria.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)