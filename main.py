import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title='Testando o Streamlit')

# Cabeçalho e título
with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard")

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("layout/resultados.csv")
    return tabela

# Exibição do gráfico
with st.container():
    st.write("---")
    dados = carregar_dados()
    st.area_chart(dados, x='Nome', y='Idade')
