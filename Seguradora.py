##Bibliotecas 
import numpy as np
import pandas as pd# manipulação de dados
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder , LabelEncoder
##StandardScaler - nromalizar variaveis numericas
## media = 0 e desvio padrao = 1 
##OneHotEncoder- codificar variáveis categóricas 
## criar variaveis binarios 

from sklearn.model_selection import train_test_split
# dividir o data set em teste e treino
from sklearn.cluster import KMeans # para o algoritmos

# leitura e carregamento de dados 
try:
    df = pd.read_excel("excel_dataset/ECF_2.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")



#definir peso/ importancia das doenças ( indeice de gravidade)
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

# contagem total de nulos na coluna
## para saber se vale a pena utilizar o parametro 

nulos_total = df['alcohol_freq'].isnull().sum()
print(f"Total de linhas sem informação de álcool: {nulos_total}")

# Percentagem de dados em falta
percentagem = (nulos_total / len(df)) * 100
print(f"\nPercentagem de buracos nos dados: {percentagem:.2f}%")


## 1- Processo Data cleaning 

##tratamento de missing values or null ou <0
df_limpo = df.drop(columns=['alcohol_freq'], errors='ignore').copy() #remove valores null

colunas_obrigatorias = ['age', 'smoker'] 
df_limpo = df_limpo.dropna(subset=colunas_obrigatorias)

df_limpo = df_limpo[df_limpo['age'] != 0] #remove idades = 0
#no caso de a sinistralidade = 0 , assume-se 0 sinitros registado 

if 'sinistralidade' in df_limpo.columns:
        df_limpo ['sinistralidade'] = df_limpo['sinistralidade'].fillna(0)

#tratar do indice de doenças , se for igual a zero , não tem nenhuma doença 
colunas_doenças= list(peso_disease.keys())
df_limpo [colunas_doenças] = df_limpo[colunas_doenças].fillna(0)
## key=  nomes das doenças , valores = peso 
# cria lista interna para acelarar o proceso


##codificação de variaveis categoricas
#aprende as palavras e associa a numeros
# Substituir porque se não da problemas no calculo 
mapa_smoker = {'Never': 0, 'Former': 1, 'Current': 2}
df_limpo['smoker'] = df_limpo['smoker'].map(mapa_smoker)

print(" categoria smoker alteradas")



print("estou aqui, datacleaning completo")

##logica :
##quanto maior o lucro para a seguradora menos o risco

#seleção de parametros para o calculo 
Collumns_risk_score = [
    'age',
    'smoker',
    'index_gravidade',
    'final_profit',
    'sinistralidade',
]

##criar dataset limpo
df_trabalho = df_limpo[Collumns_risk_score ].copy()
df_trabalho = df_trabalho.fillna(df_trabalho.mean())# caso haja um buraco
# calcula a media e preenche o buraco 

## scaling/normalização 
# utilização do minmax escala (0-100) , da valores de 0-1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(df_trabalho)

df_trabalho_scaled = pd.DataFrame(scaler.fit_transform(df_trabalho), columns=Collumns_risk_score)

#df_trabalho_scaled.to_excel("ECF_2_RESULTADO_FINAL.xlsx", index=False)
#print("ficheiro 'ECF_2_RESULTADO_FINAL.xlsx' criado com sucesso")


##calculo do risck score

try:
    df_trabalho = pd.read_excel("ECF_2_RESULTADO_FINAL.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as e: 
    print(f"Erro ao carregar o ficheiro: {e}")

colunas_para_score = ['age', 'smoker', 'index_gravidade', 'final_profit', 'sinistralidade']
pesos_finais = np.array([0.10, 0.10, 0.30, 0.30, 0.20])
#  Definir os pesos e calcular o Score


# O operador @ faz a multiplicação dos valores pelos pesos
# Multiplicamos por 100 para ter uma escala de 0 a 100
df_trabalho['NEW_RISK_SCORE'] = df_trabalho[colunas_para_score].values @ pesos_finais
#df_trabalho_scaled['NEW_RISK_SCORE'] = (X_scaled @ pesos_finais) * 100

# 4. Gravar o novo documento com a coluna do score incluída
df_trabalho.to_excel("ECF_2_LIMPO_COM_SCORE.xlsx", index=False)


print("Sucesso! Coluna 'NEW_RISK_SCORE' adicionada e ficheiro guardado.")
