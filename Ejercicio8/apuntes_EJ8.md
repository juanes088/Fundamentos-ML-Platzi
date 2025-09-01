**Ejercicio 8 - Clustering de Casas con K-means**

=======================================================================

**NOTA**

**Scatter plot de clusters (Diagrama de dispersión de clústeres):**

Los 3 tipos de casas que encontro la maquina:

(🟢) CLUSTER 0 - "Casas medianas en barrios populares"

Tamaño: 75 m² (medianas)
Estrato: 3.4 (medio)
Zona: 1.3 (principalmente barrios populares)
Habitaciones: 1.9 (casi 2)


(🟠) CLUSTER 1 - "Casas grandes en zonas mixtas"

Tamaño: 97 m² (grandes)
Estrato: 4.1 (alto)
Zona: 1.8 (entre popular y media)
Habitaciones: 2.5 (entre 2 y 3)


(🔵) CLUSTER 2 - "Casas pequeñas basicas"

Tamaño: 55 m² (pequeñas)
Estrato: 2.7 (bajo)
Zona: 1.1 (barrios populares)
Habitaciones: 1.6 (entre 1 y 2)

**Pairplot (matriz de correlación visual):**

cuadrícula de 4x4 porque tienes 4 variables:

- tamaño_m2
- estrato
- zona
- habitaciones

Relaciones principales que confirma:

* Tamaño - Estrato con casas grandes = mejor estrato
* Zona - Estrato con zonas premium (3) = mejor estrato
* Habitaciones - Tamaño con más habitaciones = casas más grandes
* Zona - Tamaño con zonas premium tienden a tener casas más grandes

=======================================================================

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
Ejemplo: Nos devuelve un promedio de 100 m2 para el cluster premium



**4- Visualizar los resultados**

sns pairplot: Genera un grafico de pares guardado como pairplot png
Ejemplo: Nos devuelve relaciones entre tamano_m2 estrato zona y habitaciones

sns scatterplot: Genera un grafico de dispersion guardado como clusters_k3 png
Ejemplo: Nos devuelve un scatterplot de tamano_m2 vs zona con 3 clusters coloreados