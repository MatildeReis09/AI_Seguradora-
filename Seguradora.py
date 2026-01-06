##Bibliotecas 
import pandas as pd# manipulação de dados
from sklearn.preprocessing import StandardScaler, OneHotEncoder 
##StandardScaler - nromalizar variaveis numericas
## media = 0 e desvio padrao = 1 
##OneHotEncoder- codificar variáveis categóricas 
## criar variaveis binarios 

from sklearn.model_selection import train_test_split
# dividir o data set em teste e treino


# ler excel dataset
df = pd.read_excel("ECF_2.xlsx")