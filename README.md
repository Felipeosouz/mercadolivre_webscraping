# 🚗 Análise de Anúncios de Carros no Mercado Livre 🚗

Este projeto utiliza **web scraping** para coletar e analisar dados de anúncios de carros na Bahia do **Mercado Livre**, com o objetivo de fornecer uma visão detalhada do mercado de veículos usados no estado da Bahia.

## 🔍 Objetivo

Coletar informações sobre os anúncios de carros na Bahia do Mercado Livre e criar um **dashboard interativo** que permite a visualização e análise de dados, como:
- Ano do veículo
- Quilometragem
- Preço
- Links dos anúncios

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Scrapy**: Utilizado para fazer o web scraping dos dados dos anúncios.
- **Pandas**: Para manipulação e limpeza dos dados.
- **Streamlit**: Para criação do dashboard interativo.
- **Plotly**: Para visualização gráfica dos dados.

## 🗂️ Estrutura do Projeto
📦mercado-livre-webscraping  
 ┣ 📂dashboard  
     ┣ 📜app.py  # Código da aplicação Streamlit para visualização  
 ┣ 📂data  
     ┣ 📜raw_data.csv  # Dados brutos coletados  
 ┣ 📂notebooks  
     ┣ 📜mercadolivre.ipynb  # Transformações nos dados  
 ┣ 📂mercadolivre_project  
     ┣ 📜scraper.py  # Script de scraping usando Scrapy  
     ┣ 📜data_cleaning.ipynb  # Notebook para limpeza de dados  
 ┣ 📜requirements.txt  # Bibliotecas necessárias  
 ┣ 📜README.md  # Descrição do projeto  

 📊 Visualização
Os dados coletados podem ser visualizados diretamente no dashboard interativo, que inclui gráficos e filtros dinâmicos para facilitar a análise.
https://felipeosouz-webscraping.streamlit.app
