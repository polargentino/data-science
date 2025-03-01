import pandas as pd

# Especifica la ruta del archivo CSV
ufo_file_path = '/home/pol/Downloads/ufo_sightings_scrubbed.csv'
# Explicación de los Cambios:

# ufo_file_path:
# Se ha actualizado la ruta del archivo a /home/pol/Downloads/ufo_sightings_scrubbed.csv.


# Carga los datos en un DataFrame de pandas con tipos especificados y low_memory=False
ufo_data = pd.read_csv(ufo_file_path)
# ufo_data:
# Se ha especificado dtype={'latitude': str, 'duration (seconds)': str} y low_memory=False al cargar los datos para manejar los tipos de datos mixtos y evitar el DtypeWarning.

# Imprimir información general sobre el DataFrame
print("Información general del DataFrame:")
print(ufo_data.info())
print("\n")