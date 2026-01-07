##Bibliotecas 
import numpy as np
import pandas as pd# manipulação de dados
from sklearn.preprocessing import StandardScaler, OneHotEncoder , LabelEncoder
##StandardScaler - nromalizar variaveis numericas
## media = 0 e desvio padrao = 1 
##OneHotEncoder- codificar variáveis categóricas 
## criar variaveis binarios 

from sklearn.model_selection import train_test_split
# dividir o data set em teste e treino

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
    'mental_health': 2  ##falar com eles (2ou 3 )como querem designar
}

## indice de doencas
## juantar todas as doenças e criar um só parametro que as engloba a todas
df ['index_gravidade'] = 0 
for disease, peso in peso_disease.item(): ##depara aso pares 
    df['index_gravidade'] += df[disease] * peso
## como no dataset esta (0ou 1) caso tenha ou não a doença apenas se multiplica pelo pelo

##tratamento de missing values

