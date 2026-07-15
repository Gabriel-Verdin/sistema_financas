import tkinter as tk

from modules import modulo_transacao

# Janela Principal
janela_principal = tk.Tk()
janela_principal.title('Sistema Finanças')
janela_principal.geometry('800x600') # Largura x Altura

# Função para trocar de módulo
def mostrar_tela(tela_modulo):
    tela_modulo.tkraise()

# Criação dos frames (Módulos)
tela_menu_principal = tk.Frame(janela_principal)
tela_modulo_transacao = tk.Frame(janela_principal)
tela_modulo_categoria = tk.Frame(janela_principal)
tela_modulo_forma_pagamento = tk.Frame(janela_principal)

# for aplica a mesma configuração em todos os frames (evita reoetição)
for frame in (tela_menu_principal, tela_modulo_transacao, tela_modulo_categoria, tela_modulo_forma_pagamento):
    frame.grid(row=0, column=0, sticky='nsew')

# ==============================================
# =============== Menu Principal ===============
# ==============================================
label_menu_principal = tk.Label(tela_menu_principal, text='===== Menu Principal =====')
label_menu_principal.pack(pady=20)

botao_modulo_transacao = tk.Button(tela_menu_principal, text='Módulo Transação', width=20, height=2, command=lambda: mostrar_tela(tela_modulo_transacao))
botao_modulo_transacao.pack()

# ================================================
# =============== Módulo Transação ===============
# ================================================
modulo_transacao.frame_modulo_transacao(tela_modulo_transacao, mostrar_tela, tela_menu_principal)

mostrar_tela(tela_menu_principal)

janela_principal.mainloop()