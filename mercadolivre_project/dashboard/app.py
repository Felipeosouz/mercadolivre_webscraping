import streamlit as st
import pandas as pd
import plotly.express as px
import os 
# os.path.abspath("data/data_tratado.csv" )
st.title("Carros no mercado livre - Bahia")
st.subheader("10 primeira páginas")

csv_file = os.path.abspath("mercadolivre_project/data/data_tratado.csv")
df = pd.read_csv(csv_file)
print(csv_file)

st.sidebar.title("Filtros")

anos = ["Todos os anos"] + sorted(df["ano"].unique(), reverse=True)
ano_selecionado = st.sidebar.selectbox('Ano do carro', anos)

marcas = ["Todas as marcas"] + sorted(df['marca'].unique())
marca_selecionada = st.sidebar.selectbox('Marca do carro', marcas)

preco_min, preco_max = st.sidebar.slider('Faixa de Preço', int(df['preco'].min()), int(df['preco'].max()), (int(df['preco'].min()), int(df['preco'].max())))

km_min, km_max = st.sidebar.slider('Kilometros rodados', int(df['km'].min()), int(df['km'].max()), (int(df['km'].min()), int(df['km'].max())))

if ano_selecionado == "Todos os anos" and marca_selecionada != "Todas as marcas":
    df_filtrado = df[(df['marca'] == marca_selecionada) & 
                     (df['preco'] >= preco_min) & 
                     (df['preco'] <= preco_max) & 
                     (df['km'] >= km_min) & 
                     (df['km'] <= km_max)]

if marca_selecionada == "Todas as marcas" and ano_selecionado != "Todos os anos":
    df_filtrado = df[(df['ano'] == ano_selecionado) &
                     (df['preco'] >= preco_min) & 
                     (df['preco'] <= preco_max) & 
                     (df['km'] >= km_min) & 
                     (df['km'] <= km_max)]
if ano_selecionado == "Todos os anos" and marca_selecionada == "Todas as marcas":
    df_filtrado = df[(df['preco'] >= preco_min) &
                     (df['preco'] <= preco_max) & 
                     (df['km'] >= km_min) & 
                     (df['km'] <= km_max)]
if ano_selecionado != "Todos os anos" and marca_selecionada != "Todas as marcas":
    df_filtrado = df[(df['ano'] == ano_selecionado) &
                     (df['marca'] == marca_selecionada) & 
                     (df['preco'] >= preco_min) & 
                     (df['preco'] <= preco_max) & 
                     (df['km'] >= km_min) & 
                     (df['km'] <= km_max)]
st.subheader('Anúncios Filtrados')

 # Métricas
st.subheader('Métricas')
total_anuncios = len(df_filtrado)
total_marcas = len(df_filtrado['marca'].unique())
total_anos = len(df_filtrado['ano'].unique())

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Anúncios", value=total_anuncios)
with col2:
    st.metric(label="Total de Marcas", value=total_marcas)
with col3:
    st.metric(label="Total de Anos", value=total_anos)

st.dataframe(df_filtrado, 
            column_config={
            "ano": st.column_config.NumberColumn(
            "ano",
            help="Ano do veículo",
            format="%d",
            ),"preco": st.column_config.NumberColumn(
            "preco",
            help="Preço do veículo",
            format="R$ %2f",
            ),"km": st.column_config.NumberColumn(
            "km",
            help="Kilometros rodados do veículo",
            format="%d",
            )
            })

 # Gráficos de Distribuição com Plotly
st.subheader('Distribuição de Preços')
fig_preco = px.histogram(df_filtrado, x='preco', nbins=30, title='Distribuição de Preços')
fig_preco.update_layout(xaxis_title='Preço', yaxis_title='Quantidade de Anúncios')
st.plotly_chart(fig_preco, use_container_width=True)

st.subheader('Distribuição de Anos')
fig_ano = px.histogram(df_filtrado, x='ano', title='Distribuição de Anos')
fig_ano.update_layout(xaxis_title='Ano', yaxis_title='Quantidade de Anúncios')
st.plotly_chart(fig_ano, use_container_width=True)