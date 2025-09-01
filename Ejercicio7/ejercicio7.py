import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets

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
        return 3 
    elif barrio in barrios_medios:
        return 2
    else:
        return 1

datos_limpios['zona'] = datos_limpios['barrio'].apply(clasificar_zona)

# Variables predictoras y objetivo
X = datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']]
y = datos_limpios['precio_cop']

# Division estandar: 80% entrenamiento / 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar y entrenar modelo
modelo_rl = LinearRegression()
modelo_rl.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo_rl.predict(X_test)

# Calcular metricas
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n!Metricas del modelo!")
print(f"MSE (Error Cuadratico Medio): {mse:.2f} COP^2")
print(f"RMSE (Raiz del Error Cuadratico Medio): {rmse:.2f} COP")
print(f"MAE (Error Absoluto Medio): {mae:.2f} COP")
print(f"R2 (Coeficiente de Determinacion): {r2:.2f}")

# Histograma de residuos
plt.figure(figsize=(8, 5))
sns.histplot(y_test - y_pred, bins=15, kde=True)
plt.title('Distribucion de Errores de Prediccion (Residuos)')
plt.xlabel('Error (Real - Prediccion)')
plt.ylabel('Frecuencia')
plt.savefig('regresion_lineal_grafica.png')
plt.close()

print("\nGrafico de residuos guardado como: regresion_lineal_grafica.png")

# Widget interactivo para evaluar MAE
def evaluar_predicciones(threshold_mae):
    calidad = "buena" if mae <= threshold_mae else "regular o mala"
    print(f"Tu modelo tiene una MAE de {mae:.2f} COP, considerada {calidad} (umbral definido: {threshold_mae} COP).")

umbral_widget = widgets.FloatSlider(min=1000000, max=100000000, step=1000000, value=20000000, description='Umbral MAE (COP):')
widgets.interactive(evaluar_predicciones, threshold_mae=umbral_widget)