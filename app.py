import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from dataset import df
from graficos import table
from graficos_impostos import table3, total_impostos, grafico_impostos
from utils import format_number
from graficos import grafico_lucro_produtos, grafico_custos_produtos, grafico_lucro_meses, grafico_produtos_vendidos

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3, aba4 = st.tabs(['Dataset', 'Lucro e Vendas', 'Despesas', 'Impostos'])
with aba1:
    st.dataframe(table3)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Lucro Total', format_number(table['Lucro'].sum(), 'R$'))
        st.pyplot(grafico_lucro_produtos, use_container_width=True)
        st.pyplot(grafico_lucro_meses)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(table['Qtde de Unidades Vendidas'].sum()))
        st.pyplot(grafico_produtos_vendidos)
        
with aba3:
        st.metric('Custo Total', format_number(table['Custo Total'].sum()))
        st.pyplot(grafico_custos_produtos)

with aba4:
     st.metric('Total de Impostos no ano de 2019', format_number(total_impostos))
     st.pyplot(grafico_impostos)