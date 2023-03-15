#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.
# 
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[6]:


import pyautogui
import time
import pyperclip

link = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"


# In[37]:


pyautogui.PAUSE = 1

#abri o sistema
pyautogui.hotkey("ctrl", "t")

#pyautogui.press("win")
#pyautogui.write("chrome")
#pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

#preencher login
pyautogui.click(x=517, y=374)
pyautogui.write("meu_login")

#preencher a senha
pyautogui.click(x=493, y=452)
pyautogui.write("minha_senha")

#apertar em acessar
pyautogui.click(510, y=520)
time.sleep(10)

#Selecionar o arquivo
pyautogui.click(x=525, y=297)

#Fazer o download
pyautogui.click(x=822, y=186)
pyautogui.click(x=557, y=596)
time.sleep(3)






# In[54]:


time.sleep(5)
print(pyautogui.position())


# In[50]:


import pandas as pd

tabela = pd.read_csv(r"D:\Downloads\Compras.csv" , sep=";")
display(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade


print(total_gasto)
print(quantidade)
print(preco_medio)


# In[72]:


pyautogui.PAUSE = 3
pyautogui.hotkey("ctrl" , "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("enter")
time.sleep(3)

pyautogui.click(x=70, y=205)

pyautogui.write("jhollsi18@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

import pyperclip
pyperclip.copy("Relatório de Compras")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("tab")

texto = f"""
prezados,
Segue o resumo das compras:

gasto Total: R${total_gasto:,.2f}
Quantidade: {quantidade:}
Preço médio: R${preco_medio:,.2f}

Att.,
Jonatas Ferreira"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl" , "v")
pyautogui.hotkey("ctrl" , "enter")




# In[ ]:





# In[ ]:




