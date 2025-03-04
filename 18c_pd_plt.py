"""
Distribución de Calificaciones de Madurez:

Podemos crear un gráfico de barras para mostrar la distribución 
de las calificaciones de madurez de las películas. Esto nos dará 
una idea de qué tipo de contenido está disponible en Netflix en 
términos de clasificación por edades
"""

import pandas as pd
import matplotlib.pyplot as plt

# Especifica la ruta del archivo CSV
netflix_file_path = '/home/pol/Downloads/Netflix Data new.csv'

# Carga los datos en un DataFrame de pandas
netflix_data = pd.read_csv(netflix_file_path)

# Contar la frecuencia de cada calificación de madurez
maturity_counts = netflix_data['Maturity Rating'].value_counts()
# Cuenta la frecuencia de cada calificación de madurez en la columna "Maturity Rating".


# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
maturity_counts.plot(kind='bar') # Crea un gráfico de barras con los resultados del conteo.

plt.xlabel('Calificación de Madurez')
plt.ylabel('Número de Películas')
plt.title('Distribución de Calificaciones de Madurez en Netflix')

plt.xticks(rotation=45, ha='right') # Rota las etiquetas del eje x para que sean más legibles.

plt.tight_layout()
plt.show()

# ¡Excelente! El gráfico de barras que generaste muestra la distribución de las 
# calificaciones de madurez en Netflix de manera clara y concisa.

# Análisis del Gráfico:

# Dominio de U/A 16+: La calificación "U/A 16+" es claramente la más frecuente 
# en el conjunto de datos, con una cantidad significativamente mayor de películas 
# en comparación con las demás calificaciones.
# Popularidad de A y U/A 13+: Las calificaciones "A" y "U/A 13+" también son muy 
# comunes, seguidas de cerca por "U/A 7+".
# Menor Cantidad de U: La calificación "U" (apta para todos los públicos) tiene 
# una representación mucho menor en el conjunto de datos.
# Interpretación:

# El gráfico sugiere que Netflix tiene una gran cantidad de contenido clasificado 
# para adolescentes mayores y adultos jóvenes ("U/A 16+" y "A"), lo que podría 
# indicar una preferencia por este tipo de contenido entre los usuarios o una 
# estrategia de producción de contenido por parte de Netflix.
# La presencia de contenido clasificado para niños mayores y adolescentes 
# ("U/A 13+" y "U/A 7+") también es notable, lo que podría indicar un 
# esfuerzo por ofrecer contenido para una variedad de edades.
# La menor cantidad de contenido clasificado para todos los públicos 
# ("U") podría deberse a una menor demanda o a una estrategia de 
# contenido más enfocada en los grupos de edad mencionados anteriormente.