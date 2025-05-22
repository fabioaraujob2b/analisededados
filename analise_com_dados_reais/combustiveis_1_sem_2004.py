import pandas as pd
import numpy as np

# Caminho para o arquivo
dados = 'base/ca-2004-01.csv'

# Leitura do CSV
df_ca = pd.read_csv(dados, sep=';', encoding='utf-8')

# Seleção das colunas relevantes
df_ca = df_ca[['Regiao - Sigla', 'Estado - Sigla', 'Valor de Venda', 'Valor de Compra']]

# Conversão das colunas numéricas
colunas_valores = ['Valor de Venda', 'Valor de Compra']
for col in colunas_valores:
    df_ca[col] = (
        df_ca[col]
        .astype(str)
        .str.replace(',', '.', regex=False)
        .str.strip()
        .replace('', np.nan)
        .astype(float)
    )

# Remove temporariamente os NaN para cálculo
venda = df_ca['Valor de Venda'].dropna()
compra = df_ca['Valor de Compra'].dropna()

# --- Estatísticas de Valor de Venda ---
media_valor_venda = np.mean(venda)
maior_valor_venda = np.max(venda)
menor_valor_venda = np.min(venda)
mediana_valor_venda = np.median(venda)
quartil_25_valor_venda = np.quantile(venda, 0.25)
quartil_75_valor_venda = np.quantile(venda, 0.75)
desvio_padrao_valor_venda = venda.std()
q1 = quartil_25_valor_venda
q3 = quartil_75_valor_venda
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers_vendas = df_ca[(df_ca['Valor de Venda'] < limite_inferior) | (df_ca['Valor de Venda'] > limite_superior)]

# --- Estatísticas de Valor de Compra ---
media_valor_compra = np.mean(compra)
maior_valor_compra = np.max(compra)
menor_valor_compra = np.min(compra)
mediana_valor_compra = np.median(compra)
quartil_25_valor_compra = np.quantile(compra, 0.25)
quartil_75_valor_compra = np.quantile(compra, 0.75)
desvio_padrao_valor_compra = compra.std()
q1_compra = quartil_25_valor_compra
q3_compra = quartil_75_valor_compra
iqr_compra = q3_compra - q1_compra
limite_inferior_compra = q1_compra - 1.5 * iqr_compra
limite_superior_compra = q3_compra + 1.5 * iqr_compra
outliers_compra = df_ca[(df_ca['Valor de Compra'] < limite_inferior_compra) | (df_ca['Valor de Compra'] > limite_superior_compra)]

# --- Impressão dos resultados ---
print('Análise de Vendas:')
print('----------------------------------')
print('Média do Valor de Venda:', round(media_valor_venda, 3))
print('Maior Valor de Venda:', round(maior_valor_venda, 3))
print('Menor Valor de Venda:', round(menor_valor_venda, 3))
print('Mediana do Valor de Venda:', round(mediana_valor_venda, 3))
print('Quartil 25 do Valor de Venda:', round(quartil_25_valor_venda, 3))
print('Quartil 75 do Valor de Venda:', round(quartil_75_valor_venda, 3))
print('Desvio Padrão do Valor de Venda:', round(desvio_padrao_valor_venda, 3))
print('Limite Inferior:', round(limite_inferior, 3))
print('Limite Superior:', round(limite_superior, 3))
if not outliers_vendas.empty:
    print('Outliers encontrados:')
    print(outliers_vendas)
else:
    print('Nenhum outlier encontrado.')

print('\nAnálise de Compras:')
print('----------------------------------')
print('Média do Valor de Compra:', round(media_valor_compra, 3))
print('Maior Valor de Compra:', round(maior_valor_compra, 3))
print('Menor Valor de Compra:', round(menor_valor_compra, 3))
print('Mediana do Valor de Compra:', round(mediana_valor_compra, 3))
print('Quartil 25 do Valor de Compra:', round(quartil_25_valor_compra, 3))
print('Quartil 75 do Valor de Compra:', round(quartil_75_valor_compra, 3))
print('Desvio Padrão do Valor de Compra:', round(desvio_padrao_valor_compra, 3))
print('Limite Inferior:', round(limite_inferior_compra, 3))
print('Limite Superior:', round(limite_superior_compra, 3))
if not outliers_compra.empty:
    print('Outliers encontrados:')
    print(outliers_compra)
else:
    print('Nenhum outlier encontrado.')
