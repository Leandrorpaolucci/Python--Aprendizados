#!/usr/bin/env python
# coding: utf-8

# ### Espaço para funções no código principal
# - Espaço somente para funções

# ### Espaço para bibliotecas utilizadas no programa principal
# - Utilizaremos a biblioteca pandas, para análise de dados!

# In[1]:


import pandas as pd
import numpy as np
from time import sleep


# In[ ]:





# In[4]:


def menu():
    auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
    print('\033[31m O dataframe foi chamado junto a função menu! selecione uma opção')
    print('\033[34m---' * 41)
    print("""
    [1] - Exibir as colunas do dataframe importado!
    [2] - Exibir amostra de Nomes da coluna DF
    [3] - Filtro por NOME analisando Colunas!
    [4] - Mostrar Display da tabela
    [0] - Sair
    """)
    

def mostrar_display():
    auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
    display(auxilio_emergencial_df)
    
    
def exibir_df():
    while True:
        auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
        for coluna in auxilio_emergencial_df:
            print(f'Lista de colunas do dataframe: {coluna}')
        break
    
    
def filtro_nome():
    auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
    #nome_input = str(input("Digite o nome que deseja localizar: "))
    nome_input = ''
    nome_input = nome_input.replace("-", "").replace("_", "")
    nome_input = nome_input.strip()
    nome_input = nome_input.upper()
    #Lista de nomes
    lista_nome_beneficiarios = [pessoas for pessoas in auxilio_emergencial_df['nome_beneficiario']]
    while True:
        #Inserir o nome e verificar se o nome existe no dataframe
        nome_input = str(input("Digite o nome que você deseja encontrar na lista: "))
        if nome_input in lista_nome_beneficiarios:
            print(f'O nome foi encontrado! {nome_input}')
            break
        else:
            tentativa = 0
            if tentativa == 3:
                visualizar_nome = str(input("Deseja visualizar a lista de nomes? S/N: "))[0].strip().upper()
                if visualizar_nome == 'S':
                    visualizar_nomes_beneficiarios = auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
                    display(visualizar_nomes_beneficiarios['nome_beneficiario'])
                else:
                    print('encerrando o programa!')
            break      
            print('''\033[31mNome não encontrado!
            verifique o nome inserido e tente novamente.''')

print(f'''\033[34mAgora que nós temos o nome "{nome_input}".\n
fazendo o download em 3 segundos!''')
sleep(3)
df_nome_input = auxilio_emergencial_df
df_nome_input = df_nome_input.loc[auxilio_emergencial_df['nome_beneficiario'] == f'{nome_input}']
df_nome_input.to_excel(f"{nome_input}.xlsx")
#print('deu certo!')
    
def amostra_nomes():
    auxilio_emergencial_df = pd.read_csv("Auxilio Emergencial.csv")
    nome_coluna_df = auxilio_emergencial_df['nome_beneficiario']
    qtde_nome = int(input("Digite quantos nomes deseja visualizar como exemplo: "))
    if qtde_nome > 0:
        display(nome_coluna_df.head(qtde_nome))
    else:
        print("Você não digitou um número válido, tente novamente.")
   


# ### Programa Principal
# - Espaço utilizado para o usuário selecionar a opção desejada e fazer um filtro com base nas opções informadas!

# In[ ]:


menu()


while True:
    x = int(input("Selecione uma opção: "))
    while x > 4 or x < 0:
        x = int(input(f'''\033[31mErro! Você digitou {x} e o valor não esta na lista de opções.
        Tente novamente com as opções listada para selecionar.'''))
        
    if x == 1:
        exibir_df()
    elif x == 2:
        amostra_nomes()
    elif x == 3:
        filtro_nome()
    elif x == 4:
        mostrar_display()
    elif x == 0:
        print(f'\033[34mVocê selecionou a opção "{0}"\nEncerrando o programa.')
        break
        

