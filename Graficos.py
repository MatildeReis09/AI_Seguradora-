## codigo a rever e ajustar
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

inertia = []
K_range = range(1, 10) # Testar de 1 a 9 grupos

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