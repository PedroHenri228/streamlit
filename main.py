import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dashboard de Dados', layout='wide')

st.title('Dashboard de Análise de Dados')

@st.cache_data
def carregar_dados():
    
    try:
        df = pd.read_json('dados.json')
        return df
    except Exception as e:
        st.error(f'Erro ao carregar os dados: {e}')
        return pd.DataFrame()

dados = carregar_dados()

if not dados.empty:
    st.subheader('Tabela de Dados')
    st.dataframe(dados)

    st.subheader('Distribuição de Salários')
    st.bar_chart(dados[['Nome', 'Salário']].set_index('Nome'))

    st.subheader('Idade vs Salário')
    st.line_chart(dados[['Idade', 'Salário']])

    st.subheader('Estatísticas Básicas')
    st.write(dados.describe())
else:
    st.warning('Nenhum dado disponível para exibir.')

url = 'https://raw.githubusercontent.com/PedroHenri228/streamlit/main/resultados.csv'
