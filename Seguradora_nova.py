##Bibliotecas

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# leitura e carregamento de dados 
try:
    df = pd.read_excel("excel_dataset/ECF_2.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")

#print(df.columns.tolist())
#da as categorias todas

#nulos_total = df['alcohol_freq'].isnull().sum()
#print(f"Total de linhas sem informação de álcool: {nulos_total}")

# Percentagem de dados em falta
#percentagem = (nulos_total / len(df)) * 100
#print(f"\nPercentagem de buracos nos dados: {percentagem:.2f}%")



#variaveis escolhidas
features = [ 
    'age',
    'smoker',
    'chronic_count',
    'employment_status',
    'income'
]
#print(df[features].head())

target = "risk_score" 
#print(df["risk_score"].describe())

## Datacleaning 

df = df.dropna(subset=[target])

df = df[df['age'] != 0] #remove idades = 0
#no caso de a sinistralidade = 0 , assume-se 0 sinitros registado 

X = df[features]
Y = df[target]


numeric_features = ["age", "chronic_count", "income"]
categorical_features = ["smoker" ,"employment_status"]

#transformação de colunas( pre-procesamento )
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(drop="first"), categorical_features)
    ]
)


#divisaõ do modelo e treino 
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)




##modelo Regressão linear ( valor continuo)
lin_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

lin_model.fit(X_train, y_train)

#previsão 
y_pred_lin = lin_model.predict(X_test)

#avaliação 
rmse_lin = np.sqrt(mean_squared_error(y_test, y_pred_lin))
mae_lin = mean_absolute_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)

rmse_lin, mae_lin, r2_lin



##modelo Random Forest
rf_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ))
    ]
)

rf_model.fit(X_train, y_train)

#previsao
y_pred_rf = rf_model.predict(X_test)


#avaliação 
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

rmse_rf, mae_rf, r2_rf


##comparação 

results = pd.DataFrame({
    "Model": ["Linear Regressions", "Random Forest"],
    "RMSE": [rmse_lin, rmse_rf],
    "MAE": [mae_lin, mae_rf],
    "R2": [r2_lin, r2_rf]
})

print (results)

plt.figure()
plt.scatter(y_test, y_pred_rf, alpha=0.4)
plt.xlabel("Risckscore Real")
plt.ylabel("Previsão Risck score ")
plt.title(" Random Forest - real vs previsão")
plt.show()


##criar excel para colucar os dados lado a lado 
df_final = X_test.copy()

df_final [ 'Risck_score_real'] = y_test
df_final ['Previsão_linearRegression'] = y_pred_lin
df_final ['previsão_randomForest']= y_pred_rf

df_final.to_excel("Previsoes_risck_seguradora.xlsx", index = False)

