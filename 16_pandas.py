import pandas as pd

# Especifica la ruta del archivo CSV
car_prices_file_path = '/home/pol/Desktop/data-science/car_price_dataset.csv'

# Carga los datos en un DataFrame de pandas
car_prices_data = pd.read_csv(car_prices_file_path)

# Imprime las primeras 5 filas para visualizar una muestra del dataset
print("Primeras 5 filas del dataset:")
print(car_prices_data.head())
print("\n")
# Primeras 5 filas del dataset:
#         Brand   Model  Year  Engine_Size  ... Mileage Doors  Owner_Count  Price
# 0         Kia     Rio  2020          4.2  ...  289944     3            5   8501
# 1   Chevrolet  Malibu  2012          2.0  ...    5356     2            3  12092
# 2    Mercedes     GLA  2020          4.2  ...  231440     4            2  11171
# 3        Audi      Q5  2023          2.0  ...  160971     2            1  11780
# 4  Volkswagen    Golf  2003          2.6  ...  286618     3            3   2867

# [5 rows x 10 columns]

# Análisis de la Salida:
# Este es un ejemplo de cómo se verían las primeras 5 filas del DataFrame. Cada fila representa un automóvil y las columnas contienen información como la marca (Brand), modelo (Model), año (Year), tamaño del motor (Engine_Size), kilometraje (Mileage), número de puertas (Doors), número de propietarios anteriores (Owner_Count) y precio (Price).

# En resumen, este código carga un conjunto de datos sobre precios de automóviles desde un archivo CSV y muestra las primeras 5 filas para que el usuario pueda visualizar una muestra de los datos.




# Conteo de marcas usando groupby()
print("Conteo de marcas usando groupby():")
print(car_prices_data.groupby('Brand')['Brand'].count())
print("\n")
# Conteo de marcas usando groupby():
# Brand
# Audi          1038
# BMW            999
# Chevrolet     1003
# Ford          1048
# Honda         1009
# Hyundai        995
# Kia            976
# Mercedes       942
# Toyota         970
# Volkswagen    1020
# Name: Brand, dtype: int64

# Análisis de la Salida:
# En esta línea se utiliza el método groupby() de pandas para agrupar los datos del DataFrame car_prices_data por la columna Brand. Esto significa que se agruparán todas las filas que tengan la misma marca de automóvil.

# car_prices_data.groupby('Brand'): Agrupa el DataFrame por la columna Brand.
# ['Brand']: Selecciona la columna Brand del DataFrame agrupado.
# .count(): Cuenta el número de ocurrencias de cada marca en el grupo.
# El resultado de esta operación es una serie que muestra cuántas veces aparece cada marca en el conjunto de datos

# Precio mínimo por marca
print("Precio mínimo por marca:")
print(car_prices_data.groupby('Brand')['Price'].min())
print("\n")
# Precio mínimo por marca:
# Brand
# Audi          2000
# BMW           2000
# Chevrolet     2000
# Ford          2000
# Honda         2000
# Hyundai       2000
# Kia           2000
# Mercedes      2000
# Toyota        2000
# Volkswagen    2000
# CName: Price, dtype: int64

# Análisis de la Salida:
# En esta línea se utiliza nuevamente el método groupby() de pandas, pero esta vez se agrupa por la columna Brand y se calcula el precio mínimo de los automóviles en cada grupo.

# car_prices_data.groupby('Brand'): Agrupa el DataFrame por la columna Brand.
# ['Price']: Selecciona la columna Price del DataFrame agrupado.
# .min(): Calcula el valor mínimo de la columna Price para cada grupo (marca).
# El resultado de esta operación es una serie que muestra el precio mínimo de los automóviles para cada marca en el conjunto de datos.



# Modelo del primer automóvil por marca (sin include_groups=False)
print("Modelo del primer automóvil por marca:")
print(car_prices_data.groupby('Brand').apply(lambda df: df['Model'].iloc[0]))
# Modelo del primer automóvil por marca:
# Brand
# Audi                Q5
# BMW           5 Series
# Chevrolet       Malibu
# Ford          Explorer
# Honda            Civic
# Hyundai        Elantra
# Kia                Rio
# Mercedes           GLA
# Toyota           Camry
# Volkswagen        Golf

# Análisis de la Salida:
# En esta línea se utiliza el método groupby() para agrupar el DataFrame car_prices_data por la columna Brand, y luego se aplica una función a cada grupo utilizando apply().

# car_prices_data.groupby('Brand'): Agrupa el DataFrame por la columna Brand.
# apply(lambda df: df['Model'].iloc[0]): Aplica una función lambda a cada grupo. La función lambda toma un DataFrame df (que representa un grupo de una marca) y devuelve el primer modelo de automóvil en ese grupo utilizando iloc[0], que selecciona la primera fila de la columna Model.
# El resultado de esta operación es una serie que muestra el primer modelo de automóvil para cada marca en el conjunto de datos.

