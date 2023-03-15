#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link

# In[3]:


import pandas as pd

tabela = pd.read_csv("Clientes.csv", encoding="latin1", sep=";")
tabela = tabela.drop("Unnamed: 8" , axis=1)
display(tabela)


# In[8]:


tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
print(tabela.info())


# In[9]:


display(tabela[tabela["Profissão"].isna()])
tabela = tabela.dropna()
print(tabela.info())


# In[10]:


display(tabela.describe())


# In[12]:


import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)" , text_auto=True, histfunc='avg', nbins=10 )
    grafico.show()


# In[ ]:




