import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####################################### PRIMEIRO DATA BASE #####################################################

''' Leitura do arquivo com encoding = latin1 porque ele nao estava conseguindo ler alguns caracteres '''
data = pd.read_csv('avengers.csv', encoding='latin1')

''' Plotando o grafico que mostra o histograma dos anos de criacao de cada vingador, onde há um erro
    encontrado entre os anos de 1900 e 1940, já que não existiam Vingadores nesta época, então farei
    uma selecao a partir do ano de 1940'''
data[['Year']].hist(figsize=(22, 15))
plt.savefig('01-AnoDeEntrada.pdf', dpi=300, format='pdf')

''' Agora os dados serão recriados em outro banco, retirando todas as informacoes anteriores a 1940,
    e recriando o histograma anteriormente feito. Pode-se perceber uma tendência maior de criação de
    personagens após o início do século XXI, que pode ser explicado pelo surgimento do Universo 
    cinematográfico da Marvel, o que impulsionou o grupo de herois.'''
selector = data['Year'] > 1940
data2 = data[selector]
data2[['Year']].hist(figsize=(22, 15))
plt.savefig('02-noDeEntradaAjustado.pdf', dpi=300, format='pdf')

''' Procurando agora quais sao os Vingadores que fazem parte do grupo a mais tempo, lembrando que
    devo usar o data modificado pois alguns dos anos apresentados possuiam erros de digitacao. 
    Tentei sem sucesso selecionar os Vingadores mais antigos da franquia, porém pelo gráfico 
    pode-se perceber que os primeiros membros estão há 50 anos no grupo.'''
y = data2['Years since joining']
y.plot.bar()
plt.savefig('03-MaisAntigos.pdf', dpi=300, format='pdf')

''' Professor, comentei com você que tentaria plotar o avanço do número de Vingadores mulheres
    em relação ao número de Vingadores homens, através de um contador pelos anos, porém não 
    encontrei uma maneira de realizar esta contagem, se tiver possibilidade, queria discutir
    com você sobre isso na proxima aula.
plt.plot(data2['Year'], data2['Gender'].value_counts())
plt.savefig('Avanco dos generos por ano.pdf', dpi=300, format='pdf')'''

''' Com o fracasso em plotar o último gráfico, agora farei um gráfico de pizza para demonstrar
    qual a parcela dos Vingadores é composta por cada um dos gêneros. Cerca de dois terços dos
    Vingadores são compostos por homens.'''
