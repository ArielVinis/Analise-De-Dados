import sqlite3
# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()

# Passo 3: Inserir um novo funcionário na tabela
novo_funcionario = (1, "João", "Analista", 5000.00)

cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)

conn.commit()