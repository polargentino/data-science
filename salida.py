import pandas as pd

# Especifica la ruta del archivo CSV
car_prices_file_path = '/home/pol/Desktop/data-science/car_price_dataset.csv'

# Carga los datos en un DataFrame de pandas
car_prices_data = pd.read_csv(car_prices_file_path)

# Automóvil más caro por marca y tipo de combustible (corregido)
print("Automóvil más caro por marca y tipo de combustible:")
print(car_prices_data.groupby(['Brand', 'Fuel_Type']).apply(lambda df: df.loc[df['Price'].idxmax()]))
print("\n")


# Modelo del primer automóvil por marca (sin include_groups=False)
print("Modelo del primer automóvil por marca:")
print(car_prices_data.groupby('Brand').apply(lambda df: df['Model'].iloc[0]))