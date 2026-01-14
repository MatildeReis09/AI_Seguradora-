import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


try:
    df_trabalho = pd.read_excel("ECF_2_RESULTADO_FINAL.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as e: 
    print(f"Erro ao carregar o ficheiro: {e}")

# 2. Preparar os dados para o cálculo
# Selecionamos apenas as colunas necessárias para garantir que a conta bate certo com os pesos
colunas_para_score = ['age', 'smoker', 'index_gravidade', 'final_profit', 'sinistralidade']

# 3. Definir os pesos e calcular o Score
# Pesos: Age(10%), Smoker(10%), Gravidade(30%), Profit(30%), Sinistralidade(20%)
pesos_finais = np.array([0.10, 0.10, 0.30, 0.30, 0.20])

# O operador @ faz a multiplicação dos valores pelos pesos
# Multiplicamos por 100 para ter uma escala de 0 a 100
df_trabalho['NEW_RISK_SCORE'] = (X_scaled @ pesos_finais) * 100

# 4. Gravar o novo documento com a coluna do score incluída
df_trabalho.to_excel("ECF_2_LIMPO_COM_SCORE.xlsx", index=False)

print("Sucesso! Coluna 'NEW_RISK_SCORE' adicionada e ficheiro guardado.")