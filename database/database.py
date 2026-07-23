import sqlite3 

# Conexão banco de dados
conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# Cria tabela forma_pagamento
def criar_tabela_forma_pagamento():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forma_pagamento (
        id_forma_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)
    conn.commit()

# Cria tabela categoria
def criar_tabela_categoria():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo_padrao TEXT NOT NULL
    )
    """)
    conn.commit()

# Criar tabela de transacao
def criar_tabela_transacao():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacao (
        id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        descricao TEXT,
        id_categoria INTEGER NOT NULL,
        id_forma_pagamento TEXT,
        valor REAL NOT NULL,
        entrada_saida TEXT,
        FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria) ON DELETE CASCADE,
        FOREIGN KEY (id_forma_pagamento) REFERENCES forma_pagamento (id_forma_pagamento) ON DELETE CASCADE
    )
    """)
    conn.commit()

# Inserir dados padrão no banco
def inserir_dados_padrao():
    # Inserir categoria
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", ('Uber', 'Despesa')) # 1
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", ('Salário', 'Receita')) # 2
    cursor.execute("INSERT INTO categoria (nome, tipo_padrao) VALUES (?, ?)", ('Ifood', 'Despesa')) # 3
    conn.commit()

    # Inserir forma_pagamento
    cursor.execute("INSERT INTO forma_pagamento (nome) VALUES ('Crédito')") # 1
    cursor.execute("INSERT INTO forma_pagamento (nome) VALUES ('Débito')") # 2
    cursor.execute("INSERT INTO forma_pagamento (nome) VALUES ('PIX')") # 3
    cursor.execute("INSERT INTO forma_pagamento (nome) VALUES ('Dinheiro')") # 4
    conn.commit()

    # Inserir transação
    cursor.execute("""
    INSERT INTO transacao (data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida)
    VALUES ('20-06-2026', 'Uber para CET', 1, 1, 30.00, 'Saida')
    """)
    cursor.execute("""
    INSERT INTO transacao (data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida)
    VALUES ('20-07-2026', 'Ifood', 3, 2, 96.42, 'Saida')
    """)
    cursor.execute("""
    INSERT INTO transacao (data, descricao, id_categoria, id_forma_pagamento, valor, entrada_saida)
    VALUES ('05-07-2026', 'Salario dia 5', 2, 3, 1100, 'Entrada')
    """)
    conn.commit()

def inicializar_banco():
    criar_tabela_forma_pagamento()
    criar_tabela_categoria()
    criar_tabela_transacao()
    inserir_dados_padrao()

    print('Banco inicializado com sucesso!')

inicializar_banco()