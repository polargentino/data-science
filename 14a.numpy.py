import pandas as pd
import numpy as np

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Resumen de la columna 'Price'
print("Resumen de 'Price':")
print(melbourne_data.Price.describe())
# Resumen de 'Price':
# count    1.358000e+04
# mean     1.075684e+06
# std      6.393107e+05
# min      8.500000e+04
# 25%      6.500000e+05
# 50%      9.030000e+05
# 75%      1.330000e+06
# max      9.000000e+06
# Name: Price, dtype: float64

# Resumen de la columna 'CouncilArea'
print("\nResumen de 'CouncilArea':")
print(melbourne_data.CouncilArea.describe())
# Resumen de 'CouncilArea':
# count        12211
# unique          33
# top       Moreland
# freq          1163
# Name: CouncilArea, dtype: object


# Media de los precios
print("\nMedia de los precios:")
print(melbourne_data.Price.mean())
# Media de los precios:
# 1075684.079455081

# Valores únicos en 'CouncilArea'
print("\nValores únicos en 'CouncilArea':")
print(melbourne_data.CouncilArea.unique())
# Valores únicos en 'CouncilArea':
# ['Yarra' 'Moonee Valley' 'Port Phillip' 'Darebin' 'Hobsons Bay'
#  'Stonnington' 'Boroondara' 'Monash' 'Glen Eira' 'Whitehorse'
#  'Maribyrnong' 'Bayside' 'Moreland' 'Manningham' 'Banyule' 'Melbourne'
#  'Kingston' 'Brimbank' 'Hume' nan 'Knox' 'Maroondah' 'Casey' 'Melton'
#  'Greater Dandenong' 'Nillumbik' 'Whittlesea' 'Frankston' 'Macedon Ranges'
#  'Yarra Ranges' 'Wyndham' 'Cardinia' 'Unavailable' 'Moorabool']

# Conteo de valores en 'CouncilArea'
print("\nConteo de valores en 'CouncilArea':")
print(melbourne_data.CouncilArea.value_counts())
# Conteo de valores en 'CouncilArea':
# CouncilArea
# Moreland             1163
# Boroondara           1160
# Moonee Valley         997
# Darebin               934
# Glen Eira             848
# Stonnington           719
# Maribyrnong           692
# Yarra                 647
# Port Phillip          628
# Banyule               594
# Bayside               489
# Melbourne             470
# Hobsons Bay           434
# Brimbank              424
# Monash                333
# Manningham            311
# Whitehorse            304
# Kingston              207
# Whittlesea            167
# Hume                  164
# Wyndham                86
# Knox                   80
# Maroondah              80
# Melton                 66
# Frankston              53
# Greater Dandenong      52
# Casey                  38
# Nillumbik              36
# Yarra Ranges           18
# Cardinia                8
# Macedon Ranges          7
# Unavailable             1
# Moorabool               1
# Name: count, dtype: int64

# 1. Calcular la mediana de 'Price' usando NumPy
print("\nMediana de 'Price' (NumPy):")
print(np.median(melbourne_data['Price']))
# Calcula la mediana (valor central) de la columna 'Price'.
# Mediana de 'Price' (NumPy):
# 903000.0

# 2. Calcular el rango de 'Price' usando NumPy
print("\nRango de 'Price' (NumPy):")
print(np.ptp(melbourne_data['Price']))
# Calcula el rango (máximo - mínimo) de la columna 'Price'.
# Rango de 'Price' (NumPy):
# 8915000.0


# 3. Calcular la varianza de 'Price' usando NumPy
print("\nVarianza de 'Price' (NumPy):")
print(np.var(melbourne_data['Price']))
# Calcula la varianza de la columna 'Price'.
# Varianza de 'Price' (NumPy):
# 408688105130.5178

