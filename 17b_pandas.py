import pandas as pd

# Especifica la ruta del archivo CSV
ufo_file_path = '/home/pol/Downloads/ufo_sightings_scrubbed.csv'

# Carga los datos en un DataFrame de pandas con tipos especificados y low_memory=False
ufo_data = pd.read_csv(ufo_file_path, dtype={'latitude': str, 'duration (seconds)': str}, low_memory=False)
"""
En esta línea, se utiliza pd.read_csv() para leer el archivo CSV y cargarlo en un 
DataFrame llamado ufo_data. Se especifican algunos parámetros:

dtype={'latitude': str, 'duration (seconds)': str}: Esto indica que las columnas 
latitude y duration (seconds) deben ser leídas como cadenas de texto (strings) 
en lugar de sus tipos predeterminados. Esto es útil si hay valores no numéricos 
en estas columnas que podrían causar errores al intentar convertirlos a números.

low_memory=False: Este parámetro se utiliza para evitar que pandas divida el archivo 
en fragmentos más pequeños para la inferencia de tipos, lo que puede ser útil en 
archivos grandes.
"""

# Limpieza de 'latitude'
ufo_data['latitude'] = pd.to_numeric(ufo_data['latitude'], errors='coerce')
ufo_data['latitude'] = ufo_data['latitude'].astype('float64')
"""
pd.to_numeric(ufo_data['latitude'], errors='coerce'): Convierte la columna 
latitude a un tipo numérico. Si hay valores que no se pueden convertir (por ejemplo, 
texto no numérico), se reemplazan por NaN (Not a Number) debido al argumento errors='coerce'.

ufo_data['latitude'].astype('float64'): Asegura que la columna latitude sea del tipo float64, 
que es un tipo de dato numérico de punto flotante.
"""

# Limpieza de 'duration (seconds)'
ufo_data['duration (seconds)'] = pd.to_numeric(ufo_data['duration (seconds)'], errors='coerce')
ufo_data['duration (seconds)'] = ufo_data['duration (seconds)'].astype('float64')
"""
Este proceso es similar al de la columna latitude. Se convierte la columna
duration (seconds) a un tipo numérico, y los valores no convertibles se reemplazan por NaN.
"""

# Manejo de valores nulos en 'shape', 'country', 'state', 'comments'
ufo_data['shape'] = ufo_data['shape'].fillna('unknown')
ufo_data['country'] = ufo_data['country'].fillna('unknown')
ufo_data['state'] = ufo_data['state'].fillna('unknown')
ufo_data['comments'] = ufo_data['comments'].fillna('No comments')
"""
En estas líneas, se manejan los valores nulos en las columnas shape, country, 
state y comments. Se utiliza el método fillna() para reemplazar los valores 
nulos con un valor predeterminado:

Para shape, country y state, se reemplazan los valores nulos con la cadena 'unknown'.
Para comments, se reemplazan los valores nulos con la cadena 'No comments'.
"""

# 1. Seleccionar filas con latitude NaN
print("Filas con latitude NaN:")
print(ufo_data[pd.isnull(ufo_data.latitude)].head())
print("\n")
# Filas con latitude NaN:
#                   datetime                          city  ... latitude  longitude 
# 43782  1974-05-22 05:30:00  mescalero indian reservation  ...      NaN -105.624152

# [1 rows x 11 columns]


# pd.isnull(ufo_data.latitude): Crea una serie booleana que indica si cada valor 
# en la columna latitude es NaN.

# ufo_data[pd.isnull(ufo_data.latitude)]: Filtra el DataFrame para mostrar 
# solo las filas donde latitude es NaN.
# head(): Muestra las primeras 5 filas del resultado filtrado.


# 2. Reemplazar NaN en 'shape' con 'Unknown'
print("shape con NaN reemplazados por 'Unknown':")
print(ufo_data['shape'].fillna("Unknown").head())
print("\n")
# shape con NaN reemplazados por 'Unknown':
# 0    cylinder
# 1       light
# 2      circle
# 3      circle
# 4       light
# Name: shape, dtype: object

# ufo_data['shape']: Accede a la columna shape del DataFrame ufo_data.
# .fillna("Unknown"): Utiliza el método fillna() para reemplazar todos los valores NaN en la columna shape con la cadena 'Unknown'. Este método no modifica el DataFrame original a menos que se asigne de nuevo, pero aquí se utiliza directamente para mostrar el resultado.
# .head(): Muestra las primeras 5 filas del resultado después de aplicar el reemplazo.
# Resumen
# En resumen, este código reemplaza los valores NaN en la columna shape 
# del DataFrame de avistamientos de OVNIs con la cadena 'Unknown'. 
# Esto es útil para manejar datos faltantes y asegurar que la columna 
# tenga un valor significativo en lugar de NaN, lo que puede facilitar 
# el análisis posterior. Aunque en este caso específico no se ven NaN en 
# las primeras filas, el método fillna() es una práctica común para limpiar datos.

# 3. Reemplazar 'light' en 'shape' con 'luz'
print("shape con 'light' reemplazados por 'luz':")
print(ufo_data['shape'].replace("light", "luz").head())
print("\n")
# shape con 'light' reemplazados por 'luz':
# 0    cylinder
# 1         luz
# 2      circle
# 3      circle
# 4         luz
# Name: shape, dtype: object

# ufo_data['shape']: Accede a la columna shape del DataFrame ufo_data.
# .replace("light", "luz"): Utiliza el método replace() para reemplazar todas 
# las ocurrencias del valor 'light' en la columna shape con la cadena 'luz'. 
# Este método devuelve una nueva serie con los valores reemplazados.
# .head(): Muestra las primeras 5 filas del resultado después de aplicar el reemplazo.
# Este es un ejemplo de cómo se vería la salida. La salida muestra las 
# primeras 5 filas de la columna shape, donde todas las ocurrencias 
# de 'light' han sido reemplazadas por 'luz'. En este caso, las filas 1 y 4, 
# que originalmente contenían 'light', ahora muestran 'luz'.




# 4. Usando backfill para llenar valores nulos en duration (seconds) (corregido)
print("duration (seconds) usando backfill:")
print(ufo_data['duration (seconds)'].bfill().head())
print('\n')
# duration (seconds) usando backfill:
# 0    2700.0
# 1    7200.0
# 2      20.0
# 3      20.0
# 4     900.0
# Name: duration (seconds), dtype: float64

# ufo_data['duration (seconds)']: Accede a la columna duration (seconds) 
# del DataFrame ufo_data.
# .bfill(): Aplica el método de "backfill" (relleno hacia atrás) a la serie. 
# Este método reemplaza los valores nulos (NaN) con el siguiente valor no nulo 
# que se encuentra más abajo en la columna. Es decir, si hay un NaN, se llenará 
# con el primer valor no nulo que se encuentre después de él en la misma columna.
# .head(): Muestra las primeras 5 filas del resultado después de aplicar el "backfill".
# Este es un ejemplo de cómo se vería la salida. La salida muestra las primeras 5 filas de la columna duration (seconds), donde los valores nulos han sido reemplazados por el siguiente valor no nulo en la columna. Por ejemplo, si la fila 0 tenía un valor nulo, se ha llenado con el valor de la fila 1, y así sucesivamente.

# Resumen
# En resumen, este código utiliza el método de "backfill" para llenar los valores 
# nulos en la columna duration (seconds) del DataFrame de avistamientos de OVNIs. 
# Este enfoque es útil para manejar datos faltantes, especialmente cuando se espera 
# que los valores nulos sean reemplazados por datos que siguen en la secuencia. 
# Sin embargo, es importante tener en cuenta que el uso de "backfill" puede no ser 
# apropiado en todos los contextos, ya que puede introducir sesgos si los datos no 
# son secuenciales o si los valores posteriores no son representativos.




# 5. Usando forward fill para llenar valores nulos en latitude (corregido)
print("latitude usando forward fill:")
print(ufo_data['latitude'].ffill().head())
# latitude usando forward fill:
# 0    29.883056
# 1    29.384210
# 2    53.200000
# 3    28.978333
# 4    21.418056
# Name: latitude, dtype: float64

# ufo_data['latitude']: Accede a la columna latitude del DataFrame ufo_data.
# .ffill(): Aplica el método de "forward fill" (relleno hacia adelante) a 
# la serie. Este método reemplaza los valores nulos (NaN) con el último valor 
# no nulo que se encuentra antes de ellos en la columna. Es decir, si hay un 
# NaN, se llenará con el último valor no nulo que se haya encontrado antes en 
# la misma columna.
# .head(): Muestra las primeras 5 filas del resultado después de aplicar el 
# "forward fill".



