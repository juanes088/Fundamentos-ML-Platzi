from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline

def entrenar_modelo_supervisado(df):
    """
    Entrena un modelo Ridge con pipeline StandardScaler
    """
    features = ['tamaño_m2', 'antiguedad', 'zona', 'habitaciones']
    X = df[features]
    y = df['precio_cop']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('ridge', Ridge(alpha=1.0))
    ])
    
    pipeline.fit(X_train, y_train)
    
    return pipeline

def entrenar_modelo_no_supervisado(df):
    """
    Entrena un modelo KMeans con pipeline StandardScaler
    """
    features = ['tamaño_m2', 'antiguedad', 'zona', 'habitaciones']
    X = df[features]
    
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=3, random_state=42))
    ])
    
    clusters = pipeline.fit_predict(X)
    df_con_clusters = df.copy()
    df_con_clusters['cluster'] = clusters
    
    return pipeline, df_con_clusters