import matplotlib.pyplot as plt

import random

# Gerando dados aleatórios
# random.sample(range(100), k=20) vai te dar uma lista de 20 números aleatórios entre 0 e 99.
dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

# Criando o gráfico
plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo

# Exibindo o gráfico
plt.show()