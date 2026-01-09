import numpy as np
import pandas as pd




try:
    df = pd.read_excel("excel_dataset/ECF_2.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")


# contagem total de nulos na coluna
## para saber se vale a pena utilizar o parametro 

nulos_total = df['alcohol_freq'].isnull().sum()
print(f"Total de linhas sem informação de álcool: {nulos_total}")

# Percentagem de dados em falta
percentagem = (nulos_total / len(df)) * 100
print(f"\nPercentagem de buracos nos dados: {percentagem:.2f}%")

#removidas = len(df) - len(df_limpo)
#print(f"Foram removidas {removidas} linhas com idade igual a zero.")
