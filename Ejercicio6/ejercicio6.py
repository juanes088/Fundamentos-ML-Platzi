import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
datos_casas = pd.read_csv("C:/Users/Juan Esteban/Downloads/Fundamentos de machine learning/casas_medellin.csv")

# Limpiar outliers extremos (quitar las casas muy caras o muy baratas que confunden al modelo)
q1 = datos_casas['precio_cop'].quantile(0.05)  
q3 = datos_casas['precio_cop'].quantile(0.95)  
datos_limpios = datos_casas[(datos_casas['precio_cop'] >= q1) & (datos_casas['precio_cop'] <= q3)]

print(f"Dataset original: {len(datos_casas)} casas")
print(f"Dataset limpio: {len(datos_limpios)} casas (quitamos extremos)")

# Agrupar barrios por zonas (mas logico que numeros aleatorios)
barrios_premium = ['El Poblado', 'Envigado', 'Laureles']
barrios_medios = ['Conquistadores', 'Prado', 'Estadio', 'Belen', 'La America', 'Guayabal']
# El resto son barrios populares

def clasificar_zona(barrio):
    if barrio in barrios_premium:
        return 3  # Zona premium
    elif barrio in barrios_medios:
        return 2  # Zona media
    else:
        return 1  # Zona popular

datos_limpios['zona'] = datos_limpios['barrio'].apply(clasificar_zona)

# Variables predictoras y objetivo (las mas importantes)
X = datos_limpios[['tamaño_m2', 'estrato', 'zona', 'habitaciones']]
y = datos_limpios['precio_cop']

# Division estandar: 80% entrenamiento / 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar y entrenar modelo
modelo_rl = LinearRegression()
modelo_rl.fit(X_train, y_train)

print("\n!Modelo entrenado exitosamente!")
print(f"Intercepto (b0): {modelo_rl.intercept_:.2f}")
print(f"Coeficientes (b): {modelo_rl.coef_}")
for idx, col_name in enumerate(X.columns):
    print(f"Si aumentamos 1 unidad en '{col_name}', el precio cambia en promedio {modelo_rl.coef_[idx]:.2f} COP")

# Hacer predicciones
y_pred = modelo_rl.predict(X_test)

# Comparar predicciones vs valores reales
df_resultados = X_test.copy()
df_resultados['Precio_Real'] = y_test
df_resultados['Precio_Predicho'] = y_pred.round(2)
print("\nPrimeros 10 resultados (Predicciones vs Reales):")
print(df_resultados.head(10).to_string())  

# Crear grafico de dispersion y guardarlo
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Precio Real (COP)')
plt.ylabel('Precio Predicho (COP)')
plt.title('Predicciones vs Resultados Reales de Precios')
plt.axline((0, 0), slope=1, color='red', linestyle='--')  
plt.savefig('grafico.png')  
plt.close()  

print("\nGrafico guardado como: grafico.png")

# Prediccion con valores ingresados
tamano = float(input("Ingresa el tamano (m2): "))
habitaciones = int(input("Ingresa numero de habitaciones: "))
estrato = int(input("Ingresa el estrato (1-6): "))

print("Zonas disponibles:")
print("1 = Zona Popular (Popular, Santa Cruz, Villa Hermosa, etc)")
print("2 = Zona Media (Prado, Estadio, Belen, La America, etc)")
print("3 = Zona Premium (El Poblado, Envigado, Laureles)")
zona = int(input("Ingresa la zona (1-3): "))

# Crear entrada para prediccion
entrada = pd.DataFrame([[tamano, estrato, zona, habitaciones]], 
columns=['tamaño_m2', 'estrato', 'zona', 'habitaciones'])
pred = modelo_rl.predict(entrada)[0]
print(f"Precio predicho: {pred:.2f} COP")
input("Enter para salir:D")