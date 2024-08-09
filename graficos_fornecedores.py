import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from utils import formato_brasileiro

table2 = pd.read_excel('database/gastos_trimestrais_fornecedores.xlsx')

table2

