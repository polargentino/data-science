import pandas as pd

melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path, index_col=0)

# Cambiar el índice a la columna 'Address'
melbourne_data_address_index = melbourne_data.set_index("Address")

# Mostrar el DataFrame con el nuevo índice
print("DataFrame con índice 'Address':")
print(melbourne_data_address_index.head())
# DataFrame con índice 'Address':
#                   Rooms Type  ...             Regionname Propertycount
# Address                       ...                                     
# 85 Turner St          2    h  ...  Northern Metropolitan        4019.0
# 25 Bloomburg St       2    h  ...  Northern Metropolitan        4019.0
# 5 Charles St          3    h  ...  Northern Metropolitan        4019.0
# 40 Federation La      3    h  ...  Northern Metropolitan        4019.0
# 55a Park St           4    h  ...  Northern Metropolitan        4019.0

# [5 rows x 19 columns]

#     * He sustituido todas las instancias de `reviews` por `melbourne_data` para reflejar tu DataFrame.
# 2.  **Reemplazo de `title` con `Address`:**
#     * He cambiado el ejemplo de la columna `title` a la columna `Address`, ya que es una columna de texto en tu conjunto de datos y puede ser usada como indice.
# 
# **Explicación Adicional:**

# * **`set_index()`:**
#     * Este método permite cambiar el índice del DataFrame a una columna existente.
#     * Es útil cuando una columna contiene valores únicos que pueden servir como identificadores para las filas.
#     * Al usar `set_index()`, la columna especificada se convierte en el índice, y se elimina como columna regular.
# * **Manipulación del Índice:**
#     * El índice no es inmutable, lo que significa que puedes modificarlo según tus necesidades.
#     * Manipular el índice puede mejorar la eficiencia y la legibilidad de tu código, especialmente cuando trabajas con `loc`.
# * **Ejemplo con `melbourne_data.set_index("Address")`:**
#     * Este código cambiará el índice del DataFrame `melbourne_data` a los valores de la columna "Address".
