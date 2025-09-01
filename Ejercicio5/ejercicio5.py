import pandas as pd
from sklearn.model_selection import train_test_split
import ipywidgets as widgets
from IPython.display import display

datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# Ingenieria basica
datos_casas['antiguedad_ajustada'] = 2025 - pd.to_datetime(datos_casas['fecha_construccion'], errors='coerce').dt.year
datos_casas['precio_por_m2'] = datos_casas['precio_cop'] / datos_casas['tamaño_m2']

# mostrar las primeras filas
print("Primeras filas del dataset:")
display(datos_casas.head())

# slider interactivo para elegir porcentaje de prueba
slider_test_size = widgets.FloatSlider(
    value=0.2, min=0.1, max=0.5, step=0.05,
    description='% Test Set:', continuous_update=False
)

display(slider_test_size)

def dividir_datos(test_size):
    # variables predictoras (X) y objetivo (y)
    X = datos_casas[['tamaño_m2', 'antiguedad', 'habitaciones', 'antiguedad_ajustada', 'precio_por_m2']]
    y = datos_casas['precio_cop']

    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    print(f"Tamaño conjunto entrenamiento: {len(X_train)} casas")
    print(f"Tamaño conjunto prueba: {len(X_test)} casas")
    print("\nConjunto de entrenamiento (primeros registros):")
    display(X_train.head())
    print("\nConjunto de prueba (primeros registros):")
    display(X_test.head())

    return X_train, X_test, y_train, y_test

# Usa el widget interactivo
widgets.interactive(dividir_datos, test_size=slider_test_size)

# Division estandar recomendada - 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    datos_casas[['tamaño_m2', 'antiguedad', 'habitaciones', 'antiguedad_ajustada', 'precio_por_m2']],
    datos_casas['precio_cop'],
    test_size=0.2, random_state=42
)

print("\nDivisión estándar (80-20):")
print(f"Tamaño conjunto entrenamiento: {len(X_train)} casas")
print(f"Tamaño conjunto prueba: {len(X_test)} casas")
print("\nConjunto de entrenamiento (primeros registros):")
display(X_train.head())
print("\nConjunto de prueba (primeros registros):")
display(X_test.head())