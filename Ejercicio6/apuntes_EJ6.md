**Ejercicio 6 - Predicción de Precios de Casas con Regresión Lineal**

**NOTA:**

Empece con el ejercicio basico que vimos en clase (solo tamano y antiguedad) pero como el profesor Juan Carlos nos dijo que experimentaramos, le agregue mas variables del dataset: habitaciones, estrato y barrio, el barrio lo agrupe por zonas (Popular, Media, Premium) porque era mas logico que asignarle numeros random a cada barrio. Tambien tuve que limpiar los outliers extremos (saque el 5% mas caro y mas barato) porque habia casas muy raras que confundian al modelo. Al final el grafico se ve mucho mejor, los puntos estan mas pegados a la linea roja y los coeficientes tienen mas sentido - resulta que el estrato y la zona son los que mas impactan el precio (cosa que tiene sentido en Medellin). Aun le falta mejorar porque sigue siendo impreciso en casas muy caras, pero ya es bastante mejor que el modelo inicial :3


**Dependencias**

Python 3.7+
Pandas
Scikit-learn
Matplotlib
Seaborn

**Métodos y Funciones**

**1- Obtener información fundamental sobre las casas:**

head(): Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 casas, como una en Santa Cruz con 67 m², en base a los datos cargados

describe(): Genera estadísticas descriptivas (opcional, implicito en limpieza)
Ejemplo: Nos devuelve un promedio de 76.7 m² para tamaño_m2 en base a las casas limpias



**2- ¿Cómo limpiar y preparar los datos para el modelo?**

quantile(): Elimina outliers extremos del 5% más barato y caro de precio_cop
Ejemplo: Nos devuelve un dataset limpio de ~270 casas quitando precios por debajo de 150M y por encima de 700M COP

apply() con clasificar_zona(): Clasifica barrios en zonas (1=popular, 2=media, 3=premium)
Ejemplo: Nos devuelve zona 3 para una casa en El Poblado en base a la lista de barrios premium



**3- Entrenar el modelo de regresión lineal:**

train_test_split(): Divide el dataset en 80% entrenamiento y 20% prueba
Ejemplo: Nos devuelve 216 casas para entrenamiento y 54 para prueba en el dataset limpio

LinearRegression.fit(): Entrena el modelo y optimiza coeficientes
Ejemplo: Nos devuelve un intercepto de -92M COP y coeficientes como +6.7M COP por m²



**4- Interpretar y visualizar las predicciones:**

predict(): Calcula precios predichos para el conjunto de prueba
Ejemplo: Nos devuelve 419M COP predicho para una casa real de 514M COP

sns.scatterplot(): Crea un grafico de dispersión guardado como grafico.png
Ejemplo: Nos devuelve un scatterplot mostrando cercanía a la linea ideal en base a precios reales vs. predichos



**5- Explorar predicciones interactivas:**

input(): Permite ingresar tamaño, habitaciones, estrato, y zona manualmente
Ejemplo: Nos devuelve 300M COP para una casa de 80 m², 2 habitaciones, estrato 3, zona 2

pd.DataFrame(): Prepara la entrada para la predicción
Ejemplo: Nos procesa los valores ingresados para predecir el precio