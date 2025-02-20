# Código para cargar datos (Data Loading Code)
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Ruta del archivo CSV
# Actualización de la ruta del archivo: Ahora apunta a '/home/pol/Downloads/melb_data.csv'
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'

# Cargar los datos en un DataFrame
melbourne_data = pd.read_csv(melbourne_file_path)

# Filtrar filas con valores nulos en la columna 'Price'
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Seleccionar la variable objetivo (y) y las características (X)
# Corrección de y = filtered_melbourne_data.Price → Ahora es y = filtered_melbourne_data['Price'] para evitar advertencias.
y = filtered_melbourne_data['Price']
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

# Definir el modelo de regresión con árbol de decisión
melbourne_model = DecisionTreeRegressor()

# Entrenar el modelo con los datos
melbourne_model.fit(X, y)





from sklearn.metrics import mean_absolute_error
# 📌 Explicación rápida:
# ✔️ melbourne_model.predict(X): Usa el modelo entrenado para predecir los precios de las casas.
# ✔️ mean_absolute_error(y, predicted_home_prices): Compara las predicciones con los valores reales y calcula el error promedio.
# ✔️ Un MAE más bajo significa que el modelo es más preciso.
# Hacer predicciones con el modelo entrenado
predicted_home_prices = melbourne_model.predict(X)

# Calcular el error absoluto medio (MAE)
mae = mean_absolute_error(y, predicted_home_prices)

# Imprimir el resultado
print(f"Error Absoluto Medio (MAE): {mae}")
# Error Absoluto Medio (MAE): 434.71594577146544

print("The predictions are") # Para verificar que que la nueva ruta del .csv funciona, descargando y descomprimiendo el .zip
print(melbourne_model.predict(X.head()))
# The predictions are
# [1035000. 1465000. 1600000. 1876000. 1636000.]

# Comentarios traducidos al español para mayor claridad.
# 🔹 ¿Qué hace este código?
# ✅ Carga los datos del archivo CSV.
# ✅ Filtra los registros con valores faltantes en la columna Price.
# ✅ Define las variables predictoras (X) y la variable objetivo (y).
# ✅ Crea un modelo de regresión de árboles de decisión.
# ✅ Entrena el modelo con los datos.

# 📊 ¿Quieres visualizar alguna predicción o hacer un gráfico con los datos? 🚀
