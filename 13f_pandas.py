import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Imprimir los nombres de las columnas
print("Nombres de las columnas:")
print(melbourne_data.columns)

# O convertir a una lista y luego imprimir
# print("Nombres de las columnas (como lista):")
# print(melbourne_data.columns.tolist())
# Nombres de las columnas:
# Index(['Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date',
#        'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 'Landsize',
#        'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude',
#        'Regionname', 'Propertycount'],
#       dtype='object')


# Usar CouncilArea
print("\nCasas en Yarra (CouncilArea):")
print(melbourne_data.loc[melbourne_data.CouncilArea == 'Yarra'].head())
# Casas en Yarra (CouncilArea):
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Usar Regionname
print("\nCasas en Northern Metropolitan (Regionname):")
print(melbourne_data.loc[melbourne_data.Regionname == 'Northern Metropolitan'].head())
# Casas en Northern Metropolitan (Regionname):
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Usar CouncilArea y Rooms
print("\nCasas en Yarra con más de 3 habitaciones:")
print(melbourne_data.loc[(melbourne_data.CouncilArea == 'Yarra') & (melbourne_data.Rooms > 3)].head())
# Casas en Yarra con más de 3 habitaciones:
#                        Address  Rooms  ...             Regionname  Propertycount
# Suburb                                 ...                                      
# Abbotsford         55a Park St      4  ...  Northern Metropolitan         4019.0
# Abbotsford     3/72 Charles St      4  ...  Northern Metropolitan         4019.0
# Abbotsford        31 Turner St      4  ...  Northern Metropolitan         4019.0
# Alphington      11 Margaret Gr      4  ...  Northern Metropolitan         2211.0
# Carlton North     112 Newry St      4  ...  Northern Metropolitan         3106.0

# [5 rows x 20 columns]

# Usar Regionname o Rooms
print("\nCasas en Northern Metropolitan o con más de 5 habitaciones:")
print(melbourne_data.loc[(melbourne_data.Regionname == 'Northern Metropolitan') | (melbourne_data.Rooms > 5)].head())
# Casas en Northern Metropolitan o con más de 5 habitaciones:
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Usar CouncilArea o Regionname con isin
print("\nCasas en Yarra o Moreland (CouncilArea):")
print(melbourne_data.loc[melbourne_data.CouncilArea.isin(['Yarra', 'Moreland'])].head())
# Casas en Yarra o Moreland (CouncilArea):
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Usar Landsize con notnull
print("\nCasas con Landsize no nulo:")
print(melbourne_data.loc[melbourne_data.Landsize.notnull()].head())
# Casas con Landsize no nulo:
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Explicación:

# print(melbourne_data.columns): Esta línea imprime el objeto Index que contiene los nombres de las columnas. Python automáticamente muestra la representación legible de este objeto.
# melbourne_data.columns.tolist(): Esta línea convierte el objeto Index a una lista de Python, lo que puede ser útil si quieres manipular los nombres de las columnas como una lista.


# Para encontrar los nombres como "Yarra" en tu DataFrame melbourne_data, necesitas explorar los valores únicos en las columnas CouncilArea y Regionname. Aquí te muestro cómo hacerlo:

# 1. Explorar los Valores Únicos en CouncilArea:

# Puedes usar el método .unique() para obtener una lista de todos los valores únicos en la columna CouncilArea.
council_areas = melbourne_data['CouncilArea'].unique()
print("Valores únicos en CouncilArea:")
print(council_areas)
# Valores únicos en CouncilArea:
# ['Yarra' 'Moonee Valley' 'Port Phillip' 'Darebin' 'Hobsons Bay'
#  'Stonnington' 'Boroondara' 'Monash' 'Glen Eira' 'Whitehorse'
#  'Maribyrnong' 'Bayside' 'Moreland' 'Manningham' 'Banyule' 'Melbourne'
#  'Kingston' 'Brimbank' 'Hume' nan 'Knox' 'Maroondah' 'Casey' 'Melton'
#  'Greater Dandenong' 'Nillumbik' 'Whittlesea' 'Frankston' 'Macedon Ranges'
#  'Yarra Ranges' 'Wyndham' 'Cardinia' 'Unavailable' 'Moorabool']


region_names = melbourne_data['Regionname'].unique()
print("\nValores únicos en Regionname:")
print(region_names)
# Valores únicos en Regionname:
# ['Northern Metropolitan' 'Western Metropolitan' 'Southern Metropolitan'
#  'Eastern Metropolitan' 'South-Eastern Metropolitan' 'Eastern Victoria'
#  'Northern Victoria' 'Western Victoria']

# Este código imprimirá una lista de todos los nombres de las regiones presentes en tu conjunto de datos.
# 3. Contar la Frecuencia de los Valores:

# Si quieres saber cuántas veces aparece cada valor en una columna, puedes usar el método .value_counts().
council_counts = melbourne_data['CouncilArea'].value_counts()
print("\nConteo de valores en CouncilArea:")
print(council_counts)
# Conteo de valores en CouncilArea:
# CouncilArea
# Moreland             1163
# Boroondara           1160
# Moonee Valley         997
# Darebin               934
# Glen Eira             848
# Stonnington           719
# Maribyrnong           692
# Yarra                 647
# Port Phillip          628
# Banyule               594
# Bayside               489
# Melbourne             470
# Hobsons Bay           434
# Brimbank              424
# Monash                333
# Manningham            311
# Whitehorse            304
# Kingston              207
# Whittlesea            167
# Hume                  164
# Wyndham                86
# Knox                   80
# Maroondah              80
# Melton                 66
# Frankston              53
# Greater Dandenong      52
# Casey                  38
# Nillumbik              36
# Yarra Ranges           18
# Cardinia                8
# Macedon Ranges          7
# Unavailable             1
# Moorabool               1
# Name: count, dtype: int64

region_counts = melbourne_data['Regionname'].value_counts()
print("\nConteo de valores en Regionname:")
print(region_counts)
# Conteo de valores en Regionname:
# Regionname
# Southern Metropolitan         4695
# Northern Metropolitan         3890
# Western Metropolitan          2948
# Eastern Metropolitan          1471
# South-Eastern Metropolitan     450
# Eastern Victoria                53
# Northern Victoria               41
# Western Victoria                32
# Name: count, dtype: int64
