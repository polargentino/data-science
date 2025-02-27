import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Ahora puedes usar melbourne_data en lugar de reviews
# 1. Imprimir las primeras 5 filas del DataFrame
print("Primeras 5 filas:")
print(melbourne_data.head())
# Primeras 5 filas:
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# 2. Imprimir información general del DataFrame
print("\nInformación general del DataFrame:")
print(melbourne_data.info())
# Información general del DataFrame:
# <class 'pandas.core.frame.DataFrame'>
# Index: 13580 entries, Abbotsford to Yarraville
# Data columns (total 20 columns):
 #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Address        13580 non-null  object 
#  1   Rooms          13580 non-null  int64  
#  2   Type           13580 non-null  object 
#  3   Price          13580 non-null  float64
#  4   Method         13580 non-null  object 
#  5   SellerG        13580 non-null  object 
#  6   Date           13580 non-null  object 
#  7   Distance       13580 non-null  float64
#  8   Postcode       13580 non-null  float64
#  9   Bedroom2       13580 non-null  float64
#  10  Bathroom       13580 non-null  float64
#  11  Car            13518 non-null  float64
#  12  Landsize       13580 non-null  float64
#  13  BuildingArea   7130 non-null   float64
#  14  YearBuilt      8205 non-null   float64
#  15  CouncilArea    12211 non-null  object 
#  16  Lattitude      13580 non-null  float64
#  17  Longtitude     13580 non-null  float64
#  18  Regionname     13580 non-null  object 
#  19  Propertycount  13580 non-null  float64
# dtypes: float64(12), int64(1), object(7)
# memory usage: 2.2+ MB
# None

# 3. Imprimir estadísticas descriptivas de las columnas numéricas
print("\nEstadísticas descriptivas:")
print(melbourne_data.describe())
# Estadísticas descriptivas:
#               Rooms         Price      Distance  ...     Lattitude    Longtitude  Propertycount
# count  13580.000000  1.358000e+04  13580.000000  ...  13580.000000  13580.000000   13580.000000
# mean       2.937997  1.075684e+06     10.137776  ...    -37.809203    144.995216    7454.417378
# ...             ...           ...           ...  ...           ...           ...            ...
# 75%        3.000000  1.330000e+06     13.000000  ...    -37.756400    145.058305   10331.000000
# max       10.000000  9.000000e+06     48.100000  ...    -37.408530    145.526350   21650.000000

# [8 rows x 13 columns]

# 4. Imprimir los nombres de las columnas
print("\nNombres de las columnas:")
print(melbourne_data.columns)
# Nombres de las columnas:
# Index(['Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date',
#        'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 'Landsize',
#        'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude',
#        'Regionname', 'Propertycount'],
#       dtype='object')


# 5. Imprimir los valores únicos de la columna 'CouncilArea'
print("\nValores únicos en CouncilArea:")
print(melbourne_data['CouncilArea'].unique())
# Valores únicos en CouncilArea:
# ['Yarra' 'Moonee Valley' 'Port Phillip' 'Darebin' 'Hobsons Bay'
#  'Stonnington' 'Boroondara' 'Monash' 'Glen Eira' 'Whitehorse'
#  'Maribyrnong' 'Bayside' 'Moreland' 'Manningham' 'Banyule' 'Melbourne'
#  'Kingston' 'Brimbank' 'Hume' nan 'Knox' 'Maroondah' 'Casey' 'Melton'
#  'Greater Dandenong' 'Nillumbik' 'Whittlesea' 'Frankston' 'Macedon Ranges'
#  'Yarra Ranges' 'Wyndham' 'Cardinia' 'Unavailable' 'Moorabool']

# 6. Imprimir una columna específica (ejemplo: 'Price')
print("\nColumna 'Price':")
print(melbourne_data['Price'])
# Columna 'Price':
# Suburb
# Abbotsford      1480000.0
# Abbotsford      1035000.0
#                   ...    
# Williamstown    2500000.0
# Yarraville      1285000.0
# Name: Price, Length: 13580, dtype: float64