# 4. Calcular la covarianza entre 'Price' y 'Rooms' usando NumPy
print("\nCovarianza entre 'Price' y 'Rooms' (NumPy):")
print(np.cov(melbourne_data['Price'], melbourne_data['Rooms'])[0, 1])
# Calcula la covarianza entre las columnas 'Price' y 'Rooms'.
# Covarianza entre 'Price' y 'Rooms' (NumPy):
# 303453.06251573586

# 5. Calcular la correlación entre 'Price' y 'Rooms' usando NumPy
print("\nCorrelación entre 'Price' y 'Rooms' (NumPy):")
print(np.corrcoef(melbourne_data['Price'], melbourne_data['Rooms'])[0, 1])
# Calcula el coeficiente de correlación entre las columnas 'Price' y 'Rooms'.
# Correlación entre 'Price' y 'Rooms' (NumPy):
# 0.4966336761865307

# 6. Calcular la suma acumulativa de 'Price' usando NumPy
print("\nSuma acumulativa de 'Price' (NumPy):")
print(np.cumsum(melbourne_data['Price'].iloc[0:10])) #solo las primeras 10 para no llenar de datos la consola.
# Calcula la suma acumulativa de los primeros 10 valores de la columna 'Price'.
# Suma acumulativa de 'Price' (NumPy):
# Suburb
# Abbotsford     1480000.0
# Abbotsford     2515000.0
# Abbotsford     3980000.0
# Abbotsford     4830000.0
# Abbotsford     6430000.0
# Abbotsford     7371000.0
# Abbotsford     9247000.0
# Abbotsford    10883000.0
# Abbotsford    11183000.0
# Abbotsford    12280000.0
# Name: Price, dtype: float64

# 7. Calcular el producto acumulativo de 'Rooms' usando NumPy
print("\nProducto acumulativo de 'Rooms' (NumPy):")
print(np.cumprod(melbourne_data['Rooms'].iloc[0:5])) #solo las primeras 5 para no llenar de datos la consola.
# Calcula el producto acumulativo de los primeros 5 valores de la columna 'Rooms'.
# Producto acumulativo de 'Rooms' (NumPy):
# Suburb
# Abbotsford      2
# Abbotsford      4
# Abbotsford     12
# Abbotsford     36
# Abbotsford    144
# Name: Rooms, dtype: int64

# 8. Calcular el seno de 'Distance' usando NumPy
print("\nSeno de 'Distance' (NumPy):")
print(np.sin(melbourne_data['Distance'].iloc[0:5])) #solo las primeras 5 para no llenar de datos la consola.
# Calcula el seno de los primeros 5 valores de la columna 'Distance'.
# Seno de 'Distance' (NumPy):
# Suburb
# Abbotsford    0.598472
# Abbotsford    0.598472
# Abbotsford    0.598472
# Abbotsford    0.598472
# Abbotsford    0.598472
# Name: Distance, dtype: float64

# 9. Calcular el valor absoluto de 'Distance' usando NumPy
print("\nValor absoluto de 'Distance' (NumPy):")
print(np.abs(melbourne_data['Distance'].iloc[0:5]))
# Calcula el valor absoluto de los primeros 5 valores de la columna 'Distance'.
# Valor absoluto de 'Distance' (NumPy):
# Suburb
# Abbotsford    2.5
# Abbotsford    2.5
# Abbotsford    2.5
# Abbotsford    2.5
# Abbotsford    2.5
# Name: Distance, dtype: float64

# 10. Redondear los valores de 'Distance' a enteros usando NumPy
print("\nRedondear 'Distance' a enteros (NumPy):")
print(np.round(melbourne_data['Distance'].iloc[0:5]))
# Redondea los primeros 5 valores de la columna 'Distance' a enteros.
# Redondear 'Distance' a enteros (NumPy):
# Suburb
# Abbotsford    2.0
# Abbotsford    2.0
# Abbotsford    2.0
# Abbotsford    2.0
# Abbotsford    2.0
# Name: Distance, dtype: float64


