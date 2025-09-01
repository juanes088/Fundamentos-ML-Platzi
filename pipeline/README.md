**Proyecto Final - Sistema de Rentabilidad Inmobiliaria Medellin**

**NOTA:**

En base a lo que vimos en el curso con el profe Juan Carlos se aplico un sistema hibrido que combina aprendizaje supervisado (Ridge Regression) para predecir precios con aprendizaje no supervisado (K-means) para segmentar propiedades. El sistema automaticamente separa las propiedades en 3 grupos donde cada uno tiene caracteristicas similares: Cluster 0 agrupa propiedades pequeñas/medianas de zonas populares, Cluster 1 junta propiedades de zonas medias con caracteristicas mixtas, y Cluster 2 reune propiedades grandes/premium de barrios como El Poblado y Laureles. Lo mejor es que permite simular rentabilidad a diferentes plazos (1-10 años) usando tasas diferenciadas por zona: 10% anual para zonas premium, 8% para medias y 6% para populares, lo cual refleja el comportamiento real del mercado inmobiliario en Medellin. Y para subir la dificultad en este ultimo ejercicio, trabaje con un dataset de 3000 datos, el cual tenia informacion de toda la area metropolitana de medellin, por lo que fue necesario hacer una limpieza del dataset

**Dependencias**

Python 3.7+
Pandas: Libreria para manipulacion de datos
Scikit-learn: Libreria para machine learning
Matplotlib: Libreria para visualizaciones
NumPy: Libreria para operaciones numericas

**Metodos y Funciones**


**1- Obtener informacion fundamental sobre las propiedades**

head(): Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 propiedades como una en El Poblado con 85 m2 en base a los datos cargados

describe(): Genera estadisticas descriptivas (implicito en limpieza)
Ejemplo: Nos devuelve un promedio de 76.7 m2 para tamaño_m2 en base a las 2700 propiedades limpias



**2- Como limpiar y preparar los datos para el analisis**
quantile(): Elimina outliers extremos del 5% mas barato y caro de precio_cop
Ejemplo: Nos devuelve un dataset limpio de ~2700 propiedades quitando precios por debajo de 150M y por encima de 1200M COP

filtrar_medellin(): Filtra solo barrios de Medellin y asigna zona (1=alta, 2=media, 3=popular)
Ejemplo: Nos devuelve zona 1 para una propiedad en El Poblado en base a la lista de barrios premium



**3- Entrenar modelos de machine learning**
Ridge() con Pipeline: Entrena modelo supervisado con normalizacion StandardScaler para predecir precios
Ejemplo: Nos devuelve un modelo que predice 300M COP para una propiedad de 80m2 en zona 2

KMeans() con Pipeline: Entrena modelo no supervisado con 3 clusters para segmentar propiedades
Ejemplo: Nos devuelve 3 grupos con un cluster de propiedades premium con tamaño_m2 alto y zona 1



**4- Simular rentabilidad con horizonte temporal**
Tasas diferenciadas por zona: Aplica crecimiento anual segun la zona de la propiedad
Ejemplo: Nos devuelve 10% anual para zona 1, 8% para zona 2 y 6% para zona 3

Calculo de interes compuesto: Proyecta precio futuro usando formula precio_actual * (1 + tasa)^años
Ejemplo: Nos devuelve 238M COP en 6 años para una propiedad de 168M COP actual en zona 3



**5- Generar visualizaciones y metricas**
PCA scatter plot: Reduce dimensionalidad a 2 componentes principales guardado como pca_rentabilidad.png
Ejemplo: Nos devuelve un scatterplot de PC1 vs PC2 que explican 84.25% + 15.67% = 99.92% de la varianza

boxplot por cluster: Muestra distribucion de rentabilidades por cluster guardado como boxplot_rentabilidad.png
Ejemplo: Nos devuelve un boxplot con medianas similares (~10%) pero diferentes outliers por cluster

Metricas del modelo: Calcula MSE, R2 y varianza explicada para evaluar calidad
Ejemplo: Nos devuelve R2 de 0.959 indicando que el modelo explica 95.9% de la variacion en precios



**6- Interaccion con el usuario y recomendaciones**
input() interactivo: Solicita datos de la propiedad y años de proyeccion
Ejemplo: Nos permite ingresar 57m2, 43 años, zona 3, 2 habitaciones y 6 años de proyeccion

calcular_rentabilidad(): Evalua viabilidad usando umbral del 15% para rentabilidad total
Ejemplo: Nos devuelve "Viable" para una rentabilidad de 41.85% en 6 años vs umbral de 15%

# ESTADO DEL MODELO

- R2 = 0.959 - Este numero significa que el modelo predice correctamente el precio de 96 de cada 100 propiedades. Es bastante bueno porque cualquier cosa arriba de 0.8 ya se considera excelente para modelos de ML.

- MSE = 2,085,944,958,835,607 - Se ve como un numero gigante y raro, pero es normal cuando trabajas con precios en millones de pesos. Lo importante es que el R2 alto nos dice que a pesar del error, el modelo funciona bien.

- Varianza explicada PCA = 0.999 - Esto significa que las 4 variables que usamos (tamaño, antiguedad, zona, habitaciones) se pueden comprimir en solo 2 "super-variables" sin perder casi nada de informacion. Es como hacer un resumen perfecto.

# GRAFICA

El boxplot muestra que los 3 clusters tienen rentabilidades parecidas (alrededor del 10% en la mediana), pero con algunos valores raros en todos los grupos. Basicamente el algoritmo de clustering encontro grupos bien balanceados

El grafico PCA es mas interesante: el Cluster 0 (morado) esta concentrado a la izquierda, el Cluster 1 (verde-azul) en el centro, y el Cluster 2 (amarillo) disperso a la derecha. El tamaño de cada punto representa la rentabilidad. PC1 explica el 84.25% de la variacion (probablemente tiene que ver con tamaño y precio) y PC2 explica el 15.67% restante (posiblemente zona y antiguedad)