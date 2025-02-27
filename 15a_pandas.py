# Ejemplo:
# Si encuentras un dataset en Kaggle, puedes descargarlo y usarlo en Python con pandas:
import pandas as pd
# comandos:
# kaggle --version
# kaggle datasets list
# kaggle datasets download asinow/car-price-dataset
# unzip car-price-dataset.zip(en la capeta que lo descargamos)
# Carga el dataset descargado
df = pd.read_csv("car_price_dataset.csv")

# Verifica su contenido
print(df.head())
#        Brand   Model  Year  Engine_Size  ... Mileage Doors  Owner_Count  Price
# 0         Kia     Rio  2020          4.2  ...  289944     3            5   8501
# 1   Chevrolet  Malibu  2012          2.0  ...    5356     2            3  12092
# 2    Mercedes     GLA  2020          4.2  ...  231440     4            2  11171
# 3        Audi      Q5  2023          2.0  ...  160971     2            1  11780
# 4  Volkswagen    Golf  2003          2.6  ...  286618     3            3   2867

# [5 rows x 10 columns]
