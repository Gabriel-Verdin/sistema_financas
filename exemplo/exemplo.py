'''
Mini Sistema criado no Copilot como Base
'''
import sqlite3
from datetime import datetime

# Conexão com banco de dados
conn = sqlite3.connect("financas_teste.db")
cursor = conn.cursor()

# Criar tabela de transações
cursor.execute("""
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    descricao TEXT,
    categoria TEXT,
    tipo TEXT,
    forma TEXT,
    valor REAL
)
""")
conn.commit()

# Função para cadastrar transação
def cadastrar_transacao(descricao, categoria, tipo, forma, valor):
    data = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
    INSERT INTO transacoes (data, descricao, categoria, tipo, forma, valor)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (data, descricao, categoria, tipo, forma, valor))
    conn.commit()

    print('Transação cadastrada com sucesso!')

# Função para listar transações
def listar_transacoes():
    cursor.execute("SELECT * FROM transacoes")
    for row in cursor.fetchall():
        print(row)

# Função para calcular saldo
def calcular_saldo():
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Receita'")
    entradas = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Despesa'")
    saidas = cursor.fetchone()[0] or 0

    saldo = entradas - saidas
    print(f'Entradas: R$ {entradas:.2f}')
    print(f'Saídas: R$ {saidas:.2f}')
    print(f'Saldo Atual: R$ {saldo:.2f}')

# ------------------------------
# Exemplo de uso
# ------------------------------

# Cadastrar algumas transações
cadastrar_transacao("Salário CLT", "Trabalho", "Receita", "Pix", 2354.02)
cadastrar_transacao("Fatura Nubank", "Cartão", "Despesa", "Crédito", 440.00)
cadastrar_transacao("Notebook", "Itaú", "Despesa", "Crédito", 260.00)

# Listar todas
print('\nTransações registradas:')
listar_transacoes()

# Calcular saldo
print("\nResumo financeiro:")
calcular_saldo()