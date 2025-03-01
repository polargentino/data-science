import pandas as pd

# Especifica la ruta del archivo CSV
ufo_file_path = '/home/pol/Downloads/ufo_sightings_scrubbed.csv'
# Explicación de los Cambios:

# ufo_file_path:
# Se ha actualizado la ruta del archivo a /home/pol/Downloads/ufo_sightings_scrubbed.csv.


# Carga los datos en un DataFrame de pandas con tipos especificados y low_memory=False
ufo_data = pd.read_csv(ufo_file_path, dtype={'latitude': str, 'duration (seconds)': str}, low_memory=False)
# ufo_data:
# Se ha especificado dtype={'latitude': str, 'duration (seconds)': str} y low_memory=False al cargar los datos para manejar los tipos de datos mixtos y evitar el DtypeWarning.

# Imprimir información general sobre el DataFrame
print("Información general del DataFrame:")
print(ufo_data.info())
print("\n")
# Información general del DataFrame:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 80332 entries, 0 to 80331
# Data columns (total 11 columns):
 #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   datetime              80332 non-null  object 
#  1   city                  80332 non-null  object 
#  2   state                 74535 non-null  object 
#  3   country               70662 non-null  object 
#  4   shape                 78400 non-null  object 
#  5   duration (seconds)    80332 non-null  object 
#  6   duration (hours/min)  80332 non-null  object 
#  7   comments              80317 non-null  object 
#  8   date posted           80332 non-null  object 
#  9   latitude              80332 non-null  object 
#  10  longitude             80332 non-null  float64
# dtypes: float64(1), object(10)
# memory usage: 6.7+ MB
# None




# Imprime las primeras 5 filas para visualizar una muestra del dataset
print("Primeras 5 filas del dataset:")
print(ufo_data.head())
print("\n")
# Primeras 5 filas del dataset:
#               datetime                  city state  ... date posted    latitude  longitude 
# 0  1949-10-10 20:30:00            san marcos    tx  ...  2004-04-27  29.8830556  -97.941111
# 1  1949-10-10 21:00:00          lackland afb    tx  ...  2005-12-16    29.38421  -98.581082
# 2  1955-10-10 17:00:00  chester (uk/england)   NaN  ...  2008-01-21        53.2   -2.916667
# 3  1956-10-10 21:00:00                  edna    tx  ...  2004-01-17  28.9783333  -96.645833
# 4  1960-10-10 20:00:00               kaneohe    hi  ...  2004-01-22  21.4180556 -157.803611

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
print("Estadísticas descriptivas de las columnas numéricas:")
print(ufo_data.describe())
print("\n")
#Estadísticas descriptivas de las columnas numéricas:
#          longitude 
# count  80332.000000
# mean     -86.772885
# std       39.697205
# min     -176.658056
# 25%     -112.073333
# 50%      -87.903611
# 75%      -78.755000
# max      178.441900

# ufo_data.describe():
# Imprime estadísticas descriptivas de las columnas numéricas.
# Ten en cuenta que, debido a que algunas columnas numéricas se 
# cargaron como cadenas, es posible que no se muestren estadísticas
# para todas las columnas numéricas esperadas.


# Imprimir los valores únicos de la columna 'shape'
print("Valores únicos en la columna 'shape':")
print(ufo_data['shape'].unique())
print("\n")
# Valores únicos en la columna 'shape':
# ['cylinder' 'light' 'circle' 'sphere' 'disk' 'fireball' 'unknown' 'oval'
#  'other' 'cigar' 'rectangle' 'chevron' 'triangle' 'formation' nan 'delta'
#  'changing' 'egg' 'diamond' 'flash' 'teardrop' 'cone' 'cross' 'pyramid'
#  'round' 'crescent' 'flare' 'hexagon' 'dome' 'changed']

# ufo_data['shape'].unique():
# Se ha cambiado a la columna shape para imprimir los
# valores únicos, ya que es una columna categórica relevante
# en este conjunto de datos.