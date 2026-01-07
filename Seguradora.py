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


try:
    df = pd.read_excel("excel_dataset/ECF_2.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")



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

print("chegou aqui")

## criar indice de doencas
## juantar todas as doenças e criar um só parametro que as engloba a todas
df ['index_gravidade'] = 0 
for disease, peso in peso_disease.items(): 
    df['index_gravidade'] += df[disease] * peso
## como no dataset esta (0ou 1) caso tenha ou não a doença apenas se multiplica pelo pelo
##o valor do inidce é a soma

##tratamento de missing values or null
df_limpo = df.drop(columns=['alcohol_freq']) #remove valores null
df_limpo = df_limpo[df_limpo['age'] != 0] #remove idades = 0

print("estou aqui")
##codificação 
#aprende as paçavras e associa a numeros
le = LabelEncoder()
df_limpo['smoker'] = le.fit_transform(df_limpo['smoker'])


#seleção de parametros para o calculo 
Collumns_risk_score = [
    'age',
    'smoker',
    'annual_medical_cost',
    'index_gravidade',
    'claims_count', 
]

##criar dataset limpo
df_trabalho = df_limpo[Collumns_risk_score ].copy()
df_trabalho = df_trabalho.fillna(df_trabalho.mean())# caso haja um buraco
# calcula a media e preenche o buraco 

## scaling/normalização 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_trabalho)

df_trabalho.to_excel("ECF_2_RESULTADO_FINAL.xlsx", index=False)
print("ficheiro 'ECF_2_RESULTADO_FINAL.xlsx' criado com sucesso")
##algoritmo clustering K-means
