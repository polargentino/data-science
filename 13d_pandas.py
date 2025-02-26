import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Seleccionar las primeras tres filas de la columna 'Address'
print("Primeras tres filas de la columna 'Address':")
print(melbourne_data.iloc[:3, 0])
# Primeras tres filas de la columna 'Address':
# Suburb
# Abbotsford       85 Turner St
# Abbotsford    25 Bloomburg St
# Abbotsford       5 Charles St
# Name: Address, dtype: object

# Seleccionar la segunda y tercera fila de la columna 'Address'
print("\nSegunda y tercera fila de la columna 'Address':")
print(melbourne_data.iloc[1:3, 0])
# Segunda y tercera fila de la columna 'Address':
# Suburb
# Abbotsford    25 Bloomburg St
# Abbotsford       5 Charles St
# Name: Address, dtype: object


# Seleccionar filas 0, 1 y 2 de la columna 'Address'
print("\nFilas 0, 1 y 2 de la columna 'Address':")
print(melbourne_data.iloc[[0, 1, 2], 0])
# Filas 0, 1 y 2 de la columna 'Address':
# Suburb
# Abbotsford       85 Turner St
# Abbotsford    25 Bloomburg St
# Abbotsford       5 Charles St
# Name: Address, dtype: object

# Seleccionar las últimas cinco filas
print("\nÚltimas cinco filas:")
print(melbourne_data.iloc[-5:])
# Últimas cinco filas:
#                      Address  Rooms  ...                  Regionname  Propertycount
# Suburb                               ...                                           
# Wheelers Hill   12 Strada Cr      4  ...  South-Eastern Metropolitan         7392.0
# Williamstown   77 Merrett Dr      3  ...        Western Metropolitan         6380.0
# Williamstown     83 Power St      3  ...        Western Metropolitan         6380.0
# Williamstown    96 Verdon St      4  ...        Western Metropolitan         6380.0
# Yarraville        6 Agnes St      4  ...        Western Metropolitan         6543.0

# [5 rows x 20 columns]

#    * He sustituido todas las instancias de `reviews` por `melbourne_data` para reflejar tu DataFrame.
# 2.  **Reemplazo de `country` con `Address`:**
#     * He cambiado el ejemplo de la columna `country` a la columna `Address`, ya que es una columna de texto en tu conjunto de datos.
# 3.  **Ejemplos con `iloc`:**
#     * Los ejemplos `melbourne_data.iloc[:3, 0]`, `melbourne_data.iloc[1:3, 0]`, `melbourne_data.iloc[[0, 1, 2], 0]`, y `melbourne_data.iloc[-5:]` muestran cómo usar el operador `:` y listas con `iloc` para seleccionar filas y columnas por posición numérica.

# **Explicación Adicional:**

# * **`iloc[:3, 0]`:**
#     * Selecciona las primeras tres filas (`:3`) y la primera columna (`0`).
# * **`iloc[1:3, 0]`:**
#     * Selecciona las filas desde la segunda (índice 1) hasta la tercera (índice 2, sin incluir el 3) y la primera columna.
# * **`iloc[[0, 1, 2], 0]`:**
#     * Selecciona las filas con índices 0, 1 y 2 y la primera columna.
# * **`iloc[-5:]`:**
#     * Selecciona las últimas cinco filas del DataFrame.


print(melbourne_data.columns) # Ver todas las columnas
# Index(['Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date',
#        'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 'Landsize',
#        'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude',
#        'Regionname', 'Propertycount'],
#       dtype='object')

# Seleccionar filas 0, 1 y 2 de la columna 'Distance'
print("\nFilas 0, 1 y 2 de la columna 'Distance':")
print(melbourne_data.iloc[[0, 1, 2], 7])
# Filas 0, 1 y 2 de la columna 'Distance':
# Suburb
# Abbotsford    2.5
# Abbotsford    2.5
# Abbotsford    2.5
# Name: Distance, dtype: float64

# Convertir las columnas a una lista:
# Si prefieres tener los nombres de las columnas en una lista de Python, puedes convertir el objeto Index a una lista:
columnas = melbourne_data.columns.tolist()
print(columnas)
# ['Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount']

