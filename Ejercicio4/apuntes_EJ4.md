**Ejercicio 4 - Selección de Características para Casas en Medellín**

**DEPENCENCIAS**
Pandas
Matplotlib
Scikit-learn
NumPy

**Métodos y Funciones**

**1- Obtener información fundamental sobre las casas:**

head(): Muestra las primeras filas para verificar los datos.
Ejemplo: Nos devuelve las primeras 5 casas, como una en Santa Cruz con 67 m², en base a los datos cargados

describe(): Genera estadísticas descriptivas (media, min, max, etc)
Ejemplo: Nos devuelve un promedio de 76.7 m² para tamaño_m2 en base a todas las casas



**2- ¿Cuáles son las variables más relevantes para el precio?**

SelectKBest con f_regression: Selecciona las variables con mayor relación lineal con precio_cop usando F-score
Ejemplo: Nos devuelve tamaño_m2 con un F-Score de 150 como la más relevante en base a su impacto en precio_cop

DecisionTreeRegressor: Evalúa la importancia de variables capturando relaciones no lineales
Ejemplo: Nos devuelve tamaño_m2 con 0.45 de importancia en base a su contribución al modelo



**3- Interpretar la relevancia de las variables y detectar diferencias:**

plt.bar() con F-Score: Crea un gráfico de barras para los puntajes de SelectKBest
Ejemplo: Nos devuelve un gráfico con tamaño_m2 como el mayor F-Score (150) en base a la selección univariada

plt.bar() con Importancia: Muestra un gráfico de barras para las importancias del árbol
Ejemplo: Nos devuelve un gráfico con tamaño_m2 como la mayor importancia (45%) en base al árbol de decisión



**4- Relación entre técnicas de selección:**

plt.subplot(): Combina gráficos para comparar SelectKBest y DecisionTreeRegressor   
Ejemplo: Nos devuelve dos gráficos lado a lado mostrando tamaño_m2 como relevante en ambas técnicas en base a los puntajes e importancias



**5- Correlación y validación de variables:**

corr(): Calcula correlaciones entre columnas numéricas (opcional para contexto)
Ejemplo: Nos devuelve una correlación de 0.8 entre tamaño_m2 y precio_por_m2 en base a las variables numéricas

sns.heatmap(): Visualiza el mapa de calor de correlaciones (opcional para validación)
Ejemplo: Nos devuelve un heatmap destacando 0.8 de correlación entre tamaño_m2 y precio_por_m2