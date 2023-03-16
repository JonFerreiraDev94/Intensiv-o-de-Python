#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e compramos e vendemos commodities:
# - Soja, Milho, Trigo, Petróleo, etc.
# 
# Precisamos pegar na internet, de forma automática, a cotação de todas as commodites e ver se ela está abaixo do nosso preço ideal de compra. Se tiver, precisamos marcar como uma ação de compra para a equipe de operações.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=share_link
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[43]:


from selenium import webdriver
nav = webdriver.Chrome()
nav.get("https://google.com")


# In[44]:


pip install selenium


# In[45]:


import pandas as pd

tabela  = pd.read_excel("commodities.Xlsx")
display(tabela)


# In[46]:


#import inicodedata
#novo_texto = unicodedata.normalize('NFKD', produto).encode('ascii','ignore')

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    produto = produto.replace("ã", "a").replace(
        "ç", "c").replace("á", "a").replace("ó", "o").replace("ú", "u").replace("é", "e")
    link = f"https://www.melhorcambio.com/{produto.lower()}-hoje"
    print(link)
    nav.get(link)
    preco = nav.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
    preco = preco.replace("." , "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    
display(tabela)
    


# In[47]:


nav.quit()
tabela["Comprar"] = tabela["Preço Ideal"] > tabela["Preço Atual"]
tabela.to_excel("commodities_atualizado.xlsx", index=False )
                          


# In[ ]:




