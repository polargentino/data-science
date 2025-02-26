import pandas as pd

# Creando datos
# Hay dos objetos principales en pandas: el DataFrame y la Serie.
# DataFrame
# Un DataFrame es una tabla. Contiene un arreglo de entradas individuales, cada una de las cuales tiene un cierto valor.
# Cada entrada corresponde a una fila (o registro) y una columna.
# Por ejemplo, considera el siguiente DataFrame simple:

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})) # Salida:
#    Yes   No
# 0   50  131
# 1   21    2

# Explicación:

# import pandas as pd:
# Esta línea importa la librería pandas y la asigna al alias pd. Esto nos permite utilizar las funciones de pandas escribiendo pd en lugar de pandas.
# "Creando datos":
# Esta sección introduce la creación de datos en pandas.
# "Hay dos objetos principales en pandas: el DataFrame y la Serie.":
# pandas utiliza dos estructuras de datos fundamentales:
# DataFrame: Una tabla bidimensional, similar a una hoja de cálculo o una tabla SQL.
# Serie: Una matriz unidimensional etiquetada, similar a una columna en un DataFrame.
# "DataFrame":
# Se explica que un DataFrame es una tabla.
# "Un DataFrame es una tabla. Contiene un arreglo de entradas individuales, cada una de las cuales tiene un cierto valor. Cada entrada corresponde a una fila (o registro) y una1 columna.":
# Esta es una descripción detallada de la estructura de un DataFrame:
# Es una colección de datos organizados en filas y columnas.
# Cada celda en la tabla contiene un valor.
# Las filas representan registros individuales, y las columnas representan diferentes variables o características.



print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})) # Salida:

#              Bob           Sue
# 0    I liked it.  Pretty good.
# 1  It was awful.        Bland.

# **Explicación:**

# 1.  **"En este ejemplo, la entrada '0, No' tiene el valor de 131. La entrada '0, Yes' tiene un valor de 50, y así sucesivamente."**:
#     * Esto se refiere al DataFrame creado en el ejemplo anterior. Explica cómo interpretar las entradas en la tabla:
#         * El índice de la fila (0, 1, etc.) se combina con el nombre de la columna ('Yes', 'No') para identificar una entrada específica.
#         * Por ejemplo, '0, No' se refiere a la entrada en la primera fila (índice 0) y la columna 'No', que tiene el valor 131.
# 2.  **"Las entradas de DataFrame no se limitan a enteros. Por ejemplo, aquí hay un DataFrame cuyos valores son cadenas de texto:"**:
#     * Este punto clave resalta la flexibilidad de los DataFrames. Pueden contener datos de diferentes tipos, no solo números enteros.
#     * El siguiente ejemplo muestra un DataFrame donde los valores son cadenas de texto (strings).
# 3.  **`pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})`**:
#     * Esta línea de código crea otro DataFrame, esta vez con datos de texto.
#     * El diccionario define dos columnas: 'Bob' y 'Sue'.
#     * Los valores en cada columna son listas de cadenas de texto, representando opiniones o comentarios.
#     * Si lo quisieramos ver, deberiamos agregar la funcion print() alrededor de la sentencia:

print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])) # Salidas:
#                      Bob           Sue
# Product A    I liked it.  Pretty good.
# Product B  It was awful.        Bland.



# **Explicación:**

# 1.  **"Estamos utilizando el constructor `pd.DataFrame()` para generar estos objetos DataFrame. La sintaxis para declarar uno nuevo es un diccionario cuyas claves son los nombres de las columnas (Bob y Sue en este ejemplo), y cuyos valores son una lista de entradas. Esta es la forma estándar de construir un nuevo DataFrame, y la que es más probable que encuentres."**:
#     * Se explica que `pd.DataFrame()` es la función que se usa para crear DataFrames.
#     * Se detalla la sintaxis: un diccionario donde las claves son los nombres de las columnas y los valores son listas que contienen los datos de cada columna.
#     * Se enfatiza que esta es la forma más común de crear DataFrames.
# 2.  **"El constructor de diccionario-lista asigna valores a las etiquetas de columna, pero simplemente utiliza un conteo ascendente desde 0 (0, 1, 2, 3, ...) para las etiquetas de fila. A veces esto está bien, pero a menudo querremos asignar estas etiquetas nosotros mismos."**:
#     * Se explica cómo pandas maneja los índices de las filas por defecto: asigna números secuenciales empezando desde 0.
#     * Se indica que, aunque esto es útil en algunos casos, a menudo es necesario personalizar los índices de las filas.
# 3.  **"La lista de etiquetas de fila utilizada en un DataFrame se conoce como un Índice. Podemos asignar valores a él utilizando un parámetro `index` en nuestro constructor:"**:
#     * Se introduce el concepto de "Índice" como la lista de etiquetas de las filas.
#     * Se muestra cómo utilizar el parámetro `index` en el constructor `pd.DataFrame()` para asignar etiquetas personalizadas a las filas.
# 4.  **`pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])`**:
#     * Este código crea un DataFrame similar al anterior, pero con índices de fila personalizados.
#     * El diccionario define las columnas 'Bob' y 'Sue' con sus respectivos datos.
#     * El parámetro `index=['Product A', 'Product B']` asigna las etiquetas 'Product A' y 'Product B' a las filas en lugar de los números 0 y 1.
#     * Si lo quisieramos ver, deberiamos agregar la funcion print() alrededor de la sentencia:

# Serie ejemplo 1
serie_1 = pd.Series([1, 2, 3, 4, 5])
print("\nSerie ejemplo 1:")
print(serie_1)
# Este print muestra una Serie con índices numéricos por defecto.
# Serie ejemplo 1:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Serie ejemplo 2 (con index y nombre)
serie_2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print("\nSerie ejemplo 2 (con index y nombre):")
print(serie_2)
# Este print muestra una Serie con índices personalizados y un nombre.
# Serie ejemplo 2 (con index y nombre):
# 2015 Sales    30
# 2016 Sales    35
# 2017 Sales    40
# Name: Product A, dtype: int64

