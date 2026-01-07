import seaborn as sns
import pandas as pd # manipulação de dados
import matplotlib.pyplot as plt 
import os

## calcular a correlação entre annual_medical_cost (custo) e claims_count (quantidade de pedido)


try:
    df_trabalho = pd.read_excel("../excel_dataset/ECF_2_RESULTADO_FINAL.xlsx")
    print("Ficheiro carregado com sucesso!")
except Exception as doc : 
    print(f"Erro ao carregar o ficheiro: {doc}")

print ("estou aqui")


#correlacao = df_trabalho [ 'annual_medical_cost'].corr(df_trabalho ['claims_count'])


##grafico visual
#plt.figure(figsize =(8,8))

