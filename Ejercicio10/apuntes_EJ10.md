**Ejercicio 10 - Analisis de Casas con PCA y K-means**

**NOTA:**

La maquina automaticamente separó las casas en 3 grupos donde cada uno tiene casas similares entre ellas: Cluster 0 (azul) agrupa casas pequeñas de estratos bajos y barrios normales, Cluster 1 (rojo) junta las casas grandes de estratos altos en barrios premium como El Poblado y Laureles, y Cluster 2 (verde) reúne casas medianas con características intermedias

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



**2- Como limpiar y preparar los datos para el analisis**

quantile: Elimina outliers extremos del 5% mas barato y caro de precio_cop
Ejemplo: Nos devuelve un dataset limpio de ~270 casas quitando precios por debajo de 150M y por encima de 700M COP

apply con clasificar_zona: Clasifica barrios en zonas 1=popular 2=media 3=premium
Ejemplo: Nos devuelve zona 3 para una casa en El Poblado en base a la lista de barrios premium



**3- Aplicar PCA y generar componentes principales**

StandardScaler: Normaliza las variables para igualar su importancia
Ejemplo: Nos devuelve datos escalados de tamano_m2 estrato zona y habitaciones

PCA fit_transform: Reduce a 2 componentes principales PC1 y PC2
Ejemplo: Nos devuelve PC1 y PC2 que explican mas del 70% de la varianza



**4- Aplicar K-means y visualizar resultados**

KMeans fit_predict: Asigna 3 clusters basados en datos escalados
Ejemplo: Nos devuelve 3 grupos con un cluster de casas premium con tamano_m2 alto

sns scatterplot: Genera graficos de dispersion guardados como pca_clusters.png y pca_tamano.png
Ejemplo: Nos devuelve un scatterplot de PC1 vs PC2 con clusters coloreados