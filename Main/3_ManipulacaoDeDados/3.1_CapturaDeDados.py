import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

print(df_selic.info())
print(df_selic)
print("-------------------------------------------------------------")

# -------------------------------

#verificar duplicidade de linhas (passo muito importante), utilizando a função drop_duplicates()
df_selic.drop_duplicates(keep='last', inplace=True)
# mantém o último registro (keep+'last')
# através do parâmetro inplace=True, faz com que a transformação seja salva do DataFrame
# no nosso caso, não existem linhas duplicadas.
print(df_selic)
print("-------------------------------------------------------------")

# -------------------------------

from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Ariel"

print(df_selic.info())
df_selic.head(10) #Você pode escolher quantas linhas quer que apareça
print("-------------------------------------------------------------")

#--------------------------------

# "loc" Localiza a linha que você deseja
df_selic.loc[9389]
print("-------------------------------------------------------------")

#---------------------------------

df_selic.loc[[0,20,70]]
print("-------------------------------------------------------------")

#--------------------------------

teste = df_selic['valor'] < 0.01

print(type(teste))