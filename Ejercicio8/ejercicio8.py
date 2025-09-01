import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import ipywidgets as widgets

# Cargar dataset
datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# Limpiar outliers extremos
q1 = datos_casas['precio_cop'].quantile(0.05)
q3 = datos_casas['precio_cop'].quantile(0.95)
datos_limpios = datos_casas[(datos_casas['precio_cop'] >= q1) & (datos_casas['precio_cop'] <= q3)]

print(f"Dataset original: {len(datos_casas)} casas")
print(f"Dataset limpio: {len(datos_limpios)} casas (quitamos extremos)")

# Clasificar zonas
barrios_premium = ['El Poblado', 'Envigado', 'Laureles']
barrios_medios = ['Conquistadores', 'Estadio', 'Belen', 'La America', 'Guayabal']

def clasificar_zona(barrio):
    if barrio in barrios_premium:
        return 3  # Zona premium
    elif barrio in barrios_medios:
        return 2  # Zona media
    else:
        return 1  # Zona popular

datos_limpios['zona'] = datos_limpios['barrio'].apply(clasificar_zona)

# Variables para clustering
X = datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']]

# Visualizacion inicial (guardar como imagen)
g = sns.pairplot(datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']])
plt.savefig('pairplot.png')
plt.close()

# Aplicar K-means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
datos_limpios['cluster'] = kmeans.fit_predict(X)

# Grafica de clusters (guardar como imagen)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='tamaño_m2', y='zona', hue='cluster', palette='Set2', data=datos_limpios)
plt.title("Clusters de casas por tamaño y zona")
plt.xlabel("Tamaño (m2)")
plt.ylabel("Zona (1-3)")
plt.savefig('clusters_k3.png')
plt.close()

# Analisis de perfiles
columnas_numericas = ['tamaño_m2', 'estrato', 'zona', 'habitaciones']
perfiles = datos_limpios.groupby('cluster')[columnas_numericas].mean()
print("Promedios por cluster:")
print(perfiles)