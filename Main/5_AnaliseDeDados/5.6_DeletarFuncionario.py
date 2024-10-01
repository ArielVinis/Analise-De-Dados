import sqlite3
# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()

# Passo 6: Deletar um funcionário da tabela
# João será demitido.
id_funcionario_para_deletar = 1

cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))

conn.commit()