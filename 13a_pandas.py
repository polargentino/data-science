import pandas as pd

# 1. Cargar los datos desde tu archivo CSV
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'  # Ruta al archivo CSV
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0) # Index_col=0, usa la primer columna como index.

# 2. Configurar opciones de visualización (opcional)
pd.set_option('display.max_rows', 5)  # Mostrar solo 5 filas para evitar salidas largas

# 3. Mostrar las primeras filas del DataFrame (para verificar la carga)
print("Primeras filas del DataFrame:")
print(melbourne_data.head()) # Salidas:
# Primeras filas del DataFrame:
#                      Address  Rooms Type  ...  Longtitude             Regionname Propertycount
# Suburb                                    ...                                                 
# Abbotsford      85 Turner St      2    h  ...    144.9984  Northern Metropolitan        4019.0
# Abbotsford   25 Bloomburg St      2    h  ...    144.9934  Northern Metropolitan        4019.0
# Abbotsford      5 Charles St      3    h  ...    144.9944  Northern Metropolitan        4019.0
# Abbotsford  40 Federation La      3    h  ...    144.9969  Northern Metropolitan        4019.0
# Abbotsford       55a Park St      4    h  ...    144.9941  Northern Metropolitan        4019.0

# [5 rows x 20 columns]

# 4. Ejemplos de selección de datos (adaptados a melbourne_data)

# Seleccionar una columna específica
print("\nColumna 'Price':")
print(melbourne_data['Price']) # Salidas:
# Columna 'Price':
# Suburb
# Abbotsford      1480000.0
# Abbotsford      1035000.0
#                   ...    
# Williamstown    2500000.0
# Yarraville      1285000.0
# Name: Price, Length: 13580, dtype: float64

# Seleccionar una fila específica por índice
# print("\nFila con índice 1:")
# print(melbourne_data.loc[1]) # Salidas:

print(melbourne_data.index) # Salidas:
# Index(['Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford',
#        'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford',
#        ...
#        'Wantirna South', 'Wantirna South', 'Watsonia', 'Werribee',
#        'Westmeadows', 'Wheelers Hill', 'Williamstown', 'Williamstown',
#        'Williamstown', 'Yarraville'],
#       dtype='object', name='Suburb', length=13580)

# Perfecto, ahora entiendo completamente el problema. Como puedes ver en la salida de melbourne_data.index, los índices de tu DataFrame son los nombres de los suburbios (ej. 'Abbotsford', 'Wantirna South', etc.), y no números secuenciales. Por lo tanto, melbourne_data.loc[1] no funciona porque no hay una fila con la etiqueta de índice 1.

# Solución y Explicación:

# Usar loc con Nombres de Suburbios:

# Para acceder a una fila específica, debes usar el nombre del suburbio como etiqueta. Por ejemplo:

print(melbourne_data.loc['Abbotsford']) # Salidas:
#  Address  Rooms Type  ...  Longtitude             Regionname Propertycount
# Suburb                                   ...                                                 
# Abbotsford     85 Turner St      2    h  ...   144.99840  Northern Metropolitan        4019.0
# Abbotsford  25 Bloomburg St      2    h  ...   144.99340  Northern Metropolitan        4019.0
# ...                     ...    ...  ...  ...         ...                    ...           ...
# Abbotsford     133 Yarra St      2    h  ...   145.00010  Northern Metropolitan        4019.0
# Abbotsford   67 Stafford St      3    h  ...   144.99569  Northern Metropolitan        4019.0

# [56 rows x 20 columns]

# Si quieres acceder a la primera fila de suburbio abbotsford, entonces puedes usar:
print(melbourne_data.loc['Abbotsford'].iloc[0]) # Salidas:
# Address                   85 Turner St
# Rooms                                2
#                          ...          
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, Length: 20, dtype: object

print(melbourne_data.iloc[1])