**Práctica 1 - Análisis de Casas en Medellín**
Este repositorio contiene el código y los datos para el análisis inicial de un dataset de casas en Medellín usando Python y Pandas. El objetivo es limpiar y preparar los datos para futuros análisis predictivos.
Dependencias

Python 3.7+: Entorno de programación.
Pandas: Librería para manipulación de datos (instalar con pip install pandas).

**Métodos y Funciones**

**Importación de datos:**

*pd.read_csv("casas_medellin.csv"): Carga el archivo CSV en un DataFrame.

    Ejemplo: Nos devuelve un DataFrame con datos de casas como tamaño y precio en base al archivo casas_medellin.csv.

*head(): Muestra las primeras 5 filas para verificar la carga.

    Ejemplo: Nos devuelve las primeras 5 casas, como una en Santa Cruz con 67 m², en base a los datos cargados.



**Detección y manejo de datos faltantes:**

*isnull().sum(): Cuenta valores nulos por columna.

    Ejemplo: Nos devuelve 0 faltantes para precio_cop en base a las 300 filas del dataset.

*fillna(): Imputa valores faltantes (usado con .mean() para precio_cop y antiguedad).

    Ejemplo: Nos devuelve un precio_cop de 303,253,600 COP para un valor faltante en base al promedio de todos los precios.



**Codificación de variables categóricas:**

*get_dummies(): Convierte columnas categóricas (barrio, estrato) en variables binarias.

    Ejemplo: Nos devuelve columnas como barrio_Santa Cruz (True/False) en base a la categoría del barrio de cada casa.



**Eliminación de duplicados:**

*drop_duplicates(): Remueve filas duplicadas del dataset.

    Ejemplo: Nos devuelve 300 filas únicas en base a la eliminación de duplicados como una casa repetida en Santa Cruz.



**Conversión de fechas:**

*to_datetime(): Transforma fecha_construccion a formato de tiempo con errors='coerce'.

    Ejemplo: Nos devuelve 1979-01-01 como fecha válida para una casa en base a la cadena "1979" en fecha_construccion.



**Revisión final:**

*info(): Proporciona detalles sobre columnas, tipos de datos y memoria.

    Ejemplo: Nos devuelve 31 columnas y 300 filas en base a la estructura del dataset procesado.

*describe(): Genera estadísticas descriptivas de las columnas numéricas.

    Ejemplo: Nos devuelve un promedio de 76.7 m² para tamaño_m2 en base a los datos de todas las casas.

    

**Instrucciones**

Instala las dependencias con pip install pandas matplotlib
Coloca casas_medellin.csv en la misma carpeta que analisis.py
Ejecuta el script con python analisis.py en tu entorno virtual (ej. (fundamentosML))

**NOTA**

El dataset contiene 300 filas con columnas como tamaño_m2, precio_cop, y barrio