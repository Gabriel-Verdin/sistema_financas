def str_para_int(valor_str):
    try:
        return int(valor_str)
    except ValueError:
       print('Digite um valor válido')
       return None