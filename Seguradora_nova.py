##Bibliotecas

import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error,median_absolute_error, r2_score


# leitura e carregamento de dados 
try:
    df = pd.read_excel("excel_dataset/ECF_2.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")


feaures = [ 
    'age',
    'smokers',
    'chronical_disease_count',
    'employment_status',
    'income'
]

target = "RISCK_SCORE" 

X = df[feaures]
Y = df[target]

## Datacleaning 