# 7. Imprimir una fila específica por etiqueta de índice (ejemplo: 'Abbotsford')
print("\nFila con etiqueta de índice 'Abbotsford':")
print(melbourne_data.loc['Abbotsford'].iloc[0]) #imprime la primera fila de abbotsford.
# Fila con etiqueta de índice 'Abbotsford':
# Address                   85 Turner St
# Rooms                                2
#                          ...          
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, Length: 20, dtype: object


# 8. Imprimir un valor específico (ejemplo: Price de la primera fila)
print("\nPrecio de la primera fila:")
print(melbourne_data['Price'].iloc[0])
# Precio de la primera fila:
# 1480000.0


# Explicación de los Casos de NumPy:

# np.mean(melbourne_data['Price']): Calcula la media de la columna 'Price' usando NumPy.
# np.std(melbourne_data['Price']): Calcula la desviación estándar de la columna 'Price' usando NumPy.
# np.max(melbourne_data['Rooms']) y np.min(melbourne_data['Rooms']): Calcula el máximo y mínimo de la columna 'Rooms' usando NumPy.
# np.sum(melbourne_data['Landsize']): Calcula la suma total de los valores en la columna 'Landsize' usando NumPy.
# np.percentile(melbourne_data['Price'], 75): Calcula el percentil 75 de la columna 'Price' usando NumPy.
# np.sqrt(melbourne_data['Landsize'].iloc[0:5]): Calcula la raíz cuadrada de los primeros 5 valores en la columna 'Landsize' usando NumPy.
# np.log(melbourne_data['Price'].iloc[0:5]): Calcula el logaritmo de los primeros 5 valores en la columna 'Price' usando NumPy.
# Estos ejemplos muestran cómo puedes usar NumPy para realizar cálculos numéricos en tus datos de Pandas de manera eficiente.

 # 9. Calcular la media de 'Price' usando NumPy
print("\nMedia de 'Price' (NumPy):")
print(np.mean(melbourne_data['Price']))
# Media de 'Price' (NumPy):
# 1075684.079455081

# 10. Calcular la desviación estándar de 'Price' usando NumPy
print("\nDesviación estándar de 'Price' (NumPy):")
print(np.std(melbourne_data['Price']))
# Desviación estándar de 'Price' (NumPy):
# 639287.1851762069

# 11. Calcular el máximo y mínimo de 'Rooms' usando NumPy
print("\nMáximo número de Rooms (NumPy):")
print(np.max(melbourne_data['Rooms']))
print("\nMinimo numero de Rooms (Numpy):")
print(np.min(melbourne_data['Rooms']))
# Máximo número de Rooms (NumPy):
# 10

# Minimo numero de Rooms (Numpy):
# 1

# 12. Calcular la suma de 'Landsize' usando NumPy
print("\nSuma total de Landsize (NumPy):")
print(np.sum(melbourne_data['Landsize']))
# Suma total de Landsize (NumPy):
# 7583291.0

# 13. Calcular el percentil 75 de 'Price' usando NumPy
print("\nPercentil 75 de 'Price' (NumPy):")
print(np.percentile(melbourne_data['Price'], 75))
# Percentil 75 de 'Price' (NumPy):
# 1330000.0

# 14. Calcular la raíz cuadrada de 'Landsize' usando NumPy
print("\nRaíz cuadrada de 'Landsize' (NumPy):")
print(np.sqrt(melbourne_data['Landsize'].iloc[0:5])) #solo las primeras 5 para no llenar de datos la consola
# Raíz cuadrada de 'Landsize' (NumPy):
# Suburb
# Abbotsford    14.212670
# Abbotsford    12.489996
# Abbotsford    11.575837
# Abbotsford     9.695360
# Abbotsford    10.954451
# Name: Landsize, dtype: float64

# 15. Calcular el logaritmo de 'Price' usando NumPy
print("\nLogaritmo de 'Price' (NumPy):")
print(np.log(melbourne_data['Price'].iloc[0:5])) #solo las primeras 5 para no llenar de datos la consola.        
# Logaritmo de 'Price' (NumPy):
# Suburb
# Abbotsford    14.207553
# Abbotsford    13.849912
# Abbotsford    14.197366
# Abbotsford    13.652992
# Abbotsford    14.285514
# Name: Price, dtype: float64

