import pandas as pd

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# Supongamos que tenemos dos conjuntos de datos de Netflix: películas y series
# (Para este ejemplo, vamos a simularlos con el mismo archivo)
netflix_movies = netflix_data.copy()
netflix_series = netflix_data.copy()

# 1. Usando concat() para combinar DataFrames
print("DataFrame combinado usando concat():")
combined_netflix = pd.concat([netflix_movies, netflix_series])
print(combined_netflix.head())
print("\n")
# DataFrame combinado usando concat():
#      N_id  ...                                    Recommendations
# 0  215309  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 1  215318  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 2  217258  ...  81156676, 81231974, 70027007, 80049939, 702179...
# 3  217303  ...  81156676, 70044593, 81231974, 70027007, 800500...
# 4  235527  ...  17517355, 80158546, 80158395, 80074065, 702042...

# [5 rows x 8 columns]
# Combina los DataFrames netflix_movies y netflix_series a lo largo del eje de filas (por defecto).
# Se muestran las primeras 5 filas del DataFrame resultante de la concatenación de netflix_movies y netflix_series.
# Como ambos DataFrames eran copias del mismo DataFrame original, el resultado es esencialmente el doble del DataFrame original.
# Las columnas se mantienen iguales.

# Supongamos que tenemos un DataFrame con información adicional sobre géneros
# (Para este ejemplo, vamos a simularlo con una columna extra)
netflix_genres = netflix_data[['N_id', 'Main Genre']].copy()
netflix_genres.rename(columns={'Main Genre': 'Genre Info'}, inplace=True)

# 2. Usando join() para combinar DataFrames
print("DataFrame combinado usando join():")
left = netflix_data.set_index('N_id')
right = netflix_genres.set_index('N_id')
joined_netflix = left.join(right, rsuffix='_genres')
print(joined_netflix.head())
print("\n")
# DataFrame combinado usando join():
#                                  Title  ... Genre Info
# N_id                                    ...           
# 215309      Ace Ventura: Pet Detective  ...     Comedy
# 215318  Ace Ventura: When Nature Calls  ...     Comedy
# 217258               The Addams Family  ...     Comedy
# 217303            Addams Family Values  ...     Comedy
# 235527                       Agneepath  ...      Drama

# [5 rows x 8 columns]
# Combina los DataFrames left y right usando el índice N_id como clave de unión.
# rsuffix='_genres' agrega el sufijo '_genres' a los nombres de las columnas en 
# el DataFrame right que se superponen con los nombres de las columnas en el DataFrame left.

# Se muestran las primeras 5 filas del DataFrame resultante de la unión de 
# netflix_data y netflix_genres.
# La unión se realizó correctamente utilizando la columna N_id como índice.
# La columna Genre Info (renombrada desde Main Genre en netflix_genres) 
# se ha agregado al DataFrame original.

# 3. Imprimir los nombres de las columnas
print("Nombres de las columnas del DataFrame combinado:")
print(joined_netflix.columns)
print("\n")
# Nombres de las columnas del DataFrame combinado:
# Index(['Title', 'Main Genre', 'Sub Genres', 'Release Year', 'Maturity Rating',
#        'Original Audio', 'Recommendations', 'Genre Info'],
#       dtype='object')

# Imprime los nombres de las columnas del DataFrame combinado.
# Este código te mostrará cómo combinar DataFrames usando concat() y join() 
# en tu conjunto de datos netflix_data.
# Se muestran los nombres de las columnas del DataFrame resultante de la unión.
# Se confirma que la columna Genre Info se ha agregado correctamente.


# Conclusión:

# El código está funcionando correctamente y realizando las operaciones 
# de combinación según lo esperado.
# concat() se ha utilizado para combinar DataFrames a lo largo del eje de filas.
# join() se ha utilizado para combinar DataFrames utilizando un índice común.
# Los resultados muestran que los DataFrames se han combinado correctamente y 
# que las columnas se han agregado según lo esperado.
# Ahora puedes proceder con el análisis de los datos combinados, por ejemplo, 
# explorando la relación entre los géneros principales y otras características 
# del conjunto de datos.
