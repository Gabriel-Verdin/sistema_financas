import unicodedata
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from functions import function_categorias
# from functions import forma_pagamento, transacoes

# Valida se valor que deveria ser int é realmente int
def str_para_int(valor_str):
    try:
        return int(valor_str)
    except ValueError:
       messagebox.showerror('Erro','Digite um valor válido')
       return None

# Valida se valor que deveria ser float é realmente int
def str_para_float(valor_str):
    try:
        return float(valor_str)
    except ValueError:
       print('Digite um valor válido')
       return None
    
# Valida se a escolha da categoria é válida ou não
def escolha_valida_categoria(id_categoria):
    id_categoria_int = str_para_int(id_categoria)
    if id_categoria_int == None:
        messagebox.showerror('Erro!', 'Categoria escolhida é inválida!')
        # print('Erro! Categoria escolhida é inválida!')
        return None
    if id_categoria_int > len(function_categorias.listar_categorias()) or id_categoria_int <= 0:
        messagebox.showerror('Erro!', 'Categoria escolhida é inválida!')
        # print('Erro! Categoria escolhida é inválida!')
        return None
    else:
        # messagebox.showinfo('Sucesso!', 'Categoria escolhida!')
        # print('Categoria escolhida!')
        return id_categoria_int

# Valida se a escolha da forma de pagamento é válida ou não
# def escolha_valida_forma_pagamento(id_forma_pagamento):
#     if id_forma_pagamento == None:
#         print('Erro! Forma de pagamento escolhida é inválida!')
#         return None
#     if id_forma_pagamento > len(forma_pagamento.listar_forma_pagamento()) or id_forma_pagamento <= 0:
#         print('Erro! Forma de pagamento escolhida é inválida!')
#         return None
#     else:
#         print('Forma de pagamento escolhida!')
#         return True
    
# # Valida se a escolha da transação é válida ou não
# def escolha_valida_transacao(id_transacao):
#     if id_transacao == None:
#         print('Erro! Transação escolhida é inválida!')
#         return None
#     if id_transacao > len(transacoes.listar_transacoes()) or id_transacao <= 0:
#         print('Erro! Transação escolhida é inválida!')
#         return None
#     else:
#         print('Transação escolhida!')
#         return True

# Remove acentos
def remover_acentos(texto=str):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto) # Decompõe caracteres 'á' vira 'a' + '´'
        if unicodedata.category(c) != 'Mn' # Mantém apenas o que não é acento
    ) # join junta tudo (mão vira mao)

# Valida se é entrada ou saída
def entrada_ou_saida(entrada_saida_sem_acento=str):
    if entrada_saida_sem_acento != 'entrada' and entrada_saida_sem_acento != 'saida':
        print('Digite um texto válido (Entrada ou Saída)!')
        return None
    
    else:
        print('Salvo com sucesso!')
        return entrada_saida_sem_acento.capitalize()

# Valida se o tipo é despesa ou receita
def despesa_ou_receita(tipo_categoria=str):
    if tipo_categoria != 'despesa' and tipo_categoria != 'receita':
        # print('Digite um tipo válido (Despesa ou Receita)!')
        messagebox.showerror('Erro','Digite um tipo válido (Despesa ou Receita)!')
        return None
    
    else:
        # print('Tipo salvo com sucesso!')
        return tipo_categoria.capitalize()
    
# Valida Valores de entrada e saída
def validar_valor(valor):
    if valor <= 0: 
        print('Digite um valor válido (Maior que 0)')
        return None

    else:
        return valor
    
# Valida entrada da data
def validar_data(data_str):
    if not data_str:
        return datetime.now().strftime("%d-%m-%Y")
    
    try:
        # Tenta converter para o formato dia/mês/ano
        data = datetime.strptime(data_str, "%d/%m/%Y")
        hoje = datetime.now()

        if data > hoje:
            print('Data inválida! Não pode ser maior que hoje.')
            return None
    
        return data.strftime("%d-%m-%Y") # Padroniza para salvar no banco
    
    except ValueError:
        print('Data inválida! Use o formato válido (ex: 01/01/1990)')
        return None