import pandas as pd
# Fuente: Códigos: Gemini2.0 Flash, Explicaciones: Blackbox AI
# Se importa la biblioteca pandas, que es esencial para la manipulación y análisis de datos en Python.
# Especifica la ruta del archivo CSV
car_prices_file_path = '/home/pol/Desktop/data-science/car_price_dataset.csv'
# Se define la variable car_prices_file_path que contiene la ruta del archivo CSV que se desea cargar.
# Carga los datos en un DataFrame de pandas
car_prices_data = pd.read_csv(car_prices_file_path)
# Se utiliza pd.read_csv() para leer el archivo CSV y cargarlo en un DataFrame llamado car_prices_data

# Agrupamiento con multi-índice
car_prices_grouped = car_prices_data.groupby(['Brand', 'Fuel_Type']).Price.agg(['count'])
print("DataFrame con multi-índice:")
print(car_prices_grouped)
# car_prices_grouped = car_prices_data.groupby(['Brand', 'Fuel_Type']).Price.agg(['count'])

# En esta línea se realiza un agrupamiento del DataFrame por las columnas Brand y Fuel_Type. Esto crea un multi-índice, donde cada combinación única de marca y tipo de combustible se convierte en un índice en el nuevo DataFrame.

# car_prices_data.groupby(['Brand', 'Fuel_Type']): Agrupa el DataFrame por las columnas Brand y Fuel_Type.
# .Price: Selecciona la columna Price del DataFrame agrupado.
# .agg(['count']): Aplica la función de agregación count para contar el número de automóviles en cada grupo (combinación de marca y tipo de combustible).
# El resultado de esta operación es un nuevo DataFrame llamado car_prices_grouped, que tiene un multi-índice y muestra el conteo de automóviles para cada combinación de marca y tipo de combustible.

# DataFrame con multi-índice:
#                       count
# Brand      Fuel_Type       
# Audi       Diesel       248
#            Electric     262
#            Hybrid       280
#            Petrol       248
# BMW        Diesel       245
#            Electric     279
#            Hybrid       217
#            Petrol       258
# Chevrolet  Diesel       260
#            Electric     250
#            Hybrid       257
#            Petrol       236
# Ford       Diesel       264
#            Electric     278
#            Hybrid       258
#            Petrol       248
# Honda      Diesel       248
#            Electric     265
#            Hybrid       256
#            Petrol       240
# Hyundai    Diesel       250
#            Electric     255
#            Hybrid       253
#            Petrol       237
# Kia        Diesel       260
#            Electric     244
#            Hybrid       242
#            Petrol       230
# Mercedes   Diesel       251
#            Electric     249
#            Hybrid       216
#            Petrol       226
# Toyota     Diesel       246
#            Electric     268
#            Hybrid       224
#            Petrol       232
# Volkswagen Diesel       240
#            Electric     275
#            Hybrid       250
#            Petrol       255




# Tipo de índice
mi = car_prices_grouped.index
print("\nTipo de índice:")
print(type(mi))
# Tipo de índice:
# <class 'pandas.core.indexes.multi.MultiIndex'>
# mi = car_prices_grouped.index
# En esta línea, se obtiene el índice del DataFrame car_prices_grouped y se almacena en la variable mi. Dado que car_prices_grouped fue creado utilizando un agrupamiento con múltiples columnas (marca y tipo de combustible), el índice será un MultiIndex.
# Este es un ejemplo de cómo se vería la salida. Indica que el tipo de índice es MultiIndex, lo que confirma que el índice del DataFrame car_prices_grouped es un índice múltiple, que se utiliza para representar datos que tienen múltiples niveles de agrupación.




# Convertir a índice regular
car_prices_reset = car_prices_grouped.reset_index()
print("\nDataFrame con índice regular:")
print(car_prices_reset)
# En esta línea, se utiliza el método reset_index() en el DataFrame car_prices_grouped. Este método convierte el índice actual (que es un MultiIndex en este caso) en columnas regulares del DataFrame. Como resultado, se crea un nuevo DataFrame llamado car_prices_reset que tiene un índice regular (numérico) y las columnas que antes formaban parte del índice se convierten en columnas del DataFrame.

# DataFrame con índice regular:
#          Brand Fuel_Type  count
# 0         Audi    Diesel    248
# 1         Audi  Electric    262
# 2         Audi    Hybrid    280
# 3         Audi    Petrol    248
# 4          BMW    Diesel    245
# 5          BMW  Electric    279
# 6          BMW    Hybrid    217
# 7          BMW    Petrol    258
# 8    Chevrolet    Diesel    260
# 9    Chevrolet  Electric    250
# 10   Chevrolet    Hybrid    257
# 11   Chevrolet    Petrol    236
# 12        Ford    Diesel    264
# 13        Ford  Electric    278
# 14        Ford    Hybrid    258
# 15        Ford    Petrol    248
# 16       Honda    Diesel    248
# 17       Honda  Electric    265
# 18       Honda    Hybrid    256
# 19       Honda    Petrol    240
# 20     Hyundai    Diesel    250
# 21     Hyundai  Electric    255
# 22     Hyundai    Hybrid    253
# 23     Hyundai    Petrol    237
# 24         Kia    Diesel    260
# 25         Kia  Electric    244
# 26         Kia    Hybrid    242
# 27         Kia    Petrol    230
# 28    Mercedes    Diesel    251
# 29    Mercedes  Electric    249
# 30    Mercedes    Hybrid    216
# 31    Mercedes    Petrol    226
# 32      Toyota    Diesel    246
# 33      Toyota  Electric    268
# 34      Toyota    Hybrid    224
# 35      Toyota    Petrol    232
# 36  Volkswagen    Diesel    240
# 37  Volkswagen  Electric    275
# 38  Volkswagen    Hybrid    250
# 39  Volkswagen    Petrol    255

