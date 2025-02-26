import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Mostrar el DataFrame
print("DataFrame melbourne_data:")
print(melbourne_data)
# DataFrame melbourne_data:
#                         Address  Rooms  ...                  Regionname  Propertycount
# Suburb                                  ...                                           
# Abbotsford         85 Turner St      2  ...       Northern Metropolitan         4019.0
# Abbotsford      25 Bloomburg St      2  ...       Northern Metropolitan         4019.0
# Abbotsford         5 Charles St      3  ...       Northern Metropolitan         4019.0
# Abbotsford     40 Federation La      3  ...       Northern Metropolitan         4019.0
# Abbotsford          55a Park St      4  ...       Northern Metropolitan         4019.0
# ...                         ...    ...  ...                         ...            ...
# Wheelers Hill      12 Strada Cr      4  ...  South-Eastern Metropolitan         7392.0
# Williamstown      77 Merrett Dr      3  ...        Western Metropolitan         6380.0
# Williamstown        83 Power St      3  ...        Western Metropolitan         6380.0
# Williamstown       96 Verdon St      4  ...        Western Metropolitan         6380.0
# Yarraville           6 Agnes St      4  ...        Western Metropolitan         6543.0

# [13580 rows x 20 columns]

# Acceder a la columna 'Price' usando notación de atributo
print("\nmelbourne_data.Price:")
print(melbourne_data.Price)
# melbourne_data.Price:
# Suburb
# Abbotsford       1480000.0
# Abbotsford       1035000.0
# Abbotsford       1465000.0
# Abbotsford        850000.0
# Abbotsford       1600000.0
#                    ...    
# Wheelers Hill    1245000.0
# Williamstown     1031000.0
# Williamstown     1170000.0
# Williamstown     2500000.0
# Yarraville       1285000.0
# Name: Price, Length: 13580, dtype: float64

# Acceder a la columna 'Price' usando notación de indexación
print("\nmelbourne_data['Price']:")
print(melbourne_data['Price'])
# melbourne_data['Price']:
# Suburb
# Abbotsford       1480000.0
# Abbotsford       1035000.0
# Abbotsford       1465000.0
# Abbotsford        850000.0
# Abbotsford       1600000.0
#                    ...    
# Wheelers Hill    1245000.0
# Williamstown     1031000.0
# Williamstown     1170000.0
# Williamstown     2500000.0
# Yarraville       1285000.0
# Name: Price, Length: 13580, dtype: float64

# Acceder al primer valor de la columna 'Price'
print("\nmelbourne_data['Price'][0]:")
print(melbourne_data['Price'].iloc[0]) #use iloc to get the first element, as index is not numeric.
# melbourne_data['Price'][0]:
# 1480000.0

# Seleccionar la primera fila usando iloc
print("Primera fila de melbourne_data (usando iloc[0]):")
print(melbourne_data.iloc[0])
# Primera fila de melbourne_data (usando iloc[0]):
# Address                   85 Turner St
# Rooms                                2
# Type                                 h
# Price                        1480000.0
# Method                               S
# SellerG                         Biggin
# Date                         3/12/2016
# Distance                           2.5
# Postcode                        3067.0
# Bedroom2                           2.0
# Bathroom                           1.0
# Car                                1.0
# Landsize                         202.0
# BuildingArea                       NaN
# YearBuilt                          NaN
# CouncilArea                      Yarra
# Lattitude                     -37.7996
# Longtitude                    144.9984
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, dtype: object

print("Segunda fila de melbourne_data (usando iloc[1]):")
print(melbourne_data.iloc[1])
# Segunda fila de melbourne_data (usando iloc[1]):
# Address                25 Bloomburg St
# Rooms                                2
# Type                                 h
# Price                        1035000.0
# Method                               S
# SellerG                         Biggin
# Date                         4/02/2016
# Distance                           2.5
# Postcode                        3067.0
# Bedroom2                           2.0
# Bathroom                           1.0
# Car                                0.0
# Landsize                         156.0
# BuildingArea                      79.0
# YearBuilt                       1900.0
# CouncilArea                      Yarra
# Lattitude                     -37.8079
# Longtitude                    144.9934
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, dtype: object

# 3. Mostrar las primeras filas del DataFrame
print("\nPrimeras filas del DataFrame:")
print(melbourne_data.head())
# Este print muestra las primeras 5 filas del DataFrame.
# Primeras filas del DataFrame:
#        Suburb           Address  Rooms  ... Longtitude             Regionname Propertycount
# 0  Abbotsford      85 Turner St      2  ...   144.9984  Northern Metropolitan        4019.0
# 1  Abbotsford   25 Bloomburg St      2  ...   144.9934  Northern Metropolitan        4019.0
# 2  Abbotsford      5 Charles St      3  ...   144.9944  Northern Metropolitan        4019.0
# 3  Abbotsford  40 Federation La      3  ...   144.9969  Northern Metropolitan        4019.0
# 4  Abbotsford       55a Park St      4  ...   144.9941  Northern Metropolitan        4019.0
print(melbourne_data.iloc[2])
# Address                   5 Charles St
# Rooms                                3
# Type                                 h
# Price                        1465000.0
# Method                              SP
# SellerG                         Biggin
# Date                         4/03/2017
# Distance                           2.5
# Postcode                        3067.0
# Bedroom2                           3.0
# Bathroom                           2.0
# Car                                0.0
# Landsize                         134.0
# BuildingArea                     150.0
# YearBuilt                       1900.0
# CouncilArea                      Yarra
# Lattitude                     -37.8093
# Longtitude                    144.9944
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, dtype: object

# Seleccionar la primera columna usando iloc
print("Primera columna de melbourne_data (usando iloc[:, 0]):")
print(melbourne_data.iloc[:, 0])
# Primera columna de melbourne_data (usando iloc[:, 0]):
# Suburb
# Abbotsford           85 Turner St
# Abbotsford        25 Bloomburg St
# Abbotsford           5 Charles St
# Abbotsford       40 Federation La
# Abbotsford            55a Park St
#                        ...       
# Wheelers Hill        12 Strada Cr
# Williamstown        77 Merrett Dr
# Williamstown          83 Power St
# Williamstown         96 Verdon St
# Yarraville             6 Agnes St
# Name: Address, Length: 13580, dtype: object

#     * He sustituido todas las instancias de `reviews` por `melbourne_data` para reflejar tu DataFrame.
# 2.  **Ejemplo con `melbourne_data.iloc[:, 0]`:**
#     * El ejemplo `melbourne_data.iloc[:, 0]` selecciona la primera columna del DataFrame `melbourne_data` utilizando la posición numérica (índice 0).

# **Explicación Adicional:**

# * **`iloc[:, 0]`:**
#     * El primer argumento (`:`) selecciona todas las filas.
#     * El segundo argumento (`0`) selecciona la primera columna (posición 0).
#     * Por lo tanto, `iloc[:, 0]` devuelve una Serie que contiene todos los valores de la primera columna.
# * **Diferencia con Python Nativo:**
#     * En Python nativo (por ejemplo, con listas anidadas), accedemos a los elementos primero por columna y luego por fila.
#     * En pandas, con `loc` e `iloc`, es al revés: primero fila, luego columna.
# * **Recuperación de Columnas:**
#    * Aunque es ligeramente más difícil, `iloc` permite recuperar columnas especificando el índice de la columna.


