# -*- coding: utf-8 -*-
"""Projeto 03 - Case Mercado Financeiro - Ações Magalu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nYxQtpDV8GzGe0PwOPOgXchHSRy3YTMv
"""

#Importando as bibliotecas/libs necessárias para o projeto:

#Libs para modelagem e matrizes:
import numpy as np
import pandas as pd

#Libs para análise gráfica:
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

#Lib para ignorar avisos:
import warnings
#Desabilitando os avisos:
warnings.filterwarnings('ignore')

#Lendo a base de dados para o projeto:
Base_Dados = pd.read_excel('CaseMagalu.xlsx')

#Verificando a base de dados e suas infos:
Base_Dados.describe()

Base_Dados.shape

Base_Dados.info()

Base_Dados.head()

#Setando a 'DATA' como index para tratar a tabela de acordo com o index DATA:
Dados = Base_Dados.set_index('Data')

Dados.head()

#Verificando um registro de eventos:
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(16,5))
plt.title('Análise das ações da Magalu - Fechamento:')
plt.plot(Dados.index,Dados['Fechamento']);
plt.xlabel('Período')
plt.ylabel('Valor da ação (R$)')

Media_Movel = Dados['Fechamento'].rolling(5).mean()
Media_Tendencia = Dados['Fechamento'].rolling(30).mean()

plt.style.use('seaborn-darkgrid')
plt.figure( figsize=(16, 5) )
plt.title('Análise das ações da magalu - Fechamento', fontsize=15, loc='left')

plt.plot( Dados.index, Dados['Fechamento'] )
plt.plot( Dados.index, Media_Movel )
plt.plot( Dados.index, Media_Tendencia )

plt.xlabel('Período da Coração')
plt.ylabel('Valor da Ação (R$)');

sns.boxplot( data=Dados, x='Fechamento')

#BOXPLOT mensal:
Base_Dados['Mes'] = Base_Dados['Data'].dt.month
Base_Dados.head()

plt.figure(figsize=(16,5))
sns.boxplot(data=Base_Dados, x ='Mes', y='Fechamento')

Base_Dados.groupby(['Mes']).describe()['Fechamento']

#Modelagem de gráfico para estudar informações :
#
Grafico = go.Figure(
    data=[
          go.Candlestick(
              x= Dados.index,
              open = Dados['Abertura'],
              high = Dados['Maior'],
              low = Dados['Menor'],
              close = Dados['Fechamento'],
          )
    ]
)

Grafico.update_layout( xaxis_rangeslider_visible=False )

Grafico.show()