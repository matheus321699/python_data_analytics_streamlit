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


lucro_meses = table.groupby('Mês')['Lucro'].sum().reset_index()
lucro_meses = lucro_meses.dropna(subset=['Mês'])

# Corrigindo o nome do mês "Abil" para "Abril"
lucro_meses['Mês'] = lucro_meses['Mês'].replace('Abil', 'Abril')

# Definindo a ordem correta dos meses
ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Convertendo a coluna 'Mês' para uma categoria com a ordem especificada
lucro_meses['Mês'] = pd.Categorical(lucro_meses['Mês'], categories=ordem_meses, ordered=True)

# Ordenando o DataFrame pela coluna 'Mês'
lucro_meses_ordenado = lucro_meses.sort_values('Mês')

plt.figure(figsize=(8, 4))
plt.plot(lucro_meses_ordenado['Mês'].astype(str), lucro_meses_ordenado['Lucro'], marker='o', linestyle='-', color='blue')
plt.title('Lucro nos meses do ano de 2019')
plt.xlabel('Meses')
plt.ylabel('Lucro')

# Configurar o eixo y para evitar notação científica
plt.gca().yaxis.set_major_formatter(FuncFormatter(formato_brasileiro))

# Rotacionar os valores do eixo x para melhorar a leitura, se necessário
plt.xticks(rotation=45, ha='right')

grafico_lucro_meses = plt.gcf()

quantidade_produtos_vendidos = table.groupby('Produto')['Qtde de Unidades Vendidas'].sum().reset_index()

plt.figure(figsize=(12,8))
plt.bar(quantidade_produtos_vendidos['Produto'], quantidade_produtos_vendidos['Qtde de Unidades Vendidas'], color='blue')
plt.title('Quantidade de Produtos Vendidos no ano de 2019')
plt.xlabel('Produtos')
plt.ylabel('Quantidade')
plt.gca().yaxis.set_major_formatter(FuncFormatter(formato_brasileiro))
grafico_produtos_vendidos = plt.gcf()