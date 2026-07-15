import tkinter as tk

# Criar janela 
janela = tk.Tk()
janela.title('Sistema Financeiro')
janela.geometry('800x600') # Largura x Altura

# ==========================================================
# ======================= Exemplo 01 =======================
# ==========================================================
# label = tk.Label(janela, text='Olá Mundo!')
# label.pack()

# botao = tk.Button(janela, text='Clique aqui', command=lambda: print('Botao clicado'))
# botao.pack()
# 

# ==========================================================
# ======================= Exemplo 02 =======================
# ==========================================================
# Adicionar elementos
# label = tk.Label(janela, text='Bem vindo ao tkinter')
# label.pack(pady=10)

# entrada = tk.Entry(janela)
# entrada.pack(pady=5)

# def mostrar_texto():
#     texto = entrada.get()
#     label.config(text=f'Você digitou {texto}')

# botao = tk.Button(janela, text='Enviar', command=mostrar_texto)
# botao.pack(pady=10)    
# 

# ==========================================================
# ======================= Exemplo 03 =======================
# ==========================================================
# Função para trocar de tela
def mostrar_tela(tela):
    tela.tkraise()

# Criar frames (telas)
tela1 = tk.Frame(janela)
tela2 = tk.Frame(janela)

for frame in (tela1, tela2):
    frame.grid(row=0, column=0, sticky="nsew")

# Conteúdo da tela 1
label1 = tk.Label(tela1, text="Tela 1 - Menu Principal")
label1.pack(pady=20)

botao1 = tk.Button(tela1, text="Ir para Tela 2", width=20, height=2,
                   command=lambda: mostrar_tela(tela2))
botao1.pack()

# Conteúdo da tela 2
label2 = tk.Label(tela2, text="Tela 2 - Configurações")
label2.pack(pady=20)

botao2 = tk.Button(tela2, text="Voltar para Tela 1", width=20, height=2,
                   command=lambda: mostrar_tela(tela1))
botao2.pack()

# Mostrar tela inicial
mostrar_tela(tela1)

# Loop principal
janela.mainloop()