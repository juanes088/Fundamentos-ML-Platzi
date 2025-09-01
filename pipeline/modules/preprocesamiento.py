import pandas as pd

def limpiar_datos(ruta_csv):
    """
    Carga el dataset y filtra outliers en precio_cop usando cuantiles 5% y 95%
    """
    df = pd.read_csv(ruta_csv)
    q5 = df['precio_cop'].quantile(0.05)
    q95 = df['precio_cop'].quantile(0.95)
    df_limpio = df[(df['precio_cop'] >= q5) & (df['precio_cop'] <= q95)]
    return df_limpio

def filtrar_medellin(df):
    """
    Filtra solo barrios de Medellin y asigna zona basada en clasificacion
    """
    barrios_medellin = [
        'Alcala', 'Alejandria', 'Alto Bonito', 'Alto de Calasanz', 'Alto de Las Palmas',
        'Ancon Sur', 'Andalucia', 'Aranjuez', 'Asturias', 'Belen', 'Bellavista',
        'Betania', 'Buenos Aires', 'Caicedo', 'Calatrava', 'Camino Verde',
        'Campo Valdes No 1', 'Canaveralejo', 'Carlos E Restrepo', 'Castropol',
        'Centro', 'Cerro Verde', 'Chaparral', 'Club Campestre', 'Conquistadores',
        'Cordoba', 'Cristo Rey', 'Ditaires', 'El Carmelo', 'El Chingui',
        'El Convento', 'El Corazon', 'El Crucero', 'El Dorado', 'El Mirador',
        'El Pedregal', 'El Poblado', 'El Portal', 'El Progreso', 'El Raizal',
        'El Ramal', 'El Rio', 'El Rodeo', 'El Rosario', 'El Tabor', 'El Tesoro',
        'El Velodromo', 'Estadio', 'Fontidueno', 'Girardota', 'Granizal',
        'Granjas de Te', 'Guayabal', 'Holanda', 'Jardin', 'La America',
        'La Cabanita', 'La Campina', 'La Candelaria', 'La Castellana', 'La Chinca',
        'La Cruz', 'La Cumbre', 'La Doctora', 'La Doctora Alta', 'La Estrella',
        'La Ferreria', 'La Floresta', 'La Florida', 'La Gabriela', 'La Inmaculada',
        'La Madera', 'La Magnolia', 'La Misericordia', 'La Piedra', 'La Quiebra',
        'La Selva', 'La Tablaza', 'La Valeria', 'La Ye', 'Las Antillas',
        'Las Casitas', 'Laureles', 'Loma Linda', 'Loma del Escobero',
        'Loma del Viento', 'Los Alamos', 'Los Balsos', 'Los Colegios',
        'Los Colores', 'Los Naranjos', 'Machado', 'Manila', 'Manrique Central',
        'Mayorca', 'Mesa', 'Montecarlo', 'Moscu No 2', 'Niquia', 'Nueva Jerusalén',
        'Olivares', 'Paris', 'Perez', 'Popular', 'Prado', 'Primavera',
        'Quinta Parro', 'Salento', 'San Andres', 'San Antonio', 'San Fernando',
        'San Isidro', 'San Jose', 'San Pio', 'Santa Ana', 'Santa Catalina',
        'Santa Cruz', 'Santa Marta', 'Santamaria', 'Senorial', 'Serramonte',
        'Simon Bolivar', 'Suarez', 'Suramericana', 'Villa Carlota', 'Villa Elena',
        'Villa Guadalupe', 'Villa Hermosa', 'Villa Nueva', 'Villa Tina',
        'Villa del Socorro', 'Yarumito', 'Zuniga'
    ]
    
    # Clasificacion por zonas (1: alta, 2: media, 3: popular)
    zona_1 = ['El Poblado', 'Laureles', 'Castropol', 'Los Balsos', 'El Tesoro', 
              'Club Campestre', 'Alto de Las Palmas', 'La Castellana']
    zona_2 = ['Belen', 'La America', 'Estadio', 'Aranjuez', 'Buenos Aires',
              'Guayabal', 'Centro', 'La Candelaria', 'Conquistadores']
    
    df_filtrado = df[df['barrio'].isin(barrios_medellin)].copy()
    
    def asignar_zona(barrio):
        if barrio in zona_1:
            return 1
        elif barrio in zona_2:
            return 2
        else:
            return 3
    
    df_filtrado['zona'] = df_filtrado['barrio'].apply(asignar_zona)
    
    return df_filtrado