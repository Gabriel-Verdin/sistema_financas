import tkinter as tk

from modules import modulo_transacao, modulo_categoria, modulo_forma_pagamento

# Janela Principal
janela_principal = tk.Tk()
janela_principal.title('Sistema Finanças')
janela_principal.geometry('800x600') # Largura x Altura

# Função para trocar de módulo
def mostrar_tela(tela_modulo):
    tela_modulo.tkraise()

# Função para criar telas
def criar_tela(tela):
    tela = tk.Frame(tela)    
    tela.grid(row=0, column=0, sticky='nsew') # aplica a mesma configuração em todos os frames (evita repetição)
    return tela

# Criação dos frames (Módulos)
frame_menu_principal = criar_tela(janela_principal)
frame_modulo_transacao = criar_tela(janela_principal)

frame_modulo_categoria = criar_tela(janela_principal)
frame_mostrar_categorias = criar_tela(janela_principal)

frame_modulo_forma_pagamento = criar_tela(janela_principal)

# ==============================================
# =============== Menu Principal ===============
# ==============================================
label_menu_principal = tk.Label(frame_menu_principal, text='===== Menu Principal =====')
label_menu_principal.pack(pady=20)

botao_modulo_transacao = tk.Button(frame_menu_principal, text='Módulo Transação', width=25, height=2, command=lambda: mostrar_tela(frame_modulo_transacao))
botao_modulo_transacao.pack()

botao_modulo_categoria = tk.Button(frame_menu_principal, text='Módulo Categoria', width=25, height=2, command=lambda: mostrar_tela(frame_modulo_categoria))
botao_modulo_categoria.pack()

botao_modulo_forma_pagamento = tk.Button(frame_menu_principal, text='Módulo Forma de Pagamento', width=25, height=2, command=lambda: mostrar_tela(frame_modulo_forma_pagamento))
botao_modulo_forma_pagamento.pack()

# ========================================================
# =================== Módulo Transação ===================
# ========================================================
modulo_transacao.tela_modulo_transacao(frame_modulo_transacao, mostrar_tela, frame_menu_principal)

# ========================================================
# =================== Módulo Categoria ===================
# ========================================================
modulo_categoria.tela_modulo_categoria(frame_modulo_categoria, mostrar_tela, frame_menu_principal, frame_mostrar_categorias)

# =========================================================
# =============== Módulo Forma de Pagamento ===============
# =========================================================
modulo_forma_pagamento.tela_modulo_forma_pagamento(frame_modulo_forma_pagamento, mostrar_tela, frame_menu_principal)

# 
mostrar_tela(frame_menu_principal)

janela_principal.mainloop()