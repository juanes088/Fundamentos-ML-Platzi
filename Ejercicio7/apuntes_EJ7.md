**Ejercicio 7 - Evaluacion de Predicciones de Precios de Casas**

**NOTA**

El grafico nos dice:

Eje horizontal:

Dice "Error (Real - Prediccion)"
- Los numeros van de -0.75 a 1.25
- En realidad significa: de -75 millones a +125 millones de pesos
- Centro (0): la maquina acertó perfecto
- Lado izquierdo (negativo): la maquina dijo un precio MUY ALTO
- Lado derecho (positivo): la maquina dijo un precio MUY BAJO


**DEPENDENCIAS**

Python 3 7+ 
Pandas: Libreria para manipulacion de datos 
Scikit-learn: Libreria para machine learning 
NumPy: Libreria para operaciones numericas 
Matplotlib: Libreria para visualizaciones 
Seaborn: Libreria para graficos estadisticos
IPywidgets: Libreria para widgets interactivos

**Metodos y Funciones**

**1- Obtener informacion fundamental sobre las casas**

head: Muestra las primeras filas para verificar los datos
Ejemplo: Nos devuelve las primeras 5 casas como una en Santa Cruz con 67 m2 en base a los datos cargados

describe: Genera estadisticas descriptivas implicito en limpieza
Ejemplo: Nos devuelve un promedio de 76 7 m2 para tamano_m2 en base a las casas limpias



**2- Como limpiar y preparar los datos para la evaluacion**

quantile: Elimina outliers extremos del 5% mas barato y caro de precio_cop
Ejemplo: Nos devuelve un dataset limpio de ~270 casas quitando precios por debajo de 150M y por encima de 700M COP

apply con clasificar_zona: Clasifica barrios en zonas 1=popular 2=media 3=premium
Ejemplo: Nos devuelve zona 3 para una casa en El Poblado en base a la lista de barrios premium



**3- Entrenar el modelo y generar predicciones**

train_test_split: Divide el dataset en 80% entrenamiento y 20% prueba
Ejemplo: Nos devuelve 216 casas para entrenamiento y 54 para prueba en el dataset limpio

LinearRegression fit y predict: Entrena el modelo y predice precios
Ejemplo: Nos devuelve 419M COP predicho para una casa real de 514M COP



**4- Evaluar el modelo con metricas**

mean_squared_error: Calcula MSE RMSE MAE y R2
Ejemplo: Nos devuelve RMSE de 50M COP y R2 de 0 6 en base a las predicciones

sns histplot: Crea un histograma de residuos guardado como residuos png
Ejemplo: Nos devuelve un histograma mostrando errores centrados cerca de 0M COP



**5- Analizar interactivamente los resultados**

widgets FloatSlider: Permite ajustar un umbral de MAE para evaluar calidad
Ejemplo: Nos devuelve buena calidad si MAE 20M COP es menor a un umbral de 30M COP

evaluar_predicciones: Muestra la calidad del modelo dinamicamente
Ejemplo: Nos indica regular o mala si MAE excede el umbral definido