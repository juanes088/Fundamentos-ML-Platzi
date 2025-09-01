import pandas as pd

# 1- Importar los datos usando Pandas
datos_casas = pd.read_csv("C:\\Users\\Juan Esteban\\Downloads\\Fundamentos de machine learning\\casas_medellin.csv")
print("Primeras 5 filas:")
print(datos_casas.head())

# 2- Detectar y tratar datos faltantes
print("\nDatos faltantes por columna:")
print(datos_casas.isnull().sum())

# Imputar valores faltantes (por ejemplo, promedio para precio_cop y antiguedad)
if datos_casas['precio_cop'].isnull().sum() > 0:
    datos_casas['precio_cop'] = datos_casas['precio_cop'].fillna(datos_casas['precio_cop'].mean())
if datos_casas['antiguedad'].isnull().sum() > 0:
    datos_casas['antiguedad'] = datos_casas['antiguedad'].fillna(datos_casas['antiguedad'].mean())

# 3- Codificar variables categóricas (barrio y estrato)
datos_preparados = pd.get_dummies(datos_casas, columns=["barrio", "estrato"])

# 4- Identificar y eliminar duplicados
datos_preparados = datos_preparados.drop_duplicates()
print("\nDatos después de eliminar duplicados:")
print(datos_preparados.head())

# 5- Convertir columnas de fechas a formato adecuado
datos_casas["fecha_construccion"] = pd.to_datetime(datos_casas["fecha_construccion"], errors='coerce')
print("\nTipo de dato de fecha_construccion:", datos_casas["fecha_construccion"].dtype)

# 6- Revision final con info() y describe()
print("\nInformacion general del dataset:")
print(datos_preparados.info())
print("\nEstadisticas descriptivas:")
print(datos_preparados.describe())