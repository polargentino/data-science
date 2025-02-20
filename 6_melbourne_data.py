import pandas as pd
# Guarde la ruta del archivo en una variable para facilitar el acceso
melbourne_file_path = "/home/pol/melbourne_data/melb_data.csv"  # Ruta corregida
# Lea los datos y almacene datos en una variable llamada melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# Imprima los primeros 5 registros de la tabla
print(melbourne_data.describe())
#               Rooms         Price  ...    Longtitude  Propertycount
# count  13580.000000  1.358000e+04  ...  13580.000000   13580.000000
# mean       2.937997  1.075684e+06  ...    144.995216    7454.417378
# std        0.955748  6.393107e+05  ...      0.103916    4378.581772
# min        1.000000  8.500000e+04  ...    144.431810     249.000000
# 25%        2.000000  6.500000e+05  ...    144.929600    4380.000000
# 50%        3.000000  9.030000e+05  ...    145.000100    6555.000000
# 75%        3.000000  1.330000e+06  ...    145.058305   10331.000000
# max       10.000000  9.000000e+06  ...    145.526350   21650.000000

# ✔️ describe() genera métricas clave sobre cada columna numérica en el dataset, como:

# count: cantidad de registros.
# mean: media (promedio).
# std: desviación estándar.
# min, max: valores mínimo y máximo.
# percentiles (25%, 50%, 75%): distribución de los datos.

# 📊 ¿Qué significa esto?

# Rooms: Número de habitaciones en cada propiedad (min: 1, max: 10).
# Price: Precio de las casas en Melbourne (min: 85,000, max: 9,000,000).
# Longtitude: Ubicación geográfica de las casas.
# Propertycount: Cantidad de propiedades en cada zona.

print(melbourne_data.head(10)) # Para 10 filas
# 📌 Explicación de print(melbourne_data.head())
# El método head() en Pandas muestra las primeras filas del DataFrame para que puedas ver un vistazo rápido a los datos.
# ¿Qué hace esto?
# ✔️ Muestra las primeras 5 filas del DataFrame melbourne_data.
# ✔️ Permite ver cómo están organizados los datos en columnas.
# ✔️ Útil para comprobar si la lectura del archivo CSV fue correcta.
# Salidas : 
#        Suburb           Address  Rooms  ... Longtitude             Regionname Propertycount
# 0  Abbotsford      85 Turner St      2  ...   144.9984  Northern Metropolitan        4019.0
# 1  Abbotsford   25 Bloomburg St      2  ...   144.9934  Northern Metropolitan        4019.0
# 2  Abbotsford      5 Charles St      3  ...   144.9944  Northern Metropolitan        4019.0
# 3  Abbotsford  40 Federation La      3  ...   144.9969  Northern Metropolitan        4019.0
# 4  Abbotsford       55a Park St      4  ...   144.9941  Northern Metropolitan        4019.0

# [5 rows x 21 columns]

# 🔎 Análisis de la tabla
# 🔹 Cada fila representa una propiedad en Melbourne.
# 🔹 Cada columna contiene información relevante sobre la propiedad, como:

# Columna	Descripción
# Suburb:	Suburbio donde está la propiedad.
# Address:	Dirección exacta de la propiedad.
# Rooms:	Número de habitaciones.
# Type:	Tipo de propiedad (h: casa, u: departamento, t: adosado).
# Price:	Precio en dólares australianos.
# Method:	Método de venta (S: venta estándar, PI: vendido antes de la subasta, etc.).
# SellerG:	Nombre del agente inmobiliario.
# Date:	Fecha de venta.
# Distance:	Distancia al centro de la ciudad (en km).
# Postcode:	Código postal.
# Bedroom2:	Número de habitaciones secundarias.
# Bathroom:	Número de baños.
# Car:	Espacios de estacionamiento.
# Landsize:	Tamaño del terreno en metros cuadrados.
# BuildingArea:	Tamaño de la construcción en metros cuadrados (puede ser NaN si falta el dato).
# YearBuilt:	Año en que se construyó la propiedad (puede ser NaN si falta).
# CouncilArea:	Nombre del área municipal.
# Lattitude y Longtitude:	Coordenadas geográficas de la propiedad.
# Regionname	Región de Melbourne.
# Propertycount:	Número de propiedades en la zona.

