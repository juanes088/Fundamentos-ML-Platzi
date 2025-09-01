import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# 1- obtener informacion fundamental sobre las casas
print("Informacion fundamental:")
print(datos_casas.head())  
print(datos_casas.describe())  

# 2- Es mejor el precio por tamaño en ciertos barrios?
datos_casas['condicion'] = datos_casas['barrio'].apply(lambda x: 'barrio_alto' if x in ['El Poblado', 'Envigado'] else 'barrio_bajo')
print("\nPromedio de precio por condicion:")
print(datos_casas.groupby('condicion')['precio_cop'].mean())  

# 3- Interpretar la distribucion de precios y detectar extremos
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(data=datos_casas, x='precio_cop', hue='condicion')  
plt.title('Distribucion de precios por condicion')
plt.subplot(1, 2, 2)
sns.boxplot(data=datos_casas, x='condicion', y='precio_cop')  
plt.title('Boxplot de precios por condicion')
plt.tight_layout()
plt.show()

# 4- Relacion entre tamaño y precio
plt.figure(figsize=(6, 4))
sns.scatterplot(data=datos_casas, x='tamaño_m2', y='precio_cop', hue='condicion')  
plt.title('Relacion entre tamaño y precio')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio (COP)')
plt.show()

# 5- Correlacion entre variables
plt.figure(figsize=(8, 6))
correlacion = datos_casas[['tamaño_m2', 'precio_cop', 'antiguedad', 'habitaciones']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Mapa de calor de correlaciones')
plt.show()