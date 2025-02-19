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