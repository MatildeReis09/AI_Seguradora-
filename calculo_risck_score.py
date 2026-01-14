import numpy as np
import pandas as pd


try:
    df = pd.read_excel("ECF_2_RESULTADO_FINAL.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")


# Definimos a importância de cada variável no risco final
pesos_finais = np.array([0.15, 0.15, 0.40, 0.10, 0.20]) # Age, Smoker, Gravidade, Profit, Sinistralidade
df_trabalho['MEU_RISK_SCORE'] = (X_scaled @ pesos_finais) * 100
