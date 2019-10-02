# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:51:28 2019

@author: André
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('all_pokemon.csv')
df.info()

print("Quantos Pokemon de cada tipo existem?")
print(df.groupby('Type').agg('count')['#'])  
x = pd.value_counts(df['Type'])
tipos = x[:18].index.values
freq = x[:18].values
plt.figure(figsize=(10,10))
plt.pie(freq, labels=tipos, explode=np.linspace(0.1,0.1,18),startangle=90,autopct='%1.2f%%')
plt.show()

print("Qual a média dos Stats(atributos) para cada tipo?")
print(df.groupby('Type').agg('median')[['HP','Sp. Atk', 'Sp. Def', 'Attack', 'Defense', 'Speed', 'Total']])

print("Qual valor máximo cada Stat(atributo) pode ter?")
print(df.agg('max')[['HP','Sp. Atk', 'Sp. Def', 'Attack', 'Defense', 'Speed', 'Total']])

print("Qual valor mínimo cada Stat(atributo) pode ter?")
print(df.agg('min')[['HP','Sp. Atk', 'Sp. Def', 'Attack', 'Defense', 'Speed', 'Total']])

tot = int(input("Digite um valor (entre 175 e 780) para saber quais Pokemon têm um total de Stats(atributos) acima disso:"))
print("Quais Pokemon têm o total de Stats(atributos) maior que", tot,"?")
print(df.Name[df.Total > tot])

tip = input("Digite um tipo (em inglês) para saber quais Pokemon têm esse tipo:")
print("Quais Pokemon têm o tipo", tip,"?")
print(df.Name[df.Type == tip])

print("Boxplot da soma de Stats(atributo)s:")
print(sns.boxplot(df.Total))
plt.show()

print("Boxplot da soma de Stats(atributo)s para cada tipo:")
print(sns.boxplot(x='Total',y='Type',data=df))
plt.show()

print("Boxplot de cada Stat(atributo):")
df2 = df.drop(['#', 'Total'],axis='columns')
print(sns.boxplot(data=df2))
plt.show()

print("Gráfico de distribuição do total de Stats(atributos):")
print(sns.distplot(df['Total']))
plt.show()


print("Gráfico de pontos do total de Stats(atributos) de acordo com cada tipo:")
plt.figure(figsize=(8,10))
sns.stripplot(x="Total", y="Type", data=df, alpha=1, zorder=0.5)
sns.pointplot(x="Total", y="Type", data=df, dodge=.1, join=False, color="black", markers=".", scale=1, ci=None)
plt.show()




















