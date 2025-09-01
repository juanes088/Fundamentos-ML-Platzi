**Ejercicio 5 - Capacidad de Generalización y Rentabilidad de Casas en Medellín**


**Dependencias**
Python 3.7+
Pandas
Scikit-learn
IPython
IPywidgets

**Métodos y Funciones**

**1- Obtener información fundamental sobre las casas:**

head(): Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 casas, como una en Santa Cruz con 67 m², en base a los datos cargados

describe(): Genera estadísticas descriptivas (media, min, max, etc)
Ejemplo: Nos devuelve un promedio de 76.7 m² para tamaño_m2 en base a todas las casas



**2- ¿Cómo dividir los datos para evaluar generalización?**

train_test_split(): Divide el dataset en conjuntos de entrenamiento y prueba
Ejemplo: Nos devuelve 240 casas para entrenamiento y 60 para prueba con un test_size=0.2 en base a la division estandar

widgets.FloatSlider: Crea un slider interactivo para ajustar el tamaño de prueba
Ejemplo: Nos devuelve un slider que muestra 240 casas de entrenamiento cuando test_size=0.2 en base a la interaccion



**3- Interpretar la division de datos y detectar tamaños:**

len(): Calcula el tamaño de los conjuntos de entrenamiento y prueba
Ejemplo: Nos devuelve 240 casas en el conjunto de entrenamiento en base a la division con test_size=0.2

display(): Muestra los primeros registros de cada conjunto
Ejemplo: Nos devuelve las primeras 5 filas de entrenamiento, como una casa con 67 m², en base a los datos divididos



**4- Relación entre tamaño de prueba y generalización:**

train_test_split() con slider: Ajusta dinámicamente la proporcion de prueba
Ejemplo: Nos devuelve 210 casas de entrenamiento y 90 de prueba cuando test_size=0.3 en base a la interaccion del slider

print(): Muestra los tamaños actualizados en tiempo real
Ejemplo: Nos devuelve "Tamaño conjunto prueba: 90 casas" en base al valor del slider



**5- Preparación para estimación de rentabilidad:**

X y y: Define variables predictoras y objetivo para futuros modelos
Ejemplo: Nos devuelve tamaño_m2 y precio_cop como base para predecir precios futuros en base a las variables seleccionadas

random_state=42: Asegura reproducibilidad en las divisiones
Ejemplo: Nos devuelve la misma division (240 train, 60 test) en cada ejecucion con test_size=0.2