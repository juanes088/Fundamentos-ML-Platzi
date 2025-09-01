import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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

# Variables para clustering
X = datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']]

# Aplicar K-means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
datos_limpios['cluster'] = kmeans.fit_predict(X)

# Analisis de perfiles
columnas_numericas = ['tamaño_m2', 'estrato', 'zona', 'habitaciones']
perfiles = datos_limpios.groupby('cluster')[columnas_numericas].mean()
print("Promedios por cluster:")
print(perfiles)

# Boxplots
features = ['tamaño_m2', 'estrato', 'zona', 'habitaciones']
for feature in features:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x='cluster', y=feature, hue='cluster', data=datos_limpios, palette='Set2', legend=False)
    plt.title(f'Analisis por Cluster - {feature}')
    plt.savefig(f'boxplot_{feature}.png')
    plt.close()

# Vista interactiva simulada
print("\n" + "="*60)
print("VISTA INTERACTIVA - DATOS POR CLUSTER")
print("="*60)

for cluster_num in sorted(datos_limpios['cluster'].unique()):
    print(f"\nCluster: {cluster_num}")
    casas = datos_limpios[datos_limpios['cluster'] == cluster_num]
    print(casas[['barrio', 'tamaño_m2', 'estrato', 'zona', 'habitaciones']])