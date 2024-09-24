import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
# usando a função connect do módulo sqlite3 para se conectar a um banco de dados SQLite
# chamado "exemplo.db". Se o banco de dados não existir, ele será crido automaticamente.
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
# o cursor é usado para executar comandos SQL no banco de dados.
# Ele atua como uma espécie de ponteiro que percorre os resultados de consultas.
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
# define uma string create_table que contém um comando SQL para criar uma tabela chamada "Produtos".

create_table = """

CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
conn.commit()

# 6. Fechar a conexão com o banco de dados
conn.close()