"""
1. Distribución de Géneros Principales:

Podemos crear un gráfico de barras o un gráfico circular para mostrar 
la distribución de los géneros principales de las películas en el conjunto de datos. 
Esto nos dará una idea de qué géneros son más comunes en Netflix.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# Contar la frecuencia de cada género principal
genre_counts = netflix_data['Main Genre'].value_counts()
# Cuenta la frecuencia de cada género principal en la columna "Main Genre

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar') # Crea un gráfico de barras con los resultados del conteo
plt.xlabel('Género Principal')
plt.ylabel('Número de Películas')
plt.title('Distribución de Géneros Principales en Netflix')
plt.xticks(rotation=45, ha='right') # Rota las etiquetas del eje x para que sean más legibles.
plt.tight_layout()
plt.show()

# ¡Excelente! El gráfico de barras que generaste muestra la distribución de los géneros 
# principales en Netflix de manera clara y concisa.

# Análisis del Gráfico:

# Dominio del Drama: El género "Drama" es claramente el más frecuente en el conjunto de datos, 
# con una cantidad significativamente mayor de películas en comparación con los demás géneros.
# Popularidad de la Comedia: La "Comedia" también es un género muy común, seguido de cerca por los "Documentales".
# Otros Géneros: Los géneros como "Kids", "Acción", "Romance", "Thriller" y "Anime" también tienen una presencia 
# notable, aunque en menor medida.
# Géneros Menos Frecuentes: Los géneros como "Sci-Fi", "Fantasía", "Música", "Talk Show", 
# "Sports", "Variety TV", "Special Interest", "Musical", "Western" y "Friendship" 
# tienen una representación mucho menor en el conjunto de datos.
# Interpretación:

# El gráfico sugiere que Netflix tiene una gran cantidad de contenido dramático y de comedia, 
# lo que podría indicar una preferencia por estos géneros entre los usuarios o una estrategia 
# de producción de contenido por parte de Netflix.
# La presencia de documentales también es notable, lo que podría indicar un interés creciente en 
# este tipo de contenido.
# La menor representación de algunos géneros podría deberse a una menor demanda o a una estrategia 
# de contenido más enfocada en los géneros más populares.
# Posibles Mejoras:

# Añadir Porcentajes: Podrías añadir porcentajes a las barras para mostrar la proporción 
# de cada género en relación con el total de películas.
# Agrupar Géneros Similares: Si hay géneros muy similares, podrías agruparlos para 
# simplificar el gráfico y facilitar la interpretación.
# Usar Colores Diferentes: Podrías usar colores diferentes para las barras para 
# resaltar ciertos géneros o para mejorar la estética del gráfico.
# En general, el gráfico es muy informativo y proporciona una buena visión 
# general de la distribución de géneros principales en Netflix. ¡Buen trabajo!