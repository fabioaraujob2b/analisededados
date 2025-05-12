import pandas as pd

dados = {
    'Nome': ['Ana', 'Beto', 'Carlos', 'Diana'],
    'Idade': [23, 34, 45, 29],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df = pd.DataFrame(dados)
#print(df)

#print(df.head())    # Primeiras 5 linhas do DataFrame
#print(df.tail())    # Últimas 5 linhas do DataFrame
#print(df.shape)     # Dimensões do DataFrame (linhas, colunas)  
#print(df.columns)   # Nomes das colunas
#print(df.dtypes)    # Tipos de dados
#print(df.info())    # Informações gerais do DataFrame

print(df['Nome'])    # Acessa a coluna 'Nome'
print(df[['Nome', 'Cidade']])  # Acessa as colunas 'Nome' e 'Idade'

print(df.iloc[0])    # Acessa a primeira linha do DataFrame
print(df.iloc[0])  # Acessa a primeira linha do DataFrame

#Fatiamento
print(df.iloc[0:2])  # Linhas da 0 até 1 (não inclui 2)

#Filtrando dados
print(df[df['Idade'] > 30])  # Filtra linhas onde a idade é maior que 30
print(df[df['Cidade'] == 'São Paulo'])  # Filtra linhas onde a cidade é São Paulo