# Seleccionar el precio de una casa en Abbotsford
print("Precio de una casa en Abbotsford:")
print(melbourne_data.loc['Abbotsford', 'Price'])
# Precio de una casa en Abbotsford:
# Suburb
# Abbotsford    1480000.0
# Abbotsford    1035000.0
# Abbotsford    1465000.0
# Abbotsford     850000.0
# Abbotsford    1600000.0
# Abbotsford     941000.0
# Abbotsford    1876000.0
# Abbotsford    1636000.0
# Abbotsford     300000.0
# Abbotsford    1097000.0
# Abbotsford     700000.0
# Abbotsford    1350000.0
# Abbotsford     750000.0
# Abbotsford    1172500.0
# Abbotsford     441000.0
# Abbotsford    1310000.0
# Abbotsford    1200000.0
# Abbotsford    1176500.0
# Abbotsford     955000.0
# Abbotsford     890000.0
# Abbotsford    1330000.0
# Abbotsford     900000.0
# Abbotsford    1090000.0
# Abbotsford     500000.0
# Abbotsford    1100000.0
# Abbotsford    1315000.0
# Abbotsford     426000.0
# Abbotsford    1447500.0
# Abbotsford     457000.0
# Abbotsford    1135000.0
# Abbotsford    1542000.0
# Abbotsford    1290000.0
# Abbotsford    1290000.0
# Abbotsford     470000.0
# Abbotsford    1180000.0
# Abbotsford    1195000.0
# Abbotsford    1012500.0
# Abbotsford    1030000.0
# Abbotsford    1000000.0
# Abbotsford     870000.0
# Abbotsford    1050000.0
# Abbotsford    1242000.0
# Abbotsford    1165000.0
# Abbotsford     480000.0
# Abbotsford     750000.0
# Abbotsford     855000.0
# Abbotsford     505000.0
# Abbotsford    1402500.0
# Abbotsford     550000.0
# Abbotsford    1635000.0
# Abbotsford     940000.0
# Abbotsford    1375000.0
# Abbotsford    1525000.0
# Abbotsford     911000.0
# Abbotsford    1190000.0
# Abbotsford    1000000.0
# Name: Price, dtype: float64

# Seleccionar columnas 'Price', 'Rooms' y 'Bathroom'
print("\nColumnas 'Price', 'Rooms' y 'Bathroom':")
print(melbourne_data.loc[:, ['Price', 'Rooms', 'Bathroom']])
# Columnas 'Price', 'Rooms' y 'Bathroom':
#                    Price  Rooms  Bathroom
# Suburb                                   
# Abbotsford     1480000.0      2       1.0
# Abbotsford     1035000.0      2       1.0
# Abbotsford     1465000.0      3       2.0
# Abbotsford      850000.0      3       2.0
# Abbotsford     1600000.0      4       1.0
# ...                  ...    ...       ...
# Wheelers Hill  1245000.0      4       2.0
# Williamstown   1031000.0      3       2.0
# Williamstown   1170000.0      3       2.0
# Williamstown   2500000.0      4       1.0
# Yarraville     1285000.0      4       1.0

# [13580 rows x 3 columns]


# * He sustituido todas las instancias de `reviews` por `melbourne_data` para reflejar tu DataFrame.
# 2.  **Ejemplo con `melbourne_data.loc['Abbotsford', 'Price']`:**
#     * El ejemplo `melbourne_data.loc['Abbotsford', 'Price']` selecciona el valor en la fila con la etiqueta de índice 'Abbotsford' y la columna 'Price'.
# 3.  **Ejemplo con `melbourne_data.loc[:, ['Price', 'Rooms', 'Bathroom']]`:**
#     * El ejemplo `melbourne_data.loc[:, ['Price', 'Rooms', 'Bathroom']]` selecciona todas las filas (`:`) y las columnas 'Price', 'Rooms' y 'Bathroom'.

# **Explicación Adicional:**

# * **`loc`:**
#     * `loc` se utiliza para la selección basada en etiquetas (label-based indexing).
#     * `loc[fila, columna]` selecciona filas y columnas por sus etiquetas de índice.
#     * Es útil cuando deseas acceder a datos utilizando los nombres de las filas y columnas.
# * **Diferencia entre `loc` e `iloc`:**
#     * `iloc` utiliza la posición numérica (índices enteros).
#     * `loc` utiliza las etiquetas de índice (nombres de filas y columnas).
# * **Ventajas de `loc`:**
#     * `loc` es más intuitivo cuando trabajas con DataFrames que tienen índices significativos.
#     * Permite seleccionar filas y columnas utilizando sus nombres, lo que puede hacer que tu código sea más legible.
