import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definiçaõ do dataframe
df = pd.read_csv('Jogos.csv')
# Colunas originais
print(df.columns)
# Redefinição do cabeçalho
df.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano', 'Gênero', 'Editora', 'Vendas-NA', 'Vendas-EU', 'Vendas-JP', 'Outras_Vendas', 'Vendas_Globais']
# Remoção da coluna outras vendas
df = df.drop('Outras_Vendas', axis = 1)
print(df.columns)

# Verificação e remoção das linhas com NA
print(df.isnull().any()) # Verifica as colunas que possuem valor NA
df = df.dropna() # Remove as linhas com valores NA
print(df.isnull().any()) #Conferindo se removeu

# Informações sobre os dados que analisaremos
print('As plataformas a serem analisadas são: {}'.format(df['Plataforma'].unique())) #imprime a lista de plataformas
print('Os anos a serem analisados são: {}'.format(df['Ano'].unique())) #imprime a lista de anos
print('Os gêneros a serem analisados são: {}'.format(df['Gênero'].unique())) #imprime a lista de gêneros
print('As editoras a serem analisadas são: {}'.format(df['Editora'].unique())) #imprime a lista de editoras

# Perdi muito tempo tentando fazer os gráficos de outra maneira e essa função ajudou bastante, mas acabei fazendo por outro jeito
# Legenda_pl = df['Plataforma'].unique().tolist() -> Coloca todos os valores (sem repetir) de uma coluna em uma lista

# Porcentagem das plataformas
df["Plataforma"].value_counts().plot.pie(figsize = (8,4), title = "Plataformas", label = '')
plt.show()

# Porcentagem dos gêneros
df["Gênero"].value_counts().plot.pie(figsize = (8,4), title = "Gêneros", label = '')
plt.show()

# Porcentagem dos anos de lançamentos
df["Ano"].value_counts().plot.pie(figsize = (10,6), title = "Anos", label = '')
plt.show()

# Porcentagem de editoras Obs: tive dificuldades para juntar as editoras com pouca expressãoo em um único conjunto de outras, por isso, acabei deixando assim
df["Editora"].value_counts().plot.pie(figsize = (10,6), title = "Editora", label = '')
plt.show()

# Definindo dataframes auxiliares para fazer cruzamentos de dados
df1 = df.groupby('Gênero',axis = 0,).sum()['Vendas_Globais'].sort_values()
df2 = df.groupby('Gênero',axis = 0,).sum()['Vendas-NA'].sort_values()
df3 = df.groupby('Gênero',axis = 0,).sum()['Vendas-JP'].sort_values()
df4 = df.groupby('Gênero',axis = 0,).sum()['Vendas-EU'].sort_values()

# Relações de gênero e vendas por locais
df1.plot.barh(y = 'Vendas_Globais', figsize = (10,6), title = "Gênero X Vendas Globais")
plt.show()
df2.plot.barh(y = 'Vendas-NA', figsize = (10,6), title = "Gênero X Vendas América do Norte")
plt.show()
df3.plot.barh(y = 'Vendas-JP', figsize = (10,6), title = "Gênero X Vendas Japão")
plt.show()
df4.plot.barh(y = 'Vendas-EU', figsize = (10,6), title = "Gênero X Vendas Europa")
plt.show()
# CONCLUSÕES: Os genêros mais vendidos na América do Norte e na Europa seguem os índices globais.
# Há uma variação quanto aos gêneros mais vendidos no Japão, onde o RPG toma a liderança

#Dataframes auxiliares
df5 = df.groupby('Editora',axis = 0,).sum()['Vendas_Globais'].sort_values(ascending = False)
df5_aux = df5.head(n=10)
df6 = df.groupby('Editora',axis = 0,).sum()['Vendas-NA'].sort_values(ascending = False)
df6_aux = df5.head(n=10)
df7 = df.groupby('Editora',axis = 0,).sum()['Vendas-JP'].sort_values(ascending = False)
df7_aux = df5.head(n=10)
df8 = df.groupby('Editora',axis = 0,).sum()['Vendas-EU'].sort_values(ascending = False)
df8_aux = df5.head(n=10)

# Realção entre as 10 melhores editoras e vendas por locais
df5_aux.plot.bar(y = 'Vendas_Globais', figsize = (10,6), title = "Editoras X Vendas Globais")
plt.show()

df6_aux.plot.bar(y = 'Vendas-NA', figsize = (10,6), title = "Editoras X Vendas América do Norte")
plt.show()

df7_aux.plot.bar(y = 'Vendas-JP', figsize = (10,6), title = "Editoras X Vendas Japão")
plt.show()

df8_aux.plot.bar(y = 'Vendas-EU', figsize = (10,6), title = "Editoras X Vendas Europa")
plt.show()
# CONCLUSÕES: aS 3 editoras (Nintendo, EA e Activision dominam todos os mercados

# CONCLUSÕES GERAIS
# Minhas análises foram um pouco superficiais. Queria fazer cruzamentos mais elaborados, porém me falta perícia para utilizar o pandas
# O grande problema é manipular o dataframE de forma que permita a construção dos gráficos.
# Por exemplo: o cruzamento Ano x Gênero x Vendas_Globais, que poderia dar um insight interessante sobre a venda maior de determinado gênero devido ao cenário da época é um cruzamento que não consegui realizar
# Acho que muitos dos métodos que utilizei não são os melhores. Mas foram os que consegui. Espero poder revisar isso e otimizar o código.
# Vi grande potencial nas bibliotecas utilizadas, mas elas são um pouco complexas. O primeiro contato foi bem desafiador, mas já imaginava isso.
# Espero poder realizar análises mais complexas com maior facilidade num futuro próximo.