# Automóvil más caro por marca y tipo de combustible (corregido)
print("Automóvil más caro por marca y tipo de combustible:")
print(car_prices_data.groupby(['Brand', 'Fuel_Type']).apply(lambda df: df.loc[df['Price'].idxmax()]))
print("\n")
# Automóvil más caro por marca y tipo de combustible:
#                            Brand     Model  Year  Engine_Size  ... Mileage Doors  Owner_Count  Price
# Brand      Fuel_Type                                           ...                                  
# Audi       Diesel           Audi        Q5  2020          4.3  ...    4064     2            4  15818
#            Electric         Audi        A3  2021          4.0  ...   54066     3            1  16818
#            Hybrid           Audi        A3  2023          5.0  ...   12234     5            5  18255
#            Petrol           Audi        Q5  2018          5.0  ...    1887     3            3  15962
# BMW        Diesel            BMW  5 Series  2022          4.2  ...   51622     5            2  15367
#            Electric          BMW  5 Series  2017          4.8  ...    5686     2            1  17386
#            Hybrid            BMW  3 Series  2021          4.7  ...   23265     5            4  17134
#            Petrol            BMW  3 Series  2022          4.8  ...   85532     3            5  15289
# Chevrolet  Diesel      Chevrolet   Equinox  2018          4.7  ...    6212     4            3  15575
#            Electric    Chevrolet    Malibu  2022          4.1  ...   31949     5            1  17661
#            Hybrid      Chevrolet    Impala  2021          4.2  ...   17008     5            3  16759
#            Petrol      Chevrolet    Impala  2022          4.9  ...  102089     5            5  15058
# Ford       Diesel           Ford  Explorer  2023          4.4  ...   28301     2            1  16333
#            Electric         Ford  Explorer  2020          4.8  ...   19112     4            5  18017
#            Hybrid           Ford  Explorer  2020          4.7  ...   54878     4            5  16202
#            Petrol           Ford  Explorer  2023          3.4  ...   42411     5            4  15051
# Honda      Diesel          Honda    Accord  2023          4.5  ...   65889     4            5  15682
#            Electric        Honda    Accord  2022          4.0  ...   14658     4            2  17906
#            Hybrid          Honda      CR-V  2023          4.6  ...   10046     4            4  17899
#            Petrol          Honda    Accord  2019          4.5  ...    1711     3            3  15765
# Hyundai    Diesel        Hyundai   Elantra  2022          5.0  ...  135041     2            2  14499
#            Electric      Hyundai   Elantra  2019          4.6  ...    1406     5            3  17871
#            Hybrid        Hyundai    Tucson  2021          4.6  ...   43494     5            1  16630
#            Petrol        Hyundai    Sonata  2022          4.8  ...   14112     2            5  16717
# Kia        Diesel            Kia    Optima  2023          3.6  ...   50457     2            4  15090
#            Electric          Kia       Rio  2015          4.9  ...     446     5            1  16991
#            Hybrid            Kia       Rio  2023          4.2  ...    3490     5            2  17630
#            Petrol            Kia       Rio  2022          4.9  ...    6863     2            1  15462
# Mercedes   Diesel       Mercedes       GLA  2022          4.5  ...   19165     2            5  16316
#            Electric     Mercedes   C-Class  2021          3.9  ...    9279     4            2  17614
#            Hybrid       Mercedes       GLA  2019          3.7  ...   18073     4            5  15638
#            Petrol       Mercedes   C-Class  2023          4.2  ...   18248     2            5  14835
# Toyota     Diesel         Toyota   Corolla  2022          4.8  ...    7292     4            3  16854
#            Electric       Toyota   Corolla  2021          4.7  ...   14924     5            3  18301
#            Hybrid         Toyota   Corolla  2023          4.8  ...   34738     2            3  16105
#            Petrol         Toyota     Camry  2022          4.0  ...   66018     4            5  14879
# Volkswagen Diesel     Volkswagen    Tiguan  2021          4.1  ...   37195     4            5  15256
#            Electric   Volkswagen    Passat  2016          4.8  ...   36943     5            1  16461
#            Hybrid     Volkswagen    Passat  2019          4.6  ...   28657     4            4  16326
#            Petrol     Volkswagen      Golf  2022          4.6  ...   28189     3            2  16236

# Análisis de la Salida:
# En esta línea se utiliza el método groupby() para agrupar el DataFrame car_prices_data por las columnas Brand y Fuel_Type, y luego se aplica una función a cada grupo utilizando apply().

# car_prices_data.groupby(['Brand', 'Fuel_Type']): Agrupa el DataFrame por las columnas Brand y Fuel_Type. Esto significa que se crearán grupos para cada combinación única de marca y tipo de combustible.
# apply(lambda df: df.loc[df['Price'].idxmax()]): Aplica una función lambda a cada grupo. La función lambda toma un DataFrame df (que representa un grupo de una marca y tipo de combustible) y utiliza idxmax() para encontrar el índice de la fila con el precio máximo en la columna Price. Luego, df.loc[...] se utiliza para seleccionar la fila correspondiente a ese índice.
# El resultado de esta operación es un DataFrame que muestra el automóvil más caro para cada combinación de marca y tipo de combustible.


# Resumen estadístico por marca (corregido)
print("Resumen estadístico por marca:")
print(car_prices_data.groupby('Brand')['Price'].agg(['count', 'min', 'max']))
print("\n")
# Resumen estadístico por marca:
#             count   min    max
# Brand                         
# Audi         1038  2000  18255
# BMW           999  2000  17386
# Chevrolet    1003  2000  17661
# Ford         1048  2000  18017
# Honda        1009  2000  17906
# Hyundai       995  2000  17871
# Kia           976  2000  17630
# Mercedes      942  2000  17614
# Toyota        970  2000  18301
# Volkswagen   1020  2000  16461

# Análisis de la Salida:

# En esta línea se utiliza el método groupby() para agrupar el DataFrame car_prices_data por la columna Brand, y luego se aplica la función agg() para calcular estadísticas específicas sobre la columna Price.

# car_prices_data.groupby('Brand'): Agrupa el DataFrame por la columna Brand.
# ['Price']: Selecciona la columna Price del DataFrame agrupado.
# .agg(['count', 'min', 'max']): Aplica varias funciones de agregación a la columna Price. En este caso, se calculan tres estadísticas:
# count: El número de automóviles por marca.
# min: El precio mínimo de los automóviles por marca.
# max: El precio máximo de los automóviles por marca.
# El resultado de esta operación es un DataFrame que muestra el conteo, el precio mínimo y el precio máximo de los automóviles para cada marca.