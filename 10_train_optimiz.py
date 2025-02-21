# De Grok3 :
# ¡Genial que ya tengas los resultados alineados con Kaggle! Ahora te proporciono una versión optimizada del código, con comentarios claros y mejoras para reducir el sobreajuste del modelo DecisionTreeRegressor. La optimización incluye limitar la profundidad del árbol y mostrar una comparación clara entre el modelo original y el optimizado. Aquí va:
# Importación de librerías necesarias para el análisis y modelado de datos
import pandas as pd
# - Maneja datos en tablas (DataFrames) para carga, limpieza y estructuración.

from sklearn.tree import DecisionTreeRegressor
# - Modelo de regresión basado en árboles de decisión para predecir valores numéricos.

from sklearn.metrics import mean_absolute_error
# - Calcula el MAE para evaluar la precisión del modelo (error promedio en predicciones).

from sklearn.model_selection import train_test_split
# - Divide los datos en entrenamiento y validación para evaluar generalización.

# Ruta del archivo CSV (ajustada a tu entorno local)
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Filtrar filas con valores nulos en 'Price'
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Definir variable objetivo (y) y características predictorias (X)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

# Dividir datos en entrenamiento y validación (random_state=0 para reproducibilidad)
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# --- Modelo original (sin optimización) ---
melbourne_model_original = DecisionTreeRegressor()
melbourne_model_original.fit(train_X, train_y)

# MAE in-sample (datos de entrenamiento)
train_predictions_original = melbourne_model_original.predict(train_X)
mae_train_original = mean_absolute_error(train_y, train_predictions_original)

# MAE out-of-sample (datos de validación)
val_predictions_original = melbourne_model_original.predict(val_X)
mae_val_original = mean_absolute_error(val_y, val_predictions_original)

# --- Modelo optimizado (limitando profundidad para reducir sobreajuste) ---
melbourne_model_optimized = DecisionTreeRegressor(max_depth=5, random_state=0)
# - max_depth=5: Limita la profundidad del árbol a 5 niveles para evitar sobreajuste.
# - random_state=0: Asegura resultados consistentes.
melbourne_model_optimized.fit(train_X, train_y)

# MAE in-sample (datos de entrenamiento)
train_predictions_optimized = melbourne_model_optimized.predict(train_X)
mae_train_optimized = mean_absolute_error(train_y, train_predictions_optimized)

# MAE out-of-sample (datos de validación)
val_predictions_optimized = melbourne_model_optimized.predict(val_X)
mae_val_optimized = mean_absolute_error(val_y, val_predictions_optimized)

# --- Comparación de resultados ---
print("=== Resultados del modelo original ===")
print(f"MAE en datos de entrenamiento (in-sample): {mae_train_original}")
print(f"MAE en datos de validación (out-of-sample): {mae_val_original}")

print("\n=== Resultados del modelo optimizado (max_depth=5) ===")
print(f"MAE en datos de entrenamiento (in-sample): {mae_train_optimized}")
print(f"MAE en datos de validación (out-of-sample): {mae_val_optimized}")

# --- Análisis adicional ---
print("\n=== Análisis ===")
print(f"Diferencia MAE (in-sample vs out-of-sample) original: {mae_val_original - mae_train_original}")
print(f"Diferencia MAE (in-sample vs out-of-sample) optimizado: {mae_val_optimized - mae_train_optimized}")
# === Resultados del modelo original ===
# MAE en datos de entrenamiento (in-sample): 281.4719173660426
# MAE en datos de validación (out-of-sample): 261990.79793415105

# === Resultados del modelo optimizado (max_depth=5) ===
# MAE en datos de entrenamiento (in-sample): 238027.59409710235
# MAE en datos de validación (out-of-sample): 275902.1465256469

# === Análisis ===
# Diferencia MAE (in-sample vs out-of-sample) original: 261709.326016785
# Diferencia MAE (in-sample vs out-of-sample) optimizado: 37874.55242854456
                                                                           