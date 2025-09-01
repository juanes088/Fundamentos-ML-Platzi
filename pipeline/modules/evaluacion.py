import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
import numpy as np

def calcular_rentabilidad(precio_actual, precio_futuro):
    """
    Calcula rentabilidad total y genera recomendacion
    """
    rentabilidad = (precio_futuro - precio_actual) / precio_actual * 100
    recomendacion = "Viable" if rentabilidad > 15 else "No viable"  # Ajustado para rentabilidad total
    
    return {
        'precio_predicho': precio_futuro,
        'rentabilidad_pct': rentabilidad,
        'recomendacion': recomendacion
    }

def generar_graficos(df_clusters, modelo_supervisado, X_test, y_test):
    """
    Genera boxplot de rentabilidad por cluster y PCA scatter plot
    """
    # Calcular rentabilidades simuladas para cada cluster
    precios_actuales = df_clusters.groupby('cluster')['precio_cop'].mean()
    precios_predichos = df_clusters.groupby('cluster')['precio_cop'].mean() * 1.15  # Simulacion
    
    rentabilidades = {}
    for cluster in range(3):
        mask = df_clusters['cluster'] == cluster
        cluster_data = df_clusters[mask]
        rent_list = []
        for _, row in cluster_data.iterrows():
            precio_actual = row['precio_cop']
            precio_pred = precio_actual * (1 + np.random.normal(0.1, 0.05))
            rent = (precio_pred - precio_actual) / precio_actual * 100
            rent_list.append(rent)
        rentabilidades[f'Cluster {cluster}'] = rent_list
    
    # Boxplot rentabilidad por cluster
    plt.figure(figsize=(10, 6))
    data_for_boxplot = [rentabilidades[f'Cluster {i}'] for i in range(3)]
    plt.boxplot(data_for_boxplot, labels=[f'Cluster {i}' for i in range(3)])
    plt.title('Rentabilidad por Cluster')
    plt.ylabel('Rentabilidad (%)')
    plt.xlabel('Cluster')
    plt.savefig('boxplot_rentabilidad.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # PCA scatter plot
    features = ['tamaño_m2', 'antiguedad', 'zona', 'habitaciones']
    X_pca = df_clusters[features]
    
    pca = PCA(n_components=2)
    X_pca_transformed = pca.fit_transform(X_pca)
    
    # Calcular rentabilidades para el scatter
    rent_values = []
    for _, row in df_clusters.iterrows():
        precio_actual = row['precio_cop']
        precio_pred = precio_actual * (1 + np.random.normal(0.1, 0.05))
        rent = abs((precio_pred - precio_actual) / precio_actual * 100)
        rent_values.append(rent)
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_pca_transformed[:, 0], X_pca_transformed[:, 1], 
                         s=[r*2 for r in rent_values], 
                         c=df_clusters['cluster'], 
                         cmap='viridis', alpha=0.7)
    plt.colorbar(scatter, label='Cluster')
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} varianza)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} varianza)')
    plt.title('PCA - Rentabilidad por tamaño de punto')
    plt.savefig('pca_rentabilidad.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Metricas del modelo supervisado
    y_pred = modelo_supervisado.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    varianza_explicada = sum(pca.explained_variance_ratio_)
    
    print(f"MSE: {mse:,.0f}")
    print(f"R2: {r2:.3f}")
    print(f"Varianza explicada PCA: {varianza_explicada:.3f}")