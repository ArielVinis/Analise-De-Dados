import sqlite3
# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()

# Passo 5: Atualizar informações de um funcionário
# Ganhou um aumento
atualizacao = ("João Silva", 5500.00, 1)

cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
conn.commit()