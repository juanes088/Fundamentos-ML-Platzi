import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Cargar dataset
datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# Limpiar outliers extremos
q1 = datos_casas['precio_cop'].quantile(0.05)
q3 = datos_casas['precio_cop'].quantile(0.95)
datos_limpios = datos_casas[(datos_casas['precio_cop'] >= q1) & (datos_casas['precio_cop'] <= q3)].copy()

print(f"Dataset original: {len(datos_casas)} casas")
print(f"Dataset limpio: {len(datos_limpios)} casas (quitamos extremos)")

# Clasificar zonas
barrios_premium = ['El Poblado', 'Envigado', 'Laureles']
barrios_medios = ['Conquistadores', 'Estadio', 'Belen', 'La America', 'Guayabal']

def clasificar_zona(barrio):
    if barrio in barrios_premium:
        return 3
    elif barrio in barrios_medios:
        return 2
    else:
        return 1

datos_limpios['zona'] = datos_limpios['barrio'].apply(clasificar_zona)

# Variables para PCA
X = datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']]

# Escalar variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar PCA
pca = PCA(n_components=2)
componentes = pca.fit_transform(X_scaled)

# Añadir componentes al dataframe
datos_limpios['PC1'] = componentes[:, 0]
datos_limpios['PC2'] = componentes[:, 1]

# Calcular varianza explicada
varianza = pca.explained_variance_ratio_
print(f"Varianza explicada por PC1: {varianza[0]:.2%}")
print(f"Varianza explicada por PC2: {varianza[1]:.2%}")
print(f"Varianza total explicada: {varianza.sum():.2%}")

# Aplicar K-means
kmeans = KMeans(n_clusters=3, random_state=42)
datos_limpios['cluster'] = kmeans.fit_predict(X_scaled)

# Graficos (guardar como imagenes)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='cluster', palette='Set1', data=datos_limpios, s=100)
plt.title('Clusters de casas en espacio PCA')
plt.grid(True)
plt.savefig('pca_clusters.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='tamaño_m2', palette='coolwarm', data=datos_limpios, s=100)
plt.title('Casas en espacio PCA por tamaño_m2')
plt.grid(True)
plt.savefig('pca_tamano.png')
plt.close()