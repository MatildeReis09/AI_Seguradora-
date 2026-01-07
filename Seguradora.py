##Bibliotecas 
import numpy as np
import pandas as pd# manipulação de dados
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder , LabelEncoder
##StandardScaler - nromalizar variaveis numericas
## media = 0 e desvio padrao = 1 
##OneHotEncoder- codificar variáveis categóricas 
## criar variaveis binarios 

from sklearn.model_selection import train_test_split
# dividir o data set em teste e treino
from sklearn.cluster import KMeans # para o algoritmos

df = pd.read_excel("ECF_2.xlsx")
## 1- Processo Data cleaning 


#definir peso/ importancia das doenças 
peso_disease = {
    'cancer_history': 3,
    'cardiovascular_disease': 1,
    'kidney_disease' : 2,
    'liver_disease' : 1,
    'copd': 2, #Doença Pulmonar Obstrutiva Crónica
    'diabetes': 2,
    'hypertension': 2,
    'asthma': 2,
    'arthritis': 2, 
    'mental_health': 2 
}

## criar indice de doencas
## juantar todas as doenças e criar um só parametro que as engloba a todas
df ['index_gravidade'] = 0 
for disease, peso in peso_disease.items(): 
    df['index_gravidade'] += df[disease] * peso
## como no dataset esta (0ou 1) caso tenha ou não a doença apenas se multiplica pelo pelo
##o valor do inidce é a soma

##tratamento de missing values
df_original = df.drop(columns=['alcohol_freq'])

# contagem total de nulos na coluna
nulos_total = df['alcohol_freq'].isnull().sum()
print(f"Total de linhas sem informação de álcool: {nulos_total}")

# Percentagem de dados em falta
percentagem = (nulos_total / len(df)) * 100
print(f"\nPercentagem de buracos nos dados: {percentagem:.2f}%")


##codificação 
#aprende as paçavras e associa a numeros
le = LabelEncoder()
df_original['smoker'] = le.fit_transform(df_original['smoker'])

#seleção de parametros para o calculo 
Collumns_risk_score = [
    'age',
    'smoker',
    'hospitalizations_last_3yrs',
    'index_gravidade',
    'claims_count', 
]


##criar dataset limpo
df_trabalho = df_original[Collumns_risk_score ].copy()

## scaling/normalização 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_trabalho)


##algoritmo clustering K-means


