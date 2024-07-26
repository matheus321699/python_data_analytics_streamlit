import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
import seaborn as sns

table = pd.read_excel('database/Base_de_Dados.xlsx')
table

produtos = table['Produto'].unique()
produtos

lucro_produtos = table.groupby('Produto')['Lucro'].sum().reset_index()
lucro_produtos

# Função de formatação para notação brasileira
def formato_brasileiro(x, pos):
    return f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

plt.figure(figsize=(12, 4))
plt.bar(lucro_produtos['Produto'], lucro_produtos['Lucro'], color='blue')
plt.xlabel('Produtos')
plt.ylabel('Lucro')
plt.title('Lucro dos Produtos no Ano de 2019')

# Configurar o eixo y para evitar notação científica
plt.gca().yaxis.set_major_formatter(FuncFormatter(formato_brasileiro))

# Rotacionar os valores do eixo y para melhorar a leitura, se necessário
# plt.xticks(rotation=45, ha='right')
grafico_lucro_produtos = plt.gcf()
grafico_lucro_produtos.show()

custos_produtos_agrupados = table.groupby('Produto')['Custo Total'].sum().reset_index()
custos_produtos_agrupados

plt.figure(figsize=(12,6))
plt.bar(custos_produtos_agrupados['Produto'], custos_produtos_agrupados['Custo Total'], color='blue')
plt.xlabel('Produtos')
plt.ylabel('Custos')
plt.title('Custos dos Produtos no Ano de 2019')

plt.gca().yaxis.set_major_formatter(FuncFormatter(formato_brasileiro))
grafico_custos_produtos = plt.gcf()
