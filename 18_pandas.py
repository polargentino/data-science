import pandas as pd

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# 1. Cambiar el nombre de la columna 'N_id' a 'Netflix_ID'
print("DataFrame con la columna 'N_id' renombrada:")
print(netflix_data.rename(columns={'N_id': 'Netflix_ID'}).head())
print("\n")
# DataFrame con la columna 'N_id' renombrada:
#    Netflix_ID  ...                                    Recommendations
# 0      215309  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 1      215318  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 2      217258  ...  81156676, 81231974, 70027007, 80049939, 702179...
# 3      217303  ...  81156676, 70044593, 81231974, 70027007, 800500...
# 4      235527  ...  17517355, 80158546, 80158395, 80074065, 702042...

# [5 rows x 8 columns]
# Cambia el nombre de la columna N_id a Netflix_ID.

# 2. Cambiar el nombre de los índices 0 y 1
print("DataFrame con los índices 0 y 1 renombrados:")
print(netflix_data.rename(index={0: 'firstEntry', 1: 'secondEntry'}).head())
print("\n")
# DataFrame con los índices 0 y 1 renombrados:
#                N_id  ...                                    Recommendations
# firstEntry   215309  ...  70184054, 60001650, 70112729, 70027007, 115246...
# secondEntry  215318  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 2            217258  ...  81156676, 81231974, 70027007, 80049939, 702179...
# 3            217303  ...  81156676, 70044593, 81231974, 70027007, 800500...
# 4            235527  ...  17517355, 80158546, 80158395, 80074065, 702042...

# [5 rows x 8 columns]
# Cambia los nombres de los índices 0 y 1 a 'firstEntry' y 'secondEntry', respectivamente.


# 3. Cambiar los nombres de los ejes
print("DataFrame con los nombres de los ejes cambiados:")
print(netflix_data.rename_axis("Netflix_Shows", axis='rows').rename_axis("Fields", axis='columns').head())
print("\n")
# DataFrame con los nombres de los ejes cambiados:
# Fields           N_id  ...                                    Recommendations
# Netflix_Shows          ...                                                   
# 0              215309  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 1              215318  ...  70184054, 60001650, 70112729, 70027007, 115246...
# 2              217258  ...  81156676, 81231974, 70027007, 80049939, 702179...
# 3              217303  ...  81156676, 70044593, 81231974, 70027007, 800500...
# 4              235527  ...  17517355, 80158546, 80158395, 80074065, 702042...

# [5 rows x 8 columns]
# Cambia el nombre del índice de filas a "Netflix_Shows" y el nombre del índice de columnas a "Fields".


# 4. Cambiar la columna 'Release Year' a int
netflix_data['Release Year'] = pd.to_numeric(netflix_data['Release Year'], errors='coerce')


# 5. Cambiar el nombre de la columna 'Release Year' a 'Year'
netflix_data = netflix_data.rename(columns={'Release Year': 'Year'})

# 6. Imprimir los nombres de las columnas
print("Nombres de las columnas:")
print(netflix_data.columns)
print("\n")
# Nombres de las columnas:
# Index(['N_id', 'Title', 'Main Genre', 'Sub Genres', 'Year', 'Maturity Rating',
#        'Original Audio', 'Recommendations'],
#       dtype='object')