f, ax = plt.subplots(figsize=(22, 15))
data['Gender'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', shadow=True)
ax.set_title('Sexo')
ax.set_ylabel('')
plt.savefig('04-Sexo.pdf', dpi=300, format='pdf')

''' Sabendo agora a porcentagem de mulheres e de homens que ja pertenceram aos Vingadores, vou
    levantar agora os dados sobre a porcentagem de cada um deles que morreu de 1 a 5 vezes nas 
    historias ate 2015. Como plotando os graficos percebi que ninguem morreu mais de duas 
    vezes, nao sera necessario calcular a porcentagem de acima de 2 mortes. Comparando os
    numeros em relacao ao grafico anterior que mostra a porcentagem de homens e mulheres,
    existe um padrao da morte dos homens, independente da quantidade de mortes, ser duas
    vezes maior que a das mulheres. Ainda existem alguns dados desnecessarios na tabela,
    pois na informacao de segunda morte nao era necessario informar caso a personagem nao 
    morresse.'''
f, ax = plt.subplots(1, 2, figsize=(22, 15))
sns.countplot('Gender', hue='Death1', data=data, ax=ax[0])
ax[0].set_title('Mortos 1 vez x Sexo')
sns.countplot('Gender', hue='Death2', data=data, ax=ax[1])
ax[1].set_title('Mortos 2 vezes x Sexo')
plt.savefig('05-Mortes x Sexo.pdf', dpi=300, format='pdf')

''' Agora, daqueles Vingadores que morreram, vou pesquisar aqueles que conseguiram retornar para
    os quadrinhos apos sua morte, atraves da comparacao de genero. Quando comparo os valores
    obtidos, a taxa de retorno das personagens mulheres quando morrem 1 vez é extremamente maior
    que a dos homens. O retorno apos a segunda morte se mostra similar em ambos os sexos. Estes
    valores demonstram que existe, talvez, um perigo maior ao ser um Vingador homem do que ser
    um Vingador mulher.'''
f, ax = plt.subplots(1, 2, figsize=(22, 15))
sns.countplot('Gender', hue='Return1', data=data, ax=ax[0])
ax[0].set_title('Retorno 1 vez x Sexo')
sns.countplot('Gender', hue='Return2', data=data, ax=ax[1])
ax[1].set_title('Retorno 2 vezes x Sexo')
plt.savefig('0-Retorno x Sexo.pdf', dpi=300, format='pdf')

######################################## SEGUNDO DATA BASE #####################################################

''' Já entendendo agora como funciona o relacionamento do perigo de ser um herói ou uma heroína dentro,
    dos vingadores, vou realizar um estudo comparando as duas principais produtoras de quadrinhos nesse 
    ramo: a Marvel e a DC. A partir de um banco de dados que lista quase todos os heróis existentes 
    nas duas produtoras. Tive de usar o encoding cp1251 porque existiam caracteres que nao eram
    lidos pelo encoding original utf-8 '''

''' Leitura do arquivo com encoding = cp1251 porque ele nao estava conseguindo ler alguns caracteres '''
data = pd.read_csv('marvel_dc_characters.csv', encoding='cp1251')

''' Inicialmente vou plotar gráficos que mostrem os dados gerais do banco de dados, para ter
    como base de comparacao com os dados para cada uma das produtoras separadamente. Através
    desses dados gerais do database, a maior parte dos personagens (independente de sua 
    tendencia a ser bom ou mau, possui uma identidade secreta. Outra hipotese que eu ja tinha
    sobre a maior quantidade das personagens ser viloes é comprovada com o segundo grafico,
    onde o numero de viloes é 33% maior que dos herois. Outros dados interessantes levantados
    foram em relacao ao genero das personagens, onde uma grande maioria é composta por 
    homens, mas existindo ainda assexuados, sem genero, genero fluido e transgeneros.'''
def plot_dist(col, ax):
    data[col][data[col].notnull()].value_counts().plot('bar', facecolor='y', ax=ax)
    ax.set_xlabel('')
    ax.set_title('{} geral'.format(col), fontsize=18)

f, ax = plt.subplots(3, 2, figsize=(22, 15))
f.tight_layout(h_pad=9, w_pad=2, rect=[0, 0.03, 1, 0.93])
cols = ['Identity', 'Alignment', 'EyeColor', 'HairColor', 'Gender', 'Status']
k = 0
for i in range(3):
    for j in range(2):
        plot_dist(cols[k], ax[i][j])
        k += 1
plt.savefig('07-Geral.pdf', dpi=300, format='pdf')

''' Agora plotarei os mesmos graficos, mas comparando os resultados apresentados
    distinguindo qual a produtora dos quadrinhos. Esses resultados comparados
    demonstram que existe um padrao seguidos por ambas as produtoras em 
    praticamente todos os dados coletados.'''
f,ax = plt.subplots(1,2, figsize = (22, 15))
sns.countplot('Universe', hue='Identity', data=data, ax=ax[0])
ax[0].set_title('Identidade x Universo')
sns.countplot('Universe', hue='Alignment', data=data, ax=ax[1])
ax[1].set_title('Parcialidade x Universo')
plt.savefig('08-Comparativo1.pdf', dpi=300, format='pdf')

f,ax = plt.subplots(1,2, figsize = (22, 15))
sns.countplot('Universe', hue='EyeColor', data=data, ax=ax[0])
ax[0].set_title('Cor de olhos x Universo')
sns.countplot('Universe', hue='HairColor', data=data, ax=ax[1])
ax[1].set_title('Cores de cabelo x Universo')
plt.savefig('09-Comparativo2.pdf', dpi=300, format='pdf')

f,ax = plt.subplots(1,2, figsize = (22, 15))
sns.countplot('Universe', hue='Gender', data=data, ax=ax[0])
ax[0].set_title('Sexo x Universo')
sns.countplot('Universe', hue='Status', data=data, ax=ax[1])
ax[1].set_title('Status x Universo')
plt.savefig('10Comparativo3.pdf', dpi=300, format='pdf')