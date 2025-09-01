**Ejercicio 2 - Análisis de Casas en Medellín**


**Dependencias**
Python 3.7+
Pandas
Matplotlib
Seaborn   

**Métodos y Funciones**

**1- Obtener información fundamental sobre las casas:**

head(): Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 casas, como una en Santa Cruz con 67 m², en base a los datos cargados

describe(): Genera estadísticas descriptivas (media, min, max, etc.).
Ejemplo: Nos devuelve un promedio de 76.7 m² para tamaño_m2 en base a todas las casas



**2- ¿Es mejor el precio por tamaño en ciertos barrios?**

groupby() con .mean(): Calcula promedios por grupos (condición simulada)
Ejemplo: Nos devuelve un promedio de 350M COP para precio_cop en barrio_alto (El Poblado) en base a los precios por barrio



**3- Interpretar la distribución de precios y detectar extremos:**

sns.histplot(): Crea histogramas para ver frecuencias de precios
Ejemplo: Nos devuelve un histograma con picos en 200M-300M COP para precio_cop en base a la distribución por condición

sns.boxplot(): Muestra boxplots para identificar outliers
Ejemplo: Nos devuelve un boxplot con extremos por encima de 1,000M COP en base a precio_cop por condición.



**4- Relación entre tamaño y precio:**

sns.scatterplot(): Grafica la relación entre dos variables
Ejemplo: Nos devuelve un scatterplot de tamaño_m2 vs precio_cop, mostrando variabilidad en base a los datos de tamaño y precio



**5- Correlación entre variables:**

corr(): Calcula correlaciones entre columnas numéricas
Ejemplo: Nos devuelve una correlación de 0.5 entre tamaño_m2 y precio_cop en base a las variables numéricas

sns.heatmap(): Visualiza el mapa de calor de correlaciones
Ejemplo: Nos devuelve un heatmap destacando correlaciones como 0.5 en base a tamaño_m2 y precio_cop