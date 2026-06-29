import sqlite3 
from datetime import datetime

# Conexão banco de dados
conn = sqlite3.connect("financas.db")
cursor = conn.cursor()

# Cria tabela forma_pagamento
cursor.execute("""
CREATE TABLE IF NOT EXISTS forma_pagamento (
    id_forma_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

# Cria tabela categoria
cursor.execute("""
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo_padrao TEXT NOT NULL
)
""")

# Criar tabela de transacao
cursor.execute("""
CREATE TABLE IF NOT EXISTS transacao (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    descricao TEXT,
    id_categoria INTEGER NOT NULL,
    tipo TEXT,
    id_forma_pagamento TEXT,
    valor REAL NOT NULL,
    entrada_saida TEXT,
    FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria) ON DELETE CASCADE,
    FOREIGN KEY (id_forma_pagamento) REFERENCES forma_pagamento (id_forma_pagamento) ON DELETE CASCADE
)
""")
conn.commit()

# ========================= Teste ========================= (Funciona)

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

# # Inserir transação
# cursor.execute("""
# INSERT INTO transacao (data, descricao, id_categoria, tipo, id_forma_pagamento, valor, entrada_saida)
# VALUES ('2026-06-20', 'Uber para CET', 1, 'Despesa', 1, 30.00, 'Saída')
# """)
# conn.commit()