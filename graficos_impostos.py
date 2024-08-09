import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from utils import formato_brasileiro

table3 = pd.read_excel('database/impostos_empresa_2019.xlsx')

total_impostos = table3['Imposto de Renda'].sum() + table3['ICMS'].sum() + table3['ISS'].sum()

imposto_renda_total = table3['Imposto de Renda'].sum()
icms_total = table3['ICMS']
iss_total = table3['ISS']

data = {
        'Impostos': ['Imposto de Renda', 'ICMS', 'ISS'],
        'Total': [imposto_renda_total, icms_total, iss_total],
}

table_impostos_total = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.bar(table_impostos_total['Impostos'].astype(str), table_impostos_total['Total'], color='blue')
plt.title('Impostos totais no ano de 2019')
plt.xlabel('Total')
plt.gca().yaxis.set_major_formatter(FuncFormatter(formato_brasileiro))
grafico_impostos = plt.gcf()