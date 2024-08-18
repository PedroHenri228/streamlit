import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title='Dashboard de Dados', layout='wide')

# Cabeçalho do dashboard
st.title('Dashboard de Análise de Dados')

# Função para carregar os dados do Excel
@st.cache_data
def carregar_dados():
    df = pd.read_excel('https://github.com/PedroHenri228/streamlit/edit/main/dados.xlsx')
    return df

# Carregar os dados
dados = carregar_dados()

# Mostrar os dados em uma tabela
st.subheader('Tabela de Dados')
st.dataframe(dados)

# Criar um gráfico de barras para mostrar a distribuição de salários
st.subheader('Distribuição de Salários')
st.bar_chart(dados[['Nome', 'Salário']].set_index('Nome'))

# Criar um gráfico de linha para mostrar a relação entre Idade e Salário
st.subheader('Idade vs Salário')
st.line_chart(dados[['Idade', 'Salário']])

# Exibir estatísticas básicas
st.subheader('Estatísticas Básicas')
st.write(dados.describe())
