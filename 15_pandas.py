import pandas as pd  # Importa la librería pandas para manejar los datos

# Especifica la ruta del archivo CSV
car_prices_file_path = 'car_price_dataset.csv'  # Asegúrate de que el archivo existe en la ruta correcta

# Carga los datos en un DataFrame de pandas
car_prices_data = pd.read_csv(car_prices_file_path)

# Imprime las primeras 5 filas para visualizar una muestra del dataset
print("Primeras 5 filas del dataset:")
print(car_prices_data.head())
# Primeras 5 filas del dataset:
#         Brand   Model  Year  Engine_Size  ... Mileage Doors  Owner_Count  Price
# 0         Kia     Rio  2020          4.2  ...  289944     3            5   8501
# 1   Chevrolet  Malibu  2012          2.0  ...    5356     2            3  12092
# 2    Mercedes     GLA  2020          4.2  ...  231440     4            2  11171
# 3        Audi      Q5  2023          2.0  ...  160971     2            1  11780
# 4  Volkswagen    Golf  2003          2.6  ...  286618     3            3   2867

# [5 rows x 10 columns]

# Muestra información general sobre las columnas, tipos de datos y valores nulos
print("\nInformación general del dataset:")
print(car_prices_data.info())
# Información general del dataset:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10000 entries, 0 to 9999
# Data columns (total 10 columns):
 #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   Brand         10000 non-null  object 
#  1   Model         10000 non-null  object 
#  2   Year          10000 non-null  int64  
#  3   Engine_Size   10000 non-null  float64
#  4   Fuel_Type     10000 non-null  object 
#  5   Transmission  10000 non-null  object 
#  6   Mileage       10000 non-null  int64  
#  7   Doors         10000 non-null  int64  
#  8   Owner_Count   10000 non-null  int64  
#  9   Price         10000 non-null  int64  
# dtypes: float64(1), int64(5), object(4)
# memory usage: 781.4+ KB
# None

# Muestra estadísticas descriptivas para las columnas numéricas
print("\nEstadísticas descriptivas del dataset:")
print(car_prices_data.describe())
# Estadísticas descriptivas del dataset:
#                Year   Engine_Size        Mileage         Doors   Owner_Count        Price
# count  10000.000000  10000.000000   10000.000000  10000.000000  10000.000000  10000.00000
# mean    2011.543700      3.000560  149239.111800      3.497100      2.991100   8852.96440
# std        6.897699      1.149324   86322.348957      1.110097      1.422682   3112.59681
# min     2000.000000      1.000000      25.000000      2.000000      1.000000   2000.00000
# 25%     2006.000000      2.000000   74649.250000      3.000000      2.000000   6646.00000
# 50%     2012.000000      3.000000  149587.000000      3.000000      3.000000   8858.50000
# 75%     2017.000000      4.000000  223577.500000      4.000000      4.000000  11086.50000
# max     2023.000000      5.000000  299947.000000      5.000000      5.000000  18301.00000


# Muestra los nombres de las columnas
print("\nNombres de las columnas en el dataset:")
print(car_prices_data.columns)
# Nombres de las columnas en el dataset:
# Index(['Brand', 'Model', 'Year', 'Engine_Size', 'Fuel_Type', 'Transmission',
#        'Mileage', 'Doors', 'Owner_Count', 'Price'],
#       dtype='object')

# Muestra la cantidad de valores únicos por cada columna categórica
print("\nValores únicos en columnas categóricas:")
for col in car_prices_data.select_dtypes(include=['object']).columns:
    print(f"{col}: {car_prices_data[col].nunique()} valores únicos")
# Valores únicos en columnas categóricas:
# Brand: 10 valores únicos
# Model: 30 valores únicos
# Fuel_Type: 4 valores únicos
# Transmission: 3 valores únicos

# Muestra la cantidad de valores nulos por columna
print("\nValores nulos por columna:")
print(car_prices_data.isnull().sum())
# Valores nulos por columna:
# Brand           0
# Model           0
# Year            0
# Engine_Size     0
# Fuel_Type       0
# Transmission    0
# Mileage         0
# Doors           0
# Owner_Count     0
# Price           0
# dtype: int64

# Muestra la cantidad total de filas y columnas
print("\nDimensiones del dataset (filas, columnas):")
print(car_prices_data.shape)
# Dimensiones del dataset (filas, columnas):
# (10000, 10)

# 🔍 Explicación adicional de las nuevas líneas:
# describe() 📊 → Proporciona estadísticas descriptivas de las columnas numéricas.
# columns 📌 → Lista los nombres de todas las columnas en el dataset.
# nunique() 🔢 → Muestra cuántos valores únicos hay en cada columna categórica.
# isnull().sum() 🚨 → Cuenta los valores nulos en cada columna para identificar posibles problemas en los datos.
# shape 📏 → Indica la cantidad total de filas y columnas en el dataset.