import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from preprocesamiento import limpiar_datos, filtrar_medellin
from modelos import entrenar_modelo_supervisado, entrenar_modelo_no_supervisado
from evaluacion import calcular_rentabilidad, generar_graficos
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    print("=== SISTEMA DE RENTABILIDAD INMOBILIARIA MEDELLIN ===\n")
    
    # Cargar y preparar datos
    print("Cargando dataset...")
    df_limpio = limpiar_datos('../dataset_inmobiliario_valle_aburra.csv')
    df_medellin = filtrar_medellin(df_limpio)
    print(f"Dataset procesado: {len(df_medellin)} propiedades\n")
    
    # Entrenar modelos
    print("Entrenando modelos...")
    modelo_supervisado = entrenar_modelo_supervisado(df_medellin)
    modelo_no_supervisado, df_con_clusters = entrenar_modelo_no_supervisado(df_medellin)
    
    # Preparar datos para evaluacion
    features = ['tamaño_m2', 'antiguedad', 'zona', 'habitaciones']
    X = df_medellin[features]
    y = df_medellin['precio_cop']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Modelos entrenados exitosamente\n")
    
    # Solicitar datos al usuario
    print("Ingrese los datos de la propiedad:")
    try:
        tamaño_m2 = float(input("Tamaño en m2: "))
        antiguedad = int(input("Antiguedad en años: "))
        zona = int(input("Zona (1-3, donde 1=alta, 2=media, 3=popular): "))
        habitaciones = int(input("Numero de habitaciones: "))
        precio_actual = float(input("Precio actual (COP): "))
        años = int(input("A cuantos años proyectar (1-10): "))
        
        # Asignar tasa de crecimiento segun zona
        if zona == 1:  # El Poblado, Laureles
            tasa_anual = 0.10  # 10% (zonas premium crecen mas)
        elif zona == 2:  # Zona media
            tasa_anual = 0.08  # 8%
        else:  # zona == 3, zonas populares
            tasa_anual = 0.06  # 6%
        
        # Calcular precio futuro proyectado
        precio_futuro = precio_actual * (1 + tasa_anual) ** años
        
        # Calcular rentabilidad
        resultado = calcular_rentabilidad(precio_actual, precio_futuro)
        
        # Mostrar resultados
        print("\n" + "="*50)
        print("ANALISIS DE RENTABILIDAD")
        print("="*50)
        print(f"Precio actual:     ${precio_actual:,.0f} COP")
        print(f"Precio en {años} años:  ${precio_futuro:,.0f} COP")
        print(f"Tasa anual:        {tasa_anual*100:.0f}%")
        print(f"Rentabilidad total: {resultado['rentabilidad_pct']:.2f}%")
        print(f"Recomendacion:     {resultado['recomendacion']}")
        print("="*50)
        
        # Generar graficos y metricas
        print("\nGenerando graficos y metricas...")
        generar_graficos(df_con_clusters, modelo_supervisado, X_test, y_test)
        print("Graficos guardados: boxplot_rentabilidad.png, pca_rentabilidad.png")
        
    except ValueError:
        print("Error: Ingrese valores numericos validos")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario")

if __name__ == "__main__":
    main()