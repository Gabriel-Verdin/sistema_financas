from functions import categorias, forma_pagamento

# Valida se valor que deveria ser int é realmente int
def str_para_int(valor_str):
    try:
        return int(valor_str)
    except ValueError:
       print('Digite um valor válido')
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
    if id_categoria == None:
        print('Erro! Categoria escolhida é inválida!')
        return None
    if id_categoria > len(categorias.listar_categorias()) or id_categoria < 0:
        print('Erro! Categoria escolhida é inválida!')
        return None
    else:
        print('Categoria escolhida!')
        return True

# Valida se a escolha da forma de pagamento é válida ou não
def escolha_valida_forma_pagamento(id_forma_pagamento):
    if id_forma_pagamento == None:
        print('Erro! Forma de pagamento escolhida é inválida!')
        return None
    if id_forma_pagamento > len(forma_pagamento.listar_forma_pagamento()) or id_forma_pagamento < 0:
        print('Erro! Forma de pagamento escolhida é inválida!')
        return None
    else:
        print('Forma de pagamento escolhida!')
        return True
    
# Valida se o tipo é despesa ou receita
def despesa_ou_receita(tipo_categoria=str):
    if tipo_categoria != 'despesa' and tipo_categoria != 'receita':
        print('Digite um tipo válido (Despesa ou Receita)!')
        return None
    
    else:
        print('Tipo salvo com sucesso!')
        return tipo_categoria.capitalize()