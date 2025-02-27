import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Re-centrar los precios usando map()
melbourne_price_mean = melbourne_data.Price.mean() 
# Esta línea calcula el precio promedio de todas las casas en la columna 'Price' del DataFrame melbourne_data.
# El método .mean() de Pandas calcula la media aritmética de los valores en la Serie melbourne_data.Price.
# El resultado (el precio promedio) se almacena en la variable melbourne_price_mean.

print("Precios re-centrados usando map():")
# Esta línea simplemente imprime un mensaje en la consola para indicar que el siguiente resultado mostrará los precios re-centrados.
print(melbourne_data.Price.map(lambda p: p - melbourne_price_mean).head())
# Esta es la parte clave del código. Vamos a analizarla por partes:
# melbourne_data.Price.map(...):
# El método .map() se aplica a la Serie melbourne_data.Price.
# .map() aplica una función a cada elemento de la Serie.
# lambda p: p - melbourne_price_mean:
# Esta es una función anónima (lambda) que se pasa a .map().
# p representa cada valor individual en la Serie melbourne_data.Price.
# p - melbourne_price_mean resta el precio promedio (melbourne_price_mean) de cada precio individual (p).
# En otras palabras, esta función lambda "re-centra" los precios alrededor de 0, donde 0 representa el precio promedio.
# .head():
# El método .head() se aplica al resultado de .map().
# .head() muestra las primeras 5 filas de la Serie resultante.
# En resumen, esta línea toma cada precio en la columna 'Price', le resta el precio promedio y muestra los primeros 5 resultados.
# Precios re-centrados usando map():
# Suburb
# Abbotsford    404315.920545
# Abbotsford    -40684.079455
# Abbotsford    389315.920545
# Abbotsford   -225684.079455
# Abbotsford    524315.920545
# Name: Price, dtype: float64
# Resultado Impreso:
# El resultado impreso muestra los primeros 5 precios re-centrados.
# Cada valor representa la diferencia entre el precio original de una casa y el precio promedio de todas las casas.
# Los valores positivos indican que el precio de la casa está por encima del promedio, y los valores negativos indican que está por debajo del promedio.
# Propósito:
# El propósito de re-centrar los precios es transformar los datos para que el valor promedio sea 0.
# Esto puede ser útil en ciertos análisis estadísticos o algoritmos de aprendizaje automático donde es importante trabajar con datos centrados.
# Por ejemplo, en algunos algoritmos de aprendizaje automático, centrar los datos puede mejorar la convergencia y el rendimiento.



# Re-centrar los precios usando apply()
def remean_price(row):
# Esta línea define una función llamada remean_price que toma un argumento row.
# Esta función está diseñada para operar sobre cada fila del DataFrame melbourne_data.
   
    row.Price = row.Price - melbourne_price_mean
# Dentro de la función, esta línea accede al valor de la columna 'Price' en la fila actual (row.Price).
# Luego, resta el precio promedio (melbourne_price_mean) del valor actual de 'Price'.
# El resultado de esta resta se asigna nuevamente a row.Price, modificando el valor de la columna 'Price' en la fila actual.    
    return row
# La función remean_price devuelve la fila modificada (row).
print("\nPrecios re-centrados usando apply():")
# Esta línea imprime un mensaje en la consola para indicar que el siguiente resultado mostrará los precios re-centrados usando apply().
print(melbourne_data.apply(remean_price, axis='columns').head())
# Esta es la parte clave del código. Vamos a analizarla por partes:
# melbourne_data.apply(remean_price, axis='columns'):
# El método .apply() se aplica al DataFrame melbourne_data.
# remean_price es la función que se aplica a cada fila del DataFrame.
# axis='columns' (o axis=1) indica que la función se aplica a cada fila (en lugar de a cada columna).
# Para cada fila, Pandas pasa la fila como una Serie a la función remean_price.
# La función remean_price modifica el valor de la columna 'Price' en cada fila restando el precio promedio.
# .apply() devuelve un nuevo DataFrame con los valores de 'Price' modificados.
# .head():
# El método .head() se aplica al DataFrame resultante de .apply().
# .head() muestra las primeras 5 filas del DataFrame modificado.
# Precios re-centrados usando apply():
#                      Address  Rooms  ...             Regionname  Propertycount
# Suburb                               ...                                      
# Abbotsford      85 Turner St      2  ...  Northern Metropolitan         4019.0
# Abbotsford   25 Bloomburg St      2  ...  Northern Metropolitan         4019.0
# Abbotsford      5 Charles St      3  ...  Northern Metropolitan         4019.0
# Abbotsford  40 Federation La      3  ...  Northern Metropolitan         4019.0
# Abbotsford       55a Park St      4  ...  Northern Metropolitan         4019.0

