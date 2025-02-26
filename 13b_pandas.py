import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

pd.set_option('display.max_rows', 5)

# Verificar los índices
print("Índices del DataFrame:")
print(melbourne_data.index)
# Índices del DataFrame:
# Index(['Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford',
#        'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford', 'Abbotsford',
#        ...
#        'Wantirna South', 'Wantirna South', 'Watsonia', 'Werribee',
#        'Westmeadows', 'Wheelers Hill', 'Williamstown', 'Williamstown',
#        'Williamstown', 'Yarraville'],
#       dtype='object', name='Suburb', length=13580)

# Acceder a una fila por nombre de suburbio
print("\nFila con índice 'Abbotsford':")
print(melbourne_data.loc['Abbotsford'].iloc[0])
# Fila con índice 'Abbotsford':
# Address                   85 Turner St
# Rooms                                2
#                          ...          
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, Length: 20, dtype: object

# Acceder a la segunda fila por posición
print("\nSegunda fila (usando iloc[1]):")
print(melbourne_data.iloc[1])
# Segunda fila (usando iloc[1]):
# Address                25 Bloomburg St
# Rooms                                2
#                          ...          
# Regionname       Northern Metropolitan
# Propertycount                   4019.0
# Name: Abbotsford, Length: 20, dtype: object

# Opcional: Restablecer el índice
# melbourne_data = melbourne_data.reset_index()
# print("\nFila con índice 1 (después de restablecer el índice):")
# print(melbourne_data.loc[1])

