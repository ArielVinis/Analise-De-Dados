import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
dados = {
    'Produto':['A', 'B', 'C'],
    'quantidade_vendida':[33, 50, 45]
    }

df = pd.DataFrame(dados)
# Gráfico de barras
df.plot(x='Produto', y='quantidade_vendida', kind='bar')
plt.show()

# Gráfico de pizza
df.plot(x='Produto', y='quantidade_vendida', kind='pie')
plt.show()

# Gráfico de linha
df.plot(x='Produto', y='quantidade_vendida', kind='line')
plt.show()