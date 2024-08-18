import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dashboard de Dados', layout='wide')

st.title('Dashboard de Análise de Dados')

@st.cache_data
def carregar_dados():
    url = 'https://raw.githubusercontent.com/PedroHenri228/streamlit/main/dados.xlsx'
    df = pd.read_excel(url, engine='openpyxl')
    return df

dados = carregar_dados()

st.subheader('Tabela de Dados')
st.dataframe(dados)

st.subheader('Distribuição de Salários')
st.bar_chart(dados[['Nome', 'Salário']].set_index('Nome'))

st.subheader('Idade vs Salário')
st.line_chart(dados[['Idade', 'Salário']])

st.subheader('Estatísticas Básicas')
st.write(dados.describe())
