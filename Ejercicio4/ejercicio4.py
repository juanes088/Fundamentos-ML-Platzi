import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.tree import DecisionTreeRegressor

datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# enriquecer el dataset
datos_casas['antiguedad_ajustada'] = 2025 - pd.to_datetime(datos_casas['fecha_construccion'], errors='coerce').dt.year
datos_casas['precio_por_m2'] = datos_casas['precio_cop'] / datos_casas['tamaño_m2']

# seleccion de variables predictoras (X) y variable objetivo (y)
X = datos_casas[['tamaño_m2', 'antiguedad', 'habitaciones', 'antiguedad_ajustada', 'precio_por_m2']]
y = datos_casas['precio_cop']

# 1- seleccion univariada con SelectKBest
selector = SelectKBest(score_func=f_regression, k=3) 
selector.fit(X, y)

# Obtener puntajes F
f_scores = pd.DataFrame({'Variable': X.columns, 'F-Score': selector.scores_})
print("Puntajes F (SelectKBest):")
print(f_scores.sort_values(by='F-Score', ascending=False))

# 2- Seleccion con arbol de decision
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Obtener importancia de caracteristicas
importances = pd.DataFrame({'Variable': X.columns, 'Importancia': model.feature_importances_})
print("\nImportancia de características (Árbol de Decisión):")
print(importances.sort_values(by='Importancia', ascending=False))

# 3- Visualizacion con dos graficos
plt.figure(figsize=(14, 5))

# Grafico de F-Score de SelectKBest
plt.subplot(1, 2, 1)
plt.bar(f_scores['Variable'], f_scores['F-Score'], color='skyblue', alpha=0.8)
plt.title('Relevancia por F-Score (SelectKBest)', fontsize=12)
plt.xlabel('Variables', fontsize=10)
plt.ylabel('F-Score', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafico de Importancia del arbol de decision
plt.subplot(1, 2, 2)
plt.bar(importances['Variable'], importances['Importancia'] * 100, color='lightcoral', alpha=0.8)
plt.title('Importancia por Árbol de Decisión', fontsize=12)
plt.xlabel('Variables', fontsize=10)
plt.ylabel('Importancia (%)', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Mostrar las variables seleccionadas
selected_features_kbest = X.columns[selector.get_support()].tolist()
print("\nVariables seleccionadas por SelectKBest:", selected_features_kbest)