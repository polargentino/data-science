# Importación de librerías necesarias para el análisis y modelado de datos

import pandas as pd
# pandas (pd): Librería esencial para manipulación y análisis de datos en Python.
# - Permite cargar, limpiar y estructurar datos en tablas (DataFrames).
# - Ejemplo: pd.read_csv() lee archivos CSV y dropna() elimina filas con valores nulos.
# - Es como una hoja de cálculo en código, ideal para manejar datos estructurados.

from sklearn.tree import DecisionTreeRegressor
# sklearn.tree.DecisionTreeRegressor: Clase de scikit-learn para crear un modelo de regresión basado en árboles de decisión.
# - Predice valores numéricos (como precios de casas) dividiendo los datos en nodos según reglas.
# - Ventaja: Fácil de usar e interpretar. Desventaja: Puede sobreajustarse si no se controla.
# - Ejemplo: melbourne_model.fit() entrena el modelo con los datos.

from sklearn.metrics import mean_absolute_error
# sklearn.metrics.mean_absolute_error: Función para evaluar la precisión del modelo.
# - Calcula el error absoluto medio (MAE) entre los valores reales (y) y las predicciones.
# - Fórmula: MAE = (1/n) * Σ|valor_real - valor_predicho|. Un MAE bajo indica mejor precisión.
# - Ejemplo: mean_absolute_error(y, predicciones) mide el error promedio en dólares.

from sklearn.model_selection import train_test_split
# sklearn.model_selection.train_test_split: Función para dividir los datos en conjuntos de entrenamiento y validación.
# - Separa X (características) y y (objetivo) en dos partes aleatoriamente.
# - Argumento random_state fija la semilla aleatoria para resultados reproducibles.
# - Ejemplo: train_X, val_X, train_y, val_y = train_test_split(X, y) crea los conjuntos.
# Ruta del archivo CSV
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Filtrar filas con valores nulos en 'Price'
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Definir variable objetivo (y) y características (X)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

# Calcular MAE en datos originales (in-sample)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(X, y)
predicted_home_prices = melbourne_model.predict(X)
mae_in_sample = mean_absolute_error(y, predicted_home_prices)
print(f"Error Absoluto Medio (MAE) en datos originales (in-sample): {mae_in_sample}")

# Dividir los datos en entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Definir y entrenar el modelo con datos de entrenamiento
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

# Obtener predicciones y calcular MAE en datos de validación (out-of-sample)
val_predictions = melbourne_model.predict(val_X)
mae_validation = mean_absolute_error(val_y, val_predictions)
print(f"Error Absoluto Medio (MAE) en datos de validación (out-of-sample): {mae_validation}")
# Error Absoluto Medio (MAE) en datos originales (in-sample): 434.71594577146544
#Error Absoluto Medio (MAE) en datos de validación (out-of-sample): 259446.41575209814
#  Resultados esperados:
# MAE in-sample: Alrededor de 500 dólares (como dice el texto de Kaggle: "about 500 dollars").
# MAE out-of-sample: Más de 250,000 dólares (como dice: "more than 250,000 dollars").
# Estos valores coinciden con el texto de Kaggle y reflejan:

# Un modelo casi perfecto en los datos de entrenamiento (MAE bajo).
# Un modelo con pobre generalización en datos nuevos (MAE alto).                                                                                     