import sqlite3
# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()

# Passo 4: Consultar e exibir funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

print("Funcionários Cadastrados:")
for funcionario in funcionarios:
    print(funcionario)