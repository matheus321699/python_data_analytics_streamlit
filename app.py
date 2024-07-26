import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from dataset import df
from graficos import table
from utils import format_number
from graficos import grafico_lucro_produtos, grafico_custos_produtos

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(['Dataset', 'Lucro e Vendas', 'Despesas'])
with aba1:
    st.dataframe(table)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Lucro Total', format_number(table['Lucro'].sum(), 'R$'))
        st.pyplot(grafico_lucro_produtos, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(table['Qtde de Unidades Vendidas'].sum()))
with aba3:
        st.metric('Custo Total', format_number(table['Custo Total'].sum()))
        st.pyplot(grafico_custos_produtos)