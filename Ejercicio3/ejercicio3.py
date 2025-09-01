import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# 1- Ingenieria de caracteristicas: Crear nuevas variables
datos_casas['antiguedad_ajustada'] = 2025 - pd.to_datetime(datos_casas['fecha_construccion'], errors='coerce').dt.year

# Ratio: Precio por metro cuadrado
datos_casas['precio_por_m2'] = datos_casas['precio_cop'] / datos_casas['tamaño_m2']

# Ratio: Habitaciones por antiguedad
datos_casas['ratio_hab_antiguedad'] = datos_casas['habitaciones'] / datos_casas['antiguedad']

# 2- Obtener informacion fundamental
print("Estadísticas descriptivas de las nuevas variables:")
print(datos_casas[['antiguedad_ajustada', 'precio_por_m2', 'ratio_hab_antiguedad']].describe())

# 3- Visualizacion y analisis
# Histograma: Distribucion de precio por m²
plt.figure(figsize=(10, 5))
sns.histplot(data=datos_casas, x='precio_por_m2')
plt.title('Distribucion de precio por m²')
plt.xlabel('Precio por m² (COP)')
plt.ylabel('Frecuencia')
plt.show()

# Boxplot: Detectar extremos en precio por m²
plt.figure(figsize=(6, 4))
sns.boxplot(data=datos_casas, y='precio_por_m2')
plt.title('Boxplot de precio por m²')
plt.ylabel('Precio por m² (COP)')
plt.show()

# Scatterplot: Relacion entre tamaño y precio por m²
plt.figure(figsize=(6, 4))
sns.scatterplot(data=datos_casas, x='tamaño_m2', y='precio_por_m2')
plt.title('Relacion entre tamaño y precio por m²')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio por m² (COP)')
plt.show()

# Heatmap: Correlacion entre variables
plt.figure(figsize=(8, 6))
correlacion = datos_casas[['tamaño_m2', 'precio_cop', 'antiguedad_ajustada', 'precio_por_m2', 'habitaciones']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Mapa de calor de correlaciones')
plt.show()