**Ejercicio 9 - Clustering de Casas con K-means**

**NOTA:**

Este ejercicio usa K-means (Como en la clase de - Interpretación de clusters de K-means para perfiles de jugadores -) para agrupar casas del dataset de Medellin y la verdad es sorprendente ver los resultados. El algoritmo automaticamente separo las casas en 3 grupos que tienen mucho sentido: Cluster 1 "Casas Grandes" (97m² promedio) que incluyen barrios premium como Envigado y Laureles, Cluster 0 "Casas Promedio" (75m²) de estratos medios, y Cluster 2 "Casas Pequeñas" (55m²) principalmente de barrios populares como Popular y Villa Hermosa. Lo más interesante es que el algoritmo descubrio solo lo que cualquier persona que conozca Medellin te diria: que los barrios premium tienen casas mas grandes y costosas, mientras que los populares son mas pequeñas y economicas. Es genial ver como el machine learning puede encontrar patrones reales del mercado inmobiliario sin que uno le tenga que explicar nada sobre la ciudad :0


**Dependencias**

Python 3 7+ 
Pandas: Libreria para manipulacion de datos 
Seaborn: Libreria para graficos estadisticos 
Matplotlib: Libreria para visualizaciones 
Scikit-learn: Libreria para machine learning 

**Metodos y Funciones**

**1- Obtener informacion fundamental sobre las casas**

head: Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 casas como una en Santa Cruz con 67 m2 en base a los datos cargados

describe: Genera estadisticas descriptivas implicito en limpieza
Ejemplo: Nos devuelve un promedio de 76 7 m2 para tamano_m2 en base a las casas limpias



**2- Como limpiar y preparar los datos para el clustering**

quantile: Elimina outliers extremos del 5% mas barato y caro de precio_cop
Ejemplo: Nos devuelve un dataset limpio de ~270 casas quitando precios por debajo de 150M y por encima de 700M COP

apply con clasificar_zona: Clasifica barrios en zonas 1=popular 2=media 3=premium
Ejemplo: Nos devuelve zona 3 para una casa en El Poblado en base a la lista de barrios premium



**3- Aplicar K-means y generar clusters**

KMeans fit_predict: Asigna 3 clusters basados en tamano_m2 estrato zona y habitaciones
Ejemplo: Nos devuelve 3 grupos con un cluster de casas premium con tamano_m2 alto y zona 3

groupby mean: Calcula promedios de caracteristicas por cluster
Ejemplo: Nos devuelve un promedio de 96 9 m2 para el cluster premium



**4- Visualizar y analizar los resultados**

sns boxplot: Genera boxplots por variable guardados como boxplot_feature png
Ejemplo: Nos devuelve un boxplot de tamano_m2 mostrando mediana y outliers por cluster

Vista interactiva simulada: Muestra datos de cada cluster en la terminal
Ejemplo: Nos devuelve una tabla con casas del cluster 1 incluyendo barrio tamano_m2 y estrato