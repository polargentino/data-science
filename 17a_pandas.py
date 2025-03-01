import pandas as pd

# Especifica la ruta del archivo CSV
ufo_file_path = '/home/pol/Downloads/ufo_sightings_scrubbed.csv'

# Carga los datos en un DataFrame de pandas con tipos especificados y low_memory=False
ufo_data = pd.read_csv(ufo_file_path, dtype={'latitude': str, 'duration (seconds)': str}, low_memory=False)

# 1. Limpieza de 'latitude'
# Convertir a numérico y manejar errores
ufo_data['latitude'] = pd.to_numeric(ufo_data['latitude'], errors='coerce')
# Convertir a float64
ufo_data['latitude'] = ufo_data['latitude'].astype('float64')

# 2. Limpieza de 'duration (seconds)'
# Convertir a numérico y manejar errores
ufo_data['duration (seconds)'] = pd.to_numeric(ufo_data['duration (seconds)'], errors='coerce')
# Convertir a float64
ufo_data['duration (seconds)'] = ufo_data['duration (seconds)'].astype('float64')

# 3. Manejo de valores nulos en 'shape'
# Rellenar con 'unknown'
ufo_data['shape'] = ufo_data['shape'].fillna('unknown')

# 4. Manejo de valores nulos en 'country'
# Rellenar con 'unknown'
ufo_data['country'] = ufo_data['country'].fillna('unknown')

# 5. Manejo de valores nulos en 'state'
# Rellenar con 'unknown'
ufo_data['state'] = ufo_data['state'].fillna('unknown')

# 6. Manejo de valores nulos en 'comments'
# Rellenar con 'No comments'
ufo_data['comments'] = ufo_data['comments'].fillna('No comments')

# Imprimir información general sobre el DataFrame
print("Información general del DataFrame (después de la limpieza):")
print(ufo_data.info())
print("\n")
# Información general del DataFrame (después de la limpieza):
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 80332 entries, 0 to 80331
# Data columns (total 11 columns):
 #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   datetime              80332 non-null  object 
#  1   city                  80332 non-null  object 
#  2   state                 80332 non-null  object 
#  3   country               80332 non-null  object 
#  4   shape                 80332 non-null  object 
#  5   duration (seconds)    80329 non-null  float64
#  6   duration (hours/min)  80332 non-null  object 
#  7   comments              80332 non-null  object 
#  8   date posted           80332 non-null  object 
#  9   latitude              80331 non-null  float64
#  10  longitude             80332 non-null  float64
# dtypes: float64(3), object(8)
# memory usage: 6.7+ MB
# None

# Imprime las primeras 5 filas para visualizar una muestra del dataset
print("Primeras 5 filas del dataset (después de la limpieza):")
print(ufo_data.head())
print("\n")
# Primeras 5 filas del dataset (después de la limpieza):
#               datetime                  city    state  ... date posted   latitude  longitude 
# 0  1949-10-10 20:30:00            san marcos       tx  ...  2004-04-27  29.883056  -97.941111
# 1  1949-10-10 21:00:00          lackland afb       tx  ...  2005-12-16  29.384210  -98.581082
# 2  1955-10-10 17:00:00  chester (uk/england)  unknown  ...  2008-01-21  53.200000   -2.916667
# 3  1956-10-10 21:00:00                  edna       tx  ...  2004-01-17  28.978333  -96.645833
# 4  1960-10-10 20:00:00               kaneohe       hi  ...  2004-01-22  21.418056 -157.803611

# [5 rows x 11 columns]

# Imprimir los nombres de las columnas
print("Nombres de las columnas:")
print(ufo_data.columns)
print("\n")
# Nombres de las columnas:
# Index(['datetime', 'city', 'state', 'country', 'shape', 'duration (seconds)',
#        'duration (hours/min)', 'comments', 'date posted', 'latitude',
#        'longitude '],
#       dtype='object')

# Imprimir estadísticas descriptivas de las columnas numéricas
print("Estadísticas descriptivas de las columnas numéricas (después de la limpieza):")
print(ufo_data.describe())
print("\n")
# Estadísticas descriptivas de las columnas numéricas (después de la limpieza):
#        duration (seconds)      latitude    longitude 
# count        8.032900e+04  80331.000000  80332.000000
# mean         9.017226e+03     38.124477    -86.772885
# std          6.202284e+05     10.469636     39.697205
# min          1.000000e-03    -82.862752   -176.658056
# 25%          3.000000e+01     34.134722   -112.073333
# 50%          1.800000e+02     39.411111    -87.903611
# 75%          6.000000e+02     42.788333    -78.755000
# max          9.783600e+07     72.700000    178.441900


# Imprimir los valores únicos de la columna 'shape'
print("Valores únicos en la columna 'shape' (después de la limpieza):")
print(ufo_data['shape'].unique())
print("\n")
# Valores únicos en la columna 'shape' (después de la limpieza):
# ['cylinder' 'light' 'circle' 'sphere' 'disk' 'fireball' 'unknown' 'oval'
#  'other' 'cigar' 'rectangle' 'chevron' 'triangle' 'formation' 'delta'
#  'changing' 'egg' 'diamond' 'flash' 'teardrop' 'cone' 'cross' 'pyramid'
#  'round' 'crescent' 'flare' 'hexagon' 'dome' 'changed']