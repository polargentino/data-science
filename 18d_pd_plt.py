"""
3. Distribución de Años de Lanzamiento:

Podemos crear un histograma o un gráfico de líneas para mostrar 
la distribución de los años de lanzamiento de las películas. 
Esto nos dará una idea de la cantidad de películas más antiguas 
y más nuevas en el conjunto de datos.

"""
import pandas as pd
import matplotlib.pyplot as plt

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# Convertir la columna 'Release Year' a numérica (manejar errores)
netflix_data['Release Year'] = pd.to_numeric(netflix_data['Release Year'], errors='coerce')
# Intenta convertir la columna "Release Year" a valores numéricos.
# errors='coerce' reemplaza los valores no válidos con NaN.

# Eliminar filas con valores NaN en 'Release Year'
netflix_data = netflix_data.dropna(subset=['Release Year'])
# Elimina las filas donde el año de lanzamiento es NaN.


# Crear el histograma
plt.figure(figsize=(10, 6))

plt.hist(netflix_data['Release Year'], bins=20, edgecolor='black')
# Crea un histograma con los años de lanzamiento.
# bins=20 especifica el número de contenedores (barras) en el histograma.
# edgecolor='black' añade bordes negros a las barras.

plt.xlabel('Año de Lanzamiento')
plt.ylabel('Número de Películas')
plt.title('Distribución de Años de Lanzamiento en Netflix')
plt.grid(axis='y', alpha=0.75) # Añade una cuadrícula al eje y para facilitar la lectura del gráfico.

plt.show()

# ¡Excelente! El histograma que generaste muestra la distribución de 
# los años de lanzamiento de las películas en Netflix de manera clara y concisa.

# Análisis del Histograma:

# Aumento Significativo en Años Recientes: Se observa un aumento dramático 
# en el número de películas lanzadas en los años más recientes, 
# especialmente a partir de la década de 2010 y con un pico notable en 
# los años cercanos a 2020.
# Pocas Películas Antiguas: Hay muy pocas películas lanzadas antes de la 
# década de 2000, lo que indica que la mayoría del contenido en Netflix es 
# relativamente nuevo.
# Crecimiento Gradual en la Década de 2000: Se observa un crecimiento 
# gradual en el número de películas lanzadas durante la década de 2000, 
# lo que sugiere un aumento constante en la producción de contenido a lo largo de esos años.
# Interpretación:

# El gráfico sugiere que Netflix se enfoca principalmente en ofrecer 
# contenido reciente, lo que podría indicar una preferencia por parte 
# de los usuarios por películas más nuevas o una estrategia de Netflix 
# para mantener su catálogo actualizado.
# La baja representación de películas antiguas podría deberse a la 
# disponibilidad limitada de derechos de distribución o a una menor 
# demanda por parte de los usuarios.
# El aumento significativo en la producción de películas en los años 
# recientes podría ser el resultado de la creciente popularidad de 
# Netflix como plataforma de streaming y su inversión en contenido original.