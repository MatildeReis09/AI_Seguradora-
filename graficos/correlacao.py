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
#calculo da correlação 
corr_matriz= df_trabalho.corr()

##mostrar apenas valores entre annual_medical_cost' &'claims_count'
value_corr= df_trabalho['annual_medical_cost'].corr(df_trabalho['claims_count'])
print(f"Resultado da Validação da Correlação  {value_corr:.2f}")


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_trabalho, x='claims_count', y='annual_medical_cost')

plt.title(f"Correlação annual_medical_cost & claims_count")
plt.xlabel("Número de vezes que o seguro foi acionado")
plt.ylabel("Custo Médico Anual")
plt.grid(True, alpha=0.3)

plt.show()