print(melbourne_data.columns)
# [10 rows x 21 columns]
# Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
#        'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
#        'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
#        'Longtitude', 'Regionname', 'Propertycount'],
#       dtype='object')

# Seleccionar objetivo de predicción
y = melbourne_data.Price
print(y)
# 0        1480000.0
# 1        1035000.0
# 2        1465000.0
# 3         850000.0
# 4        1600000.0
#            ...    
# 13575    1245000.0
# 13576    1031000.0
# 13577    1170000.0
# 13578    2500000.0
# 13579    1285000.0
# Name: Price, Length: 13580, dtype: float64


# Elejir características(features)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.head())
#    Rooms  Bathroom  Landsize  Lattitude  Longtitude
# 0      2       1.0     202.0   -37.7996    144.9984
# 1      2       1.0     156.0   -37.8079    144.9934
# 2      3       2.0     134.0   -37.8093    144.9944
# 3      3       2.0      94.0   -37.7969    144.9969
# 4      4       1.0     120.0   -37.8072    144.9941

print(X.describe())
#               Rooms      Bathroom       Landsize     Lattitude    Longtitude
# count  13580.000000  13580.000000   13580.000000  13580.000000  13580.000000
# mean       2.937997      1.534242     558.416127    -37.809203    144.995216
# std        0.955748      0.691712    3990.669241      0.079260      0.103916
# min        1.000000      0.000000       0.000000    -38.182550    144.431810
# 25%        2.000000      1.000000     177.000000    -37.856822    144.929600
# 50%        3.000000      1.000000     440.000000    -37.802355    145.000100
# 75%        3.000000      2.000000     651.000000    -37.756400    145.058305
# max       10.000000      8.000000  433014.000000    -37.408530    145.526350


# Se importa DecisionTreeRegressor de sklearn.tree.
from sklearn.tree import DecisionTreeRegressor

# Se crea una instancia del modelo de árbol de decisión y se establece random_state=1 para asegurar que los resultados sean reproducibles.
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model(ajuste del modelo)
# entrena el modelo utilizando los datos de entrada ´X´ (características de las casas) y ´y´ (precios de las casas)
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
# X.head() muestra las primeras 5 filas del DataFrame X, que contiene las características de las casas para las que se van a hacer predicciones.
print(X.head())
print("The predictions are")
# melbourne_model.predict(X.head()) utiliza el modelo entrenado para predecir los precios de las casas basándose en las características proporcionadas en las primeras 5 filas de X.

print(melbourne_model.predict(X.head()))
# Making predictions for the following 5 houses:
#    Rooms  Bathroom  Landsize  Lattitude  Longtitude
# 0      2       1.0     202.0   -37.7996    144.9984
# 1      2       1.0     156.0   -37.8079    144.9934
# 2      3       2.0     134.0   -37.8093    144.9944
# 3      3       2.0      94.0   -37.7969    144.9969
# 4      4       1.0     120.0   -37.8072    144.9941
# The predictions are
# [1480000. 1035000. 1465000.  850000. 1600000.]

# Rooms: Número de habitaciones en la casa.
# Bathroom: Número de baños.
# Landsize: Tamaño del terreno en metros cuadrados.
# Lattitude: Latitud de la ubicación de la casa.
# Longtitude: Longitud de la ubicación de la casa.

# Interpretación
# Predicciones de Precios:
# La primera casa (2 habitaciones, 1 baño, 202 m²) se predice que tiene un precio de 1,480,000.
# La segunda casa (2 habitaciones, 1 baño, 156 m²) se predice que tiene un precio de 1,035,000.
# La tercera casa (3 habitaciones, 2 baños, 134 m²) se predice que tiene un precio de 1,465,000.
# La cuarta casa (3 habitaciones, 2 baños, 94 m²) se predice que tiene un precio de 850,000.
# La quinta casa (4 habitaciones, 1 baño, 120 m²) se predice que tiene un precio de 1,600,000.

# Conclusión
# En resumen, el modelo de árbol de decisión ha sido entrenado con datos sobre casas y ha hecho predicciones sobre los precios de las primeras 5 casas en el conjunto de datos. Los resultados muestran los precios estimados basados en las características de cada casa. Puedes utilizar estas predicciones para evaluar el rendimiento del modelo o para tomar decisiones informadas sobre el mercado inmobiliario.
