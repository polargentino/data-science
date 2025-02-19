import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
melbourne_file_path = "/home/pol/melbourne_data/melb_data.csv"  
melbourne_data = pd.read_csv(melbourne_file_path)

# Crear el histograma de precios
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.hist(melbourne_data['Price'].dropna(), bins=50, color='skyblue', edgecolor='black')

# Etiquetas y título
plt.xlabel('Precio de las casas en AUD')
plt.ylabel('Cantidad de propiedades')
plt.title('Distribución de Precios de Casas en Melbourne')

# Mostrar el gráfico
plt.show()
# 📊 Explicación del código
# Carga los datos usando Pandas.
# plt.hist() crea un histograma de la columna Price.
# bins=50 divide los precios en 50 segmentos para una mejor visualización.
# color='skyblue' y edgecolor='black' mejoran la estética del gráfico.
# Se añaden etiquetas (xlabel, ylabel, title) para mayor claridad.
# plt.show() muestra el gráfico.
# 🔹 ¿Qué veremos en el gráfico?
# Un histograma que nos mostrará cómo están distribuidos los precios de las propiedades:

# Si hay muchas casas en un rango de precios, aparecerán más altas las barras en ese sector.
# Si hay pocas casas caras, las barras en la derecha serán más bajas.

# 🚀 Próximo paso
# Podemos hacer gráficos más avanzados:

# 📈 Gráfico de líneas para analizar tendencias en el tiempo.
# 🏡 Gráfico de dispersión (scatter plot) para ver la relación entre precio y tamaño de la propiedad.
# 📊 Barras para comparar los precios medios en diferentes suburbios.

