import streamlit as st
import pandas as pd

st.title("Carros mercado livre - Bahia")

df = pd.read_csv("./data/data_tratado.csv")
df1 = pd.read_csv("./data/data.csv")

# df["ano"] = df["ano"].astype(str)

st.selectbox("Escolha o ano", df["ano"].unique())
st.dataframe(df.head())
st.dataframe(df1.head())