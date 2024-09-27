import seaborn as sns
import matplotlib.pyplot as plt

# Configuração de estilo do Seaborn
sns.set(style="whitegrid") # opções: darkgrid, whitegrid, dark, white, ticks

# Carregamento do dataset 'tips'
df_tips = sns.load_dataset('tips')

# Configuração da figura e subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Criação de 3 gráficos de barras com estimadores diferentes
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
plt.show()