# Explicación:

# "Series. Una Serie, por el contrario, es una secuencia de valores de datos. Si un DataFrame es una tabla, una Serie es una lista. Y de hecho, puedes crear una con nada más que una lista:":
# Se introduce el concepto de "Serie" como una estructura de datos unidimensional, similar a una lista.
# Se establece la analogía: DataFrame es a tabla como Serie es a lista.
# Se muestra cómo crear una Serie a partir de una lista simple.
#  
# pd.Series([1, 2, 3, 4, 5]):
# Este código crea una Serie con los valores 1, 2, 3, 4 y 5.
# Por defecto, pandas asigna índices numéricos (0, 1, 2, ...) a los elementos de la Serie.
# dtype: int64 indica que los valores de la Serie son enteros de 64 bits.
# "Una Serie es, en esencia, una sola columna de un DataFrame. Así que puedes asignar etiquetas de fila a la Serie de la misma manera que antes, utilizando un parámetro index. Sin embargo, una Serie no tiene un nombre de columna, solo tiene un nombre global:":
# Se establece la conexión entre Series y DataFrames: una Serie puede ser vista como una columna de un DataFrame.
# Se confirma que se puede personalizar el índice de una Serie usando el parámetro index.
# Se diferencia de los DataFrames: las Series no tienen nombres de columna, pero pueden tener un nombre general.
# pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'):
# Este código crea una Serie con valores de ventas y un índice personalizado.
# index=['2015 Sales', '2016 Sales', '2017 Sales'] asigna etiquetas personalizadas a los elementos de la Serie.
# name='Product A' asigna el nombre "Product A" a la Serie.
# dtype: int64 indica que los valores de la Serie son enteros de 64 bits.
# "La Serie y el DataFrame están íntimamente relacionados. Es útil pensar en un DataFrame como si fuera solo un montón de Series "pegadas". Veremos más de esto en la siguiente sección de este tutorial.":
# Se enfatiza la relación cercana entre Series y DataFrames.
# Se proporciona una analogía útil: un DataFrame puede ser conceptualizado como una colección de Series unidas.
# Se indica que esta relación se explorará más a fondo en la siguiente sección del tutorial.
# En resumen, este fragmento introduce las Series como una estructura de datos unidimensional en pandas, explicando cómo crearlas, personalizarlas y cómo se relacionan con los DataFrames.

# 1. Cargar los datos
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'  # Ruta al archivo CSV
melbourne_data = pd.read_csv(melbourne_file_path)  # Leer el archivo CSV en un DataFrame de pandas

# 2. Verificar las dimensiones del DataFrame
print("Dimensiones del DataFrame:")
print(melbourne_data.shape)
# Este print muestra el número de filas y columnas del DataFrame.
# Dimensiones del DataFrame:
# (13580, 21)

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

# [5 rows x 21 columns]

# 4. Mostrar información general del DataFrame
print("\nInformación general del DataFrame:")
print(melbourne_data.info())
# Este print muestra información sobre las columnas, tipos de datos y valores no nulos.
# Información general del DataFrame:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 13580 entries, 0 to 13579
# Data columns (total 21 columns):
  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
# 0   Suburb         13580 non-null  object 
# 1   Address        13580 non-null  object 
# 2   Rooms          13580 non-null  int64  
# 3   Type           13580 non-null  object 
# 4   Price          13580 non-null  float64
# 5   Method         13580 non-null  object 
# 6   SellerG        13580 non-null  object 
# 7   Date           13580 non-null  object 
# 8   Distance       13580 non-null  float64
# 9   Postcode       13580 non-null  float64
# 10  Bedroom2       13580 non-null  float64
# 11  Bathroom       13580 non-null  float64
# 12  Car            13518 non-null  float64
# 13  Landsize       13580 non-null  float64
# 14  BuildingArea   7130 non-null   float64
# 15  YearBuilt      8205 non-null   float64
# 16  CouncilArea    12211 non-null  object 
# 17  Lattitude      13580 non-null  float64
# 18  Longtitude     13580 non-null  float64
# 19  Regionname     13580 non-null  object 
# 20  Propertycount  13580 non-null  float64
# dtypes: float64(12), int64(1), object(8)
# memory usage: 2.2+ MB
# None

# 5. Mostrar estadísticas descriptivas del DataFrame
print("\nEstadísticas descriptivas del DataFrame:")
print(melbourne_data.describe())
# Este print muestra estadísticas como la media, desviación estándar, mínimo, máximo, etc.
# Estadísticas descriptivas del DataFrame:
#               Rooms         Price      Distance  ...     Lattitude    Longtitude  Propertycount
# count  13580.000000  1.358000e+04  13580.000000  ...  13580.000000  13580.000000   13580.000000
# mean       2.937997  1.075684e+06     10.137776  ...    -37.809203    144.995216    7454.417378
# std        0.955748  6.393107e+05      5.868725  ...      0.079260      0.103916    4378.581772
# min        1.000000  8.500000e+04      0.000000  ...    -38.182550    144.431810     249.000000
# 25%        2.000000  6.500000e+05      6.100000  ...    -37.856822    144.929600    4380.000000
# 50%        3.000000  9.030000e+05      9.200000  ...    -37.802355    145.000100    6555.000000
# 75%        3.000000  1.330000e+06     13.000000  ...    -37.756400    145.058305   10331.000000
# max       10.000000  9.000000e+06     48.100000  ...    -37.408530    145.526350   21650.000000

# [8 rows x 13 columns]

