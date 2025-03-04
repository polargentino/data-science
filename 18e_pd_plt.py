"""
Ordenar el DataFrame por el Número de Recomendaciones:
Ordenar el DataFrame de forma descendente para encontrar la película con más 
recomendaciones
"""

import pandas as pd
import matplotlib.pyplot as plt

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# Asumimos que tenemos una columna 'Num_Recommendations' con datos válidos
# (En realidad, esta columna no es útil en este conjunto de datos)
# Vamos a crear una columna ficticia para el ejemplo
import numpy as np
np.random.seed(42)  # Para reproducibilidad
netflix_data['Num_Recommendations'] = np.random.randint(1, 100, size=len(netflix_data))

# Ordenar el DataFrame por el número de recomendaciones
recommendations_df = netflix_data[['Title', 'Num_Recommendations']].sort_values(by='Num_Recommendations', ascending=False)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(recommendations_df['Title'][:10], recommendations_df['Num_Recommendations'][:10])
plt.xlabel('Título de la Película')
plt.ylabel('Número de Recomendaciones')
plt.title('Películas Más Recomendadas (Datos Ficticios)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Explicación del Código:

# np.random.seed(42) y netflix_data['Num_Recommendations'] = np.random.randint(1, 100, size=len(netflix_data)):
# Estas líneas generan datos ficticios para la columna Num_Recommendations.
# np.random.seed(42) asegura que los datos generados sean los mismos cada vez que ejecutes el código.
# np.random.randint(1, 100, size=len(netflix_data)) genera números enteros aleatorios entre 1 y 100 para cada película.
# recommendations_df = netflix_data[['Title', 'Num_Recommendations']].sort_values(by='Num_Recommendations', ascending=False):
# Crea un nuevo DataFrame con las columnas "Title" y "Num_Recommendations".
# Ordena el DataFrame de forma descendente por el número de recomendaciones.
# plt.bar(recommendations_df['Title'][:10], recommendations_df['Num_Recommendations'][:10]):
# Crea un gráfico de barras con los 10 títulos de películas más recomendados (según los datos ficticios).
# plt.xticks(rotation=45, ha='right'):
# Rota las etiquetas del eje x para que sean más legibles.
# Consideraciones:

# Datos Ficticios: Recuerda que los datos en la columna Num_Recommendations son ficticios. Si tuvieras datos reales de recomendaciones, deberías usarlos en lugar de los datos generados aleatoriamente.
# Número de Películas: Puedes ajustar el número de películas mostradas en el gráfico cambiando el valor en [:10].
# Personalización del Gráfico: Puedes personalizar el gráfico aún más cambiando los colores, los estilos de línea y otros parámetros.
# Este código te mostrará cómo ordenar y graficar las películas más recomendadas si tuvieras datos válidos. ¡Espero que esto te ayude a entender el proceso!