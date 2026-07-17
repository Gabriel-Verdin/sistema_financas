import tkinter as tk

# Função para limpar os widgets da tela
def limpar_tela(tela):
    for widget in tela.winfo_children():
        widget.destroy()

# =============== Tela Cadastrar Categorias ===============
def tela_cadastrar_categoria(tela_cadastrar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_cadastrar_categoria)

    # Limpa widgets
    limpar_tela(tela_cadastrar_categoria)

    # Cria os widgets novamente
    label_cadastro = tk.Label(tela_cadastrar_categoria, text='Cadastro de Categorias')
    label_cadastro.pack(pady=20)

    botao_voltar = tk.Button(tela_cadastrar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Mostrar Categorias ===============
def tela_mostrar_categoria(tela_mostrar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_mostrar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_mostrar_categoria)
    
    # Cria os widgets novamente
    label_mostrar = tk.Label(tela_mostrar_categoria, text="Categorias")
    label_mostrar.pack(pady=20)

    botao_voltar = tk.Button(tela_mostrar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Editar Categorias ===============
def tela_editar_categoria(tela_editar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_editar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_editar_categoria)
    
    # Cria os widgets novamente
    label_mostrar = tk.Label(tela_editar_categoria, text="Categorias para Editar")
    label_mostrar.pack(pady=20)

    botao_voltar = tk.Button(tela_editar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

def tela_apagar_categoria(tela_apagar_categoria, mostrar_tela, tela_modulo_categoria):
    # Levanta a tela
    mostrar_tela(tela_apagar_categoria)

    # Limpa todos os widgets existentes
    limpar_tela(tela_apagar_categoria)
    
    # Cria os widgets novamente
    label_mostrar = tk.Label(tela_apagar_categoria, text="Categorias para Editar")
    label_mostrar.pack(pady=20)

    botao_voltar = tk.Button(tela_apagar_categoria, text='Voltar ao Módulo', command=lambda: mostrar_tela(tela_modulo_categoria))
    botao_voltar.pack(pady=20)

# =============== Tela Principal Categorias ===============
def tela_modulo_categoria(tela, mostrar_tela, tela_menu_principal, frame_mostrar_categorias, frame_cadastrar_categoria, frame_editar_categoria, frame_apagar_categoria):
    label_modulo_categoria = tk.Label(tela, text='===== Módulo Categoria =====')
    label_modulo_categoria.pack(pady=20)

    botao_cadastrar_categoria = tk.Button(tela, text='Cadastrar Categoria', command=lambda: tela_cadastrar_categoria(frame_cadastrar_categoria, mostrar_tela, tela))
    botao_cadastrar_categoria.pack(pady=20)

    botao_mostrar_categoria = tk.Button(tela, text='Mostrar Categorias', command=lambda: tela_mostrar_categoria(frame_mostrar_categorias, mostrar_tela, tela))
    botao_mostrar_categoria.pack(pady=20)

    botao_editar_categoria = tk.Button(tela, text='Editar Categoria', command=lambda: tela_editar_categoria(frame_editar_categoria, mostrar_tela, tela))
    botao_editar_categoria.pack(pady=20)

    botao_apagar_categoria = tk.Button(tela, text='Apagar Categoria', command=lambda: tela_apagar_categoria(frame_apagar_categoria, mostrar_tela, tela))
    botao_apagar_categoria.pack(pady=20)

    botao_voltar_menu_principal = tk.Button(tela, text='Voltar ao menu', command=lambda: mostrar_tela(tela_menu_principal))
    botao_voltar_menu_principal.pack(pady=20)