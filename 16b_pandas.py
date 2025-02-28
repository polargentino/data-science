import pandas as pd

# Especifica la ruta del archivo CSV
car_prices_file_path = '/home/pol/Desktop/data-science/car_price_dataset.csv'

# Carga los datos en un DataFrame de pandas
car_prices_data = pd.read_csv(car_prices_file_path)

# Agrupamiento con multi-índice
car_prices_grouped = car_prices_data.groupby(['Brand', 'Fuel_Type']).Price.agg(['count'])
# En esta línea, se agrupan los datos por las columnas Brand y Fuel_Type, y se cuenta el número de automóviles en cada grupo. El resultado es un DataFrame con un multi-índice.
# Convertir a índice regular
car_prices_grouped = car_prices_grouped.reset_index()
# Aquí se convierte el índice múltiple en un índice regular, creando un nuevo DataFrame donde las columnas Brand y Fuel_Type son columnas normales.
# Ordenar por conteo ascendente
print("Ordenado por conteo ascendente:")
print(car_prices_grouped.sort_values(by='count'))
# Ordenado por conteo ascendente:
#          Brand Fuel_Type  count
# 30    Mercedes    Hybrid    216
# 6          BMW    Hybrid    217
# 34      Toyota    Hybrid    224
# 31    Mercedes    Petrol    226
# 27         Kia    Petrol    230
# 35      Toyota    Petrol    232
# 11   Chevrolet    Petrol    236
# 23     Hyundai    Petrol    237
# 19       Honda    Petrol    240
# 36  Volkswagen    Diesel    240
# 26         Kia    Hybrid    242
# 25         Kia  Electric    244
# 4          BMW    Diesel    245

# Explicación: 
# En esta línea, se imprime un mensaje que indica que se va a mostrar el DataFrame ordenado por el conteo de automóviles en orden ascendente. Se utiliza el método sort_values(by='count') para ordenar el DataFrame car_prices_grouped por la columna count.


# Ordenar por conteo descendente
print("\nOrdenado por conteo descendente:")
print(car_prices_grouped.sort_values(by='count', ascending=False))
# Ordenado por conteo descendente:
#          Brand Fuel_Type  count
# 2         Audi    Hybrid    280
# 5          BMW  Electric    279
# 13        Ford  Electric    278
# 37  Volkswagen  Electric    275
# 33      Toyota  Electric    268
# 17       Honda  Electric    265
# 12        Ford    Diesel    264
# 1         Audi  Electric    262
# 8    Chevrolet    Diesel    260
# 24         Kia    Diesel    260
# 7          BMW    Petrol    258

# En esta línea, se utiliza el método sort_values() para ordenar el DataFrame car_prices_grouped por la columna count en orden descendente. El argumento ascending=False indica que se desea un orden de mayor a menor.
# Este es un ejemplo de cómo se vería la salida del DataFrame ordenado por el conteo descendente. Cada fila muestra una combinación de marca y tipo de combustible, junto con el conteo de automóviles en esa categoría. Por ejemplo, "Audi" tiene 280 automóviles híbridos, "BMW" tiene 279 automóviles eléctricos, y así sucesivamente.



# Ordenar por índice
print("\nOrdenado por índice:")
print(car_prices_grouped.sort_index())
# Ordenado por índice:
#          Brand Fuel_Type  count
# 0         Audi    Diesel    248
# 1         Audi  Electric    262
# 2         Audi    Hybrid    280
# 3         Audi    Petrol    248
# 4          BMW    Diesel    245
# 5          BMW  Electric    279
# 6          BMW    Hybrid    217
# 7          BMW    Petrol    258

# En esta línea, se utiliza el método sort_index() para ordenar el DataFrame car_prices_grouped por su índice. Este método organiza las filas del DataFrame en función de los valores del índice, que en este caso son los números de fila generados al restablecer el índice.




# Ordenar por marca y conteo
print("\nOrdenado por marca y conteo:")
print(car_prices_grouped.sort_values(by=['Brand', 'count']))
# Ordenado por marca y conteo:
#          Brand Fuel_Type  count
# 0         Audi    Diesel    248
# 3         Audi    Petrol    248
# 1         Audi  Electric    262
# 2         Audi    Hybrid    280
# 6          BMW    Hybrid    217
# 4          BMW    Diesel    245
# 7          BMW    Petrol    258

# En esta línea, se utiliza el método sort_values() para ordenar el DataFrame car_prices_grouped por las columnas Brand y count. Al pasar una lista de columnas al argumento by, el DataFrame se ordena primero por la columna Brand y, dentro de cada marca, se ordena por la columna count
# Este es un ejemplo de cómo se vería la salida del DataFrame ordenado por marca y conteo. En este caso, todas las filas que pertenecen a la marca "Audi" están agrupadas juntas, y dentro de esas filas, están ordenadas por el conteo de automóviles. Por ejemplo, "Audi" tiene 248 automóviles de tipo Diesel y Petrol, y 262 automóviles de tipo Electric.
