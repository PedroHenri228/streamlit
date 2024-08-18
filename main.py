import streamlit as st
import pandas as pd


st.set_page_config(page_title='Testando o Streamlit')

with st.container():
    st.subheader("MEu primeiro site com o Streamlit")
    st.title("Dashboard")
    
@st.cache_data

def carregar_dados():
    tabela = pd.read_csv("layout/resultados.csv")
    
    return tabela


with st.container():
    st.write("---")
    
    dados = carregar_dados()
    
    st.area_chart(dados, x='Nome', y='Idade')
