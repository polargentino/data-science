import pandas as pd

melbourne_file_path = "/home/pol/melbourne_data/melb_data.csv"  # Ruta corregida
melbourne_data = pd.read_csv(melbourne_file_path)

print(melbourne_data.describe())

