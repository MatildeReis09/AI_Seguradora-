import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # para o algoritmos
from sklearn.preprocessing import StandardScaler
import pandas as pd

inertia = [] # = wcss
K_range = range(1, 10) # Testar de 1 a 9 grupos

print("a calcular")
for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled) # X_scaled são os teus dados preparados
    inertia.append(model.inertia_)

# Criar o gráfico
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, 'bx-')
plt.xlabel('Número de Grupos (k)')
plt.ylabel('Inércia (Soma dos Quadrados das Distâncias)')
plt.title('Método do Cotovelo para encontrar o K ideal')
plt.show()

## importante para a validação da escola do k, nº de grupos escolhidos

wcss = [] # Within-Cluster Sum of Squares
k_range = range(1, 11) # Vamos testar de 1 a 10 grupos

print("Calculando inércia para cada K... por favor aguarde.")
for i in k_range:
    # n_init=10 garante estabilidade no cálculo
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# 5. Gerar o Gráfico do Cotovelo
plt.figure(figsize=(10, 6))
plt.plot(k_range, wcss, marker='o', linestyle='-', color='b')
plt.title('Método do Cotovelo (Elbow Method)')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('WCSS (Soma dos erros quadráticos)')
plt.xticks(k_range)
plt.grid(True, linestyle='--', alpha=0.7)

print("✅ Gráfico gerado! Procure o ponto onde a curva 'dobra'.")
plt.show()