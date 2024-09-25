import pandas as pd

# URL da lista de bancos falidos nos EUA
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

try:
    # Tenta ler todas as tabelas na página (se identificar as tabelas)
    dfs = pd.read_html(url)

    # Verifica quantas tabelas foram encontradas
    print(f"Número de tabelas encontradas: {len(dfs)}")

    # Se encontrar alguma, pega a primeira tabela
    if dfs:
        df_bancos = dfs[0]
        # print(df_bancos.head())
        print(df_bancos.shape)
        print(df_bancos.dtypes)

        df_bancos.head()
    else:
        print("Nenhuma tabela encontrada.")

except Exception as erro:
    print(f"Ocorreu um erro ao tentar ler a tabela: {erro}")
