#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Anchor → Alinhamento do texto Label

# NE – Nordeste (ponto entre o Norte e o Leste)
# SE – Sudeste (ponto entre o Leste e o Sul)
# SW ou SO – Sudoeste (ponto entre o Sul e o Oeste)
# NW – Noroeste (ponto entre o Oeste e o Norte)

import requests

requesicao = requests.get("https://economia.awesomeapi.com.br/json/all")
dicionario_moedas = requesicao.json()
print(dicionario_moedas)


# In[5]:


import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests

requesicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requesicao.json()

lista_moedas = list(dicionario_moedas.keys())


def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/10?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requesicao_moeda = requests.get(link)
    cotacao = requesicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f"A cotação da R$ {moeda} no dia {data_cotacao} foi de R$: {float(valor_moeda):.2f}"
    print(f'A moeda selecionada foi {moeda} e a data foi {data_cotacao}')
    print(valor_moeda)

    
def selecionar_arquivo():
    pass

def atualizar_cotacoes():
    pass


janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moedas')

label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid', fg='yellow', bg='black')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar Moeda", anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selecionardia = tk.Label(text="Selecione o dia que deseja pegar a cotação", anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_textocotacao = tk.Label(text="", fg='yellow', bg='black')
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao, fg='yellow', bg='black')
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')


# cotação de várias moedas

label_cotacavariasmoedas = tk.Label(text="Cotação de Múltiplas Moedas", borderwidth=2, relief='solid', fg='yellow', bg='black')
label_cotacavariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo em Excel com as Moedas na Coluna A')
label_selecionararquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_arquivo, fg='yellow', bg='black')
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

label_datainicial = tk.Label(text="Data Inicial", anchor='e')
label_datafinal = tk.Label(text="Data Final", anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

calendario_datainicial = DateEntry(year=2022, locale='pt_br')
calendario_datafinal = DateEntry(year=2022, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10,  sticky='nsew')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')

botao_atualizarcotacoes = tk.Button(text='Atualizar Cotações', command=atualizar_cotacoes, fg='yellow', bg='black')
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

botao_fechar = tk.Button(text='Fechar', command=janela.quit, fg='yellow', bg='black')
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')

janela.mainloop()


# In[ ]:




