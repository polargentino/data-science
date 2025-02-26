import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Asignar un valor constante a una nueva columna
melbourne_data['critic'] = 'everyone'
print("Columna 'critic' con valor constante:")
print(melbourne_data['critic'].head())
# Columna 'critic' con valor constante:
# Suburb
# Abbotsford    everyone
# Abbotsford    everyone
# Abbotsford    everyone
# Abbotsford    everyone
# Abbotsford    everyone
# Name: critic, dtype: object

# Asignar valores iterables a una nueva columna
melbourne_data['index_backwards'] = range(len(melbourne_data), 0, -1)
print("\nColumna 'index_backwards' con valores iterables:")
print(melbourne_data['index_backwards'].head())
# Columna 'index_backwards' con valores iterables:
# Suburb
# Abbotsford    13580
# Abbotsford    13579
# Abbotsford    13578
# Abbotsford    13577
# Abbotsford    13576
# Name: index_backwards, dtype: int64

# GEmini 2.0 Flash
#     * He sustituido todas las instancias de `reviews` por `melbourne_data` para reflejar tu DataFrame.
# 2.  **Ejemplos con Asignación de Datos:**
#     * Los ejemplos `melbourne_data['critic'] = 'everyone'` y `melbourne_data['index_backwards'] = range(len(melbourne_data), 0, -1)` muestran cómo asignar datos a nuevas columnas en el DataFrame.
#     * El primer ejemplo muestra como agregar una columna de valores constantes.
#     * El segundo ejemplo muestra como agregar una columna con valores iterables, en este caso, una secuencia de números descendentes.

# **Explicación Adicional:**

# * **Asignación de Valores Constantes:**
#     * Puedes crear una nueva columna y asignarle un valor constante a todas las filas.
#     * Esto es útil para agregar información adicional o etiquetas a tu DataFrame.
# * **Asignación con Iterables:**
#     * Puedes crear una nueva columna y asignarle valores de una lista, rango u otro iterable.
#     * La longitud del iterable debe coincidir con el número de filas en el DataFrame.
#    * En el ejemplo, `range(len(melbourne_data), 0, -1)` crea una secuencia de números descendentes desde la longitud del DataFrame hasta 1, lo que se utiliza para crear una columna de índices inversos.