# [5 rows x 20 columns]

# Re-centrar los precios usando resta directa
print("\nPrecios re-centrados usando resta directa:")
# Esta línea imprime un mensaje en la consola para indicar que el siguiente resultado mostrará los precios re-centrados usando resta directa.
print((melbourne_data.Price - melbourne_price_mean).head())
# Esta es la parte clave del código. Vamos a analizarla por partes:
# melbourne_data.Price - melbourne_price_mean:
# Esta expresión realiza una resta directa entre la Serie melbourne_data.Price y el valor escalar melbourne_price_mean.
# Pandas realiza esta operación elemento por elemento, restando el precio promedio (melbourne_price_mean) de cada precio individual en la Serie melbourne_data.Price.
# Esto es equivalente a usar .map() con una función lambda, pero es más conciso y eficiente.
# .head():
# El método .head() se aplica al resultado de la resta.
# .head() muestra las primeras 5 filas de la Serie resultante.
# En resumen, esta línea toma cada precio en la columna 'Price', le resta el precio promedio y muestra los primeros 5 resultados.

# Precios re-centrados usando resta directa:
# Suburb
# Abbotsford    404315.920545
# Abbotsford    -40684.079455
# Abbotsford    389315.920545
# Abbotsford   -225684.079455
# Abbotsford    524315.920545
# Name: Price, dtype: float64
# Resultado Impreso:
# El resultado impreso muestra los primeros 5 precios re-centrados.
# Cada valor representa la diferencia entre el precio original de una casa y el precio promedio de todas las casas.
# Los valores son los mismos que los obtenidos con .map(), lo que demuestra que la resta directa es una forma equivalente de realizar la misma operación.

# Combinar CouncilArea y Regionname
print("\nCombinación de CouncilArea y Regionname:")
# Esta línea imprime un mensaje en la consola para indicar que el siguiente resultado mostrará la combinación de las columnas CouncilArea y Regionname.
print((melbourne_data.CouncilArea + " - " + melbourne_data.Regionname).head())
# Esta es la parte clave del código. Vamos a analizarla por partes:
# melbourne_data.CouncilArea + " - " + melbourne_data.Regionname:
# Esta expresión realiza una concatenación de cadenas entre las Series melbourne_data.CouncilArea y melbourne_data.Regionname.
# El operador + se utiliza para concatenar cadenas en Pandas, al igual que en Python estándar.
# " - " es una cadena literal que se inserta entre los valores de las dos columnas para separarlos.
# Pandas realiza esta concatenación elemento por elemento, combinando los valores correspondientes de las dos columnas en cada fila.
# .head():
# El método .head() se aplica al resultado de la concatenación.
# .head() muestra las primeras 5 filas de la Serie resultante.
# En resumen, esta línea combina los valores de las columnas CouncilArea y Regionname en una nueva Serie, separando los valores con " - ", y muestra los primeros 5 resultados.
# Combinación de CouncilArea y Regionname:
# Suburb
# Abbotsford    Yarra - Northern Metropolitan
# Abbotsford    Yarra - Northern Metropolitan
# Abbotsford    Yarra - Northern Metropolitan
# Abbotsford    Yarra - Northern Metropolitan
# Abbotsford    Yarra - Northern Metropolitan
# dtype: object
# Resultado Impreso:

# El resultado impreso muestra los primeros 5 valores de la Serie resultante.
# Cada valor es una cadena que combina el nombre del consejo municipal (CouncilArea) y el nombre de la región (Regionname), separados por " - ".
# Esto es útil para crear una nueva columna que combine información de dos columnas existentes.
# Propósito:

# El propósito de este código es combinar información de dos columnas categóricas en una sola columna.
# Esto puede ser útil para crear una representación más concisa de los datos o para facilitar el análisis.
# Por ejemplo, puedes usar esta nueva columna combinada para agrupar o filtrar datos.
# Pandas maneja automáticamente la concatenación de cadenas elemento por elemento, lo que hace que esta operación sea fácil y eficiente.

